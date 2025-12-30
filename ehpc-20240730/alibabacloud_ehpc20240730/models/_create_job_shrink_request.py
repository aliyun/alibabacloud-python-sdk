# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJobShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        job_name: str = None,
        job_spec_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The job name.
        self.job_name = job_name
        # The job configurations.
        self.job_spec_shrink = job_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_spec_shrink is not None:
            result['JobSpec'] = self.job_spec_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobSpec') is not None:
            self.job_spec_shrink = m.get('JobSpec')

        return self

