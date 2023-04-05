# Sciąga (Neo)Vim

1. Tryby
2. Komendy
3. Poruszanie Kursorem
4. Manipulowanie tekstem
5. Skrót

## 1.Tryby
### 1.Normal Mode
Domyślny tryb w którym znajdujemy się po wejściu do aplikacji.
Powrót do niego z innych trybów poprzez ESC.
### 2.Insert Mode
Tryb w który wchodzimy 'i'. Można w nim normalnie wprowadzać tekst i poruszać się strzałkami. Alternatywnie można wejść 'o', linię pod aktualną linią.
### 3.Visual Mode
Tryb w który wchodzimy 'v'. Można w nim zaznaczać tekst.
### 4.Command Mode
Wchodzimy do niego ':'. Wpisujemy w nim komendy.
### 5.Replace Mode
Wchodzimy do niego 'R'. Wprowadzi nas w Insert Mode, i to co wpiszemy zastąpi istniejący tekst.

## 2.Komendy
Komendy wpisujemy tylko w trybie normalnym
:q - wyjście z aplikacji
:wq - wyjście z aplikacji zapisując
:q! - wyjście bez zapisywania
/slowo - szuka słowo
:nr - przenosi nas do lini o danym numerze

## 3.Poruszanie Kursorem
h,j,k,l - lewo, dół, góra, prawo
4j - przemieszcza 4 rzędy w dół, analogicznie dla innych kierunków i liczb
w - początek kolejnego słowa
b - początek poprzedniego słowa
e - koniec słowa
0 - początek lini
$ - koniec lini
gg - początek pliku
shift+g - koniec pliku


## 4.Manipulowanie tekstem
dd - usuwa linie
p - wkleja usuniętą linie
r - podmienia jeden znak
x - usuwa jeden znak
u - undo
ctrl+r - redo
d - operator usuwania

## 5.Skrót
gg, shift+g - początek koniec pliku
i,o - insert w obecnym miejscu, kolejnej linijce
w,b - początek następnego, poprzedniego słowa
0,$ - początek koniec lini
dd - usuwa linie
p - wkleja usuniętą linie
u - undo
:wq, :q! - write quit, force quit
:nrlini - przenosi nas do odpowiedniej lini
