# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackDetailRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        env: str = None,
        rpc_id: str = None,
        service_group_id: int = None,
        service_name: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.env = env
        self.rpc_id = rpc_id
        self.service_group_id = service_group_id
        self.service_name = service_name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.env is not None:
            result['env'] = self.env

        if self.rpc_id is not None:
            result['rpcId'] = self.rpc_id

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('rpcId') is not None:
            self.rpc_id = m.get('rpcId')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

