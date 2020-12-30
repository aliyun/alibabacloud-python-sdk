# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddConsumerRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        business_type: str = None,
        company: str = None,
        site: str = None,
        requirement: str = None,
        mobile: str = None,
        ca: str = None,
        operator: str = None,
        email: str = None,
        bandwidth_requirement: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.business_type = business_type
        self.company = company
        self.site = site
        self.requirement = requirement
        self.mobile = mobile
        self.ca = ca
        self.operator = operator
        self.email = email
        self.bandwidth_requirement = bandwidth_requirement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.company is not None:
            result['Company'] = self.company
        if self.site is not None:
            result['Site'] = self.site
        if self.requirement is not None:
            result['Requirement'] = self.requirement
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ca is not None:
            result['Ca'] = self.ca
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.email is not None:
            result['Email'] = self.email
        if self.bandwidth_requirement is not None:
            result['BandwidthRequirement'] = self.bandwidth_requirement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Company') is not None:
            self.company = m.get('Company')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('Requirement') is not None:
            self.requirement = m.get('Requirement')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ca') is not None:
            self.ca = m.get('Ca')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('BandwidthRequirement') is not None:
            self.bandwidth_requirement = m.get('BandwidthRequirement')
        return self


class AddConsumerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddConsumerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddConsumerResponseBody = None,
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
            temp_model = AddConsumerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDomainRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        business_type: str = None,
        domain: str = None,
        live_format: str = None,
        slice_domain: str = None,
        region: str = None,
        demo_urls: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.business_type = business_type
        self.domain = domain
        self.live_format = live_format
        self.slice_domain = slice_domain
        self.region = region
        self.demo_urls = demo_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.live_format is not None:
            result['LiveFormat'] = self.live_format
        if self.slice_domain is not None:
            result['SliceDomain'] = self.slice_domain
        if self.region is not None:
            result['Region'] = self.region
        if self.demo_urls is not None:
            result['DemoUrls'] = self.demo_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('LiveFormat') is not None:
            self.live_format = m.get('LiveFormat')
        if m.get('SliceDomain') is not None:
            self.slice_domain = m.get('SliceDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('DemoUrls') is not None:
            self.demo_urls = m.get('DemoUrls')
        return self


class AddDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDomainResponseBody = None,
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
            temp_model = AddDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPcdnControlRuleRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        name: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        market: str = None,
        app_version: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.name = name
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.market = market
        self.app_version = app_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.market is not None:
            result['Market'] = self.market
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Market') is not None:
            self.market = m.get('Market')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        return self


class AddPcdnControlRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddPcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddPcdnControlRuleResponseBody = None,
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
            temp_model = AddPcdnControlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDomainResponseBody = None,
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePcdnControlRuleRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        resource_id: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DeletePcdnControlRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeletePcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePcdnControlRuleResponseBody = None,
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
            temp_model = DeletePcdnControlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisablePcdnControlRuleRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        resource_id: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DisablePcdnControlRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DisablePcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisablePcdnControlRuleResponseBody = None,
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
            temp_model = DisablePcdnControlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditPcdnControlRuleRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        name: str = None,
        resource_id: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        market: str = None,
        app_version: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.name = name
        self.resource_id = resource_id
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.market = market
        self.app_version = app_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.market is not None:
            result['Market'] = self.market
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Market') is not None:
            self.market = m.get('Market')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        return self


class EditPcdnControlRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class EditPcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditPcdnControlRuleResponseBody = None,
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
            temp_model = EditPcdnControlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnablePcdnControlRuleRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        resource_id: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class EnablePcdnControlRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class EnablePcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnablePcdnControlRuleResponseBody = None,
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
            temp_model = EnablePcdnControlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetAccessDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetAccessDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetAccessDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetAccessDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetAccessDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAccessDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetAccessDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAccessDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAccessDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetAccessDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetAccessDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetAccessDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetAccessDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAccessDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccessDataResponseBody = None,
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
            temp_model = GetAccessDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllAppVersionsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAllAppVersionsResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        value: str = None,
        code: int = None,
    ):
        self.value = value
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAllAppVersionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllAppVersionsResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetAllAppVersionsResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllAppVersionsResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetAllAppVersionsResponseBodyDataList = None,
        request_id: str = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetAllAppVersionsResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAllAppVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllAppVersionsResponseBody = None,
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
            temp_model = GetAllAppVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllIspRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAllIspResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        name_en: str = None,
        name_cn: str = None,
        resource_id: str = None,
    ):
        self.name_en = name_en
        self.name_cn = name_cn
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.name_cn is not None:
            result['NameCn'] = self.name_cn
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('NameCn') is not None:
            self.name_cn = m.get('NameCn')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GetAllIspResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllIspResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetAllIspResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllIspResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetAllIspResponseBodyDataList = None,
        request_id: str = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetAllIspResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAllIspResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllIspResponseBody = None,
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
            temp_model = GetAllIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllMarketsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAllMarketsResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        code: int = None,
        market_code: str = None,
        market_name: str = None,
    ):
        self.code = code
        self.market_code = market_code
        self.market_name = market_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.market_code is not None:
            result['MarketCode'] = self.market_code
        if self.market_name is not None:
            result['MarketName'] = self.market_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MarketCode') is not None:
            self.market_code = m.get('MarketCode')
        if m.get('MarketName') is not None:
            self.market_name = m.get('MarketName')
        return self


class GetAllMarketsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllMarketsResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetAllMarketsResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllMarketsResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetAllMarketsResponseBodyDataList = None,
        request_id: str = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetAllMarketsResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAllMarketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllMarketsResponseBody = None,
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
            temp_model = GetAllMarketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllPlatformTypesRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAllPlatformTypesResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAllPlatformTypesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllPlatformTypesResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetAllPlatformTypesResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllPlatformTypesResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetAllPlatformTypesResponseBodyDataList = None,
        request_id: str = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetAllPlatformTypesResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAllPlatformTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllPlatformTypesResponseBody = None,
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
            temp_model = GetAllPlatformTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllRegionsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAllRegionsResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAllRegionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllRegionsResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetAllRegionsResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllRegionsResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetAllRegionsResponseBodyDataList = None,
        request_id: str = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetAllRegionsResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAllRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllRegionsResponseBody = None,
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
            temp_model = GetAllRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBalanceBandwidthDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        data_interval: int = None,
        resource_id: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.data_interval = data_interval
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GetBalanceBandwidthDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetBalanceBandwidthDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetBalanceBandwidthDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetBalanceBandwidthDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetBalanceBandwidthDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetBalanceBandwidthDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetBalanceBandwidthDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetBalanceBandwidthDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetBalanceBandwidthDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetBalanceBandwidthDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetBalanceBandwidthDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetBalanceBandwidthDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetBalanceBandwidthDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetBalanceBandwidthDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBalanceBandwidthDataResponseBody = None,
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
            temp_model = GetBalanceBandwidthDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBalanceTrafficDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        data_interval: int = None,
        resource_id: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.data_interval = data_interval
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GetBalanceTrafficDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetBalanceTrafficDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetBalanceTrafficDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetBalanceTrafficDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetBalanceTrafficDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetBalanceTrafficDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetBalanceTrafficDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetBalanceTrafficDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetBalanceTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetBalanceTrafficDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetBalanceTrafficDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetBalanceTrafficDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetBalanceTrafficDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetBalanceTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBalanceTrafficDataResponseBody = None,
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
            temp_model = GetBalanceTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBandwidthDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetBandwidthDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetBandwidthDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetBandwidthDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetBandwidthDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetBandwidthDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetBandwidthDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetBandwidthDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetBandwidthDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetBandwidthDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetBandwidthDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetBandwidthDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetBandwidthDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetBandwidthDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetBandwidthDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBandwidthDataResponseBody = None,
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
            temp_model = GetBandwidthDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClientsRatioRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetClientsRatioResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
        rate: str = None,
    ):
        self.value = value
        self.name = name
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class GetClientsRatioResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetClientsRatioResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetClientsRatioResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetClientsRatioResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetClientsRatioResponseBodyDataList = None,
        request_id: str = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetClientsRatioResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetClientsRatioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetClientsRatioResponseBody = None,
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
            temp_model = GetClientsRatioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerStatusRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetConsumerStatusResponseBody(TeaModel):
    def __init__(
        self,
        comment: str = None,
        live_monitor: bool = None,
        audit: int = None,
        request_id: str = None,
        integreated_mode: int = None,
        created_at: str = None,
        cdn_url_redirect_flag: bool = None,
        business_type: str = None,
        inservice: bool = None,
        realtime_monitor: bool = None,
        code: int = None,
        updated_at: str = None,
    ):
        self.comment = comment
        self.live_monitor = live_monitor
        self.audit = audit
        self.request_id = request_id
        self.integreated_mode = integreated_mode
        self.created_at = created_at
        self.cdn_url_redirect_flag = cdn_url_redirect_flag
        self.business_type = business_type
        self.inservice = inservice
        self.realtime_monitor = realtime_monitor
        self.code = code
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.live_monitor is not None:
            result['LiveMonitor'] = self.live_monitor
        if self.audit is not None:
            result['Audit'] = self.audit
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.integreated_mode is not None:
            result['IntegreatedMode'] = self.integreated_mode
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.cdn_url_redirect_flag is not None:
            result['CdnUrlRedirectFlag'] = self.cdn_url_redirect_flag
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.inservice is not None:
            result['Inservice'] = self.inservice
        if self.realtime_monitor is not None:
            result['RealtimeMonitor'] = self.realtime_monitor
        if self.code is not None:
            result['Code'] = self.code
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('LiveMonitor') is not None:
            self.live_monitor = m.get('LiveMonitor')
        if m.get('Audit') is not None:
            self.audit = m.get('Audit')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IntegreatedMode') is not None:
            self.integreated_mode = m.get('IntegreatedMode')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CdnUrlRedirectFlag') is not None:
            self.cdn_url_redirect_flag = m.get('CdnUrlRedirectFlag')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Inservice') is not None:
            self.inservice = m.get('Inservice')
        if m.get('RealtimeMonitor') is not None:
            self.realtime_monitor = m.get('RealtimeMonitor')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class GetConsumerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConsumerStatusResponseBody = None,
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
            temp_model = GetConsumerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetControlRulesRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        page: str = None,
        page_size: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetControlRulesResponseBodySettingListSetting(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        client_id: str = None,
        business_type: str = None,
        usable: bool = None,
        region: str = None,
        platform_type: str = None,
        market_type: str = None,
        onoff: bool = None,
        isp_name: str = None,
        app_version: str = None,
        updated_at: str = None,
        name: str = None,
        resource_id: str = None,
    ):
        self.created_at = created_at
        self.client_id = client_id
        self.business_type = business_type
        self.usable = usable
        self.region = region
        self.platform_type = platform_type
        self.market_type = market_type
        self.onoff = onoff
        self.isp_name = isp_name
        self.app_version = app_version
        self.updated_at = updated_at
        self.name = name
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.usable is not None:
            result['Usable'] = self.usable
        if self.region is not None:
            result['Region'] = self.region
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.market_type is not None:
            result['MarketType'] = self.market_type
        if self.onoff is not None:
            result['Onoff'] = self.onoff
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Usable') is not None:
            self.usable = m.get('Usable')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('MarketType') is not None:
            self.market_type = m.get('MarketType')
        if m.get('Onoff') is not None:
            self.onoff = m.get('Onoff')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GetControlRulesResponseBodySettingList(TeaModel):
    def __init__(
        self,
        setting: List[GetControlRulesResponseBodySettingListSetting] = None,
    ):
        self.setting = setting

    def validate(self):
        if self.setting:
            for k in self.setting:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Setting'] = []
        if self.setting is not None:
            for k in self.setting:
                result['Setting'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.setting = []
        if m.get('Setting') is not None:
            for k in m.get('Setting'):
                temp_model = GetControlRulesResponseBodySettingListSetting()
                self.setting.append(temp_model.from_map(k))
        return self


class GetControlRulesResponseBodyPager(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        total: int = None,
        page: int = None,
    ):
        self.page_size = page_size
        self.total = total
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetControlRulesResponseBody(TeaModel):
    def __init__(
        self,
        setting_list: GetControlRulesResponseBodySettingList = None,
        request_id: str = None,
        pager: GetControlRulesResponseBodyPager = None,
        code: int = None,
    ):
        self.setting_list = setting_list
        self.request_id = request_id
        self.pager = pager
        self.code = code

    def validate(self):
        if self.setting_list:
            self.setting_list.validate()
        if self.pager:
            self.pager.validate()

    def to_map(self):
        result = dict()
        if self.setting_list is not None:
            result['SettingList'] = self.setting_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SettingList') is not None:
            temp_model = GetControlRulesResponseBodySettingList()
            self.setting_list = temp_model.from_map(m['SettingList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Pager') is not None:
            temp_model = GetControlRulesResponseBodyPager()
            self.pager = temp_model.from_map(m['Pager'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetControlRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetControlRulesResponseBody = None,
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
            temp_model = GetControlRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCoverRateDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetCoverRateDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetCoverRateDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetCoverRateDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetCoverRateDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetCoverRateDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetCoverRateDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetCoverRateDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetCoverRateDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetCoverRateDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetCoverRateDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetCoverRateDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetCoverRateDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetCoverRateDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetCoverRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCoverRateDataResponseBody = None,
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
            temp_model = GetCoverRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCurrentModeRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetCurrentModeResponseBody(TeaModel):
    def __init__(
        self,
        mode_code: int = None,
        request_id: str = None,
        padding_mode_code: int = None,
        effective_at: int = None,
        estimate_bandwidth: int = None,
        code: int = None,
    ):
        self.mode_code = mode_code
        self.request_id = request_id
        self.padding_mode_code = padding_mode_code
        self.effective_at = effective_at
        self.estimate_bandwidth = estimate_bandwidth
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mode_code is not None:
            result['ModeCode'] = self.mode_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.padding_mode_code is not None:
            result['PaddingModeCode'] = self.padding_mode_code
        if self.effective_at is not None:
            result['EffectiveAt'] = self.effective_at
        if self.estimate_bandwidth is not None:
            result['EstimateBandwidth'] = self.estimate_bandwidth
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModeCode') is not None:
            self.mode_code = m.get('ModeCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PaddingModeCode') is not None:
            self.padding_mode_code = m.get('PaddingModeCode')
        if m.get('EffectiveAt') is not None:
            self.effective_at = m.get('EffectiveAt')
        if m.get('EstimateBandwidth') is not None:
            self.estimate_bandwidth = m.get('EstimateBandwidth')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetCurrentModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCurrentModeResponseBody = None,
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
            temp_model = GetCurrentModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainCountRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetDomainCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: int = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDomainCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDomainCountResponseBody = None,
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
            temp_model = GetDomainCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        page: str = None,
        page_size: str = None,
        domain: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.page = page
        self.page_size = page_size
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetDomainsResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        status: bool = None,
        domain: str = None,
        slice_format: str = None,
        created_at: str = None,
        updated_at: str = None,
        resource_id: str = None,
        business_type: str = None,
    ):
        self.status = status
        self.domain = domain
        self.slice_format = slice_format
        self.created_at = created_at
        self.updated_at = updated_at
        self.resource_id = resource_id
        self.business_type = business_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.slice_format is not None:
            result['SliceFormat'] = self.slice_format
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SliceFormat') is not None:
            self.slice_format = m.get('SliceFormat')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class GetDomainsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetDomainsResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetDomainsResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetDomainsResponseBodyPager(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        total: int = None,
        page: int = None,
    ):
        self.page_size = page_size
        self.total = total
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetDomainsResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetDomainsResponseBodyDataList = None,
        request_id: str = None,
        pager: GetDomainsResponseBodyPager = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.pager = pager
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.pager:
            self.pager.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetDomainsResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Pager') is not None:
            temp_model = GetDomainsResponseBodyPager()
            self.pager = temp_model.from_map(m['Pager'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDomainsResponseBody = None,
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
            temp_model = GetDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExpenseSummaryRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        start_date: str = None,
        end_date: str = None,
        domain: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.start_date = start_date
        self.end_date = end_date
        self.domain = domain
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class GetExpenseSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        forecast_fluency: float = None,
        top_bandwidth: int = None,
        total_traffic: int = None,
        cover_rate: float = None,
        share_rate: float = None,
        total_uv: int = None,
    ):
        self.forecast_fluency = forecast_fluency
        self.top_bandwidth = top_bandwidth
        self.total_traffic = total_traffic
        self.cover_rate = cover_rate
        self.share_rate = share_rate
        self.total_uv = total_uv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.forecast_fluency is not None:
            result['ForecastFluency'] = self.forecast_fluency
        if self.top_bandwidth is not None:
            result['TopBandwidth'] = self.top_bandwidth
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.cover_rate is not None:
            result['CoverRate'] = self.cover_rate
        if self.share_rate is not None:
            result['ShareRate'] = self.share_rate
        if self.total_uv is not None:
            result['TotalUV'] = self.total_uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForecastFluency') is not None:
            self.forecast_fluency = m.get('ForecastFluency')
        if m.get('TopBandwidth') is not None:
            self.top_bandwidth = m.get('TopBandwidth')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('CoverRate') is not None:
            self.cover_rate = m.get('CoverRate')
        if m.get('ShareRate') is not None:
            self.share_rate = m.get('ShareRate')
        if m.get('TotalUV') is not None:
            self.total_uv = m.get('TotalUV')
        return self


class GetExpenseSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetExpenseSummaryResponseBodyData = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetExpenseSummaryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetExpenseSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExpenseSummaryResponseBody = None,
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
            temp_model = GetExpenseSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeeHistoryRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        page: str = None,
        page_size: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetFeeHistoryResponseBodyFeeListFee(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        time_span: str = None,
        date: str = None,
        start_date: str = None,
        level_three_traffic: int = None,
        mode: str = None,
        total_traffic: int = None,
        business_type: str = None,
        level_two_traffic: int = None,
        level_three_bandwidth: int = None,
        level_two_bandwidth: int = None,
        flow_out: int = None,
        resource_id: str = None,
        total_bandwidth: int = None,
    ):
        self.end_date = end_date
        self.time_span = time_span
        self.date = date
        self.start_date = start_date
        self.level_three_traffic = level_three_traffic
        self.mode = mode
        self.total_traffic = total_traffic
        self.business_type = business_type
        self.level_two_traffic = level_two_traffic
        self.level_three_bandwidth = level_three_bandwidth
        self.level_two_bandwidth = level_two_bandwidth
        self.flow_out = flow_out
        self.resource_id = resource_id
        self.total_bandwidth = total_bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.time_span is not None:
            result['TimeSpan'] = self.time_span
        if self.date is not None:
            result['Date'] = self.date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.level_three_traffic is not None:
            result['LevelThreeTraffic'] = self.level_three_traffic
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.level_two_traffic is not None:
            result['LevelTwoTraffic'] = self.level_two_traffic
        if self.level_three_bandwidth is not None:
            result['LevelThreeBandwidth'] = self.level_three_bandwidth
        if self.level_two_bandwidth is not None:
            result['LevelTwoBandwidth'] = self.level_two_bandwidth
        if self.flow_out is not None:
            result['FlowOut'] = self.flow_out
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.total_bandwidth is not None:
            result['TotalBandwidth'] = self.total_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('TimeSpan') is not None:
            self.time_span = m.get('TimeSpan')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('LevelThreeTraffic') is not None:
            self.level_three_traffic = m.get('LevelThreeTraffic')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('LevelTwoTraffic') is not None:
            self.level_two_traffic = m.get('LevelTwoTraffic')
        if m.get('LevelThreeBandwidth') is not None:
            self.level_three_bandwidth = m.get('LevelThreeBandwidth')
        if m.get('LevelTwoBandwidth') is not None:
            self.level_two_bandwidth = m.get('LevelTwoBandwidth')
        if m.get('FlowOut') is not None:
            self.flow_out = m.get('FlowOut')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TotalBandwidth') is not None:
            self.total_bandwidth = m.get('TotalBandwidth')
        return self


class GetFeeHistoryResponseBodyFeeList(TeaModel):
    def __init__(
        self,
        fee: List[GetFeeHistoryResponseBodyFeeListFee] = None,
    ):
        self.fee = fee

    def validate(self):
        if self.fee:
            for k in self.fee:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Fee'] = []
        if self.fee is not None:
            for k in self.fee:
                result['Fee'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fee = []
        if m.get('Fee') is not None:
            for k in m.get('Fee'):
                temp_model = GetFeeHistoryResponseBodyFeeListFee()
                self.fee.append(temp_model.from_map(k))
        return self


class GetFeeHistoryResponseBodyPager(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        total: int = None,
        page: int = None,
    ):
        self.page_size = page_size
        self.total = total
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetFeeHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        fee_list: GetFeeHistoryResponseBodyFeeList = None,
        pager: GetFeeHistoryResponseBodyPager = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.fee_list = fee_list
        self.pager = pager
        self.code = code

    def validate(self):
        if self.fee_list:
            self.fee_list.validate()
        if self.pager:
            self.pager.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.fee_list is not None:
            result['FeeList'] = self.fee_list.to_map()
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FeeList') is not None:
            temp_model = GetFeeHistoryResponseBodyFeeList()
            self.fee_list = temp_model.from_map(m['FeeList'])
        if m.get('Pager') is not None:
            temp_model = GetFeeHistoryResponseBodyPager()
            self.pager = temp_model.from_map(m['Pager'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetFeeHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFeeHistoryResponseBody = None,
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
            temp_model = GetFeeHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFirstFrameDelayDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetFirstFrameDelayDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetFirstFrameDelayDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetFirstFrameDelayDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetFirstFrameDelayDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetFirstFrameDelayDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetFirstFrameDelayDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetFirstFrameDelayDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetFirstFrameDelayDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetFirstFrameDelayDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetFirstFrameDelayDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetFirstFrameDelayDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetFirstFrameDelayDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetFirstFrameDelayDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetFirstFrameDelayDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFirstFrameDelayDataResponseBody = None,
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
            temp_model = GetFirstFrameDelayDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFluencyDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetFluencyDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetFluencyDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetFluencyDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetFluencyDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetFluencyDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetFluencyDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetFluencyDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetFluencyDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetFluencyDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetFluencyDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetFluencyDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetFluencyDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetFluencyDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetFluencyDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFluencyDataResponseBody = None,
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
            temp_model = GetFluencyDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogsListRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
        date: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.date is not None:
            result['Date'] = self.date
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class GetLogsListResponseBodyLogListLog(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        url: str = None,
        start_date: str = None,
        file_name: str = None,
    ):
        self.end_date = end_date
        self.url = url
        self.start_date = start_date
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.url is not None:
            result['Url'] = self.url
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GetLogsListResponseBodyLogList(TeaModel):
    def __init__(
        self,
        log: List[GetLogsListResponseBodyLogListLog] = None,
    ):
        self.log = log

    def validate(self):
        if self.log:
            for k in self.log:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Log'] = []
        if self.log is not None:
            for k in self.log:
                result['Log'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log = []
        if m.get('Log') is not None:
            for k in m.get('Log'):
                temp_model = GetLogsListResponseBodyLogListLog()
                self.log.append(temp_model.from_map(k))
        return self


class GetLogsListResponseBody(TeaModel):
    def __init__(
        self,
        log_list: GetLogsListResponseBodyLogList = None,
        request_id: str = None,
        code: int = None,
    ):
        self.log_list = log_list
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.log_list:
            self.log_list.validate()

    def to_map(self):
        result = dict()
        if self.log_list is not None:
            result['LogList'] = self.log_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogList') is not None:
            temp_model = GetLogsListResponseBodyLogList()
            self.log_list = temp_model.from_map(m['LogList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetLogsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogsListResponseBody = None,
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
            temp_model = GetLogsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareRateDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetShareRateDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetShareRateDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetShareRateDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetShareRateDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetShareRateDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetShareRateDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetShareRateDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetShareRateDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetShareRateDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetShareRateDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetShareRateDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetShareRateDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetShareRateDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetShareRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetShareRateDataResponseBody = None,
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
            temp_model = GetShareRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenListRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetTokenListResponseBodyTokenListToken(TeaModel):
    def __init__(
        self,
        platform_name: str = None,
        token: str = None,
        platform_type: str = None,
        created_at: str = None,
        updated_at: str = None,
        resource_id: str = None,
        client_id: str = None,
    ):
        self.platform_name = platform_name
        self.token = token
        self.platform_type = platform_type
        self.created_at = created_at
        self.updated_at = updated_at
        self.resource_id = resource_id
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.token is not None:
            result['Token'] = self.token
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class GetTokenListResponseBodyTokenList(TeaModel):
    def __init__(
        self,
        token: List[GetTokenListResponseBodyTokenListToken] = None,
    ):
        self.token = token

    def validate(self):
        if self.token:
            for k in self.token:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Token'] = []
        if self.token is not None:
            for k in self.token:
                result['Token'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.token = []
        if m.get('Token') is not None:
            for k in m.get('Token'):
                temp_model = GetTokenListResponseBodyTokenListToken()
                self.token.append(temp_model.from_map(k))
        return self


class GetTokenListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token_list: GetTokenListResponseBodyTokenList = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.token_list = token_list
        self.code = code

    def validate(self):
        if self.token_list:
            self.token_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token_list is not None:
            result['TokenList'] = self.token_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TokenList') is not None:
            temp_model = GetTokenListResponseBodyTokenList()
            self.token_list = temp_model.from_map(m['TokenList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetTokenListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTokenListResponseBody = None,
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
            temp_model = GetTokenListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrafficByRegionRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetTrafficByRegionResponseBodyTrafficDataListTrafficData(TeaModel):
    def __init__(
        self,
        traffic: int = None,
        name: str = None,
    ):
        self.traffic = traffic
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetTrafficByRegionResponseBodyTrafficDataList(TeaModel):
    def __init__(
        self,
        traffic_data: List[GetTrafficByRegionResponseBodyTrafficDataListTrafficData] = None,
    ):
        self.traffic_data = traffic_data

    def validate(self):
        if self.traffic_data:
            for k in self.traffic_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TrafficData'] = []
        if self.traffic_data is not None:
            for k in self.traffic_data:
                result['TrafficData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_data = []
        if m.get('TrafficData') is not None:
            for k in m.get('TrafficData'):
                temp_model = GetTrafficByRegionResponseBodyTrafficDataListTrafficData()
                self.traffic_data.append(temp_model.from_map(k))
        return self


class GetTrafficByRegionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_data_list: GetTrafficByRegionResponseBodyTrafficDataList = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.traffic_data_list = traffic_data_list
        self.code = code

    def validate(self):
        if self.traffic_data_list:
            self.traffic_data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_data_list is not None:
            result['TrafficDataList'] = self.traffic_data_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficDataList') is not None:
            temp_model = GetTrafficByRegionResponseBodyTrafficDataList()
            self.traffic_data_list = temp_model.from_map(m['TrafficDataList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetTrafficByRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrafficByRegionResponseBody = None,
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
            temp_model = GetTrafficByRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrafficDataRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
        region: str = None,
        isp_name: str = None,
        platform_type: str = None,
        business_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain
        self.region = region
        self.isp_name = isp_name
        self.platform_type = platform_type
        self.business_type = business_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetTrafficDataResponseBodyDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetTrafficDataResponseBodyDataListUsageData(TeaModel):
    def __init__(
        self,
        values: GetTrafficDataResponseBodyDataListUsageDataValues = None,
        date: str = None,
    ):
        self.values = values
        self.date = date

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values.to_map()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            temp_model = GetTrafficDataResponseBodyDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetTrafficDataResponseBodyDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetTrafficDataResponseBodyDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = GetTrafficDataResponseBodyDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetTrafficDataResponseBodyLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        data_list: GetTrafficDataResponseBodyDataList = None,
        request_id: str = None,
        labels: GetTrafficDataResponseBodyLabels = None,
        code: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.labels = labels
        self.code = code

    def validate(self):
        if self.data_list:
            self.data_list.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataList') is not None:
            temp_model = GetTrafficDataResponseBodyDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Labels') is not None:
            temp_model = GetTrafficDataResponseBodyLabels()
            self.labels = temp_model.from_map(m['Labels'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrafficDataResponseBody = None,
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
            temp_model = GetTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDomainRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class StartDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StartDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDomainResponseBody = None,
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
            temp_model = StartDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDomainRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
        domain: str = None,
    ):
        self.security_token = security_token
        self.version = version
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version is not None:
            result['Version'] = self.version
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class StopDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StopDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDomainResponseBody = None,
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
            temp_model = StopDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


