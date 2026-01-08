# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetWhatsappHealthStatusResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetWhatsappHealthStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetWhatsappHealthStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetWhatsappHealthStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        can_send_message: str = None,
        entities: List[main_models.GetWhatsappHealthStatusResponseBodyDataEntities] = None,
    ):
        # Indicates whether the messages can be sent.
        self.can_send_message = can_send_message
        # The queried entities.
        self.entities = entities

    def validate(self):
        if self.entities:
            for v1 in self.entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_send_message is not None:
            result['CanSendMessage'] = self.can_send_message

        result['Entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['Entities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSendMessage') is not None:
            self.can_send_message = m.get('CanSendMessage')

        self.entities = []
        if m.get('Entities') is not None:
            for k1 in m.get('Entities'):
                temp_model = main_models.GetWhatsappHealthStatusResponseBodyDataEntities()
                self.entities.append(temp_model.from_map(k1))

        return self

class GetWhatsappHealthStatusResponseBodyDataEntities(DaraModel):
    def __init__(
        self,
        business_id: str = None,
        can_send_message: str = None,
        entity_type: str = None,
        errors: List[main_models.GetWhatsappHealthStatusResponseBodyDataEntitiesErrors] = None,
        language: str = None,
        phone_number: str = None,
        template_code: str = None,
        waba_id: str = None,
    ):
        # The Business Manager ID.
        self.business_id = business_id
        # Indicates whether the messages can be sent.
        self.can_send_message = can_send_message
        # The entity type.
        self.entity_type = entity_type
        # The reasons why the messages failed to be sent.
        self.errors = errors
        # The template language.
        self.language = language
        # The phone number to which the messages are sent.
        self.phone_number = phone_number
        # The template code. This parameter is returned when the NodeType parameter is set to **template**.
        self.template_code = template_code
        # The WABA ID. You can view the WABA ID in the Chat App Message Service console after you create the WABA.
        self.waba_id = waba_id

    def validate(self):
        if self.errors:
            for v1 in self.errors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.can_send_message is not None:
            result['CanSendMessage'] = self.can_send_message

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        result['Errors'] = []
        if self.errors is not None:
            for k1 in self.errors:
                result['Errors'].append(k1.to_map() if k1 else None)

        if self.language is not None:
            result['Language'] = self.language

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.waba_id is not None:
            result['WabaId'] = self.waba_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('CanSendMessage') is not None:
            self.can_send_message = m.get('CanSendMessage')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        self.errors = []
        if m.get('Errors') is not None:
            for k1 in m.get('Errors'):
                temp_model = main_models.GetWhatsappHealthStatusResponseBodyDataEntitiesErrors()
                self.errors.append(temp_model.from_map(k1))

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')

        return self

class GetWhatsappHealthStatusResponseBodyDataEntitiesErrors(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_description: str = None,
        possible_solution: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The description of the error.
        self.error_description = error_description
        # The possible solution to the error.
        self.possible_solution = possible_solution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_description is not None:
            result['ErrorDescription'] = self.error_description

        if self.possible_solution is not None:
            result['PossibleSolution'] = self.possible_solution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorDescription') is not None:
            self.error_description = m.get('ErrorDescription')

        if m.get('PossibleSolution') is not None:
            self.possible_solution = m.get('PossibleSolution')

        return self

