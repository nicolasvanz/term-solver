class Words:
    def __init__(self):
        self.words = get_words()
        self.all_words = get_words()
        self.word_length = 5
    
    def guess(self, guess, info):
        correct_idx = []
        present_idx = []
        wrong_idx   = []

        error = False
        for i in range(self.word_length):
            if info[i] == 'g':
                correct_idx.append((i, guess[i]))
            elif info[i] == 'y':
                present_idx.append((i, guess[i]))
            elif info[i] == 'r':
                wrong_idx.append(guess[i])
            else:
                error = True
                break
        
        wrong_idx = list(set(wrong_idx))
        for w in wrong_idx:
            for c in correct_idx:
                if c[1] == w:
                    wrong_idx.remove(w)
            for p in present_idx:
                if p[1] == w and w in wrong_idx:
                    wrong_idx.remove(w)
        
        if error:
            print("error. this guess was not processed")
            return

        if (guess in self.all_words):
            self.all_words.remove(guess)
        else:
            print("this word is not registered!")

        self.process_correct(correct_idx)
        self.process_present(present_idx)
        self.process_wrong(wrong_idx)
        print(f"suggested: {self.suggested_guess()}")

    def process_correct(self, correct):
        while(True):
            removed = False
            for idx, letter in correct:
                for word in self.words:
                    if word[idx] != letter:
                        self.words.remove(word)
                        removed = True
            if not removed:
                break
    
    def process_present(self, present):
        while(True):
            removed = False
            for idx, letter in present:
                for word in self.words:
                    if letter in word and word[idx] != letter:
                        continue
                    else:
                        removed = True
                        self.words.remove(word)
            if not removed:
                break

    def process_wrong(self, wrong):
        while (True):
            removed = False
            for letter in wrong:
                for word in self.words:
                    if letter in word:
                        self.words.remove(word)
                        removed = True
            if not removed:
                break
    
    def suggested_guess(self):
        if len(self.words) == 1:
            return self.words[0]
    
        counter = {chr(i) : 0 for i in range(97, 123)}
        counter['??'] = 0

        total = len(self.words)

        if (total == 0):
            print("no words left! the word might not be registered!")
            exit()

        # counting ocurrencies
        for word in self.words:
            for letter in set(word):
                counter[letter] += 1

        # measuring how good the letter is in a guess.
        # we are looking for letters that appear in half of the possible words
        for key, value in counter.items():
            counter[key] = abs((value/total) - 0.5) + 0.5

        # measuring how good is a word in a guess. We already know which letters
        # are good. We use this here
        values = []
        for word in self.all_words:
            value = 1
            word_set = set(word)
            for letter in word_set:
                value *= counter[letter]
            values.append((word, value))
        
        values = sorted(values, key=lambda x: x[1])
        return values[0][0]


def get_words():
    return [
        "termo", "suite", "avido", "festa", "bebia", "honra", "ouvir", "pesco", "fungo", "pagam", "ginga", "pinta", "poder", "utero", "pilha", "sarar", "fruta",
        "piano", "notar", "musgo", "tensa", "melao", "feliz", "miojo", "pagos", "texto", "mamae", "ameno", "chuva", "coral", "forte", "tonta", "temor", "ligar", 
        "rolar", "navio", "limbo", "calvo", "fedor", "balde", "oxala", "talco", "labia", "crime", "grade", "carta", "flora", "comum", "fatal", "pecar", "feroz", 
        "virus", "armar", "couro", "exito", "ecoar", "balao", "falir", "tecer", "arena", "justo", "arido", "ruiva", "mumia", "fogao", "dupla", "touca", "sogro", 
        "osseo", "treta", "manha", "carie", "brejo", "acima", "bolso", "sitio", "dolar", "aereo", "peixe", "golfo", "conde", "meses", "perua", "suino", "molas", 
        "corar", "aguia", "rumor", "senao", "risos", "milha", "chato", "praga", "cloro", "mexer", "beato", "lugar", "nuvem", "plebe", "lindo", "bispo", "idosa", 
        "funil", "artes", "supor", "vital", "entao", "trigo", "rapaz", "caldo", "bocas", "manto", "males", "renal", "caber", "menor", "seiva", "palco", "palmo", 
        "poeta", "magoa", "ideia", "bolsa", "ruivo", "forno", "sismo", "exata", "razao", "radar", "pegar", "blusa", "hinos", "baita", "trico", "chata", "vasta", 
        "rugir", "motor", "ta??as", "orgia", "aspas", "total", "ardor", "prole", "tarja", "ninho", "credo", "pente", "falar", "canoa", "prato", "clave", "opaco", 
        "anjos", "velho", "grana", "vazia", "rumos", "altos", "mutua", "missa", "pardo", "leoes", "muros", "altas", "vigor", "tonto", "bruxa", "bacon", "orgao", 
        "bioma", "miudo", "reter", "agora", "fosco", "audio", "carpa", "cacho", "fardo", "povos", "denso", "perna", "basco", "guria", "pluma", "final", "ditos", 
        "icone", "jaula", "duros", "ponei", "amago", "barao", "pomba", "ficar", "serio", "cafes", "nicho", "fraca", "catar", "dicas", "morno", "claro", "posar", 
        "acesa", "duble", "levar", "corda", "trena", "inves", "achar", "barca", "peste", "batom", "dever", "crase", "todos", "picos", "ca??ao", "pulga", "bruxo", 
        "exame", "babar", "op??ao", "tedio", "secar", "rival", "aguda", "tiros", "tenis", "curar", "moeda", "bater", "cubos", "verme", "ostra", "mundo", "sabio", 
        "nomes", "belos", "parda", "nossa", "tanga", "unida", "caqui", "colar", "girar", "panda", "laico", "sueca", "rimar", "merce", "la??os", "ritos", "verde", 
        "pesar", "nadar", "fuzue", "obter", "dedao", "moida", "disso", "longa", "autos", "surda", "pinos", "poema", "ponte", "galao", "musas", "animo", "globo", 
        "leito", "ca??ar", "ileso", "malas", "pagar", "surfe", "polvo", "vasto", "nariz", "daqui", "lombo", "ambos", "vinda", "couve", "toada", "arabe", "sabao", 
        "porem", "veloz", "tabua", "seita", "grato", "falsa", "doces", "fogos", "lenta", "veias", "arcar", "danos", "arame", "po??os", "uniao", "hiena", "tipos", 
        "sacro", "patio", "tripa", "menos", "tosco", "cargo", "tanto", "igual", "eixos", "sadia", "apice", "expor", "ponta", "bones", "farol", "rolos", "astro", 
        "tapar", "fisco", "meter", "cesta", "calmo", "aries", "fiada", "feias", "oxido", "gesso", "ordem", "birra", "corvo", "dores", "fetal", "cisne", "lapso", 
        "exato", "penal", "pompa", "ambar", "ossos", "prazo", "ambas", "finas", "regua", "parco", "capaz", "pouco", "anais", "lapis", "vosso", "linda", "canil", 
        "infra", "ditar", "pudor", "mesmo", "len??o", "enfim", "ansia", "morar", "axila", "aureo", "greve", "acido", "rolim", "divas", "sotao", "banda", "fatos", 
        "corno", "areas", "dente", "poros", "cinto", "santa", "visor", "casca", "ferir", "fonte", "mania", "urnas", "cacau", "calva", "cento", "jarra", "sutil", 
        "magos", "genio", "sexta", "pareo", "reais", "mansa", "extra", "virar", "totem", "graxa", "capuz", "morna", "pudim", "andar", "genro", "medio", "prosa", 
        "gases", "trono", "medos", "lente", "hotel", "jogos", "gatos", "coxas", "oleos", "polos", "massa", "dosar", "macio", "agudo", "focar", "se??ao", "bloco", 
        "atras", "turma", "omega", "tropa", "jarro", "motel", "focos", "penta", "fusao", "vogal", "chefe", "verba", "campo", "ainda", "noite", "mafia", "cruel", 
        "umido", "assar", "qui??a", "pizza", "ovulo", "presa", "placa", "telas", "gordo", "alias", "quina", "estes", "pista", "latao", "gatas", "mares", "nudez", 
        "aliar", "areia", "fugir", "surdo", "untar", "bolos", "polen", "obeso", "cosmo", "preto", "luvas", "sarro", "gripe", "ruina", "geral", "torax", "euros", 
        "banal", "maior", "lomba", "tenue", "pouca", "sogra", "finos", "fluxo", "lider", "latas", "bazar", "limao", "duque", "belas", "seara", "secos", "colon", 
        "monge", "gelar", "a??oes", "sacos", "caros", "media", "lagos", "torto", "suave", "baque", "al??ar", "bambu", "ricas", "otico", "no??ao", "tutor", "pires", 
        "folia", "fumar", "praia", "corja", "anoes", "toldo", "dunas", "norte", "bingo", "retro", "naves", "matos", "muito", "acaso", "viril", "vagar", "costa", 
        "esqui", "bucho", "dogma", "burra", "optar", "ardua", "rezar", "mamar", "fu??ar", "aluna", "dados", "saida", "vazar", "cervo", "negar", "picar", "furor", 
        "carma", "otima", "idolo", "juizo", "filho", "gamba", "perto", "gozar", "feudo", "sueco", "salas", "tibia", "futil", "lisos", "brasa", "facao", "sumir", 
        "socio", "bando", "etico", "grego", "pelos", "signo", "votos", "vulto", "lotus", "pampa", "lerdo", "louca", "times", "gaita", "gosma", "tarso", "telha", 
        "visao", "moela", "hifen", "murro", "sigma", "celta", "goela", "modos", "reger", "longe", "opera", "bamba", "cesto", "gemeo", "zonas", "video", "carga", 
        "julho", "ondas", "anual", "longo", "roupa", "treco", "bucal", "aroma", "citar", "vulgo", "reves", "bares", "lidar", "aveia", "novos", "bravo", "mirar", 
        "modas", "nasal", "cedro", "camas", "atlas", "anzol", "comer", "calar", "linho", "sadio", "ro??ar", "major", "tubos", "bolha", "arcos", "selva", "sagaz", 
        "puxar", "olhos", "meias", "velha", "angra", "duplo", "fixar", "garra", "impio", "algum", "setor", "japao", "pisos", "sauna", "salsa", "aonde", "furia", 
        "densa", "besta", "tribo", "loura", "socar", "indio", "pre??o", "crise", "teses", "sarda", "clara", "legal", "frase", "ceder", "lo??ao", "pra??a", "turco", 
        "boato", "olhar", "valor", "vacuo", "casar", "geada", "sodio", "dotar", "cavar", "quais", "elite", "banjo", "ultra", "vivos", "truco", "terno", "posse", 
        "bonde", "robos", "cetro", "frios", "pneus", "valer", "zerar", "pedir", "matar", "leite", "mista", "porre", "lince", "gesto", "morta", "vazao", "titia", 
        "unica", "dueto", "gavea", "pomar", "vocal", "epoca", "busto", "calor", "sutis", "faixa", "prata", "pavor", "prado", "genes", "afins", "cacos", "otica", 
        "culto", "jovem", "ideal", "negro", "lunar", "balsa", "norma", "zelar", "lutar", "ducha", "nisso", "ciclo", "rosca", "diodo", "frota", "moral", "fibra", 
        "adeus", "pedra", "culta", "turno", "pobre", "po??ao", "solar", "podar", "peoes", "idade", "clipe", "pausa", "avela", "naipe", "piada", "sucos", "trufa", 
        "parar", "cabos", "subir", "bulbo", "pilar", "fauna", "rotas", "adaga", "dorso", "atomo", "repor", "parvo", "canja", "urubu", "pedal", "sorte", "tecno", 
        "sinal", "boate", "ursos", "coisa", "botao", "rombo", "moita", "fases", "raros", "censo", "polar", "perda", "trens", "tenor", "viral", "cupom", "tosca", 
        "cheia", "terra", "menta", "brava", "hiato", "raiva", "epica", "casos", "grega", "meiga", "giria", "rosas", "lares", "cinco", "vezes", "desde", "larva", 
        "vetor", "clube", "beata", "minha", "congo", "trair", "laudo", "mapas", "fosso", "zebra", "banir", "tatil", "mimar", "ricos", "cabra", "movel", "motos", 
        "irmas", "jurar", "lobos", "manga", "persa", "pirao", "licor", "gerir", "linha", "algoz", "pombo", "zinco", "farao", "copos", "cinta", "gorro", "rodar", 
        "tigre", "taxis", "impar", "palha", "docil", "quase", "sushi", "mover", "gra??a", "mogno", "papel", "porca", "etica", "cheio", "carro", "farsa", "redor", 
        "doido", "quota", "rampa", "oeste", "facas", "balas", "vozes", "tango", "pesos", "oasis", "rimel", "foice", "lilas", "gente", "junho", "tirar", "puxao", 
        "parir", "circo", "ampla", "lebre", "mesma", "nisto", "haste", "sopas", "donos", "pirar", "radio", "farra", "senso", "nunca", "certo", "acola", "mirim", 
        "vinil", "senha", "cisto", "farpa", "estar", "haver", "aviao", "natal", "rigor", "sonar", "album", "atriz", "verbo", "homem", "germe", "labio", "parma", 
        "clima", "misto", "bocal", "bacia", "micro", "vagao", "nulos", "topar", "abono", "burro", "bra??o", "tempo", "gerar", "canal", "ritmo", "otimo", "lados", 
        "ralar", "debil", "atual", "capim", "muita", "votar", "tenso", "forum", "fator", "galho", "lixar", "ramos", "areal", "febre", "loiro", "jejum", "alado", 
        "ousar", "amplo", "impor", "museu", "manso", "delta", "idoso", "juiza", "nozes", "fiapo", "cujos", "abrir", "tripe", "sexto", "retas", "civil", "feira", 
        "servo", "nevoa", "patas", "jogar", "sanha", "doida", "bicos", "rever", "folha", "palma", "sarau", "filha", "venus", "fugaz", "obvio", "sacra", "focal", 
        "mosca", "touro", "punir", "barba", "rocha", "casco", "panos", "a??ude", "ter??o", "gotas", "favor", "usual", "ossea", "rubro", "rosto", "nevar", "dardo", 
        "brega", "prece", "regar", "frias", "rolha", "treno", "casta", "gar??a", "torpe", "fixos", "jegue", "frade", "macro", "habil", "rouca", "caule", "guiar", 
        "horto", "lidos", "somar", "mitos", "cilio", "ninar", "santo", "assim", "netos", "caspa", "ninja", "cegos", "facil", "altar", "algas", "caras", "farda", 
        "sunga", "cupim", "horta", "vespa", "lorde", "deusa", "vacas", "relva", "vidas", "abril", "super", "criar", "nivel", "grupo", "adega", "voraz", "vasos", 
        "usina", "ratos", "ter??a", "cueca", "brisa", "feita", "vetar", "podio", "fossa", "coeso", "aneis", "lirio", "tinto", "volei", "serva", "mutuo", "trapo", 
        "metro", "nobre", "ombro", "umida", "louco", "gueto", "punho", "amora", "redes", "cofre", "trama", "ageis", "ganso", "latim", "obras", "golpe", "rente", 
        "vicio", "russo", "vazio", "civis", "na??ao", "bicho", "sabia", "salmo", "podre", "alvos", "loira", "cetim", "unhas", "fobia", "salao", "praxe", "bruta", 
        "lenha", "clero", "jeito", "potes", "tumba", "ninfa", "sarna", "tomar", "macia", "sabor", "caida", "leque", "justa", "tocha", "lazer", "feixe", "selos", 
        "etapa", "unico", "duzia", "pavao", "sigla", "durar", "fazer", "truta", "tinta", "graus", "pavio", "torta", "deter", "clone", "tufao", "polpa", "trupe", 
        "malta", "irado", "selar", "boina", "atuar", "corpo", "magia", "ma??as", "pinho", "preta", "fosca", "gruta", "bossa", "magro", "lento", "lousa", "falso", 
        "tosar", "aluno", "padre", "metal", "meios", "lenda", "bonus", "crepe", "antes", "milho", "simio", "drama", "chave", "grama", "raras", "mesas", "harpa", 
        "treze", "fraco", "gorda", "magra", "leigo", "hindu", "adiar", "caixa", "voces", "magna", "fofas", "varal", "uteis", "teias", "femea", "marte", "errar", 
        "frear", "macho", "serie", "viver", "damas", "femur", "feios", "sutia", "arduo", "sujar", "golfe", "ra??ao", "cinza", "barco", "rasto", "malte", "almas", 
        "arder", "naval", "vinte", "nervo", "reler", "xampu", "lotar", "reles", "erros", "ponto", "frevo", "ervas", "copas", "pisar", "fruto", "beber", "trevo", 
        "lesao", "grata", "certa", "botar", "tocar", "sujos", "amada", "cerne", "valsa", "heroi", "ciume", "juros", "dedos", "mambo", "bruto", "reuso", "dieta", 
        "telao", "depor", "litro", "domar", "miope", "polir", "dizer", "midia", "autor", "bucha", "remar", "miolo", "letal", "plena", "fluir", "calma", "cenas", 
        "medir", "ziper", "selim", "pleno", "outra", "li??ao", "mural", "feras", "todas", "aerea", "tetra", "outro", "irmao", "co??ar", "furar", "porco", "advir", 
        "breve", "exodo", "vilao", "letra", "vapor", "libra", "amido", "imune", "pular", "lagoa", "bomba", "horas", "casal", "sacar", "meros", "tunel", "rural", 
        "mudar", "chapa", "usada", "atroz", "etnia", "nenem", "orfao", "calda", "chale", "furos", "ontem", "copia", "raiar", "novas", "cauda", "meigo", "vinho", 
        "joias", "lavar", "bufao", "aulas", "lojas", "safra", "odiar", "tchau", "arroz", "carne", "prumo", "fotos", "junco", "epico", "tesao", "refem", "manta", 
        "raios", "humor", "sanar", "dique", "ber??o", "fluor", "sosia", "local", "gemer", "saber", "visar", "raial", "disco", "leais"
    ]
