# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAIAgentOrderResponseBody(DaraModel):
    def __init__(
        self,
        agent_version: str = None,
        capacity_pack: str = None,
        expire_time: str = None,
        has_order: bool = None,
        order_id: str = None,
        order_name: str = None,
        order_num: str = None,
        order_status: str = None,
        request_id: str = None,
    ):
        # The AI assistant version.
        self.agent_version = agent_version
        # The capacity package specifications.
        self.capacity_pack = capacity_pack
        # The expiration time of the order in RFC 3339 format.
        self.expire_time = expire_time
        # Indicates whether the current account has an AI assistant order.
        self.has_order = has_order
        # The order ID.
        self.order_id = order_id
        # The order name.
        self.order_name = order_name
        # The order number.
        self.order_num = order_num
        # The order status.
        self.order_status = order_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.capacity_pack is not None:
            result['CapacityPack'] = self.capacity_pack

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.has_order is not None:
            result['HasOrder'] = self.has_order

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_name is not None:
            result['OrderName'] = self.order_name

        if self.order_num is not None:
            result['OrderNum'] = self.order_num

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('CapacityPack') is not None:
            self.capacity_pack = m.get('CapacityPack')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HasOrder') is not None:
            self.has_order = m.get('HasOrder')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderName') is not None:
            self.order_name = m.get('OrderName')

        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

