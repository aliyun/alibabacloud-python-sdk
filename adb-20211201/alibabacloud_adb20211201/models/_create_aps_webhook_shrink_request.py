# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApsWebhookShrinkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        job_type: str = None,
        region_id: str = None,
        webhook_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The type of the task. Valid value: Task type. SLS or OSS Export Task: ResultExport.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The ID of the region in which to create the dedicated block storage cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The array of webhooks.
        self.webhook_shrink = webhook_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.webhook_shrink is not None:
            result['Webhook'] = self.webhook_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Webhook') is not None:
            self.webhook_shrink = m.get('Webhook')

        return self

