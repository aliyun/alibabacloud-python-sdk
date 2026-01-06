# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class UpdateRunRequest(DaraModel):
    def __init__(
        self,
        labels: List[main_models.Label] = None,
        name: str = None,
        params: List[main_models.RunParam] = None,
    ):
        # The labels.
        self.labels = labels
        # The run name. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be 1 to 63 characters in length.
        self.name = name
        # The parameters.
        self.params = params

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.RunParam()
                self.params.append(temp_model.from_map(k1))

        return self

