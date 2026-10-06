from html import entities

import google.cloud.dialogflow_v2 as dialogflow_v2

# from google.cloud import dialogflow_v2beta1 as dialogflow








async def create_entities():
    # Create a client
    client = dialogflow_v2.EntityTypesAsyncClient()

    # Initialize request argument(s)
    entities = dialogflow_v2.Entity()
    entities.value = "value_value"
    entities.synonyms = ['synonyms_value_1', 'synonyms_value_2']

    request = dialogflow_v2.BatchCreateEntitiesRequest(
        parent="parent_value",
        entities=entities,
    )

    # Make the request
    operation = client.batch_create_entities(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

## create entity
def create_entity_type(project_id, display_name, kind):
    # Create a client
    client = dialogflow_v2.EntityTypesClient()

    # Initialize request argument(s)
    entity_type = dialogflow_v2.EntityType()
    entity_type.display_name = display_name
    entity_type.kind = kind

    request = dialogflow_v2.CreateEntityTypeRequest(
        parent=project_id,
        entity_type=entity_type,
    )

    # Make the request
    response = client.create_entity_type(request=request)

    # Handle the response
    print(response)

## find intent
def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""


    session_client = dialogflow_v2.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow_v2.TextInput(text=text, language_code=language_code)

        query_input = dialogflow_v2.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))


# Helper to get intent from display name.
# find intent by display name
def _get_intent_ids(project_id, display_name):
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    intents = intents_client.list_intents(request={"parent": parent})
    intent_names = [
        intent.name for intent in intents if intent.display_name == display_name
    ]

    intent_ids = [intent_name.split("/")[-1] for intent_name in intent_names]

    return intent_ids


# Get list of entities
def get_entity_types_list(project_id):
    # Create a client
    client = dialogflow_v2.EntityTypesClient()

    # Initialize request argument(s)
    request = dialogflow_v2.ListEntityTypesRequest(
        parent=project_id,
    )

    # Make the request
    page_result = client.list_entity_types(request=request)

    return page_result
    # Handle the response
    # for response in page_result:
    #     print(response)

# Get entity type by name
def get_entity_type(name):
    # Create a client
    client = dialogflow_v2.EntityTypesClient()

    # Initialize request argument(s)
    request = dialogflow_v2.GetEntityTypeRequest(
        name=name,
    )

    # Make the request
    return client.get_entity_type(request=request)


def get_intents_list(name):
    # Create a client
    client = dialogflow_v2.IntentsClient()

    # Initialize request argument(s)
    request = dialogflow_v2.ListIntentsRequest(
        parent=name,
    )

    return client.list_intents(request=request)


# update entity
def update_entity(parent, entity_value, synonyms):
    # Create a client
    client = dialogflow_v2.EntityTypesClient()
    synonyms = synonyms or [entity_value]
    # Initialize request argument(s)
    entity = dialogflow_v2.EntityType.Entity(
        value=entity_value,
        synonyms=synonyms
    )
    # entity.value = entity_value
    #
    # entity.synonyms.extend(synonyms)
    print('!!!!!_____',parent, entity)
    request = dialogflow_v2.BatchUpdateEntitiesRequest(
        parent=parent,
        entities=[{'value': entity_value, 'synonyms': synonyms}]
    )

    # Make the request
    operation = client.batch_update_entities(request)

    print("Waiting for operation to complete...", entity)

    print('asdADad', operation.result())
    return operation.result()



def sample_batch_update_entities():
    from google.cloud import dialogflow_v2beta1
    # Create a client
    client = dialogflow_v2beta1.EntityTypesClient()

    # Initialize request argument(s)
    entities = dialogflow_v2beta1.Entity()
    entities.value = "value_value"

    request = dialogflow_v2beta1.BatchUpdateEntitiesRequest(
        parent="parent_value",
        entities=entities,
    )

    # Make the request
    operation = client.batch_update_entities(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# async def create_entity_type(project_id, display_name, kind):
#     # Create a client
#     client = dialogflow_v2.EntityTypesAsyncClient()
#
#     # Initialize request argument(s)
#     entity_type = dialogflow_v2.EntityType()
#     entity_type.display_name = display_name
#     entity_type.kind = kind
#
#     request = dialogflow_v2.CreateEntityTypeRequest(
#         parent=project_id,
#         entity_type=entity_type,
#     )
#
#     # Make the request
#     response = await client.create_entity_type(request=request)
#
#     # Handle the response
#     print(response)

# def create_entity(project_id, entity_type_id, entity_value, synonyms):
#     """Create an entity of the given entity type."""
#     # import dialogflow_v2 as common
#     entity_types_client = common.EntityTypesClient()
#
#     # Note: synonyms must be exactly [entity_value] if the
#     # entity_type's kind is KIND_LIST
#     synonyms = synonyms or [entity_value]
#
#     entity_type_path = entity_types_client.entity_type_path(
#         project_id, entity_type_id)
#
#     entity = common.types.EntityType.Entity()
#     entity.value = entity_value
#     entity.synonyms.extend(synonyms)
#
#     response = entity_types_client.batch_create_entities(
#         entity_type_path, [entity])
#
#     print('Entity created: {}'.format(response))

#
# def create_entity_type(project_id, display_name, kind):
#     """Create an entity type with the given display name."""
#     entity_types_client = common.EntityTypesClient()
#
#     parent = common.AgentsClient.agent_path(project_id)
#     entity_type = common.types.EntityType(
#         display_name=display_name, kind=kind)
#
#     response = entity_types_client.create_entity_type(parent, entity_type)
#
#     print('Entity type created: \n{}'.format(response))


    #
    # user = get_user_by_id(id)
    # post = get_user_post_by_id(user, id)