# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateServiceVersionRequest(DaraModel):
    def __init__(
        self,
        labels: List[main_models.CreateServiceVersionRequestLabels] = None,
        name: str = None,
    ):
        # The service tags.
        # 
        # This parameter is required.
        self.labels = labels
        # The version name.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('labels') is not None:
            for k1 in m.get('labels'):
                temp_model = main_models.CreateServiceVersionRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class CreateServiceVersionRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

