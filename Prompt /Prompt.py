import openai

openai_api_key = "....." # kendi OpenAI Anahtarını buraya giriniz # burayı kulanmasanız çalışmaz
openai.api_key = openai_api_key

def generate_script(topic, platform, purpose): # giriş bilgilerine göre video senaryosunu oluşturacak.
    prompt = f"Create a video script for a video about {topic}." \
             f"Imagine a visual where {topic} is portrayed."\
             f"The video will be published on {platform} with the purpose of being {purpose}." \
             f"use the script in the {purpose} style" \
             f"Create a scenario according to the {platform} user"\
             f"The {topic} , which will be presented with emotional tone and interaction styles, should show different emotional states and targeted audience interactions."\
             f"let the sadness of the script be long according to the {platform} to be published"


    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt, # prompt bilgilerine dayanarak metin oluşturacak
        max_tokens=2000, # metinin üzünlüğü belirliyoruz
        stop=None,
        temperature=0.8 # oluşturulan metinin yaratıcılık düzeyini belirliyor
    )
    script = response.choices[0].text.strip()
    return script

def get_user_input(prompt): # girdi fonksiyonu tanımlıyoruz
    user_input = input(prompt)
    return user_input

def main():
    topics = get_user_input("Videonun konusunu girin: ")
    platforms = get_user_input("Videonun yayınlanacağı platforma girin (ör. Tik tok, YouTube, tv, instagram,Linkedın): ")
    purposes = get_user_input("Videonun amacını girin (ör. informative, creative, funny, professional,casual): ")

    script = generate_script(topics, platforms, purposes)

    print("\n Oluşturulan senaryo:")
    print(script)

if __name__ == "__main__":
    main()
