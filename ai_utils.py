def fake_large_model_stream(text):
    """
    模拟流式返回：将句子分词逐块返回（真实情况应接入支持流式的模型如 OpenAI Stream API）
    """
    # 模拟切分的响应内容
    for word in text.split():
        yield word + " "

def generate_translation_stream(text):
    
    for chunk in fake_large_model_stream(text):
        yield chunk

def generate(text):
    for chunk in generate_translation_stream(text):
        yield f"data: {chunk}\n\n"
