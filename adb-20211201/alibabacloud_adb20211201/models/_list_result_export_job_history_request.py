# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListResultExportJobHistoryRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        database_user: str = None,
        end_time: str = None,
        order: main_models.ListResultExportJobHistoryRequestOrder = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        resource_group: str = None,
        start_time: str = None,
        status_list: List[str] = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database account.
        self.database_user = database_user
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time.
        self.end_time = end_time
        # The order in which to sort the SQL statements by field, which contains the `Field` and `Type` fields. Specify the order in the JSON format. Example: `[{"Field":"CreateTimee", "Type": "desc" }]`.
        # 
        # *   `Field` specifies the field that is used to sort the SQL statements. Valid values:
        # 
        #     *   `CreateTime`: the time when the result set export job was created.
        #     *   `Status`: the execution status.
        #     *   `DatabaseUser`: the name of the database account.
        #     *   `TimeCost`: the execution duration.
        #     *   `ResourceGroup`: the name of the resource group.
        #     *   `ExportRows`: the number of exported rows.
        #     *   `Progress`: the export progress.
        # 
        # *   `Type` specifies the sorting order. Valid values (case-insensitive):
        # 
        #     *   `Desc`: descending order.
        #     *   `Asc`: ascending order.
        self.order = order
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the resource group that runs the result set export jobs. You can use this parameter to query the execution records of export jobs that are run in a specific resource group.
        self.resource_group = resource_group
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        self.start_time = start_time
        # The execution status of result set export jobs. You can use this parameter to query the execution records of export jobs that are in a specific state.
        self.status_list = status_list

    def validate(self):
        if self.order:
            self.order.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.order is not None:
            result['Order'] = self.order.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Order') is not None:
            temp_model = main_models.ListResultExportJobHistoryRequestOrder()
            self.order = temp_model.from_map(m.get('Order'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

class ListResultExportJobHistoryRequestOrder(DaraModel):
    def __init__(
        self,
        field: str = None,
        type: str = None,
    ):
        # The field that is used to sort the SQL statements. Valid values:
        # 
        # *   CreateTime
        # *   DatabaseUser
        # *   TimeCost
        # *   ResourceGroup
        # *   Status
        # *   Progress
        # *   ExportRows
        self.field = field
        # The sorting order. Valid values (case-insensitive):
        # 
        # *   **Desc**: descending order.
        # *   **Asc**: ascending order.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

