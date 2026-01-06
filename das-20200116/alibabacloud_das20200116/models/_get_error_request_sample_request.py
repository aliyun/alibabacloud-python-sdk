# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetErrorRequestSampleRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        end: int = None,
        instance_id: str = None,
        node_id: str = None,
        sql_id: str = None,
        start: int = None,
    ):
        # The name of the database.
        self.db_name = db_name
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time. The interval cannot exceed 24 hours.
        self.end = end
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # >  You must specify the node ID if your database instance is a PolarDB for MySQL cluster.
        self.node_id = node_id
        # The SQL query ID. You can call the [GetAsyncErrorRequestListByCode](https://help.aliyun.com/document_detail/410746.html) operation to query the ID of the SQL query for which MySQL error code is returned.
        self.sql_id = sql_id
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The start time must be within the storage duration of the SQL Explorer feature of the database instance, and can be up to 90 days earlier than the current time.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.end is not None:
            result['End'] = self.end

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

