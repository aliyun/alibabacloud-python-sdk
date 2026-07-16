# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RealtimeDialogAssistResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.RealtimeDialogAssistResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        # Time consumed
        self.cost = cost
        # Response data
        self.data = data
        # Data type
        self.data_type = data_type
        # Error code
        self.err_code = err_code
        # Error message
        self.message = message
        # Request ID. This is the system-recorded request ID. If issues arise, provide this ID to the Model Studio DianJin R\\&D team for troubleshooting.
        self.request_id = request_id
        # Whether successful
        self.success = success
        # Timestamp
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('data') is not None:
            temp_model = main_models.RealtimeDialogAssistResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class RealtimeDialogAssistResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis_process: str = None,
        assist_scripts: List[main_models.RealtimeDialogAssistResponseBodyDataAssistScripts] = None,
        assist_sop: List[main_models.RealtimeDialogAssistResponseBodyDataAssistSop] = None,
        conversation_model: List[main_models.RealtimeDialogAssistResponseBodyDataConversationModel] = None,
        interrupt: bool = None,
        request_id: str = None,
        session_id: str = None,
    ):
        # Analysis process
        self.analysis_process = analysis_process
        # List of dialog assist results
        self.assist_scripts = assist_scripts
        # List of flow assist results
        self.assist_sop = assist_sop
        # Current dialog content
        self.conversation_model = conversation_model
        # Whether interrupted
        self.interrupt = interrupt
        # Unique request ID. This request ID matches the request ID in the input parameter.
        self.request_id = request_id
        # Session ID
        self.session_id = session_id

    def validate(self):
        if self.assist_scripts:
            for v1 in self.assist_scripts:
                 if v1:
                    v1.validate()
        if self.assist_sop:
            for v1 in self.assist_sop:
                 if v1:
                    v1.validate()
        if self.conversation_model:
            for v1 in self.conversation_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process

        result['assistScripts'] = []
        if self.assist_scripts is not None:
            for k1 in self.assist_scripts:
                result['assistScripts'].append(k1.to_map() if k1 else None)

        result['assistSop'] = []
        if self.assist_sop is not None:
            for k1 in self.assist_sop:
                result['assistSop'].append(k1.to_map() if k1 else None)

        result['conversationModel'] = []
        if self.conversation_model is not None:
            for k1 in self.conversation_model:
                result['conversationModel'].append(k1.to_map() if k1 else None)

        if self.interrupt is not None:
            result['interrupt'] = self.interrupt

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')

        self.assist_scripts = []
        if m.get('assistScripts') is not None:
            for k1 in m.get('assistScripts'):
                temp_model = main_models.RealtimeDialogAssistResponseBodyDataAssistScripts()
                self.assist_scripts.append(temp_model.from_map(k1))

        self.assist_sop = []
        if m.get('assistSop') is not None:
            for k1 in m.get('assistSop'):
                temp_model = main_models.RealtimeDialogAssistResponseBodyDataAssistSop()
                self.assist_sop.append(temp_model.from_map(k1))

        self.conversation_model = []
        if m.get('conversationModel') is not None:
            for k1 in m.get('conversationModel'):
                temp_model = main_models.RealtimeDialogAssistResponseBodyDataConversationModel()
                self.conversation_model.append(temp_model.from_map(k1))

        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

class RealtimeDialogAssistResponseBodyDataConversationModel(DaraModel):
    def __init__(
        self,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        role: str = None,
        type: str = None,
    ):
        # Specific content of the dialog
        self.content = content
        # Unique identity of the dialog role
        self.customer_id = customer_id
        # Customer service ID
        self.customer_service_id = customer_service_id
        # Agent type. 0: Robot, 1: Human.
        self.customer_service_type = customer_service_type
        # Role. 0 indicates customer, 1 indicates agent.
        self.role = role
        # Type of dialog content
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id

        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type

        if self.role is not None:
            result['role'] = self.role

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')

        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class RealtimeDialogAssistResponseBodyDataAssistSop(DaraModel):
    def __init__(
        self,
        assist_sop: str = None,
        intent_code: str = None,
        intent_name: str = None,
        is_default: bool = None,
    ):
        # Recommended flow
        self.assist_sop = assist_sop
        # Intent encoding
        self.intent_code = intent_code
        # Intent name
        self.intent_name = intent_name
        # Indicates whether the intent is to escape.
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assist_sop is not None:
            result['assistSop'] = self.assist_sop

        if self.intent_code is not None:
            result['intentCode'] = self.intent_code

        if self.intent_name is not None:
            result['intentName'] = self.intent_name

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistSop') is not None:
            self.assist_sop = m.get('assistSop')

        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')

        if m.get('intentName') is not None:
            self.intent_name = m.get('intentName')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        return self

class RealtimeDialogAssistResponseBodyDataAssistScripts(DaraModel):
    def __init__(
        self,
        assist_script: str = None,
        intent_code: str = None,
        intent_labels: str = None,
        intent_name: str = None,
        is_default: bool = None,
    ):
        # Recommended utterance
        self.assist_script = assist_script
        # Intent encoding
        self.intent_code = intent_code
        # Intent labels
        self.intent_labels = intent_labels
        # Intent name
        self.intent_name = intent_name
        # Whether intent escaped
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assist_script is not None:
            result['assistScript'] = self.assist_script

        if self.intent_code is not None:
            result['intentCode'] = self.intent_code

        if self.intent_labels is not None:
            result['intentLabels'] = self.intent_labels

        if self.intent_name is not None:
            result['intentName'] = self.intent_name

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistScript') is not None:
            self.assist_script = m.get('assistScript')

        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')

        if m.get('intentLabels') is not None:
            self.intent_labels = m.get('intentLabels')

        if m.get('intentName') is not None:
            self.intent_name = m.get('intentName')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        return self

