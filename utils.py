class Constants:
    WIDTH = 1920
    HEIGHT = 1080
    LARGEUR_DIF = 15 #Check issue
    GRADIENTS = ['.', '-', '/', 'r', 'L', 'o', '*', "'", '_', '|', 'c', 'C', 'a', '&', '`', '+', '(', 'v', 'J', 'h', '%', ',', '<', ')', 'u', 'U', 'k', '$', '^', 'i', '1', 'n', 'Y', 'b', '#', ':', '?', ']', 'x', 'X', 'd', '@']


class Images:
    def dimensions(self,filename:str,extension:str):
        from PIL import Image
        img = Image.open(f'img/{filename}.{extension}')
        return img.size