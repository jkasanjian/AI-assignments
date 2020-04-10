import distance
import speech_recognition as sr
import pathlib as p
import os

class Speech:

	def __init__(self):
		self.original = []
		self.recognized = []
		self.similarity = []

	def read_original(self, inFile):
		f = open(inFile,'r')
		words = f.read().lower().strip().split("\n")
		self.original = words	

	def conv_audio(self, inDir):
		r = sr.Recognizer()
		pathlist = list()
		for path in os.listdir(inDir):
			if path != ".DS_Store":
				full_path = os.path.join(inDir,path)
				pathlist.append(full_path)
		
		pathlist.sort()
		for path in pathlist:
			harvard = sr.AudioFile(path)
			with harvard as source:
				audio = r.record(source)
				self.recognized.append(r.recognize_google(audio).lower().strip())
			
	def comp_string(self):
		for i in range(len(self.original)):
			# print(self.original[i])
			# print(self.recognized[i])
			self.similarity.append(distance.levenshtein(self.original[i],self.recognized[i]))
		print("Total amount of Errors:",sum(self.similarity))

if __name__ == '__main__':
  s = Speech()
  #Insert path to get to original.txt 
  s.read_original("/original.txt")
  #Insert Directory path where .wav files are located
  s.conv_audio("")
  s.comp_string()
