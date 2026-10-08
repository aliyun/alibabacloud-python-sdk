# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallAgentRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        do_async: bool = None,
        instance_ids: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is discontinued.
        self.do_async = do_async
        # The ID of the ECS instance. Separate multiple IDs with commas (,). Example: instanceId1,instanceId2.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.do_async is not None:
            result['DoAsync'] = self.do_async

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DoAsync') is not None:
            self.do_async = m.get('DoAsync')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        return self

