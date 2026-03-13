# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class InsureOrderRefundResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.InsureOrderRefundResponseBodyModule = None,
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
            temp_model = main_models.InsureOrderRefundResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class InsureOrderRefundResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        ins_order_id: str = None,
        ins_refund_list: List[main_models.InsureOrderRefundResponseBodyModuleInsRefundList] = None,
        out_apply_id: str = None,
    ):
        self.apply_id = apply_id
        self.ins_order_id = ins_order_id
        self.ins_refund_list = ins_refund_list
        self.out_apply_id = out_apply_id

    def validate(self):
        if self.ins_refund_list:
            for v1 in self.ins_refund_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.ins_order_id is not None:
            result['ins_order_id'] = self.ins_order_id

        result['ins_refund_list'] = []
        if self.ins_refund_list is not None:
            for k1 in self.ins_refund_list:
                result['ins_refund_list'].append(k1.to_map() if k1 else None)

        if self.out_apply_id is not None:
            result['out_apply_id'] = self.out_apply_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('ins_order_id') is not None:
            self.ins_order_id = m.get('ins_order_id')

        self.ins_refund_list = []
        if m.get('ins_refund_list') is not None:
            for k1 in m.get('ins_refund_list'):
                temp_model = main_models.InsureOrderRefundResponseBodyModuleInsRefundList()
                self.ins_refund_list.append(temp_model.from_map(k1))

        if m.get('out_apply_id') is not None:
            self.out_apply_id = m.get('out_apply_id')

        return self

class InsureOrderRefundResponseBodyModuleInsRefundList(DaraModel):
    def __init__(
        self,
        policy_refund_no: str = None,
        refund_status: str = None,
        sub_ins_order_id: str = None,
    ):
        self.policy_refund_no = policy_refund_no
        self.refund_status = refund_status
        self.sub_ins_order_id = sub_ins_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_refund_no is not None:
            result['policy_refund_no'] = self.policy_refund_no

        if self.refund_status is not None:
            result['refund_status'] = self.refund_status

        if self.sub_ins_order_id is not None:
            result['sub_ins_order_id'] = self.sub_ins_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policy_refund_no') is not None:
            self.policy_refund_no = m.get('policy_refund_no')

        if m.get('refund_status') is not None:
            self.refund_status = m.get('refund_status')

        if m.get('sub_ins_order_id') is not None:
            self.sub_ins_order_id = m.get('sub_ins_order_id')

        return self

