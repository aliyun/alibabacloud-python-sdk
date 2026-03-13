# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class InsureOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.InsureOrderDetailResponseBodyModule = None,
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
            temp_model = main_models.InsureOrderDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class InsureOrderDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        applicant: main_models.InsureOrderDetailResponseBodyModuleApplicant = None,
        ins_order_id: str = None,
        insure_order_detail_list: List[main_models.InsureOrderDetailResponseBodyModuleInsureOrderDetailList] = None,
        status: str = None,
    ):
        self.applicant = applicant
        self.ins_order_id = ins_order_id
        self.insure_order_detail_list = insure_order_detail_list
        self.status = status

    def validate(self):
        if self.applicant:
            self.applicant.validate()
        if self.insure_order_detail_list:
            for v1 in self.insure_order_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant is not None:
            result['applicant'] = self.applicant.to_map()

        if self.ins_order_id is not None:
            result['ins_order_id'] = self.ins_order_id

        result['insure_order_detail_list'] = []
        if self.insure_order_detail_list is not None:
            for k1 in self.insure_order_detail_list:
                result['insure_order_detail_list'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicant') is not None:
            temp_model = main_models.InsureOrderDetailResponseBodyModuleApplicant()
            self.applicant = temp_model.from_map(m.get('applicant'))

        if m.get('ins_order_id') is not None:
            self.ins_order_id = m.get('ins_order_id')

        self.insure_order_detail_list = []
        if m.get('insure_order_detail_list') is not None:
            for k1 in m.get('insure_order_detail_list'):
                temp_model = main_models.InsureOrderDetailResponseBodyModuleInsureOrderDetailList()
                self.insure_order_detail_list.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class InsureOrderDetailResponseBodyModuleInsureOrderDetailList(DaraModel):
    def __init__(
        self,
        effective_end_time: str = None,
        effective_start_time: str = None,
        insure_segment: main_models.InsureOrderDetailResponseBodyModuleInsureOrderDetailListInsureSegment = None,
        insure_time: str = None,
        insured: main_models.InsureOrderDetailResponseBodyModuleInsureOrderDetailListInsured = None,
        out_sub_ins_order_id: str = None,
        policy_no: str = None,
        price: int = None,
        product_name: str = None,
        product_no: str = None,
        status: str = None,
        sub_ins_order_id: str = None,
    ):
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.insure_segment = insure_segment
        self.insure_time = insure_time
        self.insured = insured
        self.out_sub_ins_order_id = out_sub_ins_order_id
        self.policy_no = policy_no
        self.price = price
        self.product_name = product_name
        self.product_no = product_no
        self.status = status
        self.sub_ins_order_id = sub_ins_order_id

    def validate(self):
        if self.insure_segment:
            self.insure_segment.validate()
        if self.insured:
            self.insured.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_end_time is not None:
            result['effective_end_time'] = self.effective_end_time

        if self.effective_start_time is not None:
            result['effective_start_time'] = self.effective_start_time

        if self.insure_segment is not None:
            result['insure_segment'] = self.insure_segment.to_map()

        if self.insure_time is not None:
            result['insure_time'] = self.insure_time

        if self.insured is not None:
            result['insured'] = self.insured.to_map()

        if self.out_sub_ins_order_id is not None:
            result['out_sub_ins_order_id'] = self.out_sub_ins_order_id

        if self.policy_no is not None:
            result['policy_no'] = self.policy_no

        if self.price is not None:
            result['price'] = self.price

        if self.product_name is not None:
            result['product_name'] = self.product_name

        if self.product_no is not None:
            result['product_no'] = self.product_no

        if self.status is not None:
            result['status'] = self.status

        if self.sub_ins_order_id is not None:
            result['sub_ins_order_id'] = self.sub_ins_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effective_end_time') is not None:
            self.effective_end_time = m.get('effective_end_time')

        if m.get('effective_start_time') is not None:
            self.effective_start_time = m.get('effective_start_time')

        if m.get('insure_segment') is not None:
            temp_model = main_models.InsureOrderDetailResponseBodyModuleInsureOrderDetailListInsureSegment()
            self.insure_segment = temp_model.from_map(m.get('insure_segment'))

        if m.get('insure_time') is not None:
            self.insure_time = m.get('insure_time')

        if m.get('insured') is not None:
            temp_model = main_models.InsureOrderDetailResponseBodyModuleInsureOrderDetailListInsured()
            self.insured = temp_model.from_map(m.get('insured'))

        if m.get('out_sub_ins_order_id') is not None:
            self.out_sub_ins_order_id = m.get('out_sub_ins_order_id')

        if m.get('policy_no') is not None:
            self.policy_no = m.get('policy_no')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('product_name') is not None:
            self.product_name = m.get('product_name')

        if m.get('product_no') is not None:
            self.product_no = m.get('product_no')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('sub_ins_order_id') is not None:
            self.sub_ins_order_id = m.get('sub_ins_order_id')

        return self

class InsureOrderDetailResponseBodyModuleInsureOrderDetailListInsured(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        btrip_user_id: str = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        gender: str = None,
        phone: str = None,
    ):
        self.birthday = birthday
        self.btrip_user_id = btrip_user_id
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.gender = gender
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.cert_name is not None:
            result['cert_name'] = self.cert_name

        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.gender is not None:
            result['gender'] = self.gender

        if self.phone is not None:
            result['phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')

        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        return self

class InsureOrderDetailResponseBodyModuleInsureOrderDetailListInsureSegment(DaraModel):
    def __init__(
        self,
        arr_airport_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_time: str = None,
        dep_airport_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_time: str = None,
        flight_no: str = None,
    ):
        self.arr_airport_code = arr_airport_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_time = arr_time
        self.dep_airport_code = dep_airport_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_time = dep_time
        self.flight_no = flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        return self

class InsureOrderDetailResponseBodyModuleApplicant(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        phone: str = None,
    ):
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name

        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.phone is not None:
            result['phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')

        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        return self

