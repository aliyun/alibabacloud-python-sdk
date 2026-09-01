# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAssetSelectionConfigRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        client_token: str = None,
        platform: str = None,
        target_type: str = None,
    ):
        # The business type of the asset selection. Valid values:
        # 
        # - **VIRUS_SCAN_CYCLE_CONFIG**: trojan scan configuration.
        # - **VIRUS_SCAN_ONCE_TASK**: trojan scan one-time scan.
        # - **AGENTLESS_MALICIOUS_WHITE_LIST_[ID]**: agentless detection alert whitelisting rule.
        # - **AGENTLESS_VUL_WHITE_LIST_[ID]**: agentless detection vulnerability whitelisting rule.
        # - **FILE_PROTECT_RULE_SWITCH_TYPE_[ID]**: core file protection.
        # 
        # This parameter is required.
        self.business_type = business_type
        # The client token that is used to ensure the idempotence of the request. Different requests must use different tokens. The token supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The operating system of the target asset. Valid values:
        # 
        # - **all**: all operating systems.
        # - **windows**: Windows operating system.
        # - **linux**: Linux operating system.
        # > If this parameter is left empty, the default value is determined based on the **BusinessType** value.
        # >- **VIRUS_SCAN_CYCLE_CONFIG**: the value is **all**.
        # >- **VIRUS_SCAN_ONCE_TASK**: the value is **all**.
        # >- **AGENTLESS_MALICIOUS_WHITE_LIST_[ID]**: the value is **all**.
        # >- **AGENTLESS_VUL_WHITE_LIST_[ID]**: the value is **all**.
        # >- **FILE_PROTECT_RULE_SWITCH_TYPE_[ID]**: the value is **linux**.
        self.platform = platform
        # The target asset type. Valid values:
        # 
        # - **all_instance**: all servers.
        # - **instance**: select by server.
        # - **group**: select by group.
        # - **vpc**: select by VPC.
        # 
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

