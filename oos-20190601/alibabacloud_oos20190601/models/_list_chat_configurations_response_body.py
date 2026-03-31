# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListChatConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        chat_configurations: List[main_models.ListChatConfigurationsResponseBodyChatConfigurations] = None,
        request_id: str = None,
    ):
        self.chat_configurations = chat_configurations
        self.request_id = request_id

    def validate(self):
        if self.chat_configurations:
            for v1 in self.chat_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChatConfigurations'] = []
        if self.chat_configurations is not None:
            for k1 in self.chat_configurations:
                result['ChatConfigurations'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chat_configurations = []
        if m.get('ChatConfigurations') is not None:
            for k1 in m.get('ChatConfigurations'):
                temp_model = main_models.ListChatConfigurationsResponseBodyChatConfigurations()
                self.chat_configurations.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListChatConfigurationsResponseBodyChatConfigurations(DaraModel):
    def __init__(
        self,
        created_date: str = None,
        name: str = None,
        outputs: str = None,
        ram_role: str = None,
        type: str = None,
        updated_date: str = None,
    ):
        self.created_date = created_date
        self.name = name
        self.outputs = outputs
        self.ram_role = ram_role
        self.type = type
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.type is not None:
            result['Type'] = self.type

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        return self

