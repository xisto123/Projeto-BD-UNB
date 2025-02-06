# /Service/Helper/window_size.py

def set_window_size(window, width_percent=0.8, height_percent=0.7):
    """
    Define o tamanho da janela baseado na porcentagem da tela e centraliza.

    :param window: Instância da janela Tkinter.
    :param width_percent: Porcentagem da largura da tela (padrão 80%).
    :param height_percent: Porcentagem da altura da tela (padrão 70%).
    """
    # Obtém as dimensões da tela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula o tamanho da janela
    window_width = int(screen_width * width_percent)
    window_height = int(screen_height * height_percent)

    # Centraliza a janela
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2

    # Define tamanho e posição da janela
    window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
