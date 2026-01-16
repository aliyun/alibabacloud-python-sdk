# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DeleteClusterNodesRequest(DaraModel):
    def __init__(
        self,
        body: main_models.DeleteClusterNodesRequestBody = None,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.body = body
        # This parameter is required.
        self.cluster_id = cluster_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.DeleteClusterNodesRequestBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

class DeleteClusterNodesRequestBody(DaraModel):
    def __init__(
        self,
        nodes: List[str] = None,
    ):
        # This parameter is required.
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nodes is not None:
            result['Nodes'] = self.nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        return self

