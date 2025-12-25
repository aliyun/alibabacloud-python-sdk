# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribePGHbaConfigResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        default_hba_items: main_models.DescribePGHbaConfigResponseBodyDefaultHbaItems = None,
        hba_modify_time: str = None,
        last_modify_status: str = None,
        modify_status_reason: str = None,
        request_id: str = None,
        running_hba_items: main_models.DescribePGHbaConfigResponseBodyRunningHbaItems = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The default configuration items of the pg_hba.conf file.
        self.default_hba_items = default_hba_items
        # The time when the previous modification was made to the pg_hba.conf file.
        self.hba_modify_time = hba_modify_time
        # The status of the previous modification to the pg_hba.conf file. Valid values:
        # 
        # *   **success**
        # *   **setting**
        # *   **failed**
        self.last_modify_status = last_modify_status
        # The reason why the previous modification was made to the pg_hba.conf file.
        self.modify_status_reason = modify_status_reason
        # The request ID.
        self.request_id = request_id
        # The current configuration items of the pg_hba.conf file.
        self.running_hba_items = running_hba_items

    def validate(self):
        if self.default_hba_items:
            self.default_hba_items.validate()
        if self.running_hba_items:
            self.running_hba_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.default_hba_items is not None:
            result['DefaultHbaItems'] = self.default_hba_items.to_map()

        if self.hba_modify_time is not None:
            result['HbaModifyTime'] = self.hba_modify_time

        if self.last_modify_status is not None:
            result['LastModifyStatus'] = self.last_modify_status

        if self.modify_status_reason is not None:
            result['ModifyStatusReason'] = self.modify_status_reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.running_hba_items is not None:
            result['RunningHbaItems'] = self.running_hba_items.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DefaultHbaItems') is not None:
            temp_model = main_models.DescribePGHbaConfigResponseBodyDefaultHbaItems()
            self.default_hba_items = temp_model.from_map(m.get('DefaultHbaItems'))

        if m.get('HbaModifyTime') is not None:
            self.hba_modify_time = m.get('HbaModifyTime')

        if m.get('LastModifyStatus') is not None:
            self.last_modify_status = m.get('LastModifyStatus')

        if m.get('ModifyStatusReason') is not None:
            self.modify_status_reason = m.get('ModifyStatusReason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningHbaItems') is not None:
            temp_model = main_models.DescribePGHbaConfigResponseBodyRunningHbaItems()
            self.running_hba_items = temp_model.from_map(m.get('RunningHbaItems'))

        return self

class DescribePGHbaConfigResponseBodyRunningHbaItems(DaraModel):
    def __init__(
        self,
        hba_item: List[main_models.DescribePGHbaConfigResponseBodyRunningHbaItemsHbaItem] = None,
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
                temp_model = main_models.DescribePGHbaConfigResponseBodyRunningHbaItemsHbaItem()
                self.hba_item.append(temp_model.from_map(k1))

        return self

class DescribePGHbaConfigResponseBodyRunningHbaItemsHbaItem(DaraModel):
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
        # The IP address of the client.
        self.address = address
        # The name of the database.
        self.database = database
        # The mask of the IP address.
        self.mask = mask
        # The authentication method.
        self.method = method
        # The value of this parameter varies based on the value of the Method parameter. The value is fixed as null.
        self.option = option
        # The priority.
        self.priority_id = priority_id
        # The connection type. Valor:
        # 
        # *   **host**: The record matches TCP/IP connections, including SSL connections and non-SSL connections.
        # *   **hostssl**: The record matches only TCP/IP connections that are established over SSL.
        # *   **hostnossl**: The record matches only TCP/IP connections that are not established over SSL connections.
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

class DescribePGHbaConfigResponseBodyDefaultHbaItems(DaraModel):
    def __init__(
        self,
        hba_item: List[main_models.DescribePGHbaConfigResponseBodyDefaultHbaItemsHbaItem] = None,
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
                temp_model = main_models.DescribePGHbaConfigResponseBodyDefaultHbaItemsHbaItem()
                self.hba_item.append(temp_model.from_map(k1))

        return self

class DescribePGHbaConfigResponseBodyDefaultHbaItemsHbaItem(DaraModel):
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
        # The IP addresses from which the specified users can access the specified databases. The value is fixed as 0.0.0.0/0.
        self.address = address
        # The names of the databases that the specified users are allowed to access. The value is fixed as all or replication.
        self.database = database
        # The mask of the instance. The value is fixed as null.
        self.mask = mask
        # The authentication method. The value is fixed as md5.
        self.method = method
        # The value of this parameter is based on the value of the Method parameter. The value is fixed as null.
        self.option = option
        # The priority of the configuration items in the pg_hba.conf file. This value is automatically generated.
        self.priority_id = priority_id
        # The type of connection to the instance. The value is fixed as host.
        self.type = type
        # The user that is allowed to access the instance. The value is fixed as all.
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

