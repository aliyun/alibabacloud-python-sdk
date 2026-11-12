# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAIDBClusterTaskLogFilesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        log_type: str = None,
        page_number: int = None,
        page_size: int = None,
        relative_dbcluster_id: str = None,
        reverse: bool = None,
        start_time: str = None,
    ):
        # The instance ID of the model operator.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The log type. Valid values:
        # 
        # - **sls**
        # 
        # This parameter is required.
        self.log_type = log_type
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**. Default value: **100**.
        self.page_size = page_size
        # The instance ID of the associated PolarDB instance.
        self.relative_dbcluster_id = relative_dbcluster_id
        # Specifies whether to sort the results in descending order. Default value: *false*.
        self.reverse = reverse
        # The start time of the query. Specify the time in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.relative_dbcluster_id is not None:
            result['RelativeDBClusterId'] = self.relative_dbcluster_id

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RelativeDBClusterId') is not None:
            self.relative_dbcluster_id = m.get('RelativeDBClusterId')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

