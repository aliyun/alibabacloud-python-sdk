# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreatePickUpWaybillPreQueryRequest(DaraModel):
    def __init__(
        self,
        consignee_info: main_models.CreatePickUpWaybillPreQueryRequestConsigneeInfo = None,
        cp_code: str = None,
        order_channels: str = None,
        outer_order_code: str = None,
        pre_weight: str = None,
        sender_info: main_models.CreatePickUpWaybillPreQueryRequestSenderInfo = None,
    ):
        # The recipient information.
        # 
        # This parameter is required.
        self.consignee_info = consignee_info
        # The courier company code. If not specified, the system automatically assigns a courier company.
        self.cp_code = cp_code
        # The external channel source identifier. The value cannot contain underscores. The value is agreed upon with the system during integration.
        # 
        # This parameter is required.
        self.order_channels = order_channels
        # The order number in the caller\\"s system.
        self.outer_order_code = outer_order_code
        # The estimated weight, in grams.
        # 
        # > If you want to query the estimated price, this parameter is required.
        self.pre_weight = pre_weight
        # The sender information.
        # 
        # This parameter is required.
        self.sender_info = sender_info

    def validate(self):
        if self.consignee_info:
            self.consignee_info.validate()
        if self.sender_info:
            self.sender_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consignee_info is not None:
            result['ConsigneeInfo'] = self.consignee_info.to_map()

        if self.cp_code is not None:
            result['CpCode'] = self.cp_code

        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels

        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code

        if self.pre_weight is not None:
            result['PreWeight'] = self.pre_weight

        if self.sender_info is not None:
            result['SenderInfo'] = self.sender_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsigneeInfo') is not None:
            temp_model = main_models.CreatePickUpWaybillPreQueryRequestConsigneeInfo()
            self.consignee_info = temp_model.from_map(m.get('ConsigneeInfo'))

        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')

        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')

        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')

        if m.get('PreWeight') is not None:
            self.pre_weight = m.get('PreWeight')

        if m.get('SenderInfo') is not None:
            temp_model = main_models.CreatePickUpWaybillPreQueryRequestSenderInfo()
            self.sender_info = temp_model.from_map(m.get('SenderInfo'))

        return self

class CreatePickUpWaybillPreQueryRequestSenderInfo(DaraModel):
    def __init__(
        self,
        address_info: main_models.CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo = None,
        mobile: str = None,
        name: str = None,
    ):
        # The address information of the sender.
        self.address_info = address_info
        # The mobile phone number of the sender.
        # 
        # This parameter is required.
        self.mobile = mobile
        # The name of the sender.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.address_info:
            self.address_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info.to_map()

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressInfo') is not None:
            temp_model = main_models.CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo()
            self.address_info = temp_model.from_map(m.get('AddressInfo'))

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo(DaraModel):
    def __init__(
        self,
        address_detail: str = None,
        area_name: str = None,
        city_name: str = None,
        province_name: str = None,
        town_name: str = None,
    ):
        # The detailed address of the sender.
        self.address_detail = address_detail
        # The district where the sender is located.
        self.area_name = area_name
        # The city where the sender is located.
        self.city_name = city_name
        # The province where the sender is located.
        self.province_name = province_name
        # The street where the sender is located.
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail

        if self.area_name is not None:
            result['AreaName'] = self.area_name

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.province_name is not None:
            result['ProvinceName'] = self.province_name

        if self.town_name is not None:
            result['TownName'] = self.town_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')

        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')

        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')

        return self

class CreatePickUpWaybillPreQueryRequestConsigneeInfo(DaraModel):
    def __init__(
        self,
        address_info: main_models.CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo = None,
        mobile: str = None,
        name: str = None,
    ):
        # The address information of the recipient.
        self.address_info = address_info
        # The mobile phone number of the recipient.
        # 
        # This parameter is required.
        self.mobile = mobile
        # The name of the recipient.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.address_info:
            self.address_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info.to_map()

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressInfo') is not None:
            temp_model = main_models.CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo()
            self.address_info = temp_model.from_map(m.get('AddressInfo'))

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo(DaraModel):
    def __init__(
        self,
        address_detail: str = None,
        area_name: str = None,
        city_name: str = None,
        province_name: str = None,
        town_name: str = None,
    ):
        # The detailed address of the recipient.
        self.address_detail = address_detail
        # The district where the recipient is located.
        self.area_name = area_name
        # The city where the recipient is located.
        self.city_name = city_name
        # The province where the recipient is located.
        self.province_name = province_name
        # The street where the recipient is located.
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail

        if self.area_name is not None:
            result['AreaName'] = self.area_name

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.province_name is not None:
            result['ProvinceName'] = self.province_name

        if self.town_name is not None:
            result['TownName'] = self.town_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')

        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')

        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')

        return self

