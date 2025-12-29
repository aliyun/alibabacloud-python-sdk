# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class AppStackInstance(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        endpoints: List[main_models.AppStackInstanceEndpoints] = None,
        instance_id: str = None,
        instance_name: str = None,
        parameters: List[main_models.AppStackInstanceParameters] = None,
        stack_id: str = None,
        status: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.endpoints = endpoints
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.parameters = parameters
        self.stack_id = stack_id
        self.status = status
        self.update_time = update_time

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.AppStackInstanceEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.AppStackInstanceParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class AppStackInstanceParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self



class AppStackInstanceEndpoints(DaraModel):
    def __init__(
        self,
        address: str = None,
        name: str = None,
        protocol: str = None,
    ):
        self.address = address
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

