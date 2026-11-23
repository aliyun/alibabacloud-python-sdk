# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qwenb2bchat20261121 import models as main_models
from darabonba.model import DaraModel

class OpenServiceResponseBody(DaraModel):
    def __init__(
        self,
        error: main_models.OpenServiceResponseBodyError = None,
        order_id: str = None,
        sp_instance_id: str = None,
        status: str = None,
    ):
        # 网关拒绝或处理失败时返回。成功响应没有此对象；平台在抵达业务网关前产生的错误遵循 OpenAPI 公共错误结构。
        self.error = error
        # OPENING 或 ACTIVE 时返回的订单号；其他状态省略，无默认值。
        self.order_id = order_id
        # ACTIVE 时返回的 SP 实例 ID；其他状态省略，无默认值。
        self.sp_instance_id = sp_instance_id
        # 正常响应必填。TEST_OK：接口验证通过，未发起实际开通；OPENING：已取得订单号，开通仍在处理中；ACTIVE：服务已开通，并返回订单号和实例 ID；ORDER_UNKNOWN：本次开通结果暂不能确认，不表示必定失败；REJECTED：本次因可用额度不足明确拒绝且未返回订单。HTTP 200 不等于已开通。
        self.status = status

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.sp_instance_id is not None:
            result['spInstanceId'] = self.sp_instance_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            temp_model = main_models.OpenServiceResponseBodyError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('spInstanceId') is not None:
            self.sp_instance_id = m.get('spInstanceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class OpenServiceResponseBodyError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # 错误码列表见接口说明。请求校验、鉴权、授权、配额及开通处理错误都使用此位置。
        # 
        # This parameter is required.
        self.code = code
        # 对应错误的可读说明，不应依赖固定文案判断。开通处理错误可能返回 service activation failed。
        # 
        # This parameter is required.
        self.message = message
        # 用于排查错误；通常对应 X-Request-Id。客户关联号缺失或非法时可返回服务端诊断号，不是订单号。
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['request_id'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        return self

