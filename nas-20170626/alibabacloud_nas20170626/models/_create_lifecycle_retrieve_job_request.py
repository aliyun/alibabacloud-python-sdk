# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateLifecycleRetrieveJobRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        paths: List[str] = None,
        storage_type: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The directories or files that you want to retrieve. You can specify a maximum of 10 paths.
        # 
        # This parameter is required.
        self.paths = paths
        # The storage class.
        # 
        # *   InfrequentAccess (default): the Infrequent Access (IA) storage class.
        # *   Archive: the Archive storage class.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

