goodwords = ["hi", "cool", "nice", "good", "perfect", "achievement",
"bigger", "biggest", "goodest", "coolest", "hello",
"nicest", "lovely", "cute", "cutest", "thank",
"thanks", "helped", "qpr", "advice", "wise",
"wish", "wished", "wisdom", "acquintance",
"enjoy", "happy", "happiness", "kind", "like",
"forgiveness", "friend", "feel", "understand", "hope",
"reconciliation", "accept", "strength", "faith", "solidarity",
"tolerance", "peace", "compassion", "freedom", "respect", "peace",
"hope", "faith", "reconciliation", "friendship",
"respect", "freedom", "happiness", "solidarity", "compassion",
"strength", "tolerance", "understanding", "acceptance", "affection",
"loyalty", "support", "joy", "trust", "honesty",
"warmth", "sincerity", "empathy", "grace",
"connect", "body", "wake up", "dream", "life", "do", "nothing",
"party", "walk", "doing", "new", "peace", "love", "love", "feel",
"live", "light", "take", "take", "car", "take", "find", "look",
"all", "future", "love", "walk", "always", "take", "light", "freedom",
"journey", "find", "all", "new", "leave", "care", "love","hola", "genial", "amable", "bueno", "perfecto", "logro",
"más grande", "más grande", "más bueno", "más genial", "hola",
"más agradable", "encantador", "lindo", "más lindo", "gracias",
"gracias", "ayudó", "qpr", "consejo", "sabio",
"deseo", "deseado", "sabiduría", "conocimiento",
"disfrutar", "feliz", "felicidad", "amable", "gustar",
"perdón", "amigo", "sentir", "entender", "esperanza",
"reconciliación", "aceptar", "fuerza", "fe", "solidaridad",
"tolerancia", "paz", "compasión", "libertad", "respeto", "paz",
"esperanza", "fe", "reconciliación", "amistad",
"respeto", "libertad", "felicidad", "solidaridad", "compasión",
"fuerza", "tolerancia", "comprensión", "aceptación", "afecto",
"lealtad", "apoyo", "alegría", "confianza", "honestidad",
"calidez", "sinceridad", "empatía", "gracia",
"conectar", "cuerpo", "despertar", "soñar", "vida", "hacer", "nada",
"fiesta", "caminar", "haciendo", "nuevo", "paz", "amar", "amar", "sentir",
"vivir", "luz", "tomar", "tomar", "coche", "tomar", "encontrar", "mirar",
"todos", "futuro", "amar", "caminar", "siempre", "tomar", "luz", "libertad",
"viajar", "encontrar", "todos", "nuevo", "dejar", "cuidar", "amar", "like", "gusta", "friendship", "power", "freedom", "future", "truth", "hope", "family",
"love", "honor", "union", "respect", "brother", "sister", "support", "survival",
"loyalty", "protection", "courage", "justice", "fight", "resistance",
"unity", "true", "strength", "change", "new", "grow", "challenge", "revolution",
"trust", "strength", "integrity", "awakening", "evolution", "success", "amistad", "poder", "libertad", "futuro", "verdad", "esperanza", "familia",
"amor", "honor", "unión", "respeto", "hermano", "hermana", "apoyo", "supervivencia",
"lealtad", "protección", "coraje", "justicia", "lucha", "resistencia",
"unidad", "verdad", "fuerza", "cambio", "nuevo", "crecer", "desafío", "revolución",
"confianza", "fuerza", "integridad", "despertar", "evolución", "éxito"]

pronouns = ["I", "you", "he", "she", "they", "them", "we"]

badwords = ["no", "uf", "tonto", "malo", "raro", "amor", "silbidos",
 "silbido", "silbido", "malo", "horrible", "terrible", "más raro",
 "más malo", "asustado", "encerrado", "susto", "amor", "procrastinación",
 "trauma", "desconocido", "coqueteo", "romance", "solo", "asesino", "muerto",
 "mortal", "osadía", "ir", "dolor", "tristeza", "engaño", "culpa",
 "fracaso", "miedo", "soledad", "rencor", "desilusión", "llorar",
 "maldición", "sufrimiento", "venganza", "desesperación", "resentimiento",
 "dolor", "tristeza", "fracaso", "culpa", "sufrimiento", "miedo",
 "soledad", "resentimiento", "venganza", "engaño", "desesperación",
 "rencor", "abandono", "desilusión", "traición", "confusión", "ira",
 "vergüenza", "odio", "lamento", "pérdida", "desconfianza",
 "desprecio", "inseguridad", "angustia", "guerra", "noche", "matar", "no", "creo", "todavía", "matar", "traición",
 "miedo", "despierto", "dolor", "trampa", "caída", "desgaste", "mentira",
 "muerte", "confusión", "vacío", "fracaso", "tristeza", "miseria", "oscuridad",
 "soledad", "mentira", "sufrimiento", "fracaso", "olvido", "ruina", "depresión",
 "irreal", "lucha", "desesperación", "no", "ugh", "dumb", "bad", "weird", "love", "whistles",
"whistle", "hiss", "bad", "horrible", "terrible", "weirdest",
"worst", "scared", "locked up", "fright", "love", "procrastination",
"trauma", "unknown", "flirting", "romance", "alone", "killer", "dead",
"deadly", "daring", "go", "pain", "sadness", "deception", "guilt",
"failure", "fear", "loneliness", "resentment", "disillusionment", "cry",
"curse", "suffering", "revenge", "despair", "resentment",
"pain", "sadness", "failure", "guilt", "suffering", "fear",
"loneliness", "resentment", "revenge", "deception", "despair",
"resentment", "abandonment", "disillusionment", "betrayal", "confusion", "anger",
"shame", "hate", "regret", "loss", "distrust",
"contempt", "insecurity", "anguish", "war", "night", "kill", "no", "I believe", "still", "kill", "betrayal",
"fear", "awake", "pain", "trap", "fall", "wear", "lie",
"death", "confusion", "emptiness", "failure", "sadness", "misery", "darkness",
"loneliness", "lie", "suffering", "failure", "forgetfulness", "ruin", "depression",
"unreal", "struggle", "despair", "war", "kill", "fear", "hate", "evil", "lie", "betrayal", "deception",
"violence", "guilt", "suffering", "failure", "confusion", "despair", "destruction",
"hell", "desolation", "revenge", "corruption", "liar", "hypocrisy", "dishonesty",
"manipulation", "secret", "low", "curse", "sin", "misery", "falsehood", "desire",
"depression", "vulnerability", "loneliness", "hatred", "traitor", "domination", "colonization",
"rape", "discrimination", "humiliation", "confrontation", "distrust", "guerra", "matar", "miedo", "odio", "maldad", "mentira", "traición", "engaño",
"violencia", "culpa", "sufrimiento", "fracaso", "confusión", "desesperación", "destrucción",
"infierno", "desolación", "venganza", "corrupción", "mentiroso", "hipocresía", "deshonestidad",
"manipulación", "secreto", "bajo", "maldición", "pecado", "miseria", "falsedad", "deseo",
"depresión", "vulnerabilidad", "soledad", "odio", "traidor", "dominación", "colonización",
"violación", "discriminación", "humillación", "confrontación", "desconfianza"]

#############################################################################################

mood = 0
while True:
    usersaid = input("Text: ").lower()


    lenght = len(usersaid)
    word = 0

    for word in goodwords:
     if word in usersaid:
            mood = mood + 1

    for word in badwords:
        if word in usersaid:
            mood = mood - 1

    print(mood)
