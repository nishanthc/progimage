import base64
import imghdr
import io

import requests


def get_file_type(base_64):
    try:
        sample = base64.b64decode(base_64)  # 33 bytes / 3 times 4 is 44 base64 chars
        for tf in imghdr.tests:
            res = tf(sample, None)
            if res:
                break
        if res == "png" or res == "jpeg":
            return res
        else:
            return False
    except Exception:
        return False


def valid_remote_image(remote_url):
    data = requests.get(remote_url).content
    img = io.BytesIO(data)
    base_64 = base64.b64encode(img.getvalue()).decode()
    file_type = get_file_type(base_64)
    if file_type:
        return True, file_type, base_64
    else:
        return False
