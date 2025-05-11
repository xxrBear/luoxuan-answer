def call_large_model(prompt):
    # 模拟大模型的调用过程
    return f"[大模型输出] {prompt}"

def translate_zh_to_en(text):
    prompt = f'''
        你是一位经验丰富的中英翻译专家，请将以下中文翻译成自然、地道、符合语境的英文。如果原文是口语化的，请使用地道的美式英语表达：
        【中文原文】：
        {{text}}
        【英文翻译】：
        '''
    return call_large_model(prompt)

def translate_en_to_zh(text):
    prompt = f'''
        你是一位专业的中英翻译专家，请将以下英文翻译成准确、自然、通顺的中文。如果原文包含专业术语或技术内容，请尽量保留原意并使用通用中文术语。
        【英文原文】：
        {{text}}
        【中文翻译】：
    '''
    return call_large_model(prompt)

def summarize_text(text):
    prompt = f"请对以下内容进行简洁总结：{text}"
    return call_large_model(prompt)
