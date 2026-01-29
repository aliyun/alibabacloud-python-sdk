# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserOmsDataRequest(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        end_time: str = None,
        marker: str = None,
        owner_id: int = None,
        page_size: int = None,
        start_time: str = None,
        table: str = None,
    ):
        # The time type of the usage data. Set the parameter based on the description in the documentation of the specified service. Valid values:
        # 
        # *   Raw
        # *   Hour
        # *   Day
        # *   Month
        # 
        # This parameter is required.
        self.data_type = data_type
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the record from which the usage data starts to return. The usage data records whose names are alphabetically after the value of the Marker parameter are returned. By default, the usage data starts to return from the earliest record.
        self.marker = marker
        self.owner_id = owner_id
        # The number of entries to return on each page. Valid values: 1 to 200. Default value: 100.
        self.page_size = page_size
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The service whose usage data you want to query and the details of the usage data. The parameter value is usually set to the code of a service. Various usage models are provided for different services.
        # 
        # This parameter is required.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

