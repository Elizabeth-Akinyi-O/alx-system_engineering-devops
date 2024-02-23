#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - infinite loop that runs forever
 *
 * Return: 0 (nothing)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main entry point that creates 5 zombie processes
 * Description: For every zombie process created, it displays
 * Zombie process created, PID: ZOMBIE_PID
 *
 * Return: 0 (success)
 */
int main(void)
{
	int childProc = 0; /* child process */
	pid_t pid;

	while (childProc < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		childProc++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}

