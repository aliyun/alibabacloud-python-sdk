# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class QueryExportDomainExpireSnatchsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryExportDomainExpireSnatchsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryExportDomainExpireSnatchsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryExportDomainExpireSnatchsResponseBodyData(DaraModel):
    def __init__(
        self,
        auction_end_time: str = None,
        auction_remaining_seconds: int = None,
        baidu_anti_link: int = None,
        baidu_ex_link: int = None,
        baidu_index: int = None,
        baidu_weight: int = None,
        book_end_time: str = None,
        book_remaining_seconds: int = None,
        booked_num: int = None,
        booked_partners: str = None,
        constitute: str = None,
        currency_type: str = None,
        delivery_time: str = None,
        domain_id: str = None,
        domain_len: int = None,
        domain_name: str = None,
        domain_type: str = None,
        end_date: str = None,
        expire_date: str = None,
        extend: str = None,
        freeze_amount: float = None,
        icp_number: str = None,
        icp_status: bool = None,
        introduction: str = None,
        is_premium: bool = None,
        partner_types: str = None,
        price: float = None,
        product_id: str = None,
        publish_time: str = None,
        reg_date: str = None,
        registrar: str = None,
        renew_price: float = None,
        reserved: bool = None,
        rmb_price: float = None,
        s_360weight: int = None,
        seo_attributes: str = None,
        short_name: str = None,
        snatch_no: str = None,
        snatch_type_desc: str = None,
        sougou_anti_link: int = None,
        sougou_index: int = None,
        sougou_weight: int = None,
        suffix: str = None,
        weight: int = None,
    ):
        self.auction_end_time = auction_end_time
        self.auction_remaining_seconds = auction_remaining_seconds
        self.baidu_anti_link = baidu_anti_link
        self.baidu_ex_link = baidu_ex_link
        self.baidu_index = baidu_index
        self.baidu_weight = baidu_weight
        self.book_end_time = book_end_time
        self.book_remaining_seconds = book_remaining_seconds
        self.booked_num = booked_num
        self.booked_partners = booked_partners
        self.constitute = constitute
        self.currency_type = currency_type
        self.delivery_time = delivery_time
        self.domain_id = domain_id
        self.domain_len = domain_len
        self.domain_name = domain_name
        self.domain_type = domain_type
        self.end_date = end_date
        self.expire_date = expire_date
        self.extend = extend
        self.freeze_amount = freeze_amount
        self.icp_number = icp_number
        self.icp_status = icp_status
        self.introduction = introduction
        self.is_premium = is_premium
        self.partner_types = partner_types
        self.price = price
        self.product_id = product_id
        self.publish_time = publish_time
        self.reg_date = reg_date
        self.registrar = registrar
        self.renew_price = renew_price
        self.reserved = reserved
        self.rmb_price = rmb_price
        self.s_360weight = s_360weight
        self.seo_attributes = seo_attributes
        self.short_name = short_name
        self.snatch_no = snatch_no
        self.snatch_type_desc = snatch_type_desc
        self.sougou_anti_link = sougou_anti_link
        self.sougou_index = sougou_index
        self.sougou_weight = sougou_weight
        self.suffix = suffix
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auction_end_time is not None:
            result['AuctionEndTime'] = self.auction_end_time

        if self.auction_remaining_seconds is not None:
            result['AuctionRemainingSeconds'] = self.auction_remaining_seconds

        if self.baidu_anti_link is not None:
            result['BaiduAntiLink'] = self.baidu_anti_link

        if self.baidu_ex_link is not None:
            result['BaiduExLink'] = self.baidu_ex_link

        if self.baidu_index is not None:
            result['BaiduIndex'] = self.baidu_index

        if self.baidu_weight is not None:
            result['BaiduWeight'] = self.baidu_weight

        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time

        if self.book_remaining_seconds is not None:
            result['BookRemainingSeconds'] = self.book_remaining_seconds

        if self.booked_num is not None:
            result['BookedNum'] = self.booked_num

        if self.booked_partners is not None:
            result['BookedPartners'] = self.booked_partners

        if self.constitute is not None:
            result['Constitute'] = self.constitute

        if self.currency_type is not None:
            result['CurrencyType'] = self.currency_type

        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_len is not None:
            result['DomainLen'] = self.domain_len

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.freeze_amount is not None:
            result['FreezeAmount'] = self.freeze_amount

        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number

        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.is_premium is not None:
            result['IsPremium'] = self.is_premium

        if self.partner_types is not None:
            result['PartnerTypes'] = self.partner_types

        if self.price is not None:
            result['Price'] = self.price

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.reg_date is not None:
            result['RegDate'] = self.reg_date

        if self.registrar is not None:
            result['Registrar'] = self.registrar

        if self.renew_price is not None:
            result['RenewPrice'] = self.renew_price

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.rmb_price is not None:
            result['RmbPrice'] = self.rmb_price

        if self.s_360weight is not None:
            result['S360Weight'] = self.s_360weight

        if self.seo_attributes is not None:
            result['SeoAttributes'] = self.seo_attributes

        if self.short_name is not None:
            result['ShortName'] = self.short_name

        if self.snatch_no is not None:
            result['SnatchNo'] = self.snatch_no

        if self.snatch_type_desc is not None:
            result['SnatchTypeDesc'] = self.snatch_type_desc

        if self.sougou_anti_link is not None:
            result['SougouAntiLink'] = self.sougou_anti_link

        if self.sougou_index is not None:
            result['SougouIndex'] = self.sougou_index

        if self.sougou_weight is not None:
            result['SougouWeight'] = self.sougou_weight

        if self.suffix is not None:
            result['Suffix'] = self.suffix

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')

        if m.get('AuctionRemainingSeconds') is not None:
            self.auction_remaining_seconds = m.get('AuctionRemainingSeconds')

        if m.get('BaiduAntiLink') is not None:
            self.baidu_anti_link = m.get('BaiduAntiLink')

        if m.get('BaiduExLink') is not None:
            self.baidu_ex_link = m.get('BaiduExLink')

        if m.get('BaiduIndex') is not None:
            self.baidu_index = m.get('BaiduIndex')

        if m.get('BaiduWeight') is not None:
            self.baidu_weight = m.get('BaiduWeight')

        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')

        if m.get('BookRemainingSeconds') is not None:
            self.book_remaining_seconds = m.get('BookRemainingSeconds')

        if m.get('BookedNum') is not None:
            self.booked_num = m.get('BookedNum')

        if m.get('BookedPartners') is not None:
            self.booked_partners = m.get('BookedPartners')

        if m.get('Constitute') is not None:
            self.constitute = m.get('Constitute')

        if m.get('CurrencyType') is not None:
            self.currency_type = m.get('CurrencyType')

        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainLen') is not None:
            self.domain_len = m.get('DomainLen')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('FreezeAmount') is not None:
            self.freeze_amount = m.get('FreezeAmount')

        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')

        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('IsPremium') is not None:
            self.is_premium = m.get('IsPremium')

        if m.get('PartnerTypes') is not None:
            self.partner_types = m.get('PartnerTypes')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')

        if m.get('Registrar') is not None:
            self.registrar = m.get('Registrar')

        if m.get('RenewPrice') is not None:
            self.renew_price = m.get('RenewPrice')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('RmbPrice') is not None:
            self.rmb_price = m.get('RmbPrice')

        if m.get('S360Weight') is not None:
            self.s_360weight = m.get('S360Weight')

        if m.get('SeoAttributes') is not None:
            self.seo_attributes = m.get('SeoAttributes')

        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')

        if m.get('SnatchNo') is not None:
            self.snatch_no = m.get('SnatchNo')

        if m.get('SnatchTypeDesc') is not None:
            self.snatch_type_desc = m.get('SnatchTypeDesc')

        if m.get('SougouAntiLink') is not None:
            self.sougou_anti_link = m.get('SougouAntiLink')

        if m.get('SougouIndex') is not None:
            self.sougou_index = m.get('SougouIndex')

        if m.get('SougouWeight') is not None:
            self.sougou_weight = m.get('SougouWeight')

        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

