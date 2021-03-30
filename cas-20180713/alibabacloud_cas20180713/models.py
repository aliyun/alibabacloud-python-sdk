# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateDVOrderAuditRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        domain: str = None,
        domain_verify_type: str = None,
        username: str = None,
        email: str = None,
        mobile: str = None,
        province: str = None,
        city: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.domain = domain
        self.domain_verify_type = domain_verify_type
        self.username = username
        self.email = email
        self.mobile = mobile
        self.province = province
        self.city = city

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_verify_type is not None:
            result['DomainVerifyType'] = self.domain_verify_type
        if self.username is not None:
            result['Username'] = self.username
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainVerifyType') is not None:
            self.domain_verify_type = m.get('DomainVerifyType')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        return self


class CreateDVOrderAuditResponseBody(TeaModel):
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


class CreateDVOrderAuditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDVOrderAuditResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDVOrderAuditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserCertificateRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        cert: str = None,
        key: str = None,
        source_ip: str = None,
        lang: str = None,
    ):
        self.name = name
        self.cert = cert
        self.key = key
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.key is not None:
            result['Key'] = self.key
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class CreateUserCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cert_id: int = None,
    ):
        self.request_id = request_id
        self.cert_id = cert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        return self


class CreateUserCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_id: int = None,
        source_ip: str = None,
        lang: str = None,
    ):
        self.cert_id = cert_id
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DeleteUserCertificateResponseBody(TeaModel):
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


class DeleteUserCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDVOrderResultRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDVOrderResultResponseBody(TeaModel):
    def __init__(
        self,
        order_status: str = None,
        check_name: str = None,
        private_key: str = None,
        request_id: str = None,
        check_type: str = None,
        check_value: str = None,
        certificate: str = None,
    ):
        self.order_status = order_status
        self.check_name = check_name
        self.private_key = private_key
        self.request_id = request_id
        self.check_type = check_type
        self.check_value = check_value
        self.certificate = certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_value is not None:
            result['CheckValue'] = self.check_value
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckValue') is not None:
            self.check_value = m.get('CheckValue')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        return self


class DescribeDVOrderResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDVOrderResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDVOrderResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOrderInstanceListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_index: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_index = start_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_index is not None:
            result['StartIndex'] = self.start_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')
        return self


class DescribeOrderInstanceListResponseBodyOrderList(TeaModel):
    def __init__(
        self,
        status: str = None,
        cert_type: str = None,
        instance_id: str = None,
        source: str = None,
        id: int = None,
    ):
        self.status = status
        self.cert_type = cert_type
        self.instance_id = instance_id
        self.source = source
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source is not None:
            result['Source'] = self.source
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeOrderInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        order_list: List[DescribeOrderInstanceListResponseBodyOrderList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.order_list = order_list

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OrderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['OrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.order_list = []
        if m.get('OrderList') is not None:
            for k in m.get('OrderList'):
                temp_model = DescribeOrderInstanceListResponseBodyOrderList()
                self.order_list.append(temp_model.from_map(k))
        return self


class DescribeOrderInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOrderInstanceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOrderInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        cert_id: int = None,
        source_ip: str = None,
        lang: str = None,
    ):
        self.cert_id = cert_id
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUserCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        request_id: str = None,
        issuer: str = None,
        expired: bool = None,
        org_name: str = None,
        city: str = None,
        end_date: str = None,
        province: str = None,
        buy_in_aliyun: bool = None,
        common: str = None,
        name: str = None,
        start_date: str = None,
        sans: str = None,
        country: str = None,
        cert: str = None,
        id: int = None,
        key: str = None,
    ):
        self.fingerprint = fingerprint
        self.request_id = request_id
        self.issuer = issuer
        self.expired = expired
        self.org_name = org_name
        self.city = city
        self.end_date = end_date
        self.province = province
        self.buy_in_aliyun = buy_in_aliyun
        self.common = common
        self.name = name
        self.start_date = start_date
        self.sans = sans
        self.country = country
        self.cert = cert
        self.id = id
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.city is not None:
            result['City'] = self.city
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.province is not None:
            result['Province'] = self.province
        if self.buy_in_aliyun is not None:
            result['BuyInAliyun'] = self.buy_in_aliyun
        if self.common is not None:
            result['Common'] = self.common
        if self.name is not None:
            result['Name'] = self.name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.country is not None:
            result['Country'] = self.country
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.id is not None:
            result['Id'] = self.id
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('BuyInAliyun') is not None:
            self.buy_in_aliyun = m.get('BuyInAliyun')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class DescribeUserCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserCertificateDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserCertificateListRequest(TeaModel):
    def __init__(
        self,
        show_size: int = None,
        current_page: int = None,
        source_ip: str = None,
        lang: str = None,
    ):
        self.show_size = show_size
        self.current_page = current_page
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUserCertificateListResponseBodyCertificateList(TeaModel):
    def __init__(
        self,
        start_date: str = None,
        province: str = None,
        sans: str = None,
        common: str = None,
        id: int = None,
        country: str = None,
        issuer: str = None,
        buy_in_aliyun: bool = None,
        end_date: str = None,
        expired: bool = None,
        fingerprint: str = None,
        name: str = None,
        city: str = None,
        org_name: str = None,
    ):
        self.start_date = start_date
        self.province = province
        self.sans = sans
        self.common = common
        self.id = id
        self.country = country
        self.issuer = issuer
        self.buy_in_aliyun = buy_in_aliyun
        self.end_date = end_date
        self.expired = expired
        self.fingerprint = fingerprint
        self.name = name
        self.city = city
        self.org_name = org_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.province is not None:
            result['province'] = self.province
        if self.sans is not None:
            result['sans'] = self.sans
        if self.common is not None:
            result['common'] = self.common
        if self.id is not None:
            result['id'] = self.id
        if self.country is not None:
            result['country'] = self.country
        if self.issuer is not None:
            result['issuer'] = self.issuer
        if self.buy_in_aliyun is not None:
            result['buyInAliyun'] = self.buy_in_aliyun
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.expired is not None:
            result['expired'] = self.expired
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.name is not None:
            result['name'] = self.name
        if self.city is not None:
            result['city'] = self.city
        if self.org_name is not None:
            result['orgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('sans') is not None:
            self.sans = m.get('sans')
        if m.get('common') is not None:
            self.common = m.get('common')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        if m.get('buyInAliyun') is not None:
            self.buy_in_aliyun = m.get('buyInAliyun')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        return self


class DescribeUserCertificateListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        current_page: int = None,
        certificate_list: List[DescribeUserCertificateListResponseBodyCertificateList] = None,
        show_size: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.current_page = current_page
        self.certificate_list = certificate_list
        self.show_size = show_size

    def validate(self):
        if self.certificate_list:
            for k in self.certificate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k in self.certificate_list:
                result['CertificateList'].append(k.to_map() if k else None)
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k in m.get('CertificateList'):
                temp_model = DescribeUserCertificateListResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k))
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class DescribeUserCertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserCertificateListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


