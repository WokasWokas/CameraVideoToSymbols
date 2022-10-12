class FontSize:
    def __init__(self, size: int) -> None:
        self.size = size
    
    def set_size(self, size: int) -> None:
        self.size = size
    
    def up_size(self) -> None:
        self.size += 1
    
    def down_size(self) -> None:
        self.size -= 1