# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBlockingDetailListRequest(DaraModel):
    def __init__(
        self,
        db_name_list: str = None,
        end_time: str = None,
        instance_id: str = None,
        page_no: str = None,
        page_size: str = None,
        query_hash: str = None,
        start_time: str = None,
    ):
        # The name of the database. Separate multiple database names with commas (,).
        self.db_name_list = db_name_list
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the database instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. The value must be an integer that is greater than 0. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. The value must be an integer that is greater than 0. Default value: 10.
        self.page_size = page_size
        # The hash value of the SQL statement. The hash values of SQL statements of the same type are the same.
        self.query_hash = query_hash
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name_list is not None:
            result['DbNameList'] = self.db_name_list

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_hash is not None:
            result['QueryHash'] = self.query_hash

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbNameList') is not None:
            self.db_name_list = m.get('DbNameList')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryHash') is not None:
            self.query_hash = m.get('QueryHash')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

