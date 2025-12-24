# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferTaskApprovalCallbackRequest(DaraModel):
    def __init__(
        self,
        oss_bucket_name: str = None,
        oss_bucket_region_id: str = None,
        result: str = None,
        task_id: str = None,
    ):
        # The name of the OSS bucket where the file resides.
        self.oss_bucket_name = oss_bucket_name
        # The region where the OSS bucket storing the file resides.
        self.oss_bucket_region_id = oss_bucket_region_id
        # The approval result.
        # 
        # Valid values:
        # 
        # *   Approved
        # *   Rejected
        self.result = result
        # The ID of the transmission task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_bucket_region_id is not None:
            result['OssBucketRegionId'] = self.oss_bucket_region_id

        if self.result is not None:
            result['Result'] = self.result

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssBucketRegionId') is not None:
            self.oss_bucket_region_id = m.get('OssBucketRegionId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

