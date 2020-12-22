# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


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
        self.validate_required(self.version, 'version')
        self.validate_required(self.domain, 'domain')

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


class StopDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.domain, 'domain')

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


class StartDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.domain, 'domain')

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


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.domain, 'domain')

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


class AddDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

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


class GetBalanceTrafficDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetBalanceTrafficDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetBalanceTrafficDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetBalanceTrafficDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetBalanceTrafficDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetBalanceTrafficDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetBalanceTrafficDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetBalanceTrafficDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetBalanceTrafficDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetBalanceTrafficDataResponseDataList = None,
        labels: GetBalanceTrafficDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetBalanceTrafficDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetBalanceTrafficDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.name, 'name')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.market, 'market')
        self.validate_required(self.app_version, 'app_version')

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


class AddPcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


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
        self.validate_required(self.version, 'version')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.company, 'company')
        self.validate_required(self.site, 'site')
        self.validate_required(self.requirement, 'requirement')
        self.validate_required(self.mobile, 'mobile')

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


class AddConsumerResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

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


class GetAccessDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetAccessDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetAccessDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetAccessDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetAccessDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAccessDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetAccessDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAccessDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetAccessDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetAccessDataResponseDataList = None,
        labels: GetAccessDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetAccessDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetAccessDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

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


class EnablePcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.name, 'name')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.market, 'market')
        self.validate_required(self.app_version, 'app_version')

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


class EditPcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

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


class DisablePcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

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


class DeletePcdnControlRuleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
    ):
        self.request_id = request_id
        self.code = code

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

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


class GetAllPlatformTypesRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        version: str = None,
    ):
        self.security_token = security_token
        self.version = version

    def validate(self):
        self.validate_required(self.version, 'version')

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


class GetAllPlatformTypesResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.name, 'name')

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


class GetAllPlatformTypesResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllPlatformTypesResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetAllPlatformTypesResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllPlatformTypesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetAllPlatformTypesResponseDataList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetAllPlatformTypesResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
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
        self.validate_required(self.version, 'version')

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


class GetAllMarketsResponseDataListUsageData(TeaModel):
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
        self.validate_required(self.code, 'code')
        self.validate_required(self.market_code, 'market_code')
        self.validate_required(self.market_name, 'market_name')

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


class GetAllMarketsResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllMarketsResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetAllMarketsResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllMarketsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetAllMarketsResponseDataList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetAllMarketsResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
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
        self.validate_required(self.version, 'version')

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


class GetAllIspResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        name_cn: str = None,
        name_en: str = None,
        resource_id: str = None,
    ):
        self.name_cn = name_cn
        self.name_en = name_en
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.name_cn, 'name_cn')
        self.validate_required(self.name_en, 'name_en')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.name_cn is not None:
            result['NameCn'] = self.name_cn
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameCn') is not None:
            self.name_cn = m.get('NameCn')
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GetAllIspResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllIspResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetAllIspResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllIspResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetAllIspResponseDataList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetAllIspResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
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
        self.validate_required(self.version, 'version')

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


class GetAllAppVersionsResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        code: int = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAllAppVersionsResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllAppVersionsResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetAllAppVersionsResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllAppVersionsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetAllAppVersionsResponseDataList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetAllAppVersionsResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
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
        self.validate_required(self.version, 'version')

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


class GetConsumerStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        integreated_mode: int = None,
        inservice: bool = None,
        realtime_monitor: bool = None,
        live_monitor: bool = None,
        cdn_url_redirect_flag: bool = None,
        business_type: str = None,
        audit: int = None,
        comment: str = None,
        created_at: str = None,
        updated_at: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.integreated_mode = integreated_mode
        self.inservice = inservice
        self.realtime_monitor = realtime_monitor
        self.live_monitor = live_monitor
        self.cdn_url_redirect_flag = cdn_url_redirect_flag
        self.business_type = business_type
        self.audit = audit
        self.comment = comment
        self.created_at = created_at
        self.updated_at = updated_at

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.integreated_mode, 'integreated_mode')
        self.validate_required(self.inservice, 'inservice')
        self.validate_required(self.realtime_monitor, 'realtime_monitor')
        self.validate_required(self.live_monitor, 'live_monitor')
        self.validate_required(self.cdn_url_redirect_flag, 'cdn_url_redirect_flag')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.audit, 'audit')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.updated_at, 'updated_at')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.integreated_mode is not None:
            result['IntegreatedMode'] = self.integreated_mode
        if self.inservice is not None:
            result['Inservice'] = self.inservice
        if self.realtime_monitor is not None:
            result['RealtimeMonitor'] = self.realtime_monitor
        if self.live_monitor is not None:
            result['LiveMonitor'] = self.live_monitor
        if self.cdn_url_redirect_flag is not None:
            result['CdnUrlRedirectFlag'] = self.cdn_url_redirect_flag
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.audit is not None:
            result['Audit'] = self.audit
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IntegreatedMode') is not None:
            self.integreated_mode = m.get('IntegreatedMode')
        if m.get('Inservice') is not None:
            self.inservice = m.get('Inservice')
        if m.get('RealtimeMonitor') is not None:
            self.realtime_monitor = m.get('RealtimeMonitor')
        if m.get('LiveMonitor') is not None:
            self.live_monitor = m.get('LiveMonitor')
        if m.get('CdnUrlRedirectFlag') is not None:
            self.cdn_url_redirect_flag = m.get('CdnUrlRedirectFlag')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Audit') is not None:
            self.audit = m.get('Audit')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
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
        self.validate_required(self.version, 'version')

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


class GetClientsRatioResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        name: str = None,
        rate: str = None,
        value: str = None,
    ):
        self.name = name
        self.rate = rate
        self.value = value

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetClientsRatioResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetClientsRatioResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetClientsRatioResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetClientsRatioResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetClientsRatioResponseDataList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetClientsRatioResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

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


class GetBandwidthDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetBandwidthDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetBandwidthDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetBandwidthDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetBandwidthDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetBandwidthDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetBandwidthDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetBandwidthDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetBandwidthDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetBandwidthDataResponseDataList = None,
        labels: GetBandwidthDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetBandwidthDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetBandwidthDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

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


class GetBalanceBandwidthDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetBalanceBandwidthDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetBalanceBandwidthDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetBalanceBandwidthDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetBalanceBandwidthDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetBalanceBandwidthDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetBalanceBandwidthDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetBalanceBandwidthDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetBalanceBandwidthDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetBalanceBandwidthDataResponseDataList = None,
        labels: GetBalanceBandwidthDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetBalanceBandwidthDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetBalanceBandwidthDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')

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


class GetControlRulesResponseSettingListSetting(TeaModel):
    def __init__(
        self,
        platform_type: str = None,
        app_version: str = None,
        isp_name: str = None,
        business_type: str = None,
        client_id: str = None,
        created_at: str = None,
        market_type: str = None,
        name: str = None,
        onoff: bool = None,
        usable: bool = None,
        region: str = None,
        resource_id: str = None,
        updated_at: str = None,
    ):
        self.platform_type = platform_type
        self.app_version = app_version
        self.isp_name = isp_name
        self.business_type = business_type
        self.client_id = client_id
        self.created_at = created_at
        self.market_type = market_type
        self.name = name
        self.onoff = onoff
        self.usable = usable
        self.region = region
        self.resource_id = resource_id
        self.updated_at = updated_at

    def validate(self):
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.app_version, 'app_version')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.market_type, 'market_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.onoff, 'onoff')
        self.validate_required(self.usable, 'usable')
        self.validate_required(self.region, 'region')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.updated_at, 'updated_at')

    def to_map(self):
        result = dict()
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.market_type is not None:
            result['MarketType'] = self.market_type
        if self.name is not None:
            result['Name'] = self.name
        if self.onoff is not None:
            result['Onoff'] = self.onoff
        if self.usable is not None:
            result['Usable'] = self.usable
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('MarketType') is not None:
            self.market_type = m.get('MarketType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Onoff') is not None:
            self.onoff = m.get('Onoff')
        if m.get('Usable') is not None:
            self.usable = m.get('Usable')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class GetControlRulesResponseSettingList(TeaModel):
    def __init__(
        self,
        setting: List[GetControlRulesResponseSettingListSetting] = None,
    ):
        self.setting = setting

    def validate(self):
        self.validate_required(self.setting, 'setting')
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
                temp_model = GetControlRulesResponseSettingListSetting()
                self.setting.append(temp_model.from_map(k))
        return self


class GetControlRulesResponsePager(TeaModel):
    def __init__(
        self,
        page: int = None,
        total: int = None,
        page_size: int = None,
    ):
        self.page = page
        self.total = total
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.page, 'page')
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.total is not None:
            result['Total'] = self.total
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetControlRulesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        setting_list: GetControlRulesResponseSettingList = None,
        pager: GetControlRulesResponsePager = None,
    ):
        self.request_id = request_id
        self.code = code
        self.setting_list = setting_list
        self.pager = pager

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.setting_list, 'setting_list')
        if self.setting_list:
            self.setting_list.validate()
        self.validate_required(self.pager, 'pager')
        if self.pager:
            self.pager.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.setting_list is not None:
            result['SettingList'] = self.setting_list.to_map()
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SettingList') is not None:
            temp_model = GetControlRulesResponseSettingList()
            self.setting_list = temp_model.from_map(m['SettingList'])
        if m.get('Pager') is not None:
            temp_model = GetControlRulesResponsePager()
            self.pager = temp_model.from_map(m['Pager'])
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
        self.validate_required(self.version, 'version')

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


class GetDomainCountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data: int = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
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
        self.validate_required(self.version, 'version')

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


class GetCurrentModeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        mode_code: int = None,
        padding_mode_code: int = None,
        effective_at: int = None,
        estimate_bandwidth: int = None,
    ):
        self.request_id = request_id
        self.code = code
        self.mode_code = mode_code
        self.padding_mode_code = padding_mode_code
        self.effective_at = effective_at
        self.estimate_bandwidth = estimate_bandwidth

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.mode_code, 'mode_code')
        self.validate_required(self.padding_mode_code, 'padding_mode_code')
        self.validate_required(self.effective_at, 'effective_at')
        self.validate_required(self.estimate_bandwidth, 'estimate_bandwidth')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.mode_code is not None:
            result['ModeCode'] = self.mode_code
        if self.padding_mode_code is not None:
            result['PaddingModeCode'] = self.padding_mode_code
        if self.effective_at is not None:
            result['EffectiveAt'] = self.effective_at
        if self.estimate_bandwidth is not None:
            result['EstimateBandwidth'] = self.estimate_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ModeCode') is not None:
            self.mode_code = m.get('ModeCode')
        if m.get('PaddingModeCode') is not None:
            self.padding_mode_code = m.get('PaddingModeCode')
        if m.get('EffectiveAt') is not None:
            self.effective_at = m.get('EffectiveAt')
        if m.get('EstimateBandwidth') is not None:
            self.estimate_bandwidth = m.get('EstimateBandwidth')
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

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


class GetCoverRateDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetCoverRateDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetCoverRateDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetCoverRateDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetCoverRateDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetCoverRateDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetCoverRateDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetCoverRateDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetCoverRateDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetCoverRateDataResponseDataList = None,
        labels: GetCoverRateDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetCoverRateDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetCoverRateDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')

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


class GetFeeHistoryResponseFeeListFee(TeaModel):
    def __init__(
        self,
        date: str = None,
        mode: str = None,
        total_bandwidth: int = None,
        level_two_bandwidth: int = None,
        level_three_bandwidth: int = None,
        total_traffic: int = None,
        level_two_traffic: int = None,
        level_three_traffic: int = None,
        time_span: str = None,
        business_type: str = None,
        start_date: str = None,
        end_date: str = None,
        resource_id: str = None,
        flow_out: int = None,
    ):
        self.date = date
        self.mode = mode
        self.total_bandwidth = total_bandwidth
        self.level_two_bandwidth = level_two_bandwidth
        self.level_three_bandwidth = level_three_bandwidth
        self.total_traffic = total_traffic
        self.level_two_traffic = level_two_traffic
        self.level_three_traffic = level_three_traffic
        self.time_span = time_span
        self.business_type = business_type
        self.start_date = start_date
        self.end_date = end_date
        self.resource_id = resource_id
        self.flow_out = flow_out

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.total_bandwidth, 'total_bandwidth')
        self.validate_required(self.level_two_bandwidth, 'level_two_bandwidth')
        self.validate_required(self.level_three_bandwidth, 'level_three_bandwidth')
        self.validate_required(self.total_traffic, 'total_traffic')
        self.validate_required(self.level_two_traffic, 'level_two_traffic')
        self.validate_required(self.level_three_traffic, 'level_three_traffic')
        self.validate_required(self.time_span, 'time_span')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.flow_out, 'flow_out')

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.total_bandwidth is not None:
            result['TotalBandwidth'] = self.total_bandwidth
        if self.level_two_bandwidth is not None:
            result['LevelTwoBandwidth'] = self.level_two_bandwidth
        if self.level_three_bandwidth is not None:
            result['LevelThreeBandwidth'] = self.level_three_bandwidth
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.level_two_traffic is not None:
            result['LevelTwoTraffic'] = self.level_two_traffic
        if self.level_three_traffic is not None:
            result['LevelThreeTraffic'] = self.level_three_traffic
        if self.time_span is not None:
            result['TimeSpan'] = self.time_span
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.flow_out is not None:
            result['FlowOut'] = self.flow_out
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('TotalBandwidth') is not None:
            self.total_bandwidth = m.get('TotalBandwidth')
        if m.get('LevelTwoBandwidth') is not None:
            self.level_two_bandwidth = m.get('LevelTwoBandwidth')
        if m.get('LevelThreeBandwidth') is not None:
            self.level_three_bandwidth = m.get('LevelThreeBandwidth')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('LevelTwoTraffic') is not None:
            self.level_two_traffic = m.get('LevelTwoTraffic')
        if m.get('LevelThreeTraffic') is not None:
            self.level_three_traffic = m.get('LevelThreeTraffic')
        if m.get('TimeSpan') is not None:
            self.time_span = m.get('TimeSpan')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('FlowOut') is not None:
            self.flow_out = m.get('FlowOut')
        return self


class GetFeeHistoryResponseFeeList(TeaModel):
    def __init__(
        self,
        fee: List[GetFeeHistoryResponseFeeListFee] = None,
    ):
        self.fee = fee

    def validate(self):
        self.validate_required(self.fee, 'fee')
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
                temp_model = GetFeeHistoryResponseFeeListFee()
                self.fee.append(temp_model.from_map(k))
        return self


class GetFeeHistoryResponsePager(TeaModel):
    def __init__(
        self,
        page: int = None,
        total: int = None,
        page_size: int = None,
    ):
        self.page = page
        self.total = total
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.page, 'page')
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.total is not None:
            result['Total'] = self.total
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetFeeHistoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        fee_list: GetFeeHistoryResponseFeeList = None,
        pager: GetFeeHistoryResponsePager = None,
    ):
        self.request_id = request_id
        self.code = code
        self.fee_list = fee_list
        self.pager = pager

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.fee_list, 'fee_list')
        if self.fee_list:
            self.fee_list.validate()
        self.validate_required(self.pager, 'pager')
        if self.pager:
            self.pager.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.fee_list is not None:
            result['FeeList'] = self.fee_list.to_map()
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FeeList') is not None:
            temp_model = GetFeeHistoryResponseFeeList()
            self.fee_list = temp_model.from_map(m['FeeList'])
        if m.get('Pager') is not None:
            temp_model = GetFeeHistoryResponsePager()
            self.pager = temp_model.from_map(m['Pager'])
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
        self.validate_required(self.version, 'version')

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


class GetExpenseSummaryResponseData(TeaModel):
    def __init__(
        self,
        total_traffic: int = None,
        total_uv: int = None,
        share_rate: float = None,
        cover_rate: float = None,
        forecast_fluency: float = None,
        top_bandwidth: int = None,
    ):
        self.total_traffic = total_traffic
        self.total_uv = total_uv
        self.share_rate = share_rate
        self.cover_rate = cover_rate
        self.forecast_fluency = forecast_fluency
        self.top_bandwidth = top_bandwidth

    def validate(self):
        self.validate_required(self.total_traffic, 'total_traffic')
        self.validate_required(self.total_uv, 'total_uv')
        self.validate_required(self.share_rate, 'share_rate')
        self.validate_required(self.cover_rate, 'cover_rate')
        self.validate_required(self.forecast_fluency, 'forecast_fluency')
        self.validate_required(self.top_bandwidth, 'top_bandwidth')

    def to_map(self):
        result = dict()
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.total_uv is not None:
            result['TotalUV'] = self.total_uv
        if self.share_rate is not None:
            result['ShareRate'] = self.share_rate
        if self.cover_rate is not None:
            result['CoverRate'] = self.cover_rate
        if self.forecast_fluency is not None:
            result['ForecastFluency'] = self.forecast_fluency
        if self.top_bandwidth is not None:
            result['TopBandwidth'] = self.top_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('TotalUV') is not None:
            self.total_uv = m.get('TotalUV')
        if m.get('ShareRate') is not None:
            self.share_rate = m.get('ShareRate')
        if m.get('CoverRate') is not None:
            self.cover_rate = m.get('CoverRate')
        if m.get('ForecastFluency') is not None:
            self.forecast_fluency = m.get('ForecastFluency')
        if m.get('TopBandwidth') is not None:
            self.top_bandwidth = m.get('TopBandwidth')
        return self


class GetExpenseSummaryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data: GetExpenseSummaryResponseData = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetExpenseSummaryResponseData()
            self.data = temp_model.from_map(m['Data'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')

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


class GetDomainsResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        domain: str = None,
        business_type: str = None,
        status: bool = None,
        created_at: str = None,
        updated_at: str = None,
        slice_format: str = None,
    ):
        self.resource_id = resource_id
        self.domain = domain
        self.business_type = business_type
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.slice_format = slice_format

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.updated_at, 'updated_at')
        self.validate_required(self.slice_format, 'slice_format')

    def to_map(self):
        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.status is not None:
            result['Status'] = self.status
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.slice_format is not None:
            result['SliceFormat'] = self.slice_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('SliceFormat') is not None:
            self.slice_format = m.get('SliceFormat')
        return self


class GetDomainsResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetDomainsResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetDomainsResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetDomainsResponsePager(TeaModel):
    def __init__(
        self,
        page: int = None,
        total: int = None,
        page_size: int = None,
    ):
        self.page = page
        self.total = total
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.page, 'page')
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.total is not None:
            result['Total'] = self.total
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetDomainsResponseDataList = None,
        pager: GetDomainsResponsePager = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.pager = pager

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.pager, 'pager')
        if self.pager:
            self.pager.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetDomainsResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Pager') is not None:
            temp_model = GetDomainsResponsePager()
            self.pager = temp_model.from_map(m['Pager'])
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
        self.validate_required(self.version, 'version')

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


class GetLogsListResponseLogListLog(TeaModel):
    def __init__(
        self,
        url: str = None,
        file_name: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.url = url
        self.file_name = file_name
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetLogsListResponseLogList(TeaModel):
    def __init__(
        self,
        log: List[GetLogsListResponseLogListLog] = None,
    ):
        self.log = log

    def validate(self):
        self.validate_required(self.log, 'log')
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
                temp_model = GetLogsListResponseLogListLog()
                self.log.append(temp_model.from_map(k))
        return self


class GetLogsListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        log_list: GetLogsListResponseLogList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.log_list = log_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.log_list, 'log_list')
        if self.log_list:
            self.log_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.log_list is not None:
            result['LogList'] = self.log_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogList') is not None:
            temp_model = GetLogsListResponseLogList()
            self.log_list = temp_model.from_map(m['LogList'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

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


class GetFluencyDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetFluencyDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetFluencyDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetFluencyDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetFluencyDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetFluencyDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetFluencyDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetFluencyDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetFluencyDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetFluencyDataResponseDataList = None,
        labels: GetFluencyDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetFluencyDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetFluencyDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

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


class GetFirstFrameDelayDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetFirstFrameDelayDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetFirstFrameDelayDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetFirstFrameDelayDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetFirstFrameDelayDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetFirstFrameDelayDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetFirstFrameDelayDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetFirstFrameDelayDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetFirstFrameDelayDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetFirstFrameDelayDataResponseDataList = None,
        labels: GetFirstFrameDelayDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetFirstFrameDelayDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetFirstFrameDelayDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')

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


class GetTokenListResponseTokenListToken(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        resource_id: str = None,
        platform_name: str = None,
        platform_type: str = None,
        token: str = None,
        created_at: str = None,
        updated_at: str = None,
    ):
        self.client_id = client_id
        self.resource_id = resource_id
        self.platform_name = platform_name
        self.platform_type = platform_type
        self.token = token
        self.created_at = created_at
        self.updated_at = updated_at

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.platform_name, 'platform_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.token, 'token')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.updated_at, 'updated_at')

    def to_map(self):
        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.token is not None:
            result['Token'] = self.token
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class GetTokenListResponseTokenList(TeaModel):
    def __init__(
        self,
        token: List[GetTokenListResponseTokenListToken] = None,
    ):
        self.token = token

    def validate(self):
        self.validate_required(self.token, 'token')
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
                temp_model = GetTokenListResponseTokenListToken()
                self.token.append(temp_model.from_map(k))
        return self


class GetTokenListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        token_list: GetTokenListResponseTokenList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.token_list = token_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.token_list, 'token_list')
        if self.token_list:
            self.token_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.token_list is not None:
            result['TokenList'] = self.token_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TokenList') is not None:
            temp_model = GetTokenListResponseTokenList()
            self.token_list = temp_model.from_map(m['TokenList'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

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


class GetShareRateDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetShareRateDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetShareRateDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetShareRateDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetShareRateDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetShareRateDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetShareRateDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetShareRateDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetShareRateDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetShareRateDataResponseDataList = None,
        labels: GetShareRateDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetShareRateDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetShareRateDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

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


class GetTrafficDataResponseDataListUsageDataValues(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        # Values
        self.values = values

    def validate(self):
        self.validate_required(self.values, 'values')

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


class GetTrafficDataResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        date: str = None,
        values: GetTrafficDataResponseDataListUsageDataValues = None,
    ):
        self.date = date
        self.values = values

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Values') is not None:
            temp_model = GetTrafficDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class GetTrafficDataResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetTrafficDataResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetTrafficDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetTrafficDataResponseLabels(TeaModel):
    def __init__(
        self,
        label: List[str] = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

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


class GetTrafficDataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetTrafficDataResponseDataList = None,
        labels: GetTrafficDataResponseLabels = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list
        self.labels = labels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetTrafficDataResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        if m.get('Labels') is not None:
            temp_model = GetTrafficDataResponseLabels()
            self.labels = temp_model.from_map(m['Labels'])
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
        self.validate_required(self.version, 'version')

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


class GetTrafficByRegionResponseTrafficDataListTrafficData(TeaModel):
    def __init__(
        self,
        name: str = None,
        traffic: int = None,
    ):
        self.name = name
        self.traffic = traffic

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.traffic, 'traffic')

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class GetTrafficByRegionResponseTrafficDataList(TeaModel):
    def __init__(
        self,
        traffic_data: List[GetTrafficByRegionResponseTrafficDataListTrafficData] = None,
    ):
        self.traffic_data = traffic_data

    def validate(self):
        self.validate_required(self.traffic_data, 'traffic_data')
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
                temp_model = GetTrafficByRegionResponseTrafficDataListTrafficData()
                self.traffic_data.append(temp_model.from_map(k))
        return self


class GetTrafficByRegionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        traffic_data_list: GetTrafficByRegionResponseTrafficDataList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.traffic_data_list = traffic_data_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.traffic_data_list, 'traffic_data_list')
        if self.traffic_data_list:
            self.traffic_data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.traffic_data_list is not None:
            result['TrafficDataList'] = self.traffic_data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TrafficDataList') is not None:
            temp_model = GetTrafficByRegionResponseTrafficDataList()
            self.traffic_data_list = temp_model.from_map(m['TrafficDataList'])
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
        self.validate_required(self.version, 'version')

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


class GetAllRegionsResponseDataListUsageData(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.name, 'name')

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


class GetAllRegionsResponseDataList(TeaModel):
    def __init__(
        self,
        usage_data: List[GetAllRegionsResponseDataListUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
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
                temp_model = GetAllRegionsResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class GetAllRegionsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data_list: GetAllRegionsResponseDataList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data_list = data_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataList') is not None:
            temp_model = GetAllRegionsResponseDataList()
            self.data_list = temp_model.from_map(m['DataList'])
        return self


