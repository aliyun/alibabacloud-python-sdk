# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class UpdateAutopilotPolicyRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        policy_config: main_models.AutopilotPolicy = None,
    ):
        # Specifies whether to enable automatic tuning. A value of true enables automatic tuning (ACTIVE), and a value of false disables tuning (DISABLED). If this parameter is not specified, the current status is not changed.
        self.enabled = enabled
        # The tuning policy configuration. This parameter uses full PUT mode: when specified, the complete policy object replaces the existing configuration entirely (fields not included are cleared). If this parameter is not specified, the existing configuration is retained.
        self.policy_config = policy_config

    def validate(self):
        if self.policy_config:
            self.policy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('policyConfig') is not None:
            temp_model = main_models.AutopilotPolicy()
            self.policy_config = temp_model.from_map(m.get('policyConfig'))

        return self

