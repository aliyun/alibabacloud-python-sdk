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
        # The unique ID of the data asset such as an instance, database, or bucket. You can call [DescribeDataLimits](~~DescribeDataLimits~~) to obtain the ID.
        # 
        # This parameter is required.
        self.data_limit_id = data_limit_id
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The interval in days between two consecutive custom scan tasks. Valid values: 1 to 2147483648.
        # 
        # This parameter is required.
        self.interval_day = interval_day
        # The language of the request and response. Valid values:
        # 
        # - **zh**: Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The scan scope for OSS assets. Prefix match, suffix match, and regular expression match are supported.
        self.oss_scan_path = oss_scan_path
        # The resource type of the product to query. Valid values:
        # - **1**: MaxCompute.
        # - **2**: OSS.
        # - **3**: ADS.
        # - **4**: OTS.
        # - **5**: RDS.
        # - **6**: SELF_DB.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The runtime of the next scan task. Unit: hours.
        # 
        # This parameter is required.
        self.run_hour = run_hour
        # The runtime of the next scan task. Unit: minutes.
        # 
        # This parameter is required.
        self.run_minute = run_minute
        # The scan scope matching rule for the custom scan task. This parameter takes effect only when used together with **ScanRangeContent**. Valid values:
        # - **0**: full match.
        # - **1**: prefix match.
        # - **2**: suffix match.
        # - **3**: regular expression match.
        # 
        # This parameter is required.
        self.scan_range = scan_range
        # The content to match within the scan scope of structured data assets by using prefix match, suffix match, or regular expression match.
        # 
        # > When ScanRange is set to 0, all content in this field is fully matched. When ScanRange is set to 1, the content in this field is matched by prefix. For example, if this field is set to test/abc, file paths that start with test/abc are matched. When ScanRange is set to 2, the content in this field is matched by suffix. When ScanRange is set to 3, the content in this field is matched by regular expression.
        # 
        # This parameter is required.
        self.scan_range_content = scan_range_content
        # This parameter is deprecated.
        self.source_ip = source_ip
        # The name of the scan task.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The account that creates the scan task.
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

