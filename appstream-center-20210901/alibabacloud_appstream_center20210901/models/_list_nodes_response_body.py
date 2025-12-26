# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListNodesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        node_models: List[main_models.ListNodesResponseBodyNodeModels] = None,
        per_page_size: int = None,
        request_id: str = None,
        to_page: int = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The resource nodes.
        self.node_models = node_models
        # The number of entries per page.
        self.per_page_size = per_page_size
        # The request ID.
        self.request_id = request_id
        # The page number.
        self.to_page = to_page

    def validate(self):
        if self.node_models:
            for v1 in self.node_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['NodeModels'] = []
        if self.node_models is not None:
            for k1 in self.node_models:
                result['NodeModels'].append(k1.to_map() if k1 else None)

        if self.per_page_size is not None:
            result['PerPageSize'] = self.per_page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.to_page is not None:
            result['ToPage'] = self.to_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.node_models = []
        if m.get('NodeModels') is not None:
            for k1 in m.get('NodeModels'):
                temp_model = main_models.ListNodesResponseBodyNodeModels()
                self.node_models.append(temp_model.from_map(k1))

        if m.get('PerPageSize') is not None:
            self.per_page_size = m.get('PerPageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ToPage') is not None:
            self.to_page = m.get('ToPage')

        return self

class ListNodesResponseBodyNodeModels(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        node_id: str = None,
    ):
        # The billing method of the resource node.
        # 
        # >  This parameter is returned only if the ChargeResourceMode parameter of the delivery group to which the resource node belongs is set to Node.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   Prepaid: subscription
        self.charge_type = charge_type
        # The ID of the resource node.
        # 
        # >  This parameter is returned only if the ChargeResourceMode parameter of the delivery group to which the resource node belongs is set to Node.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

