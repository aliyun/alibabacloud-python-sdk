# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructDlfSnapshotDto(DaraModel):
    def __init__(
        self,
        changelog_record_count: int = None,
        commit_kind: str = None,
        delta_record_count: int = None,
        schema_id: int = None,
        snapshot_id: int = None,
        time_millis: int = None,
        total_record_count: int = None,
    ):
        self.changelog_record_count = changelog_record_count
        self.commit_kind = commit_kind
        self.delta_record_count = delta_record_count
        self.schema_id = schema_id
        self.snapshot_id = snapshot_id
        self.time_millis = time_millis
        self.total_record_count = total_record_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changelog_record_count is not None:
            result['changelogRecordCount'] = self.changelog_record_count

        if self.commit_kind is not None:
            result['commitKind'] = self.commit_kind

        if self.delta_record_count is not None:
            result['deltaRecordCount'] = self.delta_record_count

        if self.schema_id is not None:
            result['schemaId'] = self.schema_id

        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id

        if self.time_millis is not None:
            result['timeMillis'] = self.time_millis

        if self.total_record_count is not None:
            result['totalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changelogRecordCount') is not None:
            self.changelog_record_count = m.get('changelogRecordCount')

        if m.get('commitKind') is not None:
            self.commit_kind = m.get('commitKind')

        if m.get('deltaRecordCount') is not None:
            self.delta_record_count = m.get('deltaRecordCount')

        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')

        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')

        if m.get('timeMillis') is not None:
            self.time_millis = m.get('timeMillis')

        if m.get('totalRecordCount') is not None:
            self.total_record_count = m.get('totalRecordCount')

        return self

