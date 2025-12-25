# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceLoginAuditLogRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        op_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_name: str = None,
        start_time: str = None,
        tid: int = None,
    ):
        # The end of the time range to query.
        # 
        # >  The end time supports fuzzy match. Specify the time in the YYYY-MM-DD hh:mm:ss format. We recommend that you use the StartTime and EndTime parameters to specify a time range that does not exceed one day. This way, the returned entries can be displayed by page to increase query efficiency.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The alias of the user.
        self.op_user_name = op_user_name
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100.
        self.page_size = page_size
        # The name of the database or instance whose logon records you want to query.
        # 
        # >  If SQL statements are executed at the instance level, you can set this parameter to an instance name. If SQL statements are executed at the database level, you can set this parameter to a database name.
        self.search_name = search_name
        # The beginning of the time range to query.
        # 
        # >  The start time supports fuzzy match. Specify the time in the YYYY-MM-DD hh:mm:ss format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.op_user_name is not None:
            result['OpUserName'] = self.op_user_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OpUserName') is not None:
            self.op_user_name = m.get('OpUserName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

