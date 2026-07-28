# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructDlfTagDto(DaraModel):
    def __init__(
        self,
        snapshot_id: int = None,
        tag_name: str = None,
        time_millis: int = None,
        total_record_count: int = None,
    ):
        self.snapshot_id = snapshot_id
        self.tag_name = tag_name
        self.time_millis = time_millis
        self.total_record_count = total_record_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id

        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        if self.time_millis is not None:
            result['timeMillis'] = self.time_millis

        if self.total_record_count is not None:
            result['totalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')

        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        if m.get('timeMillis') is not None:
            self.time_millis = m.get('timeMillis')

        if m.get('totalRecordCount') is not None:
            self.total_record_count = m.get('totalRecordCount')

        return self

