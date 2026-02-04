# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReverseDtsJobRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        resource_group_id: str = None,
        shard_password: str = None,
        shard_username: str = None,
    ):
        # The ID of the synchronization or migration task, which can be queried by calling [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html).
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # Resource GroupId
        self.resource_group_id = resource_group_id
        # Shard Password
        self.shard_password = shard_password
        # Shard User name
        self.shard_username = shard_username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.shard_password is not None:
            result['ShardPassword'] = self.shard_password

        if self.shard_username is not None:
            result['ShardUsername'] = self.shard_username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShardPassword') is not None:
            self.shard_password = m.get('ShardPassword')

        if m.get('ShardUsername') is not None:
            self.shard_username = m.get('ShardUsername')

        return self

