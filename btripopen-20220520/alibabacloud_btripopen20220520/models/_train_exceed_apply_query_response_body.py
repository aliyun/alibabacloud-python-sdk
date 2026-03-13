# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainExceedApplyQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TrainExceedApplyQueryResponseBodyModule = None,
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
            temp_model = main_models.TrainExceedApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainExceedApplyQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_intention_info_do: main_models.TrainExceedApplyQueryResponseBodyModuleApplyIntentionInfoDO = None,
        btrip_cause: str = None,
        corp_id: str = None,
        exceed_reason: str = None,
        exceed_type: int = None,
        origin_standard: str = None,
        status: int = None,
        submit_time: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_corp_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.apply_intention_info_do = apply_intention_info_do
        self.btrip_cause = btrip_cause
        self.corp_id = corp_id
        self.exceed_reason = exceed_reason
        self.exceed_type = exceed_type
        self.origin_standard = origin_standard
        self.status = status
        self.submit_time = submit_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_corp_id = thirdpart_corp_id
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.apply_intention_info_do:
            self.apply_intention_info_do.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.apply_intention_info_do is not None:
            result['apply_intention_info_d_o'] = self.apply_intention_info_do.to_map()

        if self.btrip_cause is not None:
            result['btrip_cause'] = self.btrip_cause

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.exceed_reason is not None:
            result['exceed_reason'] = self.exceed_reason

        if self.exceed_type is not None:
            result['exceed_type'] = self.exceed_type

        if self.origin_standard is not None:
            result['origin_standard'] = self.origin_standard

        if self.status is not None:
            result['status'] = self.status

        if self.submit_time is not None:
            result['submit_time'] = self.submit_time

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('apply_intention_info_d_o') is not None:
            temp_model = main_models.TrainExceedApplyQueryResponseBodyModuleApplyIntentionInfoDO()
            self.apply_intention_info_do = temp_model.from_map(m.get('apply_intention_info_d_o'))

        if m.get('btrip_cause') is not None:
            self.btrip_cause = m.get('btrip_cause')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('exceed_reason') is not None:
            self.exceed_reason = m.get('exceed_reason')

        if m.get('exceed_type') is not None:
            self.exceed_type = m.get('exceed_type')

        if m.get('origin_standard') is not None:
            self.origin_standard = m.get('origin_standard')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('submit_time') is not None:
            self.submit_time = m.get('submit_time')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class TrainExceedApplyQueryResponseBodyModuleApplyIntentionInfoDO(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_name: str = None,
        arr_station: str = None,
        arr_time: str = None,
        dep_city: str = None,
        dep_city_name: str = None,
        dep_station: str = None,
        dep_time: str = None,
        price: int = None,
        seat_name: str = None,
        train_no: str = None,
        train_type_desc: str = None,
        type: int = None,
    ):
        self.arr_city = arr_city
        self.arr_city_name = arr_city_name
        self.arr_station = arr_station
        self.arr_time = arr_time
        self.dep_city = dep_city
        self.dep_city_name = dep_city_name
        self.dep_station = dep_station
        self.dep_time = dep_time
        self.price = price
        self.seat_name = seat_name
        self.train_no = train_no
        self.train_type_desc = train_type_desc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_station is not None:
            result['arr_station'] = self.arr_station

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_station is not None:
            result['dep_station'] = self.dep_station

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.price is not None:
            result['price'] = self.price

        if self.seat_name is not None:
            result['seat_name'] = self.seat_name

        if self.train_no is not None:
            result['train_no'] = self.train_no

        if self.train_type_desc is not None:
            result['train_type_desc'] = self.train_type_desc

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_station') is not None:
            self.dep_station = m.get('dep_station')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('seat_name') is not None:
            self.seat_name = m.get('seat_name')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        if m.get('train_type_desc') is not None:
            self.train_type_desc = m.get('train_type_desc')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

