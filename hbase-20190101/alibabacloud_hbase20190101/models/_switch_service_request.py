# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchServiceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        operate: str = None,
        service_name: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # - open: Enable  
        # - close: Shutdown
        # 
        # This parameter is required.
        self.operate = operate
        # Service name.
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.operate is not None:
            result['Operate'] = self.operate

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

