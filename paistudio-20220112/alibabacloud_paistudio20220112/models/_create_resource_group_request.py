# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class CreateResourceGroupRequest(DaraModel):
    def __init__(
        self,
        computing_resource_provider: str = None,
        description: str = None,
        name: str = None,
        resource_type: str = None,
        tag: List[main_models.CreateResourceGroupRequestTag] = None,
        user_vpc: main_models.UserVpc = None,
        version: str = None,
    ):
        self.computing_resource_provider = computing_resource_provider
        self.description = description
        self.name = name
        self.resource_type = resource_type
        self.tag = tag
        self.user_vpc = user_vpc
        self.version = version

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.computing_resource_provider is not None:
            result['ComputingResourceProvider'] = self.computing_resource_provider

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingResourceProvider') is not None:
            self.computing_resource_provider = m.get('ComputingResourceProvider')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateResourceGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserVpc') is not None:
            temp_model = main_models.UserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateResourceGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

