# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class StopDomainRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        return self


class StopDomainResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class StartDomainRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        return self


class StartDomainResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class AddDomainRequest(TeaModel):
    def __init__(self, security_token=None, version=None, business_type=None, domain=None, live_format=None,
                 slice_domain=None, region=None, demo_urls=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.business_type = business_type  # type: str
        self.domain = domain            # type: str
        self.live_format = live_format  # type: str
        self.slice_domain = slice_domain  # type: str
        self.region = region            # type: str
        self.demo_urls = demo_urls      # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['BusinessType'] = self.business_type
        result['Domain'] = self.domain
        result['LiveFormat'] = self.live_format
        result['SliceDomain'] = self.slice_domain
        result['Region'] = self.region
        result['DemoUrls'] = self.demo_urls
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.business_type = map.get('BusinessType')
        self.domain = map.get('Domain')
        self.live_format = map.get('LiveFormat')
        self.slice_domain = map.get('SliceDomain')
        self.region = map.get('Region')
        self.demo_urls = map.get('DemoUrls')
        return self


class AddDomainResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class GetBalanceTrafficDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, data_interval=None, resource_id=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.data_interval = data_interval  # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['DataInterval'] = self.data_interval
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.data_interval = map.get('DataInterval')
        self.resource_id = map.get('ResourceId')
        return self


class GetBalanceTrafficDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetBalanceTrafficDataResponseDataList
        self.labels = labels            # type: GetBalanceTrafficDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetBalanceTrafficDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetBalanceTrafficDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetBalanceTrafficDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetBalanceTrafficDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetBalanceTrafficDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetBalanceTrafficDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetBalanceTrafficDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetBalanceTrafficDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetBalanceTrafficDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetBalanceTrafficDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class AddPcdnControlRuleRequest(TeaModel):
    def __init__(self, security_token=None, version=None, name=None, region=None, isp_name=None, platform_type=None,
                 business_type=None, market=None, app_version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.name = name                # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.market = market            # type: str
        self.app_version = app_version  # type: str

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
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Name'] = self.name
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['Market'] = self.market
        result['AppVersion'] = self.app_version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.name = map.get('Name')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.market = map.get('Market')
        self.app_version = map.get('AppVersion')
        return self


class AddPcdnControlRuleResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class AddConsumerRequest(TeaModel):
    def __init__(self, security_token=None, version=None, business_type=None, company=None, site=None,
                 requirement=None, mobile=None, ca=None, operator=None, email=None, bandwidth_requirement=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.business_type = business_type  # type: str
        self.company = company          # type: str
        self.site = site                # type: str
        self.requirement = requirement  # type: str
        self.mobile = mobile            # type: str
        self.ca = ca                    # type: str
        self.operator = operator        # type: str
        self.email = email              # type: str
        self.bandwidth_requirement = bandwidth_requirement  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.company, 'company')
        self.validate_required(self.site, 'site')
        self.validate_required(self.requirement, 'requirement')
        self.validate_required(self.mobile, 'mobile')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['BusinessType'] = self.business_type
        result['Company'] = self.company
        result['Site'] = self.site
        result['Requirement'] = self.requirement
        result['Mobile'] = self.mobile
        result['Ca'] = self.ca
        result['Operator'] = self.operator
        result['Email'] = self.email
        result['BandwidthRequirement'] = self.bandwidth_requirement
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.business_type = map.get('BusinessType')
        self.company = map.get('Company')
        self.site = map.get('Site')
        self.requirement = map.get('Requirement')
        self.mobile = map.get('Mobile')
        self.ca = map.get('Ca')
        self.operator = map.get('Operator')
        self.email = map.get('Email')
        self.bandwidth_requirement = map.get('BandwidthRequirement')
        return self


class AddConsumerResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class GetAccessDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None, region=None, isp_name=None,
                 platform_type=None, business_type=None, start_date=None, end_date=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetAccessDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetAccessDataResponseDataList
        self.labels = labels            # type: GetAccessDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetAccessDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetAccessDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetAccessDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetAccessDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetAccessDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetAccessDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetAccessDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetAccessDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetAccessDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetAccessDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class EnablePcdnControlRuleRequest(TeaModel):
    def __init__(self, security_token=None, version=None, resource_id=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.resource_id = map.get('ResourceId')
        return self


class EnablePcdnControlRuleResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class EditPcdnControlRuleRequest(TeaModel):
    def __init__(self, security_token=None, version=None, name=None, resource_id=None, region=None, isp_name=None,
                 platform_type=None, business_type=None, market=None, app_version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.name = name                # type: str
        self.resource_id = resource_id  # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.market = market            # type: str
        self.app_version = app_version  # type: str

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
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Name'] = self.name
        result['ResourceId'] = self.resource_id
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['Market'] = self.market
        result['AppVersion'] = self.app_version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.name = map.get('Name')
        self.resource_id = map.get('ResourceId')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.market = map.get('Market')
        self.app_version = map.get('AppVersion')
        return self


class EditPcdnControlRuleResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class DisablePcdnControlRuleRequest(TeaModel):
    def __init__(self, security_token=None, version=None, resource_id=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.resource_id = map.get('ResourceId')
        return self


class DisablePcdnControlRuleResponse(TeaModel):
    def __init__(self, request_id=None, code=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.resource_id = map.get('ResourceId')
        return self


class DeletePcdnControlRuleRequest(TeaModel):
    def __init__(self, security_token=None, version=None, resource_id=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.resource_id = map.get('ResourceId')
        return self


class DeletePcdnControlRuleResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self


class GetAllPlatformTypesRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetAllPlatformTypesResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetAllPlatformTypesResponseDataList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetAllPlatformTypesResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        return self


class GetAllPlatformTypesResponseDataListUsageData(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code                # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.name = map.get('Name')
        return self


class GetAllPlatformTypesResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetAllPlatformTypesResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetAllPlatformTypesResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetAllMarketsRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetAllMarketsResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetAllMarketsResponseDataList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetAllMarketsResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        return self


class GetAllMarketsResponseDataListUsageData(TeaModel):
    def __init__(self, code=None, market_code=None, market_name=None):
        self.code = code                # type: int
        self.market_code = market_code  # type: str
        self.market_name = market_name  # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.market_code, 'market_code')
        self.validate_required(self.market_name, 'market_name')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['MarketCode'] = self.market_code
        result['MarketName'] = self.market_name
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.market_code = map.get('MarketCode')
        self.market_name = map.get('MarketName')
        return self


class GetAllMarketsResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetAllMarketsResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetAllMarketsResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetAllIspRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetAllIspResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetAllIspResponseDataList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetAllIspResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        return self


class GetAllIspResponseDataListUsageData(TeaModel):
    def __init__(self, name_cn=None, name_en=None, resource_id=None):
        self.name_cn = name_cn          # type: str
        self.name_en = name_en          # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.name_cn, 'name_cn')
        self.validate_required(self.name_en, 'name_en')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['NameCn'] = self.name_cn
        result['NameEn'] = self.name_en
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.name_cn = map.get('NameCn')
        self.name_en = map.get('NameEn')
        self.resource_id = map.get('ResourceId')
        return self


class GetAllIspResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetAllIspResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetAllIspResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetAllAppVersionsRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetAllAppVersionsResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetAllAppVersionsResponseDataList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetAllAppVersionsResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        return self


class GetAllAppVersionsResponseDataListUsageData(TeaModel):
    def __init__(self, code=None, value=None):
        self.code = code                # type: int
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.value = map.get('Value')
        return self


class GetAllAppVersionsResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetAllAppVersionsResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetAllAppVersionsResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetConsumerStatusRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetConsumerStatusResponse(TeaModel):
    def __init__(self, request_id=None, code=None, integreated_mode=None, inservice=None, realtime_monitor=None,
                 live_monitor=None, cdn_url_redirect_flag=None, business_type=None, audit=None, comment=None, created_at=None,
                 updated_at=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.integreated_mode = integreated_mode  # type: int
        self.inservice = inservice      # type: bool
        self.realtime_monitor = realtime_monitor  # type: bool
        self.live_monitor = live_monitor  # type: bool
        self.cdn_url_redirect_flag = cdn_url_redirect_flag  # type: bool
        self.business_type = business_type  # type: bool
        self.audit = audit              # type: int
        self.comment = comment          # type: str
        self.created_at = created_at    # type: str
        self.updated_at = updated_at    # type: str

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['IntegreatedMode'] = self.integreated_mode
        result['Inservice'] = self.inservice
        result['RealtimeMonitor'] = self.realtime_monitor
        result['LiveMonitor'] = self.live_monitor
        result['CdnUrlRedirectFlag'] = self.cdn_url_redirect_flag
        result['BusinessType'] = self.business_type
        result['Audit'] = self.audit
        result['Comment'] = self.comment
        result['CreatedAt'] = self.created_at
        result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.integreated_mode = map.get('IntegreatedMode')
        self.inservice = map.get('Inservice')
        self.realtime_monitor = map.get('RealtimeMonitor')
        self.live_monitor = map.get('LiveMonitor')
        self.cdn_url_redirect_flag = map.get('CdnUrlRedirectFlag')
        self.business_type = map.get('BusinessType')
        self.audit = map.get('Audit')
        self.comment = map.get('Comment')
        self.created_at = map.get('CreatedAt')
        self.updated_at = map.get('UpdatedAt')
        return self


class GetClientsRatioRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetClientsRatioResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetClientsRatioResponseDataList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetClientsRatioResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        return self


class GetClientsRatioResponseDataListUsageData(TeaModel):
    def __init__(self, name=None, rate=None, value=None):
        self.name = name                # type: str
        self.rate = rate                # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Rate'] = self.rate
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.rate = map.get('Rate')
        self.value = map.get('Value')
        return self


class GetClientsRatioResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetClientsRatioResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetClientsRatioResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetBandwidthDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None, region=None, isp_name=None,
                 platform_type=None, business_type=None, start_date=None, end_date=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetBandwidthDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetBandwidthDataResponseDataList
        self.labels = labels            # type: GetBandwidthDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetBandwidthDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetBandwidthDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetBandwidthDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetBandwidthDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetBandwidthDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetBandwidthDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetBandwidthDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetBandwidthDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetBandwidthDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetBandwidthDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class GetBalanceBandwidthDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, data_interval=None, resource_id=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.data_interval = data_interval  # type: int
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['DataInterval'] = self.data_interval
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.data_interval = map.get('DataInterval')
        self.resource_id = map.get('ResourceId')
        return self


class GetBalanceBandwidthDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetBalanceBandwidthDataResponseDataList
        self.labels = labels            # type: GetBalanceBandwidthDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetBalanceBandwidthDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetBalanceBandwidthDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetBalanceBandwidthDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetBalanceBandwidthDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetBalanceBandwidthDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetBalanceBandwidthDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetBalanceBandwidthDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetBalanceBandwidthDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetBalanceBandwidthDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetBalanceBandwidthDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class GetControlRulesRequest(TeaModel):
    def __init__(self, security_token=None, version=None, page=None, page_size=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.page = page                # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Page'] = self.page
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.page = map.get('Page')
        self.page_size = map.get('PageSize')
        return self


class GetControlRulesResponse(TeaModel):
    def __init__(self, request_id=None, code=None, setting_list=None, pager=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.setting_list = setting_list  # type: GetControlRulesResponseSettingList
        self.pager = pager              # type: GetControlRulesResponsePager

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.setting_list is not None:
            result['SettingList'] = self.setting_list.to_map()
        else:
            result['SettingList'] = None
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        else:
            result['Pager'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('SettingList') is not None:
            temp_model = GetControlRulesResponseSettingList()
            self.setting_list = temp_model.from_map(map['SettingList'])
        else:
            self.setting_list = None
        if map.get('Pager') is not None:
            temp_model = GetControlRulesResponsePager()
            self.pager = temp_model.from_map(map['Pager'])
        else:
            self.pager = None
        return self


class GetControlRulesResponseSettingListSetting(TeaModel):
    def __init__(self, platform_type=None, app_version=None, isp_name=None, business_type=None, client_id=None,
                 created_at=None, market_type=None, name=None, onoff=None, usable=None, region=None, resource_id=None,
                 updated_at=None):
        self.platform_type = platform_type  # type: str
        self.app_version = app_version  # type: str
        self.isp_name = isp_name        # type: str
        self.business_type = business_type  # type: str
        self.client_id = client_id      # type: str
        self.created_at = created_at    # type: str
        self.market_type = market_type  # type: str
        self.name = name                # type: str
        self.onoff = onoff              # type: bool
        self.usable = usable            # type: bool
        self.region = region            # type: str
        self.resource_id = resource_id  # type: str
        self.updated_at = updated_at    # type: str

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
        result = {}
        result['PlatformType'] = self.platform_type
        result['AppVersion'] = self.app_version
        result['IspName'] = self.isp_name
        result['BusinessType'] = self.business_type
        result['ClientId'] = self.client_id
        result['CreatedAt'] = self.created_at
        result['MarketType'] = self.market_type
        result['Name'] = self.name
        result['Onoff'] = self.onoff
        result['Usable'] = self.usable
        result['Region'] = self.region
        result['ResourceId'] = self.resource_id
        result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.platform_type = map.get('PlatformType')
        self.app_version = map.get('AppVersion')
        self.isp_name = map.get('IspName')
        self.business_type = map.get('BusinessType')
        self.client_id = map.get('ClientId')
        self.created_at = map.get('CreatedAt')
        self.market_type = map.get('MarketType')
        self.name = map.get('Name')
        self.onoff = map.get('Onoff')
        self.usable = map.get('Usable')
        self.region = map.get('Region')
        self.resource_id = map.get('ResourceId')
        self.updated_at = map.get('UpdatedAt')
        return self


class GetControlRulesResponseSettingList(TeaModel):
    def __init__(self, setting=None):
        self.setting = setting          # type: List[GetControlRulesResponseSettingListSetting]

    def validate(self):
        self.validate_required(self.setting, 'setting')
        if self.setting:
            for k in self.setting:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Setting'] = []
        if self.setting is not None:
            for k in self.setting:
                result['Setting'].append(k.to_map() if k else None)
        else:
            result['Setting'] = None
        return result

    def from_map(self, map={}):
        self.setting = []
        if map.get('Setting') is not None:
            for k in map.get('Setting'):
                temp_model = GetControlRulesResponseSettingListSetting()
                self.setting.append(temp_model.from_map(k))
        else:
            self.setting = None
        return self


class GetControlRulesResponsePager(TeaModel):
    def __init__(self, page=None, total=None, page_size=None):
        self.page = page                # type: int
        self.total = total              # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.page, 'page')
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['Page'] = self.page
        result['Total'] = self.total
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.page = map.get('Page')
        self.total = map.get('Total')
        self.page_size = map.get('PageSize')
        return self


class GetDomainCountRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetDomainCountResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data = data                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.data = map.get('Data')
        return self


class GetCurrentModeRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetCurrentModeResponse(TeaModel):
    def __init__(self, request_id=None, code=None, mode_code=None, padding_mode_code=None, effective_at=None,
                 estimate_bandwidth=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.mode_code = mode_code      # type: int
        self.padding_mode_code = padding_mode_code  # type: int
        self.effective_at = effective_at  # type: int
        self.estimate_bandwidth = estimate_bandwidth  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.mode_code, 'mode_code')
        self.validate_required(self.padding_mode_code, 'padding_mode_code')
        self.validate_required(self.effective_at, 'effective_at')
        self.validate_required(self.estimate_bandwidth, 'estimate_bandwidth')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['ModeCode'] = self.mode_code
        result['PaddingModeCode'] = self.padding_mode_code
        result['EffectiveAt'] = self.effective_at
        result['EstimateBandwidth'] = self.estimate_bandwidth
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.mode_code = map.get('ModeCode')
        self.padding_mode_code = map.get('PaddingModeCode')
        self.effective_at = map.get('EffectiveAt')
        self.estimate_bandwidth = map.get('EstimateBandwidth')
        return self


class GetCoverRateDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None, region=None, isp_name=None,
                 platform_type=None, business_type=None, start_date=None, end_date=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetCoverRateDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetCoverRateDataResponseDataList
        self.labels = labels            # type: GetCoverRateDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetCoverRateDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetCoverRateDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetCoverRateDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetCoverRateDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetCoverRateDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetCoverRateDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetCoverRateDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetCoverRateDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetCoverRateDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetCoverRateDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class GetFeeHistoryRequest(TeaModel):
    def __init__(self, security_token=None, version=None, page=None, page_size=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.page = page                # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Page'] = self.page
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.page = map.get('Page')
        self.page_size = map.get('PageSize')
        return self


class GetFeeHistoryResponse(TeaModel):
    def __init__(self, request_id=None, code=None, fee_list=None, pager=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.fee_list = fee_list        # type: GetFeeHistoryResponseFeeList
        self.pager = pager              # type: GetFeeHistoryResponsePager

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.fee_list is not None:
            result['FeeList'] = self.fee_list.to_map()
        else:
            result['FeeList'] = None
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        else:
            result['Pager'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('FeeList') is not None:
            temp_model = GetFeeHistoryResponseFeeList()
            self.fee_list = temp_model.from_map(map['FeeList'])
        else:
            self.fee_list = None
        if map.get('Pager') is not None:
            temp_model = GetFeeHistoryResponsePager()
            self.pager = temp_model.from_map(map['Pager'])
        else:
            self.pager = None
        return self


class GetFeeHistoryResponseFeeListFee(TeaModel):
    def __init__(self, date=None, mode=None, total_bandwidth=None, level_two_bandwidth=None,
                 level_three_bandwidth=None, total_traffic=None, level_two_traffic=None, level_three_traffic=None, time_span=None,
                 business_type=None, start_date=None, end_date=None, resource_id=None, flow_out=None):
        self.date = date                # type: str
        self.mode = mode                # type: str
        self.total_bandwidth = total_bandwidth  # type: int
        self.level_two_bandwidth = level_two_bandwidth  # type: int
        self.level_three_bandwidth = level_three_bandwidth  # type: int
        self.total_traffic = total_traffic  # type: int
        self.level_two_traffic = level_two_traffic  # type: int
        self.level_three_traffic = level_three_traffic  # type: int
        self.time_span = time_span      # type: str
        self.business_type = business_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.resource_id = resource_id  # type: str
        self.flow_out = flow_out        # type: int

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
        result = {}
        result['Date'] = self.date
        result['Mode'] = self.mode
        result['TotalBandwidth'] = self.total_bandwidth
        result['LevelTwoBandwidth'] = self.level_two_bandwidth
        result['LevelThreeBandwidth'] = self.level_three_bandwidth
        result['TotalTraffic'] = self.total_traffic
        result['LevelTwoTraffic'] = self.level_two_traffic
        result['LevelThreeTraffic'] = self.level_three_traffic
        result['TimeSpan'] = self.time_span
        result['BusinessType'] = self.business_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['ResourceId'] = self.resource_id
        result['FlowOut'] = self.flow_out
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        self.mode = map.get('Mode')
        self.total_bandwidth = map.get('TotalBandwidth')
        self.level_two_bandwidth = map.get('LevelTwoBandwidth')
        self.level_three_bandwidth = map.get('LevelThreeBandwidth')
        self.total_traffic = map.get('TotalTraffic')
        self.level_two_traffic = map.get('LevelTwoTraffic')
        self.level_three_traffic = map.get('LevelThreeTraffic')
        self.time_span = map.get('TimeSpan')
        self.business_type = map.get('BusinessType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.resource_id = map.get('ResourceId')
        self.flow_out = map.get('FlowOut')
        return self


class GetFeeHistoryResponseFeeList(TeaModel):
    def __init__(self, fee=None):
        self.fee = fee                  # type: List[GetFeeHistoryResponseFeeListFee]

    def validate(self):
        self.validate_required(self.fee, 'fee')
        if self.fee:
            for k in self.fee:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Fee'] = []
        if self.fee is not None:
            for k in self.fee:
                result['Fee'].append(k.to_map() if k else None)
        else:
            result['Fee'] = None
        return result

    def from_map(self, map={}):
        self.fee = []
        if map.get('Fee') is not None:
            for k in map.get('Fee'):
                temp_model = GetFeeHistoryResponseFeeListFee()
                self.fee.append(temp_model.from_map(k))
        else:
            self.fee = None
        return self


class GetFeeHistoryResponsePager(TeaModel):
    def __init__(self, page=None, total=None, page_size=None):
        self.page = page                # type: int
        self.total = total              # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.page, 'page')
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['Page'] = self.page
        result['Total'] = self.total
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.page = map.get('Page')
        self.total = map.get('Total')
        self.page_size = map.get('PageSize')
        return self


class GetExpenseSummaryRequest(TeaModel):
    def __init__(self, security_token=None, version=None, start_date=None, end_date=None, domain=None, region=None,
                 isp_name=None, platform_type=None, business_type=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.domain = domain            # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['Domain'] = self.domain
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.domain = map.get('Domain')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        return self


class GetExpenseSummaryResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data = data                # type: GetExpenseSummaryResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('Data') is not None:
            temp_model = GetExpenseSummaryResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetExpenseSummaryResponseData(TeaModel):
    def __init__(self, total_traffic=None, total_uv=None, share_rate=None, cover_rate=None, forecast_fluency=None,
                 top_bandwidth=None):
        self.total_traffic = total_traffic  # type: int
        self.total_uv = total_uv        # type: int
        self.share_rate = share_rate    # type: float
        self.cover_rate = cover_rate    # type: float
        self.forecast_fluency = forecast_fluency  # type: float
        self.top_bandwidth = top_bandwidth  # type: int

    def validate(self):
        self.validate_required(self.total_traffic, 'total_traffic')
        self.validate_required(self.total_uv, 'total_uv')
        self.validate_required(self.share_rate, 'share_rate')
        self.validate_required(self.cover_rate, 'cover_rate')
        self.validate_required(self.forecast_fluency, 'forecast_fluency')
        self.validate_required(self.top_bandwidth, 'top_bandwidth')

    def to_map(self):
        result = {}
        result['TotalTraffic'] = self.total_traffic
        result['TotalUV'] = self.total_uv
        result['ShareRate'] = self.share_rate
        result['CoverRate'] = self.cover_rate
        result['ForecastFluency'] = self.forecast_fluency
        result['TopBandwidth'] = self.top_bandwidth
        return result

    def from_map(self, map={}):
        self.total_traffic = map.get('TotalTraffic')
        self.total_uv = map.get('TotalUV')
        self.share_rate = map.get('ShareRate')
        self.cover_rate = map.get('CoverRate')
        self.forecast_fluency = map.get('ForecastFluency')
        self.top_bandwidth = map.get('TopBandwidth')
        return self


class GetDomainsRequest(TeaModel):
    def __init__(self, security_token=None, version=None, page=None, page_size=None, domain=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.page = page                # type: str
        self.page_size = page_size      # type: str
        self.domain = domain            # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Page'] = self.page
        result['PageSize'] = self.page_size
        result['Domain'] = self.domain
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.page = map.get('Page')
        self.page_size = map.get('PageSize')
        self.domain = map.get('Domain')
        return self


class GetDomainsResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, pager=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetDomainsResponseDataList
        self.pager = pager              # type: GetDomainsResponsePager

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.pager is not None:
            result['Pager'] = self.pager.to_map()
        else:
            result['Pager'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetDomainsResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Pager') is not None:
            temp_model = GetDomainsResponsePager()
            self.pager = temp_model.from_map(map['Pager'])
        else:
            self.pager = None
        return self


class GetDomainsResponseDataListUsageData(TeaModel):
    def __init__(self, resource_id=None, domain=None, business_type=None, status=None, created_at=None,
                 updated_at=None, slice_format=None):
        self.resource_id = resource_id  # type: str
        self.domain = domain            # type: str
        self.business_type = business_type  # type: str
        self.status = status            # type: bool
        self.created_at = created_at    # type: str
        self.updated_at = updated_at    # type: str
        self.slice_format = slice_format  # type: str

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.updated_at, 'updated_at')
        self.validate_required(self.slice_format, 'slice_format')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['Domain'] = self.domain
        result['BusinessType'] = self.business_type
        result['Status'] = self.status
        result['CreatedAt'] = self.created_at
        result['UpdatedAt'] = self.updated_at
        result['SliceFormat'] = self.slice_format
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.domain = map.get('Domain')
        self.business_type = map.get('BusinessType')
        self.status = map.get('Status')
        self.created_at = map.get('CreatedAt')
        self.updated_at = map.get('UpdatedAt')
        self.slice_format = map.get('SliceFormat')
        return self


class GetDomainsResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetDomainsResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetDomainsResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetDomainsResponsePager(TeaModel):
    def __init__(self, page=None, total=None, page_size=None):
        self.page = page                # type: int
        self.total = total              # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.page, 'page')
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['Page'] = self.page
        result['Total'] = self.total
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.page = map.get('Page')
        self.total = map.get('Total')
        self.page_size = map.get('PageSize')
        return self


class GetLogsListRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None, date=None, start_time=None, end_time=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str
        self.date = date                # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        result['Date'] = self.date
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        self.date = map.get('Date')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class GetLogsListResponse(TeaModel):
    def __init__(self, request_id=None, code=None, log_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.log_list = log_list        # type: GetLogsListResponseLogList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.log_list, 'log_list')
        if self.log_list:
            self.log_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.log_list is not None:
            result['LogList'] = self.log_list.to_map()
        else:
            result['LogList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('LogList') is not None:
            temp_model = GetLogsListResponseLogList()
            self.log_list = temp_model.from_map(map['LogList'])
        else:
            self.log_list = None
        return self


class GetLogsListResponseLogListLog(TeaModel):
    def __init__(self, url=None, file_name=None, start_date=None, end_date=None):
        self.url = url                  # type: str
        self.file_name = file_name      # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['Url'] = self.url
        result['FileName'] = self.file_name
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.url = map.get('Url')
        self.file_name = map.get('FileName')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetLogsListResponseLogList(TeaModel):
    def __init__(self, log=None):
        self.log = log                  # type: List[GetLogsListResponseLogListLog]

    def validate(self):
        self.validate_required(self.log, 'log')
        if self.log:
            for k in self.log:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Log'] = []
        if self.log is not None:
            for k in self.log:
                result['Log'].append(k.to_map() if k else None)
        else:
            result['Log'] = None
        return result

    def from_map(self, map={}):
        self.log = []
        if map.get('Log') is not None:
            for k in map.get('Log'):
                temp_model = GetLogsListResponseLogListLog()
                self.log.append(temp_model.from_map(k))
        else:
            self.log = None
        return self


class GetFluencyDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None, region=None, isp_name=None,
                 platform_type=None, business_type=None, start_date=None, end_date=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetFluencyDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetFluencyDataResponseDataList
        self.labels = labels            # type: GetFluencyDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetFluencyDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetFluencyDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetFluencyDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetFluencyDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetFluencyDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetFluencyDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetFluencyDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetFluencyDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetFluencyDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetFluencyDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class GetFirstFrameDelayDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None, region=None, isp_name=None,
                 platform_type=None, business_type=None, start_date=None, end_date=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetFirstFrameDelayDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetFirstFrameDelayDataResponseDataList
        self.labels = labels            # type: GetFirstFrameDelayDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetFirstFrameDelayDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetFirstFrameDelayDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetFirstFrameDelayDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetFirstFrameDelayDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetFirstFrameDelayDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetFirstFrameDelayDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetFirstFrameDelayDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetFirstFrameDelayDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetFirstFrameDelayDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetFirstFrameDelayDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class GetTokenListRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetTokenListResponse(TeaModel):
    def __init__(self, request_id=None, code=None, token_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.token_list = token_list    # type: GetTokenListResponseTokenList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.token_list, 'token_list')
        if self.token_list:
            self.token_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.token_list is not None:
            result['TokenList'] = self.token_list.to_map()
        else:
            result['TokenList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('TokenList') is not None:
            temp_model = GetTokenListResponseTokenList()
            self.token_list = temp_model.from_map(map['TokenList'])
        else:
            self.token_list = None
        return self


class GetTokenListResponseTokenListToken(TeaModel):
    def __init__(self, client_id=None, resource_id=None, platform_name=None, platform_type=None, token=None,
                 created_at=None, updated_at=None):
        self.client_id = client_id      # type: str
        self.resource_id = resource_id  # type: str
        self.platform_name = platform_name  # type: str
        self.platform_type = platform_type  # type: str
        self.token = token              # type: str
        self.created_at = created_at    # type: str
        self.updated_at = updated_at    # type: str

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.platform_name, 'platform_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.token, 'token')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.updated_at, 'updated_at')

    def to_map(self):
        result = {}
        result['ClientId'] = self.client_id
        result['ResourceId'] = self.resource_id
        result['PlatformName'] = self.platform_name
        result['PlatformType'] = self.platform_type
        result['Token'] = self.token
        result['CreatedAt'] = self.created_at
        result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.client_id = map.get('ClientId')
        self.resource_id = map.get('ResourceId')
        self.platform_name = map.get('PlatformName')
        self.platform_type = map.get('PlatformType')
        self.token = map.get('Token')
        self.created_at = map.get('CreatedAt')
        self.updated_at = map.get('UpdatedAt')
        return self


class GetTokenListResponseTokenList(TeaModel):
    def __init__(self, token=None):
        self.token = token              # type: List[GetTokenListResponseTokenListToken]

    def validate(self):
        self.validate_required(self.token, 'token')
        if self.token:
            for k in self.token:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Token'] = []
        if self.token is not None:
            for k in self.token:
                result['Token'].append(k.to_map() if k else None)
        else:
            result['Token'] = None
        return result

    def from_map(self, map={}):
        self.token = []
        if map.get('Token') is not None:
            for k in map.get('Token'):
                temp_model = GetTokenListResponseTokenListToken()
                self.token.append(temp_model.from_map(k))
        else:
            self.token = None
        return self


class GetShareRateDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None, region=None, isp_name=None,
                 platform_type=None, business_type=None, start_date=None, end_date=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetShareRateDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetShareRateDataResponseDataList
        self.labels = labels            # type: GetShareRateDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetShareRateDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetShareRateDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetShareRateDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetShareRateDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetShareRateDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetShareRateDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetShareRateDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetShareRateDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetShareRateDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetShareRateDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class GetTrafficDataRequest(TeaModel):
    def __init__(self, security_token=None, version=None, domain=None, region=None, isp_name=None,
                 platform_type=None, business_type=None, start_date=None, end_date=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str
        self.domain = domain            # type: str
        self.region = region            # type: str
        self.isp_name = isp_name        # type: str
        self.platform_type = platform_type  # type: str
        self.business_type = business_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.region, 'region')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.platform_type, 'platform_type')
        self.validate_required(self.business_type, 'business_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        result['Domain'] = self.domain
        result['Region'] = self.region
        result['IspName'] = self.isp_name
        result['PlatformType'] = self.platform_type
        result['BusinessType'] = self.business_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        self.domain = map.get('Domain')
        self.region = map.get('Region')
        self.isp_name = map.get('IspName')
        self.platform_type = map.get('PlatformType')
        self.business_type = map.get('BusinessType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetTrafficDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None, labels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetTrafficDataResponseDataList
        self.labels = labels            # type: GetTrafficDataResponseLabels

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
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        if self.labels is not None:
            result['Labels'] = self.labels.to_map()
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetTrafficDataResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        if map.get('Labels') is not None:
            temp_model = GetTrafficDataResponseLabels()
            self.labels = temp_model.from_map(map['Labels'])
        else:
            self.labels = None
        return self


class GetTrafficDataResponseDataListUsageDataValues(TeaModel):
    def __init__(self, values=None):
        # Values
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        result['Values'] = self.values
        return result

    def from_map(self, map={}):
        self.values = map.get('Values')
        return self


class GetTrafficDataResponseDataListUsageData(TeaModel):
    def __init__(self, date=None, values=None):
        self.date = date                # type: str
        self.values = values            # type: GetTrafficDataResponseDataListUsageDataValues

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        if map.get('Values') is not None:
            temp_model = GetTrafficDataResponseDataListUsageDataValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class GetTrafficDataResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetTrafficDataResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetTrafficDataResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class GetTrafficDataResponseLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class GetTrafficByRegionRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetTrafficByRegionResponse(TeaModel):
    def __init__(self, request_id=None, code=None, traffic_data_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.traffic_data_list = traffic_data_list  # type: GetTrafficByRegionResponseTrafficDataList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.traffic_data_list, 'traffic_data_list')
        if self.traffic_data_list:
            self.traffic_data_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.traffic_data_list is not None:
            result['TrafficDataList'] = self.traffic_data_list.to_map()
        else:
            result['TrafficDataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('TrafficDataList') is not None:
            temp_model = GetTrafficByRegionResponseTrafficDataList()
            self.traffic_data_list = temp_model.from_map(map['TrafficDataList'])
        else:
            self.traffic_data_list = None
        return self


class GetTrafficByRegionResponseTrafficDataListTrafficData(TeaModel):
    def __init__(self, name=None, traffic=None):
        self.name = name                # type: str
        self.traffic = traffic          # type: int

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.traffic, 'traffic')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Traffic'] = self.traffic
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.traffic = map.get('Traffic')
        return self


class GetTrafficByRegionResponseTrafficDataList(TeaModel):
    def __init__(self, traffic_data=None):
        self.traffic_data = traffic_data  # type: List[GetTrafficByRegionResponseTrafficDataListTrafficData]

    def validate(self):
        self.validate_required(self.traffic_data, 'traffic_data')
        if self.traffic_data:
            for k in self.traffic_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TrafficData'] = []
        if self.traffic_data is not None:
            for k in self.traffic_data:
                result['TrafficData'].append(k.to_map() if k else None)
        else:
            result['TrafficData'] = None
        return result

    def from_map(self, map={}):
        self.traffic_data = []
        if map.get('TrafficData') is not None:
            for k in map.get('TrafficData'):
                temp_model = GetTrafficByRegionResponseTrafficDataListTrafficData()
                self.traffic_data.append(temp_model.from_map(k))
        else:
            self.traffic_data = None
        return self


class GetAllRegionsRequest(TeaModel):
    def __init__(self, security_token=None, version=None):
        self.security_token = security_token  # type: str
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.version = map.get('Version')
        return self


class GetAllRegionsResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_list=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_list = data_list      # type: GetAllRegionsResponseDataList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('DataList') is not None:
            temp_model = GetAllRegionsResponseDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        return self


class GetAllRegionsResponseDataListUsageData(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code                # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.name = map.get('Name')
        return self


class GetAllRegionsResponseDataList(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[GetAllRegionsResponseDataListUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = GetAllRegionsResponseDataListUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


