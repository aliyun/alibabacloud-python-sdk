# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUniBackupPolicyDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        uni_backup_policy_dto: main_models.DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTO = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The details of the anti-ransomware policy.
        self.uni_backup_policy_dto = uni_backup_policy_dto

    def validate(self):
        if self.uni_backup_policy_dto:
            self.uni_backup_policy_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.uni_backup_policy_dto is not None:
            result['UniBackupPolicyDTO'] = self.uni_backup_policy_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UniBackupPolicyDTO') is not None:
            temp_model = main_models.DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTO()
            self.uni_backup_policy_dto = temp_model.from_map(m.get('UniBackupPolicyDTO'))

        return self

class DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTO(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        agent_status: str = None,
        database_type: str = None,
        full_plan: main_models.DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTOFullPlan = None,
        inc_plan: main_models.DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTOIncPlan = None,
        instance_id: str = None,
        instance_name: str = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_status: str = None,
        retention: int = None,
        speed_limiter: int = None,
    ):
        # The name of the database account.
        self.account_name = account_name
        # The status of the database client. Valid values:
        # 
        # *   **UNKNOWN**: unknown
        # *   **INSTALLED**: installed
        # *   **INSTALL_FAILED**: installation failed
        # *   **UNINSTALL_FAILED**: uninstallation failed
        self.agent_status = agent_status
        # The type of the database. Valid values:
        # 
        # *   **MYSQL**
        # *   **MSSQL**
        # *   **Oracle**
        self.database_type = database_type
        # The details of the policy for full backup.
        self.full_plan = full_plan
        # The policy for incremental data backup.
        self.inc_plan = inc_plan
        # The ID of the server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The ID of the anti-ransomware policy.
        self.policy_id = policy_id
        # The name of the anti-ransomware policy.
        self.policy_name = policy_name
        # The status of the anti-ransomware policy. Valid values:
        # 
        # *   **initiating**: initializing
        # *   **opening**: enabled
        # *   **closing**: disabled
        # *   **deleting**: deleting
        self.policy_status = policy_status
        # The retention period of the backup snapshot.
        self.retention = retention
        # The maximum network bandwidth that is allowed during data backup. Unit: bytes.
        self.speed_limiter = speed_limiter

    def validate(self):
        if self.full_plan:
            self.full_plan.validate()
        if self.inc_plan:
            self.inc_plan.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.full_plan is not None:
            result['FullPlan'] = self.full_plan.to_map()

        if self.inc_plan is not None:
            result['IncPlan'] = self.inc_plan.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.speed_limiter is not None:
            result['SpeedLimiter'] = self.speed_limiter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('FullPlan') is not None:
            temp_model = main_models.DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTOFullPlan()
            self.full_plan = temp_model.from_map(m.get('FullPlan'))

        if m.get('IncPlan') is not None:
            temp_model = main_models.DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTOIncPlan()
            self.inc_plan = temp_model.from_map(m.get('IncPlan'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('SpeedLimiter') is not None:
            self.speed_limiter = m.get('SpeedLimiter')

        return self

class DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTOIncPlan(DaraModel):
    def __init__(
        self,
        days: List[str] = None,
        interval: int = None,
        plan_type: str = None,
        start_time: str = None,
    ):
        # An array that consists of the days of a week on which the backup is performed.
        self.days = days
        # The interval of backup tasks.
        self.interval = interval
        # The unit of the interval. Valid values:
        # 
        # *   **hourly**: hour
        # *   **daily**: day
        # *   **weekly**: week
        self.plan_type = plan_type
        # The time when the incremental data backup starts. The time is in the hh:mm:ss format.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['Days'] = self.days

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeUniBackupPolicyDetailResponseBodyUniBackupPolicyDTOFullPlan(DaraModel):
    def __init__(
        self,
        days: List[str] = None,
        interval: int = None,
        plan_type: str = None,
        start_time: str = None,
    ):
        # An array that consists of the days of a week on which the backup is performed.
        self.days = days
        # The interval of backup tasks.
        self.interval = interval
        # The unit of the interval. Valid values:
        # 
        # *   **hourly**: hour
        # *   **daily**: day
        # *   **weekly**: week
        self.plan_type = plan_type
        # The time when the full backup started. The time is in the HH:mm:ss format.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['Days'] = self.days

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

