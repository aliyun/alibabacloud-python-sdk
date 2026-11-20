# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreatePickUpWaybillRequest(DaraModel):
    def __init__(
        self,
        appoint_got_end_time: str = None,
        appoint_got_start_time: str = None,
        biz_type: int = None,
        consignee_address: main_models.CreatePickUpWaybillRequestConsigneeAddress = None,
        consignee_mobile: str = None,
        consignee_name: str = None,
        consignee_phone: str = None,
        cp_code: str = None,
        goods_infos: List[main_models.CreatePickUpWaybillRequestGoodsInfos] = None,
        order_channels: str = None,
        outer_order_code: str = None,
        remark: str = None,
        send_address: main_models.CreatePickUpWaybillRequestSendAddress = None,
        send_mobile: str = None,
        send_name: str = None,
        send_phone: str = None,
    ):
        # The end time of the scheduled door-to-door pickup, in the YYYY-MM-DD HH:mm:ss format. To obtain the value of **AppointGotEndTime**, obtain the **EndTime** value from **AppointTimes** in the **CpTimeSelectList** response parameter of the [CreatePickUpWaybillPreQuery](https://api.aliyun.com/document/Dyplsapi/2017-05-25/CreatePickUpWaybillPreQuery) operation.
        # > Required when **bizType** is set to **1**.
        self.appoint_got_end_time = appoint_got_end_time
        # The start time of the scheduled door-to-door pickup, in the YYYY-MM-DD HH:mm:ss format. To obtain the value of **AppointGotStartTime**, obtain the **StartTime** value from **AppointTimes** in the **CpTimeSelectList** response parameter of the [CreatePickUpWaybillPreQuery](https://api.aliyun.com/document/Dyplsapi/2017-05-25/CreatePickUpWaybillPreQuery) operation.
        # 
        # > Required when **bizType** is set to **1**.
        self.appoint_got_start_time = appoint_got_start_time
        # The delivery mode. Valid values:
        # 
        # - **0**: real-time order (default)
        # - **1**: scheduled order
        self.biz_type = biz_type
        # The address of the recipient.
        # 
        # This parameter is required.
        self.consignee_address = consignee_address
        # The mobile phone number of the recipient.
        # 
        # > You must specify either ConsigneeMobile or ConsigneePhone.
        self.consignee_mobile = consignee_mobile
        # The name of the recipient.
        # 
        # This parameter is required.
        self.consignee_name = consignee_name
        # The landline phone number of the recipient.
        # > You must specify either ConsigneeMobile or ConsigneePhone.
        self.consignee_phone = consignee_phone
        # The express delivery company code.
        self.cp_code = cp_code
        # The list of goods.
        self.goods_infos = goods_infos
        # The external channel source.
        # 
        # This parameter is required.
        self.order_channels = order_channels
        # The external order ID.
        # 
        # This parameter is required.
        self.outer_order_code = outer_order_code
        # The remark. The remark content printed on the waybill.
        self.remark = remark
        # The address of the sender.
        # 
        # This parameter is required.
        self.send_address = send_address
        # The mobile phone number of the sender.
        # 
        # > You must specify either SendMobile or SendPhone.
        self.send_mobile = send_mobile
        # The name of the sender.
        # 
        # This parameter is required.
        self.send_name = send_name
        # The landline phone number of the sender.
        # > You must specify either SendMobile or SendPhone.
        self.send_phone = send_phone

    def validate(self):
        if self.consignee_address:
            self.consignee_address.validate()
        if self.goods_infos:
            for v1 in self.goods_infos:
                 if v1:
                    v1.validate()
        if self.send_address:
            self.send_address.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appoint_got_end_time is not None:
            result['AppointGotEndTime'] = self.appoint_got_end_time

        if self.appoint_got_start_time is not None:
            result['AppointGotStartTime'] = self.appoint_got_start_time

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.consignee_address is not None:
            result['ConsigneeAddress'] = self.consignee_address.to_map()

        if self.consignee_mobile is not None:
            result['ConsigneeMobile'] = self.consignee_mobile

        if self.consignee_name is not None:
            result['ConsigneeName'] = self.consignee_name

        if self.consignee_phone is not None:
            result['ConsigneePhone'] = self.consignee_phone

        if self.cp_code is not None:
            result['CpCode'] = self.cp_code

        result['GoodsInfos'] = []
        if self.goods_infos is not None:
            for k1 in self.goods_infos:
                result['GoodsInfos'].append(k1.to_map() if k1 else None)

        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels

        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.send_address is not None:
            result['SendAddress'] = self.send_address.to_map()

        if self.send_mobile is not None:
            result['SendMobile'] = self.send_mobile

        if self.send_name is not None:
            result['SendName'] = self.send_name

        if self.send_phone is not None:
            result['SendPhone'] = self.send_phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppointGotEndTime') is not None:
            self.appoint_got_end_time = m.get('AppointGotEndTime')

        if m.get('AppointGotStartTime') is not None:
            self.appoint_got_start_time = m.get('AppointGotStartTime')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ConsigneeAddress') is not None:
            temp_model = main_models.CreatePickUpWaybillRequestConsigneeAddress()
            self.consignee_address = temp_model.from_map(m.get('ConsigneeAddress'))

        if m.get('ConsigneeMobile') is not None:
            self.consignee_mobile = m.get('ConsigneeMobile')

        if m.get('ConsigneeName') is not None:
            self.consignee_name = m.get('ConsigneeName')

        if m.get('ConsigneePhone') is not None:
            self.consignee_phone = m.get('ConsigneePhone')

        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')

        self.goods_infos = []
        if m.get('GoodsInfos') is not None:
            for k1 in m.get('GoodsInfos'):
                temp_model = main_models.CreatePickUpWaybillRequestGoodsInfos()
                self.goods_infos.append(temp_model.from_map(k1))

        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')

        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SendAddress') is not None:
            temp_model = main_models.CreatePickUpWaybillRequestSendAddress()
            self.send_address = temp_model.from_map(m.get('SendAddress'))

        if m.get('SendMobile') is not None:
            self.send_mobile = m.get('SendMobile')

        if m.get('SendName') is not None:
            self.send_name = m.get('SendName')

        if m.get('SendPhone') is not None:
            self.send_phone = m.get('SendPhone')

        return self

class CreatePickUpWaybillRequestSendAddress(DaraModel):
    def __init__(
        self,
        address_detail: str = None,
        area_name: str = None,
        city_name: str = None,
        province_name: str = None,
        town_name: str = None,
    ):
        # The detailed address.
        # 
        # This parameter is required.
        self.address_detail = address_detail
        # The district.
        # 
        # This parameter is required.
        self.area_name = area_name
        # The city.
        # 
        # This parameter is required.
        self.city_name = city_name
        # The province.
        # 
        # This parameter is required.
        self.province_name = province_name
        # The street.
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

class CreatePickUpWaybillRequestGoodsInfos(DaraModel):
    def __init__(
        self,
        name: str = None,
        quantity: str = None,
        weight: str = None,
    ):
        # The name of the item.
        self.name = name
        # The quantity.
        self.quantity = quantity
        # The weight. Unit: grams.
        self.weight = weight

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

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreatePickUpWaybillRequestConsigneeAddress(DaraModel):
    def __init__(
        self,
        address_detail: str = None,
        area_name: str = None,
        city_name: str = None,
        province_name: str = None,
        town_name: str = None,
    ):
        # The detailed address.
        # 
        # This parameter is required.
        self.address_detail = address_detail
        # The district.
        # 
        # This parameter is required.
        self.area_name = area_name
        # The city.
        # 
        # This parameter is required.
        self.city_name = city_name
        # The province.
        # 
        # This parameter is required.
        self.province_name = province_name
        # The street.
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

