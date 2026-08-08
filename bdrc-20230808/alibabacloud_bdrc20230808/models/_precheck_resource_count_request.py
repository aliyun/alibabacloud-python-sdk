# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class PrecheckResourceCountRequest(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_resource_matchers: List[main_models.PrecheckResourceCountRequestTagResourceMatchers] = None,
    ):
        self.resource_type = resource_type
        # This parameter is required.
        self.tag_resource_matchers = tag_resource_matchers

    def validate(self):
        if self.tag_resource_matchers:
            for v1 in self.tag_resource_matchers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['TagResourceMatchers'] = []
        if self.tag_resource_matchers is not None:
            for k1 in self.tag_resource_matchers:
                result['TagResourceMatchers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag_resource_matchers = []
        if m.get('TagResourceMatchers') is not None:
            for k1 in m.get('TagResourceMatchers'):
                temp_model = main_models.PrecheckResourceCountRequestTagResourceMatchers()
                self.tag_resource_matchers.append(temp_model.from_map(k1))

        return self

class PrecheckResourceCountRequestTagResourceMatchers(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.operator = operator
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

