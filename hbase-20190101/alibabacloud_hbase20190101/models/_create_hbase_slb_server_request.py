# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHBaseSlbServerRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_id: str = None,
        slb_server: str = None,
    ):
        # The client token.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The load balancing service to create. Valid values:
        # 
        # - **thrift**: the Thrift cross-language and cross-platform remote procedure call (RPC) protocol service.
        # - **rest**: the HTTP protocol service.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.slb_server is not None:
            result['SlbServer'] = self.slb_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('SlbServer') is not None:
            self.slb_server = m.get('SlbServer')

        return self

