import requests


def fetch_page():
        url = "https://www.skyscanner.com.br/transporte/passagens-aereas/joi/poa/250307/250310/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
        response = requests.get(url)
        return response.text

if __name__ == "__main__":
    page_content = fetch_page()
    print(page_content)

    