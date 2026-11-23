# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenServiceResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        sp_instance_id: str = None,
        status: str = None,
    ):
        # 关联本次开通申请的订单 ID，存在时返回。
        self.order_id = order_id
        # 服务已开通时返回的实例标识。
        self.sp_instance_id = sp_instance_id
        # TEST_OK 表示仅验证调用成功。OPENING 表示开通处理中。ACTIVE 表示已开通。ORDER_UNKNOWN 表示暂时无法确认开通结果。REJECTED 表示开通请求未获通过。
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.sp_instance_id is not None:
            result['spInstanceId'] = self.sp_instance_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('spInstanceId') is not None:
            self.sp_instance_id = m.get('spInstanceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

