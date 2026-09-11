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
        # The ID of the synchronization or migration task. You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to query the task ID.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The ID of the resource group. This is a global parameter that does not need to be specified for this operation.
        self.resource_group_id = resource_group_id
        # The password of the shard in a MongoDB sharded cluster instance.
        # 
        # > - This parameter is available and required only when the source database instance is a MongoDB sharded cluster instance.
        # - This parameter takes effect only when **ModifyAccount** is set to **true**.
        self.shard_password = shard_password
        # The account of the shard in a MongoDB sharded cluster instance.
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

