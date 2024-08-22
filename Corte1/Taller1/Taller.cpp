#include <windows.h>
#include <string>
#include <sstream>
#include <iostream>
#include <chrono>  // Incluir la librería para el cálculo del tiempo

#define ID_INPUT 1001
#define ID_OK 1002
#define ID_PROMPT 1003

// Variables globales para capturar la entrada
HWND hInput;
HWND hPrompt;
std::string inputText;
std::wstring wPromptText;

// Función de procedimiento para la ventana de entrada
LRESULT CALLBACK InputDlgProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch (msg) {
    case WM_CREATE:
        // Crear el control de texto para mostrar el mensaje
        CreateWindowW(L"STATIC", wPromptText.c_str(), WS_CHILD | WS_VISIBLE | SS_CENTER,
            10, 10, 300, 20, hwnd, (HMENU)ID_PROMPT, GetModuleHandle(NULL), NULL);

        // Crear el control de entrada de texto
        hInput = CreateWindowW(L"EDIT", L"", WS_CHILD | WS_VISIBLE | WS_BORDER | ES_LEFT,
            10, 40, 300, 20, hwnd, (HMENU)ID_INPUT, GetModuleHandle(NULL), NULL);

        // Crear el botón OK
        CreateWindowW(L"BUTTON", L"OK", WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 70, 50, 20, hwnd, (HMENU)ID_OK, GetModuleHandle(NULL), NULL);
        break;
    case WM_COMMAND:
        if (LOWORD(wParam) == ID_OK) {
            wchar_t buffer[256];
            GetWindowTextW(hInput, buffer, 256);
            inputText = std::string(buffer, buffer + wcslen(buffer));
            DestroyWindow(hwnd);
            PostQuitMessage(0);
        }
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hwnd, msg, wParam, lParam);
    }
    return 0;
}

// Función para mostrar una ventana de entrada personalizada
std::string promptForInput(const std::string& prompt) {
    // Convertir std::string a std::wstring para usar con la API de Windows
    wPromptText = std::wstring(prompt.begin(), prompt.end());

    // Registrar la clase de ventana
    WNDCLASSW wc = {};
    wc.lpfnWndProc = InputDlgProc;
    wc.hInstance = GetModuleHandle(NULL);
    wc.lpszClassName = L"InputDialogClass";
    RegisterClassW(&wc);

    // Dimensiones de la ventana
    int width = 340;
    int height = 120;

    // Obtener las dimensiones de la pantalla
    int screenWidth = GetSystemMetrics(SM_CXSCREEN);
    int screenHeight = GetSystemMetrics(SM_CYSCREEN);

    // Calcular las coordenadas para centrar la ventana
    int x = (screenWidth - width) / 2;
    int y = (screenHeight - height) / 2;

    // Crear la ventana
    HWND hwnd = CreateWindowExW(0, L"InputDialogClass", L"Input",
        WS_OVERLAPPEDWINDOW & ~WS_THICKFRAME & ~WS_MAXIMIZEBOX,
        x, y, width, height,
        NULL, NULL, GetModuleHandle(NULL), NULL);

    ShowWindow(hwnd, SW_SHOW);
    UpdateWindow(hwnd);

    // Bucle de mensajes
    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return inputText;
}

void showMessage(const std::string& message) {
    // Convertir std::string a std::wstring para usar con MessageBoxW
    std::wstring wMessage(message.begin(), message.end());
    MessageBoxW(NULL, wMessage.c_str(), L"Resultados", MB_OK | MB_ICONINFORMATION);
}

int main() {
    std::string baseInput, exponenteInput;
    long long base = 0, exponente = 0;

    // Obtener el tiempo inicial
    auto start = std::chrono::high_resolution_clock::now();

    while (true) {
        baseInput = promptForInput("Primer numero (base):");
        if (baseInput.empty()) {
            int result = MessageBoxW(NULL, L"¿Seguro que quiere salir del programa? (s/n)", L"Confirmar Salida", MB_YESNO | MB_ICONQUESTION);
            if (result == IDYES) {
                return 0;
            }
        }
        try {
            base = std::stoll(baseInput);
            if (base == 0) {
                showMessage("El primer número no puede ser cero. Ingrese de nuevo.");
            } else {
                break;
            }
        } catch (std::invalid_argument&) {
            showMessage("Por favor ingrese un número válido.");
        }
    }

    while (true) {
        exponenteInput = promptForInput("Segundo numero (exponente):");
        if (exponenteInput.empty()) {
            int result = MessageBoxW(NULL, L"¿Seguro que quiere salir del programa? (s/n)", L"Confirmar Salida", MB_YESNO | MB_ICONQUESTION);
            if (result == IDYES) {
                return 0;
            }
        }
        try {
            exponente = std::stoll(exponenteInput);
            break;
        } catch (std::invalid_argument&) {
            showMessage("Por favor ingrese un número valido.");
        }
    }

    std::stringstream resultados;
    for (long long i = 0; i <= exponente; i++) {
        long long resultado = 1;
        for (long long j = 1; j <= i; j++) {
            resultado *= base;
        }
        resultados << base << "^" << i << " = " << resultado << "\n";
    }

    // Obtener el tiempo final
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::nano> duration = end - start;

    std::string mensaje = resultados.str() + "Tiempo de ejecución: " + std::to_string(duration.count()) + " nanosegundos";
    showMessage(mensaje);

    return 0;
}
