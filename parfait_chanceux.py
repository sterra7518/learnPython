
# imports
from parfait_chanceux_m import estParfait, estChanceux


# programme principal -----------------------------------------------
parfaits, chanceux = [], []
intervalle = range(2, 1001)

for i in intervalle:
	if estParfait(i):
		parfaits.append(i)
	if estChanceux(i):
		chanceux.append(i)


msg = " Nombres remarquables dans [2 .. 1000] ".center(70, '-')

msg += "\n\nParfaits :\t{}\n\nChanceux :\t{}".format(parfaits, chanceux)

print(msg)
