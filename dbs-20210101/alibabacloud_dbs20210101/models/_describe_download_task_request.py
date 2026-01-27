# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDownloadTaskRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        cluster_name: str = None,
        current_page: str = None,
        datasource_id: str = None,
        end_time: str = None,
        instance_name: str = None,
        order_column: str = None,
        order_direct: str = None,
        page_size: str = None,
        region_code: str = None,
        start_time: str = None,
        state: str = None,
        task_type: str = None,
    ):
        # The ID of the backup set generated when you create a download task. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the ID.
        self.backup_set_id = backup_set_id
        self.cluster_name = cluster_name
        # The page number of the page to return.
        self.current_page = current_page
        # The ID of the Database Backup (DBS) data source. Specify the parameter in the format of *ds-${Instance ID}_${regionId}*.
        self.datasource_id = datasource_id
        # The end of the time range to query. Specify this parameter as a timestamp of the LONG type. Unit: milliseconds.
        self.end_time = end_time
        # The ID of the instance.
        # 
        # > This parameter is required.
        self.instance_name = instance_name
        # The column based on which the entries are sorted. By default, the entries are sorted by the time when the download task was created. Set the value to **gmt_create**.
        self.order_column = order_column
        # The order in which you want to sort the entries. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order_direct = order_direct
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/26231.html) operation to query the region ID of the instance.
        # 
        # This parameter is required.
        self.region_code = region_code
        # The beginning of the time range to query. Specify this parameter as a timestamp of the LONG type. Unit: milliseconds.
        self.start_time = start_time
        # The state of the download task. Valid values:
        # 
        # *   **Initializing**: The download task is being initialized.
        # *   **queueing**: The download task is queuing.
        # *   **running**: The download task is running.
        # *   **failed**: The download task fails.
        # *   **finished**: The download task is complete.
        # *   **expired**: The download task expires.
        self.state = state
        # The type of the download task. Valid values:
        # 
        # *   **full**: downloads a full backup set.
        # *   **pitr**: downloads a backup set at a specific point in time.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_direct is not None:
            result['OrderDirect'] = self.order_direct

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderDirect') is not None:
            self.order_direct = m.get('OrderDirect')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

