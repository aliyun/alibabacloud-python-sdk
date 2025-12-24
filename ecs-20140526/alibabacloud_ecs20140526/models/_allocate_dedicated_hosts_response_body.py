# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class AllocateDedicatedHostsResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_host_id_sets: main_models.AllocateDedicatedHostsResponseBodyDedicatedHostIdSets = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # A list of dedicated host IDs.
        self.dedicated_host_id_sets = dedicated_host_id_sets
        # The ID of the order.
        # 
        # >  This parameter has a return value only when the dedicated host is a subscription one (request parameter **ChargeType set to PrePaid**).
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dedicated_host_id_sets:
            self.dedicated_host_id_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_id_sets is not None:
            result['DedicatedHostIdSets'] = self.dedicated_host_id_sets.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostIdSets') is not None:
            temp_model = main_models.AllocateDedicatedHostsResponseBodyDedicatedHostIdSets()
            self.dedicated_host_id_sets = temp_model.from_map(m.get('DedicatedHostIdSets'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AllocateDedicatedHostsResponseBodyDedicatedHostIdSets(DaraModel):
    def __init__(
        self,
        dedicated_host_id: List[str] = None,
    ):
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        return self

