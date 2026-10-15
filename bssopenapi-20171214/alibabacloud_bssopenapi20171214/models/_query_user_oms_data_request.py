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
        # The data timestamp type of the metering data. Refer to the specific service documentation for details. Valid values:
        # - Raw: hourly
        # - Hour: hourly
        # - Day: daily
        # - Month: monthly
        # 
        # This parameter is required.
        self.data_type = data_type
        # The end time of the request.
        # 
        # The date format must comply with the ISO 8601 standard and use UTC time. Format: yyyy-mm-ddThh:mm:ssZ.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The marker that specifies the starting point for returning results in alphabetical order after the NextToken. By default, results are returned from the beginning.
        self.marker = marker
        self.owner_id = owner_id
        # The number of rows per page for paging in a paged query. Valid values: 1 to 200. Default value: 100.
        self.page_size = page_size
        # The start time of the request.
        # 
        # The date format must comply with the ISO 8601 standard and use UTC time. Format: yyyy-mm-ddThh:mm:ssZ.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The product and detail information for the usage data, which is typically the ProductCode. Different services support multiple metering models.
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

