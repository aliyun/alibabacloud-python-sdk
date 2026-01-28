# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class SaveBatchTaskForCreatingOrderActivateRequest(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        lang: str = None,
        order_activate_param: List[main_models.SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam] = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        self.lang = lang
        # This parameter is required.
        self.order_activate_param = order_activate_param
        self.promotion_no = promotion_no
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.order_activate_param:
            for v1 in self.order_activate_param:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.lang is not None:
            result['Lang'] = self.lang

        result['OrderActivateParam'] = []
        if self.order_activate_param is not None:
            for k1 in self.order_activate_param:
                result['OrderActivateParam'].append(k1.to_map() if k1 else None)

        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no

        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon

        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.order_activate_param = []
        if m.get('OrderActivateParam') is not None:
            for k1 in m.get('OrderActivateParam'):
                temp_model = main_models.SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam()
                self.order_activate_param.append(temp_model.from_map(k1))

        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')

        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')

        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

class SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam(DaraModel):
    def __init__(
        self,
        address: str = None,
        aliyun_dns: bool = None,
        city: str = None,
        country: str = None,
        dns_1: str = None,
        dns_2: str = None,
        domain_name: str = None,
        email: str = None,
        enable_domain_proxy: bool = None,
        permit_premium_activation: bool = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_type: str = None,
        resource_group_id: str = None,
        subscription_duration: int = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        trademark_domain_activation: bool = None,
        zh_address: str = None,
        zh_city: str = None,
        zh_province: str = None,
        zh_registrant_name: str = None,
        zh_registrant_organization: str = None,
    ):
        self.address = address
        self.aliyun_dns = aliyun_dns
        self.city = city
        self.country = country
        self.dns_1 = dns_1
        self.dns_2 = dns_2
        # This parameter is required.
        self.domain_name = domain_name
        self.email = email
        self.enable_domain_proxy = enable_domain_proxy
        self.permit_premium_activation = permit_premium_activation
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_profile_id = registrant_profile_id
        self.registrant_type = registrant_type
        self.resource_group_id = resource_group_id
        self.subscription_duration = subscription_duration
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone
        self.trademark_domain_activation = trademark_domain_activation
        self.zh_address = zh_address
        self.zh_city = zh_city
        self.zh_province = zh_province
        self.zh_registrant_name = zh_registrant_name
        self.zh_registrant_organization = zh_registrant_organization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.aliyun_dns is not None:
            result['AliyunDns'] = self.aliyun_dns

        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.dns_1 is not None:
            result['Dns1'] = self.dns_1

        if self.dns_2 is not None:
            result['Dns2'] = self.dns_2

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.email is not None:
            result['Email'] = self.email

        if self.enable_domain_proxy is not None:
            result['EnableDomainProxy'] = self.enable_domain_proxy

        if self.permit_premium_activation is not None:
            result['PermitPremiumActivation'] = self.permit_premium_activation

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.province is not None:
            result['Province'] = self.province

        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name

        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration

        if self.tel_area is not None:
            result['TelArea'] = self.tel_area

        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.trademark_domain_activation is not None:
            result['TrademarkDomainActivation'] = self.trademark_domain_activation

        if self.zh_address is not None:
            result['ZhAddress'] = self.zh_address

        if self.zh_city is not None:
            result['ZhCity'] = self.zh_city

        if self.zh_province is not None:
            result['ZhProvince'] = self.zh_province

        if self.zh_registrant_name is not None:
            result['ZhRegistrantName'] = self.zh_registrant_name

        if self.zh_registrant_organization is not None:
            result['ZhRegistrantOrganization'] = self.zh_registrant_organization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Dns1') is not None:
            self.dns_1 = m.get('Dns1')

        if m.get('Dns2') is not None:
            self.dns_2 = m.get('Dns2')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EnableDomainProxy') is not None:
            self.enable_domain_proxy = m.get('EnableDomainProxy')

        if m.get('PermitPremiumActivation') is not None:
            self.permit_premium_activation = m.get('PermitPremiumActivation')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')

        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')

        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')

        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('TrademarkDomainActivation') is not None:
            self.trademark_domain_activation = m.get('TrademarkDomainActivation')

        if m.get('ZhAddress') is not None:
            self.zh_address = m.get('ZhAddress')

        if m.get('ZhCity') is not None:
            self.zh_city = m.get('ZhCity')

        if m.get('ZhProvince') is not None:
            self.zh_province = m.get('ZhProvince')

        if m.get('ZhRegistrantName') is not None:
            self.zh_registrant_name = m.get('ZhRegistrantName')

        if m.get('ZhRegistrantOrganization') is not None:
            self.zh_registrant_organization = m.get('ZhRegistrantOrganization')

        return self

