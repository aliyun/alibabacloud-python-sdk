# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateDBNodesResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbnode_ids: main_models.CreateDBNodesResponseBodyDBNodeIds = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # Details about the nodes.
        self.dbnode_ids = dbnode_ids
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dbnode_ids:
            self.dbnode_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeIds') is not None:
            temp_model = main_models.CreateDBNodesResponseBodyDBNodeIds()
            self.dbnode_ids = temp_model.from_map(m.get('DBNodeIds'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateDBNodesResponseBodyDBNodeIds(DaraModel):
    def __init__(
        self,
        dbnode_id: List[str] = None,
    ):
        self.dbnode_id = dbnode_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        return self

