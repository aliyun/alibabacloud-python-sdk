# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class InsureOrderCreateRequest(DaraModel):
    def __init__(
        self,
        applicant: main_models.InsureOrderCreateRequestApplicant = None,
        btrip_user_id: str = None,
        buyer_name: str = None,
        ins_person_and_segment_list: List[main_models.InsureOrderCreateRequestInsPersonAndSegmentList] = None,
        isv_name: str = None,
        out_ins_order_id: str = None,
        out_order_id: str = None,
        out_sub_order_id: str = None,
        supplier_code: str = None,
    ):
        # This parameter is required.
        self.applicant = applicant
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        # This parameter is required.
        self.ins_person_and_segment_list = ins_person_and_segment_list
        # This parameter is required.
        self.isv_name = isv_name
        self.out_ins_order_id = out_ins_order_id
        # This parameter is required.
        self.out_order_id = out_order_id
        self.out_sub_order_id = out_sub_order_id
        self.supplier_code = supplier_code

    def validate(self):
        if self.applicant:
            self.applicant.validate()
        if self.ins_person_and_segment_list:
            for v1 in self.ins_person_and_segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant is not None:
            result['applicant'] = self.applicant.to_map()

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        result['ins_person_and_segment_list'] = []
        if self.ins_person_and_segment_list is not None:
            for k1 in self.ins_person_and_segment_list:
                result['ins_person_and_segment_list'].append(k1.to_map() if k1 else None)

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.out_ins_order_id is not None:
            result['out_ins_order_id'] = self.out_ins_order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_sub_order_id is not None:
            result['out_sub_order_id'] = self.out_sub_order_id

        if self.supplier_code is not None:
            result['supplier_code'] = self.supplier_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicant') is not None:
            temp_model = main_models.InsureOrderCreateRequestApplicant()
            self.applicant = temp_model.from_map(m.get('applicant'))

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        self.ins_person_and_segment_list = []
        if m.get('ins_person_and_segment_list') is not None:
            for k1 in m.get('ins_person_and_segment_list'):
                temp_model = main_models.InsureOrderCreateRequestInsPersonAndSegmentList()
                self.ins_person_and_segment_list.append(temp_model.from_map(k1))

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('out_ins_order_id') is not None:
            self.out_ins_order_id = m.get('out_ins_order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_sub_order_id') is not None:
            self.out_sub_order_id = m.get('out_sub_order_id')

        if m.get('supplier_code') is not None:
            self.supplier_code = m.get('supplier_code')

        return self

class InsureOrderCreateRequestInsPersonAndSegmentList(DaraModel):
    def __init__(
        self,
        insure_segment: main_models.InsureOrderCreateRequestInsPersonAndSegmentListInsureSegment = None,
        insured: main_models.InsureOrderCreateRequestInsPersonAndSegmentListInsured = None,
        out_sub_ins_order_id: str = None,
    ):
        self.insure_segment = insure_segment
        self.insured = insured
        self.out_sub_ins_order_id = out_sub_ins_order_id

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
        if self.insure_segment is not None:
            result['insure_segment'] = self.insure_segment.to_map()

        if self.insured is not None:
            result['insured'] = self.insured.to_map()

        if self.out_sub_ins_order_id is not None:
            result['out_sub_ins_order_id'] = self.out_sub_ins_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('insure_segment') is not None:
            temp_model = main_models.InsureOrderCreateRequestInsPersonAndSegmentListInsureSegment()
            self.insure_segment = temp_model.from_map(m.get('insure_segment'))

        if m.get('insured') is not None:
            temp_model = main_models.InsureOrderCreateRequestInsPersonAndSegmentListInsured()
            self.insured = temp_model.from_map(m.get('insured'))

        if m.get('out_sub_ins_order_id') is not None:
            self.out_sub_ins_order_id = m.get('out_sub_ins_order_id')

        return self

class InsureOrderCreateRequestInsPersonAndSegmentListInsured(DaraModel):
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

class InsureOrderCreateRequestInsPersonAndSegmentListInsureSegment(DaraModel):
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

class InsureOrderCreateRequestApplicant(DaraModel):
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

