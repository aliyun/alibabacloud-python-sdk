# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAssetSelectionConfigRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
    ):
        # The feature that is selected for the asset. Valid values:
        # 
        # *   **VIRUS_SCAN_CYCLE_CONFIG**: virus detection and removal
        # *   **VIRUS_SCAN_ONCE_TASK**: one-time scan for viruses
        # *   **AGENTLESS_MALICIOUS_WHITE_LIST_[ID]**: a whitelist rule for alerts that are detected by using the agentless detection feature
        # *   **AGENTLESS_VUL_WHITE_LIST_[ID]**: a whitelist rule for vulnerabilities that are detected by using the agentless detection feature
        # *   **FILE_PROTECT_RULE_SWITCH_TYPE_[ID]**: core file protectioion
        # 
        # This parameter is required.
        self.business_type = business_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        return self

