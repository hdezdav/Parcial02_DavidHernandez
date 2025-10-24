# Microservicio de Factorial en Flask

### Pregunta
Como modificaria el diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de calculos en una base de datos externa?

### Respuesta

Para integrar un servicio de historial externo trataria de usar una cola como en AWS, para que este no interfiriera con las solicitudes del usuario.
Configurandolo de forma asincrona; publicando un evento el cual apenas termine, se envie la informacion del servicio para que se guarde en la base de datos, asi no se afecta la respuesta en caso de que falle el servicio del historial, que es la ventaja de usar microservicios.
