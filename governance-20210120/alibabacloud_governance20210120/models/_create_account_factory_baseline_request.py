# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class CreateAccountFactoryBaselineRequest(DaraModel):
    def __init__(
        self,
        baseline_items: List[main_models.CreateAccountFactoryBaselineRequestBaselineItems] = None,
        baseline_name: str = None,
        description: str = None,
        region_id: str = None,
    ):
        # An array that contains the baseline items.
        # 
        # You can call the [ListAccountFactoryBaselineItems](~~ListAccountFactoryBaselineItems~~) operation to query a list of baseline items supported by the account factory in Cloud Governance Center.
        self.baseline_items = baseline_items
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The description of the baseline.
        self.description = description
        # The region ID.
        self.region_id = region_id

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

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k1 in m.get('BaselineItems'):
                temp_model = main_models.CreateAccountFactoryBaselineRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k1))

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateAccountFactoryBaselineRequestBaselineItems(DaraModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        version: str = None,
    ):
        # The configurations of the baseline item. The value of this parameter is a JSON string.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

