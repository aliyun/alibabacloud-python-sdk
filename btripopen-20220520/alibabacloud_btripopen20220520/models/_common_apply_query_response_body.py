# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class CommonApplyQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.CommonApplyQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.CommonApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class CommonApplyQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        biz_category: int = None,
        cause: str = None,
        corp_id: str = None,
        extend_value: str = None,
        gmt_create: str = None,
        order_id: int = None,
        status: int = None,
        thirdpart_corp_id: str = None,
        thirdpart_id: str = None,
        trip_cause: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.biz_category = biz_category
        self.cause = cause
        self.corp_id = corp_id
        self.extend_value = extend_value
        self.gmt_create = gmt_create
        self.order_id = order_id
        self.status = status
        self.thirdpart_corp_id = thirdpart_corp_id
        self.thirdpart_id = thirdpart_id
        self.trip_cause = trip_cause
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.biz_category is not None:
            result['biz_category'] = self.biz_category

        if self.cause is not None:
            result['cause'] = self.cause

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.extend_value is not None:
            result['extend_value'] = self.extend_value

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.status is not None:
            result['status'] = self.status

        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id

        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        if self.trip_cause is not None:
            result['trip_cause'] = self.trip_cause

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('biz_category') is not None:
            self.biz_category = m.get('biz_category')

        if m.get('cause') is not None:
            self.cause = m.get('cause')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('extend_value') is not None:
            self.extend_value = m.get('extend_value')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')

        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        if m.get('trip_cause') is not None:
            self.trip_cause = m.get('trip_cause')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

