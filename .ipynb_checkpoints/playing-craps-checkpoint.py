{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a406d09b-a593-47ec-8fb0-a5c14b3240aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Face    Frequency\n",
      "   1            0\n",
      "   2       166777\n",
      "   3       333275\n",
      "   4       500748\n",
      "   5       666364\n",
      "   6       833892\n",
      "   7       999890\n",
      "   8       833264\n",
      "   9       664714\n",
      "  10       500499\n",
      "  11       334030\n",
      "  12       166547\n"
     ]
    }
   ],
   "source": [
    "\"\"\"Roll a six-sided die 6,000,000 times.\"\"\"\n",
    "import random\n",
    "\n",
    "# face frequency counters\n",
    "frequency1 = 0\n",
    "frequency2 = 0\n",
    "frequency3 = 0\n",
    "frequency4 = 0\n",
    "frequency5 = 0\n",
    "frequency6 = 0\n",
    "frequency7 = 0\n",
    "frequency8 = 0\n",
    "frequency9 = 0\n",
    "frequency10 = 0\n",
    "frequency11 = 0\n",
    "frequency12 = 0\n",
    "\n",
    "# 6,000,000 die rolls\n",
    "for roll in range(6_000_000):  # note underscore separators\n",
    "    face = random.randrange(1, 7)+random.randrange(1, 7)\n",
    "\n",
    "    # increment appropriate face counter\n",
    "    if face == 1:\n",
    "        frequency1 += 1\n",
    "    elif face == 2:\n",
    "        frequency2 += 1\n",
    "    elif face == 3:\n",
    "        frequency3 += 1\n",
    "    elif face == 4:\n",
    "        frequency4 += 1\n",
    "    elif face == 5:\n",
    "        frequency5 += 1\n",
    "    elif face == 6:\n",
    "        frequency6 += 1\n",
    "    elif face == 7:\n",
    "        frequency7 += 1\n",
    "    elif face == 8:\n",
    "        frequency8 += 1\n",
    "    elif face == 9:\n",
    "        frequency9 += 1\n",
    "    elif face == 10:\n",
    "        frequency10 += 1\n",
    "    elif face == 11:\n",
    "        frequency11 += 1\n",
    "    elif face == 12:\n",
    "        frequency12 += 1\n",
    "        \n",
    "print(f'Face{\"Frequency\":>13}')\n",
    "print(f'{1:>4}{frequency1:>13}')\n",
    "print(f'{2:>4}{frequency2:>13}')\n",
    "print(f'{3:>4}{frequency3:>13}')\n",
    "print(f'{4:>4}{frequency4:>13}')\n",
    "print(f'{5:>4}{frequency5:>13}')\n",
    "print(f'{6:>4}{frequency6:>13}')\n",
    "print(f'{7:>4}{frequency7:>13}')\n",
    "print(f'{8:>4}{frequency8:>13}')\n",
    "print(f'{9:>4}{frequency9:>13}')\n",
    "print(f'{10:>4}{frequency10:>13}')\n",
    "print(f'{11:>4}{frequency11:>13}')\n",
    "print(f'{12:>4}{frequency12:>13}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cb278c45-04c7-480f-bd6d-3c043257224d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "craps: 0.11109983333333333\n"
     ]
    }
   ],
   "source": [
    "craps = frequency2 + frequency3 + frequency12\n",
    "print(\"craps:\", craps/6_000_000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "de15e289-6e18-462b-889e-c14a73292f57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "win: 0.22232\n"
     ]
    }
   ],
   "source": [
    "win = frequency7 + frequency11\n",
    "print(\"win:\", win/6_000_000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d17ca5ee-ed4c-425b-9d8c-c41f8a631c9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#surya_rayudu_module3"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
