class Solution:
    delimiter = "Σ"

    def encode(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return "Δ"
        encoded_symbols = "Σ".join(strs)
        return encoded_symbols


    def decode(self, s: str) -> list[str]:
        if s == "Δ":
            return []
        result = s.split(self.delimiter)
        return result