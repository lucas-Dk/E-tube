import moviepy.editor as mp
import os
import sys
from time import sleep as suspender

os.makedirs("SUAS_MÚSICAS",exist_ok=True)

def converter_video_para_mp3(fun="vazio"):
        if fun == "cheio":
                try:
                        print("\033[1;36m[+] Exemplo de caminho a ser colocado abaixo:\033[m \\Users\\Cliente\\Downloads\\E-tube")
                        caminho = input("\033[1;32m[+] Caminho:\033[m ")
                except KeyboardInterrupt:
                        print("\n\033[1;31mSaindo...\033[m")
                        suspender(1)
                        sys.exit()
                except FileNotFoundError:
                        print("\033[1;31m[!] Desculpe, não foi possível localizar esse caminho...")
                        print("Verifique se o caminho está correto!\033[m")
                        sys.exit()
                else:
                        if sys.platform == "win32":
                                if r"\playlist" not in caminho:
                                        caminho2 = caminho + r"\playlist\\"
                                        print("\n\033[1;33m[*] CONVERSÃO INICIADA!\n\033[m")
                                        for item in os.listdir(str(caminho2)):
                                                if item.endswith("mp4"):
                                                        seuvideo = item
                                                        download = caminho2 + seuvideo
                                                        fileouts = item.replace(".mp4",".mp3")
                                                        baixando = mp.VideoFileClip(download)
                                                        if baixando:
                                                                try:
                                                                        os.chdir("SUAS_MÚSICAS")
                                                                        os.path.join("SUAS_MÚSICAS" + "/" + str(baixando.audio.write_audiofile(fileouts)))
                                                                except:
                                                                        os.path.join("SUAS_MÚSICAS" + "/" + str(baixando.audio.write_audiofile(fileouts)))
                                        print("\033[1;32m[*] CONVERSÃO FINALIZADA COM SUCESSO! VOLTANDO AO MENU...\033[m")
                                        suspender(1)
                                        os.system("clear")
                                else:
                                        while "\playlist\\" not in caminho:
                                                print("\033[1;31m[ATENÇÃO] Está faltando uma \\ contra barra no final de playlist!\033[m")
                                                caminho = input("\033[1;32m[+] Caminho:\033[m ")
                                        
                                        if "\playlist\\" in caminho:
                                                for item2 in os.listdir(str(caminho)):
                                                        if item2.endswith("mp4"):
                                                                seuvideo2 = item2
                                                                download2 = caminho + seuvideo2
                                                                fileouts2 = item2.replace(".mp4",".mp3")
                                                                baixando2 = mp.VideoFileClip(download2)
                                                                if baixando2:
                                                                        try:
                                                                                os.chdir("SUAS_MÚSICAS")
                                                                                os.path.join("SUAS_MÚSICAS" + "/" + str(baixando2.audio.write_audiofile(fileouts2)))
                                                                        except:
                                                                                os.path.join("SUAS_MÚSICAS" + "/" + str(baixando2.audio.write_audiofile(fileouts2)))
                                                print("\033[1;32m[*] CONVERSÃO FINALIZADA COM SUCESSO! VOLTANDO AO MENU...")
                                                suspender(1)
                                                os.system("clear")
                        elif sys.platform == "linux":
                                if "/playlist" not in caminho:
                                        caminho2 = caminho + "/playlist/"
                                        print("\033[1;33m[+] CONVERSÃO INICIADA!\n\033[m")
                                        for videos in os.listdir(str(caminho)):
                                                if videos.endswith("mp4"):
                                                        seuvideo = videos
                                                        download_ = caminho2 + seuvideo
                                                        saida_musica = seuvideo.replace(".mp4",".mp3")
                                                        baixando_ = mp.VideoFileClip(download)
                                                        if baixando_:
                                                                try:
                                                                        os.chdir("SUAS_MÚSICAS")
                                                                        os.path.join("SUAS_MÚSICAS" + "/" + str(baixando_.audio.write_audiofile(saida_musica)))
                                                                except:
                                                                        os.path.join("SUAS_MÚSICAS" + "/" + str(baixando_.audio.write_audiofile(saida_musica)))
                                        print("\033[1;32m[*] CONVERSÃO INICIADA COM SUCESSO! VOLTANDO AO MENU...\033[m")
                                        suspender(1)
                                        os.system("clear")
                                else:
                                        while "/playlist/" not in caminho:
                                                print("\033[1;31m[ATENÇÃO] Está faltando uma barra / no final de playlist!\033[m")
                                                caminho = input("\033[1;32m[+] Caminho:\033[m ")
                                        if "/playlist/" in caminho:
                                                for video in os.listdir(str(caminho)):
                                                        seuvideo_ = video
                                                        downloads_ = caminho + seuvideo_
                                                        saida_musica_ = seuvideo.replace(".mp4",".mp3")
                                                        baixando_musica = mp.VideoFileClip(downloads_)
                                                        if baixando_musica:
                                                                try:
                                                                        os.chdir("SUAS_MÚSICAS")
                                                                        os.path.join("SUAS_MÚSICAS" + "/" + str(baixando_musica.audio.write_audiofile(saida_musica_)))
                                                                except:
                                                                        os.path.join("SUAS_MÚSICAS" + "/" + str(baixando_musica.audio.write_audiofile(saida_musica_)))
                                                print("\033[1;32m[*] CONVERSÃO FINALIZADA COM SUCESSO! VOLTANDO AO MENU...\033[m")
                                                suspender(1)
                                                os.system("clear")



                        
        elif fun == "vazio":
                os.system("clear")
                print("\033[1;94m=========================== CONVERTER PARA MP3 ===========================\033[m")
                print("\n\033[1;33m[SAIBA UTILIZAR ESSA FUNÇÃO. LEIA ABAIXO PARA NÃO TER ERROS!]\033[m\n")
                print("\033[1;32m[!] Para converter o video para mp3 siga as instruções.\033[m")
                print("\033[1;32m[!] Pegue o caminho onde se encontra o vídeo. Exemplos:\033[m")
                print("\n----------------\n")
                print("\033[1;33m[!] EXEMPLO PARA USUÁRIOS DO TERMUX!\033[m\n")
                print("\033[1;33m[+]\033[m Caminho: /storage/downloads/E-tube/VideosConvertidos  (\033[1;31mONDE SE ENCONTRA O VÍDEO A SER CONVERTIDO\033[m)")
                print("\033[1;33m[+]\033[m Nome do arquivo Exemplo: /Whatever It Takes.mp4 [\033[1;31mO .mp4 NÃO PODE FALTAR!\033[m]")
                print("\033[1;33m[+]\033[m No nome do arquivo vocês sempre colocam uma / antes \033[1;31m( SEM ESPAÇO APÓS A / para usuários do Termux)\033[m")
                print("\n----------------\n")
                print("\033[1;33m[!] EXEMPLO PARA USUÁRIOS DO PC/LINUX!\033[m\n")
                print("\033[1;33m[+]\033[m Caminho: \\Users\Cliente\Downloads\E-tube\VideosConvertidos  (\033[1;31mONDE SE ENCONTRA O VÍDEO A SER CONVERTIDO\033[m)")
                print("\033[1;33m[+]\033[m Nome do arquivo Exemplo: \\Whatever It Takes.mp4 [\033[1;31mO .mp4 NÃO PODE FALTAR!\033[m]")
                print("\033[1;33m[+]\033[m \033[1;31m[IMPORTANTE] O CAMINHO acima é um exemplo, na opção que pedir, cole o caminho certo!\033[m")
                print("\033[1;33m[+]\033[m No nome do arquivo vocês sempre colocam uma \ antes \033[1;31m( SEM ESPAÇO APÓS A \ para usuários do PC)\033[m\n")
                print("----------------\n")
                try:
                        input("\033[1;33m[!] Enter para começar a conversão:\033[m ")
                except KeyboardInterrupt:
                        print("\n\033[1;31mSaindo...\033[m")
                        suspender(1)
                        sys.exit()
                else:
                        print()
                        print()
                        try:
                                caminho = input("\033[1;33m[*] Digite o caminho:\033[m ")
                                nome_entrada = input("\033[1;33m[*] Nome do mp4 baixado:\033[m ")
                                nome2 = caminho + nome_entrada
                                nome = input("\033[1;33m[*] Nome de saída em mp3:\033[m ")
                        except KeyboardInterrupt:
                                print("\n\033[1;31mSaindo...\033[m")
                                suspender(1)
                                sys.exit() # Essa linha está aqui para evitar algum bug inesperado!
                        else:
                                print("\n\033[1;32m[!] Convertendo para mp3...\n\033[m")
                                meuclipe = mp.VideoFileClip(nome2)
                                meuclipe.audio.write_audiofile(nome)
                                print("\n\033[1;32m[!] Conversão completa! Veja abaixo o nome do seu MP3:\033[m")
                                print("\033[1;33m[+] Nome MP3:\033[m {}\n".format(nome))
                                try:
                                        input("\033[1;31m[!] Aperte ENTER para voltar ao menu:\033[m ")
                                except KeyboardInterrupt:
                                        print("\n\033[1;31mSaindo...\033[m")
                                        suspender(1)
                                        sys.exit()
                                else:
                                        pass

#
