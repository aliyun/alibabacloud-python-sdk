# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliyunauth20181222 import models as main_models
from darabonba.model import DaraModel

class AuthenticateResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.AuthenticateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AuthenticateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AuthenticateResponseBodyData(DaraModel):
    def __init__(
        self,
        authorized: bool = None,
        instance_id: str = None,
        operate_code: str = None,
        product_code: str = None,
        record_vid: str = None,
        user_input_list: main_models.AuthenticateResponseBodyDataUserInputList = None,
    ):
        self.authorized = authorized
        self.instance_id = instance_id
        self.operate_code = operate_code
        self.product_code = product_code
        self.record_vid = record_vid
        self.user_input_list = user_input_list

    def validate(self):
        if self.user_input_list:
            self.user_input_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized is not None:
            result['Authorized'] = self.authorized

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operate_code is not None:
            result['OperateCode'] = self.operate_code

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.record_vid is not None:
            result['RecordVid'] = self.record_vid

        if self.user_input_list is not None:
            result['UserInputList'] = self.user_input_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperateCode') is not None:
            self.operate_code = m.get('OperateCode')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RecordVid') is not None:
            self.record_vid = m.get('RecordVid')

        if m.get('UserInputList') is not None:
            temp_model = main_models.AuthenticateResponseBodyDataUserInputList()
            self.user_input_list = temp_model.from_map(m.get('UserInputList'))

        return self

class AuthenticateResponseBodyDataUserInputList(DaraModel):
    def __init__(
        self,
        query_auth_rsdto: List[main_models.AuthenticateResponseBodyDataUserInputListQueryAuthRSDTO] = None,
    ):
        self.query_auth_rsdto = query_auth_rsdto

    def validate(self):
        if self.query_auth_rsdto:
            for v1 in self.query_auth_rsdto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QueryAuthRSDTO'] = []
        if self.query_auth_rsdto is not None:
            for k1 in self.query_auth_rsdto:
                result['QueryAuthRSDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_auth_rsdto = []
        if m.get('QueryAuthRSDTO') is not None:
            for k1 in m.get('QueryAuthRSDTO'):
                temp_model = main_models.AuthenticateResponseBodyDataUserInputListQueryAuthRSDTO()
                self.query_auth_rsdto.append(temp_model.from_map(k1))

        return self



class AuthenticateResponseBodyDataUserInputListQueryAuthRSDTO(DaraModel):
    def __init__(
        self,
        content: str = None,
        expand_content: str = None,
        field_name: str = None,
        field_vid: str = None,
    ):
        self.content = content
        self.expand_content = expand_content
        self.field_name = field_name
        self.field_vid = field_vid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.expand_content is not None:
            result['ExpandContent'] = self.expand_content

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_vid is not None:
            result['FieldVid'] = self.field_vid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ExpandContent') is not None:
            self.expand_content = m.get('ExpandContent')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldVid') is not None:
            self.field_vid = m.get('FieldVid')

        return self

