# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderInfoQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelOrderInfoQueryResponseBodyModule = None,
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
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelOrderInfoQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        base_order_info: main_models.HotelOrderInfoQueryResponseBodyModuleBaseOrderInfo = None,
        booker_info: main_models.HotelOrderInfoQueryResponseBodyModuleBookerInfo = None,
        hotel_info: main_models.HotelOrderInfoQueryResponseBodyModuleHotelInfo = None,
        hotel_order_fee_info: main_models.HotelOrderInfoQueryResponseBodyModuleHotelOrderFeeInfo = None,
        hotel_order_refund_info: List[main_models.HotelOrderInfoQueryResponseBodyModuleHotelOrderRefundInfo] = None,
        room_traver_info: List[main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfo] = None,
    ):
        self.base_order_info = base_order_info
        self.booker_info = booker_info
        self.hotel_info = hotel_info
        self.hotel_order_fee_info = hotel_order_fee_info
        self.hotel_order_refund_info = hotel_order_refund_info
        self.room_traver_info = room_traver_info

    def validate(self):
        if self.base_order_info:
            self.base_order_info.validate()
        if self.booker_info:
            self.booker_info.validate()
        if self.hotel_info:
            self.hotel_info.validate()
        if self.hotel_order_fee_info:
            self.hotel_order_fee_info.validate()
        if self.hotel_order_refund_info:
            for v1 in self.hotel_order_refund_info:
                 if v1:
                    v1.validate()
        if self.room_traver_info:
            for v1 in self.room_traver_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_order_info is not None:
            result['base_order_info'] = self.base_order_info.to_map()

        if self.booker_info is not None:
            result['booker_info'] = self.booker_info.to_map()

        if self.hotel_info is not None:
            result['hotel_info'] = self.hotel_info.to_map()

        if self.hotel_order_fee_info is not None:
            result['hotel_order_fee_info'] = self.hotel_order_fee_info.to_map()

        result['hotel_order_refund_info'] = []
        if self.hotel_order_refund_info is not None:
            for k1 in self.hotel_order_refund_info:
                result['hotel_order_refund_info'].append(k1.to_map() if k1 else None)

        result['room_traver_info'] = []
        if self.room_traver_info is not None:
            for k1 in self.room_traver_info:
                result['room_traver_info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base_order_info') is not None:
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleBaseOrderInfo()
            self.base_order_info = temp_model.from_map(m.get('base_order_info'))

        if m.get('booker_info') is not None:
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleBookerInfo()
            self.booker_info = temp_model.from_map(m.get('booker_info'))

        if m.get('hotel_info') is not None:
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleHotelInfo()
            self.hotel_info = temp_model.from_map(m.get('hotel_info'))

        if m.get('hotel_order_fee_info') is not None:
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleHotelOrderFeeInfo()
            self.hotel_order_fee_info = temp_model.from_map(m.get('hotel_order_fee_info'))

        self.hotel_order_refund_info = []
        if m.get('hotel_order_refund_info') is not None:
            for k1 in m.get('hotel_order_refund_info'):
                temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleHotelOrderRefundInfo()
                self.hotel_order_refund_info.append(temp_model.from_map(k1))

        self.room_traver_info = []
        if m.get('room_traver_info') is not None:
            for k1 in m.get('room_traver_info'):
                temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfo()
                self.room_traver_info.append(temp_model.from_map(k1))

        return self

class HotelOrderInfoQueryResponseBodyModuleRoomTraverInfo(DaraModel):
    def __init__(
        self,
        live_room_no: str = None,
        room_type_name: str = None,
        traver_infos: List[main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfos] = None,
    ):
        self.live_room_no = live_room_no
        self.room_type_name = room_type_name
        self.traver_infos = traver_infos

    def validate(self):
        if self.traver_infos:
            for v1 in self.traver_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_room_no is not None:
            result['live_room_no'] = self.live_room_no

        if self.room_type_name is not None:
            result['room_type_name'] = self.room_type_name

        result['traver_infos'] = []
        if self.traver_infos is not None:
            for k1 in self.traver_infos:
                result['traver_infos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('live_room_no') is not None:
            self.live_room_no = m.get('live_room_no')

        if m.get('room_type_name') is not None:
            self.room_type_name = m.get('room_type_name')

        self.traver_infos = []
        if m.get('traver_infos') is not None:
            for k1 in m.get('traver_infos'):
                temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfos()
                self.traver_infos.append(temp_model.from_map(k1))

        return self

class HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfos(DaraModel):
    def __init__(
        self,
        apply_info: main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosApplyInfo = None,
        cert_no: str = None,
        cert_type: int = None,
        department: main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosDepartment = None,
        job_no: str = None,
        telephone: str = None,
        traveler_id: str = None,
        traveler_name: str = None,
        traveler_type: int = None,
        trip_cost_center: main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosTripCostCenter = None,
        user_type: int = None,
    ):
        self.apply_info = apply_info
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.department = department
        self.job_no = job_no
        self.telephone = telephone
        self.traveler_id = traveler_id
        self.traveler_name = traveler_name
        self.traveler_type = traveler_type
        self.trip_cost_center = trip_cost_center
        self.user_type = user_type

    def validate(self):
        if self.apply_info:
            self.apply_info.validate()
        if self.department:
            self.department.validate()
        if self.trip_cost_center:
            self.trip_cost_center.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_info is not None:
            result['apply_info'] = self.apply_info.to_map()

        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.department is not None:
            result['department'] = self.department.to_map()

        if self.job_no is not None:
            result['job_no'] = self.job_no

        if self.telephone is not None:
            result['telephone'] = self.telephone

        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id

        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name

        if self.traveler_type is not None:
            result['traveler_type'] = self.traveler_type

        if self.trip_cost_center is not None:
            result['trip_cost_center'] = self.trip_cost_center.to_map()

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_info') is not None:
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosApplyInfo()
            self.apply_info = temp_model.from_map(m.get('apply_info'))

        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('department') is not None:
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosDepartment()
            self.department = temp_model.from_map(m.get('department'))

        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')

        if m.get('telephone') is not None:
            self.telephone = m.get('telephone')

        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')

        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')

        if m.get('traveler_type') is not None:
            self.traveler_type = m.get('traveler_type')

        if m.get('trip_cost_center') is not None:
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosTripCostCenter()
            self.trip_cost_center = temp_model.from_map(m.get('trip_cost_center'))

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosTripCostCenter(DaraModel):
    def __init__(
        self,
        cost_center_code: str = None,
        cost_center_id: str = None,
        cost_center_name: str = None,
        external_ext_field: str = None,
        fee_type: int = None,
        invoice_id: int = None,
        invoice_title: str = None,
        project_code: str = None,
        project_title: str = None,
    ):
        self.cost_center_code = cost_center_code
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.external_ext_field = external_ext_field
        self.fee_type = fee_type
        self.invoice_id = invoice_id
        self.invoice_title = invoice_title
        self.project_code = project_code
        self.project_title = project_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_code is not None:
            result['cost_center_code'] = self.cost_center_code

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.external_ext_field is not None:
            result['external_ext_field'] = self.external_ext_field

        if self.fee_type is not None:
            result['fee_type'] = self.fee_type

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_code') is not None:
            self.cost_center_code = m.get('cost_center_code')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('external_ext_field') is not None:
            self.external_ext_field = m.get('external_ext_field')

        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        return self

class HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosDepartment(DaraModel):
    def __init__(
        self,
        cascade_dept_mask: str = None,
        cascade_dept_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        out_depart_id: str = None,
    ):
        self.cascade_dept_mask = cascade_dept_mask
        self.cascade_dept_name = cascade_dept_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.out_depart_id = out_depart_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascade_dept_mask is not None:
            result['cascade_dept_mask'] = self.cascade_dept_mask

        if self.cascade_dept_name is not None:
            result['cascade_dept_name'] = self.cascade_dept_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.out_depart_id is not None:
            result['out_depart_id'] = self.out_depart_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cascade_dept_mask') is not None:
            self.cascade_dept_mask = m.get('cascade_dept_mask')

        if m.get('cascade_dept_name') is not None:
            self.cascade_dept_name = m.get('cascade_dept_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('out_depart_id') is not None:
            self.out_depart_id = m.get('out_depart_id')

        return self

class HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosApplyInfo(DaraModel):
    def __init__(
        self,
        apply_business_id: str = None,
        apply_business_name: str = None,
        apply_id: str = None,
        exceed_apply: List[main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosApplyInfoExceedApply] = None,
        itinerary_no: str = None,
    ):
        self.apply_business_id = apply_business_id
        self.apply_business_name = apply_business_name
        self.apply_id = apply_id
        self.exceed_apply = exceed_apply
        self.itinerary_no = itinerary_no

    def validate(self):
        if self.exceed_apply:
            for v1 in self.exceed_apply:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_business_id is not None:
            result['apply_business_id'] = self.apply_business_id

        if self.apply_business_name is not None:
            result['apply_business_name'] = self.apply_business_name

        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        result['exceed_apply'] = []
        if self.exceed_apply is not None:
            for k1 in self.exceed_apply:
                result['exceed_apply'].append(k1.to_map() if k1 else None)

        if self.itinerary_no is not None:
            result['itinerary_no'] = self.itinerary_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_business_id') is not None:
            self.apply_business_id = m.get('apply_business_id')

        if m.get('apply_business_name') is not None:
            self.apply_business_name = m.get('apply_business_name')

        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        self.exceed_apply = []
        if m.get('exceed_apply') is not None:
            for k1 in m.get('exceed_apply'):
                temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosApplyInfoExceedApply()
                self.exceed_apply.append(temp_model.from_map(k1))

        if m.get('itinerary_no') is not None:
            self.itinerary_no = m.get('itinerary_no')

        return self

class HotelOrderInfoQueryResponseBodyModuleRoomTraverInfoTraverInfosApplyInfoExceedApply(DaraModel):
    def __init__(
        self,
        exceed_reason: str = None,
        exceed_type: int = None,
        flow_no: int = None,
        id: int = None,
    ):
        self.exceed_reason = exceed_reason
        self.exceed_type = exceed_type
        self.flow_no = flow_no
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exceed_reason is not None:
            result['exceed_reason'] = self.exceed_reason

        if self.exceed_type is not None:
            result['exceed_type'] = self.exceed_type

        if self.flow_no is not None:
            result['flow_no'] = self.flow_no

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exceed_reason') is not None:
            self.exceed_reason = m.get('exceed_reason')

        if m.get('exceed_type') is not None:
            self.exceed_type = m.get('exceed_type')

        if m.get('flow_no') is not None:
            self.flow_no = m.get('flow_no')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

class HotelOrderInfoQueryResponseBodyModuleHotelOrderRefundInfo(DaraModel):
    def __init__(
        self,
        cancel_fine: int = None,
        refund_apply_id: int = None,
        refund_end_time: int = None,
        refund_price: int = None,
        refund_reason: str = None,
        refund_start_time: int = None,
        refund_type: int = None,
    ):
        self.cancel_fine = cancel_fine
        self.refund_apply_id = refund_apply_id
        self.refund_end_time = refund_end_time
        self.refund_price = refund_price
        self.refund_reason = refund_reason
        self.refund_start_time = refund_start_time
        self.refund_type = refund_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_fine is not None:
            result['cancel_fine'] = self.cancel_fine

        if self.refund_apply_id is not None:
            result['refund_apply_id'] = self.refund_apply_id

        if self.refund_end_time is not None:
            result['refund_end_time'] = self.refund_end_time

        if self.refund_price is not None:
            result['refund_price'] = self.refund_price

        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason

        if self.refund_start_time is not None:
            result['refund_start_time'] = self.refund_start_time

        if self.refund_type is not None:
            result['refund_type'] = self.refund_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancel_fine') is not None:
            self.cancel_fine = m.get('cancel_fine')

        if m.get('refund_apply_id') is not None:
            self.refund_apply_id = m.get('refund_apply_id')

        if m.get('refund_end_time') is not None:
            self.refund_end_time = m.get('refund_end_time')

        if m.get('refund_price') is not None:
            self.refund_price = m.get('refund_price')

        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')

        if m.get('refund_start_time') is not None:
            self.refund_start_time = m.get('refund_start_time')

        if m.get('refund_type') is not None:
            self.refund_type = m.get('refund_type')

        return self

class HotelOrderInfoQueryResponseBodyModuleHotelOrderFeeInfo(DaraModel):
    def __init__(
        self,
        order_amount: int = None,
        other_fee: int = None,
        pay_amount: int = None,
        promotion_amount: int = None,
        total_room_amount: int = None,
    ):
        self.order_amount = order_amount
        self.other_fee = other_fee
        self.pay_amount = pay_amount
        self.promotion_amount = promotion_amount
        self.total_room_amount = total_room_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_amount is not None:
            result['order_amount'] = self.order_amount

        if self.other_fee is not None:
            result['other_fee'] = self.other_fee

        if self.pay_amount is not None:
            result['pay_amount'] = self.pay_amount

        if self.promotion_amount is not None:
            result['promotion_amount'] = self.promotion_amount

        if self.total_room_amount is not None:
            result['total_room_amount'] = self.total_room_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_amount') is not None:
            self.order_amount = m.get('order_amount')

        if m.get('other_fee') is not None:
            self.other_fee = m.get('other_fee')

        if m.get('pay_amount') is not None:
            self.pay_amount = m.get('pay_amount')

        if m.get('promotion_amount') is not None:
            self.promotion_amount = m.get('promotion_amount')

        if m.get('total_room_amount') is not None:
            self.total_room_amount = m.get('total_room_amount')

        return self

class HotelOrderInfoQueryResponseBodyModuleHotelInfo(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        country_code: str = None,
        country_name: str = None,
        district_code: str = None,
        district_name: str = None,
        hotel_address: str = None,
        hotel_brand_code: str = None,
        hotel_brand_name: str = None,
        hotel_group: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
        hotel_name_en: str = None,
        star: str = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.country_code = country_code
        self.country_name = country_name
        self.district_code = district_code
        self.district_name = district_name
        self.hotel_address = hotel_address
        self.hotel_brand_code = hotel_brand_code
        self.hotel_brand_name = hotel_brand_name
        self.hotel_group = hotel_group
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.hotel_name_en = hotel_name_en
        self.star = star

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.country_code is not None:
            result['country_code'] = self.country_code

        if self.country_name is not None:
            result['country_name'] = self.country_name

        if self.district_code is not None:
            result['district_code'] = self.district_code

        if self.district_name is not None:
            result['district_name'] = self.district_name

        if self.hotel_address is not None:
            result['hotel_address'] = self.hotel_address

        if self.hotel_brand_code is not None:
            result['hotel_brand_code'] = self.hotel_brand_code

        if self.hotel_brand_name is not None:
            result['hotel_brand_name'] = self.hotel_brand_name

        if self.hotel_group is not None:
            result['hotel_group'] = self.hotel_group

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.hotel_name_en is not None:
            result['hotel_name_en'] = self.hotel_name_en

        if self.star is not None:
            result['star'] = self.star

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        if m.get('country_name') is not None:
            self.country_name = m.get('country_name')

        if m.get('district_code') is not None:
            self.district_code = m.get('district_code')

        if m.get('district_name') is not None:
            self.district_name = m.get('district_name')

        if m.get('hotel_address') is not None:
            self.hotel_address = m.get('hotel_address')

        if m.get('hotel_brand_code') is not None:
            self.hotel_brand_code = m.get('hotel_brand_code')

        if m.get('hotel_brand_name') is not None:
            self.hotel_brand_name = m.get('hotel_brand_name')

        if m.get('hotel_group') is not None:
            self.hotel_group = m.get('hotel_group')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('hotel_name_en') is not None:
            self.hotel_name_en = m.get('hotel_name_en')

        if m.get('star') is not None:
            self.star = m.get('star')

        return self

class HotelOrderInfoQueryResponseBodyModuleBookerInfo(DaraModel):
    def __init__(
        self,
        booker_role: str = None,
        contact_email: str = None,
        contact_phone: str = None,
        corp_id: str = None,
        department: main_models.HotelOrderInfoQueryResponseBodyModuleBookerInfoDepartment = None,
        en_name: str = None,
        job_no: str = None,
        need_apply: bool = None,
        real_name: str = None,
        user_id: str = None,
    ):
        self.booker_role = booker_role
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.corp_id = corp_id
        self.department = department
        self.en_name = en_name
        self.job_no = job_no
        self.need_apply = need_apply
        self.real_name = real_name
        self.user_id = user_id

    def validate(self):
        if self.department:
            self.department.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.booker_role is not None:
            result['booker_role'] = self.booker_role

        if self.contact_email is not None:
            result['contact_email'] = self.contact_email

        if self.contact_phone is not None:
            result['contact_phone'] = self.contact_phone

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.department is not None:
            result['department'] = self.department.to_map()

        if self.en_name is not None:
            result['en_name'] = self.en_name

        if self.job_no is not None:
            result['job_no'] = self.job_no

        if self.need_apply is not None:
            result['need_apply'] = self.need_apply

        if self.real_name is not None:
            result['real_name'] = self.real_name

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('booker_role') is not None:
            self.booker_role = m.get('booker_role')

        if m.get('contact_email') is not None:
            self.contact_email = m.get('contact_email')

        if m.get('contact_phone') is not None:
            self.contact_phone = m.get('contact_phone')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('department') is not None:
            temp_model = main_models.HotelOrderInfoQueryResponseBodyModuleBookerInfoDepartment()
            self.department = temp_model.from_map(m.get('department'))

        if m.get('en_name') is not None:
            self.en_name = m.get('en_name')

        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')

        if m.get('need_apply') is not None:
            self.need_apply = m.get('need_apply')

        if m.get('real_name') is not None:
            self.real_name = m.get('real_name')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class HotelOrderInfoQueryResponseBodyModuleBookerInfoDepartment(DaraModel):
    def __init__(
        self,
        cascade_dept_mask: str = None,
        cascade_dept_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        out_depart_id: str = None,
    ):
        self.cascade_dept_mask = cascade_dept_mask
        self.cascade_dept_name = cascade_dept_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.out_depart_id = out_depart_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascade_dept_mask is not None:
            result['cascade_dept_mask'] = self.cascade_dept_mask

        if self.cascade_dept_name is not None:
            result['cascade_dept_name'] = self.cascade_dept_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.out_depart_id is not None:
            result['out_depart_id'] = self.out_depart_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cascade_dept_mask') is not None:
            self.cascade_dept_mask = m.get('cascade_dept_mask')

        if m.get('cascade_dept_name') is not None:
            self.cascade_dept_name = m.get('cascade_dept_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('out_depart_id') is not None:
            self.out_depart_id = m.get('out_depart_id')

        return self

class HotelOrderInfoQueryResponseBodyModuleBaseOrderInfo(DaraModel):
    def __init__(
        self,
        book_mode: str = None,
        booker_id: str = None,
        booker_name: str = None,
        btrip_corp_id: str = None,
        category: int = None,
        check_in_time: int = None,
        check_out_time: int = None,
        is_agreement_price: bool = None,
        nights: int = None,
        order_create_time: int = None,
        order_id: int = None,
        order_status: int = None,
        order_status_desc: str = None,
        pay_status: int = None,
        pay_time: int = None,
        room_num: int = None,
        settle_type: int = None,
        trip_mode: int = None,
    ):
        self.book_mode = book_mode
        self.booker_id = booker_id
        self.booker_name = booker_name
        self.btrip_corp_id = btrip_corp_id
        self.category = category
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.is_agreement_price = is_agreement_price
        self.nights = nights
        self.order_create_time = order_create_time
        self.order_id = order_id
        self.order_status = order_status
        self.order_status_desc = order_status_desc
        self.pay_status = pay_status
        self.pay_time = pay_time
        self.room_num = room_num
        self.settle_type = settle_type
        self.trip_mode = trip_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.book_mode is not None:
            result['book_mode'] = self.book_mode

        if self.booker_id is not None:
            result['booker_id'] = self.booker_id

        if self.booker_name is not None:
            result['booker_name'] = self.booker_name

        if self.btrip_corp_id is not None:
            result['btrip_corp_id'] = self.btrip_corp_id

        if self.category is not None:
            result['category'] = self.category

        if self.check_in_time is not None:
            result['check_in_time'] = self.check_in_time

        if self.check_out_time is not None:
            result['check_out_time'] = self.check_out_time

        if self.is_agreement_price is not None:
            result['is_agreement_price'] = self.is_agreement_price

        if self.nights is not None:
            result['nights'] = self.nights

        if self.order_create_time is not None:
            result['order_create_time'] = self.order_create_time

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.order_status_desc is not None:
            result['order_status_desc'] = self.order_status_desc

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.room_num is not None:
            result['room_num'] = self.room_num

        if self.settle_type is not None:
            result['settle_type'] = self.settle_type

        if self.trip_mode is not None:
            result['trip_mode'] = self.trip_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('book_mode') is not None:
            self.book_mode = m.get('book_mode')

        if m.get('booker_id') is not None:
            self.booker_id = m.get('booker_id')

        if m.get('booker_name') is not None:
            self.booker_name = m.get('booker_name')

        if m.get('btrip_corp_id') is not None:
            self.btrip_corp_id = m.get('btrip_corp_id')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('check_in_time') is not None:
            self.check_in_time = m.get('check_in_time')

        if m.get('check_out_time') is not None:
            self.check_out_time = m.get('check_out_time')

        if m.get('is_agreement_price') is not None:
            self.is_agreement_price = m.get('is_agreement_price')

        if m.get('nights') is not None:
            self.nights = m.get('nights')

        if m.get('order_create_time') is not None:
            self.order_create_time = m.get('order_create_time')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('order_status_desc') is not None:
            self.order_status_desc = m.get('order_status_desc')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('room_num') is not None:
            self.room_num = m.get('room_num')

        if m.get('settle_type') is not None:
            self.settle_type = m.get('settle_type')

        if m.get('trip_mode') is not None:
            self.trip_mode = m.get('trip_mode')

        return self

