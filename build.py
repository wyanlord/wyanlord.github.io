import codecs
import os
import time

version = str(time.time())

def read_home():
    ctx = '* 首页' + "\n"
    ctx += '  * [笔记说明](/README.md?v=' + version + ')' + "\n"
    return ctx


def read_lang():
    ctx = ''
    path_dirs = os.listdir('./lang')
    for path_dir in path_dirs:
        ctx += '* ' + path_dir.capitalize() + '语言' + "\n"
        lang_dirs = os.listdir('./lang/' + path_dir)
        if 'README.md' in lang_dirs:
            ctx += '  * [' + path_dir.capitalize() + '导读](' + '/lang/' + path_dir + '/README.md?v=' + version + ')' + "\n"
        for lang_dir in lang_dirs:
            if lang_dir != 'README.md':
                ctx += '  * [' + lang_dir[0:-3] + '](' + '/lang/' + path_dir + '/' + lang_dir + '?v=' + version + ')' + "\n"
    return ctx


def read_linux():
    ctx = ''
    ctx += '* Linux系统' + "\n"
    lang_dirs = os.listdir('./linux/')
    if 'README.md' in lang_dirs:
        ctx += '  * [Linux导读](' + '/linux/README.md?v=' + version + ')' + "\n"
    for lang_dir in lang_dirs:
        if lang_dir != 'README.md':
            ctx += '  * [' + lang_dir[0:-3] + '](' + '/linux/' + lang_dir + '?v=' + version + ')' + "\n"
    return ctx


def read_algorithm():
    ctx = ''
    ctx += '* 算法' + "\n"
    lang_dirs = os.listdir('./algorithm/')
    if 'README.md' in lang_dirs:
        ctx += '  * [算法导读](' + '/algorithm/README.md?v=' + version + ')' + "\n"
    for lang_dir in lang_dirs:
        if lang_dir != 'README.md':
            ctx += '  * [' + lang_dir[0:-3] + '](' + '/algorithm/' + lang_dir + '?v=' + version + ')' + "\n"
    return ctx


def write_sidebar(ctx):
    with codecs.open('_sidebar.md', 'w', 'utf-8') as file_object:
        file_object.write(ctx)


write_sidebar(read_home() + read_lang() + read_linux() + read_algorithm())
