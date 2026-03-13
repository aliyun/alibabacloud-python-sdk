# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class InsureOrderApplyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.InsureOrderApplyResponseBodyModule = None,
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
            temp_model = main_models.InsureOrderApplyResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class InsureOrderApplyResponseBodyModule(DaraModel):
    def __init__(
        self,
        ins_order_id: str = None,
        ins_order_policy_list: List[main_models.InsureOrderApplyResponseBodyModuleInsOrderPolicyList] = None,
    ):
        self.ins_order_id = ins_order_id
        self.ins_order_policy_list = ins_order_policy_list

    def validate(self):
        if self.ins_order_policy_list:
            for v1 in self.ins_order_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ins_order_id is not None:
            result['ins_order_id'] = self.ins_order_id

        result['ins_order_policy_list'] = []
        if self.ins_order_policy_list is not None:
            for k1 in self.ins_order_policy_list:
                result['ins_order_policy_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ins_order_id') is not None:
            self.ins_order_id = m.get('ins_order_id')

        self.ins_order_policy_list = []
        if m.get('ins_order_policy_list') is not None:
            for k1 in m.get('ins_order_policy_list'):
                temp_model = main_models.InsureOrderApplyResponseBodyModuleInsOrderPolicyList()
                self.ins_order_policy_list.append(temp_model.from_map(k1))

        return self

class InsureOrderApplyResponseBodyModuleInsOrderPolicyList(DaraModel):
    def __init__(
        self,
        out_sub_ins_order_id: str = None,
        policy_no: str = None,
        status: str = None,
        sub_ins_order_id: str = None,
    ):
        self.out_sub_ins_order_id = out_sub_ins_order_id
        self.policy_no = policy_no
        self.status = status
        self.sub_ins_order_id = sub_ins_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_sub_ins_order_id is not None:
            result['out_sub_ins_order_id'] = self.out_sub_ins_order_id

        if self.policy_no is not None:
            result['policy_no'] = self.policy_no

        if self.status is not None:
            result['status'] = self.status

        if self.sub_ins_order_id is not None:
            result['sub_ins_order_id'] = self.sub_ins_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('out_sub_ins_order_id') is not None:
            self.out_sub_ins_order_id = m.get('out_sub_ins_order_id')

        if m.get('policy_no') is not None:
            self.policy_no = m.get('policy_no')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('sub_ins_order_id') is not None:
            self.sub_ins_order_id = m.get('sub_ins_order_id')

        return self

