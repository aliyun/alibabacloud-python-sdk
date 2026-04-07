# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class DataDesensPlanTemplateValue(DaraModel):
    def __init__(
        self,
        name: str = None,
        support_water_mark: bool = None,
        ext_param_template: List[Any] = None,
    ):
        # The name of the data masking method.
        self.name = name
        # Indicates whether a watermark is added. Valid values:
        # 
        # *   true: allow
        # *   false: disallow
        self.support_water_mark = support_water_mark
        # The data masking parameters and their descriptions.
        self.ext_param_template = ext_param_template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.support_water_mark is not None:
            result['SupportWaterMark'] = self.support_water_mark

        if self.ext_param_template is not None:
            result['ExtParamTemplate'] = self.ext_param_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SupportWaterMark') is not None:
            self.support_water_mark = m.get('SupportWaterMark')

        if m.get('ExtParamTemplate') is not None:
            self.ext_param_template = m.get('ExtParamTemplate')

        return self

