# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class CommodityValue(DaraModel):
    def __init__(
        self,
        result: main_models.CommodityValueResult = None,
    ):
        # The result model.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = main_models.CommodityValueResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CommodityValueResult(DaraModel):
    def __init__(
        self,
        order: main_models.CommodityValueResultOrder = None,
        inquiry_type: str = None,
        sub_orders: main_models.CommodityValueResultSubOrders = None,
        coupons: List[main_models.CommodityValueResultCoupons] = None,
    ):
        # The information about the order.
        self.order = order
        # The RFQ type. Valid values:
        # 
        # 1.  Buy: price inquiry for new resources.
        # 2.  ModificationBuy: price inquiry for resource configuration changes.
        self.inquiry_type = inquiry_type
        # The order sub-items.
        self.sub_orders = sub_orders
        # The coupons.
        self.coupons = coupons

    def validate(self):
        if self.order:
            self.order.validate()
        if self.sub_orders:
            self.sub_orders.validate()
        if self.coupons:
            for v1 in self.coupons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order.to_map()

        if self.inquiry_type is not None:
            result['InquiryType'] = self.inquiry_type

        if self.sub_orders is not None:
            result['SubOrders'] = self.sub_orders.to_map()

        result['Coupons'] = []
        if self.coupons is not None:
            for k1 in self.coupons:
                result['Coupons'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = main_models.CommodityValueResultOrder()
            self.order = temp_model.from_map(m.get('Order'))

        if m.get('InquiryType') is not None:
            self.inquiry_type = m.get('InquiryType')

        if m.get('SubOrders') is not None:
            temp_model = main_models.CommodityValueResultSubOrders()
            self.sub_orders = temp_model.from_map(m.get('SubOrders'))

        self.coupons = []
        if m.get('Coupons') is not None:
            for k1 in m.get('Coupons'):
                temp_model = main_models.CommodityValueResultCoupons()
                self.coupons.append(temp_model.from_map(k1))

        return self

class CommodityValueResultCoupons(DaraModel):
    def __init__(
        self,
        can_prom_fee: float = None,
        coupon_desc: str = None,
        coupon_name: str = None,
        coupon_option_no: str = None,
        selected: bool = None,
    ):
        # The payable amount.
        self.can_prom_fee = can_prom_fee
        # The description of the coupon.
        self.coupon_desc = coupon_desc
        # The name of the coupon.
        self.coupon_name = coupon_name
        # The coupon ID.
        self.coupon_option_no = coupon_option_no
        # Indicates whether the coupon is selected.
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee

        if self.coupon_desc is not None:
            result['CouponDesc'] = self.coupon_desc

        if self.coupon_name is not None:
            result['CouponName'] = self.coupon_name

        if self.coupon_option_no is not None:
            result['CouponOptionNo'] = self.coupon_option_no

        if self.selected is not None:
            result['Selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')

        if m.get('CouponDesc') is not None:
            self.coupon_desc = m.get('CouponDesc')

        if m.get('CouponName') is not None:
            self.coupon_name = m.get('CouponName')

        if m.get('CouponOptionNo') is not None:
            self.coupon_option_no = m.get('CouponOptionNo')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        return self

class CommodityValueResultSubOrders(DaraModel):
    def __init__(
        self,
        sub_order: List[main_models.CommodityValueResultSubOrdersSubOrder] = None,
    ):
        # The order sub-item.
        self.sub_order = sub_order

    def validate(self):
        if self.sub_order:
            for v1 in self.sub_order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubOrder'] = []
        if self.sub_order is not None:
            for k1 in self.sub_order:
                result['SubOrder'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_order = []
        if m.get('SubOrder') is not None:
            for k1 in m.get('SubOrder'):
                temp_model = main_models.CommodityValueResultSubOrdersSubOrder()
                self.sub_order.append(temp_model.from_map(k1))

        return self

class CommodityValueResultSubOrdersSubOrder(DaraModel):
    def __init__(
        self,
        module_instance: List[main_models.CommodityValueResultSubOrdersSubOrderModuleInstance] = None,
    ):
        # The information about the module (instance).
        self.module_instance = module_instance

    def validate(self):
        if self.module_instance:
            for v1 in self.module_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModuleInstance'] = []
        if self.module_instance is not None:
            for k1 in self.module_instance:
                result['ModuleInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_instance = []
        if m.get('ModuleInstance') is not None:
            for k1 in m.get('ModuleInstance'):
                temp_model = main_models.CommodityValueResultSubOrdersSubOrderModuleInstance()
                self.module_instance.append(temp_model.from_map(k1))

        return self

class CommodityValueResultSubOrdersSubOrderModuleInstance(DaraModel):
    def __init__(
        self,
        module_id: int = None,
        module_name: str = None,
        module_code: str = None,
        total_product_fee: float = None,
        discount_fee: float = None,
        pay_fee: float = None,
        price_unit: str = None,
        is_pricing_module: bool = None,
        need_order_pay: bool = None,
        price_type: str = None,
        module_attrs: List[main_models.CommodityValueResultSubOrdersSubOrderModuleInstanceModuleAttrs] = None,
        module_name_en: str = None,
        price_unit_en: str = None,
    ):
        # The module ID.
        self.module_id = module_id
        # The module name.
        self.module_name = module_name
        # The module code.
        self.module_code = module_code
        # The original price (RMB).
        self.total_product_fee = total_product_fee
        # The discount amount (RMB).
        self.discount_fee = discount_fee
        # The amount actually paid (RMB).
        self.pay_fee = pay_fee
        # The unit of the price.
        self.price_unit = price_unit
        # Indicates whether the item is billed.
        self.is_pricing_module = is_pricing_module
        # Indicates whether the order is paid.
        self.need_order_pay = need_order_pay
        # The pricing type.
        self.price_type = price_type
        # The module attributes.
        self.module_attrs = module_attrs
        # Module English name.
        self.module_name_en = module_name_en
        # Price Unit English Name
        self.price_unit_en = price_unit_en

    def validate(self):
        if self.module_attrs:
            for v1 in self.module_attrs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.total_product_fee is not None:
            result['TotalProductFee'] = self.total_product_fee

        if self.discount_fee is not None:
            result['DiscountFee'] = self.discount_fee

        if self.pay_fee is not None:
            result['PayFee'] = self.pay_fee

        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit

        if self.is_pricing_module is not None:
            result['IsPricingModule'] = self.is_pricing_module

        if self.need_order_pay is not None:
            result['NeedOrderPay'] = self.need_order_pay

        if self.price_type is not None:
            result['PriceType'] = self.price_type

        result['ModuleAttrs'] = []
        if self.module_attrs is not None:
            for k1 in self.module_attrs:
                result['ModuleAttrs'].append(k1.to_map() if k1 else None)

        if self.module_name_en is not None:
            result['ModuleNameEn'] = self.module_name_en

        if self.price_unit_en is not None:
            result['PriceUnitEn'] = self.price_unit_en

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('TotalProductFee') is not None:
            self.total_product_fee = m.get('TotalProductFee')

        if m.get('DiscountFee') is not None:
            self.discount_fee = m.get('DiscountFee')

        if m.get('PayFee') is not None:
            self.pay_fee = m.get('PayFee')

        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')

        if m.get('IsPricingModule') is not None:
            self.is_pricing_module = m.get('IsPricingModule')

        if m.get('NeedOrderPay') is not None:
            self.need_order_pay = m.get('NeedOrderPay')

        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')

        self.module_attrs = []
        if m.get('ModuleAttrs') is not None:
            for k1 in m.get('ModuleAttrs'):
                temp_model = main_models.CommodityValueResultSubOrdersSubOrderModuleInstanceModuleAttrs()
                self.module_attrs.append(temp_model.from_map(k1))

        if m.get('ModuleNameEn') is not None:
            self.module_name_en = m.get('ModuleNameEn')

        if m.get('PriceUnitEn') is not None:
            self.price_unit_en = m.get('PriceUnitEn')

        return self

class CommodityValueResultSubOrdersSubOrderModuleInstanceModuleAttrs(DaraModel):
    def __init__(
        self,
        type: int = None,
        name: str = None,
        code: str = None,
        value: str = None,
        unit: str = None,
    ):
        # The type of the attribute. Valid values:
        # 
        # 1.  1: product
        # 2.  2\\. specifications
        # 3.  3: module
        # 4.  4: external parameters (backup)
        self.type = type
        # The attribute name.
        self.name = name
        # The attribute code.
        self.code = code
        # The attribute value.
        self.value = value
        # The unit of the value.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.name is not None:
            result['Name'] = self.name

        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self



class CommodityValueResultOrder(DaraModel):
    def __init__(
        self,
        currency: str = None,
        trade_amount: str = None,
        discount_amount: str = None,
        original_amount: str = None,
    ):
        # The code of the native currency.
        self.currency = currency
        # Amount after the discount.
        self.trade_amount = trade_amount
        # The discount amount.
        self.discount_amount = discount_amount
        # Amount before the discount.
        self.original_amount = original_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        return self

