# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class InstanceEventItem(DaraModel):
    def __init__(
        self,
        children: List[main_models.InstanceEventItem] = None,
        level: str = None,
        message: str = None,
        time: str = None,
        type: str = None,
    ):
        self.children = children
        self.level = level
        self.message = message
        self.time = time
        self.type = type

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['children'].append(k1.to_map() if k1 else None)

        if self.level is not None:
            result['level'] = self.level

        if self.message is not None:
            result['message'] = self.message

        if self.time is not None:
            result['time'] = self.time

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k1 in m.get('children'):
                temp_model = main_models.InstanceEventItem()
                self.children.append(temp_model.from_map(k1))

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

