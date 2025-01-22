import wikipedia


def get_wiki(page_name):
    wikipedia.set_lang('ru')
    result = wikipedia.page(page_name)
    return result.summary


if __name__ == '__main__':
    print(get_wiki("Python"))
