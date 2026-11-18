# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNetworkAccessRequest(DaraModel):
    def __init__(
        self,
        network_access_type: str = None,
    ):
        # The expected network access type after the modification. For example, if public network access is added to a private gateway, set this parameter to private&pubnet. If private network access is removed from a gateway with both public and private network access, set this parameter to pubnet.
        # 
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

