# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUniBackupPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeUniBackupPoliciesResponseBodyPageInfo = None,
        request_id: str = None,
        uni_backup_policies: List[main_models.DescribeUniBackupPoliciesResponseBodyUniBackupPolicies] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the anti-ransomware policies.
        self.uni_backup_policies = uni_backup_policies

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.uni_backup_policies:
            for v1 in self.uni_backup_policies:
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

        result['UniBackupPolicies'] = []
        if self.uni_backup_policies is not None:
            for k1 in self.uni_backup_policies:
                result['UniBackupPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeUniBackupPoliciesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.uni_backup_policies = []
        if m.get('UniBackupPolicies') is not None:
            for k1 in m.get('UniBackupPolicies'):
                temp_model = main_models.DescribeUniBackupPoliciesResponseBodyUniBackupPolicies()
                self.uni_backup_policies.append(temp_model.from_map(k1))

        return self

class DescribeUniBackupPoliciesResponseBodyUniBackupPolicies(DaraModel):
    def __init__(
        self,
        agent_error_message: str = None,
        agent_status: str = None,
        database_name: str = None,
        database_type: str = None,
        error_code: str = None,
        error_message: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_uuid: str = None,
        latest_back_result: str = None,
        latest_backup_time: str = None,
        plan_status: str = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_status: str = None,
        uni_region_id: str = None,
    ):
        # The error message for the anti-ransomware agent.
        self.agent_error_message = agent_error_message
        # The status of the agent. Valid values:
        # 
        # *   **UNKNOWN**
        # *   **INSTALLED**
        # *   **INSTALL_FAILED**
        # *   **UNINSTALL_FAILED**
        self.agent_status = agent_status
        # The name of the database.
        self.database_name = database_name
        # The type of the database. Valid values:
        # 
        # *   **MYSQL**
        # *   **MSSQL**
        # *   **Oracle**
        self.database_type = database_type
        # The error code returned when the backup task fails.
        self.error_code = error_code
        # The error message for the anti-ransomware policy.
        self.error_message = error_message
        # The ID of the server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The status of the Elastic Compute Service (ECS) instance. Valid values:
        # 
        # *   **Stopped**
        # *   **Running**
        self.instance_status = instance_status
        # The UUID of the agent that is used to back up the data of the database.
        self.instance_uuid = instance_uuid
        # The execution result of the last backup task.
        self.latest_back_result = latest_back_result
        # The time when the last backup task was executed.
        self.latest_backup_time = latest_backup_time
        # The status of the backup task. Valid values:
        # 
        # *   **init**
        # *   **running**
        # *   **completed**
        # *   **restoring**
        # *   **creating**
        # *   **created**
        self.plan_status = plan_status
        # The ID of the anti-ransomware policy.
        self.policy_id = policy_id
        # The name of the anti-ransomware policy.
        self.policy_name = policy_name
        # The status of the anti-ransomware policy. Valid values:
        # 
        # *   **initiating**
        # *   **opening**
        # *   **closing**
        # *   **deleting**
        # *   **enabled**
        # *   **disabled**
        self.policy_status = policy_status
        # The region ID of the server that hosts the database.
        self.uni_region_id = uni_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_error_message is not None:
            result['AgentErrorMessage'] = self.agent_error_message

        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_uuid is not None:
            result['InstanceUuid'] = self.instance_uuid

        if self.latest_back_result is not None:
            result['LatestBackResult'] = self.latest_back_result

        if self.latest_backup_time is not None:
            result['LatestBackupTime'] = self.latest_backup_time

        if self.plan_status is not None:
            result['PlanStatus'] = self.plan_status

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.uni_region_id is not None:
            result['UniRegionId'] = self.uni_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentErrorMessage') is not None:
            self.agent_error_message = m.get('AgentErrorMessage')

        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceUuid') is not None:
            self.instance_uuid = m.get('InstanceUuid')

        if m.get('LatestBackResult') is not None:
            self.latest_back_result = m.get('LatestBackResult')

        if m.get('LatestBackupTime') is not None:
            self.latest_backup_time = m.get('LatestBackupTime')

        if m.get('PlanStatus') is not None:
            self.plan_status = m.get('PlanStatus')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('UniRegionId') is not None:
            self.uni_region_id = m.get('UniRegionId')

        return self

class DescribeUniBackupPoliciesResponseBodyPageInfo(DaraModel):
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

