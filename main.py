import google.generativeai as genai

genai.configure(api_key="AIzaSyDFznK7OFFa9zOZAvEw7gxliFWZddGpjk4")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

bem_vindo = "# Bem Vindo a Assistente PUPPY#"
print(len(bem_vindo) * "#")
print(bem_vindo)
print(len(bem_vindo) * "#")
print("###   Digite 'sair' para encerrar    ###")
print("")

while True:
    texto = input("Escreva sua mensagem: ")

    if texto == "sair":
        break

    response = chat.send_message(texto)
    print("PUPPY_ASSISTENTE:", response.text, "\n")

print("Encerrando Chat")