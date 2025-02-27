import os
import requests
from urllib.parse import urlparse, parse_qs

def get_file_id_from_url(url):
    """Extract file ID from Google Drive URL."""
    parsed = urlparse(url)
    if parsed.path.startswith('/file/d/'):
        return parsed.path.split('/')[3]
    return parse_qs(parsed.query).get('id', [None])[0]

def download_file_from_drive(file_id, destination):
    """Download a file from Google Drive."""
    URL = "https://drive.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)

    # Check if there's a download warning (for large files)
    if 'content-disposition' not in response.headers:
        # Get the confirmation token
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                params = {'id': file_id, 'confirm': value}
                response = session.get(URL, params=params, stream=True)
                break

    if response.status_code == 200:
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=32768):
                if chunk:
                    f.write(chunk)
        return True
    return False

def main():
    # Certifique-se que a pasta static/images existe
    os.makedirs('static/images', exist_ok=True)

    # URLs dos mapas do Google Drive
    map_urls = [
        "https://drive.google.com/file/d/1gMwWzxC9kKANOv3GY7wz8N5GWHwCTUUx/view?usp=drive_link",  # mapa1.png
        "https://drive.google.com/file/d/1WUPr_uAVLrMJ8UZKv-MBJ4LMXDQQwWGo/view?usp=drive_link",  # mapa2.png
        "https://drive.google.com/file/d/1wDSXzW0Xr0qGBjB1OBK27J7ZwUL_PfAE/view?usp=drive_link",  # mapa3.png
        "https://drive.google.com/file/d/1_IKGsqgbVNlmLcJfENKk-2P_D8fJjxB5/view?usp=drive_link",  # mapa4.png
        "https://drive.google.com/file/d/1LPiT6-mOWZkWXHyJf1lKtFv2xUwPDGUB/view?usp=drive_link",  # mapa5.png
        "https://drive.google.com/file/d/1WUmBpvHvRm8pIVT_O7OADpb49AQMPYgZ/view?usp=drive_link",  # mapa6.png
        "https://drive.google.com/file/d/1eE48fApGTlzAF4HKlcMxlQV1Ef61MXwK/view?usp=drive_link",  # mapa7.png
        "https://drive.google.com/file/d/1FiX2UDHmz4kSHPrw_Yvg2oOCL-9OCpCf/view?usp=drive_link",  # mapa8.png
        "https://drive.google.com/file/d/1p0hVAYgZ-h0dHKkr1D_jfEKBfTZ83qUq/view?usp=drive_link",  # mapa9.png
        "https://drive.google.com/file/d/1kABIIKxLDPBgJsUlI-YlqFE-33vEIQZ0/view?usp=drive_link",  # mapa10.png
        "https://drive.google.com/file/d/1sOz0cCpYeOTEJy_EUH1w4xMbgn2AKBPY/view?usp=drive_link",  # mapa11.png
        "https://drive.google.com/file/d/1Wm9QBOgZmQbZqc5RZgBE-_o1OZGivvV7/view?usp=drive_link",  # mapa12.png
        "https://drive.google.com/file/d/1bVSOPe3RVNuGEqbp4MnNoPXjixjTh7Lm/view?usp=drive_link",  # mapa13.png
        "https://drive.google.com/file/d/1mP7PF_YtIgOL8xX0VYmOB1PKAWz-hbC4/view?usp=drive_link",  # mapa14.png
        "https://drive.google.com/file/d/11DFLZGYcjEFTbTU_HVFG5hTCJPHYRVcH/view?usp=drive_link",  # mapa15.png
        "https://drive.google.com/file/d/1SV5BAHOjTx7p4Z8qz9fCBHF0r-WtCh7E/view?usp=drive_link",  # mapa16.png
        "https://drive.google.com/file/d/1Oo6k0p0JmZJbHJLnBWbDBcIQpw3ZCnmJ/view?usp=drive_link",  # mapa17.png
        "https://drive.google.com/file/d/1wR5GHKdAMpxqADQp5qPyxE3f2GInSYVJ/view?usp=drive_link",  # mapa18.png
        "https://drive.google.com/file/d/1XMh_2VXBzHMJSoN6-mo2LFBu-3TQ4wIW/view?usp=drive_link",  # mapa19.png
    ]

    # Baixar cada mapa
    for i, url in enumerate(map_urls, 1):
        file_id = get_file_id_from_url(url)
        if file_id:
            destination = f'static/images/mapa{i}.png'
            if download_file_from_drive(file_id, destination):
                print(f'Downloaded mapa{i}.png successfully')
            else:
                print(f'Failed to download mapa{i}.png')

if __name__ == '__main__':
    main()