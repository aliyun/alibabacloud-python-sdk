# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class CreateFlowAliasResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        flow_name: str = None,
        name: str = None,
        request_id: str = None,
        routing_configurations: List[main_models.CreateFlowAliasResponseBodyRoutingConfigurations] = None,
    ):
        self.created_time = created_time
        self.description = description
        self.flow_name = flow_name
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.routing_configurations = routing_configurations

    def validate(self):
        if self.routing_configurations:
            for v1 in self.routing_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RoutingConfigurations'] = []
        if self.routing_configurations is not None:
            for k1 in self.routing_configurations:
                result['RoutingConfigurations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.routing_configurations = []
        if m.get('RoutingConfigurations') is not None:
            for k1 in m.get('RoutingConfigurations'):
                temp_model = main_models.CreateFlowAliasResponseBodyRoutingConfigurations()
                self.routing_configurations.append(temp_model.from_map(k1))

        return self

class CreateFlowAliasResponseBodyRoutingConfigurations(DaraModel):
    def __init__(
        self,
        version: str = None,
        weight: int = None,
    ):
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version is not None:
            result['Version'] = self.version

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

