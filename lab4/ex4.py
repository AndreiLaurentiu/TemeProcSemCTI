"""
"Cele mai joase frecvențe emise de un contrabas se încadrează într-un interval de la 40 Hz la 200 Hz. Pentru a captura cu precizie toate aceste componente de frecvență în semnalul discretizat provenit din înregistrarea instrumentului, este esențial să alegem o frecvență de eșantionare adecvată.

Conform teoremei Nyquist-Shannon, așa cum este detaliat în fișa laboratorului, există o relație crucială între frecvența minimă de eșantionare (fs) și frecvența maximă conținută în semnal (B). Această relație ne indică că fs trebuie să fie cel puțin dublul valorii lui B, adică fs >= 2B. În cazul nostru, valoarea lui B este de 200 Hz, așadar, frecvența de eșantionare (fs) trebuie să fie mai mare de 2 * 200 Hz, adică fs > 400 Hz.

Astfel, pentru a asigura că semnalul discretizat conține toate componentele de frecvență ale contrabasului, este necesar ca frecvența de eșantionare să fie mai mare de 400 Hz. În acest fel, toate frecvențele mai mici sau egale cu 200 Hz vor fi reprezentate corect în semnalul nostru."
"""