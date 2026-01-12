# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppInstancesRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        dbinstance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The ID of the RDS for PostgreSQL instance with which the RDS Supabase instances are associated. If you specify this parameter, the RDS Supabase instances associated with the specified RDS for PostgreSQL instance are queried.
        self.app_type = app_type
        # The region ID.
        self.dbinstance_name = dbinstance_name
        # The number of records per page. Valid values: **1 to 50**.
        self.page_number = page_number
        # The application type. Only **supabase** is supported. For more information, see [RDS Supabase](https://help.aliyun.com/document_detail/2938735.html).
        self.page_size = page_size
        # The operation that you want to perform. Set the value to **DescribeAppInstances**.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

