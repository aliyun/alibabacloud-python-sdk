# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAutoGroupingConfigRequest(DaraModel):
    def __init__(
        self,
        enable_existing_resources_transfer: bool = None,
    ):
        # Specifies whether to enable the Transfer Existing Associated Resources feature. Valid values:
        # 
        # *   false
        # *   true
        self.enable_existing_resources_transfer = enable_existing_resources_transfer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_existing_resources_transfer is not None:
            result['EnableExistingResourcesTransfer'] = self.enable_existing_resources_transfer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExistingResourcesTransfer') is not None:
            self.enable_existing_resources_transfer = m.get('EnableExistingResourcesTransfer')

        return self

