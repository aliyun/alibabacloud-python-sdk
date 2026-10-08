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
        # The voucher ID.
        self.coupon_no = coupon_no
        # The language of the error message returned by the API operation. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # The list of task details.
        # 
        # This parameter is required.
        self.order_activate_param = order_activate_param
        # The coupon ID.
        self.promotion_no = promotion_no
        # Specifies whether to use a voucher.
        self.use_coupon = use_coupon
        # Specifies whether to use a coupon.
        self.use_promotion = use_promotion
        # The IP address of the user.
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
        expected_punycode: str = None,
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
        # The mailing address in English.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.address = address
        # Specifies whether to use Alibaba Cloud DNS. Valid values: **true** and **false**. Default value: **true**.
        # 
        # > - If this parameter is set to **true**, you do not need to specify the **OrderActivateParam.N.Dns1** and **OrderActivateParam.N.Dns2** parameters. Otherwise, the specified **OrderActivateParam.N.Dns1** and **OrderActivateParam.N.Dns2** parameters do not take effect. 
        # - If this parameter is set to **false**, you must also specify the **OrderActivateParam.N.Dns1** and **OrderActivateParam.N.Dns2** parameters.
        self.aliyun_dns = aliyun_dns
        # The city name in English.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.city = city
        # The country code. For example, **CN** represents China, and **US** represents the United States.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.country = country
        # The custom DNS server 1.
        # 
        # > - This parameter is available and required only when the **OrderActivateParam.N.AliyunDns** parameter is set to **false**.
        # - Make sure that the custom DNS server is correct. Otherwise, the registration may fail.
        self.dns_1 = dns_1
        # The custom DNS server 2.
        # 
        # > - This parameter is available and required only when the **OrderActivateParam.N.AliyunDns** parameter is set to **false**.
        # - Make sure that the custom DNS server is correct. Otherwise, the registration may fail.
        self.dns_2 = dns_2
        # The domain name to be registered.
        # 
        # > When you register a domain name, you must specify the domain name registrant information. Otherwise, the domain name registration fails. You can specify the domain name registrant information by using the OrderActivateParam.N.RegistrantProfileId parameter to associate a domain name registrant profile.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The email address.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.email = email
        # Specifies whether to enable the domain name privacy protection service. Default value: **true**.
        self.enable_domain_proxy = enable_domain_proxy
        # The domain name in Punycode format. This parameter can be left empty.
        self.expected_punycode = expected_punycode
        # Specifies whether to allow the registration of premium domain names. Default value: **false**.
        self.permit_premium_activation = permit_premium_activation
        # The postal code.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.postal_code = postal_code
        # The province name in English.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.province = province
        # The domain name contact in English.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.registrant_name = registrant_name
        # The name of the domain name registrant in English.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.registrant_organization = registrant_organization
        # The ID of the domain name registrant profile. The profile contains information such as the name of the domain name registrant, the domain name contact, the phone number, and the email address. You can only use the ID of a real-name verified domain name registrant profile to register a domain name. If you have created a domain name registrant profile, you can call the [QueryRegistrantProfiles](https://help.aliyun.com/document_detail/67701.html) operation to query the profile ID.
        # 
        # > After you specify this parameter, you do not need to specify the **OrderActivateParam.N.RegistrantType**, **OrderActivateParam.N.ZhRegistrantOrganization**, **OrderActivateParam.N.ZhRegistrantName**, **OrderActivateParam.N.ZhProvince**, **OrderActivateParam.N.ZhCity**, **OrderActivateParam.N.ZhAddress**, **OrderActivateParam.N.RegistrantOrganization**, **OrderActivateParam.N.RegistrantName**, **OrderActivateParam.N.Province**, **OrderActivateParam.N.City**, **OrderActivateParam.N.Address**, **OrderActivateParam.N.PostalCode**, **OrderActivateParam.N.Country**, **OrderActivateParam.N.TelArea**, **OrderActivateParam.N.Telephone**, **OrderActivateParam.N.TelExt**, and **OrderActivateParam.N.Email** parameters.
        self.registrant_profile_id = registrant_profile_id
        # The type of the domain name registrant. Valid values:
        # - **1**: Individual.
        # - **2**: Enterprise or organization.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.registrant_type = registrant_type
        # The resource group ID.
        # > If this parameter is not specified or the specified resource group ID does not exist, the default resource group ID is used.
        self.resource_group_id = resource_group_id
        # The subscription duration. Unit: **year**. Default value: **1**.
        self.subscription_duration = subscription_duration
        # The country code for the phone number. For example, the country code for China is **86**.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.tel_area = tel_area
        # The extension number.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.tel_ext = tel_ext
        # The phone number.
        # 
        # > This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.telephone = telephone
        # Specifies whether to allow the registration of trademark terms.
        self.trademark_domain_activation = trademark_domain_activation
        # The mailing address in Chinese.
        # 
        # > This parameter is applicable only to the China site. This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.zh_address = zh_address
        # The city name in Chinese.
        # 
        # > This parameter is applicable only to the China site. This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.zh_city = zh_city
        # The province name in Chinese.
        # 
        # > This parameter is applicable only to the China site. This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.zh_province = zh_province
        # The domain name contact in Chinese.
        # 
        # > This parameter is applicable only to the China site. This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
        self.zh_registrant_name = zh_registrant_name
        # The name of the domain name registrant in Chinese.
        # 
        # > This parameter is applicable only to the China site. This parameter is available and required only when the **OrderActivateParam.N.RegistrantProfileId** parameter is not specified. If this parameter is not specified, the domain name registration fails.
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

        if self.expected_punycode is not None:
            result['ExpectedPunycode'] = self.expected_punycode

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

        if m.get('ExpectedPunycode') is not None:
            self.expected_punycode = m.get('ExpectedPunycode')

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

