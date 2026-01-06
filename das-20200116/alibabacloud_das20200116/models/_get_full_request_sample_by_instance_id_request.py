# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFullRequestSampleByInstanceIdRequest(DaraModel):
    def __init__(
        self,
        end: int = None,
        instance_id: str = None,
        role: str = None,
        sql_id: str = None,
        start: int = None,
        user_id: str = None,
    ):
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time. The interval between the start time and the end time must be equal to or greater than 1 hour.
        # 
        # This parameter is required.
        self.end = end
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The role of the PolarDB-X 2.0 node. Valid values:
        # 
        # *   **polarx_cn**: compute node.
        # *   **polarx_en**: data node.
        self.role = role
        # The SQL statement ID.
        # 
        # This parameter is required.
        self.sql_id = sql_id
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The start time must be within the storage duration of the SQL Explorer feature of the database instance, and can be up to 90 days earlier than the current time.
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
        if self.end is not None:
            result['End'] = self.end

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.role is not None:
            result['Role'] = self.role

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.start is not None:
            result['Start'] = self.start

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

