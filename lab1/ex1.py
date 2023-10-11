import numpy as np
import matplotlib.pyplot as plt

def ex1():
    # a
    t = np.linspace(0, 0.03, num=int(0.03 / 0.0005) + 1)
    print(t)

    # b

    x_t = np.cos(520 * np.pi * t + np.pi/3)
    y_t = np.cos(280 * np.pi * t - np.pi/3)
    z_t = np.cos(120 * np.pi * t + np.pi/3)

    fig, axs = plt.subplots(3)
    fig.suptitle('Cele 3 semnale')

    axs[0].plot(t, x_t)
    axs[0].set_title('Semnal x(t) = cos(520πt + π/3)')

    axs[1].plot(t, y_t)
    axs[1].set_title('Semnal y(t) = cos(280πt − π/3)')

    axs[2].plot(t, z_t)
    axs[2].set_title('Semnal z(t) = cos(120πt + π/3)')

    plt.tight_layout()
    plt.show()

    # c
    fs = 200

    t_discret = np.arange(0, 0.03, 1 / fs)

    x_n = np.cos(520 * np.pi * t_discret + np.pi/3)
    y_n = np.cos(280 * np.pi * t_discret - np.pi/3)
    z_n = np.cos(120 * np.pi * t_discret + np.pi/3)

    fig, axs = plt.subplots(3)
    fig.suptitle('Cele 3 semnale mod discret')

    axs[0].stem(t_discret, x_n, use_line_collection=True)
    axs[0].set_title('Semnal x[n] eșantionat la 200 Hz')

    axs[1].stem(t_discret, y_n, use_line_collection=True)
    axs[1].set_title('Semnal y[n] eșantionat la 200 Hz')

    axs[2].stem(t_discret, z_n, use_line_collection=True)
    axs[2].set_title('Semnal z[n] eșantionat la 200 Hz')

    plt.tight_layout()
    plt.show()