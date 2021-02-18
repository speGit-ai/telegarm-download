from telethon import TelegramClient, sync
#from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo
#import aiohttp_socks
#import os

proxy = None

# =============需要被替换的值=================
'''
api_id 你的api id
api_hash 你的api hash
channel_link 要下载图片的频道链接
proxy 将localhost改成代理地址,12345改成代理端口
picture_storage_path 图片下载到的路径
'''
# api_id = 809268
# api_hash = "4777715f01d208f7e4dfed2f44c3c702"
# link = 'DianCang'
# channel_link = "https://t.me/" + link
# proxy = ("socks5", "127.0.0.1", 10808) #不需要代理的话删掉该行
# storage_path = "D:\\Program Files\\bdtmp\\" + link
# # ==========================================
# client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, proxy=proxy).start()


def video(start, link, storage_path, client):
    channel_link = "https://t.me/" + link
    videos = client.get_messages(channel_link, None, filter=InputMessagesFilterVideo)
    #InputMessagesFilterPhotoVideo
    #InputMessagesFilterMusic
    #InputMessagesFilterVideo
    total = len(videos)
    index = start
    for start in range(start, total-1):
        filename = storage_path + "\\" + str(videos[start].id) + ".mp4"
        index = index + 1
        print("downloading:", index, "/", total, " : ", filename)
        client.download_media(videos[start], filename)

    client.disconnect()
    print("viodes Done.")
    #os.system("pause")
