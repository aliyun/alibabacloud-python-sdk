# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProcessListRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        keyword: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        running_time: int = None,
        show_full: bool = None,
        user: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The keyword in an SQL statement, which is used to filter queries. Set the value to **SELECT**.
        self.keyword = keyword
        # The order in which queries are sorted based on the specified fields. Specify this parameter as an ordered JSON array in the `[{"Field":"Time","Type":"Desc" },{ "Field":"User", "Type":"Asc" }]` format.
        # 
        # *   **Field** specifies the field used to sort queries. Valid values: Time, User, Host, and DB.
        # *   **Type** specifies the sorting sequence. Valid values: **Desc** and **Asc**.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The execution duration used to filter queries. Queries that take a longer time than the specified execution duration are displayed. Unit: seconds.
        self.running_time = running_time
        # Specifies whether to show a complete SQL statement. Valid values:
        # 
        # *   **True**: shows a complete SQL statement.
        # *   **False**: shows only the first 100 characters of an SQL statement.
        # 
        # >  The default value is False.
        self.show_full = show_full
        # The name of the user used to filter queries.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.running_time is not None:
            result['RunningTime'] = self.running_time

        if self.show_full is not None:
            result['ShowFull'] = self.show_full

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')

        if m.get('ShowFull') is not None:
            self.show_full = m.get('ShowFull')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

