# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFullRequestOriginStatByInstanceIdRequest(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        end: int = None,
        instance_id: str = None,
        node_id: str = None,
        order_by: str = None,
        page_no: int = None,
        page_size: int = None,
        role: str = None,
        sql_type: str = None,
        start: int = None,
        user_id: str = None,
    ):
        # Specifies whether to sort the results in ascending order. By default, the results are not sorted in ascending order.
        self.asc = asc
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time. The interval between the start time and the end time cannot exceed 24 hours.
        # 
        # This parameter is required.
        self.end = end
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # >  This parameter must be specified if the database instance is a PolarDB for MySQL cluster.
        self.node_id = node_id
        # The field by which the results to be returned are sorted. Default value: **count**. Valid values:
        # 
        # *   **count**: the number of executions.
        # *   **avgRt**: the average execution duration.
        # *   **rtRate**: the execution duration percentage.
        # *   **rowsExamined**: the total number of scanned rows.
        # *   **avgRowsExamined**: the average number of scanned rows.
        # *   **avgRowsReturned**: the average number of returned rows.
        self.order_by = order_by
        # The page number. Pages start from page 1. Default value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Default value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The role of the PolarDB-X 2.0 node. Valid values:
        # 
        # *   **polarx_cn**: compute node.
        # *   **polarx_en**: data node.
        self.role = role
        # The type of the SQL statement. Valid values: **SELECT**, **INSERT**, **UPDATE**, **DELETE**, **MERGE**, **ALTER**, **CREATEINDEX**, **DROPINDEX**, **CREATE**, **DROP**, **SET**, **DESC**, **REPLACE**, **CALL**, **BEGIN**, **DESCRIBE**, **ROLLBACK**, **FLUSH**, **USE**, **SHOW**, **START**, **COMMIT**, and **RENAME**.
        # 
        # >  If the database instance is an ApsaraDB RDS for MySQL instance, a PolarDB for MySQL instance, or a PolarDB-X 2.0 instance, statistics can be collected based on the SQL statement type.
        self.sql_type = sql_type
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The start time must be within the storage duration of the SQL Explorer of the database instance, and can be up to 90 days earlier than the current time.
        # 
        # This parameter is required.
        self.start = start
        # The ID of the Alibaba Cloud account that is used to create the database instance.
        # 
        # >  This parameter is optional. The system can automatically obtain the account ID based on the value of InstanceId when you call this operation.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['Asc'] = self.asc

        if self.end is not None:
            result['End'] = self.end

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role is not None:
            result['Role'] = self.role

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start is not None:
            result['Start'] = self.start

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

