# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetModelProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetModelProviderResponseBodyData = None,
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
            temp_model = main_models.GetModelProviderResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetModelProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        address: str = None,
        api_keys: List[str] = None,
        create_time: str = None,
        deploy_status: str = None,
        description: str = None,
        id: str = None,
        instance_id: str = None,
        name: str = None,
        protocols: List[str] = None,
        provider: str = None,
        region_id: str = None,
    ):
        self.address = address
        self.api_keys = api_keys
        self.create_time = create_time
        self.deploy_status = deploy_status
        self.description = description
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.protocols = protocols
        self.provider = provider
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.api_keys is not None:
            result['ApiKeys'] = self.api_keys

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('ApiKeys') is not None:
            self.api_keys = m.get('ApiKeys')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

