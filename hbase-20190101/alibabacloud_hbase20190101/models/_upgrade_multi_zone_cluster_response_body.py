# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeMultiZoneClusterResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upgrading_components: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The components that triggered the upgrade among the multiple components to be upgraded.
        self.upgrading_components = upgrading_components

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upgrading_components is not None:
            result['UpgradingComponents'] = self.upgrading_components

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpgradingComponents') is not None:
            self.upgrading_components = m.get('UpgradingComponents')

        return self

