# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Machine(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        ip: str = None,
        last_heartbeat_time: int = None,
        machine_uniqueid: str = None,
        userdefined_id: str = None,
    ):
        self.host_id = host_id
        self.ip = ip
        self.last_heartbeat_time = last_heartbeat_time
        self.machine_uniqueid = machine_uniqueid
        self.userdefined_id = userdefined_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['host-id'] = self.host_id

        if self.ip is not None:
            result['ip'] = self.ip

        if self.last_heartbeat_time is not None:
            result['lastHeartbeatTime'] = self.last_heartbeat_time

        if self.machine_uniqueid is not None:
            result['machine-uniqueid'] = self.machine_uniqueid

        if self.userdefined_id is not None:
            result['userdefined-id'] = self.userdefined_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host-id') is not None:
            self.host_id = m.get('host-id')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('lastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('lastHeartbeatTime')

        if m.get('machine-uniqueid') is not None:
            self.machine_uniqueid = m.get('machine-uniqueid')

        if m.get('userdefined-id') is not None:
            self.userdefined_id = m.get('userdefined-id')

        return self

