# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeJobResourceUsageRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        spark_app_name: str = None,
        start_time: str = None,
    ):
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. The end time must be later than the start time. Format: <i>yyyy-MM-ddTHH:mm:ssZ</i> (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The page number. The value must be a positive integer. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # - 30
        # - 50
        # - 100
        # 
        # Default value: 30.
        self.page_size = page_size
        self.spark_app_name = spark_app_name
        # The start time of the query. Format: <i>yyyy-MM-ddTHH:mm:ssZ</i> (UTC).
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.spark_app_name is not None:
            result['SparkAppName'] = self.spark_app_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SparkAppName') is not None:
            self.spark_app_name = m.get('SparkAppName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

