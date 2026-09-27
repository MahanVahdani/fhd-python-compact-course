def converter(text):
    return list(text)

strList = ['mahan', 'vahdani', 'sanavi', 'mdt', 'fhdortmund']

result = map(converter, strList)

print('Converted List:', list(result))