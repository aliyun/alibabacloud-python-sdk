# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeModifyPGHbaConfigLogResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        hba_log_items: main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItems = None,
        log_item_count: int = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # An array that consists of the modifications to the pg_hba.conf file.
        self.hba_log_items = hba_log_items
        # The number of modification records.
        self.log_item_count = log_item_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.hba_log_items:
            self.hba_log_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.hba_log_items is not None:
            result['HbaLogItems'] = self.hba_log_items.to_map()

        if self.log_item_count is not None:
            result['LogItemCount'] = self.log_item_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('HbaLogItems') is not None:
            temp_model = main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItems()
            self.hba_log_items = temp_model.from_map(m.get('HbaLogItems'))

        if m.get('LogItemCount') is not None:
            self.log_item_count = m.get('LogItemCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeModifyPGHbaConfigLogResponseBodyHbaLogItems(DaraModel):
    def __init__(
        self,
        hba_log_item: List[main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItem] = None,
    ):
        self.hba_log_item = hba_log_item

    def validate(self):
        if self.hba_log_item:
            for v1 in self.hba_log_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HbaLogItem'] = []
        if self.hba_log_item is not None:
            for k1 in self.hba_log_item:
                result['HbaLogItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hba_log_item = []
        if m.get('HbaLogItem') is not None:
            for k1 in m.get('HbaLogItem'):
                temp_model = main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItem()
                self.hba_log_item.append(temp_model.from_map(k1))

        return self

class DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItem(DaraModel):
    def __init__(
        self,
        after_hba_items: main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemAfterHbaItems = None,
        before_hba_items: main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemBeforeHbaItems = None,
        modify_status: str = None,
        modify_time: str = None,
        status_reason: str = None,
    ):
        # The configurations of the pg_hba.conf file after modification.
        self.after_hba_items = after_hba_items
        # The configurations of the pg_hba.conf file before modification.
        self.before_hba_items = before_hba_items
        # The status of the modification.
        # 
        # *   **success**: The modification is successful.
        # *   **failed**: The modification failed.
        # *   **setting**: The modification is being applied.
        self.modify_status = modify_status
        # The time when the pg_hba.conf file was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The reason why the modification failed.
        self.status_reason = status_reason

    def validate(self):
        if self.after_hba_items:
            self.after_hba_items.validate()
        if self.before_hba_items:
            self.before_hba_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_hba_items is not None:
            result['AfterHbaItems'] = self.after_hba_items.to_map()

        if self.before_hba_items is not None:
            result['BeforeHbaItems'] = self.before_hba_items.to_map()

        if self.modify_status is not None:
            result['ModifyStatus'] = self.modify_status

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterHbaItems') is not None:
            temp_model = main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemAfterHbaItems()
            self.after_hba_items = temp_model.from_map(m.get('AfterHbaItems'))

        if m.get('BeforeHbaItems') is not None:
            temp_model = main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemBeforeHbaItems()
            self.before_hba_items = temp_model.from_map(m.get('BeforeHbaItems'))

        if m.get('ModifyStatus') is not None:
            self.modify_status = m.get('ModifyStatus')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        return self

class DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemBeforeHbaItems(DaraModel):
    def __init__(
        self,
        hba_item: List[main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemBeforeHbaItemsHbaItem] = None,
    ):
        self.hba_item = hba_item

    def validate(self):
        if self.hba_item:
            for v1 in self.hba_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HbaItem'] = []
        if self.hba_item is not None:
            for k1 in self.hba_item:
                result['HbaItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hba_item = []
        if m.get('HbaItem') is not None:
            for k1 in m.get('HbaItem'):
                temp_model = main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemBeforeHbaItemsHbaItem()
                self.hba_item.append(temp_model.from_map(k1))

        return self

class DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemBeforeHbaItemsHbaItem(DaraModel):
    def __init__(
        self,
        address: str = None,
        database: str = None,
        mask: str = None,
        method: str = None,
        option: str = None,
        priority_id: int = None,
        type: str = None,
        user: str = None,
    ):
        # The IP address.
        self.address = address
        # The name of the database.
        self.database = database
        # The mask of the IP address.
        self.mask = mask
        # The authentication method.
        self.method = method
        # The value of this parameter varies based on the value of the Method parameter.
        self.option = option
        # The priority.
        self.priority_id = priority_id
        # The connection type.
        self.type = type
        # The username of the account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.database is not None:
            result['Database'] = self.database

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.method is not None:
            result['Method'] = self.method

        if self.option is not None:
            result['Option'] = self.option

        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemAfterHbaItems(DaraModel):
    def __init__(
        self,
        hba_item: List[main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemAfterHbaItemsHbaItem] = None,
    ):
        self.hba_item = hba_item

    def validate(self):
        if self.hba_item:
            for v1 in self.hba_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HbaItem'] = []
        if self.hba_item is not None:
            for k1 in self.hba_item:
                result['HbaItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hba_item = []
        if m.get('HbaItem') is not None:
            for k1 in m.get('HbaItem'):
                temp_model = main_models.DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemAfterHbaItemsHbaItem()
                self.hba_item.append(temp_model.from_map(k1))

        return self

class DescribeModifyPGHbaConfigLogResponseBodyHbaLogItemsHbaLogItemAfterHbaItemsHbaItem(DaraModel):
    def __init__(
        self,
        address: str = None,
        database: str = None,
        mask: str = None,
        method: str = None,
        option: str = None,
        priority_id: int = None,
        type: str = None,
        user: str = None,
    ):
        # The IP address.
        self.address = address
        # The name of the database.
        self.database = database
        # The mask of the IP address.
        self.mask = mask
        # The authentication method.
        self.method = method
        # The value of this parameter was set based on the value of the Method parameter.
        self.option = option
        # The priority.
        self.priority_id = priority_id
        # The connection type.
        self.type = type
        # The username of the account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.database is not None:
            result['Database'] = self.database

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.method is not None:
            result['Method'] = self.method

        if self.option is not None:
            result['Option'] = self.option

        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

