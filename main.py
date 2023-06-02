from main import settings


def main():
	for command in settings.STARTING_CMDS:
		exec(command)
		print("")


if __name__ == '__main__':
	main()
