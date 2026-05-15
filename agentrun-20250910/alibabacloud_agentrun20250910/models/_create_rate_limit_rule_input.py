# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateRateLimitRuleInput(DaraModel):
    def __init__(
        self,
        descriptor_id: str = None,
        descriptor_type: str = None,
        enabled: bool = None,
        windows: List[main_models.WindowLimit] = None,
    ):
        # 限流规则的描述符标识；非model维时必填，model维由服务端拼接
        self.descriptor_id = descriptor_id
        # 限流规则的描述符类型，如model、user等
        # 
        # This parameter is required.
        self.descriptor_type = descriptor_type
        # 是否启用该限流规则
        self.enabled = enabled
        # 限流时间窗口配置列表，至少需要一个窗口
        # 
        # This parameter is required.
        self.windows = windows

    def validate(self):
        if self.windows:
            for v1 in self.windows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.descriptor_id is not None:
            result['descriptorId'] = self.descriptor_id

        if self.descriptor_type is not None:
            result['descriptorType'] = self.descriptor_type

        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['windows'] = []
        if self.windows is not None:
            for k1 in self.windows:
                result['windows'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('descriptorId') is not None:
            self.descriptor_id = m.get('descriptorId')

        if m.get('descriptorType') is not None:
            self.descriptor_type = m.get('descriptorType')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.windows = []
        if m.get('windows') is not None:
            for k1 in m.get('windows'):
                temp_model = main_models.WindowLimit()
                self.windows.append(temp_model.from_map(k1))

        return self

