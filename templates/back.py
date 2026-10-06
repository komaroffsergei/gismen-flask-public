# import os
# from google.cloud import dialogflow_v2beta1 as dialogflow
# from google.api_core.exceptions import InvalidArgument
#
# from common.df import create_entity_type, get_entities_list
#
# from flask import Flask, request, make_response, jsonify, render_template
#
# app = Flask(__name__)
#
#
# # session_client = dialogflow.SessionsClient()
# # session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'gismen-dev-caxv-a612ec97f4e4.json'
#
#     DIALOGFLOW_PROJECT_ID = 'gismen-dev-caxv'
#     DIALOGFLOW_LANGUAGE_CODE = 'ru'
#     SESSION_ID = 'me'
#     # if request.method == 'POST':
#     #     if request.form.get('create_entity') == 'CREATE ENTITY':
#     #         return render_template('./home/0.html')
#     #         pass
#     #         # create_entity(conf.PROJECT_REALESTATE_ID, 'KIND_MAP', 'bot_new_entity', )
#     #     elif request.form.get('create_entity_type') == 'CREATE ENTITY TYPE':
#     #         # create_entity_type(conf.PROJECT_REALESTATE_ID, 'bot_new_entity', 'KIND_MAP')
#     #         return render_template('./home/0.html')
#     #         pass  # do something else
#     #     elif request.form.get('create_key') == 'CREATE KEY':
#     #         create_key('init.reg@gmail.com')
#     #     else:
#     #         pass  # unknown
#     # elif request.method == 'GET':
#     #     return render_template('./home/0.html')
#     l = get_entities_list(DIALOGFLOW_PROJECT_ID)
#
#     print(l)
#     return render_template("./home/0.html", entities=[])
#
#
# # function for responses
# def results():
#     # build a request object
#     req = request.get_json(force=True)
#     # fetch action from json
#     action = req.get('queryResult').get('action')
#     # return a fulfillment response
#     return {'fulfillmentText': 'This is a response from webhook.'}
#
#
# # create a route for webhook
# @app.route('/wh/realestate', methods=['GET', 'POST'])
# def webhook():
#     # return response
#     return make_response(jsonify(results()))
#
#
# # run the app
# if __name__ == '__main__':
#     app.debug = True
#     app.run()
#
# ### TEST INTENT ###
# # text_to_be_analyzed = "Хочу купить"
# # text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
# # query_input = dialogflow.types.QueryInput(text=text_input)
# # try:
# #     response = session_client.detect_intent(session=session, query_input=query_input)
# # except InvalidArgument:
# #     raise
# #
# # print("Query text:", response.query_result.query_text)
# # print("Detected intent:", response.query_result.intent.display_name)
# # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
# # print("Fulfillment text:", response.query_result.fulfillment_text)
#
# ### END TEST INTENT
#
# ### CREATE ENTITY TYPE
#
# # Create a client
# # client = dialogflow.EntityTypesClient()
# #
# # # Initialize request argument(s)
# # entity_type = dialogflow.EntityType()
# # entity_type.display_name = "display_name_value"
# # entity_type.kind = "KIND_REGEXP"
# #
# # request = dialogflow.CreateEntityTypeRequest(
# #     parent='projects/'+DIALOGFLOW_PROJECT_ID+'/agent',
# #     entity_type=entity_type,
# # )
# #
# # # Make the request
# # response = client.create_entity_type(request=request)
# #
# # # Handle the response
# # print(response)
#
# ### END CREATE ENTITY
#
#
# # import os
# # # from common import dialogflow
# # # from google.api_core.exceptions import InvalidArgument
# # from google.api_core.exceptions import InvalidArgument
# # from google.cloud import dialogflow_v2
# #
# # from common.df import create_entity_type
# #
# # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'gismen-dev-gger-725ebef1ce0c.json'
# #
# # DIALOGFLOW_PROJECT_ID = 'gismen-dev-caxv'
# # DIALOGFLOW_LANGUAGE_CODE = 'ru'
# # SESSION_ID = 'me'
# #
# # text_to_be_analyzed = "Хочу купить"
# #
# # session_client = dialogflow_v2.SessionsClient()
# # session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
# # text_input = dialogflow_v2.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
# # query_input = dialogflow_v2.types.QueryInput(text=text_input)
# # print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
# # print('!!!!!!!!!!')
# #
# # create_entity_type(DIALOGFLOW_PROJECT_ID, 'bot_new_entity', 'KIND_MAP')
# # try:
# #     response = session_client.detect_intent(session=session, query_input=query_input)
# # except InvalidArgument:
# #     raise
# #
# # print("Query text:", response.query_result.query_text)
# # print("Detected intent:", response.query_result.intent.display_name)
# # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
# # print("Fulfillment text:", response.query_result.fulfillment_text)
# #
# #
# #
# # # import os
# # #
#
# # #
# # # # initialize the flask app
# # # import conf
# # # from common.lib import create_entity_type
# # #
# # # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gismen-realestate-33e24e6f5c53.json"
#
# # #
# # # from google.oauth2 import service_account
# # # import googleapiclient.discovery
# # #
# # #
# # # def create_key(service_account_email):
# # #     """Creates a key for a service account."""
# # #
# # #     credentials = service_account.Credentials.from_service_account_file(
# # #         filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
# # #         scopes=['https://www.googleapis.com/auth/cloud-platform'])
# # #
# # #     service = googleapiclient.discovery.build(
# # #         'iam', 'v1', credentials=credentials)
# # #
# # #     key = service.projects().serviceAccounts().keys().create(
# # #         name='projects/-/serviceAccounts/' + service_account_email, body={}
# # #     ).execute()
# # #
# # #     # The privateKeyData field contains the base64-encoded service account key
# # #     # in JSON format.
# # #     # TODO(Developer): Save the below key {json_key_file} to a secure location.
# # #     #  You cannot download it again later.
# # #     # import base64
# # #     # json_key_file = base64.b64decode(key['privateKeyData']).decode('utf-8')
# # #
# # #     if not key['disabled']:
# # #         print('Created json key')
# # #
# # #
# # default route
# # import conf
