from Classifier import WebClassifier
import WebScrapper
import DataLoader

# init data loader
loader = DataLoader.DataLoader(verbose=True)

# try to load previous repository
loader.loadRepoFromJSON('repo.json')

# load links and categories from Excel
loader.loadClassesAndCategoriesFromExcel(r'Categories.xlsx')

# if site was not present in loader's WordRepository object, pull it here
loader.scrapMissingSites()

# get data for classifier
pages, classes, images = loader.getPagesClassesAndImagesCount()

# save repo for the next time
loader.saveToJSON('repo.json')

#---------
#imagePretender = [int(randint(50,500)) for x in range(len(classes))] #WHAT IF I SAY THAT I NEVER SURRENDER
#---------

clf = WebClassifier()
clf.loadData(pages, classes, list(images.values()))
clf.saveToDataToFile('wyniki.txt')

site = 'https://likegeeks.com/python-gui-examples-tkinter-tutorial/'
print('predicting category for ',site,'...')
data = WebScrapper.Scrapper().scrapPage(site)
clf.predict(data[0], data[1], addToData=True) #<---- ta 20, to nic innego, jak ilosc zdjec na tej strinie

clf.saveToDataToFile('wyniki2.txt')
print(classes)