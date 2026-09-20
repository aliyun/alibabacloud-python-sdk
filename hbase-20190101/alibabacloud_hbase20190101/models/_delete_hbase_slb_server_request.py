# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHBaseSlbServerRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        slb_server: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The load balancing service. Valid values:
        # thrift
        # rest.
        # 
        # This parameter is required.
        self.slb_server = slb_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.slb_server is not None:
            result['SlbServer'] = self.slb_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('SlbServer') is not None:
            self.slb_server = m.get('SlbServer')

        return self

