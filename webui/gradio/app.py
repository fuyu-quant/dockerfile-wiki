import random
import gradio as gr

def get_foturne(your_name):
    fortune_lists = ['大吉', '吉', '小吉', '凶', '末吉']
    fortune_result = random.choice(fortune_lists)
    return your_name + "さんの今日の運勢は・・・" + fortune_result + "です"


demo = gr.Interface(fn=get_foturne,
                    inputs="text",
                    outputs="text")

# share=Trueにすることで発行されるURLにより他者にも共有できる
demo.launch(server_name = "0.0.0.0", server_port=8070, share=True)


# docker run -p 8070:8070 --name gradio -d fuyuquant/gradio