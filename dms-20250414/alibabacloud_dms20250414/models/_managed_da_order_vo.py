# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManagedDaOrderVO(DaraModel):
    def __init__(
        self,
        expire_time: str = None,
        gmt_create: str = None,
        instance_id: str = None,
        order_id: int = None,
        pay_num: int = None,
        region: str = None,
        state: str = None,
        subscription_plan: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.expire_time = expire_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.order_id = order_id
        self.pay_num = pay_num
        self.region = region
        self.state = state
        self.subscription_plan = subscription_plan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.pay_num is not None:
            result['payNum'] = self.pay_num

        if self.region is not None:
            result['region'] = self.region

        if self.state is not None:
            result['state'] = self.state

        if self.subscription_plan is not None:
            result['subscriptionPlan'] = self.subscription_plan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('payNum') is not None:
            self.pay_num = m.get('payNum')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('subscriptionPlan') is not None:
            self.subscription_plan = m.get('subscriptionPlan')

        return self

