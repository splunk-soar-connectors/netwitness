# --
# File: netwitness_consts.py
#
# Copyright (c) Phantom Cyber Corporation, 2017
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber Corporation.
#
# --

NETWITNESS_ERR_BAD_RANGE = 'Session ID parameter has a bad range - smaller number should come first'
NETWITNESS_ERR_BAD_PARAMS = 'This action requires a session ID, query, or start and end times'
NETWITNESS_ERR_REVERSE_TIMES = 'Given time range is invalid - times appear to be reversed'
NETWITNESS_ERR_VAULT_INFO = "Unable to get Vault item details from Phantom. Details: {0}"
NETWITNESS_ERR_FROM_SERVER = 'API failed\nStatus code: {status}\nDetail: {detail}'
NETWITNESS_ERR_TIMEOUT = 'Request timed out. Try limiting the scope of the search'
NETWITNESS_ERR_BAD_CAP = 'Found no capture data based on the given parameters'
NETWITNESS_ERR_NOT_IN_VAULT = 'Specified vault ID not found in vault'
NETWITNESS_ERR_API_UNSUPPORTED_METHOD = 'Unsupported method {method}'
NETWITNESS_ERR_SERVER_CONNECTION = 'Connection failed'
NETWITNESS_ERR_VAULT = 'Could not move file to vault'

NETWITNESS_GET_PCAPS_FAIL = 'Response from server was incorrect data type'
NETWITNESS_CONNECTION_TEST_MSG = 'Querying endpoint to test connectivity'
NETWITNESS_REPORT_ALREADY_AVAILABLE = 'Report already available in vault'
NETWITNESS_CAP_TYPE_DICT = {'log': 'application/json', 'pcap': 'pcap'}
NETWITNESS_SUCC_FILE_ADD_TO_VAULT = 'Successfully added file to Vault'
NETWITNESS_SUCC_UPLOAD = 'Feed/Parser file successfully uploaded'
NETWITNESS_FILE_TYPE_DICT = {'pcap': 'pcap', 'log': 'json'}
NETWITNESS_INVALID_PARAM = 'Invalid parameters: {message}'
NETWITNESS_EXCEPTION_OCCURRED = 'Exception occurred'
NETWITNESS_FILE_ERROR = 'Error while creating file'
NETWITNESS_ENDPOINT_GET_CAP = '/sdk/packets'

NETWITNESS_REST_RESP_UNAUTHORIZED_MSG = 'Invalid username or password'
NETWITNESS_REST_RESP_RESOURCE_NOT_FOUND_MSG = 'No data found'
NETWITNESS_REST_RESP_OTHER_ERR_MSG = 'Unknown error occurred'
NETWITNESS_REST_RESP_BAD_REQUEST_MSG = 'Bad Request'
NETWITNESS_REST_RESP_RESOURCE_NOT_FOUND = 404
NETWITNESS_REST_RESP_UNAUTHORIZED = 401
NETWITNESS_REST_RESP_BAD_REQUEST = 400
NETWITNESS_REST_RESP_SUCCESS = 200

NETWITNESS_TEST_CONNECTIVITY_PASS = 'Connectivity test succeeded'
NETWITNESS_TEST_CONNECTIVITY_FAIL = 'Connectivity test failed'

NETWITNESS_CONFIG_VERIFY = 'verify_server_cert'
NETWITNESS_CONFIG_API_USERNAME = 'username'
NETWITNESS_CONFIG_API_PASSWORD = 'password'
NETWITNESS_CONFIG_SERVER = 'url'

NETWITNESS_JSON_START_TIME = 'start_time'
NETWITNESS_JSON_SESSION_ID = 'session_ids'
NETWITNESS_JSON_FILE_NAME = 'file_name'
NETWITNESS_JSON_END_TIME = 'end_time'
NETWITNESS_JSON_QUERY = 'query'

NETWITNESS_DEFAULT_REST_TIMEOUT = 300
NETWITNESS_DEFAULT_TEST_TIMEOUT = 30

NETWITNESS_CAP_TYPE_PACKET = 'pcap'
NETWITNESS_CAP_TYPE_LOG = 'log'

NETWITNESS_BAD_CAP_HASHES = [ '2d59f05b63bda3d74db5685834e137911c7279f282f0d595ac465fd3b97e348f',
                              '8eba672603c531f466c75ca729b66378b92271d78ef1570574757cd5fd8244e6']
NETWITNESS_BAD_CAP_SIZES = [ 77, 41 ]
