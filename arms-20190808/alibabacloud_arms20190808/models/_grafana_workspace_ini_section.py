# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GrafanaWorkspaceIniSection(DaraModel):
    def __init__(
        self,
        propertys: List[main_models.GrafanaWorkspaceIniProperty] = None,
        section: str = None,
    ):
        self.propertys = propertys
        self.section = section

    def validate(self):
        if self.propertys:
            for v1 in self.propertys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['propertys'] = []
        if self.propertys is not None:
            for k1 in self.propertys:
                result['propertys'].append(k1.to_map() if k1 else None)

        if self.section is not None:
            result['section'] = self.section

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.propertys = []
        if m.get('propertys') is not None:
            for k1 in m.get('propertys'):
                temp_model = main_models.GrafanaWorkspaceIniProperty()
                self.propertys.append(temp_model.from_map(k1))

        if m.get('section') is not None:
            self.section = m.get('section')

        return self

