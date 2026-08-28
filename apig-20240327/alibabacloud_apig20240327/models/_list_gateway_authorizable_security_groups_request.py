# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayAuthorizableSecurityGroupsRequest(DaraModel):
    def __init__(
        self,
        cs_cluster_id: str = None,
    ):
        # The cluster ID.
        self.cs_cluster_id = cs_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cs_cluster_id is not None:
            result['csClusterId'] = self.cs_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('csClusterId') is not None:
            self.cs_cluster_id = m.get('csClusterId')

        return self

