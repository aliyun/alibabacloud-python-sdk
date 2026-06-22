# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAssetSelectionConfigRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
    ):
        # The business type of the asset selection. Valid values:
        # 
        # - **VIRUS_SCAN_CYCLE_CONFIG**: trojan scan configuration
        # - **VIRUS_SCAN_ONCE_TASK**: trojan scan one-time scan
        # - **AGENTLESS_MALICIOUS_WHITE_LIST_[ID]**: agentless detection alert whitelisting rule
        # - **AGENTLESS_VUL_WHITE_LIST_[ID]**: agentless detection vulnerability whitelisting rule
        # - **FILE_PROTECT_RULE_SWITCH_TYPE_[ID]**: core file protection.
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

