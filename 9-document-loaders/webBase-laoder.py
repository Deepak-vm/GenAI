from langchain_community.document_loaders import WebBaseLoader



url = 'https://www.flipkart.com/audio-video/headset/earphones/wireless-earphones/true-wireless/~cs-6ef68bc8d283b86730515a8f2c87ff23/pr?sid=0pm%2Cfcn%2C821%2Ca7x%2C2si&marketplace=FLIPKART&restrictLocale=true'
loader = WebBaseLoader(url)

docs = loader.load()
document = docs[0].page_content

print(document)