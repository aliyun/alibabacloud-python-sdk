# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class GetAccountFactoryBaselineResponseBody(DaraModel):
    def __init__(
        self,
        baseline_id: str = None,
        baseline_items: List[main_models.GetAccountFactoryBaselineResponseBodyBaselineItems] = None,
        baseline_name: str = None,
        create_time: str = None,
        description: str = None,
        request_id: str = None,
        type: str = None,
        update_time: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The baseline items.
        self.baseline_items = baseline_items
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The time when the baseline was created.
        self.create_time = create_time
        # The description of the baseline.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The type of the baseline. Valid values:
        # 
        # *   System: default baseline.
        # *   Custom: custom baseline.
        self.type = type
        # The time when the baseline was updated.
        self.update_time = update_time

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
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k1 in self.baseline_items:
                result['BaselineItems'].append(k1.to_map() if k1 else None)

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k1 in m.get('BaselineItems'):
                temp_model = main_models.GetAccountFactoryBaselineResponseBodyBaselineItems()
                self.baseline_items.append(temp_model.from_map(k1))

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetAccountFactoryBaselineResponseBodyBaselineItems(DaraModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        version: str = None,
    ):
        # The configuration of the baseline item.
        # 
        # The value is a JSON string.
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

