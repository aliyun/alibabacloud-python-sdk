# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGlobalDataNetworkRequest(DaraModel):
    def __init__(
        self,
        network_id: str = None,
    ):
        # GDN ID
        self.network_id = network_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        return self

