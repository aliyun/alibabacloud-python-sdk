# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCacheAnalysisJobRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        job_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the cache analysis task. You can obtain the task ID from the response parameters of the [CreateCacheAnalysisJob](https://help.aliyun.com/document_detail/180982.html) operation.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

