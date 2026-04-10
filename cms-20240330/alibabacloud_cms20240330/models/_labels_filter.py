# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class LabelsFilter(DaraModel):
    def __init__(
        self,
        all_of: List[main_models.LabelMatcher] = None,
        any_of: List[main_models.LabelMatcher] = None,
    ):
        # 匹配所有标签（AND）
        self.all_of = all_of
        # 匹配任意一个标签（OR）
        self.any_of = any_of

    def validate(self):
        if self.all_of:
            for v1 in self.all_of:
                 if v1:
                    v1.validate()
        if self.any_of:
            for v1 in self.any_of:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['allOf'] = []
        if self.all_of is not None:
            for k1 in self.all_of:
                result['allOf'].append(k1.to_map() if k1 else None)

        result['anyOf'] = []
        if self.any_of is not None:
            for k1 in self.any_of:
                result['anyOf'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_of = []
        if m.get('allOf') is not None:
            for k1 in m.get('allOf'):
                temp_model = main_models.LabelMatcher()
                self.all_of.append(temp_model.from_map(k1))

        self.any_of = []
        if m.get('anyOf') is not None:
            for k1 in m.get('anyOf'):
                temp_model = main_models.LabelMatcher()
                self.any_of.append(temp_model.from_map(k1))

        return self

