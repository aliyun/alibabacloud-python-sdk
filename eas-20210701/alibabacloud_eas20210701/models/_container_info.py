# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContainerInfo(DaraModel):
    def __init__(
        self,
        current_reaon: str = None,
        current_status: str = None,
        current_timestamp: str = None,
        image: str = None,
        last_reason: str = None,
        last_status: str = None,
        last_timestamp: str = None,
        name: str = None,
        port: int = None,
        ready: bool = None,
        restart_count: int = None,
    ):
        self.current_reaon = current_reaon
        self.current_status = current_status
        self.current_timestamp = current_timestamp
        self.image = image
        self.last_reason = last_reason
        self.last_status = last_status
        self.last_timestamp = last_timestamp
        self.name = name
        self.port = port
        self.ready = ready
        self.restart_count = restart_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_reaon is not None:
            result['CurrentReaon'] = self.current_reaon

        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status

        if self.current_timestamp is not None:
            result['CurrentTimestamp'] = self.current_timestamp

        if self.image is not None:
            result['Image'] = self.image

        if self.last_reason is not None:
            result['LastReason'] = self.last_reason

        if self.last_status is not None:
            result['LastStatus'] = self.last_status

        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentReaon') is not None:
            self.current_reaon = m.get('CurrentReaon')

        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')

        if m.get('CurrentTimestamp') is not None:
            self.current_timestamp = m.get('CurrentTimestamp')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('LastReason') is not None:
            self.last_reason = m.get('LastReason')

        if m.get('LastStatus') is not None:
            self.last_status = m.get('LastStatus')

        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')

        return self

