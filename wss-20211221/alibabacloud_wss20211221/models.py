# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CreateMultiOrderRequestOrderItemsComponents(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateMultiOrderRequestOrderItems(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        buy_change: bool = None,
        components: List[CreateMultiOrderRequestOrderItemsComponents] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.amount = amount
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.buy_change = buy_change
        self.components = components
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.resource_ids = resource_ids
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.buy_change is not None:
            result['BuyChange'] = self.buy_change
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BuyChange') is not None:
            self.buy_change = m.get('BuyChange')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = CreateMultiOrderRequestOrderItemsComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateMultiOrderRequest(TeaModel):
    def __init__(
        self,
        order_items: List[CreateMultiOrderRequestOrderItems] = None,
        order_type: str = None,
        properties: Dict[str, str] = None,
        reseller_owner_uid: int = None,
    ):
        self.order_items = order_items
        self.order_type = order_type
        self.properties = properties
        self.reseller_owner_uid = reseller_owner_uid

    def validate(self):
        if self.order_items:
            for k in self.order_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderItems'] = []
        if self.order_items is not None:
            for k in self.order_items:
                result['OrderItems'].append(k.to_map() if k else None)
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_items = []
        if m.get('OrderItems') is not None:
            for k in m.get('OrderItems'):
                temp_model = CreateMultiOrderRequestOrderItems()
                self.order_items.append(temp_model.from_map(k))
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')
        return self


class CreateMultiOrderShrinkRequestOrderItemsComponents(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateMultiOrderShrinkRequestOrderItems(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        buy_change: bool = None,
        components: List[CreateMultiOrderShrinkRequestOrderItemsComponents] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.amount = amount
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.buy_change = buy_change
        self.components = components
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.resource_ids = resource_ids
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.buy_change is not None:
            result['BuyChange'] = self.buy_change
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BuyChange') is not None:
            self.buy_change = m.get('BuyChange')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = CreateMultiOrderShrinkRequestOrderItemsComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateMultiOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        order_items: List[CreateMultiOrderShrinkRequestOrderItems] = None,
        order_type: str = None,
        properties_shrink: str = None,
        reseller_owner_uid: int = None,
    ):
        self.order_items = order_items
        self.order_type = order_type
        self.properties_shrink = properties_shrink
        self.reseller_owner_uid = reseller_owner_uid

    def validate(self):
        if self.order_items:
            for k in self.order_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderItems'] = []
        if self.order_items is not None:
            for k in self.order_items:
                result['OrderItems'].append(k.to_map() if k else None)
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink
        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_items = []
        if m.get('OrderItems') is not None:
            for k in m.get('OrderItems'):
                temp_model = CreateMultiOrderShrinkRequestOrderItems()
                self.order_items.append(temp_model.from_map(k))
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')
        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')
        return self


class CreateMultiOrderResponseBody(TeaModel):
    def __init__(
        self,
        order_ids: List[int] = None,
        request_id: str = None,
    ):
        self.order_ids = order_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMultiOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMultiOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMultiOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeliveryAddressResponseBodyAddressesArea(TeaModel):
    def __init__(
        self,
        area_id: int = None,
        area_name: str = None,
    ):
        self.area_id = area_id
        self.area_name = area_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        return self


class DescribeDeliveryAddressResponseBodyAddressesCity(TeaModel):
    def __init__(
        self,
        city_id: int = None,
        city_name: str = None,
    ):
        self.city_id = city_id
        self.city_name = city_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_id is not None:
            result['CityId'] = self.city_id
        if self.city_name is not None:
            result['CityName'] = self.city_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        return self


class DescribeDeliveryAddressResponseBodyAddressesProvince(TeaModel):
    def __init__(
        self,
        province_id: int = None,
        province_name: str = None,
    ):
        self.province_id = province_id
        self.province_name = province_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        return self


class DescribeDeliveryAddressResponseBodyAddressesTown(TeaModel):
    def __init__(
        self,
        town_id: int = None,
        town_name: str = None,
    ):
        self.town_id = town_id
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.town_id is not None:
            result['TownId'] = self.town_id
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TownId') is not None:
            self.town_id = m.get('TownId')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class DescribeDeliveryAddressResponseBodyAddresses(TeaModel):
    def __init__(
        self,
        area: DescribeDeliveryAddressResponseBodyAddressesArea = None,
        city: DescribeDeliveryAddressResponseBodyAddressesCity = None,
        contacts: str = None,
        default_address: bool = None,
        detail: str = None,
        mobile: str = None,
        postal_code: str = None,
        province: DescribeDeliveryAddressResponseBodyAddressesProvince = None,
        town: DescribeDeliveryAddressResponseBodyAddressesTown = None,
    ):
        self.area = area
        self.city = city
        self.contacts = contacts
        self.default_address = default_address
        self.detail = detail
        self.mobile = mobile
        self.postal_code = postal_code
        self.province = province
        self.town = town

    def validate(self):
        if self.area:
            self.area.validate()
        if self.city:
            self.city.validate()
        if self.province:
            self.province.validate()
        if self.town:
            self.town.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area.to_map()
        if self.city is not None:
            result['City'] = self.city.to_map()
        if self.contacts is not None:
            result['Contacts'] = self.contacts
        if self.default_address is not None:
            result['DefaultAddress'] = self.default_address
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province.to_map()
        if self.town is not None:
            result['Town'] = self.town.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            temp_model = DescribeDeliveryAddressResponseBodyAddressesArea()
            self.area = temp_model.from_map(m['Area'])
        if m.get('City') is not None:
            temp_model = DescribeDeliveryAddressResponseBodyAddressesCity()
            self.city = temp_model.from_map(m['City'])
        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')
        if m.get('DefaultAddress') is not None:
            self.default_address = m.get('DefaultAddress')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            temp_model = DescribeDeliveryAddressResponseBodyAddressesProvince()
            self.province = temp_model.from_map(m['Province'])
        if m.get('Town') is not None:
            temp_model = DescribeDeliveryAddressResponseBodyAddressesTown()
            self.town = temp_model.from_map(m['Town'])
        return self


class DescribeDeliveryAddressResponseBody(TeaModel):
    def __init__(
        self,
        addresses: List[DescribeDeliveryAddressResponseBodyAddresses] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.addresses = addresses
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = DescribeDeliveryAddressResponseBodyAddresses()
                self.addresses.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeliveryAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeliveryAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDeliveryAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiPriceRequestOrderItemsComponents(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeMultiPriceRequestOrderItems(TeaModel):
    def __init__(
        self,
        amount: int = None,
        components: List[DescribeMultiPriceRequestOrderItemsComponents] = None,
        instance_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.amount = amount
        self.components = components
        self.instance_ids = instance_ids
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = DescribeMultiPriceRequestOrderItemsComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeMultiPriceRequest(TeaModel):
    def __init__(
        self,
        order_items: List[DescribeMultiPriceRequestOrderItems] = None,
        order_type: str = None,
        package_code: str = None,
        reseller_owner_uid: int = None,
    ):
        self.order_items = order_items
        self.order_type = order_type
        self.package_code = package_code
        self.reseller_owner_uid = reseller_owner_uid

    def validate(self):
        if self.order_items:
            for k in self.order_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderItems'] = []
        if self.order_items is not None:
            for k in self.order_items:
                result['OrderItems'].append(k.to_map() if k else None)
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.package_code is not None:
            result['PackageCode'] = self.package_code
        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_items = []
        if m.get('OrderItems') is not None:
            for k in m.get('OrderItems'):
                temp_model = DescribeMultiPriceRequestOrderItems()
                self.order_items.append(temp_model.from_map(k))
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PackageCode') is not None:
            self.package_code = m.get('PackageCode')
        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')
        return self


class DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsModuleDetails(TeaModel):
    def __init__(
        self,
        discount_price: float = None,
        module_code: str = None,
        module_name: str = None,
        module_value: str = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.discount_price = discount_price
        self.module_code = module_code
        self.module_name = module_name
        self.module_value = module_value
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_value is not None:
            result['ModuleValue'] = self.module_value
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleValue') is not None:
            self.module_value = m.get('ModuleValue')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsPriceDetail(TeaModel):
    def __init__(
        self,
        discount_price: float = None,
        original_price: float = None,
        resource_type: str = None,
        trade_price: float = None,
    ):
        self.discount_price = discount_price
        self.original_price = original_price
        self.resource_type = resource_type
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeMultiPriceResponseBodyPriceInfoPricePriceDetails(TeaModel):
    def __init__(
        self,
        module_details: List[DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsModuleDetails] = None,
        order_item: int = None,
        price_detail: DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsPriceDetail = None,
    ):
        self.module_details = module_details
        self.order_item = order_item
        self.price_detail = price_detail

    def validate(self):
        if self.module_details:
            for k in self.module_details:
                if k:
                    k.validate()
        if self.price_detail:
            self.price_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModuleDetails'] = []
        if self.module_details is not None:
            for k in self.module_details:
                result['ModuleDetails'].append(k.to_map() if k else None)
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.price_detail is not None:
            result['PriceDetail'] = self.price_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_details = []
        if m.get('ModuleDetails') is not None:
            for k in m.get('ModuleDetails'):
                temp_model = DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsModuleDetails()
                self.module_details.append(temp_model.from_map(k))
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PriceDetail') is not None:
            temp_model = DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsPriceDetail()
            self.price_detail = temp_model.from_map(m['PriceDetail'])
        return self


class DescribeMultiPriceResponseBodyPriceInfoPricePromotions(TeaModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        self.option_code = option_code
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class DescribeMultiPriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        price_details: List[DescribeMultiPriceResponseBodyPriceInfoPricePriceDetails] = None,
        promotions: List[DescribeMultiPriceResponseBodyPriceInfoPricePromotions] = None,
        refund_instance_id_price_map: Dict[str, float] = None,
        refund_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.price_details = price_details
        self.promotions = promotions
        self.refund_instance_id_price_map = refund_instance_id_price_map
        self.refund_price = refund_price
        self.trade_price = trade_price

    def validate(self):
        if self.price_details:
            for k in self.price_details:
                if k:
                    k.validate()
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['PriceDetails'] = []
        if self.price_details is not None:
            for k in self.price_details:
                result['PriceDetails'].append(k.to_map() if k else None)
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.refund_instance_id_price_map is not None:
            result['RefundInstanceIdPriceMap'] = self.refund_instance_id_price_map
        if self.refund_price is not None:
            result['RefundPrice'] = self.refund_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.price_details = []
        if m.get('PriceDetails') is not None:
            for k in m.get('PriceDetails'):
                temp_model = DescribeMultiPriceResponseBodyPriceInfoPricePriceDetails()
                self.price_details.append(temp_model.from_map(k))
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = DescribeMultiPriceResponseBodyPriceInfoPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('RefundInstanceIdPriceMap') is not None:
            self.refund_instance_id_price_map = m.get('RefundInstanceIdPriceMap')
        if m.get('RefundPrice') is not None:
            self.refund_price = m.get('RefundPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeMultiPriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeMultiPriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        price: DescribeMultiPriceResponseBodyPriceInfoPrice = None,
        rules: List[DescribeMultiPriceResponseBodyPriceInfoRules] = None,
    ):
        self.price = price
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = DescribeMultiPriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeMultiPriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeMultiPriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: DescribeMultiPriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        self.price_info = price_info
        self.request_id = request_id

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = DescribeMultiPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMultiPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMultiPriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMultiPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackageDeductionsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_ids: List[str] = None,
        package_ids: List[str] = None,
        page_num: int = None,
        page_size: int = None,
        resource_type: str = None,
        resource_types: List[str] = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance_ids = instance_ids
        self.package_ids = package_ids
        self.page_num = page_num
        self.page_size = page_size
        self.resource_type = resource_type
        self.resource_types = resource_types
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.package_ids is not None:
            result['PackageIds'] = self.package_ids
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PackageIds') is not None:
            self.package_ids = m.get('PackageIds')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePackageDeductionsResponseBodyDeductions(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_type: str = None,
        end_time: str = None,
        group_resource_type: str = None,
        instance_id: str = None,
        instance_state: str = None,
        instance_type: str = None,
        memory: int = None,
        os_type: str = None,
        region_id: str = None,
        resource_type: str = None,
        session_id: str = None,
        sta_time: str = None,
        used_core_time: float = None,
        used_time: int = None,
        used_time_with_scale: int = None,
    ):
        self.cpu = cpu
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_type = desktop_type
        self.end_time = end_time
        self.group_resource_type = group_resource_type
        self.instance_id = instance_id
        self.instance_state = instance_state
        self.instance_type = instance_type
        self.memory = memory
        self.os_type = os_type
        self.region_id = region_id
        self.resource_type = resource_type
        self.session_id = session_id
        self.sta_time = sta_time
        self.used_core_time = used_core_time
        self.used_time = used_time
        self.used_time_with_scale = used_time_with_scale

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_resource_type is not None:
            result['GroupResourceType'] = self.group_resource_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_state is not None:
            result['InstanceState'] = self.instance_state
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sta_time is not None:
            result['StaTime'] = self.sta_time
        if self.used_core_time is not None:
            result['UsedCoreTime'] = self.used_core_time
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.used_time_with_scale is not None:
            result['UsedTimeWithScale'] = self.used_time_with_scale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupResourceType') is not None:
            self.group_resource_type = m.get('GroupResourceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceState') is not None:
            self.instance_state = m.get('InstanceState')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StaTime') is not None:
            self.sta_time = m.get('StaTime')
        if m.get('UsedCoreTime') is not None:
            self.used_core_time = m.get('UsedCoreTime')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('UsedTimeWithScale') is not None:
            self.used_time_with_scale = m.get('UsedTimeWithScale')
        return self


class DescribePackageDeductionsResponseBody(TeaModel):
    def __init__(
        self,
        deductions: List[DescribePackageDeductionsResponseBodyDeductions] = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_used_core_time: float = None,
        total_used_time: int = None,
    ):
        self.deductions = deductions
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_used_core_time = total_used_core_time
        self.total_used_time = total_used_time

    def validate(self):
        if self.deductions:
            for k in self.deductions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Deductions'] = []
        if self.deductions is not None:
            for k in self.deductions:
                result['Deductions'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_used_core_time is not None:
            result['TotalUsedCoreTime'] = self.total_used_core_time
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deductions = []
        if m.get('Deductions') is not None:
            for k in m.get('Deductions'):
                temp_model = DescribePackageDeductionsResponseBodyDeductions()
                self.deductions.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalUsedCoreTime') is not None:
            self.total_used_core_time = m.get('TotalUsedCoreTime')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        return self


class DescribePackageDeductionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePackageDeductionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePackageDeductionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstancePropertiesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_ids: List[str] = None,
        key: str = None,
        resource_type: str = None,
        value: str = None,
    ):
        self.instance_id = instance_id
        self.instance_ids = instance_ids
        self.key = key
        # This parameter is required.
        self.resource_type = resource_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyInstancePropertiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstancePropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstancePropertiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstancePropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


