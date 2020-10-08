import base64
import imghdr

def get_file_type(base_64):
    try:
        sample = base64.b64decode(base_64)  # 33 bytes / 3 times 4 is 44 base64 chars
        for tf in imghdr.tests:
            res = tf(sample, None)
            if res:
                break
        return res
    except Exception:
        return False
