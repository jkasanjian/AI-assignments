import distance
import speech_recognition as sr
import pathlib as p
import os
import matplotlib.pyplot as plt

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
		#print(pathlist)
		for path in pathlist:
			harvard = sr.AudioFile(path)
			with harvard as source:
				audio = r.record(source)
				self.recognized.append(r.recognize_google(audio).lower().strip())
				#print(r.recognize_google(audio).lower().strip())
			
	def comp_string(self):
		for i in range(len(self.original)):
			# print(self.original[i])
			# print(self.recognized[i])
			self.similarity.append(distance.levenshtein(self.original[i],self.recognized[i]))
		print("Total amount of Errors:",sum(self.similarity))
		return self.similarity

if __name__ == '__main__':
  s = Speech()
  s2 = Speech()
  s3 = Speech()
  #Insert path to get to original.txt 
  s.read_original("original.txt")
  s2.read_original("original.txt")
  s3.read_original("original.txt")
  #Insert Directory path where .wav files are located
  s.conv_audio("Speech")
  s2.conv_audio("EF")
  s3.conv_audio("CM")

  #s.comp_string()
  #s2.comp_string()
  #s3.comp_string()

  data = [s.comp_string(), s2.comp_string()]
  fig1, ax1 = plt.subplots()
  ax1.set_title('Male vs. Female')
  ax1.set_xticklabels(['Male','Female'], rotation ='horizontal')
  ax1.boxplot(data)

  plt.show()

  data = [s.comp_string(), s3.comp_string()]
  fig2, ax2 = plt.subplots()
  ax2.set_title('English vs. Chinese')
  ax2.set_xticklabels(['English','Chinese'], rotation='horizontal')
  ax2.boxplot(data)

  plt.show()
