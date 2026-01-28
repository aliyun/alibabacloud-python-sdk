# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateConnectDatasourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_params: str = None,
        password: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.connection_params = connection_params
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connection_params is not None:
            result['ConnectionParams'] = self.connection_params

        if self.password is not None:
            result['Password'] = self.password

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectionParams') is not None:
            self.connection_params = m.get('ConnectionParams')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

