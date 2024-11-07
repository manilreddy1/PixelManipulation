from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image and convert it to RGB mode
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixel_data = np.array(img)

    # Apply pixel manipulation - XOR operation with key
    encrypted_data = pixel_data ^ key  # XOR each pixel with key

    # Create an encrypted image from the modified pixels
    encrypted_img = Image.fromarray(encrypted_data)
    return encrypted_img

def decrypt_image(encrypted_img, key):
    # Convert encrypted image data to numpy array
    encrypted_data = np.array(encrypted_img)
    
    # Reverse the XOR operation using the same key
    decrypted_data = encrypted_data ^ key
    
    # Create a decrypted image from the modified pixels
    decrypted_img = Image.fromarray(decrypted_data)
    return decrypted_img

# Main program
if __name__ == "__main__":
    key = 123  # Simple XOR key for encryption/decryption
    
    # Encrypt the image
    image_path = "image.jpg"
    encrypted_img = encrypt_image(image_path, key)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as encrypted_image.png")
    
    # Decrypt the image
    decrypted_img = decrypt_image(encrypted_img, key)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as decrypted_image.png")
