# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ResetApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ResetApiKeyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        # Id of the request
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
        if m.get('Data') is not None:
            temp_model = main_models.ResetApiKeyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ResetApiKeyResponseBodyData(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        custom_key_list: List[main_models.ResetApiKeyResponseBodyDataCustomKeyList] = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.custom_key_list = custom_key_list

    def validate(self):
        if self.custom_key_list:
            for v1 in self.custom_key_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        result['CustomKeyList'] = []
        if self.custom_key_list is not None:
            for k1 in self.custom_key_list:
                result['CustomKeyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        self.custom_key_list = []
        if m.get('CustomKeyList') is not None:
            for k1 in m.get('CustomKeyList'):
                temp_model = main_models.ResetApiKeyResponseBodyDataCustomKeyList()
                self.custom_key_list.append(temp_model.from_map(k1))

        return self

class ResetApiKeyResponseBodyDataCustomKeyList(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        key_name: str = None,
    ):
        self.api_key = api_key
        self.key_name = key_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        return self

