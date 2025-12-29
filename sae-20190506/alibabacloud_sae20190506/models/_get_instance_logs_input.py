# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceLogsInput(DaraModel):
    def __init__(
        self,
        backward_line: int = None,
        end_time: int = None,
        forward_line: int = None,
        is_tail: bool = None,
        match: str = None,
        message: str = None,
        offset: int = None,
        pack_id: str = None,
        pack_meta: str = None,
        start_time: int = None,
        timestamp: str = None,
        version_id: str = None,
    ):
        self.backward_line = backward_line
        # This parameter is required.
        self.end_time = end_time
        self.forward_line = forward_line
        self.is_tail = is_tail
        self.match = match
        self.message = message
        self.offset = offset
        self.pack_id = pack_id
        self.pack_meta = pack_meta
        # This parameter is required.
        self.start_time = start_time
        self.timestamp = timestamp
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backward_line is not None:
            result['backwardLine'] = self.backward_line

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.forward_line is not None:
            result['forwardLine'] = self.forward_line

        if self.is_tail is not None:
            result['isTail'] = self.is_tail

        if self.match is not None:
            result['match'] = self.match

        if self.message is not None:
            result['message'] = self.message

        if self.offset is not None:
            result['offset'] = self.offset

        if self.pack_id is not None:
            result['packID'] = self.pack_id

        if self.pack_meta is not None:
            result['packMeta'] = self.pack_meta

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.version_id is not None:
            result['versionID'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backwardLine') is not None:
            self.backward_line = m.get('backwardLine')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('forwardLine') is not None:
            self.forward_line = m.get('forwardLine')

        if m.get('isTail') is not None:
            self.is_tail = m.get('isTail')

        if m.get('match') is not None:
            self.match = m.get('match')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('packID') is not None:
            self.pack_id = m.get('packID')

        if m.get('packMeta') is not None:
            self.pack_meta = m.get('packMeta')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('versionID') is not None:
            self.version_id = m.get('versionID')

        return self

