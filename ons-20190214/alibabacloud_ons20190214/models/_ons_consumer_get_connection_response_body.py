# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsConsumerGetConnectionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsConsumerGetConnectionResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.OnsConsumerGetConnectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsConsumerGetConnectionResponseBodyData(DaraModel):
    def __init__(
        self,
        connection_list: main_models.OnsConsumerGetConnectionResponseBodyDataConnectionList = None,
        message_model: str = None,
    ):
        self.connection_list = connection_list
        self.message_model = message_model

    def validate(self):
        if self.connection_list:
            self.connection_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_list is not None:
            result['ConnectionList'] = self.connection_list.to_map()

        if self.message_model is not None:
            result['MessageModel'] = self.message_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionList') is not None:
            temp_model = main_models.OnsConsumerGetConnectionResponseBodyDataConnectionList()
            self.connection_list = temp_model.from_map(m.get('ConnectionList'))

        if m.get('MessageModel') is not None:
            self.message_model = m.get('MessageModel')

        return self

class OnsConsumerGetConnectionResponseBodyDataConnectionList(DaraModel):
    def __init__(
        self,
        connection_do: List[main_models.OnsConsumerGetConnectionResponseBodyDataConnectionListConnectionDo] = None,
    ):
        self.connection_do = connection_do

    def validate(self):
        if self.connection_do:
            for v1 in self.connection_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnectionDo'] = []
        if self.connection_do is not None:
            for k1 in self.connection_do:
                result['ConnectionDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_do = []
        if m.get('ConnectionDo') is not None:
            for k1 in m.get('ConnectionDo'):
                temp_model = main_models.OnsConsumerGetConnectionResponseBodyDataConnectionListConnectionDo()
                self.connection_do.append(temp_model.from_map(k1))

        return self

class OnsConsumerGetConnectionResponseBodyDataConnectionListConnectionDo(DaraModel):
    def __init__(
        self,
        client_addr: str = None,
        client_id: str = None,
        language: str = None,
        version: str = None,
    ):
        self.client_addr = client_addr
        self.client_id = client_id
        self.language = language
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.language is not None:
            result['Language'] = self.language

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

