# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class WaitApplyInvoiceTaskDetailQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.WaitApplyInvoiceTaskDetailQueryResponseBodyModule] = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        # requestId
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

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

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.WaitApplyInvoiceTaskDetailQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class WaitApplyInvoiceTaskDetailQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        contact: str = None,
        email: str = None,
        flight_invoice_fee: str = None,
        fu_point_invoice_fee: str = None,
        hotel_normal_invoice_fee: str = None,
        hotel_special_invoice_fee: str = None,
        ie_vehicle_normal_invoice_fee: str = None,
        international_flight_invoice_fee: str = None,
        international_hotel_invoice_fee: str = None,
        invoice_third_part_id: str = None,
        invoice_title: str = None,
        mail_address: str = None,
        mail_city: str = None,
        mail_full_address: str = None,
        mail_province: str = None,
        meal_normal_invoice_fee: str = None,
        meal_tc_7normal_invoice_fee: str = None,
        penalty_fee: str = None,
        remark: str = None,
        service_fee: str = None,
        telephone: str = None,
        train_acceleration_package_invoice_fee: str = None,
        train_invoice_fee: str = None,
        vacation_normal_invoice_fee: str = None,
        vas_mall_special_invoice_fee: str = None,
        vehicle_invoice_fee: str = None,
        vehicle_normal_invoice_fee: str = None,
    ):
        self.contact = contact
        self.email = email
        self.flight_invoice_fee = flight_invoice_fee
        self.fu_point_invoice_fee = fu_point_invoice_fee
        self.hotel_normal_invoice_fee = hotel_normal_invoice_fee
        self.hotel_special_invoice_fee = hotel_special_invoice_fee
        self.ie_vehicle_normal_invoice_fee = ie_vehicle_normal_invoice_fee
        self.international_flight_invoice_fee = international_flight_invoice_fee
        self.international_hotel_invoice_fee = international_hotel_invoice_fee
        self.invoice_third_part_id = invoice_third_part_id
        self.invoice_title = invoice_title
        self.mail_address = mail_address
        self.mail_city = mail_city
        self.mail_full_address = mail_full_address
        self.mail_province = mail_province
        self.meal_normal_invoice_fee = meal_normal_invoice_fee
        self.meal_tc_7normal_invoice_fee = meal_tc_7normal_invoice_fee
        self.penalty_fee = penalty_fee
        self.remark = remark
        self.service_fee = service_fee
        self.telephone = telephone
        self.train_acceleration_package_invoice_fee = train_acceleration_package_invoice_fee
        self.train_invoice_fee = train_invoice_fee
        self.vacation_normal_invoice_fee = vacation_normal_invoice_fee
        self.vas_mall_special_invoice_fee = vas_mall_special_invoice_fee
        self.vehicle_invoice_fee = vehicle_invoice_fee
        self.vehicle_normal_invoice_fee = vehicle_normal_invoice_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact is not None:
            result['contact'] = self.contact

        if self.email is not None:
            result['email'] = self.email

        if self.flight_invoice_fee is not None:
            result['flight_invoice_fee'] = self.flight_invoice_fee

        if self.fu_point_invoice_fee is not None:
            result['fu_point_invoice_fee'] = self.fu_point_invoice_fee

        if self.hotel_normal_invoice_fee is not None:
            result['hotel_normal_invoice_fee'] = self.hotel_normal_invoice_fee

        if self.hotel_special_invoice_fee is not None:
            result['hotel_special_invoice_fee'] = self.hotel_special_invoice_fee

        if self.ie_vehicle_normal_invoice_fee is not None:
            result['ie_vehicle_normal_invoice_fee'] = self.ie_vehicle_normal_invoice_fee

        if self.international_flight_invoice_fee is not None:
            result['international_flight_invoice_fee'] = self.international_flight_invoice_fee

        if self.international_hotel_invoice_fee is not None:
            result['international_hotel_invoice_fee'] = self.international_hotel_invoice_fee

        if self.invoice_third_part_id is not None:
            result['invoice_third_part_id'] = self.invoice_third_part_id

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.mail_address is not None:
            result['mail_address'] = self.mail_address

        if self.mail_city is not None:
            result['mail_city'] = self.mail_city

        if self.mail_full_address is not None:
            result['mail_full_address'] = self.mail_full_address

        if self.mail_province is not None:
            result['mail_province'] = self.mail_province

        if self.meal_normal_invoice_fee is not None:
            result['meal_normal_invoice_fee'] = self.meal_normal_invoice_fee

        if self.meal_tc_7normal_invoice_fee is not None:
            result['meal_tc7_normal_invoice_fee'] = self.meal_tc_7normal_invoice_fee

        if self.penalty_fee is not None:
            result['penalty_fee'] = self.penalty_fee

        if self.remark is not None:
            result['remark'] = self.remark

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        if self.telephone is not None:
            result['telephone'] = self.telephone

        if self.train_acceleration_package_invoice_fee is not None:
            result['train_acceleration_package_invoice_fee'] = self.train_acceleration_package_invoice_fee

        if self.train_invoice_fee is not None:
            result['train_invoice_fee'] = self.train_invoice_fee

        if self.vacation_normal_invoice_fee is not None:
            result['vacation_normal_invoice_fee'] = self.vacation_normal_invoice_fee

        if self.vas_mall_special_invoice_fee is not None:
            result['vas_mall_special_invoice_fee'] = self.vas_mall_special_invoice_fee

        if self.vehicle_invoice_fee is not None:
            result['vehicle_invoice_fee'] = self.vehicle_invoice_fee

        if self.vehicle_normal_invoice_fee is not None:
            result['vehicle_normal_invoice_fee'] = self.vehicle_normal_invoice_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact') is not None:
            self.contact = m.get('contact')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('flight_invoice_fee') is not None:
            self.flight_invoice_fee = m.get('flight_invoice_fee')

        if m.get('fu_point_invoice_fee') is not None:
            self.fu_point_invoice_fee = m.get('fu_point_invoice_fee')

        if m.get('hotel_normal_invoice_fee') is not None:
            self.hotel_normal_invoice_fee = m.get('hotel_normal_invoice_fee')

        if m.get('hotel_special_invoice_fee') is not None:
            self.hotel_special_invoice_fee = m.get('hotel_special_invoice_fee')

        if m.get('ie_vehicle_normal_invoice_fee') is not None:
            self.ie_vehicle_normal_invoice_fee = m.get('ie_vehicle_normal_invoice_fee')

        if m.get('international_flight_invoice_fee') is not None:
            self.international_flight_invoice_fee = m.get('international_flight_invoice_fee')

        if m.get('international_hotel_invoice_fee') is not None:
            self.international_hotel_invoice_fee = m.get('international_hotel_invoice_fee')

        if m.get('invoice_third_part_id') is not None:
            self.invoice_third_part_id = m.get('invoice_third_part_id')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('mail_address') is not None:
            self.mail_address = m.get('mail_address')

        if m.get('mail_city') is not None:
            self.mail_city = m.get('mail_city')

        if m.get('mail_full_address') is not None:
            self.mail_full_address = m.get('mail_full_address')

        if m.get('mail_province') is not None:
            self.mail_province = m.get('mail_province')

        if m.get('meal_normal_invoice_fee') is not None:
            self.meal_normal_invoice_fee = m.get('meal_normal_invoice_fee')

        if m.get('meal_tc7_normal_invoice_fee') is not None:
            self.meal_tc_7normal_invoice_fee = m.get('meal_tc7_normal_invoice_fee')

        if m.get('penalty_fee') is not None:
            self.penalty_fee = m.get('penalty_fee')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        if m.get('telephone') is not None:
            self.telephone = m.get('telephone')

        if m.get('train_acceleration_package_invoice_fee') is not None:
            self.train_acceleration_package_invoice_fee = m.get('train_acceleration_package_invoice_fee')

        if m.get('train_invoice_fee') is not None:
            self.train_invoice_fee = m.get('train_invoice_fee')

        if m.get('vacation_normal_invoice_fee') is not None:
            self.vacation_normal_invoice_fee = m.get('vacation_normal_invoice_fee')

        if m.get('vas_mall_special_invoice_fee') is not None:
            self.vas_mall_special_invoice_fee = m.get('vas_mall_special_invoice_fee')

        if m.get('vehicle_invoice_fee') is not None:
            self.vehicle_invoice_fee = m.get('vehicle_invoice_fee')

        if m.get('vehicle_normal_invoice_fee') is not None:
            self.vehicle_normal_invoice_fee = m.get('vehicle_normal_invoice_fee')

        return self

