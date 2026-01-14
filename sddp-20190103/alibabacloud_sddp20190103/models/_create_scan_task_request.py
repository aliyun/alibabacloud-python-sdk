# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScanTaskRequest(DaraModel):
    def __init__(
        self,
        data_limit_id: int = None,
        feature_type: int = None,
        interval_day: int = None,
        lang: str = None,
        oss_scan_path: str = None,
        resource_type: int = None,
        run_hour: int = None,
        run_minute: int = None,
        scan_range: int = None,
        scan_range_content: str = None,
        source_ip: str = None,
        task_name: str = None,
        task_user_name: str = None,
    ):
        # The unique ID of the data asset, such as an instance, a database, and a bucket. You can call the [DescribeDataLimits](~~DescribeDataLimits~~) operation to query the unique ID.
        # 
        # This parameter is required.
        self.data_limit_id = data_limit_id
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The interval between two consecutive custom scan tasks. Unit: days. Valid values: 1 to 2147483648.
        # 
        # This parameter is required.
        self.interval_day = interval_day
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The data to be scanned in the Object Storage Service (OSS) bucket. Prefix match, suffix match, and regular expression match are supported.
        self.oss_scan_path = oss_scan_path
        # The type of the service to which the data assets to be scanned belong. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The time when the scan task is executed next time. Unit: hours.
        # 
        # This parameter is required.
        self.run_hour = run_hour
        # The time when the scan task is executed next time. Unit: minutes.
        # 
        # This parameter is required.
        self.run_minute = run_minute
        # The matching rule that specifies the scan scope of the custom scan task. This parameter takes effect only if you set the **ScanRangeContent** parameter. Valid values:
        # 
        # *   **0**: exact match
        # *   **1**: prefix match
        # *   **2**: suffix match
        # *   **3**: regular expression match
        # 
        # This parameter is required.
        self.scan_range = scan_range
        # The data to be scanned in a structured data asset. Prefix match, suffix match, and regular expression match are supported.
        # 
        # This parameter is required.
        self.scan_range_content = scan_range_content
        # This parameter is deprecated.
        self.source_ip = source_ip
        # The name of the scan task.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The account that is used to create the scan task.
        self.task_user_name = task_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_limit_id is not None:
            result['DataLimitId'] = self.data_limit_id

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.interval_day is not None:
            result['IntervalDay'] = self.interval_day

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.oss_scan_path is not None:
            result['OssScanPath'] = self.oss_scan_path

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.run_hour is not None:
            result['RunHour'] = self.run_hour

        if self.run_minute is not None:
            result['RunMinute'] = self.run_minute

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.scan_range_content is not None:
            result['ScanRangeContent'] = self.scan_range_content

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_user_name is not None:
            result['TaskUserName'] = self.task_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLimitId') is not None:
            self.data_limit_id = m.get('DataLimitId')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('IntervalDay') is not None:
            self.interval_day = m.get('IntervalDay')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OssScanPath') is not None:
            self.oss_scan_path = m.get('OssScanPath')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RunHour') is not None:
            self.run_hour = m.get('RunHour')

        if m.get('RunMinute') is not None:
            self.run_minute = m.get('RunMinute')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('ScanRangeContent') is not None:
            self.scan_range_content = m.get('ScanRangeContent')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskUserName') is not None:
            self.task_user_name = m.get('TaskUserName')

        return self

