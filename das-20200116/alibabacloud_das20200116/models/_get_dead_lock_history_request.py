# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeadLockHistoryRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        node_id: str = None,
        page_no: int = None,
        page_size: int = None,
        source: str = None,
        start_time: int = None,
    ):
        # The end time of the query. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # >Notice: 
        # 
        # This parameter is a Long value. To prevent precision loss during serialization and deserialization, make sure that the value does not exceed 9007199254740991.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # > Specify the node ID for a PolarDB for MySQL instance.
        self.node_id = node_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page. The maximum value is **100**.
        self.page_size = page_size
        # The source of the task:
        # 
        # - **MANUAL** or unspecified: queries tasks for recent deadlock analysis.
        # 
        # - **AUTO**: queries tasks for full deadlock analysis.
        # 
        # >Notice: 
        # 
        # If you set this parameter to AUTO to query tasks for full deadlock analysis, the start time can be a maximum of seven days earlier than the end time.
        self.source = source
        # The start time of the query. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # >Notice: 
        # 
        # This parameter is a Long value. To prevent precision loss during serialization and deserialization, make sure that the value does not exceed 9007199254740991.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

