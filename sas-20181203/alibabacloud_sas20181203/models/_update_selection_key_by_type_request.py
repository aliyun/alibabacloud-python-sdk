# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSelectionKeyByTypeRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        selection_key: str = None,
    ):
        # The business type of the asset selection. Valid values:
        # 
        # - **VIRUS_SCAN_CYCLE_CONFIG**: virus scan configuration.
        # - **VIRUS_SCAN_ONCE_TASK**: one-time virus scan.
        # - **AGENTLESS_MALICIOUS_WHITE_LIST_[ID]**: agentless detection alert whitelisting rule.
        # - **AGENTLESS_VUL_WHITE_LIST_[ID]**: agentless detection vulnerability whitelisting rule.
        # - **FILE_PROTECT_RULE_SWITCH_TYPE_[ID]**: core file protection.
        self.business_type = business_type
        # The unique identifier of the asset selection.
        self.selection_key = selection_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        return self

