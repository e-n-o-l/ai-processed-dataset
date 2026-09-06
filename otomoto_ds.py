from torch.utils.data import IterableDataset
from otomoto_scrapper import scrape_otomoto_offer, get_offer_urls_from_page


class OtomotoIterableDataset(IterableDataset):
    def __init__(self, start_page: int = 1, max_pages: int = 50):
        super().__init__()
        self.start_page = start_page
        self.max_pages = max_pages

    def __iter__(self):
        for page in range(self.start_page, self.start_page + self.max_pages):
            urls = get_offer_urls_from_page(page)
            for url in urls:
                result = scrape_otomoto_offer(url)
                if result is None:
                    continue

                images, html, offer_url = result
                if images and html:
                    yield images, html, offer_url