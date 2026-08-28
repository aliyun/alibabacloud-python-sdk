# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNetworkAccessRequest(DaraModel):
    def __init__(
        self,
        network_access_type: str = None,
    ):
        # This parameter is required.
        self.network_access_type = network_access_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_access_type is not None:
            result['networkAccessType'] = self.network_access_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('networkAccessType') is not None:
            self.network_access_type = m.get('networkAccessType')

        return self

