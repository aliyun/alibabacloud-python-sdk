# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeWebAppStaticsOutput(DaraModel):
    def __init__(
        self,
        length: int = None,
        web_app_statics: List[main_models.WebStaticsInfo] = None,
    ):
        self.length = length
        self.web_app_statics = web_app_statics

    def validate(self):
        if self.web_app_statics:
            for v1 in self.web_app_statics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.length is not None:
            result['Length'] = self.length

        result['WebAppStatics'] = []
        if self.web_app_statics is not None:
            for k1 in self.web_app_statics:
                result['WebAppStatics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')

        self.web_app_statics = []
        if m.get('WebAppStatics') is not None:
            for k1 in m.get('WebAppStatics'):
                temp_model = main_models.WebStaticsInfo()
                self.web_app_statics.append(temp_model.from_map(k1))

        return self

