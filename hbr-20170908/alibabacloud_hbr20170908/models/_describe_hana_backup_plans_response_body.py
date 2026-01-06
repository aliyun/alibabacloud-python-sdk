# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeHanaBackupPlansResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        hana_backup_plans: main_models.DescribeHanaBackupPlansResponseBodyHanaBackupPlans = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The details of the backup plan.
        self.hana_backup_plans = hana_backup_plans
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.hana_backup_plans:
            self.hana_backup_plans.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hana_backup_plans is not None:
            result['HanaBackupPlans'] = self.hana_backup_plans.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HanaBackupPlans') is not None:
            temp_model = main_models.DescribeHanaBackupPlansResponseBodyHanaBackupPlans()
            self.hana_backup_plans = temp_model.from_map(m.get('HanaBackupPlans'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHanaBackupPlansResponseBodyHanaBackupPlans(DaraModel):
    def __init__(
        self,
        hana_backup_plan: List[main_models.DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan] = None,
    ):
        self.hana_backup_plan = hana_backup_plan

    def validate(self):
        if self.hana_backup_plan:
            for v1 in self.hana_backup_plan:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HanaBackupPlan'] = []
        if self.hana_backup_plan is not None:
            for k1 in self.hana_backup_plan:
                result['HanaBackupPlan'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hana_backup_plan = []
        if m.get('HanaBackupPlan') is not None:
            for k1 in m.get('HanaBackupPlan'):
                temp_model = main_models.DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan()
                self.hana_backup_plan.append(temp_model.from_map(k1))

        return self

class DescribeHanaBackupPlansResponseBodyHanaBackupPlansHanaBackupPlan(DaraModel):
    def __init__(
        self,
        backup_prefix: str = None,
        backup_type: str = None,
        business_status: str = None,
        cluster_id: str = None,
        database_name: str = None,
        disabled: bool = None,
        plan_id: str = None,
        plan_name: str = None,
        schedule: str = None,
        vault_id: str = None,
    ):
        # The backup prefix.
        self.backup_prefix = backup_prefix
        # The backup type. Valid values:
        # 
        # *   COMPLETE: full backup
        # *   INCREMENTAL: incremental backup
        # *   DIFFERENTIAL: differential backup
        self.backup_type = backup_type
        self.business_status = business_status
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The database name.
        self.database_name = database_name
        # Indicates whether the backup plan is disabled. Valid values:
        # 
        # *   true: The backup plan is disabled.
        # *   false: The backup plan is enabled.
        self.disabled = disabled
        # The ID of the backup plan.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

