# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class RateLimitRule(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        descriptor_id: str = None,
        descriptor_type: str = None,
        enabled: bool = None,
        last_updated_at: str = None,
        rate_limit_rule_id: str = None,
        windows: List[main_models.WindowLimit] = None,
    ):
        # 限流规则的创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 限流规则的描述符标识，用于关联具体的限流对象
        self.descriptor_id = descriptor_id
        # 限流规则的描述符类型，如model、user等
        self.descriptor_type = descriptor_type
        # 限流规则是否启用，true表示启用，false表示禁用
        self.enabled = enabled
        # 限流规则最后一次更新的时间，采用ISO 8601格式
        self.last_updated_at = last_updated_at
        # 限流规则的唯一标识符
        self.rate_limit_rule_id = rate_limit_rule_id
        # 限流时间窗口配置列表，支持多个窗口叠加限流
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
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.descriptor_id is not None:
            result['descriptorId'] = self.descriptor_id

        if self.descriptor_type is not None:
            result['descriptorType'] = self.descriptor_type

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.rate_limit_rule_id is not None:
            result['rateLimitRuleId'] = self.rate_limit_rule_id

        result['windows'] = []
        if self.windows is not None:
            for k1 in self.windows:
                result['windows'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('descriptorId') is not None:
            self.descriptor_id = m.get('descriptorId')

        if m.get('descriptorType') is not None:
            self.descriptor_type = m.get('descriptorType')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('rateLimitRuleId') is not None:
            self.rate_limit_rule_id = m.get('rateLimitRuleId')

        self.windows = []
        if m.get('windows') is not None:
            for k1 in m.get('windows'):
                temp_model = main_models.WindowLimit()
                self.windows.append(temp_model.from_map(k1))

        return self

