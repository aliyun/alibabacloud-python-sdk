# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TicketPageQueryProductResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TicketPageQueryProductResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TicketPageQueryProductResponseBodyData(DaraModel):
    def __init__(
        self,
        products: List[main_models.TicketPageQueryProductResponseBodyDataProducts] = None,
        total_size: int = None,
    ):
        self.products = products
        self.total_size = total_size

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.TicketPageQueryProductResponseBodyDataProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class TicketPageQueryProductResponseBodyDataProducts(DaraModel):
    def __init__(
        self,
        booking_type: int = None,
        buy_rule: main_models.TicketPageQueryProductResponseBodyDataProductsBuyRule = None,
        cost_include_remark: str = None,
        deliver_guarantee_minutes: int = None,
        images: List[str] = None,
        invoice_issuer_type: int = None,
        payment_limit_minutes: int = None,
        product_id: str = None,
        product_name: str = None,
        refund_rule: main_models.TicketPageQueryProductResponseBodyDataProductsRefundRule = None,
        region: main_models.TicketPageQueryProductResponseBodyDataProductsRegion = None,
        scenic_id: int = None,
        session: main_models.TicketPageQueryProductResponseBodyDataProductsSession = None,
        settle_price_calculate_type: int = None,
        spu: main_models.TicketPageQueryProductResponseBodyDataProductsSpu = None,
        supplier_name: str = None,
        ticket_kind: main_models.TicketPageQueryProductResponseBodyDataProductsTicketKind = None,
        use_rule: main_models.TicketPageQueryProductResponseBodyDataProductsUseRule = None,
    ):
        self.booking_type = booking_type
        self.buy_rule = buy_rule
        self.cost_include_remark = cost_include_remark
        self.deliver_guarantee_minutes = deliver_guarantee_minutes
        self.images = images
        self.invoice_issuer_type = invoice_issuer_type
        self.payment_limit_minutes = payment_limit_minutes
        self.product_id = product_id
        self.product_name = product_name
        self.refund_rule = refund_rule
        self.region = region
        self.scenic_id = scenic_id
        self.session = session
        self.settle_price_calculate_type = settle_price_calculate_type
        self.spu = spu
        self.supplier_name = supplier_name
        self.ticket_kind = ticket_kind
        self.use_rule = use_rule

    def validate(self):
        if self.buy_rule:
            self.buy_rule.validate()
        if self.refund_rule:
            self.refund_rule.validate()
        if self.region:
            self.region.validate()
        if self.session:
            self.session.validate()
        if self.spu:
            self.spu.validate()
        if self.ticket_kind:
            self.ticket_kind.validate()
        if self.use_rule:
            self.use_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.booking_type is not None:
            result['BookingType'] = self.booking_type

        if self.buy_rule is not None:
            result['BuyRule'] = self.buy_rule.to_map()

        if self.cost_include_remark is not None:
            result['CostIncludeRemark'] = self.cost_include_remark

        if self.deliver_guarantee_minutes is not None:
            result['DeliverGuaranteeMinutes'] = self.deliver_guarantee_minutes

        if self.images is not None:
            result['Images'] = self.images

        if self.invoice_issuer_type is not None:
            result['InvoiceIssuerType'] = self.invoice_issuer_type

        if self.payment_limit_minutes is not None:
            result['PaymentLimitMinutes'] = self.payment_limit_minutes

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.refund_rule is not None:
            result['RefundRule'] = self.refund_rule.to_map()

        if self.region is not None:
            result['Region'] = self.region.to_map()

        if self.scenic_id is not None:
            result['ScenicId'] = self.scenic_id

        if self.session is not None:
            result['Session'] = self.session.to_map()

        if self.settle_price_calculate_type is not None:
            result['SettlePriceCalculateType'] = self.settle_price_calculate_type

        if self.spu is not None:
            result['Spu'] = self.spu.to_map()

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.ticket_kind is not None:
            result['TicketKind'] = self.ticket_kind.to_map()

        if self.use_rule is not None:
            result['UseRule'] = self.use_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BookingType') is not None:
            self.booking_type = m.get('BookingType')

        if m.get('BuyRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRule()
            self.buy_rule = temp_model.from_map(m.get('BuyRule'))

        if m.get('CostIncludeRemark') is not None:
            self.cost_include_remark = m.get('CostIncludeRemark')

        if m.get('DeliverGuaranteeMinutes') is not None:
            self.deliver_guarantee_minutes = m.get('DeliverGuaranteeMinutes')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('InvoiceIssuerType') is not None:
            self.invoice_issuer_type = m.get('InvoiceIssuerType')

        if m.get('PaymentLimitMinutes') is not None:
            self.payment_limit_minutes = m.get('PaymentLimitMinutes')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RefundRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsRefundRule()
            self.refund_rule = temp_model.from_map(m.get('RefundRule'))

        if m.get('Region') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsRegion()
            self.region = temp_model.from_map(m.get('Region'))

        if m.get('ScenicId') is not None:
            self.scenic_id = m.get('ScenicId')

        if m.get('Session') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsSession()
            self.session = temp_model.from_map(m.get('Session'))

        if m.get('SettlePriceCalculateType') is not None:
            self.settle_price_calculate_type = m.get('SettlePriceCalculateType')

        if m.get('Spu') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsSpu()
            self.spu = temp_model.from_map(m.get('Spu'))

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('TicketKind') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsTicketKind()
            self.ticket_kind = temp_model.from_map(m.get('TicketKind'))

        if m.get('UseRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsUseRule()
            self.use_rule = temp_model.from_map(m.get('UseRule'))

        return self

class TicketPageQueryProductResponseBodyDataProductsUseRule(DaraModel):
    def __init__(
        self,
        effect_time_point_rule: main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleEffectTimePointRule = None,
        entry_address: str = None,
        entry_remark: str = None,
        entry_time_periods: List[main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleEntryTimePeriods] = None,
        entry_type: int = None,
        entry_with_voucher_rule: main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleEntryWithVoucherRule = None,
        need_assemble: bool = None,
        need_prebook: bool = None,
        other_note: str = None,
        pickups_rule: main_models.TicketPageQueryProductResponseBodyDataProductsUseRulePickupsRule = None,
        validity_period_rule: main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRule = None,
    ):
        self.effect_time_point_rule = effect_time_point_rule
        self.entry_address = entry_address
        self.entry_remark = entry_remark
        self.entry_time_periods = entry_time_periods
        self.entry_type = entry_type
        self.entry_with_voucher_rule = entry_with_voucher_rule
        self.need_assemble = need_assemble
        self.need_prebook = need_prebook
        self.other_note = other_note
        self.pickups_rule = pickups_rule
        self.validity_period_rule = validity_period_rule

    def validate(self):
        if self.effect_time_point_rule:
            self.effect_time_point_rule.validate()
        if self.entry_time_periods:
            for v1 in self.entry_time_periods:
                 if v1:
                    v1.validate()
        if self.entry_with_voucher_rule:
            self.entry_with_voucher_rule.validate()
        if self.pickups_rule:
            self.pickups_rule.validate()
        if self.validity_period_rule:
            self.validity_period_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect_time_point_rule is not None:
            result['EffectTimePointRule'] = self.effect_time_point_rule.to_map()

        if self.entry_address is not None:
            result['EntryAddress'] = self.entry_address

        if self.entry_remark is not None:
            result['EntryRemark'] = self.entry_remark

        result['EntryTimePeriods'] = []
        if self.entry_time_periods is not None:
            for k1 in self.entry_time_periods:
                result['EntryTimePeriods'].append(k1.to_map() if k1 else None)

        if self.entry_type is not None:
            result['EntryType'] = self.entry_type

        if self.entry_with_voucher_rule is not None:
            result['EntryWithVoucherRule'] = self.entry_with_voucher_rule.to_map()

        if self.need_assemble is not None:
            result['NeedAssemble'] = self.need_assemble

        if self.need_prebook is not None:
            result['NeedPrebook'] = self.need_prebook

        if self.other_note is not None:
            result['OtherNote'] = self.other_note

        if self.pickups_rule is not None:
            result['PickupsRule'] = self.pickups_rule.to_map()

        if self.validity_period_rule is not None:
            result['ValidityPeriodRule'] = self.validity_period_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectTimePointRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleEffectTimePointRule()
            self.effect_time_point_rule = temp_model.from_map(m.get('EffectTimePointRule'))

        if m.get('EntryAddress') is not None:
            self.entry_address = m.get('EntryAddress')

        if m.get('EntryRemark') is not None:
            self.entry_remark = m.get('EntryRemark')

        self.entry_time_periods = []
        if m.get('EntryTimePeriods') is not None:
            for k1 in m.get('EntryTimePeriods'):
                temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleEntryTimePeriods()
                self.entry_time_periods.append(temp_model.from_map(k1))

        if m.get('EntryType') is not None:
            self.entry_type = m.get('EntryType')

        if m.get('EntryWithVoucherRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleEntryWithVoucherRule()
            self.entry_with_voucher_rule = temp_model.from_map(m.get('EntryWithVoucherRule'))

        if m.get('NeedAssemble') is not None:
            self.need_assemble = m.get('NeedAssemble')

        if m.get('NeedPrebook') is not None:
            self.need_prebook = m.get('NeedPrebook')

        if m.get('OtherNote') is not None:
            self.other_note = m.get('OtherNote')

        if m.get('PickupsRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsUseRulePickupsRule()
            self.pickups_rule = temp_model.from_map(m.get('PickupsRule'))

        if m.get('ValidityPeriodRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRule()
            self.validity_period_rule = temp_model.from_map(m.get('ValidityPeriodRule'))

        return self

class TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRule(DaraModel):
    def __init__(
        self,
        available_weeks: List[int] = None,
        from_: main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRuleFrom_ = None,
        to: main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRuleTo = None,
        unavailable_dates: List[str] = None,
    ):
        self.available_weeks = available_weeks
        self.from_ = from_
        self.to = to
        self.unavailable_dates = unavailable_dates

    def validate(self):
        if self.from_:
            self.from_.validate()
        if self.to:
            self.to.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_weeks is not None:
            result['AvailableWeeks'] = self.available_weeks

        if self.from_ is not None:
            result['From'] = self.from_.to_map()

        if self.to is not None:
            result['To'] = self.to.to_map()

        if self.unavailable_dates is not None:
            result['UnavailableDates'] = self.unavailable_dates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableWeeks') is not None:
            self.available_weeks = m.get('AvailableWeeks')

        if m.get('From') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRuleFrom_()
            self.from_ = temp_model.from_map(m.get('From'))

        if m.get('To') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRuleTo()
            self.to = temp_model.from_map(m.get('To'))

        if m.get('UnavailableDates') is not None:
            self.unavailable_dates = m.get('UnavailableDates')

        return self

class TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRuleTo(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        fixed_time: str = None,
        offset_day_of_time: str = None,
        offset_unit: int = None,
        offset_value: int = None,
    ):
        self.anchor = anchor
        self.fixed_time = fixed_time
        self.offset_day_of_time = offset_day_of_time
        self.offset_unit = offset_unit
        self.offset_value = offset_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time

        if self.offset_day_of_time is not None:
            result['OffsetDayOfTime'] = self.offset_day_of_time

        if self.offset_unit is not None:
            result['OffsetUnit'] = self.offset_unit

        if self.offset_value is not None:
            result['OffsetValue'] = self.offset_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')

        if m.get('OffsetDayOfTime') is not None:
            self.offset_day_of_time = m.get('OffsetDayOfTime')

        if m.get('OffsetUnit') is not None:
            self.offset_unit = m.get('OffsetUnit')

        if m.get('OffsetValue') is not None:
            self.offset_value = m.get('OffsetValue')

        return self

class TicketPageQueryProductResponseBodyDataProductsUseRuleValidityPeriodRuleFrom(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        fixed_time: str = None,
        offset_day_of_time: str = None,
        offset_unit: int = None,
        offset_value: int = None,
    ):
        self.anchor = anchor
        self.fixed_time = fixed_time
        self.offset_day_of_time = offset_day_of_time
        self.offset_unit = offset_unit
        self.offset_value = offset_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time

        if self.offset_day_of_time is not None:
            result['OffsetDayOfTime'] = self.offset_day_of_time

        if self.offset_unit is not None:
            result['OffsetUnit'] = self.offset_unit

        if self.offset_value is not None:
            result['OffsetValue'] = self.offset_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')

        if m.get('OffsetDayOfTime') is not None:
            self.offset_day_of_time = m.get('OffsetDayOfTime')

        if m.get('OffsetUnit') is not None:
            self.offset_unit = m.get('OffsetUnit')

        if m.get('OffsetValue') is not None:
            self.offset_value = m.get('OffsetValue')

        return self

class TicketPageQueryProductResponseBodyDataProductsUseRulePickupsRule(DaraModel):
    def __init__(
        self,
        pickups_address: str = None,
        voucher_remark: str = None,
        voucher_types: List[int] = None,
    ):
        self.pickups_address = pickups_address
        self.voucher_remark = voucher_remark
        self.voucher_types = voucher_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pickups_address is not None:
            result['PickupsAddress'] = self.pickups_address

        if self.voucher_remark is not None:
            result['VoucherRemark'] = self.voucher_remark

        if self.voucher_types is not None:
            result['VoucherTypes'] = self.voucher_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PickupsAddress') is not None:
            self.pickups_address = m.get('PickupsAddress')

        if m.get('VoucherRemark') is not None:
            self.voucher_remark = m.get('VoucherRemark')

        if m.get('VoucherTypes') is not None:
            self.voucher_types = m.get('VoucherTypes')

        return self

class TicketPageQueryProductResponseBodyDataProductsUseRuleEntryWithVoucherRule(DaraModel):
    def __init__(
        self,
        voucher_remark: str = None,
        voucher_types: List[int] = None,
    ):
        self.voucher_remark = voucher_remark
        self.voucher_types = voucher_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.voucher_remark is not None:
            result['VoucherRemark'] = self.voucher_remark

        if self.voucher_types is not None:
            result['VoucherTypes'] = self.voucher_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VoucherRemark') is not None:
            self.voucher_remark = m.get('VoucherRemark')

        if m.get('VoucherTypes') is not None:
            self.voucher_types = m.get('VoucherTypes')

        return self

class TicketPageQueryProductResponseBodyDataProductsUseRuleEntryTimePeriods(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        return self

class TicketPageQueryProductResponseBodyDataProductsUseRuleEffectTimePointRule(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        fixed_time: str = None,
        offset_day_of_time: str = None,
        offset_unit: int = None,
        offset_value: int = None,
    ):
        self.anchor = anchor
        self.fixed_time = fixed_time
        self.offset_day_of_time = offset_day_of_time
        self.offset_unit = offset_unit
        self.offset_value = offset_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time

        if self.offset_day_of_time is not None:
            result['OffsetDayOfTime'] = self.offset_day_of_time

        if self.offset_unit is not None:
            result['OffsetUnit'] = self.offset_unit

        if self.offset_value is not None:
            result['OffsetValue'] = self.offset_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')

        if m.get('OffsetDayOfTime') is not None:
            self.offset_day_of_time = m.get('OffsetDayOfTime')

        if m.get('OffsetUnit') is not None:
            self.offset_unit = m.get('OffsetUnit')

        if m.get('OffsetValue') is not None:
            self.offset_value = m.get('OffsetValue')

        return self

class TicketPageQueryProductResponseBodyDataProductsTicketKind(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class TicketPageQueryProductResponseBodyDataProductsSpu(DaraModel):
    def __init__(
        self,
        primary_type_name: str = None,
        reserve_detail: str = None,
        reserve_title: str = None,
        secondary_type_name: str = None,
        spu_id: int = None,
        spu_name: str = None,
    ):
        self.primary_type_name = primary_type_name
        self.reserve_detail = reserve_detail
        self.reserve_title = reserve_title
        self.secondary_type_name = secondary_type_name
        self.spu_id = spu_id
        self.spu_name = spu_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary_type_name is not None:
            result['PrimaryTypeName'] = self.primary_type_name

        if self.reserve_detail is not None:
            result['ReserveDetail'] = self.reserve_detail

        if self.reserve_title is not None:
            result['ReserveTitle'] = self.reserve_title

        if self.secondary_type_name is not None:
            result['SecondaryTypeName'] = self.secondary_type_name

        if self.spu_id is not None:
            result['SpuId'] = self.spu_id

        if self.spu_name is not None:
            result['SpuName'] = self.spu_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrimaryTypeName') is not None:
            self.primary_type_name = m.get('PrimaryTypeName')

        if m.get('ReserveDetail') is not None:
            self.reserve_detail = m.get('ReserveDetail')

        if m.get('ReserveTitle') is not None:
            self.reserve_title = m.get('ReserveTitle')

        if m.get('SecondaryTypeName') is not None:
            self.secondary_type_name = m.get('SecondaryTypeName')

        if m.get('SpuId') is not None:
            self.spu_id = m.get('SpuId')

        if m.get('SpuName') is not None:
            self.spu_name = m.get('SpuName')

        return self

class TicketPageQueryProductResponseBodyDataProductsSession(DaraModel):
    def __init__(
        self,
        session_end_time: str = None,
        session_name: str = None,
        session_start_time: str = None,
    ):
        self.session_end_time = session_end_time
        self.session_name = session_name
        self.session_start_time = session_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_end_time is not None:
            result['SessionEndTime'] = self.session_end_time

        if self.session_name is not None:
            result['SessionName'] = self.session_name

        if self.session_start_time is not None:
            result['SessionStartTime'] = self.session_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionEndTime') is not None:
            self.session_end_time = m.get('SessionEndTime')

        if m.get('SessionName') is not None:
            self.session_name = m.get('SessionName')

        if m.get('SessionStartTime') is not None:
            self.session_start_time = m.get('SessionStartTime')

        return self

class TicketPageQueryProductResponseBodyDataProductsRegion(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class TicketPageQueryProductResponseBodyDataProductsRefundRule(DaraModel):
    def __init__(
        self,
        refund_stage_rules: List[main_models.TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRules] = None,
        refund_type: int = None,
    ):
        self.refund_stage_rules = refund_stage_rules
        self.refund_type = refund_type

    def validate(self):
        if self.refund_stage_rules:
            for v1 in self.refund_stage_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RefundStageRules'] = []
        if self.refund_stage_rules is not None:
            for k1 in self.refund_stage_rules:
                result['RefundStageRules'].append(k1.to_map() if k1 else None)

        if self.refund_type is not None:
            result['RefundType'] = self.refund_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refund_stage_rules = []
        if m.get('RefundStageRules') is not None:
            for k1 in m.get('RefundStageRules'):
                temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRules()
                self.refund_stage_rules.append(temp_model.from_map(k1))

        if m.get('RefundType') is not None:
            self.refund_type = m.get('RefundType')

        return self

class TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRules(DaraModel):
    def __init__(
        self,
        fee: float = None,
        fee_base: int = None,
        fee_type: int = None,
        from_: main_models.TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRulesFrom_ = None,
        to: main_models.TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRulesTo = None,
    ):
        self.fee = fee
        self.fee_base = fee_base
        self.fee_type = fee_type
        self.from_ = from_
        self.to = to

    def validate(self):
        if self.from_:
            self.from_.validate()
        if self.to:
            self.to.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee is not None:
            result['Fee'] = self.fee

        if self.fee_base is not None:
            result['FeeBase'] = self.fee_base

        if self.fee_type is not None:
            result['FeeType'] = self.fee_type

        if self.from_ is not None:
            result['From'] = self.from_.to_map()

        if self.to is not None:
            result['To'] = self.to.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fee') is not None:
            self.fee = m.get('Fee')

        if m.get('FeeBase') is not None:
            self.fee_base = m.get('FeeBase')

        if m.get('FeeType') is not None:
            self.fee_type = m.get('FeeType')

        if m.get('From') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRulesFrom_()
            self.from_ = temp_model.from_map(m.get('From'))

        if m.get('To') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRulesTo()
            self.to = temp_model.from_map(m.get('To'))

        return self

class TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRulesTo(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        fixed_time: str = None,
        offset_day_of_time: str = None,
        offset_unit: int = None,
        offset_value: int = None,
    ):
        self.anchor = anchor
        self.fixed_time = fixed_time
        self.offset_day_of_time = offset_day_of_time
        self.offset_unit = offset_unit
        self.offset_value = offset_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time

        if self.offset_day_of_time is not None:
            result['OffsetDayOfTime'] = self.offset_day_of_time

        if self.offset_unit is not None:
            result['OffsetUnit'] = self.offset_unit

        if self.offset_value is not None:
            result['OffsetValue'] = self.offset_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')

        if m.get('OffsetDayOfTime') is not None:
            self.offset_day_of_time = m.get('OffsetDayOfTime')

        if m.get('OffsetUnit') is not None:
            self.offset_unit = m.get('OffsetUnit')

        if m.get('OffsetValue') is not None:
            self.offset_value = m.get('OffsetValue')

        return self

class TicketPageQueryProductResponseBodyDataProductsRefundRuleRefundStageRulesFrom(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        fixed_time: str = None,
        offset_day_of_time: str = None,
        offset_unit: int = None,
        offset_value: int = None,
    ):
        self.anchor = anchor
        self.fixed_time = fixed_time
        self.offset_day_of_time = offset_day_of_time
        self.offset_unit = offset_unit
        self.offset_value = offset_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time

        if self.offset_day_of_time is not None:
            result['OffsetDayOfTime'] = self.offset_day_of_time

        if self.offset_unit is not None:
            result['OffsetUnit'] = self.offset_unit

        if self.offset_value is not None:
            result['OffsetValue'] = self.offset_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')

        if m.get('OffsetDayOfTime') is not None:
            self.offset_day_of_time = m.get('OffsetDayOfTime')

        if m.get('OffsetUnit') is not None:
            self.offset_unit = m.get('OffsetUnit')

        if m.get('OffsetValue') is not None:
            self.offset_value = m.get('OffsetValue')

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRule(DaraModel):
    def __init__(
        self,
        ahead_buy_time_point_rule: main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleAheadBuyTimePointRule = None,
        contact_rule: main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleContactRule = None,
        cross_order_buy_quantity_limit_rules: List[main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleCrossOrderBuyQuantityLimitRules] = None,
        per_order_buy_quantity_limit_rule: main_models.TicketPageQueryProductResponseBodyDataProductsBuyRulePerOrderBuyQuantityLimitRule = None,
        traveler_rule: main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRule = None,
    ):
        self.ahead_buy_time_point_rule = ahead_buy_time_point_rule
        self.contact_rule = contact_rule
        self.cross_order_buy_quantity_limit_rules = cross_order_buy_quantity_limit_rules
        self.per_order_buy_quantity_limit_rule = per_order_buy_quantity_limit_rule
        self.traveler_rule = traveler_rule

    def validate(self):
        if self.ahead_buy_time_point_rule:
            self.ahead_buy_time_point_rule.validate()
        if self.contact_rule:
            self.contact_rule.validate()
        if self.cross_order_buy_quantity_limit_rules:
            for v1 in self.cross_order_buy_quantity_limit_rules:
                 if v1:
                    v1.validate()
        if self.per_order_buy_quantity_limit_rule:
            self.per_order_buy_quantity_limit_rule.validate()
        if self.traveler_rule:
            self.traveler_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ahead_buy_time_point_rule is not None:
            result['AheadBuyTimePointRule'] = self.ahead_buy_time_point_rule.to_map()

        if self.contact_rule is not None:
            result['ContactRule'] = self.contact_rule.to_map()

        result['CrossOrderBuyQuantityLimitRules'] = []
        if self.cross_order_buy_quantity_limit_rules is not None:
            for k1 in self.cross_order_buy_quantity_limit_rules:
                result['CrossOrderBuyQuantityLimitRules'].append(k1.to_map() if k1 else None)

        if self.per_order_buy_quantity_limit_rule is not None:
            result['PerOrderBuyQuantityLimitRule'] = self.per_order_buy_quantity_limit_rule.to_map()

        if self.traveler_rule is not None:
            result['TravelerRule'] = self.traveler_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AheadBuyTimePointRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleAheadBuyTimePointRule()
            self.ahead_buy_time_point_rule = temp_model.from_map(m.get('AheadBuyTimePointRule'))

        if m.get('ContactRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleContactRule()
            self.contact_rule = temp_model.from_map(m.get('ContactRule'))

        self.cross_order_buy_quantity_limit_rules = []
        if m.get('CrossOrderBuyQuantityLimitRules') is not None:
            for k1 in m.get('CrossOrderBuyQuantityLimitRules'):
                temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleCrossOrderBuyQuantityLimitRules()
                self.cross_order_buy_quantity_limit_rules.append(temp_model.from_map(k1))

        if m.get('PerOrderBuyQuantityLimitRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRulePerOrderBuyQuantityLimitRule()
            self.per_order_buy_quantity_limit_rule = temp_model.from_map(m.get('PerOrderBuyQuantityLimitRule'))

        if m.get('TravelerRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRule()
            self.traveler_rule = temp_model.from_map(m.get('TravelerRule'))

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRule(DaraModel):
    def __init__(
        self,
        crowd_limit_rules: List[main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleCrowdLimitRules] = None,
        crowd_quantity_limits: List[main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleCrowdQuantityLimits] = None,
        need_fill_traveler: bool = None,
        traveler_field_rule: main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleTravelerFieldRule = None,
        traveler_fill_dimension: int = None,
        traveler_quantity: int = None,
    ):
        self.crowd_limit_rules = crowd_limit_rules
        self.crowd_quantity_limits = crowd_quantity_limits
        self.need_fill_traveler = need_fill_traveler
        self.traveler_field_rule = traveler_field_rule
        self.traveler_fill_dimension = traveler_fill_dimension
        self.traveler_quantity = traveler_quantity

    def validate(self):
        if self.crowd_limit_rules:
            for v1 in self.crowd_limit_rules:
                 if v1:
                    v1.validate()
        if self.crowd_quantity_limits:
            for v1 in self.crowd_quantity_limits:
                 if v1:
                    v1.validate()
        if self.traveler_field_rule:
            self.traveler_field_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CrowdLimitRules'] = []
        if self.crowd_limit_rules is not None:
            for k1 in self.crowd_limit_rules:
                result['CrowdLimitRules'].append(k1.to_map() if k1 else None)

        result['CrowdQuantityLimits'] = []
        if self.crowd_quantity_limits is not None:
            for k1 in self.crowd_quantity_limits:
                result['CrowdQuantityLimits'].append(k1.to_map() if k1 else None)

        if self.need_fill_traveler is not None:
            result['NeedFillTraveler'] = self.need_fill_traveler

        if self.traveler_field_rule is not None:
            result['TravelerFieldRule'] = self.traveler_field_rule.to_map()

        if self.traveler_fill_dimension is not None:
            result['TravelerFillDimension'] = self.traveler_fill_dimension

        if self.traveler_quantity is not None:
            result['TravelerQuantity'] = self.traveler_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.crowd_limit_rules = []
        if m.get('CrowdLimitRules') is not None:
            for k1 in m.get('CrowdLimitRules'):
                temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleCrowdLimitRules()
                self.crowd_limit_rules.append(temp_model.from_map(k1))

        self.crowd_quantity_limits = []
        if m.get('CrowdQuantityLimits') is not None:
            for k1 in m.get('CrowdQuantityLimits'):
                temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleCrowdQuantityLimits()
                self.crowd_quantity_limits.append(temp_model.from_map(k1))

        if m.get('NeedFillTraveler') is not None:
            self.need_fill_traveler = m.get('NeedFillTraveler')

        if m.get('TravelerFieldRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleTravelerFieldRule()
            self.traveler_field_rule = temp_model.from_map(m.get('TravelerFieldRule'))

        if m.get('TravelerFillDimension') is not None:
            self.traveler_fill_dimension = m.get('TravelerFillDimension')

        if m.get('TravelerQuantity') is not None:
            self.traveler_quantity = m.get('TravelerQuantity')

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleTravelerFieldRule(DaraModel):
    def __init__(
        self,
        birthday: bool = None,
        certificate: bool = None,
        certificate_types: List[int] = None,
        dialing_code: bool = None,
        email: bool = None,
        first_name: bool = None,
        gender: bool = None,
        last_name: bool = None,
        mobile: bool = None,
        name: bool = None,
        nationality: bool = None,
    ):
        self.birthday = birthday
        self.certificate = certificate
        self.certificate_types = certificate_types
        self.dialing_code = dialing_code
        self.email = email
        self.first_name = first_name
        self.gender = gender
        self.last_name = last_name
        self.mobile = mobile
        self.name = name
        self.nationality = nationality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['Birthday'] = self.birthday

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.certificate_types is not None:
            result['CertificateTypes'] = self.certificate_types

        if self.dialing_code is not None:
            result['DialingCode'] = self.dialing_code

        if self.email is not None:
            result['Email'] = self.email

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.name is not None:
            result['Name'] = self.name

        if self.nationality is not None:
            result['Nationality'] = self.nationality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('CertificateTypes') is not None:
            self.certificate_types = m.get('CertificateTypes')

        if m.get('DialingCode') is not None:
            self.dialing_code = m.get('DialingCode')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleCrowdQuantityLimits(DaraModel):
    def __init__(
        self,
        name: str = None,
        quantity: int = None,
    ):
        self.name = name
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRuleTravelerRuleCrowdLimitRules(DaraModel):
    def __init__(
        self,
        age_base_time_type: int = None,
        age_calculate_type: int = None,
        age_max: int = None,
        age_min: int = None,
        name: str = None,
    ):
        self.age_base_time_type = age_base_time_type
        self.age_calculate_type = age_calculate_type
        self.age_max = age_max
        self.age_min = age_min
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.age_base_time_type is not None:
            result['AgeBaseTimeType'] = self.age_base_time_type

        if self.age_calculate_type is not None:
            result['AgeCalculateType'] = self.age_calculate_type

        if self.age_max is not None:
            result['AgeMax'] = self.age_max

        if self.age_min is not None:
            result['AgeMin'] = self.age_min

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgeBaseTimeType') is not None:
            self.age_base_time_type = m.get('AgeBaseTimeType')

        if m.get('AgeCalculateType') is not None:
            self.age_calculate_type = m.get('AgeCalculateType')

        if m.get('AgeMax') is not None:
            self.age_max = m.get('AgeMax')

        if m.get('AgeMin') is not None:
            self.age_min = m.get('AgeMin')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRulePerOrderBuyQuantityLimitRule(DaraModel):
    def __init__(
        self,
        max_buy_quantity: int = None,
        min_buy_quantity: int = None,
    ):
        self.max_buy_quantity = max_buy_quantity
        self.min_buy_quantity = min_buy_quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_buy_quantity is not None:
            result['MaxBuyQuantity'] = self.max_buy_quantity

        if self.min_buy_quantity is not None:
            result['MinBuyQuantity'] = self.min_buy_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxBuyQuantity') is not None:
            self.max_buy_quantity = m.get('MaxBuyQuantity')

        if m.get('MinBuyQuantity') is not None:
            self.min_buy_quantity = m.get('MinBuyQuantity')

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRuleCrossOrderBuyQuantityLimitRules(DaraModel):
    def __init__(
        self,
        limit_day_type: int = None,
        limit_days: int = None,
        limit_period: int = None,
        limit_quantity_type: int = None,
        limit_type: int = None,
        max_buy_quantity: int = None,
    ):
        self.limit_day_type = limit_day_type
        self.limit_days = limit_days
        self.limit_period = limit_period
        self.limit_quantity_type = limit_quantity_type
        self.limit_type = limit_type
        self.max_buy_quantity = max_buy_quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit_day_type is not None:
            result['LimitDayType'] = self.limit_day_type

        if self.limit_days is not None:
            result['LimitDays'] = self.limit_days

        if self.limit_period is not None:
            result['LimitPeriod'] = self.limit_period

        if self.limit_quantity_type is not None:
            result['LimitQuantityType'] = self.limit_quantity_type

        if self.limit_type is not None:
            result['LimitType'] = self.limit_type

        if self.max_buy_quantity is not None:
            result['MaxBuyQuantity'] = self.max_buy_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LimitDayType') is not None:
            self.limit_day_type = m.get('LimitDayType')

        if m.get('LimitDays') is not None:
            self.limit_days = m.get('LimitDays')

        if m.get('LimitPeriod') is not None:
            self.limit_period = m.get('LimitPeriod')

        if m.get('LimitQuantityType') is not None:
            self.limit_quantity_type = m.get('LimitQuantityType')

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        if m.get('MaxBuyQuantity') is not None:
            self.max_buy_quantity = m.get('MaxBuyQuantity')

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRuleContactRule(DaraModel):
    def __init__(
        self,
        contact_field_rule: main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleContactRuleContactFieldRule = None,
    ):
        self.contact_field_rule = contact_field_rule

    def validate(self):
        if self.contact_field_rule:
            self.contact_field_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_field_rule is not None:
            result['ContactFieldRule'] = self.contact_field_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactFieldRule') is not None:
            temp_model = main_models.TicketPageQueryProductResponseBodyDataProductsBuyRuleContactRuleContactFieldRule()
            self.contact_field_rule = temp_model.from_map(m.get('ContactFieldRule'))

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRuleContactRuleContactFieldRule(DaraModel):
    def __init__(
        self,
        certificate: bool = None,
        certificate_types: List[int] = None,
        dialing_code: bool = None,
        email: bool = None,
        first_name: bool = None,
        last_name: bool = None,
        mobile: bool = None,
        name: bool = None,
    ):
        self.certificate = certificate
        self.certificate_types = certificate_types
        self.dialing_code = dialing_code
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.certificate_types is not None:
            result['CertificateTypes'] = self.certificate_types

        if self.dialing_code is not None:
            result['DialingCode'] = self.dialing_code

        if self.email is not None:
            result['Email'] = self.email

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('CertificateTypes') is not None:
            self.certificate_types = m.get('CertificateTypes')

        if m.get('DialingCode') is not None:
            self.dialing_code = m.get('DialingCode')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class TicketPageQueryProductResponseBodyDataProductsBuyRuleAheadBuyTimePointRule(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        fixed_time: str = None,
        offset_day_of_time: str = None,
        offset_unit: int = None,
        offset_value: int = None,
    ):
        self.anchor = anchor
        self.fixed_time = fixed_time
        self.offset_day_of_time = offset_day_of_time
        self.offset_unit = offset_unit
        self.offset_value = offset_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time

        if self.offset_day_of_time is not None:
            result['OffsetDayOfTime'] = self.offset_day_of_time

        if self.offset_unit is not None:
            result['OffsetUnit'] = self.offset_unit

        if self.offset_value is not None:
            result['OffsetValue'] = self.offset_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')

        if m.get('OffsetDayOfTime') is not None:
            self.offset_day_of_time = m.get('OffsetDayOfTime')

        if m.get('OffsetUnit') is not None:
            self.offset_unit = m.get('OffsetUnit')

        if m.get('OffsetValue') is not None:
            self.offset_value = m.get('OffsetValue')

        return self

