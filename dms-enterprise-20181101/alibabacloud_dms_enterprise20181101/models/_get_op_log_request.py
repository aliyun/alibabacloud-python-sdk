# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOpLogRequest(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        end_time: str = None,
        module: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        tid: int = None,
        user_nick: str = None,
    ):
        # DatabaseName.
        self.database_name = database_name
        # The end of the time range to query. Specify the time in the yyyy-MM-DD HH:mm:ss format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The functional module for which you want to query operation logs. If you do not specify this parameter, operation logs for all functional modules are returned. Valid values:
        # 
        # *   **PERMISSION**: permissions
        # *   **OWNER**: data owner
        # *   **SQL_CONSOLE**: data query
        # *   **SQL_CONSOLE_EXPORT**: query result export
        # *   **DATA_CHANGE**: data change
        # *   **DATA_EXPORT**: data export
        # *   **SQL_REVIEW**: SQL review
        # *   **DT_SYNC**: database and table synchronization
        # *   **DT_DETAIL**: database and table details
        # *   **DB_TASK**: task management
        # *   **INSTANCE_MANAGE**: instance management
        # *   **USER_MANAGE**: user management
        # *   **SECURITY_RULE**: security rules
        # *   **CONFIG_MANAGE**: configuration management
        # *   **RESOURCE_AUTH**: resource authorization
        # *   **ACCESS_WHITE_IP**: access IP address whitelist
        # *   **NDDL**: schema design
        # *   **DSQL_CONSOLE**: cross-database data query
        # *   **DSQL_CONSOLE_EXPORT**: cross-database query result export
        # *   **DATA_TRACT**: data tracking
        # *   **DATA_QUALITY**: data quality
        # *   **DATALINK_MANAGE** :DBLink management
        # *   **DATASEC_MANAGE**: sensitive data management
        # *   **SELL**: sales
        self.module = module
        # The number of the page to return. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        # 
        # This parameter is required.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the yyyy-MM-DD HH:mm:ss format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid
        # UserNick.
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.module is not None:
            result['Module'] = self.module

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

