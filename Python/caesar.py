def caesar(text: str, shift: int) -> str:
    """
    Encrypt a text using the Caesar cipher.
    Everything that is not a lowercase letter will be removee.

    Parameters
    ----------
        text : str
            The text to encrypt.
        shift : int
            The encryption key.
    Returns
    -------
        encrypted : str
            The encrypted text.
    """
    encrypted = ''
    for i in range(len(text)):
        if ord(text[i]) >= ord('a') and ord(text[i]) <= ord('z'):
            new_chr = ord(text[i])+shift
            while new_chr > ord('z'):
                new_chr -= 26
            while new_chr < ord('a'):
                new_chr += 26
            encrypted += chr(new_chr)
    return encrypted
