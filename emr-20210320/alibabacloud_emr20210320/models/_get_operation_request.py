# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOperationRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        operation_id: str = None,
        region_id: str = None,
    ):
        # The ID of the cluster that you want to query.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The operation ID.
        # 
        # References:
        # 
        # *   [CreateCluster](https://help.aliyun.com/document_detail/454393.html)
        # *   [IncreaseNodes](https://help.aliyun.com/document_detail/454397.html)
        # 
        # This parameter is required.
        self.operation_id = operation_id
        # The district ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

