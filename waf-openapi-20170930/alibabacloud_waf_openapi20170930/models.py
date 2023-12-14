# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AppOpenAckRequest(TeaModel):
    def __init__(
        self,
        ack: str = None,
        app_name: str = None,
        async_method: str = None,
        region: str = None,
        resource_owner_id: int = None,
        service_id: str = None,
    ):
        self.ack = ack
        self.app_name = app_name
        self.async_method = async_method
        self.region = region
        self.resource_owner_id = resource_owner_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ack is not None:
            result['Ack'] = self.ack
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.async_method is not None:
            result['AsyncMethod'] = self.async_method
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ack') is not None:
            self.ack = m.get('Ack')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AsyncMethod') is not None:
            self.async_method = m.get('AsyncMethod')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class AppOpenAckResponseBody(TeaModel):
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


class AppOpenAckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AppOpenAckResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AppOpenAckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainConfigRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
        http_port: str = None,
        http_to_user_ip: int = None,
        https_port: str = None,
        https_redirect: int = None,
        instance_id: str = None,
        is_access_product: int = None,
        is_non_standard_port: int = None,
        load_balancing: int = None,
        protocols: str = None,
        region: str = None,
        resource_owner_id: int = None,
        rs_type: int = None,
        source_ips: str = None,
    ):
        self.caller = caller
        self.domain = domain
        self.http_port = http_port
        self.http_to_user_ip = http_to_user_ip
        self.https_port = https_port
        self.https_redirect = https_redirect
        self.instance_id = instance_id
        self.is_access_product = is_access_product
        self.is_non_standard_port = is_non_standard_port
        self.load_balancing = load_balancing
        self.protocols = protocols
        self.region = region
        self.resource_owner_id = resource_owner_id
        self.rs_type = rs_type
        self.source_ips = source_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.is_non_standard_port is not None:
            result['IsNonStandardPort'] = self.is_non_standard_port
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('IsNonStandardPort') is not None:
            self.is_non_standard_port = m.get('IsNonStandardPort')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        return self


class CreateDomainConfigResponseBody(TeaModel):
    def __init__(
        self,
        cname: str = None,
        request_id: str = None,
    ):
        self.cname = cname
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDomainConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainConfigRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
        instance_id: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.caller = caller
        self.domain = domain
        self.instance_id = instance_id
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDomainConfigResponseBody(TeaModel):
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


class DeleteDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainNamesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.instance_id = instance_id
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDomainNamesResponseBodyDomainNames(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
    ):
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainNamesResponseBody(TeaModel):
    def __init__(
        self,
        domain_names: DescribeDomainNamesResponseBodyDomainNames = None,
        request_id: str = None,
    ):
        self.domain_names = domain_names
        self.request_id = request_id

    def validate(self):
        if self.domain_names:
            self.domain_names.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            temp_model = DescribeDomainNamesResponseBodyDomainNames()
            self.domain_names = temp_model.from_map(m['DomainNames'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainNamesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDomainNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTransferConfigRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.caller = caller
        self.domain = domain
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDomainTransferConfigResponseBody(TeaModel):
    def __init__(
        self,
        cname: str = None,
        http_port: str = None,
        https_port: str = None,
        is_owned: int = None,
        is_waf_active: int = None,
        protocol_type: int = None,
        protocols: str = None,
        request_id: str = None,
        source_ips: str = None,
        waf_affect_mode: int = None,
    ):
        self.cname = cname
        self.http_port = http_port
        self.https_port = https_port
        self.is_owned = is_owned
        self.is_waf_active = is_waf_active
        self.protocol_type = protocol_type
        self.protocols = protocols
        self.request_id = request_id
        self.source_ips = source_ips
        self.waf_affect_mode = waf_affect_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.is_owned is not None:
            result['IsOwned'] = self.is_owned
        if self.is_waf_active is not None:
            result['IsWafActive'] = self.is_waf_active
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.waf_affect_mode is not None:
            result['WafAffectMode'] = self.waf_affect_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('IsOwned') is not None:
            self.is_owned = m.get('IsOwned')
        if m.get('IsWafActive') is not None:
            self.is_waf_active = m.get('IsWafActive')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('WafAffectMode') is not None:
            self.waf_affect_mode = m.get('WafAffectMode')
        return self


class DescribeDomainTransferConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainTransferConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDomainTransferConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        page: int = None,
        page_size: int = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.domain = domain
        self.instance_id = instance_id
        self.page = page
        self.page_size = page_size
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
    ):
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainsResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: DescribeDomainsResponseBodyDomains = None,
        page_info: DescribeDomainsResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.domains = domains
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.domains:
            self.domains.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = DescribeDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('PageInfo') is not None:
            temp_model = DescribeDomainsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHttpsCertInUseRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.domain = domain
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeHttpsCertInUseResponseBody(TeaModel):
    def __init__(
        self,
        cert_content: str = None,
        cert_id: str = None,
        cert_key: str = None,
        cert_name: str = None,
        request_id: str = None,
    ):
        self.cert_content = cert_content
        self.cert_id = cert_id
        self.cert_key = cert_key
        self.cert_name = cert_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_content is not None:
            result['CertContent'] = self.cert_content
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_key is not None:
            result['CertKey'] = self.cert_key
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertContent') is not None:
            self.cert_content = m.get('CertContent')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertKey') is not None:
            self.cert_key = m.get('CertKey')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHttpsCertInUseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHttpsCertInUseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeHttpsCertInUseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNeedUpgradeDomainLimitRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.domain = domain
        self.instance_id = instance_id
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeNeedUpgradeDomainLimitResponseBody(TeaModel):
    def __init__(
        self,
        need_upgrade: bool = None,
        request_id: str = None,
    ):
        self.need_upgrade = need_upgrade
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNeedUpgradeDomainLimitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNeedUpgradeDomainLimitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeNeedUpgradeDomainLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackageRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribePackageResponseBodyRules(TeaModel):
    def __init__(
        self,
        rule: List[str] = None,
    ):
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class DescribePackageResponseBody(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        instance_id: str = None,
        request_id: str = None,
        rules: DescribePackageResponseBodyRules = None,
        version: str = None,
    ):
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.request_id = request_id
        self.rules = rules
        self.version = version

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rules') is not None:
            temp_model = DescribePackageResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQpsRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        end_millisecond: int = None,
        field: List[str] = None,
        instance_id: str = None,
        interval: int = None,
        region: str = None,
        resource_owner_id: int = None,
        start_millisecond: int = None,
    ):
        self.domain = domain
        self.end_millisecond = end_millisecond
        self.field = field
        self.instance_id = instance_id
        self.interval = interval
        self.region = region
        self.resource_owner_id = resource_owner_id
        self.start_millisecond = start_millisecond

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_millisecond is not None:
            result['EndMillisecond'] = self.end_millisecond
        if self.field is not None:
            result['Field'] = self.field
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_millisecond is not None:
            result['StartMillisecond'] = self.start_millisecond
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndMillisecond') is not None:
            self.end_millisecond = m.get('EndMillisecond')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartMillisecond') is not None:
            self.start_millisecond = m.get('StartMillisecond')
        return self


class DescribeQpsResponseBodyItems(TeaModel):
    def __init__(
        self,
        qps: List[str] = None,
    ):
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        return self


class DescribeQpsResponseBodyTimeScope(TeaModel):
    def __init__(
        self,
        end: int = None,
        start: int = None,
        step: int = None,
    ):
        self.end = end
        self.start = start
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeQpsResponseBody(TeaModel):
    def __init__(
        self,
        items: DescribeQpsResponseBodyItems = None,
        request_id: str = None,
        time_scope: DescribeQpsResponseBodyTimeScope = None,
    ):
        self.items = items
        self.request_id = request_id
        self.time_scope = time_scope

    def validate(self):
        if self.items:
            self.items.validate()
        if self.time_scope:
            self.time_scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_scope is not None:
            result['TimeScope'] = self.time_scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeQpsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeScope') is not None:
            temp_model = DescribeQpsResponseBodyTimeScope()
            self.time_scope = temp_model.from_map(m['TimeScope'])
        return self


class DescribeQpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeQpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionStatusRequest(TeaModel):
    def __init__(
        self,
        instance_source: str = None,
        lang: str = None,
        region: str = None,
        source_ip: str = None,
    ):
        self.instance_source = instance_source
        self.lang = lang
        self.region = region
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeRegionStatusResponseBody(TeaModel):
    def __init__(
        self,
        in_debt: int = None,
        pay_type: int = None,
        request_id: str = None,
    ):
        self.in_debt = in_debt
        self.pay_type = pay_type
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRegionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
    ):
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[str] = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTransferConfigInWorkRequest(TeaModel):
    def __init__(
        self,
        check_request_id: str = None,
        domain: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.check_request_id = check_request_id
        self.domain = domain
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_request_id is not None:
            result['CheckRequestId'] = self.check_request_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRequestId') is not None:
            self.check_request_id = m.get('CheckRequestId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeTransferConfigInWorkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        waf_request_id: str = None,
    ):
        self.request_id = request_id
        self.status = status
        self.waf_request_id = waf_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.waf_request_id is not None:
            result['WafRequestId'] = self.waf_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WafRequestId') is not None:
            self.waf_request_id = m.get('WafRequestId')
        return self


class DescribeTransferConfigInWorkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTransferConfigInWorkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeTransferConfigInWorkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQpsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        resource_owner_id: int = None,
        e: int = None,
        f: List[str] = None,
        n: str = None,
        s: int = None,
        x: int = None,
    ):
        self.instance_id = instance_id
        self.region = region
        self.resource_owner_id = resource_owner_id
        self.e = e
        self.f = f
        self.n = n
        self.s = s
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.e is not None:
            result['e'] = self.e
        if self.f is not None:
            result['f'] = self.f
        if self.n is not None:
            result['n'] = self.n
        if self.s is not None:
            result['s'] = self.s
        if self.x is not None:
            result['x'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('e') is not None:
            self.e = m.get('e')
        if m.get('f') is not None:
            self.f = m.get('f')
        if m.get('n') is not None:
            self.n = m.get('n')
        if m.get('s') is not None:
            self.s = m.get('s')
        if m.get('x') is not None:
            self.x = m.get('x')
        return self


class GetQpsResponseBodyItemsQpsData(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetQpsResponseBodyItemsQps(TeaModel):
    def __init__(
        self,
        data: GetQpsResponseBodyItemsQpsData = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetQpsResponseBodyItemsQpsData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetQpsResponseBodyItems(TeaModel):
    def __init__(
        self,
        qps: List[GetQpsResponseBodyItemsQps] = None,
    ):
        self.qps = qps

    def validate(self):
        if self.qps:
            for k in self.qps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Qps'] = []
        if self.qps is not None:
            for k in self.qps:
                result['Qps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qps = []
        if m.get('Qps') is not None:
            for k in m.get('Qps'):
                temp_model = GetQpsResponseBodyItemsQps()
                self.qps.append(temp_model.from_map(k))
        return self


class GetQpsResponseBodyTimeScope(TeaModel):
    def __init__(
        self,
        end: int = None,
        start: int = None,
        step: int = None,
    ):
        self.end = end
        self.start = start
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class GetQpsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        items: GetQpsResponseBodyItems = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time_scope: GetQpsResponseBodyTimeScope = None,
    ):
        self.code = code
        self.items = items
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time_scope = time_scope

    def validate(self):
        if self.items:
            self.items.validate()
        if self.time_scope:
            self.time_scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.time_scope is not None:
            result['timeScope'] = self.time_scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Items') is not None:
            temp_model = GetQpsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('timeScope') is not None:
            temp_model = GetQpsResponseBodyTimeScope()
            self.time_scope = temp_model.from_map(m['timeScope'])
        return self


class GetQpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetQpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQpsTotalRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_owner_id: int = None,
        e: int = None,
        f: List[str] = None,
        instance_id: str = None,
        n: str = None,
        s: int = None,
        x: int = None,
    ):
        self.region = region
        self.resource_owner_id = resource_owner_id
        self.e = e
        self.f = f
        self.instance_id = instance_id
        self.n = n
        self.s = s
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.e is not None:
            result['e'] = self.e
        if self.f is not None:
            result['f'] = self.f
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.n is not None:
            result['n'] = self.n
        if self.s is not None:
            result['s'] = self.s
        if self.x is not None:
            result['x'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('e') is not None:
            self.e = m.get('e')
        if m.get('f') is not None:
            self.f = m.get('f')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('n') is not None:
            self.n = m.get('n')
        if m.get('s') is not None:
            self.s = m.get('s')
        if m.get('x') is not None:
            self.x = m.get('x')
        return self


class GetQpsTotalResponseBodyItemsQpsData(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetQpsTotalResponseBodyItemsQps(TeaModel):
    def __init__(
        self,
        data: GetQpsTotalResponseBodyItemsQpsData = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetQpsTotalResponseBodyItemsQpsData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetQpsTotalResponseBodyItems(TeaModel):
    def __init__(
        self,
        qps: List[GetQpsTotalResponseBodyItemsQps] = None,
    ):
        self.qps = qps

    def validate(self):
        if self.qps:
            for k in self.qps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Qps'] = []
        if self.qps is not None:
            for k in self.qps:
                result['Qps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qps = []
        if m.get('Qps') is not None:
            for k in m.get('Qps'):
                temp_model = GetQpsTotalResponseBodyItemsQps()
                self.qps.append(temp_model.from_map(k))
        return self


class GetQpsTotalResponseBodyTimeScope(TeaModel):
    def __init__(
        self,
        end: int = None,
        start: int = None,
        step: int = None,
    ):
        self.end = end
        self.start = start
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class GetQpsTotalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        items: GetQpsTotalResponseBodyItems = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time_scope: GetQpsTotalResponseBodyTimeScope = None,
    ):
        self.code = code
        self.items = items
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time_scope = time_scope

    def validate(self):
        if self.items:
            self.items.validate()
        if self.time_scope:
            self.time_scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.time_scope is not None:
            result['timeScope'] = self.time_scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Items') is not None:
            temp_model = GetQpsTotalResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('timeScope') is not None:
            temp_model = GetQpsTotalResponseBodyTimeScope()
            self.time_scope = temp_model.from_map(m['timeScope'])
        return self


class GetQpsTotalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQpsTotalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetQpsTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionListRequest(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
    ):
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetRegionListResponseBodyDataRegionInfo(TeaModel):
    def __init__(
        self,
        display: str = None,
        region: str = None,
    ):
        self.display = display
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetRegionListResponseBodyData(TeaModel):
    def __init__(
        self,
        region_info: List[GetRegionListResponseBodyDataRegionInfo] = None,
    ):
        self.region_info = region_info

    def validate(self):
        if self.region_info:
            for k in self.region_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionInfo'] = []
        if self.region_info is not None:
            for k in self.region_info:
                result['RegionInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_info = []
        if m.get('RegionInfo') is not None:
            for k in m.get('RegionInfo'):
                temp_model = GetRegionListResponseBodyDataRegionInfo()
                self.region_info.append(temp_model.from_map(k))
        return self


class GetRegionListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRegionListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRegionListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRegionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegionListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetRegionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCertAndKeyRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        cert: str = None,
        domain: str = None,
        https_cert_id: str = None,
        https_cert_name: str = None,
        key: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.caller = caller
        self.cert = cert
        self.domain = domain
        self.https_cert_id = https_cert_id
        self.https_cert_name = https_cert_name
        self.key = key
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id
        if self.https_cert_name is not None:
            result['HttpsCertName'] = self.https_cert_name
        if self.key is not None:
            result['Key'] = self.key
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')
        if m.get('HttpsCertName') is not None:
            self.https_cert_name = m.get('HttpsCertName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyCertAndKeyResponseBody(TeaModel):
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


class ModifyCertAndKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCertAndKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyCertAndKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainConfigRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
        http_port: str = None,
        http_to_user_ip: int = None,
        https_port: str = None,
        https_redirect: int = None,
        instance_id: str = None,
        is_access_product: int = None,
        is_non_standard_port: int = None,
        load_balancing: int = None,
        protocols: str = None,
        region: str = None,
        resource_owner_id: int = None,
        rs_type: int = None,
        source_ips: str = None,
    ):
        self.caller = caller
        self.domain = domain
        self.http_port = http_port
        self.http_to_user_ip = http_to_user_ip
        self.https_port = https_port
        self.https_redirect = https_redirect
        self.instance_id = instance_id
        self.is_access_product = is_access_product
        self.is_non_standard_port = is_non_standard_port
        self.load_balancing = load_balancing
        self.protocols = protocols
        self.region = region
        self.resource_owner_id = resource_owner_id
        self.rs_type = rs_type
        self.source_ips = source_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.is_non_standard_port is not None:
            result['IsNonStandardPort'] = self.is_non_standard_port
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('IsNonStandardPort') is not None:
            self.is_non_standard_port = m.get('IsNonStandardPort')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        return self


class ModifyDomainConfigResponseBody(TeaModel):
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


class ModifyDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDomainConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainPackageCountRequest(TeaModel):
    def __init__(
        self,
        domain_package_count: int = None,
        instance_id: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.domain_package_count = domain_package_count
        self.instance_id = instance_id
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_package_count is not None:
            result['DomainPackageCount'] = self.domain_package_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainPackageCount') is not None:
            self.domain_package_count = m.get('DomainPackageCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDomainPackageCountResponseBody(TeaModel):
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


class ModifyDomainPackageCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDomainPackageCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyDomainPackageCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWafSwitchRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
        instance_id: str = None,
        region: str = None,
        resource_owner_id: int = None,
        service_on: int = None,
    ):
        self.caller = caller
        self.domain = domain
        self.instance_id = instance_id
        self.region = region
        self.resource_owner_id = resource_owner_id
        self.service_on = service_on

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.service_on is not None:
            result['ServiceOn'] = self.service_on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ServiceOn') is not None:
            self.service_on = m.get('ServiceOn')
        return self


class ModifyWafSwitchResponseBody(TeaModel):
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


class ModifyWafSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyWafSwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyWafSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


