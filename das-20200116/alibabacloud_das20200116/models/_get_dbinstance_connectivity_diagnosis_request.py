# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDBInstanceConnectivityDiagnosisRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        src_ip: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The source IP address.
        # 
        # This parameter is required.
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        return self

