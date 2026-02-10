# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeRestorePlansResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeRestorePlansResponseBodyPageInfo = None,
        request_id: str = None,
        restore_plans: List[main_models.DescribeRestorePlansResponseBodyRestorePlans] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the restoration tasks.
        self.restore_plans = restore_plans

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.restore_plans:
            for v1 in self.restore_plans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RestorePlans'] = []
        if self.restore_plans is not None:
            for k1 in self.restore_plans:
                result['RestorePlans'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeRestorePlansResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.restore_plans = []
        if m.get('RestorePlans') is not None:
            for k1 in m.get('RestorePlans'):
                temp_model = main_models.DescribeRestorePlansResponseBodyRestorePlans()
                self.restore_plans.append(temp_model.from_map(k1))

        return self

class DescribeRestorePlansResponseBodyRestorePlans(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        database_name: str = None,
        instance_name: str = None,
        policy_id: int = None,
        policy_name: str = None,
        restore_point: int = None,
        status: str = None,
        target_database_name: str = None,
        target_instance_id: str = None,
        target_instance_name: str = None,
        updated_time: int = None,
    ):
        # The timestamp when the restoration task was created. Unit: milliseconds.
        self.created_time = created_time
        # The name of the database.
        self.database_name = database_name
        # The name of the server on which the database resides.
        self.instance_name = instance_name
        # The ID of the anti-ransomware policy.
        self.policy_id = policy_id
        # The name of the anti-ransomware policy.
        self.policy_name = policy_name
        # The point in time to which data is restored.
        self.restore_point = restore_point
        # The status of the restoration task. Valid values:
        # 
        # *   **init**: initializing
        # *   **created**: creating
        # *   **running**: running
        # *   **completed**: complete
        # *   **error**: failed
        # *   **restoring**: restoring
        self.status = status
        # The name of the destination database.
        self.target_database_name = target_database_name
        # The ID of the destination server.
        self.target_instance_id = target_instance_id
        # The name of the destination server.
        self.target_instance_name = target_instance_name
        # The timestamp when the restoration task was last updated. Unit: milliseconds.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.restore_point is not None:
            result['RestorePoint'] = self.restore_point

        if self.status is not None:
            result['Status'] = self.status

        if self.target_database_name is not None:
            result['TargetDatabaseName'] = self.target_database_name

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('RestorePoint') is not None:
            self.restore_point = m.get('RestorePoint')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetDatabaseName') is not None:
            self.target_database_name = m.get('TargetDatabaseName')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class DescribeRestorePlansResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

