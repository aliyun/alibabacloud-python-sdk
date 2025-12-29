# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class UpgradeClusterAddonsRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.UpgradeClusterAddonsRequestBody] = None,
    ):
        # The request parameters.
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.UpgradeClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k1))

        return self

class UpgradeClusterAddonsRequestBody(DaraModel):
    def __init__(
        self,
        component_name: str = None,
        config: str = None,
        next_version: str = None,
        policy: str = None,
        version: str = None,
    ):
        # The name of the component.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The custom component settings that you want to use. The value is a JSON string.
        self.config = config
        # The version to which the component can be updated. You can call the `DescribeClusterAddonsVersion` operation to query the version to which the component can be updated.
        # 
        # This parameter is required.
        self.next_version = next_version
        # The update policy. Valid values:
        # 
        # *   overwrite
        # *   canary
        self.policy = policy
        # The current version of the component.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_name is not None:
            result['component_name'] = self.component_name

        if self.config is not None:
            result['config'] = self.config

        if self.next_version is not None:
            result['next_version'] = self.next_version

        if self.policy is not None:
            result['policy'] = self.policy

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('component_name') is not None:
            self.component_name = m.get('component_name')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

