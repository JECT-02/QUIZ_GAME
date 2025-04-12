class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
        
def run_quiz():
    print("Bienvenido al juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    
    quiz = Quiz()
    
    # Preguntas de ejemplo (debes agregar 10)
    preguntas = [
        Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], "3"),
        Question("¿Cuál es el planeta más cercano al Sol?", ["Venus", "Mercurio", "Tierra", "Marte"], "2"),
        Question("¿Qué lenguaje se usa en la web?", ["Python", "HTML", "Java", "C++"], "2"),
        Question("¿Qué animal es el rey de la selva?", ["León", "Elefante", "Tigre", "Gorila"], "1"),
        Question("¿Cuánto es 5 x 5?", ["20", "10", "25", "15"], "3"),
        Question("¿Qué país tiene forma de bota?", ["España", "Italia", "Chile", "Brasil"], "2"),
        Question("¿Cuál es el océano más grande?", ["Atlántico", "Índico", "Ártico", "Pacífico"], "4"),
        Question("¿Cuál es la moneda de Japón?", ["Yen", "Won", "Dólar", "Euro"], "1"),
        Question("¿Cuál es el color resultante de mezclar azul y amarillo?", ["Rojo", "Verde", "Morado", "Naranja"], "2"),
        Question("¿En qué continente está Egipto?", ["Asia", "América", "África", "Europa"], "3")
    ]

    for q in preguntas:
        quiz.add_question(q)

    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        print(f"\nPregunta {quiz.current_question_index}: {question.description}")
        for i, opt in enumerate(question.options):
            print(f"{i + 1}) {opt}")
        respuesta = input("Tu respuesta: ")
        if quiz.answer_question(question, respuesta):
            print("¡Correcto!")
        else:
            print("Incorrecto.")

    print("\nJuego terminado.")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")