# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List, Dict

from darabonba.model import DaraModel

class RefundNoticeParam(DaraModel):
    def __init__(
        self,
        aliuid: int = None,
        aliyun_produce_code: str = None,
        commodity_code: str = None,
        instance_id: str = None,
        new_expire_time: Any = None,
        order_ids: List[int] = None,
        refund_param_map: Dict[str, str] = None,
        refund_type: str = None,
    ):
        self.aliuid = aliuid
        self.aliyun_produce_code = aliyun_produce_code
        self.commodity_code = commodity_code
        self.instance_id = instance_id
        self.new_expire_time = new_expire_time
        self.order_ids = order_ids
        self.refund_param_map = refund_param_map
        self.refund_type = refund_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuid is not None:
            result['aliuid'] = self.aliuid

        if self.aliyun_produce_code is not None:
            result['aliyunProduceCode'] = self.aliyun_produce_code

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.new_expire_time is not None:
            result['newExpireTime'] = self.new_expire_time

        if self.order_ids is not None:
            result['orderIds'] = self.order_ids

        if self.refund_param_map is not None:
            result['refundParamMap'] = self.refund_param_map

        if self.refund_type is not None:
            result['refundType'] = self.refund_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliuid') is not None:
            self.aliuid = m.get('aliuid')

        if m.get('aliyunProduceCode') is not None:
            self.aliyun_produce_code = m.get('aliyunProduceCode')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('newExpireTime') is not None:
            self.new_expire_time = m.get('newExpireTime')

        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')

        if m.get('refundParamMap') is not None:
            self.refund_param_map = m.get('refundParamMap')

        if m.get('refundType') is not None:
            self.refund_type = m.get('refundType')

        return self

