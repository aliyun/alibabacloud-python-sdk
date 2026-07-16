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
        # The creation time of the rate limit rule, in ISO 8601 format.
        self.created_at = created_at
        # The descriptor ID for the rate limit rule, which associates the rule with a specific throttling target.
        self.descriptor_id = descriptor_id
        # The descriptor type for the rate limit rule, such as \\"model\\" or \\"user\\".
        self.descriptor_type = descriptor_type
        # Indicates whether the rate limit rule is enabled.
        self.enabled = enabled
        # The last update time of the rate limit rule, in ISO 8601 format.
        self.last_updated_at = last_updated_at
        # The unique identifier for the rate limit rule.
        self.rate_limit_rule_id = rate_limit_rule_id
        # A list of time window configurations. Multiple windows can be used to enforce layered rate limiting.
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

