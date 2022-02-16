# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateSSLCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        private_key: str = None,
    ):
        self.certificate = certificate
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        return self


class CreateSSLCertificateResponseBody(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        request_id: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSSLCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSSLCertificateResponseBody = None,
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
            temp_model = CreateSSLCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSSLCertificateWithNameRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        certificate: str = None,
        private_key: str = None,
    ):
        self.cert_name = cert_name
        self.certificate = certificate
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        return self


class CreateSSLCertificateWithNameResponseBody(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        request_id: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSSLCertificateWithNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSSLCertificateWithNameResponseBody = None,
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
            temp_model = CreateSSLCertificateWithNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSSLCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
    ):
        self.cert_identifier = cert_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        return self


class DeleteSSLCertificateResponseBody(TeaModel):
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


class DeleteSSLCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSSLCertificateResponseBody = None,
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
            temp_model = DeleteSSLCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSSLCertificateCountRequest(TeaModel):
    def __init__(
        self,
        search_value: str = None,
    ):
        self.search_value = search_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        return self


class DescribeSSLCertificateCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSSLCertificateCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSSLCertificateCountResponseBody = None,
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
            temp_model = DescribeSSLCertificateCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSSLCertificateListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        search_value: str = None,
        show_size: int = None,
    ):
        self.current_page = current_page
        self.search_value = search_value
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class DescribeSSLCertificateListResponseBodyCertMetaList(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        issuer: str = None,
        key_size: int = None,
        md_5: str = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
    ):
        self.after_date = after_date
        self.algorithm = algorithm
        self.before_date = before_date
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common_name = common_name
        self.issuer = issuer
        self.key_size = key_size
        self.md_5 = md_5
        self.sans = sans
        self.serial_no = serial_no
        self.sha_2 = sha_2
        self.sign_algorithm = sign_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        return self


class DescribeSSLCertificateListResponseBody(TeaModel):
    def __init__(
        self,
        cert_meta_list: List[DescribeSSLCertificateListResponseBodyCertMetaList] = None,
        current_page: int = None,
        page_count: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        self.cert_meta_list = cert_meta_list
        self.current_page = current_page
        self.page_count = page_count
        self.request_id = request_id
        self.show_size = show_size
        self.total_count = total_count

    def validate(self):
        if self.cert_meta_list:
            for k in self.cert_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertMetaList'] = []
        if self.cert_meta_list is not None:
            for k in self.cert_meta_list:
                result['CertMetaList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_meta_list = []
        if m.get('CertMetaList') is not None:
            for k in m.get('CertMetaList'):
                temp_model = DescribeSSLCertificateListResponseBodyCertMetaList()
                self.cert_meta_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSSLCertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSSLCertificateListResponseBody = None,
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
            temp_model = DescribeSSLCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSSLCertificateMatchDomainListRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        current_page: int = None,
        domain: str = None,
        match_type: str = None,
        show_size: int = None,
    ):
        self.algorithm = algorithm
        self.current_page = current_page
        self.domain = domain
        self.match_type = match_type
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class DescribeSSLCertificateMatchDomainListResponseBodyCertMetaList(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        domain_match_cert: bool = None,
        issuer: str = None,
        key_size: int = None,
        md_5: str = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
    ):
        self.after_date = after_date
        self.algorithm = algorithm
        self.before_date = before_date
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common_name = common_name
        self.domain_match_cert = domain_match_cert
        self.issuer = issuer
        self.key_size = key_size
        self.md_5 = md_5
        self.sans = sans
        self.serial_no = serial_no
        self.sha_2 = sha_2
        self.sign_algorithm = sign_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.domain_match_cert is not None:
            result['DomainMatchCert'] = self.domain_match_cert
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('DomainMatchCert') is not None:
            self.domain_match_cert = m.get('DomainMatchCert')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        return self


class DescribeSSLCertificateMatchDomainListResponseBody(TeaModel):
    def __init__(
        self,
        cert_meta_list: List[DescribeSSLCertificateMatchDomainListResponseBodyCertMetaList] = None,
        current_page: int = None,
        page_count: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        self.cert_meta_list = cert_meta_list
        self.current_page = current_page
        self.page_count = page_count
        self.request_id = request_id
        self.show_size = show_size
        self.total_count = total_count

    def validate(self):
        if self.cert_meta_list:
            for k in self.cert_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertMetaList'] = []
        if self.cert_meta_list is not None:
            for k in self.cert_meta_list:
                result['CertMetaList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_meta_list = []
        if m.get('CertMetaList') is not None:
            for k in m.get('CertMetaList'):
                temp_model = DescribeSSLCertificateMatchDomainListResponseBodyCertMetaList()
                self.cert_meta_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSSLCertificateMatchDomainListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSSLCertificateMatchDomainListResponseBody = None,
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
            temp_model = DescribeSSLCertificateMatchDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSSLCertificatePrivateKeyRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        encrypted_code: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.encrypted_code = encrypted_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.encrypted_code is not None:
            result['EncryptedCode'] = self.encrypted_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('EncryptedCode') is not None:
            self.encrypted_code = m.get('EncryptedCode')
        return self


class DescribeSSLCertificatePrivateKeyResponseBody(TeaModel):
    def __init__(
        self,
        encrypt_private_key: str = None,
        request_id: str = None,
        sign_private_key: str = None,
        x_509private_key: str = None,
    ):
        self.encrypt_private_key = encrypt_private_key
        self.request_id = request_id
        self.sign_private_key = sign_private_key
        self.x_509private_key = x_509private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_private_key is not None:
            result['EncryptPrivateKey'] = self.encrypt_private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_private_key is not None:
            result['SignPrivateKey'] = self.sign_private_key
        if self.x_509private_key is not None:
            result['X509PrivateKey'] = self.x_509private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptPrivateKey') is not None:
            self.encrypt_private_key = m.get('EncryptPrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignPrivateKey') is not None:
            self.sign_private_key = m.get('SignPrivateKey')
        if m.get('X509PrivateKey') is not None:
            self.x_509private_key = m.get('X509PrivateKey')
        return self


class DescribeSSLCertificatePrivateKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSSLCertificatePrivateKeyResponseBody = None,
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
            temp_model = DescribeSSLCertificatePrivateKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSSLCertificatePublicKeyDetailRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
    ):
        self.cert_identifier = cert_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        return self


class DescribeSSLCertificatePublicKeyDetailResponseBodyCertificateInfo(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        issuer: str = None,
        key_size: int = None,
        md_5: str = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
    ):
        self.after_date = after_date
        self.algorithm = algorithm
        self.before_date = before_date
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common_name = common_name
        self.issuer = issuer
        self.key_size = key_size
        self.md_5 = md_5
        self.sans = sans
        self.serial_no = serial_no
        self.sha_2 = sha_2
        self.sign_algorithm = sign_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        return self


class DescribeSSLCertificatePublicKeyDetailResponseBody(TeaModel):
    def __init__(
        self,
        certificate_info: DescribeSSLCertificatePublicKeyDetailResponseBodyCertificateInfo = None,
        encrypt_certificate: str = None,
        request_id: str = None,
        sign_certificate: str = None,
        x_509certificate: str = None,
    ):
        self.certificate_info = certificate_info
        self.encrypt_certificate = encrypt_certificate
        self.request_id = request_id
        self.sign_certificate = sign_certificate
        self.x_509certificate = x_509certificate

    def validate(self):
        if self.certificate_info:
            self.certificate_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_info is not None:
            result['CertificateInfo'] = self.certificate_info.to_map()
        if self.encrypt_certificate is not None:
            result['EncryptCertificate'] = self.encrypt_certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_certificate is not None:
            result['SignCertificate'] = self.sign_certificate
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateInfo') is not None:
            temp_model = DescribeSSLCertificatePublicKeyDetailResponseBodyCertificateInfo()
            self.certificate_info = temp_model.from_map(m['CertificateInfo'])
        if m.get('EncryptCertificate') is not None:
            self.encrypt_certificate = m.get('EncryptCertificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignCertificate') is not None:
            self.sign_certificate = m.get('SignCertificate')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class DescribeSSLCertificatePublicKeyDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSSLCertificatePublicKeyDetailResponseBody = None,
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
            temp_model = DescribeSSLCertificatePublicKeyDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadSSLCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        certificate: str = None,
        encrypt_certificate: str = None,
        encrypt_private_key: str = None,
        private_key: str = None,
        sign_certificate: str = None,
        sign_private_key: str = None,
    ):
        self.cert_name = cert_name
        self.certificate = certificate
        self.encrypt_certificate = encrypt_certificate
        self.encrypt_private_key = encrypt_private_key
        self.private_key = private_key
        self.sign_certificate = sign_certificate
        self.sign_private_key = sign_private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.encrypt_certificate is not None:
            result['EncryptCertificate'] = self.encrypt_certificate
        if self.encrypt_private_key is not None:
            result['EncryptPrivateKey'] = self.encrypt_private_key
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.sign_certificate is not None:
            result['SignCertificate'] = self.sign_certificate
        if self.sign_private_key is not None:
            result['SignPrivateKey'] = self.sign_private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('EncryptCertificate') is not None:
            self.encrypt_certificate = m.get('EncryptCertificate')
        if m.get('EncryptPrivateKey') is not None:
            self.encrypt_private_key = m.get('EncryptPrivateKey')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('SignCertificate') is not None:
            self.sign_certificate = m.get('SignCertificate')
        if m.get('SignPrivateKey') is not None:
            self.sign_private_key = m.get('SignPrivateKey')
        return self


class UploadSSLCertificateResponseBody(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        request_id: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadSSLCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadSSLCertificateResponseBody = None,
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
            temp_model = UploadSSLCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


