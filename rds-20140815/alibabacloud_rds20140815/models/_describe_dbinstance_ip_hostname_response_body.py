# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceIpHostnameResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        ip_hostname_infos: str = None,
        request_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.ip_hostname_infos = ip_hostname_infos
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.ip_hostname_infos is not None:
            result['IpHostnameInfos'] = self.ip_hostname_infos

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IpHostnameInfos') is not None:
            self.ip_hostname_infos = m.get('IpHostnameInfos')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

