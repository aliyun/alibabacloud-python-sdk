# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupSetDownloadTaskListRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_set_download_task_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The ID of the backup plan. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the value of this parameter.
        # 
        # > You must specify either **BackupPlanId** or **BackupSetDownloadTaskId**.
        self.backup_plan_id = backup_plan_id
        # The ID of the backup set download task.
        # 
        # - For a full backup, call the [CreateFullBackupSetDownload](https://help.aliyun.com/document_detail/2869842.html) operation to obtain the value of this parameter.
        # 
        # - For an incremental backup, call the [CreateIncrementBackupSetDownload](https://help.aliyun.com/document_detail/2869843.html) operation to obtain the value of this parameter.
        self.backup_set_download_task_id = backup_set_download_task_id
        # A client token that is used to ensure the idempotence of the request. This prevents duplicate requests.
        self.client_token = client_token
        self.owner_id = owner_id
        # The page number. The value must be a non-negative integer that does not exceed the maximum value of the integer type. The default value is 0.
        self.page_num = page_num
        # The number of entries to return on each page. Valid values: 30, 50, and 100.
        # 
        # > The default value is 30.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

