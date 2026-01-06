# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPfsSqlSummariesRequest(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        end_time: int = None,
        instance_id: str = None,
        keywords: str = None,
        node_id: str = None,
        order_by: str = None,
        page_no: int = None,
        page_size: int = None,
        sql_id: str = None,
        start_time: int = None,
    ):
        # Specifies whether to sort the returned entries in ascending order. Default value: **false**. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.asc = asc
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time. You can view the data of up to seven days within the last month.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The keywords of the SQL template. Separate multiple keywords with spaces.
        self.keywords = keywords
        # The node ID.
        # 
        # >  This parameter is required if the database instance is an ApsaraDB RDS for MySQL Cluster Edition instance or a PolarDB for MySQL cluster.
        self.node_id = node_id
        # The field by which to sort the returned entries. Default value: **count**.
        # 
        # *   **count**: the number of executions.
        # *   **avgRt**: the average execution duration.
        # *   **rtRate**: the execution duration percentage.
        # *   **rowsExamined**: the total number of scanned rows.
        # *   **avgRowsExamined**: the average number of scanned rows.
        # *   **avgRowsReturned**: the average number of returned rows.
        self.order_by = order_by
        # The page number. Pages start from page 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Valid values: 1 to 100.
        self.page_size = page_size
        # The SQL ID.
        # 
        # >  If this parameter is specified, the full request statistics of the specified SQL query are collected. If this parameter is left empty, the full request statistics of the entire database instance are collected.
        self.sql_id = sql_id
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['Asc'] = self.asc

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

