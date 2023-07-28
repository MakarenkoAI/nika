Данный агент выполняет классификацию сообщений по темам (приветствие, про условия лабораторной работы, про сущность и т.д.).
Кроме того, агент классифицирует сообщение по признакам (нейтральная, позитивная, отрицательная эмоциональная окраска) и получает сущности сообщения.
Агент классифицирует сообщение с помощью Wit.ai.

**Класс действий:**

`action_message_topic_classification`

**Параметры:**

1. `message node` - принадлежит `concept_message`;

**Используемые библиотеки:**

* [Wit.ai](https://wit.ai/) - для классификации сообщений и получения сущностей.

**Комментарий:**

* Входное сообщение должно содержать текстовый файл с текстом на русском языке;
* Исключаемая сущность должна быть формализованна в базе знаний.

### Пример

Пример вводимой структуры:

<img src="../images/messageTopicClassificationAgentInput.png"></img>

Пример выводимой структуры:
<img src="../images/messageTopicClassificationAgentOutput.png"></img>

Пример структуры, необходимой для классификации сообщения по цели:

<img src="../images/messageTopicClassificationAgentIntentFormalization.png"></img>

Пример структуры, необходимой для классификации сообщения по признакам:

<img src="../images/messageTopicClassificationAgentTraitFormalization.png"></img>

Пример структуры, необходимой для получения сущностей сообщения:

<img src="../images/messageTopicClassificationAgentEntityFormalization.png"></img>

**Классы для messages:**

1. `concept_greeting_message`
2. `concept_message_about_entity`
3. `concept_message_about_lab_work_condition`
4. `concept_message_about_lab_work_deadline`

### Язык реализации агента
C++

### Итог

Возможные результаты:

* `SC_RESULT_OK` - сообщение успешно классифицировано (или произошла пустая классификация) или действие не принадлежит action_message_topic_classification.
* `SC_RESULT_ERROR`- внутренняя ошибка.
