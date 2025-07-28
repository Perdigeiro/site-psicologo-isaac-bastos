from rembg import remove
from PIL import Image
import io
import base64

def remove_background(image_data):
    # Converte a imagem de entrada (base64) para um objeto PIL
    image_bytes = base64.b64decode(image_data.split(",")[1])
    input_image = Image.open(io.BytesIO(image_bytes))
    
    # Remove o fundo usando rembg
    output_image = remove(input_image)
    
    # Salva a imagem resultante em um buffer
    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")
    
    # Converte a imagem resultante para base64
    result_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{result_base64}"

# Exemplo de uso (para Pyodide, a imagem deve ser fornecida como base64)
# Substitua 'image_base64' pela string base64 da sua imagem
# image_base64 = "data:image/jpeg;base64,..."
# result = remove_background(image_base64)