# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupStorageResponseBody(DaraModel):
    def __init__(
        self,
        free_size: int = None,
        full_storage_size: int = None,
        log_storage_size: int = None,
        request_id: str = None,
    ):
        # The free quota for the storage capacity used for backup. Unit: bytes.
        self.free_size = free_size
        # The storage capacity used for the full backup. Unit: bytes.
        # 
        # >  Instances that use cloud disks support snapshot backup. The size of the storage used for the current full backup is the size of the snapshot chain.
        self.full_storage_size = full_storage_size
        # The storage capacity used for the log backup. Unit: bytes.
        self.log_storage_size = log_storage_size
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.free_size is not None:
            result['FreeSize'] = self.free_size

        if self.full_storage_size is not None:
            result['FullStorageSize'] = self.full_storage_size

        if self.log_storage_size is not None:
            result['LogStorageSize'] = self.log_storage_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeSize') is not None:
            self.free_size = m.get('FreeSize')

        if m.get('FullStorageSize') is not None:
            self.full_storage_size = m.get('FullStorageSize')

        if m.get('LogStorageSize') is not None:
            self.log_storage_size = m.get('LogStorageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

