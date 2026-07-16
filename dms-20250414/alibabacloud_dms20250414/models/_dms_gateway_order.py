# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DmsGatewayOrder(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        charge_type: str = None,
        commodity_code: str = None,
        expire_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        order_id: int = None,
        pay_num: int = None,
        region: str = None,
        state: str = None,
    ):
        self.biz_type = biz_type
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.order_id = order_id
        self.pay_num = pay_num
        self.region = region
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.pay_num is not None:
            result['PayNum'] = self.pay_num

        if self.region is not None:
            result['Region'] = self.region

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PayNum') is not None:
            self.pay_num = m.get('PayNum')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

