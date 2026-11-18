# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ModelApiPolicyConfig(DaraModel):
    def __init__(
        self,
        ai_security_guard_config: main_models.AiSecurityGuardConfig = None,
        ai_statistics_config: main_models.AiStatisticsConfig = None,
        enable: bool = None,
        type: str = None,
    ):
        # The AI security protection settings.
        self.ai_security_guard_config = ai_security_guard_config
        # The AI observability and request log configuration.
        self.ai_statistics_config = ai_statistics_config
        # Specifies whether to enable the policy.
        self.enable = enable
        # The policy type. Only AiStatistics and AiSecurityGuard are supported.
        self.type = type

    def validate(self):
        if self.ai_security_guard_config:
            self.ai_security_guard_config.validate()
        if self.ai_statistics_config:
            self.ai_statistics_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_security_guard_config is not None:
            result['aiSecurityGuardConfig'] = self.ai_security_guard_config.to_map()

        if self.ai_statistics_config is not None:
            result['aiStatisticsConfig'] = self.ai_statistics_config.to_map()

        if self.enable is not None:
            result['enable'] = self.enable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiSecurityGuardConfig') is not None:
            temp_model = main_models.AiSecurityGuardConfig()
            self.ai_security_guard_config = temp_model.from_map(m.get('aiSecurityGuardConfig'))

        if m.get('aiStatisticsConfig') is not None:
            temp_model = main_models.AiStatisticsConfig()
            self.ai_statistics_config = temp_model.from_map(m.get('aiStatisticsConfig'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

