
# from utils.crypto_utils import load_private_key, sign_response

# private_key = load_private_key()

def custom_response(status, status_code, message, data=None):
    # signature = sign_response(private_key, data)
    response = {
        "status": status,
        "status_code": status_code,
        "message": message,
        "data": data,
        # "signature": signature
    }

    return response
