# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHttpApiRequest(DaraModel):
    def __init__(
        self,
        expand_policy_configs: bool = None,
    ):
        # Specifies whether to expand independent policy configurations. If omitted or set to true, a complete compatibility view is returned. If set to false, the ModelAPI token throttling managed by the policy returns a policy reference and an optional read-only plugin status. You can use GetPolicy to retrieve the rule body.
        self.expand_policy_configs = expand_policy_configs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expand_policy_configs is not None:
            result['expandPolicyConfigs'] = self.expand_policy_configs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expandPolicyConfigs') is not None:
            self.expand_policy_configs = m.get('expandPolicyConfigs')

        return self

