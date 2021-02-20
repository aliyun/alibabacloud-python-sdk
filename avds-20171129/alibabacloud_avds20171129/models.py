# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddAssetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        start_after_verified: bool = None,
        asset_group_id: str = None,
        assets: List[str] = None,
        tags: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.start_after_verified = start_after_verified
        self.asset_group_id = asset_group_id
        self.assets = assets
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_after_verified is not None:
            result['StartAfterVerified'] = self.start_after_verified
        if self.asset_group_id is not None:
            result['AssetGroupId'] = self.asset_group_id
        if self.assets is not None:
            result['Assets'] = self.assets
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartAfterVerified') is not None:
            self.start_after_verified = m.get('StartAfterVerified')
        if m.get('AssetGroupId') is not None:
            self.asset_group_id = m.get('AssetGroupId')
        if m.get('Assets') is not None:
            self.assets = m.get('Assets')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddAssetsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAssetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAssetTagsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        assets: List[str] = None,
        tags: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.assets = assets
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.assets is not None:
            result['Assets'] = self.assets
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Assets') is not None:
            self.assets = m.get('Assets')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddAssetTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddAssetTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAssetTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAssetTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrgDomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_id: int = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.org_id = org_id
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class AddOrgDomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddOrgDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddOrgDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddOrgDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrgHostsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_id: int = None,
        hosts: List[str] = None,
    ):
        self.source_ip = source_ip
        self.org_id = org_id
        self.hosts = hosts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        return self


class AddOrgHostsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddOrgHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddOrgHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddOrgHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrgSubdomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_id: int = None,
        subdomains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.org_id = org_id
        self.subdomains = subdomains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.subdomains is not None:
            result['Subdomains'] = self.subdomains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Subdomains') is not None:
            self.subdomains = m.get('Subdomains')
        return self


class AddOrgSubdomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddOrgSubdomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddOrgSubdomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddOrgSubdomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrgWebPathsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_id: int = None,
        urls: List[str] = None,
    ):
        self.source_ip = source_ip
        self.org_id = org_id
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.urls is not None:
            result['URLs'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('URLs') is not None:
            self.urls = m.get('URLs')
        return self


class AddOrgWebPathsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddOrgWebPathsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddOrgWebPathsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddOrgWebPathsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAvdsBagOrderRequest(TeaModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        flowout_spec: str = None,
        pack: str = None,
    ):
        self.period = period
        self.period_unit = period_unit
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        self.flowout_spec = flowout_spec
        self.pack = pack

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.flowout_spec is not None:
            result['FlowoutSpec'] = self.flowout_spec
        if self.pack is not None:
            result['Pack'] = self.pack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('FlowoutSpec') is not None:
            self.flowout_spec = m.get('FlowoutSpec')
        if m.get('Pack') is not None:
            self.pack = m.get('Pack')
        return self


class CreateAvdsBagOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateAvdsBagOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAvdsBagOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAvdsBagOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAvdsOrderRequest(TeaModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        site_num: str = None,
        service_version: str = None,
        url_num: str = None,
        add_vul_num: str = None,
    ):
        self.period = period
        self.period_unit = period_unit
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        self.site_num = site_num
        self.service_version = service_version
        self.url_num = url_num
        self.add_vul_num = add_vul_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.site_num is not None:
            result['SiteNum'] = self.site_num
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.url_num is not None:
            result['UrlNum'] = self.url_num
        if self.add_vul_num is not None:
            result['AddVulNum'] = self.add_vul_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('SiteNum') is not None:
            self.site_num = m.get('SiteNum')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('UrlNum') is not None:
            self.url_num = m.get('UrlNum')
        if m.get('AddVulNum') is not None:
            self.add_vul_num = m.get('AddVulNum')
        return self


class CreateAvdsOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateAvdsOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAvdsOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAvdsOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAvdsPublicOrderRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        name_time: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        self.name_time = name_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.name_time is not None:
            result['NameTime'] = self.name_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('NameTime') is not None:
            self.name_time = m.get('NameTime')
        return self


class CreateAvdsPublicOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateAvdsPublicOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAvdsPublicOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAvdsPublicOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrganizationRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        name: str = None,
        description: str = None,
        domains: List[str] = None,
    ):
        self.source_ip = source_ip
        self.name = name
        self.description = description
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class CreateOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrganizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSessionRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        asset: str = None,
        ttl: int = None,
        login_session: str = None,
    ):
        self.source_ip = source_ip
        self.asset = asset
        self.ttl = ttl
        self.login_session = login_session

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.login_session is not None:
            result['LoginSession'] = self.login_session
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('LoginSession') is not None:
            self.login_session = m.get('LoginSession')
        return self


class CreateSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSessionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAssetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        asset_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.asset_ids = asset_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.asset_ids is not None:
            result['AssetIds'] = self.asset_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AssetIds') is not None:
            self.asset_ids = m.get('AssetIds')
        return self


class DeleteAssetsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAssetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOrganizationsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.org_ids = org_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_ids is not None:
            result['OrgIds'] = self.org_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgIds') is not None:
            self.org_ids = m.get('OrgIds')
        return self


class DeleteOrganizationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteOrganizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOrganizationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOrgAttackSurfaceRecordsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        source: str = None,
        org_id: int = None,
        records: List[int] = None,
    ):
        self.source_ip = source_ip
        self.source = source
        self.org_id = org_id
        self.records = records

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source is not None:
            result['Source'] = self.source
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.records is not None:
            result['Records'] = self.records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Records') is not None:
            self.records = m.get('Records')
        return self


class DeleteOrgAttackSurfaceRecordsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteOrgAttackSurfaceRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOrgAttackSurfaceRecordsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteOrgAttackSurfaceRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSessionRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        session_id: int = None,
    ):
        self.source_ip = source_ip
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DeleteSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSessionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserAttackSurfaceRecordsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        source: str = None,
        records: List[int] = None,
    ):
        self.source_ip = source_ip
        self.source = source
        self.records = records

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source is not None:
            result['Source'] = self.source
        if self.records is not None:
            result['Records'] = self.records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Records') is not None:
            self.records = m.get('Records')
        return self


class DeleteUserAttackSurfaceRecordsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserAttackSurfaceRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserAttackSurfaceRecordsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserAttackSurfaceRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllVulnerabilitiesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        scan_id: str = None,
        name: str = None,
        search: str = None,
        lang: str = None,
        severity: int = None,
        status: str = None,
        begin_time: int = None,
        end_time: int = None,
        task_id: int = None,
        category: str = None,
        module: str = None,
        vul_type: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.scan_id = scan_id
        self.name = name
        self.search = search
        self.lang = lang
        self.severity = severity
        self.status = status
        self.begin_time = begin_time
        self.end_time = end_time
        self.task_id = task_id
        self.category = category
        self.module = module
        self.vul_type = vul_type
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scan_id is not None:
            result['ScanId'] = self.scan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.search is not None:
            result['Search'] = self.search
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.status is not None:
            result['Status'] = self.status
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.category is not None:
            result['Category'] = self.category
        if self.module is not None:
            result['Module'] = self.module
        if self.vul_type is not None:
            result['VulType'] = self.vul_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScanId') is not None:
            self.scan_id = m.get('ScanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('VulType') is not None:
            self.vul_type = m.get('VulType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAllVulnerabilitiesResponseBodyList(TeaModel):
    def __init__(
        self,
        status: int = None,
        severity: int = None,
        last_discovered_at: int = None,
        hostname: str = None,
        name: str = None,
        task_id: int = None,
        vulnerability_type_des: str = None,
        target: str = None,
        id: int = None,
    ):
        self.status = status
        self.severity = severity
        self.last_discovered_at = last_discovered_at
        self.hostname = hostname
        self.name = name
        self.task_id = task_id
        self.vulnerability_type_des = vulnerability_type_des
        self.target = target
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.last_discovered_at is not None:
            result['LastDiscoveredAt'] = self.last_discovered_at
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.name is not None:
            result['Name'] = self.name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vulnerability_type_des is not None:
            result['VulnerabilityTypeDes'] = self.vulnerability_type_des
        if self.target is not None:
            result['Target'] = self.target
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('LastDiscoveredAt') is not None:
            self.last_discovered_at = m.get('LastDiscoveredAt')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VulnerabilityTypeDes') is not None:
            self.vulnerability_type_des = m.get('VulnerabilityTypeDes')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeAllVulnerabilitiesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_count: int = None,
        current_page: int = None,
        list: List[DescribeAllVulnerabilitiesResponseBodyList] = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_count = page_count
        self.current_page = current_page
        self.list = list
        self.count = count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeAllVulnerabilitiesResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeAllVulnerabilitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAllVulnerabilitiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAllVulnerabilitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        status: str = None,
        search: str = None,
        asset_group_id: str = None,
        source: str = None,
        gmt_create_from: int = None,
        gmt_create_to: int = None,
        current_page: int = None,
        page_size: int = None,
        types: List[str] = None,
        assets: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.status = status
        self.search = search
        self.asset_group_id = asset_group_id
        self.source = source
        self.gmt_create_from = gmt_create_from
        self.gmt_create_to = gmt_create_to
        self.current_page = current_page
        self.page_size = page_size
        self.types = types
        self.assets = assets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.search is not None:
            result['Search'] = self.search
        if self.asset_group_id is not None:
            result['AssetGroupId'] = self.asset_group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.gmt_create_from is not None:
            result['GmtCreateFrom'] = self.gmt_create_from
        if self.gmt_create_to is not None:
            result['GmtCreateTo'] = self.gmt_create_to
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.types is not None:
            result['Types'] = self.types
        if self.assets is not None:
            result['Assets'] = self.assets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('AssetGroupId') is not None:
            self.asset_group_id = m.get('AssetGroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('GmtCreateFrom') is not None:
            self.gmt_create_from = m.get('GmtCreateFrom')
        if m.get('GmtCreateTo') is not None:
            self.gmt_create_to = m.get('GmtCreateTo')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        if m.get('Assets') is not None:
            self.assets = m.get('Assets')
        return self


class DescribeAssetsResponseBodyList(TeaModel):
    def __init__(
        self,
        type: str = None,
        last_scan_date: int = None,
        expire_time: int = None,
        asset_id: str = None,
        gmt_create: int = None,
        source: str = None,
        asset: str = None,
    ):
        self.type = type
        self.last_scan_date = last_scan_date
        self.expire_time = expire_time
        self.asset_id = asset_id
        self.gmt_create = gmt_create
        self.source = source
        self.asset = asset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.last_scan_date is not None:
            result['LastScanDate'] = self.last_scan_date
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.source is not None:
            result['Source'] = self.source
        if self.asset is not None:
            result['Asset'] = self.asset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('LastScanDate') is not None:
            self.last_scan_date = m.get('LastScanDate')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        return self


class DescribeAssetsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_count: int = None,
        current_page: int = None,
        list: List[DescribeAssetsResponseBodyList] = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_count = page_count
        self.current_page = current_page
        self.list = list
        self.count = count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeAssetsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAssetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAttackSurfacesFacetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeAttackSurfacesFacetsResponseBody(TeaModel):
    def __init__(
        self,
        domains: int = None,
        hosts: int = None,
        web_paths: int = None,
        request_id: str = None,
        dnsmap: int = None,
        web_servers: int = None,
        ports: int = None,
        crawler_requests: int = None,
        web_techs: int = None,
        subdomains: int = None,
    ):
        self.domains = domains
        self.hosts = hosts
        self.web_paths = web_paths
        self.request_id = request_id
        self.dnsmap = dnsmap
        self.web_servers = web_servers
        self.ports = ports
        self.crawler_requests = crawler_requests
        self.web_techs = web_techs
        self.subdomains = subdomains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.web_paths is not None:
            result['WebPaths'] = self.web_paths
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dnsmap is not None:
            result['DNSMap'] = self.dnsmap
        if self.web_servers is not None:
            result['WebServers'] = self.web_servers
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.crawler_requests is not None:
            result['CrawlerRequests'] = self.crawler_requests
        if self.web_techs is not None:
            result['WebTechs'] = self.web_techs
        if self.subdomains is not None:
            result['Subdomains'] = self.subdomains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('WebPaths') is not None:
            self.web_paths = m.get('WebPaths')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DNSMap') is not None:
            self.dnsmap = m.get('DNSMap')
        if m.get('WebServers') is not None:
            self.web_servers = m.get('WebServers')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('CrawlerRequests') is not None:
            self.crawler_requests = m.get('CrawlerRequests')
        if m.get('WebTechs') is not None:
            self.web_techs = m.get('WebTechs')
        if m.get('Subdomains') is not None:
            self.subdomains = m.get('Subdomains')
        return self


class DescribeAttackSurfacesFacetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAttackSurfacesFacetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAttackSurfacesFacetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCrawlerRequestsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCrawlerRequestsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        data: str = None,
        url: str = None,
        method: str = None,
        updated_at: int = None,
        cookies: str = None,
    ):
        self.index = index
        self.data = data
        self.url = url
        self.method = method
        self.updated_at = updated_at
        self.cookies = cookies

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.data is not None:
            result['Data'] = self.data
        if self.url is not None:
            result['URL'] = self.url
        if self.method is not None:
            result['Method'] = self.method
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        return self


class DescribeCrawlerRequestsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribeCrawlerRequestsResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeCrawlerRequestsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeCrawlerRequestsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCrawlerRequestsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCrawlerRequestsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDNSMapRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDNSMapResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        type: str = None,
        domain: str = None,
        updated_at: int = None,
        record: str = None,
    ):
        self.index = index
        self.type = type
        self.domain = domain
        self.updated_at = updated_at
        self.record = record

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.record is not None:
            result['Record'] = self.record
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        return self


class DescribeDNSMapResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribeDNSMapResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDNSMapResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeDNSMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDNSMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDNSMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAttackSurfacesFacetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainAttackSurfacesFacetsResponseBody(TeaModel):
    def __init__(
        self,
        web_paths: int = None,
        request_id: str = None,
        web_servers: int = None,
        crawler_requests: int = None,
        web_techs: int = None,
    ):
        self.web_paths = web_paths
        self.request_id = request_id
        self.web_servers = web_servers
        self.crawler_requests = crawler_requests
        self.web_techs = web_techs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.web_paths is not None:
            result['WebPaths'] = self.web_paths
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.web_servers is not None:
            result['WebServers'] = self.web_servers
        if self.crawler_requests is not None:
            result['CrawlerRequests'] = self.crawler_requests
        if self.web_techs is not None:
            result['WebTechs'] = self.web_techs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebPaths') is not None:
            self.web_paths = m.get('WebPaths')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebServers') is not None:
            self.web_servers = m.get('WebServers')
        if m.get('CrawlerRequests') is not None:
            self.crawler_requests = m.get('CrawlerRequests')
        if m.get('WebTechs') is not None:
            self.web_techs = m.get('WebTechs')
        return self


class DescribeDomainAttackSurfacesFacetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainAttackSurfacesFacetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainAttackSurfacesFacetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        domain: str = None,
        updated_at: int = None,
    ):
        self.index = index
        self.domain = domain
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribeDomainsResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDomainsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostAttackSurfacesFacetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        host: str = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.host = host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.host is not None:
            result['Host'] = self.host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        return self


class DescribeHostAttackSurfacesFacetsResponseBody(TeaModel):
    def __init__(
        self,
        hosts: int = None,
        web_paths: int = None,
        request_id: str = None,
        ports: int = None,
        crawler_requests: int = None,
        web_techs: int = None,
    ):
        self.hosts = hosts
        self.web_paths = web_paths
        self.request_id = request_id
        self.ports = ports
        self.crawler_requests = crawler_requests
        self.web_techs = web_techs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.web_paths is not None:
            result['WebPaths'] = self.web_paths
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.crawler_requests is not None:
            result['CrawlerRequests'] = self.crawler_requests
        if self.web_techs is not None:
            result['WebTechs'] = self.web_techs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('WebPaths') is not None:
            self.web_paths = m.get('WebPaths')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('CrawlerRequests') is not None:
            self.crawler_requests = m.get('CrawlerRequests')
        if m.get('WebTechs') is not None:
            self.web_techs = m.get('WebTechs')
        return self


class DescribeHostAttackSurfacesFacetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHostAttackSurfacesFacetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHostAttackSurfacesFacetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeHostsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        os: str = None,
        hostname: str = None,
        updated_at: int = None,
        ip: str = None,
        is_up: str = None,
    ):
        self.index = index
        self.os = os
        self.hostname = hostname
        self.updated_at = updated_at
        self.ip = ip
        self.is_up = is_up

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.os is not None:
            result['OS'] = self.os
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.ip is not None:
            result['IP'] = self.ip
        if self.is_up is not None:
            result['IsUp'] = self.is_up
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('OS') is not None:
            self.os = m.get('OS')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('IsUp') is not None:
            self.is_up = m.get('IsUp')
        return self


class DescribeHostsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribeHostsResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeHostsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeListSessionsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeListSessionsResponseBodySessions(TeaModel):
    def __init__(
        self,
        ttl: int = None,
        expired: int = None,
        created_at: int = None,
        ali_uid: int = None,
        modified_at: int = None,
        login_session: str = None,
        session_id: int = None,
        asset: str = None,
    ):
        self.ttl = ttl
        self.expired = expired
        self.created_at = created_at
        self.ali_uid = ali_uid
        self.modified_at = modified_at
        self.login_session = login_session
        self.session_id = session_id
        self.asset = asset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.login_session is not None:
            result['LoginSession'] = self.login_session
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.asset is not None:
            result['Asset'] = self.asset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('LoginSession') is not None:
            self.login_session = m.get('LoginSession')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        return self


class DescribeListSessionsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        sessions: List[DescribeListSessionsResponseBodySessions] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.sessions = sessions

    def validate(self):
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['Sessions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = DescribeListSessionsResponseBodySessions()
                self.sessions.append(temp_model.from_map(k))
        return self


class DescribeListSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeListSessionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeListSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOrgAttackSurfaceDetailsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        record_id: int = None,
        org_id: int = None,
        source: str = None,
    ):
        self.source_ip = source_ip
        self.record_id = record_id
        self.org_id = org_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeOrgAttackSurfaceDetailsResponseBody(TeaModel):
    def __init__(
        self,
        last_scanned_at: int = None,
        request_id: str = None,
        first_scanned_at: int = None,
        occurrences: int = None,
    ):
        self.last_scanned_at = last_scanned_at
        self.request_id = request_id
        self.first_scanned_at = first_scanned_at
        self.occurrences = occurrences

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.last_scanned_at is not None:
            result['LastScannedAt'] = self.last_scanned_at
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.first_scanned_at is not None:
            result['FirstScannedAt'] = self.first_scanned_at
        if self.occurrences is not None:
            result['Occurrences'] = self.occurrences
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastScannedAt') is not None:
            self.last_scanned_at = m.get('LastScannedAt')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FirstScannedAt') is not None:
            self.first_scanned_at = m.get('FirstScannedAt')
        if m.get('Occurrences') is not None:
            self.occurrences = m.get('Occurrences')
        return self


class DescribeOrgAttackSurfaceDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOrgAttackSurfaceDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOrgAttackSurfaceDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOrgInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_id: int = None,
    ):
        self.source_ip = source_ip
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class DescribeOrgInfoResponseBody(TeaModel):
    def __init__(
        self,
        org_id: int = None,
        description: str = None,
        request_id: str = None,
        created_at: int = None,
        ali_uid: int = None,
        name: str = None,
    ):
        self.org_id = org_id
        self.description = description
        self.request_id = request_id
        self.created_at = created_at
        self.ali_uid = ali_uid
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeOrgInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOrgInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOrgInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePortsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        service: str = None,
        index: int = None,
        fingerprint: str = None,
        version: str = None,
        product: str = None,
        protocol: str = None,
        updated_at: int = None,
        port: str = None,
        ip: str = None,
    ):
        self.service = service
        self.index = index
        self.fingerprint = fingerprint
        self.version = version
        self.product = product
        self.protocol = protocol
        self.updated_at = updated_at
        self.port = port
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.index is not None:
            result['Index'] = self.index
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.version is not None:
            result['Version'] = self.version
        if self.product is not None:
            result['Product'] = self.product
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.port is not None:
            result['Port'] = self.port
        if self.ip is not None:
            result['IP'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class DescribePortsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribePortsResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribePortsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribePortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScanSessionsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        scan_id: str = None,
        current_page: int = None,
        page_size: int = None,
        search: str = None,
        status_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.scan_id = scan_id
        self.current_page = current_page
        self.page_size = page_size
        self.search = search
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scan_id is not None:
            result['ScanId'] = self.scan_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search is not None:
            result['Search'] = self.search
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScanId') is not None:
            self.scan_id = m.get('ScanId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class DescribeScanSessionsResponseBodyList(TeaModel):
    def __init__(
        self,
        report_status: str = None,
        finished_at: int = None,
        targets: List[str] = None,
        created_at: int = None,
        scan_id: str = None,
        period: str = None,
        trigger_type: str = None,
        report_url: str = None,
        job_status: str = None,
        run_percent: float = None,
        interval: int = None,
        name: str = None,
        task_id: int = None,
    ):
        self.report_status = report_status
        self.finished_at = finished_at
        self.targets = targets
        self.created_at = created_at
        self.scan_id = scan_id
        self.period = period
        self.trigger_type = trigger_type
        self.report_url = report_url
        self.job_status = job_status
        self.run_percent = run_percent
        self.interval = interval
        self.name = name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.scan_id is not None:
            result['ScanId'] = self.scan_id
        if self.period is not None:
            result['Period'] = self.period
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.run_percent is not None:
            result['RunPercent'] = self.run_percent
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.name is not None:
            result['Name'] = self.name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('ScanId') is not None:
            self.scan_id = m.get('ScanId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('RunPercent') is not None:
            self.run_percent = m.get('RunPercent')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeScanSessionsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_count: int = None,
        current_page: int = None,
        list: List[DescribeScanSessionsResponseBodyList] = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_count = page_count
        self.current_page = current_page
        self.list = list
        self.count = count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeScanSessionsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeScanSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScanSessionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScanSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSessionRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        session_id: int = None,
    ):
        self.source_ip = source_ip
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DescribeSessionResponseBodySession(TeaModel):
    def __init__(
        self,
        ttl: int = None,
        expired: int = None,
        created_at: int = None,
        ali_uid: int = None,
        modified_at: int = None,
        login_session: str = None,
        session_id: int = None,
        asset: str = None,
    ):
        self.ttl = ttl
        self.expired = expired
        self.created_at = created_at
        self.ali_uid = ali_uid
        self.modified_at = modified_at
        self.login_session = login_session
        self.session_id = session_id
        self.asset = asset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.login_session is not None:
            result['LoginSession'] = self.login_session
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.asset is not None:
            result['Asset'] = self.asset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('LoginSession') is not None:
            self.login_session = m.get('LoginSession')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        return self


class DescribeSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session: DescribeSessionResponseBodySession = None,
    ):
        self.request_id = request_id
        self.session = session

    def validate(self):
        if self.session:
            self.session.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session is not None:
            result['Session'] = self.session.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Session') is not None:
            temp_model = DescribeSessionResponseBodySession()
            self.session = temp_model.from_map(m['Session'])
        return self


class DescribeSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSessionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubdomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSubdomainsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        domain: str = None,
        updated_at: int = None,
        root_domain: str = None,
    ):
        self.index = index
        self.domain = domain
        self.updated_at = updated_at
        self.root_domain = root_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.root_domain is not None:
            result['RootDomain'] = self.root_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('RootDomain') is not None:
            self.root_domain = m.get('RootDomain')
        return self


class DescribeSubdomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribeSubdomainsResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeSubdomainsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeSubdomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubdomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSubdomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskBriefInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeTaskBriefInfoResponseBodyRisksFacets(TeaModel):
    def __init__(
        self,
        medium: int = None,
        low: int = None,
        total: int = None,
        high: int = None,
        info: int = None,
    ):
        self.medium = medium
        self.low = low
        self.total = total
        self.high = high
        self.info = info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.low is not None:
            result['Low'] = self.low
        if self.total is not None:
            result['Total'] = self.total
        if self.high is not None:
            result['High'] = self.high
        if self.info is not None:
            result['Info'] = self.info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Low') is not None:
            self.low = m.get('Low')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('High') is not None:
            self.high = m.get('High')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        return self


class DescribeTaskBriefInfoResponseBodyBriefActionRunsFacet(TeaModel):
    def __init__(
        self,
        completed: int = None,
        total: int = None,
    ):
        self.completed = completed
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeTaskBriefInfoResponseBodyBrief(TeaModel):
    def __init__(
        self,
        finished_at: int = None,
        progress: float = None,
        description: str = None,
        created_at: str = None,
        action_runs_facet: DescribeTaskBriefInfoResponseBodyBriefActionRunsFacet = None,
    ):
        self.finished_at = finished_at
        self.progress = progress
        self.description = description
        self.created_at = created_at
        self.action_runs_facet = action_runs_facet

    def validate(self):
        if self.action_runs_facet:
            self.action_runs_facet.validate()

    def to_map(self):
        result = dict()
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.description is not None:
            result['Description'] = self.description
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.action_runs_facet is not None:
            result['ActionRunsFacet'] = self.action_runs_facet.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('ActionRunsFacet') is not None:
            temp_model = DescribeTaskBriefInfoResponseBodyBriefActionRunsFacet()
            self.action_runs_facet = temp_model.from_map(m['ActionRunsFacet'])
        return self


class DescribeTaskBriefInfoResponseBody(TeaModel):
    def __init__(
        self,
        risks_facets: DescribeTaskBriefInfoResponseBodyRisksFacets = None,
        request_id: str = None,
        brief: DescribeTaskBriefInfoResponseBodyBrief = None,
    ):
        self.risks_facets = risks_facets
        self.request_id = request_id
        self.brief = brief

    def validate(self):
        if self.risks_facets:
            self.risks_facets.validate()
        if self.brief:
            self.brief.validate()

    def to_map(self):
        result = dict()
        if self.risks_facets is not None:
            result['RisksFacets'] = self.risks_facets.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.brief is not None:
            result['Brief'] = self.brief.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RisksFacets') is not None:
            temp_model = DescribeTaskBriefInfoResponseBodyRisksFacets()
            self.risks_facets = temp_model.from_map(m['RisksFacets'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Brief') is not None:
            temp_model = DescribeTaskBriefInfoResponseBodyBrief()
            self.brief = temp_model.from_map(m['Brief'])
        return self


class DescribeTaskBriefInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTaskBriefInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTaskBriefInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserTagsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeUserTagsResponseBodyList(TeaModel):
    def __init__(
        self,
        asset_count: int = None,
        tag_key: str = None,
    ):
        self.asset_count = asset_count
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeUserTagsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_count: int = None,
        current_page: int = None,
        list: List[DescribeUserTagsResponseBodyList] = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_count = page_count
        self.current_page = current_page
        self.list = list
        self.count = count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeUserTagsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeUserTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulnerabilityRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        id: int = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.id = id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeVulnerabilityResponseBodyVulnerability(TeaModel):
    def __init__(
        self,
        severity: int = None,
        status: int = None,
        data: str = None,
        args: str = None,
        owasp: str = None,
        impact: str = None,
        cwe: str = None,
        hostname: str = None,
        reference: str = None,
        wasc: str = None,
        last_discovered_at: int = None,
        description: str = None,
        common_type: str = None,
        solution: str = None,
        name: str = None,
        target: str = None,
        poc: str = None,
        id: int = None,
    ):
        self.severity = severity
        self.status = status
        self.data = data
        self.args = args
        self.owasp = owasp
        self.impact = impact
        self.cwe = cwe
        self.hostname = hostname
        self.reference = reference
        self.wasc = wasc
        self.last_discovered_at = last_discovered_at
        self.description = description
        self.common_type = common_type
        self.solution = solution
        self.name = name
        self.target = target
        self.poc = poc
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.status is not None:
            result['Status'] = self.status
        if self.data is not None:
            result['Data'] = self.data
        if self.args is not None:
            result['Args'] = self.args
        if self.owasp is not None:
            result['Owasp'] = self.owasp
        if self.impact is not None:
            result['Impact'] = self.impact
        if self.cwe is not None:
            result['Cwe'] = self.cwe
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.reference is not None:
            result['Reference'] = self.reference
        if self.wasc is not None:
            result['Wasc'] = self.wasc
        if self.last_discovered_at is not None:
            result['LastDiscoveredAt'] = self.last_discovered_at
        if self.description is not None:
            result['Description'] = self.description
        if self.common_type is not None:
            result['CommonType'] = self.common_type
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.name is not None:
            result['Name'] = self.name
        if self.target is not None:
            result['Target'] = self.target
        if self.poc is not None:
            result['Poc'] = self.poc
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Owasp') is not None:
            self.owasp = m.get('Owasp')
        if m.get('Impact') is not None:
            self.impact = m.get('Impact')
        if m.get('Cwe') is not None:
            self.cwe = m.get('Cwe')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        if m.get('Wasc') is not None:
            self.wasc = m.get('Wasc')
        if m.get('LastDiscoveredAt') is not None:
            self.last_discovered_at = m.get('LastDiscoveredAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CommonType') is not None:
            self.common_type = m.get('CommonType')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Poc') is not None:
            self.poc = m.get('Poc')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeVulnerabilityResponseBody(TeaModel):
    def __init__(
        self,
        impact: str = None,
        args: str = None,
        description: str = None,
        request_id: str = None,
        last_discovered_at: int = None,
        poc: str = None,
        reference: str = None,
        hostname: str = None,
        severity: int = None,
        data: str = None,
        vulnerability: DescribeVulnerabilityResponseBodyVulnerability = None,
        success: bool = None,
        name: str = None,
        target: str = None,
        id: int = None,
        solution: str = None,
    ):
        self.impact = impact
        self.args = args
        self.description = description
        self.request_id = request_id
        self.last_discovered_at = last_discovered_at
        self.poc = poc
        self.reference = reference
        self.hostname = hostname
        self.severity = severity
        self.data = data
        self.vulnerability = vulnerability
        self.success = success
        self.name = name
        self.target = target
        self.id = id
        self.solution = solution

    def validate(self):
        if self.vulnerability:
            self.vulnerability.validate()

    def to_map(self):
        result = dict()
        if self.impact is not None:
            result['Impact'] = self.impact
        if self.args is not None:
            result['Args'] = self.args
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.last_discovered_at is not None:
            result['LastDiscoveredAt'] = self.last_discovered_at
        if self.poc is not None:
            result['Poc'] = self.poc
        if self.reference is not None:
            result['Reference'] = self.reference
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.data is not None:
            result['Data'] = self.data
        if self.vulnerability is not None:
            result['Vulnerability'] = self.vulnerability.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.name is not None:
            result['Name'] = self.name
        if self.target is not None:
            result['Target'] = self.target
        if self.id is not None:
            result['Id'] = self.id
        if self.solution is not None:
            result['Solution'] = self.solution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Impact') is not None:
            self.impact = m.get('Impact')
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LastDiscoveredAt') is not None:
            self.last_discovered_at = m.get('LastDiscoveredAt')
        if m.get('Poc') is not None:
            self.poc = m.get('Poc')
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Vulnerability') is not None:
            temp_model = DescribeVulnerabilityResponseBodyVulnerability()
            self.vulnerability = temp_model.from_map(m['Vulnerability'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        return self


class DescribeVulnerabilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVulnerabilityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulnerabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebPathsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeWebPathsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        extension: str = None,
        site: str = None,
        path: str = None,
        updated_at: int = None,
    ):
        self.index = index
        self.extension = extension
        self.site = site
        self.path = path
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.site is not None:
            result['Site'] = self.site
        if self.path is not None:
            result['Path'] = self.path
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class DescribeWebPathsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribeWebPathsResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeWebPathsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeWebPathsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebPathsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebPathsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebServersRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeWebServersResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        host: str = None,
        scheme: str = None,
        updated_at: int = None,
        port: str = None,
    ):
        self.index = index
        self.host = host
        self.scheme = scheme
        self.updated_at = updated_at
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.host is not None:
            result['Host'] = self.host
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeWebServersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribeWebServersResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeWebServersResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeWebServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebServersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebTechsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: int = None,
        asset: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id
        self.asset = asset
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeWebTechsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        powered_by: str = None,
        version: str = None,
        url: str = None,
        server: str = None,
        updated_at: int = None,
        title: str = None,
        name: str = None,
    ):
        self.index = index
        self.powered_by = powered_by
        self.version = version
        self.url = url
        self.server = server
        self.updated_at = updated_at
        self.title = title
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.powered_by is not None:
            result['PoweredBy'] = self.powered_by
        if self.version is not None:
            result['Version'] = self.version
        if self.url is not None:
            result['URL'] = self.url
        if self.server is not None:
            result['Server'] = self.server
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.title is not None:
            result['Title'] = self.title
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('PoweredBy') is not None:
            self.powered_by = m.get('PoweredBy')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeWebTechsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        records: List[DescribeWebTechsResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeWebTechsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeWebTechsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebTechsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebTechsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditSessionRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        session_id: int = None,
        asset: str = None,
        ttl: int = None,
        login_session: str = None,
    ):
        self.source_ip = source_ip
        self.session_id = session_id
        self.asset = asset
        self.ttl = ttl
        self.login_session = login_session

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.login_session is not None:
            result['LoginSession'] = self.login_session
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('LoginSession') is not None:
            self.login_session = m.get('LoginSession')
        return self


class EditSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditSessionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EditSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVulReportRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        format: str = None,
        lang: str = None,
        task_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.format = format
        self.lang = lang
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.format is not None:
            result['format'] = self.format
        if self.lang is not None:
            result['lang'] = self.lang
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class GenerateVulReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateVulReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateVulReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateVulReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgDNSMapRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_id: int = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.org_id = org_id
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrgDNSMapResponseBodyRecords(TeaModel):
    def __init__(
        self,
        type: str = None,
        index: int = None,
        domain: str = None,
        org_id: int = None,
        subdomain: str = None,
        updated_at: int = None,
        record: str = None,
        id: int = None,
    ):
        self.type = type
        self.index = index
        self.domain = domain
        self.org_id = org_id
        self.subdomain = subdomain
        self.updated_at = updated_at
        self.record = record
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.index is not None:
            result['Index'] = self.index
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.subdomain is not None:
            result['Subdomain'] = self.subdomain
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.record is not None:
            result['Record'] = self.record
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Subdomain') is not None:
            self.subdomain = m.get('Subdomain')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListOrgDNSMapResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListOrgDNSMapResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListOrgDNSMapResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListOrgDNSMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgDNSMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgDNSMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgDomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        org_id: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.org_id = org_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrgDomainsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        domain: str = None,
        org_id: int = None,
        updated_at: int = None,
        id: int = None,
    ):
        self.index = index
        self.domain = domain
        self.org_id = org_id
        self.updated_at = updated_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListOrgDomainsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListOrgDomainsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListOrgDomainsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListOrgDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgHostsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        org_id: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.org_id = org_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrgHostsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        state: str = None,
        org_id: int = None,
        os: str = None,
        hostname: str = None,
        updated_at: int = None,
        ip: str = None,
        id: int = None,
    ):
        self.index = index
        self.state = state
        self.org_id = org_id
        self.os = os
        self.hostname = hostname
        self.updated_at = updated_at
        self.ip = ip
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.state is not None:
            result['State'] = self.state
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.os is not None:
            result['OS'] = self.os
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.ip is not None:
            result['IP'] = self.ip
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OS') is not None:
            self.os = m.get('OS')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListOrgHostsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListOrgHostsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListOrgHostsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListOrgHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgPortsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        org_id: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.org_id = org_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrgPortsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        service: str = None,
        index: int = None,
        fingerprint: str = None,
        version: str = None,
        product: str = None,
        protocol: str = None,
        org_id: int = None,
        updated_at: int = None,
        port: int = None,
        ip: str = None,
        id: int = None,
    ):
        self.service = service
        self.index = index
        self.fingerprint = fingerprint
        self.version = version
        self.product = product
        self.protocol = protocol
        self.org_id = org_id
        self.updated_at = updated_at
        self.port = port
        self.ip = ip
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.index is not None:
            result['Index'] = self.index
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.version is not None:
            result['Version'] = self.version
        if self.product is not None:
            result['Product'] = self.product
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.port is not None:
            result['Port'] = self.port
        if self.ip is not None:
            result['IP'] = self.ip
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListOrgPortsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListOrgPortsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListOrgPortsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListOrgPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgPortsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgRiskyAssetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_id: int = None,
    ):
        self.source_ip = source_ip
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class ListOrgRiskyAssetsResponseBodyAssets(TeaModel):
    def __init__(
        self,
        type: str = None,
        asset: str = None,
        count: int = None,
    ):
        self.type = type
        self.asset = asset
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListOrgRiskyAssetsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        assets: List[ListOrgRiskyAssetsResponseBodyAssets] = None,
        total: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.assets = assets
        self.total = total

    def validate(self):
        if self.assets:
            for k in self.assets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Assets'] = []
        if self.assets is not None:
            for k in self.assets:
                result['Assets'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.assets = []
        if m.get('Assets') is not None:
            for k in m.get('Assets'):
                temp_model = ListOrgRiskyAssetsResponseBodyAssets()
                self.assets.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListOrgRiskyAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgRiskyAssetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgRiskyAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgSubdomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        org_id: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.org_id = org_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrgSubdomainsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        domain: str = None,
        org_id: int = None,
        subdomain: str = None,
        updated_at: int = None,
        id: int = None,
    ):
        self.index = index
        self.domain = domain
        self.org_id = org_id
        self.subdomain = subdomain
        self.updated_at = updated_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.subdomain is not None:
            result['Subdomain'] = self.subdomain
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Subdomain') is not None:
            self.subdomain = m.get('Subdomain')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListOrgSubdomainsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListOrgSubdomainsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListOrgSubdomainsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListOrgSubdomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgSubdomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgSubdomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgVulFacetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        org_id: int = None,
        asset: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.org_id = org_id
        self.asset = asset
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrgVulFacetsResponseBodyVuls(TeaModel):
    def __init__(
        self,
        index: int = None,
        severity: str = None,
        module_id: int = None,
        classification: str = None,
        name: str = None,
        count: int = None,
    ):
        self.index = index
        self.severity = severity
        self.module_id = module_id
        self.classification = classification
        self.name = name
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.module_id is not None:
            result['ModuleID'] = self.module_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.name is not None:
            result['Name'] = self.name
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('ModuleID') is not None:
            self.module_id = m.get('ModuleID')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListOrgVulFacetsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        total: int = None,
        vuls: List[ListOrgVulFacetsResponseBodyVuls] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.total = total
        self.vuls = vuls

    def validate(self):
        if self.vuls:
            for k in self.vuls:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total is not None:
            result['Total'] = self.total
        result['Vuls'] = []
        if self.vuls is not None:
            for k in self.vuls:
                result['Vuls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.vuls = []
        if m.get('Vuls') is not None:
            for k in m.get('Vuls'):
                temp_model = ListOrgVulFacetsResponseBodyVuls()
                self.vuls.append(temp_model.from_map(k))
        return self


class ListOrgVulFacetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgVulFacetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgVulFacetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgWebPathsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        org_id: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.org_id = org_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrgWebPathsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        org_id: int = None,
        site: str = None,
        path: str = None,
        updated_at: int = None,
        id: int = None,
    ):
        self.index = index
        self.org_id = org_id
        self.site = site
        self.path = path
        self.updated_at = updated_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.site is not None:
            result['Site'] = self.site
        if self.path is not None:
            result['Path'] = self.path
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListOrgWebPathsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListOrgWebPathsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListOrgWebPathsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListOrgWebPathsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgWebPathsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgWebPathsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrgWebTechsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        org_id: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.org_id = org_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrgWebTechsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        powered_by: str = None,
        version: str = None,
        org_id: int = None,
        url: str = None,
        server: str = None,
        updated_at: int = None,
        title: str = None,
        name: str = None,
        id: int = None,
    ):
        self.index = index
        self.powered_by = powered_by
        self.version = version
        self.org_id = org_id
        self.url = url
        self.server = server
        self.updated_at = updated_at
        self.title = title
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.powered_by is not None:
            result['PoweredBy'] = self.powered_by
        if self.version is not None:
            result['Version'] = self.version
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.url is not None:
            result['URL'] = self.url
        if self.server is not None:
            result['Server'] = self.server
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.title is not None:
            result['Title'] = self.title
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('PoweredBy') is not None:
            self.powered_by = m.get('PoweredBy')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListOrgWebTechsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListOrgWebTechsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListOrgWebTechsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListOrgWebTechsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrgWebTechsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOrgWebTechsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDNSMapRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserDNSMapResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        type: str = None,
        domain: str = None,
        subdomain: str = None,
        updated_at: int = None,
        record: str = None,
        id: int = None,
    ):
        self.index = index
        self.type = type
        self.domain = domain
        self.subdomain = subdomain
        self.updated_at = updated_at
        self.record = record
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.subdomain is not None:
            result['Subdomain'] = self.subdomain
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.record is not None:
            result['Record'] = self.record
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Subdomain') is not None:
            self.subdomain = m.get('Subdomain')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserDNSMapResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListUserDNSMapResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUserDNSMapResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListUserDNSMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserDNSMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserDNSMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDNSMapHistoriesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        id: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.id = id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.id is not None:
            result['Id'] = self.id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserDNSMapHistoriesResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        type: str = None,
        domain: str = None,
        created_at: int = None,
        subdomain: str = None,
        record: str = None,
        task_id: int = None,
    ):
        self.index = index
        self.type = type
        self.domain = domain
        self.created_at = created_at
        self.subdomain = subdomain
        self.record = record
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.subdomain is not None:
            result['Subdomain'] = self.subdomain
        if self.record is not None:
            result['Record'] = self.record
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Subdomain') is not None:
            self.subdomain = m.get('Subdomain')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListUserDNSMapHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListUserDNSMapHistoriesResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUserDNSMapHistoriesResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListUserDNSMapHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserDNSMapHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserDNSMapHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserDomainsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        domain: str = None,
        updated_at: int = None,
        id: int = None,
    ):
        self.index = index
        self.domain = domain
        self.updated_at = updated_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserDomainsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListUserDomainsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUserDomainsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListUserDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserHostsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserHostsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        os: str = None,
        state: str = None,
        hostname: str = None,
        updated_at: int = None,
        ip: str = None,
        id: int = None,
    ):
        self.index = index
        self.os = os
        self.state = state
        self.hostname = hostname
        self.updated_at = updated_at
        self.ip = ip
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.os is not None:
            result['OS'] = self.os
        if self.state is not None:
            result['State'] = self.state
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.ip is not None:
            result['IP'] = self.ip
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('OS') is not None:
            self.os = m.get('OS')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserHostsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListUserHostsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUserHostsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListUserHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserOrganizationsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserOrganizationsResponseBodyOrganizations(TeaModel):
    def __init__(
        self,
        index: int = None,
        description: str = None,
        org_id: int = None,
        created_at: int = None,
        updated_at: int = None,
        name: str = None,
    ):
        self.index = index
        self.description = description
        self.org_id = org_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.description is not None:
            result['Description'] = self.description
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListUserOrganizationsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        organizations: List[ListUserOrganizationsResponseBodyOrganizations] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.organizations = organizations

    def validate(self):
        if self.organizations:
            for k in self.organizations:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Organizations'] = []
        if self.organizations is not None:
            for k in self.organizations:
                result['Organizations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.organizations = []
        if m.get('Organizations') is not None:
            for k in m.get('Organizations'):
                temp_model = ListUserOrganizationsResponseBodyOrganizations()
                self.organizations.append(temp_model.from_map(k))
        return self


class ListUserOrganizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserOrganizationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserPortsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserPortsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        service: str = None,
        index: int = None,
        fingerprint: str = None,
        version: str = None,
        product: str = None,
        protocol: str = None,
        updated_at: int = None,
        port: int = None,
        ip: str = None,
        id: int = None,
    ):
        self.service = service
        self.index = index
        self.fingerprint = fingerprint
        self.version = version
        self.product = product
        self.protocol = protocol
        self.updated_at = updated_at
        self.port = port
        self.ip = ip
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.index is not None:
            result['Index'] = self.index
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.version is not None:
            result['Version'] = self.version
        if self.product is not None:
            result['Product'] = self.product
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.port is not None:
            result['Port'] = self.port
        if self.ip is not None:
            result['IP'] = self.ip
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserPortsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListUserPortsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUserPortsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListUserPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserPortsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserSubdomainsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserSubdomainsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        domain: str = None,
        subdomain: str = None,
        updated_at: int = None,
        id: int = None,
    ):
        self.index = index
        self.domain = domain
        self.subdomain = subdomain
        self.updated_at = updated_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.subdomain is not None:
            result['Subdomain'] = self.subdomain
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Subdomain') is not None:
            self.subdomain = m.get('Subdomain')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserSubdomainsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListUserSubdomainsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUserSubdomainsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListUserSubdomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserSubdomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserSubdomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserWebPathsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserWebPathsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        site: str = None,
        path: str = None,
        updated_at: int = None,
        id: int = None,
    ):
        self.index = index
        self.site = site
        self.path = path
        self.updated_at = updated_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.site is not None:
            result['Site'] = self.site
        if self.path is not None:
            result['Path'] = self.path
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserWebPathsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListUserWebPathsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUserWebPathsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListUserWebPathsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserWebPathsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserWebPathsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserWebTechsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        search: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.search = search
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.search is not None:
            result['Search'] = self.search
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserWebTechsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        index: int = None,
        powered_by: str = None,
        version: str = None,
        url: str = None,
        server: str = None,
        updated_at: int = None,
        title: str = None,
        name: str = None,
        id: int = None,
    ):
        self.index = index
        self.powered_by = powered_by
        self.version = version
        self.url = url
        self.server = server
        self.updated_at = updated_at
        self.title = title
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.powered_by is not None:
            result['PoweredBy'] = self.powered_by
        if self.version is not None:
            result['Version'] = self.version
        if self.url is not None:
            result['URL'] = self.url
        if self.server is not None:
            result['Server'] = self.server
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.title is not None:
            result['Title'] = self.title
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('PoweredBy') is not None:
            self.powered_by = m.get('PoweredBy')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserWebTechsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        records: List[ListUserWebTechsResponseBodyRecords] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUserWebTechsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListUserWebTechsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserWebTechsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserWebTechsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOrganizationRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        name: str = None,
        description: str = None,
        org_id: int = None,
    ):
        self.source_ip = source_ip
        self.name = name
        self.description = description
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class ModifyOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyOrganizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagAssetsByRecordsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        source: str = None,
        asset_type: str = None,
        tags: List[str] = None,
        record_ids: List[int] = None,
    ):
        self.source_ip = source_ip
        self.source = source
        self.asset_type = asset_type
        self.tags = tags
        self.record_ids = record_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source is not None:
            result['Source'] = self.source
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.record_ids is not None:
            result['RecordIds'] = self.record_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RecordIds') is not None:
            self.record_ids = m.get('RecordIds')
        return self


class TagAssetsByRecordsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagAssetsByRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagAssetsByRecordsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagAssetsByRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagAssetsBySearchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        source: str = None,
        search: str = None,
        asset_type: str = None,
        tags: List[str] = None,
    ):
        self.source_ip = source_ip
        self.source = source
        self.search = search
        self.asset_type = asset_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source is not None:
            result['Source'] = self.source
        if self.search is not None:
            result['Search'] = self.search
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagAssetsBySearchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagAssetsBySearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagAssetsBySearchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagAssetsBySearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


