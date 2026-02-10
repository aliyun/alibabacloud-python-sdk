# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAssetSelectionConfigRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        platform: str = None,
        target_type: str = None,
    ):
        # The feature that you want to select for the asset. Valid values:
        # 
        # *   **VIRUS_SCAN_CYCLE_CONFIG**: virus detection and removal
        # *   **VIRUS_SCAN_ONCE_TASK**: one-time scan for viruses
        # *   **AGENTLESS_MALICIOUS_WHITE_LIST_[ID]**: a whitelist rule for alerts that are detected by using the agentless detection feature
        # *   **AGENTLESS_VUL_WHITE_LIST_[ID]**: a whitelist rule for vulnerabilities that are detected by using the agentless detection feature
        # *   **FILE_PROTECT_RULE_SWITCH_TYPE_[ID]**: core file protection
        # 
        # This parameter is required.
        self.business_type = business_type
        # The operating system of the asset. Valid values:
        # 
        # *   **all**: all operating systems
        # *   **windows**: the Windows operating system
        # *   **linux**: the Linux operating system
        # 
        # >  If you leave this parameter empty, the system automatically selects a value for the parameter based on the value of the **BusinessType** parameter.
        # 
        # *   If the BusinessType parameter is set to **VIRUS_SCAN_CYCLE_CONFIG**, the value of the Platform parameter is **all**.
        # 
        # *   If the BusinessType parameter is set to **VIRUS_SCAN_ONCE_TASK**, the value of the Platform parameter is **all**.
        # 
        # *   If the BusinessType parameter is set to **AGENTLESS_MALICIOUS_WHITE_LIST_[ID]**, the value of the Platform parameter is **all**.
        # 
        # *   If the BusinessType parameter is set to **AGENTLESS_VUL_WHITE_LIST_[ID]** the value of the Platform parameter is **all**.
        # 
        # *   If the BusinessType parameter is set to **FILE_PROTECT_RULE_SWITCH_TYPE_[ID]**, the value of the Platform parameter is **linux**.
        self.platform = platform
        # The dimension based on which you want to select the asset. Valid values:
        # 
        # *   **instance**: selects the asset by server.
        # *   **group**: selects the asset by group.
        # *   **vpc**: selects the asset by virtual private cloud (VPC).
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

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

