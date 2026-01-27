# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDownloadBackupSetStorageInfoRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        cluster_name: str = None,
        duration: str = None,
        instance_name: str = None,
        region_code: str = None,
        task_id: str = None,
    ):
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        self.cluster_name = cluster_name
        # The validity period of the URL that is used as the download destination. Take note of the following items:
        # 
        # *   Default value: 7200. This means that the URL is valid for 2 hours by default.
        # *   Valid values: 300 to 86400. Unit: seconds. This means that you can specify a validity period in the range of 5 minutes to 1 day.
        # *   Before you specify this parameter, convert the validity period to seconds. For example, if you want to set the validity period of the URL to 5 minutes, enter 300.
        # 
        # This parameter is required.
        self.duration = duration
        # The ID of the instance.
        # 
        # > The **BackupSetId** parameter is required if you specify the **InstanceName** parameter.
        self.instance_name = instance_name
        # The ID of the region in which the instance resides.
        # 
        # This parameter is required.
        self.region_code = region_code
        # The download task ID.
        # 
        # *   The **BackupSetId** and **InstanceName** parameters are required if you do not specify the **TaskId** parameter.
        # *   To view the download task ID, go to the instance details page in the console and click **Backup and Restoration** in the left-side navigation pane. On the **Backup Download** tab, view the task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

