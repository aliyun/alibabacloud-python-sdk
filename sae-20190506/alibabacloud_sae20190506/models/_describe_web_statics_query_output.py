# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeWebStaticsQueryOutput(DaraModel):
    def __init__(
        self,
        length: int = None,
        web_statics: List[main_models.WebStaticsInfo] = None,
    ):
        self.length = length
        self.web_statics = web_statics

    def validate(self):
        if self.web_statics:
            for v1 in self.web_statics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.length is not None:
            result['Length'] = self.length

        result['WebStatics'] = []
        if self.web_statics is not None:
            for k1 in self.web_statics:
                result['WebStatics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')

        self.web_statics = []
        if m.get('WebStatics') is not None:
            for k1 in m.get('WebStatics'):
                temp_model = main_models.WebStaticsInfo()
                self.web_statics.append(temp_model.from_map(k1))

        return self

