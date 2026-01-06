# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQueryOptimizeExecErrorStatsRequest(DaraModel):
    def __init__(
        self,
        asc: str = None,
        db_names: str = None,
        engine: str = None,
        instance_ids: str = None,
        keywords: str = None,
        logical_operator: str = None,
        order_by: str = None,
        page_no: str = None,
        page_size: str = None,
        region: str = None,
        time: str = None,
    ):
        # Specifies whether to sort the returned entries in ascending order. Default value: **true**. Valid values:
        # 
        # *   **true**: sorts the returned entries in ascending order.
        # *   **false**: does not sort the returned entries in ascending order.
        self.asc = asc
        # The name of the database to be queried.
        self.db_names = db_names
        # The database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **PolarDBMySQL**
        # *   **PostgreSQL**
        # 
        # This parameter is required.
        self.engine = engine
        # The instance IDs. Separate multiple IDs with commas (,).
        self.instance_ids = instance_ids
        # The keywords of the SQL template. Separate multiple keywords with spaces.
        self.keywords = keywords
        # The logical relationship between multiple keywords. Valid values:
        # 
        # *   **or**
        # *   **and**
        self.logical_operator = logical_operator
        # The field by which to sort the returned entries. Only error_count is supported, which specifies that the entries are sorted based on the number of failed executions.
        self.order_by = order_by
        # The page number. Pages start from page 1. Default value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region in which the instance resides. Valid values:
        # 
        # *   **cn-china**: Chinese mainland
        # *   **cn-hongkong**: China (Hong Kong)
        # *   **ap-southeast-1**: Singapore
        # 
        # This parameter takes effect only if **InstanceIds** is left empty. If you leave **InstanceIds** empty, the system obtains data from the region set by **Region**. By default, Region is set to **cn-china**. If you specify **InstanceIds**, **Region** does not take effect and the system obtains data from the region in which the first specified instance resides.****
        # 
        # >  Set this parameter to **cn-china** for the instances that are created in the regions in the Chinese mainland.
        self.region = region
        # The time range to query. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        # 
        # This parameter is required.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['Asc'] = self.asc

        if self.db_names is not None:
            result['DbNames'] = self.db_names

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')

        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

