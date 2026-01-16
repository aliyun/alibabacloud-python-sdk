# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class ScaleClusterNodePoolRequest(DaraModel):
    def __init__(
        self,
        body: main_models.ScaleClusterNodePoolRequestBody = None,
        cluster_id: str = None,
        nodepool_id: str = None,
    ):
        self.body = body
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.nodepool_id = nodepool_id

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.nodepool_id is not None:
            result['NodepoolId'] = self.nodepool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.ScaleClusterNodePoolRequestBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodepoolId') is not None:
            self.nodepool_id = m.get('NodepoolId')

        return self

class ScaleClusterNodePoolRequestBody(DaraModel):
    def __init__(
        self,
        count: int = None,
    ):
        # This parameter is required.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

