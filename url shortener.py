import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, long_url):
        # Generate MD5 hash of the long URL
        hash_object = hashlib.md5(long_url.encode())
        hash_hex = hash_object.hexdigest()
        # Take the first 8 characters of the hash as the short URL
        short_url = hash_hex[:8]
        # Store the mapping of short URL to long URL
        self.url_map[short_url] = long_url
        return short_url

    def expand_url(self, short_url):
        if short_url in self.url_map:
            return self.url_map[short_url]
        else:
            return "Short URL not found"

# Example usage:
shortener = URLShortener()
long_url = input("Enter the long_url:")
short_url = shortener.shorten_url(long_url)
print("Shortened URL:", short_url)
print("Expanded URL:", shortener.expand_url(short_url))

