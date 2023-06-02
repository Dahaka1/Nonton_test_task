from main import settings


def main():
	for command in settings.STARTING_CMDS:
		exec(command)
		print(settings.STARTING_MSG)


if __name__ == '__main__':
	main()
