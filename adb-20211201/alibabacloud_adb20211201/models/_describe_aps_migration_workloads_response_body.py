# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeApsMigrationWorkloadsResponseBody(DaraModel):
    def __init__(
        self,
        migration_workloads: List[main_models.DescribeApsMigrationWorkloadsResponseBodyMigrationWorkloads] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried migration workloads.
        self.migration_workloads = migration_workloads
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.migration_workloads:
            for v1 in self.migration_workloads:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MigrationWorkloads'] = []
        if self.migration_workloads is not None:
            for k1 in self.migration_workloads:
                result['MigrationWorkloads'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.migration_workloads = []
        if m.get('MigrationWorkloads') is not None:
            for k1 in m.get('MigrationWorkloads'):
                temp_model = main_models.DescribeApsMigrationWorkloadsResponseBodyMigrationWorkloads()
                self.migration_workloads.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApsMigrationWorkloadsResponseBodyMigrationWorkloads(DaraModel):
    def __init__(
        self,
        acu_count: int = None,
        create_time: str = None,
        failed_msg: str = None,
        id: str = None,
        max_rt: str = None,
        modify_time: str = None,
        name: str = None,
        oss_location: str = None,
        state: str = None,
        target_type: str = None,
        workload_sub_type: str = None,
    ):
        # The number of AnalyticDB compute units (ACUs).
        self.acu_count = acu_count
        # The time when the job was created.
        self.create_time = create_time
        # The error message.
        self.failed_msg = failed_msg
        # The job ID.
        self.id = id
        # The maximum response time.
        self.max_rt = max_rt
        # The time when the migration job was modified.
        self.modify_time = modify_time
        # The name of the workload.
        self.name = name
        # The OSS URL.
        self.oss_location = oss_location
        # The status.
        self.state = state
        # The destination type.
        self.target_type = target_type
        # The sub-type of the workload.
        self.workload_sub_type = workload_sub_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acu_count is not None:
            result['AcuCount'] = self.acu_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.failed_msg is not None:
            result['FailedMsg'] = self.failed_msg

        if self.id is not None:
            result['Id'] = self.id

        if self.max_rt is not None:
            result['MaxRT'] = self.max_rt

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_location is not None:
            result['OssLocation'] = self.oss_location

        if self.state is not None:
            result['State'] = self.state

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.workload_sub_type is not None:
            result['WorkloadSubType'] = self.workload_sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcuCount') is not None:
            self.acu_count = m.get('AcuCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FailedMsg') is not None:
            self.failed_msg = m.get('FailedMsg')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaxRT') is not None:
            self.max_rt = m.get('MaxRT')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssLocation') is not None:
            self.oss_location = m.get('OssLocation')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('WorkloadSubType') is not None:
            self.workload_sub_type = m.get('WorkloadSubType')

        return self

