# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class UpdateFlowAliasResponseBody(DaraModel):
    def __init__(
        self,
        alias: main_models.UpdateFlowAliasResponseBodyAlias = None,
        request_id: str = None,
    ):
        self.alias = alias
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.alias:
            self.alias.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            temp_model = main_models.UpdateFlowAliasResponseBodyAlias()
            self.alias = temp_model.from_map(m.get('Alias'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateFlowAliasResponseBodyAlias(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        name: str = None,
        routing_configurations: List[main_models.UpdateFlowAliasResponseBodyAliasRoutingConfigurations] = None,
    ):
        self.created_time = created_time
        self.description = description
        self.name = name
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

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.routing_configurations = []
        if m.get('RoutingConfigurations') is not None:
            for k1 in m.get('RoutingConfigurations'):
                temp_model = main_models.UpdateFlowAliasResponseBodyAliasRoutingConfigurations()
                self.routing_configurations.append(temp_model.from_map(k1))

        return self

class UpdateFlowAliasResponseBodyAliasRoutingConfigurations(DaraModel):
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

