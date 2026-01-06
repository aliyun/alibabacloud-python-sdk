# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListLakeStoragesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListLakeStoragesResponseBodyItems] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code or the error code.
        self.code = code
        # The response code. The status code 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The queried lake storages.
        self.items = items
        # The returned message. Valid values:
        # 
        # *   If the request was successful, a success message is returned.****
        # *   If the request failed, an error message is returned.
        self.message = message
        # The token that is used for paging when the number of results is greater than the value of MaxResults.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the dry run succeeds. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListLakeStoragesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLakeStoragesResponseBodyItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator_uid: str = None,
        dbcluster_id: str = None,
        description: str = None,
        file_size: str = None,
        lake_storage_id: str = None,
        operator_uid: str = None,
        owner_uid: str = None,
        permissions: List[main_models.ListLakeStoragesResponseBodyItemsPermissions] = None,
        region_id: str = None,
        table_count: int = None,
        total_rows: int = None,
        total_storage: str = None,
        update_time: str = None,
    ):
        # The time when the lake storage was created.
        self.create_time = create_time
        # The creator UID.
        self.creator_uid = creator_uid
        # The ID of the AnalyticDB for MySQL cluster.
        self.dbcluster_id = dbcluster_id
        # The description of the lake storage.
        self.description = description
        # The size of data files.
        self.file_size = file_size
        # The unique identifier of the lake storage.
        self.lake_storage_id = lake_storage_id
        # The operator UID.
        self.operator_uid = operator_uid
        # The queried lake storage.
        self.owner_uid = owner_uid
        # The permissions on the lake storage.
        self.permissions = permissions
        # The region ID.
        self.region_id = region_id
        # The number of tables.
        self.table_count = table_count
        # The total number of entries returned.
        self.total_rows = total_rows
        # The total storage size.
        self.total_storage = total_storage
        # The time when the lake storage was last updated.
        self.update_time = update_time

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_uid is not None:
            result['CreatorUid'] = self.creator_uid

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.lake_storage_id is not None:
            result['LakeStorageId'] = self.lake_storage_id

        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.table_count is not None:
            result['TableCount'] = self.table_count

        if self.total_rows is not None:
            result['TotalRows'] = self.total_rows

        if self.total_storage is not None:
            result['TotalStorage'] = self.total_storage

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorUid') is not None:
            self.creator_uid = m.get('CreatorUid')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('LakeStorageId') is not None:
            self.lake_storage_id = m.get('LakeStorageId')

        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.ListLakeStoragesResponseBodyItemsPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')

        if m.get('TotalRows') is not None:
            self.total_rows = m.get('TotalRows')

        if m.get('TotalStorage') is not None:
            self.total_storage = m.get('TotalStorage')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListLakeStoragesResponseBodyItemsPermissions(DaraModel):
    def __init__(
        self,
        account: str = None,
        read: bool = None,
        type: str = None,
        write: bool = None,
    ):
        # The database account ID.
        self.account = account
        # The read permissions.
        self.read = read
        # The type of the database account.
        self.type = type
        # The write permissions.
        self.write = write

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.read is not None:
            result['Read'] = self.read

        if self.type is not None:
            result['Type'] = self.type

        if self.write is not None:
            result['Write'] = self.write

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Read') is not None:
            self.read = m.get('Read')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Write') is not None:
            self.write = m.get('Write')

        return self

