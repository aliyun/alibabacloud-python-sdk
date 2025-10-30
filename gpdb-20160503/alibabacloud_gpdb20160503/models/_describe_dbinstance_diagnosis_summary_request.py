# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceDiagnosisSummaryRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        role_preferd: str = None,
        start_status: str = None,
        sync_mode: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **20**
        # *   **50**
        # *   **100**
        # 
        # Default value: **20**.
        self.page_size = page_size
        # The role state of the node. It specifies whether a primary/secondary switchover occurs. Valid values:
        # 
        # *   **normal**: The node role is normal. No primary/secondary switchover occurs.
        # *   **reverse**: The node role is reversed. A primary/secondary switchover occurs.
        self.role_preferd = role_preferd
        # The running state of the node. Valid values:
        # 
        # *   **UP**: The node is running.
        # *   **DOWN**: The node is faulty.
        # 
        # If you do not specify this parameter, the information about nodes in all running states is returned.
        self.start_status = start_status
        # The data synchronization state of the node. Valid values:
        # 
        # *   **synced**: The node data is synchronized.
        # *   **notSyncing**: The node data is not synchronized.
        # 
        # If you do not specify this parameter, the information about nodes in all synchronization states is returned.
        self.sync_mode = sync_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role_preferd is not None:
            result['RolePreferd'] = self.role_preferd

        if self.start_status is not None:
            result['StartStatus'] = self.start_status

        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RolePreferd') is not None:
            self.role_preferd = m.get('RolePreferd')

        if m.get('StartStatus') is not None:
            self.start_status = m.get('StartStatus')

        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')

        return self

