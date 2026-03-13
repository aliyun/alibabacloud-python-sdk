# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class ListAccountFactoryBaselineItemsResponseBody(DaraModel):
    def __init__(
        self,
        baseline_items: List[main_models.ListAccountFactoryBaselineItemsResponseBodyBaselineItems] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The baseline items.
        self.baseline_items = baseline_items
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.baseline_items:
            for v1 in self.baseline_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k1 in self.baseline_items:
                result['BaselineItems'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k1 in m.get('BaselineItems'):
                temp_model = main_models.ListAccountFactoryBaselineItemsResponseBodyBaselineItems()
                self.baseline_items.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAccountFactoryBaselineItemsResponseBodyBaselineItems(DaraModel):
    def __init__(
        self,
        depends_on: List[main_models.ListAccountFactoryBaselineItemsResponseBodyBaselineItemsDependsOn] = None,
        description: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        # The dependency of the baseline item.
        self.depends_on = depends_on
        # The description of the baseline item.
        self.description = description
        # The name of the baseline item.
        self.name = name
        # The type of the baseline item.
        self.type = type
        # The version of the baseline item.
        self.version = version

    def validate(self):
        if self.depends_on:
            for v1 in self.depends_on:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DependsOn'] = []
        if self.depends_on is not None:
            for k1 in self.depends_on:
                result['DependsOn'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.depends_on = []
        if m.get('DependsOn') is not None:
            for k1 in m.get('DependsOn'):
                temp_model = main_models.ListAccountFactoryBaselineItemsResponseBodyBaselineItemsDependsOn()
                self.depends_on.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListAccountFactoryBaselineItemsResponseBodyBaselineItemsDependsOn(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        # The name of the baseline item.
        self.name = name
        # The type of the baseline item.
        self.type = type
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

