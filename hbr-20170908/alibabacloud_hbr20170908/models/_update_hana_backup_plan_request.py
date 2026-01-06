# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHanaBackupPlanRequest(DaraModel):
    def __init__(
        self,
        backup_prefix: str = None,
        cluster_id: str = None,
        plan_id: str = None,
        plan_name: str = None,
        resource_group_id: str = None,
        schedule: str = None,
        vault_id: str = None,
    ):
        # The backup prefix.
        self.backup_prefix = backup_prefix
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # The ID of the backup vault.
        # 
        # This parameter is required.
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

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

