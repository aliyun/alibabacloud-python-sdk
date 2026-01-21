# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatabasesForUserGroupRequest(DaraModel):
    def __init__(
        self,
        database_address: str = None,
        database_name: str = None,
        database_type: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The address of the database to query. Only exact match is supported.
        self.database_address = database_address
        # The name of the database to query.
        self.database_name = database_name
        # The engine of the database to query. Valid values:
        # 
        # *   **MySQL**
        # *   **Oracle**
        # *   **PostgreSQL**
        # *   **SQLServer**
        self.database_type = database_type
        # The bastion host ID.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.network_domain_id = network_domain_id
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.\\
        # Valid values: 1 to 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the user group to query.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_address is not None:
            result['DatabaseAddress'] = self.database_address

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAddress') is not None:
            self.database_address = m.get('DatabaseAddress')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

