# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelExceedApplyQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelExceedApplyQueryResponseBodyModule = None,
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
            temp_model = main_models.HotelExceedApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelExceedApplyQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_intention_info_do: main_models.HotelExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo = None,
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
            result['apply_intention_info_do'] = self.apply_intention_info_do.to_map()

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

        if m.get('apply_intention_info_do') is not None:
            temp_model = main_models.HotelExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo()
            self.apply_intention_info_do = temp_model.from_map(m.get('apply_intention_info_do'))

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

class HotelExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo(DaraModel):
    def __init__(
        self,
        check_in: str = None,
        check_out: str = None,
        city_code: str = None,
        city_name: str = None,
        price: int = None,
        together: bool = None,
        type: int = None,
    ):
        self.check_in = check_in
        self.check_out = check_out
        self.city_code = city_code
        self.city_name = city_name
        self.price = price
        self.together = together
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.price is not None:
            result['price'] = self.price

        if self.together is not None:
            result['together'] = self.together

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('together') is not None:
            self.together = m.get('together')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

