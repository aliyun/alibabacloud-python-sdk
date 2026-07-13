# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class CreateModelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateModelResponseBodyData = None,
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
            temp_model = main_models.CreateModelResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateModelResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        id: str = None,
        instance_id: str = None,
        name: str = None,
        protocols: List[str] = None,
        provider: str = None,
        provider_name: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.protocols = protocols
        self.provider = provider
        self.provider_name = provider_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

