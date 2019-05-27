import matplotlib.pyplot as plt

def grafic(temperatura,humitat):   
    dades = temperatura # Valors de les variables
    dades2=humitat
    ind=range(10) # Coordenades x
    fig, (ax1,ax2) = plt.subplots(1,2) # Numero de grafiques que dibuixem a la figura. que passa si fem fig, (ax1,ax2) = plt.subplots(2,1)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=1, hspace=None)
    
    ############################ DIAGRAMA DE BARRES HORITZONTAL###################################################################################
    rects = ax1.barh(ind, dades, align='center',color='green', ecolor='black')
    ax1.set_yticks(ind)
    ax1.set_yticklabels(('hora1', 'hora2','hora3', 'hora4','hora5', 'hora6','hora7', 'hora8','hora9', 'hora10'))
    ax1.invert_yaxis()  # labels read top-to-bottom
    ax1.set_xlabel('Temperatura') 
    ax1.set_title('Temperatures')
    for i, v in enumerate(dades):
        ax1.text(v , i, str(v), color='blue', fontweight='bold')
    ax1.xaxis.set_major_locator(plt.NullLocator())
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)

    rects2 = ax2.barh(ind, dades2, align='center',color='green', ecolor='black')
    ax2.set_yticks(ind)
    ax2.set_yticklabels(('hora1', 'hora2','hora3', 'hora4','hora5', 'hora6','hora7', 'hora8','hora9', 'hora10'))
    ax2.invert_yaxis()  # labels read top-to-bottom
    ax2.set_xlabel('Humitat') 
    ax2.set_title('Humitat2')
    for i, v in enumerate(dades2):
        ax2.text(v , i, str(v), color='blue', fontweight='bold')
    ax2.xaxis.set_major_locator(plt.NullLocator())
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)

    ########################################## GUARDAR LA FIGURA #########################################################################
    plt.savefig('prova1.png', bbox_inches='tight')
    plt.close(fig)

grafic([23,45,10,50,32,12,45,32,5,17],[50,30,28,50,60,70,20,32,54,45])