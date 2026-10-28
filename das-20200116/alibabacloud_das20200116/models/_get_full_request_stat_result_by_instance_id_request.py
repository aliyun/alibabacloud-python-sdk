# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFullRequestStatResultByInstanceIdRequest(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        db_name: str = None,
        end: int = None,
        instance_id: str = None,
        keyword: str = None,
        node_id: str = None,
        order_by: str = None,
        origin_host: str = None,
        page_no: int = None,
        page_size: int = None,
        role: str = None,
        sql_id: str = None,
        sql_type: str = None,
        start: int = None,
        user_id: str = None,
    ):
        # Specifies whether to sort the results in ascending order. Default value: false.
        self.asc = asc
        # The name of the database.
        self.db_name = db_name
        # The end time of the query. The time is a UNIX timestamp in milliseconds.
        # 
        # > The end time must be later than the start time, and the interval between the start time and the end time cannot exceed one day.
        # 
        # This parameter is required.
        self.end = end
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The query keyword.
        self.keyword = keyword
        # The node ID.
        # 
        # > For PolarDB for MySQL instances, the node ID is required.
        self.node_id = node_id
        # The field by which to sort the results. Default value: **count**.
        # 
        # - **count**: the number of executions.
        # 
        # - **avgRt**: the average execution time.
        # 
        # - **rtRate**: the execution time proportion.
        # 
        # - **rowsExamined**: the total number of scanned rows.
        # 
        # - **avgRowsExamined**: the average number of scanned rows.
        # 
        # - **avgRowsReturned**: the average number of returned rows.
        self.order_by = order_by
        # The IP address of the client that executed the SQL statement.
        # 
        # > This parameter is optional. If you specify a client IP address, the full request data of the specified client IP address is aggregated. If you leave this parameter empty, the full request data of the entire database instance is aggregated.
        self.origin_host = origin_host
        # The page number for the paged query. The paging starts from 1. Default value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The data volume per page for paging in a paged query. Default value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The node information of the PolarDB-X 2.0 database instance. Valid values:
        # 
        # - **polarx_cn**: compute node.
        # 
        # - **polarx_dn**: data node.
        self.role = role
        # The SQL ID.
        # 
        # > If you specify an SQL ID, the full request data of the specified SQL ID is aggregated. If you leave this parameter empty, the full request data of the entire database instance is aggregated.
        self.sql_id = sql_id
        # The type of the SQL statement. Valid values: **SELECT**, **INSERT**, **UPDATE**, **DELETE**, **LOGIN**, **LOGOUT**, **MERGE**, **ALTER**, **CREATEINDEX**, **DROPINDEX**, **CREATE**, **DROP**, **SET**, **DESC**, **REPLACE**, **CALL**, **BEGIN**, **DESCRIBE**, **ROLLBACK**, **FLUSH**, **USE**, **SHOW**, **START**, **COMMIT**, and **RENAME**.
        # 
        # > If the database instance is an ApsaraDB RDS for MySQL, PolarDB for MySQL, or PolarDB-X 2.0 instance, you can aggregate data by SQL statement type.
        self.sql_type = sql_type
        # The start time of the query. The format is a UNIX timestamp, in milliseconds.
        # 
        # > The start time must be within the SQL Explorer storage duration for the database instance and cannot be more than 90 days earlier than the current time.
        # 
        # This parameter is required.
        self.start = start
        # The instance ID, which is the ID of the Alibaba Cloud account that created the database instance.
        # 
        # > This parameter is optional. After you enter the ID of the target database instance, the system automatically obtains the instance ID when you call the API operation.
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

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.end is not None:
            result['End'] = self.end

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.origin_host is not None:
            result['OriginHost'] = self.origin_host

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role is not None:
            result['Role'] = self.role

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

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

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OriginHost') is not None:
            self.origin_host = m.get('OriginHost')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

