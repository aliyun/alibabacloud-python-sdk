# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLifecycleRetrieveJobsRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        storage_type: str = None,
    ):
        # The file system ID.
        self.file_system_id = file_system_id
        # The page number of the list.
        # 
        # Start value (default value): 1.
        self.page_number = page_number
        # The number of data retrieval tasks on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The status of the data retrieval task. Valid values:
        # - active: running.
        # - canceled: canceled.
        # - completed: completed.
        # - failed: failed.
        self.status = status
        # The storage class. Valid values:
        # - InfrequentAccess: IA storage class.
        # - Archive: Archive storage class.
        # > If StorageType is not specified, data retrieval tasks of all storage classes are returned.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

