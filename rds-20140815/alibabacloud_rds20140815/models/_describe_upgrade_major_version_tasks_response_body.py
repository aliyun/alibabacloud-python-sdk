# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeUpgradeMajorVersionTasksResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeUpgradeMajorVersionTasksResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of major engine version upgrade tasks.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeUpgradeMajorVersionTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeUpgradeMajorVersionTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        collect_stat_mode: str = None,
        detail: str = None,
        end_time: str = None,
        result: str = None,
        source_ins_name: str = None,
        source_major_version: str = None,
        start_time: str = None,
        switch_end_time: str = None,
        switch_time: str = None,
        target_ins_name: str = None,
        target_major_version: str = None,
        task_id: int = None,
        upgrade_mode: str = None,
        cut_over: bool = None,
        total_logic_rep_delay_time: int = None,
        total_logic_rep_latency_mb: int = None,
        zero_down_time_connection_string: str = None,
        zero_down_time_port: int = None,
    ):
        # The statistics information collection pattern.
        # 
        # Valid values:
        # - **After**: Upgrade after the cutover.
        # - **Before**: Upgrade before the cutover.
        self.collect_stat_mode = collect_stat_mode
        # The detailed information about the task.
        self.detail = detail
        # The end time of the major engine version upgrade.
        # 
        # The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The final result of the task. Valid values:
        # * **Success**: The task is successful.
        # * **Failed**: The task failed.
        # * **Running**: The migration is in progress.
        self.result = result
        # The ID of the original instance before the upgrade.
        self.source_ins_name = source_ins_name
        # The version of the original instance before the upgrade.
        self.source_major_version = source_major_version
        # The start time of the major engine version upgrade.
        # 
        # The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The end time of the instance switchover from the original instance to the new instance.
        # 
        # The value is a UNIX timestamp. Unit: milliseconds.
        self.switch_end_time = switch_end_time
        # The time of the instance switchover from the original instance to the new instance.
        # 
        # The value is a UNIX timestamp. Unit: milliseconds.
        self.switch_time = switch_time
        # The ID of the new instance after the upgrade.
        self.target_ins_name = target_ins_name
        # The major engine version after the upgrade. Valid values:
        # * **10.0**
        # * **11.0**
        # * **12.0**
        # * **13.0**
        # * **14.0**
        # * **15.0**
        self.target_major_version = target_major_version
        # The task ID.
        self.task_id = task_id
        # The upgrade mode.
        # 
        # Valid values:
        # - **clone**: no cutover
        # - **switch**: cutover
        self.upgrade_mode = upgrade_mode
        # Indicates whether a cutover is performed.
        # 
        # - **true**: A cutover is performed.
        # - **false**: No cutover is performed.
        self.cut_over = cut_over
        # The estimated synchronization time for the logical replication lag. Unit: seconds.
        # > This parameter is used only for **zero-downtime** major engine version upgrades.
        self.total_logic_rep_delay_time = total_logic_rep_delay_time
        # The size of the logical replication lag. Unit: MB.
        # 
        # > This parameter is used only for **zero-downtime** major engine version upgrades.
        self.total_logic_rep_latency_mb = total_logic_rep_latency_mb
        # The temporary internal endpoint of the higher-version instance for the zero-downtime major engine version upgrade. The format is `****.pg.rds.aliyuncs.com`.
        # > This parameter is used only for **zero-downtime** major engine version upgrades.
        self.zero_down_time_connection_string = zero_down_time_connection_string
        # The port of the higher-version instance, which is the same as the port of the source instance.
        # > This parameter is used only for **zero-downtime** major engine version upgrades.
        self.zero_down_time_port = zero_down_time_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collect_stat_mode is not None:
            result['CollectStatMode'] = self.collect_stat_mode

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.result is not None:
            result['Result'] = self.result

        if self.source_ins_name is not None:
            result['SourceInsName'] = self.source_ins_name

        if self.source_major_version is not None:
            result['SourceMajorVersion'] = self.source_major_version

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.switch_end_time is not None:
            result['SwitchEndTime'] = self.switch_end_time

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.target_ins_name is not None:
            result['TargetInsName'] = self.target_ins_name

        if self.target_major_version is not None:
            result['TargetMajorVersion'] = self.target_major_version

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode

        if self.cut_over is not None:
            result['cutOver'] = self.cut_over

        if self.total_logic_rep_delay_time is not None:
            result['totalLogicRepDelayTime'] = self.total_logic_rep_delay_time

        if self.total_logic_rep_latency_mb is not None:
            result['totalLogicRepLatencyMB'] = self.total_logic_rep_latency_mb

        if self.zero_down_time_connection_string is not None:
            result['zeroDownTimeConnectionString'] = self.zero_down_time_connection_string

        if self.zero_down_time_port is not None:
            result['zeroDownTimePort'] = self.zero_down_time_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectStatMode') is not None:
            self.collect_stat_mode = m.get('CollectStatMode')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SourceInsName') is not None:
            self.source_ins_name = m.get('SourceInsName')

        if m.get('SourceMajorVersion') is not None:
            self.source_major_version = m.get('SourceMajorVersion')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SwitchEndTime') is not None:
            self.switch_end_time = m.get('SwitchEndTime')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TargetInsName') is not None:
            self.target_ins_name = m.get('TargetInsName')

        if m.get('TargetMajorVersion') is not None:
            self.target_major_version = m.get('TargetMajorVersion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')

        if m.get('cutOver') is not None:
            self.cut_over = m.get('cutOver')

        if m.get('totalLogicRepDelayTime') is not None:
            self.total_logic_rep_delay_time = m.get('totalLogicRepDelayTime')

        if m.get('totalLogicRepLatencyMB') is not None:
            self.total_logic_rep_latency_mb = m.get('totalLogicRepLatencyMB')

        if m.get('zeroDownTimeConnectionString') is not None:
            self.zero_down_time_connection_string = m.get('zeroDownTimeConnectionString')

        if m.get('zeroDownTimePort') is not None:
            self.zero_down_time_port = m.get('zeroDownTimePort')

        return self

