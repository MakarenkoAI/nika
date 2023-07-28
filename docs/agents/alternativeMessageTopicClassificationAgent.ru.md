Это агент, который выполняет классификацию сообщений, используя [логические правила](../subsystems/scl-machine.md).

**Класс действий:**

`action_alternative_message_topic_classification`

**Параметры:**

1. `message node` - принадлежит `concept_message`;

### Пример

Пример вводимой структуры:

<img src="../images/alternativeMessageTopicClassificationAgentInput.png"></img>

Пример логической формулы для классификации агента:

<img src="../images/lr_greeting_message.png"></img>

Результат работы агента зависит от результатов агента вывода. Если какая-либо формула была применена успешно, то `message node` имеет класс согласно формуле.
В противном случае, `message node` принадлежит классу `concept_not_classified_by_intent_message`.

### Язык реализации агента
C++

### Итог

Возможные результаты:

* `SC_RESULT_OK` - сообщение успешно классифицировано (или произошла пустая классификация) или действие не принадлежит action_message_topic_classification.
* `SC_RESULT_ERROR`- внутренняя ошибка.
