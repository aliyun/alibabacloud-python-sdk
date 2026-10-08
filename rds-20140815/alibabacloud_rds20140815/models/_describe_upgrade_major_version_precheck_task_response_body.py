# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeUpgradeMajorVersionPrecheckTaskResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeUpgradeMajorVersionPrecheckTaskResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The property list of the major engine version upgrade check report. Each attribute column contains the details of a check report entry.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the upgrade check report.
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
                temp_model = main_models.DescribeUpgradeMajorVersionPrecheckTaskResponseBodyItems()
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

class DescribeUpgradeMajorVersionPrecheckTaskResponseBodyItems(DaraModel):
    def __init__(
        self,
        check_time: str = None,
        detail: str = None,
        effective_time: str = None,
        recommend_disk_size: int = None,
        recommend_least_mem_size: int = None,
        recommend_mem_size: int = None,
        result: str = None,
        source_major_version: str = None,
        target_major_version: str = None,
        task_id: int = None,
        upgrade_mode: str = None,
    ):
        # The check time.
        # 
        # The value is a UNIX timestamp. Unit: milliseconds.
        self.check_time = check_time
        # The content of the major engine version upgrade check report.
        self.detail = detail
        # The expiration time of the check report.
        # 
        # The value is a UNIX timestamp. Unit: milliseconds.
        self.effective_time = effective_time
        # The recommended minimum disk capacity for the upgrade. Unit: GB.
        # 
        # > This parameter is returned only for ApsaraDB RDS for PostgreSQL instances.
        self.recommend_disk_size = recommend_disk_size
        # The recommended minimum memory for the upgrade. Unit: GB.
        # 
        # > This parameter is returned only for ApsaraDB RDS for PostgreSQL instances.
        self.recommend_least_mem_size = recommend_least_mem_size
        # The recommended memory for the upgrade. Unit: GB.
        # 
        # If the memory of the instance is greater than or equal to the recommended memory, the upgrade is performed at the fastest speed to minimize the read-only duration of the instance.
        # 
        # > This parameter is returned only for ApsaraDB RDS for PostgreSQL instances.
        self.recommend_mem_size = recommend_mem_size
        # The result of major engine version upgrade check.
        # 
        # Valid values:
        # - Success: The check is passed.
        # - Fail: The check failed.
        # - warning: The check returned warnings. Review the report to determine whether to proceed with the upgrade.
        # 
        # > If the check result is **Fail**, check the value of the **Detail** parameter, resolve the errors, and try again. For common errors and solutions, see [Understand major engine version upgrade check report for ApsaraDB RDS for PostgreSQL](https://help.aliyun.com/document_detail/218391.html).
        self.result = result
        # The current major engine version of the instance.
        self.source_major_version = source_major_version
        # The target instance version.
        self.target_major_version = target_major_version
        # The node ID of the major engine version upgrade pre-check task.
        self.task_id = task_id
        self.upgrade_mode = upgrade_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_time is not None:
            result['CheckTime'] = self.check_time

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.recommend_disk_size is not None:
            result['RecommendDiskSize'] = self.recommend_disk_size

        if self.recommend_least_mem_size is not None:
            result['RecommendLeastMemSize'] = self.recommend_least_mem_size

        if self.recommend_mem_size is not None:
            result['RecommendMemSize'] = self.recommend_mem_size

        if self.result is not None:
            result['Result'] = self.result

        if self.source_major_version is not None:
            result['SourceMajorVersion'] = self.source_major_version

        if self.target_major_version is not None:
            result['TargetMajorVersion'] = self.target_major_version

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('RecommendDiskSize') is not None:
            self.recommend_disk_size = m.get('RecommendDiskSize')

        if m.get('RecommendLeastMemSize') is not None:
            self.recommend_least_mem_size = m.get('RecommendLeastMemSize')

        if m.get('RecommendMemSize') is not None:
            self.recommend_mem_size = m.get('RecommendMemSize')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SourceMajorVersion') is not None:
            self.source_major_version = m.get('SourceMajorVersion')

        if m.get('TargetMajorVersion') is not None:
            self.target_major_version = m.get('TargetMajorVersion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')

        return self

