import argparse, os
from os import walk

parser = argparse.ArgumentParser("JLSGenerator")
parser.add_argument("input", nargs='?', default=os.getcwd()+"/input/", help="Your input folder where audio samples and timing file are located.", type=str)
parser.add_argument("output", nargs='?', default=os.getcwd()+"/output/", help="Your output folder where JLSpeech formatted slices and metadata will be located.", type=str)
parser.add_argument("-c", nargs='?', default=0, help="[NotYetImplemented] - Create a tar.gz archive", type=bool)
parser.add_argument("-d", nargs='?', default=0, help="Convert wav file to mono when stereo detected", type=bool)
parser.add_argument("-r", nargs='?', default=48000, help="[NotYetImplemented] - Convert wav sample rate to your will", type=int)
args = parser.parse_args()

print("[ {} configuration ]".format(parser.prog))
print("Input directory path           : {}".format(args.input))
print("Output directory path          : {}".format(args.output))
print("Compress dataset               : {}".format(bool(args.c)))
print("Convert audio samples          : {}".format(bool(args.d)))

# Look for input folder content:
wav_dir = "{}/wav/".format(args.input)
srt_dir = "{}/srt/".format(args.input)
samples = []
subtitles = []
metadata = "metadata.csv"
metadata_path = "{}{}".format(args.output,metadata)

for (dirpath, dirnames, filenames) in walk(wav_dir):
    samples.extend(filenames)
    break

for (dirpath, dirnames, filenames) in walk(srt_dir):
    subtitles.extend(filenames)
    break

print("Audio directory content        : {}".format(samples))
print("Subtitles directory content    : {}\n".format(subtitles))

not_found = []
for sample in samples:
  subtitle = str(".".join([os.path.splitext(sample)[0], "srt"]))
  if not subtitle in subtitles:
    not_found.append(subtitle)

if len(subtitles) != len(samples) or len(samples) == 0 :
  print("Audio files to process         : {}".format(len(samples)))
  print("Subtitle files to process      : {}".format(len(subtitles)))
  print("Not found subtitles            : {}\n".format(len(not_found)))
  print("Too many missing files to process, exiting, Bye bye!")
  exit(1)

# Splitting audio samples onto segment using timing file:
import srt
for idx, sample in enumerate(samples, start=1):
  sample_path = wav_dir+sample
  sub_name = str(".".join([os.path.splitext(sample)[0], "srt"]))
  sub_path = srt_dir + sub_name

  print("[ INFO ]  - Starting to process {} with {}".format(sample,sub_name))
  with open(sub_path, 'r', encoding='UTF-8') as translate:
    from pydub import AudioSegment
    data = translate.read()
    generator = srt.parse(data)
    subtitles = list(generator)
    for subtitle in subtitles:
      chunck_name="{}{:04d}-{:04d}".format(os.path.splitext(sample)[0],idx,subtitle.index)

      t0=int(subtitle.start.total_seconds() * 1000)
      t1=int(subtitle.end.total_seconds() * 1000)
      audio = AudioSegment.from_wav(sample_path)

      if bool(args.d) :
        mono = audio.set_channels(1)
        segment = mono[t0:t1]
        print("          - Creating mono chunck {}".format(args.output + "wavs/" + chunck_name))
      else:
        segment = audio[t0:t1]
        print("          - Creating stereo chunck {}".format(args.output + "wavs/" + chunck_name))

      segment.export(args.output + "/wavs/" + chunck_name + ".wav", format="wav")
      with open(metadata_path, 'a', encoding='UTF-8') as m:
        m.write("{}|{}|{}\n".format(chunck_name,subtitle.content,subtitle.content))
  print("[ INFO ]  - {} processed and exported to {}".format(sample,args.output))
  print("[ INFO ]  - Metadata.csv updated with {}\n".format(sample))
