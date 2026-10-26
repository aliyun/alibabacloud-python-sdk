# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperationDatabaseAccountsRequest(DaraModel):
    def __init__(
        self,
        database_account_name: str = None,
        database_id: str = None,
        instance_id: str = None,
        operation_project_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The name of the database account. Exact match.
        self.database_account_name = database_account_name
        # The database instance ID.
        # > You can invoke the [ListOperationDatabases](https://help.aliyun.com/document_detail/2758856.html) operation to obtain this parameter.
        self.database_id = database_id
        # The ID of the Bastionhost instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The project ID.
        self.operation_project_id = operation_project_id
        # The page number of the current page for a paged query. Default value: **1**.
        self.page_number = page_number
        # The maximum number of entries to return on each page for a paged query.
        # <br>The maximum value of the PageSize parameter is 100. The default number of entries returned per page is 20. If the PageSize parameter is left empty, 20 entries are returned by default.
        # 
        # > Do not leave the PageSize parameter empty.
        self.page_size = page_size
        # The region ID of the Bastionhost instance.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operation_project_id is not None:
            result['OperationProjectId'] = self.operation_project_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperationProjectId') is not None:
            self.operation_project_id = m.get('OperationProjectId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

