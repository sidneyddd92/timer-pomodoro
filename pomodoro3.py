import time
from win10toast import ToastNotifier

def pomodoro_timer():
    count = 0
    work_duration = 25 * 60  # 25 minutos em segundos
    break_duration = 5 * 60   # 5 minutos em segundos

    toaster = ToastNotifier()
    print("Timer iniciado! Hora de focar!")

    while True:
        # Ciclo de trabalho
        time.sleep(work_duration)
        count += 1
        toaster.show_toast(
            "⏰ Hora do descanso!",
            f"Você completou {count} Pomodoro(s). Descanse por 5 minutos!",
            duration=10
        )

        # Ciclo de descanso
        time.sleep(break_duration)
        toaster.show_toast(
            "Hora de voltar ao trabalho!",
            "Prepare-se para mais um Pomodoro...",
            duration=10
        )

if __name__ == "__main__":
    pomodoro_timer()
