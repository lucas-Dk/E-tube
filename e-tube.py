# Necessário internet
# Ele não deixa rodar o código se não tiver internet
try:
	import sys
	from pytube import YouTube, Playlist
	from time import sleep as suspender
	import urllib.request
	import os
	import banner
except:
	print("\n\033[1;31m[ERROR]: Parece que você não instalou a biblioteca Pytube\033[m")
	print("\n\033[1;33m[+] Digite esse comando:\033[m pip install -r requirements.txt")
	print("\n\033[1;31mE tente novamente!\033[m")
	sys.exit()
else:
	pass
print()

previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        bytes_archive = int(bytes_remaining)
        print("\033[1;34m[+] Baixando:\033[m [{}]% | [{}] \033[1;34mMib/s\033[m \033[1;32mconcluído\033[m".format(liveprogress,bytes_archive))


os.system("clear")
mensagem_boas_vindas = "Seja bem vindo ao E-tube!"
for letra in mensagem_boas_vindas:
	print("\033[1;36m{}\033[m".format(letra), end='', flush=True)
	suspender(0.1)
suspender(1.1)
os.system("clear")
mensagem_erro_etube = "Olá, aqui é o programador do E-tube! Escrevi esse texto para avisar"
mensagem_erro_etube2 = "que se caso o script der algum erro, é por causa do próprio YouTube."
mensagem_erro_etube3 = "Isso acontece ok!"
for x in mensagem_erro_etube:
	print("\033[1;32m{}\033[m".format(x),flush=True,end="")
	suspender(0.1)
print()
for z in mensagem_erro_etube2:
	print("\033[1;32m{}\033[m".format(z),flush=True,end="")
	suspender(0.1)
print()
for y in mensagem_erro_etube3:
	print("\033[1;32m{}\033[m".format(y),flush=True,end="")
	suspender(0.1)
print()
continuar = input("Se entendeu digite Enter para continuar: ")
os.system("clear")
try:
	print("\033[1;31m[+] Verificando se você está conectado na internet...\033[m")
	suspender(1.4)
	connection = urllib.request.urlopen("https://www.google.com.br")
except:
	print("\n\033[1;31m[ERROR]: Você não está conectado a internet :( \033[m\n")
else:
	os.system("clear")
	while True:
		banner.change_banner()
		print("""

> Coded by: Lucas-DK
> Meu GitHub: https://github.com/lucas-Dk
> Reporte erros: https://www.facebook.com/Walker.Lxrd/

MENU:

\033[1;31m[\033[1;32m 1 \033[m\033[1;31m]\033[m - Baixar um vídeo MP4
\033[1;31m[\033[1;32m 2 \033[m\033[1;31m]\033[m - Baixar uma playlist MP4
\033[1;31m[\033[1;32m 3 \033[m\033[1;31m]\033[m - Baixar uma música MP3
\033[1;31m[\033[1;32m 4 \033[m\033[1;31m]\033[m - Mudar cor do banner
\033[1;31m[\033[1;32m 5 \033[m\033[1;31m]\033[m - Fale comigo
\033[1;31m[\033[1;32m x \033[m\033[1;31m]\033[m - Sair
			""")
		try:
			user = input("\n\033[1;33mO que você deseja:\033[m ")
		except KeyboardInterrupt:
			print("\nSaindo...")
			suspender(1)
			sys.exit() # Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
		if user.isnumeric():
			user = int(user)
			
			if user == 1:
				print()
				print("\033[1;32m[+] Opção 1 > Download de um video.mp4\033[m")
				print("\033[1;32m[+] O vídeo ficará salvo na pasta do script!\033[m")
				print()
				try:
					link = str(input("\033[1;33mUrl do vídeo:\033[m "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				url_video = link
				yt = YouTube(url_video)

				print("\n\033[1;31m[+] Buscando streams diponíveis para download...\033[m\n")

				for streams in yt.streams.filter(file_extension="mp4"):
					print("\033[1;31m[Vídeo]\033[m \033[1;33m{}\033[m".format(streams))
					suspender(0.5)

				print("\n\033[1;32m[+] Iniciando o download...\033[m")
				try:
					suspender(2)
					video = yt.streams.get_highest_resolution()
					yt.register_on_progress_callback(on_progress)
					video.download()
				except VideoUnavailable:
					print("\033[1;31mO vídeo:\033[m [{}] \033[1;31mse encontra indísponivel para download...\033[m ")
				except KeyboardInterrupt:
					print("\033[1;31m[OPS]: Ocorreu alguma interrupção! Fechando o script...\033[m")
					suspender(1)
					sys.exit()
				print("\n\033[1;96m[+] Download completo do vídeo!\033[m")
				print("\033[1;35m[+] Voltando ao menu...\033[m")
				suspender(2)
				os.system("clear")

			elif user == 2:
				print()
				print("\033[1;32m[+] Opção 2 > Download de uma Playlist.mp4\033[m")
				print("\033[1;32m[+] Os vídeos ficarão salvos na pasta 'Playlist YT' do script!\n\033[m")
				print()
				try:
					link_play = str(input("\033[1;33mUrl da playlist:\033[m "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				else:
					PLAYLIST_URL = link_play
					playlist = Playlist(PLAYLIST_URL)
					tamanho_da_playlist = 0
					for videos in playlist:
						tamanho_da_playlist += 1
					print()
					print("\n\033[1;32mSobre a sua playlist:\033[m\n")
					print("\033[1;31m[+] Nome:\033[m {}".format(playlist.title))
					print("\033[1;31m[+] Tamanho da sua playlist:\033[m {} \033[1;31mvídeos!\033[m".format(tamanho_da_playlist))
					print("\033[1;31m[+] link quebrado:\033[m o vídeo é pulado!")
					print("\033[1;31m[+] Local de armazenamento:\033[m pasta Playlist YT")
					print()
					print("\033[1;92m[+] Iniciando o download dos vídeos...\033[m\n")
					suspender(1.1)
					tamanho_da_playlist = 0
					for numero_play, url in enumerate(playlist):
						print("\033[1;33m[+] Baixando o [{}]º video:\033[m {}".format(numero_play+1,url))
						video = YouTube(url)
						stream = video.streams.get_highest_resolution()
						print("\033[1;31mStatus:\033[m \033[1;32m[COMPLETO]\033[m")
						try:
							stream.download(output_path='Playlist YT')
						except VideoUnavailable:
							print("\033[1;31mStatus:\033[m \033[1;33m[PULADO]\033[m")
							print("\n\033[1;91mO video foi pulado porque o o link está quebrado!\033[m")
							time.sleep(2)
						except KeyboardInterrupt:
							print("\n\033[m[ERROR]: Download quebrado porque o usuário saiu!\033[m")
						else:
							pass
					print("\n\033[1;32m[+] Download Completo da playlist! Verifique na pasta: Playlist YT !\n\033[m")
					print("\n\033[1;35m[+] Voltando ao menu...\n\033[m")
					suspender(2)
					os.system("clear")

			elif user == 3:
				print("\n\033[1;32m[+] Opção 3 > Download de uma Musica.mp3\033[m")
				print("\033[1;32m[+] A música ficará salva na pasta do script!\n\033[m")
				print("\n\033[1;31m[OBS]: Essa opção por enquanto não converte o vídeo para .MP3\033[m")
				try:
					link = str(input("\033[1;33mUrl do vídeo:\033[m "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit() # Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				else:
					url_download = link
					yt = YouTube(url_download)
					print("\n\033[1;31m[+] Buscando streams diponíveis para download...\033[m\n")
					for streams in yt.streams.filter(only_audio=True):
						print("\033[1;31m[Música]\033[m \033[1;33m{}\033[m".format(streams))
						suspender(0.5)
					print("\n\033[1;92m[+] Fazendo o download...\033[m")
					try:
						musica = yt.streams.get_highest_resolution()
						yt.register_on_progress_callback(on_progress)
						musica.download()
					except:
						print("\033[1;31m[OPS]: Ocorreu alguma interrupção! Fechando o script...\033[m")
						suspender(1)
						sys.exit()
					else:

						print("\n\033[1;31m[+] Download completo!\033[m\n")
						print("\n\033[1;35m[+] Voltando ao menu...\n\033[m")
						suspender(2)
						os.system("clear")

			elif user == 4:
				os.system("clear")

			elif user == 5:
				os.system("clear")
				print("""
\033[1;33m[+] Para contato:\033[m

---------------------------------------------------------------
\033[1;4mE-mail:\033[m lucas2000bss@gmail.com
\033[1;4mFacebook:\033[m https://www.facebook.com/Walker.Lxrd/
---------------------------------------------------------------

\033[1;92m[+] Fale comigo por uma dessas redes e terá contato comigo\n\033[m
				""")
				try:
					input("Dê enter para voltar ao menu... ")
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				os.system("clear")
			else:
				print("\033[1;31mOpção inválida! Tente novamente.\033[m")
				suspender(0.8)
				os.system("clear")

		elif user == 'X' or user == 'x':
			print("Saindo...")
			suspender(1)
			sys.exit()

		else:
			print("\033[1;31mOpção inválida! Tente novamente.\033[m")
			suspender(0.8)
			os.system("clear")

# Fim do script
