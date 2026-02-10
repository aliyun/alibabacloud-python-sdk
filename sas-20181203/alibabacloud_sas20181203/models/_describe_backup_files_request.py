# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupFilesRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        page_size: str = None,
        path: str = None,
        snapshot_hash: str = None,
        uuid: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries to return on each page. Default value: **10**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The path to the backup file.
        self.path = path
        # The hash value of the backup file.
        # 
        # This parameter is required.
        self.snapshot_hash = snapshot_hash
        # The UUID of the server to which an anti-ransomware policy is applied.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

