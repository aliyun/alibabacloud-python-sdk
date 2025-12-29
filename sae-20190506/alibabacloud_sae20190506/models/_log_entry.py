# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LogEntry(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        message: str = None,
        offset: int = None,
        pack_id: str = None,
        pack_meta: str = None,
        qualifier: str = None,
        timestamp: int = None,
        version_id: str = None,
    ):
        self.instance_id = instance_id
        self.message = message
        self.offset = offset
        self.pack_id = pack_id
        self.pack_meta = pack_meta
        self.qualifier = qualifier
        self.timestamp = timestamp
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceID'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        if self.offset is not None:
            result['offset'] = self.offset

        if self.pack_id is not None:
            result['packID'] = self.pack_id

        if self.pack_meta is not None:
            result['packMeta'] = self.pack_meta

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.version_id is not None:
            result['versionID'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('packID') is not None:
            self.pack_id = m.get('packID')

        if m.get('packMeta') is not None:
            self.pack_meta = m.get('packMeta')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('versionID') is not None:
            self.version_id = m.get('versionID')

        return self

