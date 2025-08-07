# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 


class TableSnapshot(DaraModel):
    def __init__(
        self,
        file_count: int = None,
        file_size_in_bytes: int = None,
        last_file_creation_time: int = None,
        record_count: int = None,
        snapshot: main_models.Snapshot = None,
    ):
        self.file_count = file_count
        self.file_size_in_bytes = file_size_in_bytes
        self.last_file_creation_time = last_file_creation_time
        self.record_count = record_count
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            self.snapshot.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_count is not None:
            result['fileCount'] = self.file_count

        if self.file_size_in_bytes is not None:
            result['fileSizeInBytes'] = self.file_size_in_bytes

        if self.last_file_creation_time is not None:
            result['lastFileCreationTime'] = self.last_file_creation_time

        if self.record_count is not None:
            result['recordCount'] = self.record_count

        if self.snapshot is not None:
            result['snapshot'] = self.snapshot.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileCount') is not None:
            self.file_count = m.get('fileCount')

        if m.get('fileSizeInBytes') is not None:
            self.file_size_in_bytes = m.get('fileSizeInBytes')

        if m.get('lastFileCreationTime') is not None:
            self.last_file_creation_time = m.get('lastFileCreationTime')

        if m.get('recordCount') is not None:
            self.record_count = m.get('recordCount')

        if m.get('snapshot') is not None:
            temp_model = main_models.Snapshot()
            self.snapshot = temp_model.from_map(m.get('snapshot'))

        return self

