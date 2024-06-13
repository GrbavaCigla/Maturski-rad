# Sistem za procenu više fundamentalnih frekvencija

## Predgovor
## Uvod
## Zvuk

### Definicija
Zvuk je mehanicki talas u ciju pojavu karakterisu tri osnovna cinioca: izvor (generator), materijalna okolina i prijemnik (receptor). Izvor ili generator moze biti bilo koje telo koje se nekakvim uticajem dovede u stanje treperenja. Medjutim, sam izvor nije dovoljan sam po sebi vec mu je neophodan i prostor na koji ce se njegovo treperenje preneti i izazvati sabijanja i razređenja cestica obrazujuci zvucne talase. Da bi ljudi mogli da cuju zvuk, potreban je i treci cinilac - prijemnik. Prijemnik ili receptor nadrazaje zvuka pretvara u osecaj. Prema tome, zvuk se moze definisati na vise nacina, kao objektivna fizicka pojava i kao subjektivna psihicka pojava.

### Osobine
Svaki zvuk poseduje cetiri osnovne osobine: trajanje, jacinu, visinu i boju.

Znajuci da zvuk nastaje treperenjem tela pod uticajem, lako se moze zakljuciti da trajanje zvuka zavisi od tog uticaja, ali u mnogim slucajevima to nije sasvim tacno. U prethodni zakljucak izvodi nemajuci u vidu inerciju zvucnog izvora. Kod odredjenih zvucnih izvora, treperenje prakticno odmah staje po prestanku uticaja na telo, dok kod drugih traje duze i stvara odzvuk.

Jačina zvuka je direktno povezana sa amplitudom treperenja čestica. Što je amplituda veća, to je zvuk jači. Moguće je promeniti jačinu zvuka menjanjem jacine uticaja na izvor, ali nakon prestanka uticaja, kada treperenje opstaje zbog inercije, amplituda opada, samim tim i zvuk postaje sve tiši.

Visina zvuka zavisi od ucestalosti treptaja i jos se naziva frekvencija. Preciznije, frenkvencija je broj oscilacija u jedinici vremena, a jedan treptaj po sekundi se smatra frekvencijom od jednog herca. Zvukom se nazivaju mehanicki talasi od oko 16Hz (subkontra C, najnizeg kod velikih orgulja) do oko izmedju 16kHz i 20kHz jer su to granice cujnosti kod ljudi. Zvucna treperenja ispod granica cujnosti se nazivaju infrazvukom, a iznad ultrazvukom. Tacnu visinu tona covek moze da prepozna u pribliznom rasponu od 32Hz do 5kHz (u orkestru obuhvata frekvenciju najnizeg tona subkontra B kontrafagota od oko 29Hz do najviseg tona C5 pikolo-flaute od oko 4185Hz).

[slika tona flaute, oboe i suma (sl. 3 u knjizi)](#)

Boja zvuka ili na francuskom tembr predstavlja osobinu po kojoj se dva zvuka jednake visine i jacine razlikuju. Ton nastaje pravilnim, harmonicnim oscilacijama, dok nepravilnim i neujednacenim nastaje sum. Svaki ton koji nije cist nastaje iz treperenja vise tonova razlicitih frekvencija. Osnovni ton se naziva fundamentala, a ostali tonovi se nazivaju alikvotni tonovi (takodje prirodni, harmonicni, parcijalni ili gornji) i njihov odnos je uvek jednak. Kao primer, ton A4 se koristi kao referentna frekvencija, poznata kao kamerton, s frekvencijom od 440 Hz. Ako je ovo fundamentalna frekvencija, njeni harmonijski tonovi će biti: 880Hz, 1320Hz, 1760Hz, 2200Hz, itd. Konacni oblik treperenja se dobija intereferencijom svih tonova, tj. sabiranjem svih oscilacija.

[slika sabiranja (sl. 5 u knjizi)](#)

## Procena fundamentale
### Diskretna Furijeova transformacija

Diskretna Furijeova transformacija (DFT) je matematička tehnika koja se koristi za analizu periodičnih signala i njihovu reprezentaciju u frekvencijskom domenu. Ova transformacija pretvara vremenski domen signala u frekvencijski domen, omogućavajući nam da vidimo koje su frekvencije prisutne u signalu i s kojom amplitudom.

[slika bez DFT i sa DFT](#)

A njegova formula se moze izraziti kao:

[formula za DFT](#)

gde X(k) predstavlja vrednost spektralne komponente na frekvenciji k, x(n) je vrednost signala u vremenskom domenu za vreme n, N je ukupan broj uzoraka signala, a e je Ojlerov broj.

Osim DFT-a, postoji i Short-Time Fourier Transform (STFT), koji predstavlja DFT primijenjen na određenom vremenskom intervalu. Koristi se zbog promjenjive prirode podataka u zvučnom signalu.

### Jednostavan DFT tjuner

Za izradu jednostavnog DFT tjuner, bitno je odrediti veličinu prozora STFT, odnosno trajanje pojedinačne Furijeove transformacije. Što je veći prozor, preciznost DFT-a je veća, ali je i "kašnjenje" veće.

[inline formula 1/t=resolution](#)

Za svaki prozor u ulaznom signalu, izvodi se STFT, a zatim se odabire fundamentalna frekvencija - frekvencija s najvećom magnitudom. Za ovaj algoritam se podrazumeva da je dominantna frekvencija, frekvencija sa najvećom magnitudom ekvivalentna fundamentali, što najčešće nije slučaj zbog čega ovaj algoritam nije pouzdan.

### HPS tjuner

Da bi ispravili grešku u prethodnom algoritmu, koristimo proizvod harmoničnog spektra (HPS). HPS koristi to što su njihovi odnosi izmedju alikvota jednaki.

[formula za HPS](#)

gde je Y(x) verovatnoća da je data frekvencija x fundamentala. Za fundamentalu se uzima najveći frekvencija sa najvećim Y. Ovaj metod se koristi i danas i za razliku od prethodnog, pouzdan je. Jedan od mana algoritma koji je vrlo lako rešiv je da se često desi da algoritam nađe ton pogrešne oktave. Rešenje tog problema je provera 1/2 nađene fundamentale.

## Procena više fundamentala

Nakon analiziranja više radova o ovoj temi, odlučio sam da svoj rad baziram na dva rada Ansija Klapurija. Ti radovi su [] i [].

### Spektralno beljenje

Zvuk koji se dobija snimanjem audija se može opisati sledećom funkcijom:

[formula X(k) = H(k) * S(k) + N(k)](#)

gde je X(k) zvuk koji se, S(k) zvuk instrumenta koji se posmatra, H(k) okruzenje i boja instrumenta, a N(k) aditivan šum. Da bi algoritam za procenu više fundamentala bolje radio, potrebno je eliminisati šum i ujednačiti H(k). Za ujednačavanje se koristi spektralno beljenje.

[formula za trouglove](#)

Gde je ... TODO

Algoritam korišćen u ovom radu započinje izračunavanjem trouglova nad ulaznom frekvencijom, pri čemu se vrednosti kreću od 0 do 1 prema zadatoj formuli. Zatim se za svaki od tih trouglova izvršava množenje sa ulaznim signalom kako bi se dobio izolovani frekvencijski opseg. Upotreba trouglova u ovom algoritmu je analogna upotrebi Hann prozora u STFT-u, gde se koristi za postizanje glatkog prelaza između značajnih i manje značajnih informacija. Sabiranjem svih uzoraka dobijenih proizvoda dolazi se do vrednosti koja predstavlja važnost određenog centra, dok se vrednosti opsega dobijaju interpolacijom centara. Precizna formula za ocenu važnosti opsega nije od ključnog značaja.

### Izračunavanje važnosti kandidata

ODAVDE TREBA U ČETDžiPiTiju preformulisati glupe reči

Mnogi radovi koji imaju cilj da nađu funkciju koja definiše bitnost ili važnost neke fundamentale se manje ili više zasnivaju na formuli

[formula za S(tau)](#)

Gde je ... TODO

koja u suštini sabira fundamentalu sa svojim harmonicima pomnoženim sa njihovim težinama.

Zbog brzine, koristimo diskretnu verziju Furijeove transformacije, zbog čega [|Y(f)|](#) postaje [max(Y(k))](#), a formula postaje

[formula za S(tau) brza](#).

Gde je ... TODO

Ovim metodom možemo brzo izračunati kolika je verovatnoća da je neki kandidat zapravo fundamentalna frekvencija. Ostaje još samo da se izračuna težinska funkcija [G(Tau, m)](#).

### Nalaženje težina

U originalnom radu napravljena je baza prvo pojedinačnih tonova različitih instrumenata, a potom su ti tonovi nasumično mešani. Mešani uzorci se sastoje od 2, 3, 4 ili 6 tonova i zajedno sa pojedinačnim tonovima grade bazu sa oko 4000 uzoraka. Prepoznavanje fundamentale je rađeno tako što se izabere nekoliko "najvažnijih" frekvencija u zavisnosti koliko uzorak ima tonova.

Funkcija [G(Tau, m)](#) je izražena na dva načina:

[G(Tau, m) = ](#)
[G(Tau, m) = ](#)

Korišćenjem dve funkcije sa jednim parametrom umesto dva olakšava izračunavanje i dalju optimizaciju. Čitanja ranije navedenih uzoraka nam govori kretanja g1, g2 i g3 funkcija što se može videti na sledećim graficima.

[Grafici g1 g2](#)
[Grafici g1 g3](#)

Tačno izračunavanje ove tri funkcije prevazilazi obim rada, ali je dovoljno reći [g1(tau) = fs/tau](#), [g2(m) = 1 / m](#), [g3(Ftm) = 1 / Ftm](#). Zbog jednostavnije implementacije, druga formual je korišćena. Množenjem te dve funkcije se dolazi do formule

[g(tau, m) = (fs/tau)/(Ftm)](#),

koja se dalje može izračunati kao

[g(tau, m) = (fs/tau)/(m*fs/tau)](#)

i na kraju se dodaju [alfa]() i [beta]() koji menjaju više parametara da bi formula bila jednostavnija:

[g(tau, m) = (fs/tau + alfa)/(m*fs/tau + beta)](#)

### Iterativni postupak i poništavanje

Problem sa prethodno navedenim postupkom nalaženja fundamentale sa najvećom važnosti je to što ne radi dobro na više vrhova na DFT grafu. Ako se uzme prvi i najviši vrh sa najvećom važnosti, frekvencija koja odgovara tom vrhu najverovatnije jeste fundamentala prvog tona, ali ostali vrhovi sa sledećom najvećom važnosti vrlo često nisu drugi, treći... ton. Iz tog razloga se nađeni ton oduzima od celog grafa zajedno sa svojim harmonicima, a [s(t)](#) se menja u skladu sa promenama. Ovaj proces se ponavlja dok sve fundamentale ne budu promanđene.

Za nalaženje maksimuma vrednosti [s(t)](#) nije potrebno računati [s(t)](#) za svako [tau](#), dovoljno je koristiti algoritam sličan binarnoj pretrazi. Slično kao u numeričkoj metodi nalaženja nula funkcije metodom polovljenja, definišemo [tau gornje](#) i [tau donje](#) koji na početku predstavljaju minimum i maksimum za vrednost [tau](#). Polovimo opseg u dva bloka i tražimo blok sa najvećom važnosti. Algoritam se ponavlja sve dok moguća greška nije manja od [tau prec](#).

Nakon nalaženja [tau](#) za maksimalno [s(t)](#) pravi se novi graf sa fundamentalom i njegovim harmonicima pomnoženim sa težinama g. Zatim se od grafa Y oduzima novi graf i algoritam se ponavlja dok postoje vrhovi.

### Konačan algoritam

Prethodno naveden algoritam pravi dobre rezultate, ali postoji problem prepoznavanja broja tonova u nekom zvuku, tj. koliko puta iterativni postupak treba da se ponovi.

## Literatura
Muzicki instrumenti, Dejan Despic, 1986  
Fundamentals of Telephone Communication Systems, Western Electrical Company, 1969
https://www.chciken.com/digital/signal/processing/2020/05/13/guitar-tuner.html  
https://en.wikipedia.org/wiki/Discrete_Fourier_transform?useskin=vector
http://musicweb.ucsd.edu/~trsmyth/analysis/Harmonic_Product_Spectrum.html