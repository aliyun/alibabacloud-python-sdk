# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddDcdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        domain_name: str = None,
        resource_group_id: str = None,
        sources: str = None,
        check_url: str = None,
        scope: str = None,
        top_level_domain: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_name = domain_name
        self.resource_group_id = resource_group_id
        self.sources = sources
        self.check_url = check_url
        self.scope = scope
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class AddDcdnDomainResponseBody(TeaModel):
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


class AddDcdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDcdnDomainResponseBody = None,
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
            temp_model = AddDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDcdnIpaDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        domain_name: str = None,
        resource_group_id: str = None,
        sources: str = None,
        check_url: str = None,
        scope: str = None,
        top_level_domain: str = None,
        protocol: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_name = domain_name
        self.resource_group_id = resource_group_id
        self.sources = sources
        self.check_url = check_url
        self.scope = scope
        self.top_level_domain = top_level_domain
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class AddDcdnIpaDomainResponseBody(TeaModel):
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


class AddDcdnIpaDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDcdnIpaDomainResponseBody = None,
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
            temp_model = AddDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddDcdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        domain_name: str = None,
        resource_group_id: str = None,
        sources: str = None,
        check_url: str = None,
        scope: str = None,
        top_level_domain: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_name = domain_name
        self.resource_group_id = resource_group_id
        self.sources = sources
        self.check_url = check_url
        self.scope = scope
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class BatchAddDcdnDomainResponseBody(TeaModel):
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


class BatchAddDcdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchAddDcdnDomainResponseBody = None,
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
            temp_model = BatchAddDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteDcdnDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        domain_names: str = None,
        function_names: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_names = domain_names
        self.function_names = function_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        return self


class BatchDeleteDcdnDomainConfigsResponseBody(TeaModel):
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


class BatchDeleteDcdnDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDeleteDcdnDomainConfigsResponseBody = None,
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
            temp_model = BatchDeleteDcdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetDcdnDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        cert_name: str = None,
        cert_type: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        sslpri: str = None,
        region: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.cert_name = cert_name
        self.cert_type = cert_type
        self.sslprotocol = sslprotocol
        self.sslpub = sslpub
        self.sslpri = sslpri
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class BatchSetDcdnDomainCertificateResponseBody(TeaModel):
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


class BatchSetDcdnDomainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSetDcdnDomainCertificateResponseBody = None,
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
            temp_model = BatchSetDcdnDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetDcdnDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        domain_names: str = None,
        functions: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_names = domain_names
        self.functions = functions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        return self


class BatchSetDcdnDomainConfigsResponseBody(TeaModel):
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


class BatchSetDcdnDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSetDcdnDomainConfigsResponseBody = None,
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
            temp_model = BatchSetDcdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetDcdnIpaDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        domain_names: str = None,
        functions: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_names = domain_names
        self.functions = functions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        return self


class BatchSetDcdnIpaDomainConfigsResponseBody(TeaModel):
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


class BatchSetDcdnIpaDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSetDcdnIpaDomainConfigsResponseBody = None,
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
            temp_model = BatchSetDcdnIpaDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartDcdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_names: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class BatchStartDcdnDomainResponseBody(TeaModel):
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


class BatchStartDcdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStartDcdnDomainResponseBody = None,
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
            temp_model = BatchStartDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopDcdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_names: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class BatchStopDcdnDomainResponseBody(TeaModel):
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


class BatchStopDcdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStopDcdnDomainResponseBody = None,
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
            temp_model = BatchStopDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommitStagingRoutineCodeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        code_description: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.code_description = code_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        return self


class CommitStagingRoutineCodeResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CommitStagingRoutineCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CommitStagingRoutineCodeResponseBody = None,
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
            temp_model = CommitStagingRoutineCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnCertificateSigningRequestRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        common_name: str = None,
        sans: str = None,
        organization: str = None,
        organization_unit: str = None,
        country: str = None,
        state: str = None,
        city: str = None,
        email: str = None,
    ):
        self.owner_id = owner_id
        self.common_name = common_name
        self.sans = sans
        self.organization = organization
        self.organization_unit = organization_unit
        self.country = country
        self.state = state
        self.city = city
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.sans is not None:
            result['SANs'] = self.sans
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.country is not None:
            result['Country'] = self.country
        if self.state is not None:
            result['State'] = self.state
        if self.city is not None:
            result['City'] = self.city
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('SANs') is not None:
            self.sans = m.get('SANs')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class CreateDcdnCertificateSigningRequestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        pub_md_5: str = None,
        csr: str = None,
        common_name: str = None,
    ):
        self.request_id = request_id
        self.pub_md_5 = pub_md_5
        self.csr = csr
        self.common_name = common_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pub_md_5 is not None:
            result['PubMd5'] = self.pub_md_5
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PubMd5') is not None:
            self.pub_md_5 = m.get('PubMd5')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        return self


class CreateDcdnCertificateSigningRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDcdnCertificateSigningRequestResponseBody = None,
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
            temp_model = CreateDcdnCertificateSigningRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnDeliverTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        status: str = None,
        reports: str = None,
        domain_name: str = None,
        deliver: Dict[str, Any] = None,
        schedule: Dict[str, Any] = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.status = status
        self.reports = reports
        self.domain_name = domain_name
        self.deliver = deliver
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.deliver is not None:
            result['Deliver'] = self.deliver
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class CreateDcdnDeliverTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        status: str = None,
        reports: str = None,
        domain_name: str = None,
        deliver_shrink: str = None,
        schedule_shrink: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.status = status
        self.reports = reports
        self.domain_name = domain_name
        self.deliver_shrink = deliver_shrink
        self.schedule_shrink = schedule_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.deliver_shrink is not None:
            result['Deliver'] = self.deliver_shrink
        if self.schedule_shrink is not None:
            result['Schedule'] = self.schedule_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Deliver') is not None:
            self.deliver_shrink = m.get('Deliver')
        if m.get('Schedule') is not None:
            self.schedule_shrink = m.get('Schedule')
        return self


class CreateDcdnDeliverTaskResponseBody(TeaModel):
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


class CreateDcdnDeliverTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDcdnDeliverTaskResponseBody = None,
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
            temp_model = CreateDcdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnDomainOfflineLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        region_id: str = None,
        field_id: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.region_id = region_id
        self.field_id = field_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.field_id is not None:
            result['FieldId'] = self.field_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')
        return self


class CreateDcdnDomainOfflineLogDeliveryResponseBody(TeaModel):
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


class CreateDcdnDomainOfflineLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDcdnDomainOfflineLogDeliveryResponseBody = None,
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
            temp_model = CreateDcdnDomainOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDcdnSubTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        status: str = None,
        report_ids: str = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.status = status
        self.report_ids = report_ids
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class CreateDcdnSubTaskResponseBody(TeaModel):
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


class CreateDcdnSubTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDcdnSubTaskResponseBody = None,
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
            temp_model = CreateDcdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoutineRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        description: str = None,
        env_conf: Dict[str, Any] = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.description = description
        self.env_conf = env_conf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        return self


class CreateRoutineShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        description: str = None,
        env_conf_shrink: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.description = description
        self.env_conf_shrink = env_conf_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf_shrink is not None:
            result['EnvConf'] = self.env_conf_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf_shrink = m.get('EnvConf')
        return self


class CreateRoutineResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRoutineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRoutineResponseBody = None,
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
            temp_model = CreateRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnDeliverTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        deliver_id: int = None,
    ):
        self.owner_id = owner_id
        self.deliver_id = deliver_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        return self


class DeleteDcdnDeliverTaskResponseBody(TeaModel):
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


class DeleteDcdnDeliverTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDcdnDeliverTaskResponseBody = None,
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
            temp_model = DeleteDcdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteDcdnDomainResponseBody(TeaModel):
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


class DeleteDcdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDcdnDomainResponseBody = None,
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
            temp_model = DeleteDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnIpaDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteDcdnIpaDomainResponseBody(TeaModel):
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


class DeleteDcdnIpaDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDcdnIpaDomainResponseBody = None,
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
            temp_model = DeleteDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnIpaSpecificConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        config_id: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class DeleteDcdnIpaSpecificConfigResponseBody(TeaModel):
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


class DeleteDcdnIpaSpecificConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDcdnIpaSpecificConfigResponseBody = None,
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
            temp_model = DeleteDcdnIpaSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnSpecificConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        config_id: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class DeleteDcdnSpecificConfigResponseBody(TeaModel):
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


class DeleteDcdnSpecificConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDcdnSpecificConfigResponseBody = None,
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
            temp_model = DeleteDcdnSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnSpecificStagingConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        config_id: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class DeleteDcdnSpecificStagingConfigResponseBody(TeaModel):
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


class DeleteDcdnSpecificStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDcdnSpecificStagingConfigResponseBody = None,
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
            temp_model = DeleteDcdnSpecificStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDcdnSubTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteDcdnSubTaskResponseBody(TeaModel):
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


class DeleteDcdnSubTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDcdnSubTaskResponseBody = None,
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
            temp_model = DeleteDcdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
    ):
        self.owner_id = owner_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteRoutineResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRoutineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRoutineResponseBody = None,
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
            temp_model = DeleteRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineCodeRevisionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        select_code_revision: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.select_code_revision = select_code_revision

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        return self


class DeleteRoutineCodeRevisionResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRoutineCodeRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRoutineCodeRevisionResponseBody = None,
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
            temp_model = DeleteRoutineCodeRevisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoutineConfEnvsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        envs: Dict[str, Any] = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.envs = envs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.envs is not None:
            result['Envs'] = self.envs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        return self


class DeleteRoutineConfEnvsShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        envs_shrink: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.envs_shrink = envs_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.envs_shrink is not None:
            result['Envs'] = self.envs_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Envs') is not None:
            self.envs_shrink = m.get('Envs')
        return self


class DeleteRoutineConfEnvsResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRoutineConfEnvsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRoutineConfEnvsResponseBody = None,
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
            temp_model = DeleteRoutineConfEnvsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnBgpBpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        isp: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.isp = isp
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval(TeaModel):
    def __init__(
        self,
        out: float = None,
        in_: float = None,
        time_stamp: str = None,
    ):
        self.out = out
        self.in_ = in_
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out is not None:
            result['Out'] = self.out
        if self.in_ is not None:
            result['In'] = self.in_
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnBgpBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        bgp_data_interval: List[DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval] = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.bgp_data_interval = bgp_data_interval

    def validate(self):
        if self.bgp_data_interval:
            for k in self.bgp_data_interval:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['BgpDataInterval'] = []
        if self.bgp_data_interval is not None:
            for k in self.bgp_data_interval:
                result['BgpDataInterval'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bgp_data_interval = []
        if m.get('BgpDataInterval') is not None:
            for k in m.get('BgpDataInterval'):
                temp_model = DescribeDcdnBgpBpsDataResponseBodyBgpDataInterval()
                self.bgp_data_interval.append(temp_model.from_map(k))
        return self


class DescribeDcdnBgpBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnBgpBpsDataResponseBody = None,
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
            temp_model = DescribeDcdnBgpBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnBgpTrafficDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        isp: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.isp = isp
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval(TeaModel):
    def __init__(
        self,
        out: int = None,
        in_: int = None,
        time_stamp: str = None,
    ):
        self.out = out
        self.in_ = in_
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out is not None:
            result['Out'] = self.out
        if self.in_ is not None:
            result['In'] = self.in_
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnBgpTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        bgp_data_interval: List[DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval] = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.bgp_data_interval = bgp_data_interval

    def validate(self):
        if self.bgp_data_interval:
            for k in self.bgp_data_interval:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['BgpDataInterval'] = []
        if self.bgp_data_interval is not None:
            for k in self.bgp_data_interval:
                result['BgpDataInterval'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bgp_data_interval = []
        if m.get('BgpDataInterval') is not None:
            for k in m.get('BgpDataInterval'):
                temp_model = DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval()
                self.bgp_data_interval.append(temp_model.from_map(k))
        return self


class DescribeDcdnBgpTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnBgpTrafficDataResponseBody = None,
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
            temp_model = DescribeDcdnBgpTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnBlockedRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        language: str = None,
    ):
        self.owner_id = owner_id
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem(TeaModel):
    def __init__(
        self,
        countries_and_regions: str = None,
        continent: str = None,
        countries_and_regions_name: str = None,
    ):
        self.countries_and_regions = countries_and_regions
        self.continent = continent
        self.countries_and_regions_name = countries_and_regions_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.countries_and_regions is not None:
            result['CountriesAndRegions'] = self.countries_and_regions
        if self.continent is not None:
            result['Continent'] = self.continent
        if self.countries_and_regions_name is not None:
            result['CountriesAndRegionsName'] = self.countries_and_regions_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountriesAndRegions') is not None:
            self.countries_and_regions = m.get('CountriesAndRegions')
        if m.get('Continent') is not None:
            self.continent = m.get('Continent')
        if m.get('CountriesAndRegionsName') is not None:
            self.countries_and_regions_name = m.get('CountriesAndRegionsName')
        return self


class DescribeDcdnBlockedRegionsResponseBodyInfoList(TeaModel):
    def __init__(
        self,
        info_item: List[DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem] = None,
    ):
        self.info_item = info_item

    def validate(self):
        if self.info_item:
            for k in self.info_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InfoItem'] = []
        if self.info_item is not None:
            for k in self.info_item:
                result['InfoItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info_item = []
        if m.get('InfoItem') is not None:
            for k in m.get('InfoItem'):
                temp_model = DescribeDcdnBlockedRegionsResponseBodyInfoListInfoItem()
                self.info_item.append(temp_model.from_map(k))
        return self


class DescribeDcdnBlockedRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        info_list: DescribeDcdnBlockedRegionsResponseBodyInfoList = None,
    ):
        self.request_id = request_id
        self.info_list = info_list

    def validate(self):
        if self.info_list:
            self.info_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.info_list is not None:
            result['InfoList'] = self.info_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InfoList') is not None:
            temp_model = DescribeDcdnBlockedRegionsResponseBodyInfoList()
            self.info_list = temp_model.from_map(m['InfoList'])
        return self


class DescribeDcdnBlockedRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnBlockedRegionsResponseBody = None,
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
            temp_model = DescribeDcdnBlockedRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        cert_name: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.cert_name = cert_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        return self


class DescribeDcdnCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        key: str = None,
        cert: str = None,
        cert_id: int = None,
        request_id: str = None,
    ):
        self.cert_name = cert_name
        self.key = key
        self.cert = cert
        self.cert_id = cert_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.key is not None:
            result['Key'] = self.key
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnCertificateDetailResponseBody = None,
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
            temp_model = DescribeDcdnCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnCertificateListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
    def __init__(
        self,
        last_time: int = None,
        fingerprint: str = None,
        cert_name: str = None,
        issuer: str = None,
        cert_id: int = None,
        common: str = None,
    ):
        self.last_time = last_time
        self.fingerprint = fingerprint
        self.cert_name = cert_name
        self.issuer = issuer
        self.cert_id = cert_id
        self.common = common

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.common is not None:
            result['Common'] = self.common
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        return self


class DescribeDcdnCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(
        self,
        cert: List[DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert] = None,
    ):
        self.cert = cert

    def validate(self):
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cert'] = []
        if self.cert is not None:
            for k in self.cert:
                result['Cert'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert = []
        if m.get('Cert') is not None:
            for k in m.get('Cert'):
                temp_model = DescribeDcdnCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeDcdnCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(
        self,
        count: int = None,
        cert_list: DescribeDcdnCertificateListResponseBodyCertificateListModelCertList = None,
    ):
        self.count = count
        self.cert_list = cert_list

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CertList') is not None:
            temp_model = DescribeDcdnCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        return self


class DescribeDcdnCertificateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        certificate_list_model: DescribeDcdnCertificateListResponseBodyCertificateListModel = None,
    ):
        self.request_id = request_id
        self.certificate_list_model = certificate_list_model

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeDcdnCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        return self


class DescribeDcdnCertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnCertificateListResponseBody = None,
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
            temp_model = DescribeDcdnCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnConfigOfVersionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        version_id: str = None,
        function_id: int = None,
        function_name: str = None,
        group_id: int = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.version_id = version_id
        self.function_id = function_id
        self.function_name = function_name
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        self.arg_name = arg_name
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs(TeaModel):
    def __init__(
        self,
        function_arg: List[DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg] = None,
    ):
        self.function_arg = function_arg

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k in m.get('FunctionArg'):
                temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfig(TeaModel):
    def __init__(
        self,
        status: str = None,
        config_id: str = None,
        function_name: str = None,
        function_args: DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs = None,
    ):
        self.status = status
        self.config_id = config_id
        self.function_name = function_name
        self.function_args = function_args

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        return self


class DescribeDcdnConfigOfVersionResponseBodyVersionConfigs(TeaModel):
    def __init__(
        self,
        version_config: List[DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfig] = None,
    ):
        self.version_config = version_config

    def validate(self):
        if self.version_config:
            for k in self.version_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VersionConfig'] = []
        if self.version_config is not None:
            for k in self.version_config:
                result['VersionConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.version_config = []
        if m.get('VersionConfig') is not None:
            for k in m.get('VersionConfig'):
                temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigsVersionConfig()
                self.version_config.append(temp_model.from_map(k))
        return self


class DescribeDcdnConfigOfVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_configs: DescribeDcdnConfigOfVersionResponseBodyVersionConfigs = None,
    ):
        self.request_id = request_id
        self.version_configs = version_configs

    def validate(self):
        if self.version_configs:
            self.version_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_configs is not None:
            result['VersionConfigs'] = self.version_configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionConfigs') is not None:
            temp_model = DescribeDcdnConfigOfVersionResponseBodyVersionConfigs()
            self.version_configs = temp_model.from_map(m['VersionConfigs'])
        return self


class DescribeDcdnConfigOfVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnConfigOfVersionResponseBody = None,
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
            temp_model = DescribeDcdnConfigOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDeliverListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        deliver_id: int = None,
        status: str = None,
    ):
        self.owner_id = owner_id
        self.deliver_id = deliver_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnDeliverListResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDeliverListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDeliverListResponseBody = None,
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
            temp_model = DescribeDcdnDeliverListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainBpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        static_https_bps: float = None,
        bps: float = None,
        dynamic_https_bps: float = None,
        dynamic_http_bps: float = None,
        static_http_bps: float = None,
    ):
        self.time_stamp = time_stamp
        self.static_https_bps = static_https_bps
        self.bps = bps
        self.dynamic_https_bps = dynamic_https_bps
        self.dynamic_http_bps = dynamic_http_bps
        self.static_http_bps = static_http_bps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.static_https_bps is not None:
            result['StaticHttpsBps'] = self.static_https_bps
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.dynamic_https_bps is not None:
            result['DynamicHttpsBps'] = self.dynamic_https_bps
        if self.dynamic_http_bps is not None:
            result['DynamicHttpBps'] = self.dynamic_http_bps
        if self.static_http_bps is not None:
            result['StaticHttpBps'] = self.static_http_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('StaticHttpsBps') is not None:
            self.static_https_bps = m.get('StaticHttpsBps')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DynamicHttpsBps') is not None:
            self.dynamic_https_bps = m.get('DynamicHttpsBps')
        if m.get('DynamicHttpBps') is not None:
            self.dynamic_http_bps = m.get('DynamicHttpBps')
        if m.get('StaticHttpBps') is not None:
            self.static_http_bps = m.get('StaticHttpBps')
        return self


class DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        bps_data_per_interval: DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.bps_data_per_interval = bps_data_per_interval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        return self


class DescribeDcdnDomainBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainBpsDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainByCertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        sslpub: str = None,
    ):
        self.owner_id = owner_id
        self.sslpub = sslpub

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        return self


class DescribeDcdnDomainByCertificateResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        cert_start_time: str = None,
        cert_expire_time: str = None,
        cert_ca_is_legacy: str = None,
        cert_subject_common_name: str = None,
        cert_type: str = None,
        domain_names: str = None,
        cert_expired: str = None,
        issuer: str = None,
        domain_list: str = None,
    ):
        self.cert_start_time = cert_start_time
        self.cert_expire_time = cert_expire_time
        self.cert_ca_is_legacy = cert_ca_is_legacy
        self.cert_subject_common_name = cert_subject_common_name
        self.cert_type = cert_type
        self.domain_names = domain_names
        self.cert_expired = cert_expired
        self.issuer = issuer
        self.domain_list = domain_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_ca_is_legacy is not None:
            result['CertCaIsLegacy'] = self.cert_ca_is_legacy
        if self.cert_subject_common_name is not None:
            result['CertSubjectCommonName'] = self.cert_subject_common_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.cert_expired is not None:
            result['CertExpired'] = self.cert_expired
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertCaIsLegacy') is not None:
            self.cert_ca_is_legacy = m.get('CertCaIsLegacy')
        if m.get('CertSubjectCommonName') is not None:
            self.cert_subject_common_name = m.get('CertSubjectCommonName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('CertExpired') is not None:
            self.cert_expired = m.get('CertExpired')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        return self


class DescribeDcdnDomainByCertificateResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeDcdnDomainByCertificateResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeDcdnDomainByCertificateResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainByCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cert_infos: DescribeDcdnDomainByCertificateResponseBodyCertInfos = None,
    ):
        self.request_id = request_id
        self.cert_infos = cert_infos

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnDomainByCertificateResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        return self


class DescribeDcdnDomainByCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainByCertificateResponseBody = None,
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
            temp_model = DescribeDcdnDomainByCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainCertificateInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        cert_life: str = None,
        cert_expire_time: str = None,
        sslpub: str = None,
        sslprotocol: str = None,
        cert_type: str = None,
        cert_domain_name: str = None,
        cert_name: str = None,
        cert_org: str = None,
        domain_name: str = None,
    ):
        self.status = status
        self.cert_life = cert_life
        self.cert_expire_time = cert_expire_time
        self.sslpub = sslpub
        self.sslprotocol = sslprotocol
        self.cert_type = cert_type
        self.cert_domain_name = cert_domain_name
        self.cert_name = cert_name
        self.cert_org = cert_org
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeDcdnDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainCertificateInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cert_infos: DescribeDcdnDomainCertificateInfoResponseBodyCertInfos = None,
    ):
        self.request_id = request_id
        self.cert_infos = cert_infos

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        return self


class DescribeDcdnDomainCertificateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainCertificateInfoResponseBody = None,
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
            temp_model = DescribeDcdnDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainCnameRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainCnameResponseBodyCnameDatasData(TeaModel):
    def __init__(
        self,
        status: int = None,
        domain: str = None,
        cname: str = None,
    ):
        self.status = status
        self.domain = domain
        self.cname = cname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        return self


class DescribeDcdnDomainCnameResponseBodyCnameDatas(TeaModel):
    def __init__(
        self,
        data: List[DescribeDcdnDomainCnameResponseBodyCnameDatasData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDcdnDomainCnameResponseBodyCnameDatasData()
                self.data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainCnameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cname_datas: DescribeDcdnDomainCnameResponseBodyCnameDatas = None,
    ):
        self.request_id = request_id
        self.cname_datas = cname_datas

    def validate(self):
        if self.cname_datas:
            self.cname_datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cname_datas is not None:
            result['CnameDatas'] = self.cname_datas.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CnameDatas') is not None:
            temp_model = DescribeDcdnDomainCnameResponseBodyCnameDatas()
            self.cname_datas = temp_model.from_map(m['CnameDatas'])
        return self


class DescribeDcdnDomainCnameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainCnameResponseBody = None,
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
            temp_model = DescribeDcdnDomainCnameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        function_names: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.function_names = function_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        return self


class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        self.arg_name = arg_name
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(
        self,
        function_arg: List[DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg] = None,
    ):
        self.function_arg = function_arg

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k in m.get('FunctionArg'):
                temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(
        self,
        status: str = None,
        config_id: str = None,
        function_name: str = None,
        function_args: DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs = None,
    ):
        self.status = status
        self.config_id = config_id
        self.function_name = function_name
        self.function_args = function_args

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        return self


class DescribeDcdnDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        domain_config: List[DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig] = None,
    ):
        self.domain_config = domain_config

    def validate(self):
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfig'] = []
        if self.domain_config is not None:
            for k in self.domain_config:
                result['DomainConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_config = []
        if m.get('DomainConfig') is not None:
            for k in m.get('DomainConfig'):
                temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_configs: DescribeDcdnDomainConfigsResponseBodyDomainConfigs = None,
    ):
        self.request_id = request_id
        self.domain_configs = domain_configs

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeDcdnDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        return self


class DescribeDcdnDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainConfigsResponseBody = None,
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
            temp_model = DescribeDcdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: str = None,
        enabled: str = None,
        priority: str = None,
        port: int = None,
        content: str = None,
    ):
        self.type = type
        self.weight = weight
        self.enabled = enabled
        self.priority = priority
        self.port = port
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeDcdnDomainDetailResponseBodyDomainDetailSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainDetailResponseBodyDomainDetail(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        sslpub: str = None,
        description: str = None,
        sslprotocol: str = None,
        resource_group_id: str = None,
        cert_name: str = None,
        scope: str = None,
        cname: str = None,
        domain_status: str = None,
        gmt_modified: str = None,
        domain_name: str = None,
        sources: DescribeDcdnDomainDetailResponseBodyDomainDetailSources = None,
    ):
        self.gmt_created = gmt_created
        self.sslpub = sslpub
        self.description = description
        self.sslprotocol = sslprotocol
        self.resource_group_id = resource_group_id
        self.cert_name = cert_name
        self.scope = scope
        self.cname = cname
        self.domain_status = domain_status
        self.gmt_modified = gmt_modified
        self.domain_name = domain_name
        self.sources = sources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnDomainDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_detail: DescribeDcdnDomainDetailResponseBodyDomainDetail = None,
    ):
        self.request_id = request_id
        self.domain_detail = domain_detail

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainDetail') is not None:
            temp_model = DescribeDcdnDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m['DomainDetail'])
        return self


class DescribeDcdnDomainDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainDetailResponseBody = None,
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
            temp_model = DescribeDcdnDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainHitRateDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        byte_hit_rate: float = None,
        req_hit_rate: float = None,
    ):
        self.time_stamp = time_stamp
        self.byte_hit_rate = byte_hit_rate
        self.req_hit_rate = req_hit_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
        return self


class DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        hit_rate_per_interval: DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.hit_rate_per_interval = hit_rate_per_interval

    def validate(self):
        if self.hit_rate_per_interval:
            self.hit_rate_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.hit_rate_per_interval is not None:
            result['HitRatePerInterval'] = self.hit_rate_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('HitRatePerInterval') is not None:
            temp_model = DescribeDcdnDomainHitRateDataResponseBodyHitRatePerInterval()
            self.hit_rate_per_interval = temp_model.from_map(m['HitRatePerInterval'])
        return self


class DescribeDcdnDomainHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainHitRateDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainHttpCodeDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule(TeaModel):
    def __init__(
        self,
        code: int = None,
        proportion: float = None,
        count: float = None,
    ):
        self.code = code
        self.proportion = proportion
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval(TeaModel):
    def __init__(
        self,
        http_code_data_module: List[DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule] = None,
    ):
        self.http_code_data_module = http_code_data_module

    def validate(self):
        if self.http_code_data_module:
            for k in self.http_code_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HttpCodeDataModule'] = []
        if self.http_code_data_module is not None:
            for k in self.http_code_data_module:
                result['HttpCodeDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.http_code_data_module = []
        if m.get('HttpCodeDataModule') is not None:
            for k in m.get('HttpCodeDataModule'):
                temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule()
                self.http_code_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        http_code_data_per_interval: DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval = None,
    ):
        self.time_stamp = time_stamp
        self.http_code_data_per_interval = http_code_data_per_interval

    def validate(self):
        if self.http_code_data_per_interval:
            self.http_code_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.http_code_data_per_interval is not None:
            result['HttpCodeDataPerInterval'] = self.http_code_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('HttpCodeDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval()
            self.http_code_data_per_interval = temp_model.from_map(m['HttpCodeDataPerInterval'])
        return self


class DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        data_per_interval: DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.data_per_interval = data_per_interval

    def validate(self):
        if self.data_per_interval:
            self.data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.data_per_interval is not None:
            result['DataPerInterval'] = self.data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DataPerInterval') is not None:
            temp_model = DescribeDcdnDomainHttpCodeDataResponseBodyDataPerInterval()
            self.data_per_interval = temp_model.from_map(m['DataPerInterval'])
        return self


class DescribeDcdnDomainHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainHttpCodeDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainIpaBpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        time_merge: str = None,
        interval: str = None,
        fix_time_gap: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.time_merge = time_merge
        self.interval = interval
        self.fix_time_gap = fix_time_gap
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.fix_time_gap is not None:
            result['FixTimeGap'] = self.fix_time_gap
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        ipa_bps: float = None,
        time_stamp: str = None,
    ):
        self.ipa_bps = ipa_bps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipa_bps is not None:
            result['IpaBps'] = self.ipa_bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpaBps') is not None:
            self.ipa_bps = m.get('IpaBps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainIpaBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        bps_data_per_interval: DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.bps_data_per_interval = bps_data_per_interval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainIpaBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        return self


class DescribeDcdnDomainIpaBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainIpaBpsDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainIpaBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainIpaTrafficDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        time_merge: str = None,
        interval: str = None,
        fix_time_gap: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.time_merge = time_merge
        self.interval = interval
        self.fix_time_gap = fix_time_gap
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.fix_time_gap is not None:
            result['FixTimeGap'] = self.fix_time_gap
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        ipa_traffic: float = None,
        time_stamp: str = None,
    ):
        self.ipa_traffic = ipa_traffic
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipa_traffic is not None:
            result['IpaTraffic'] = self.ipa_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpaTraffic') is not None:
            self.ipa_traffic = m.get('IpaTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainIpaTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        traffic_data_per_interval: DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.traffic_data_per_interval = traffic_data_per_interval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainIpaTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeDcdnDomainIpaTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainIpaTrafficDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainIpaTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainIspDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainIspDataResponseBodyValueIspProportionData(TeaModel):
    def __init__(
        self,
        qps: str = None,
        total_query: str = None,
        total_bytes: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        proportion: str = None,
        avg_object_size: str = None,
        isp_ename: str = None,
        bps: str = None,
        isp: str = None,
        bytes_proportion: str = None,
    ):
        self.qps = qps
        self.total_query = total_query
        self.total_bytes = total_bytes
        self.avg_response_rate = avg_response_rate
        self.avg_response_time = avg_response_time
        self.proportion = proportion
        self.avg_object_size = avg_object_size
        self.isp_ename = isp_ename
        self.bps = bps
        self.isp = isp
        self.bytes_proportion = bytes_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        return self


class DescribeDcdnDomainIspDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        isp_proportion_data: List[DescribeDcdnDomainIspDataResponseBodyValueIspProportionData] = None,
    ):
        self.isp_proportion_data = isp_proportion_data

    def validate(self):
        if self.isp_proportion_data:
            for k in self.isp_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IspProportionData'] = []
        if self.isp_proportion_data is not None:
            for k in self.isp_proportion_data:
                result['IspProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_proportion_data = []
        if m.get('IspProportionData') is not None:
            for k in m.get('IspProportionData'):
                temp_model = DescribeDcdnDomainIspDataResponseBodyValueIspProportionData()
                self.isp_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainIspDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        value: DescribeDcdnDomainIspDataResponseBodyValue = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('Value') is not None:
            temp_model = DescribeDcdnDomainIspDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDcdnDomainIspDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainIspDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainIspDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainLogRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        page_size: int = None,
        page_number: int = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.page_size = page_size
        self.page_number = page_number
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        log_size: int = None,
        start_time: str = None,
        log_name: str = None,
        log_path: str = None,
    ):
        self.end_time = end_time
        self.log_size = log_size
        self.start_time = start_time
        self.log_name = log_name
        self.log_path = log_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos(TeaModel):
    def __init__(
        self,
        log_info_detail: List[DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail] = None,
    ):
        self.log_info_detail = log_info_detail

    def validate(self):
        if self.log_info_detail:
            for k in self.log_info_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogInfoDetail'] = []
        if self.log_info_detail is not None:
            for k in self.log_info_detail:
                result['LogInfoDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_info_detail = []
        if m.get('LogInfoDetail') is not None:
            for k in m.get('LogInfoDetail'):
                temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(
        self,
        log_count: int = None,
        log_infos: DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos = None,
        page_infos: DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos = None,
    ):
        self.log_count = log_count
        self.log_infos = log_infos
        self.page_infos = page_infos

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()
        if self.page_infos:
            self.page_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('LogInfos') is not None:
            temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        if m.get('PageInfos') is not None:
            temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m['PageInfos'])
        return self


class DescribeDcdnDomainLogResponseBodyDomainLogDetails(TeaModel):
    def __init__(
        self,
        domain_log_detail: List[DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail] = None,
    ):
        self.domain_log_detail = domain_log_detail

    def validate(self):
        if self.domain_log_detail:
            for k in self.domain_log_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainLogDetail'] = []
        if self.domain_log_detail is not None:
            for k in self.domain_log_detail:
                result['DomainLogDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_log_detail = []
        if m.get('DomainLogDetail') is not None:
            for k in m.get('DomainLogDetail'):
                temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainLogResponseBody(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        request_id: str = None,
        domain_log_details: DescribeDcdnDomainLogResponseBodyDomainLogDetails = None,
    ):
        self.domain_name = domain_name
        self.request_id = request_id
        self.domain_log_details = domain_log_details

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeDcdnDomainLogResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        return self


class DescribeDcdnDomainLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainLogResponseBody = None,
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
            temp_model = DescribeDcdnDomainLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainMultiUsageDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule(TeaModel):
    def __init__(
        self,
        type: str = None,
        time_stamp: str = None,
        domain: str = None,
        request: int = None,
    ):
        self.type = type
        self.time_stamp = time_stamp
        self.domain = domain
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval(TeaModel):
    def __init__(
        self,
        request_data_module: List[DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule] = None,
    ):
        self.request_data_module = request_data_module

    def validate(self):
        if self.request_data_module:
            for k in self.request_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestDataModule'] = []
        if self.request_data_module is not None:
            for k in self.request_data_module:
                result['RequestDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_data_module = []
        if m.get('RequestDataModule') is not None:
            for k in m.get('RequestDataModule'):
                temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule()
                self.request_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule(TeaModel):
    def __init__(
        self,
        type: str = None,
        domain: str = None,
        time_stamp: str = None,
        area: str = None,
        bps: float = None,
    ):
        self.type = type
        self.domain = domain
        self.time_stamp = time_stamp
        self.area = area
        self.bps = bps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.area is not None:
            result['Area'] = self.area
        if self.bps is not None:
            result['Bps'] = self.bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        return self


class DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval(TeaModel):
    def __init__(
        self,
        traffic_data_module: List[DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule] = None,
    ):
        self.traffic_data_module = traffic_data_module

    def validate(self):
        if self.traffic_data_module:
            for k in self.traffic_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficDataModule'] = []
        if self.traffic_data_module is not None:
            for k in self.traffic_data_module:
                result['TrafficDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_data_module = []
        if m.get('TrafficDataModule') is not None:
            for k in m.get('TrafficDataModule'):
                temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule()
                self.traffic_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainMultiUsageDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        request_per_interval: DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval = None,
        traffic_per_interval: DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.request_per_interval = request_per_interval
        self.traffic_per_interval = traffic_per_interval

    def validate(self):
        if self.request_per_interval:
            self.request_per_interval.validate()
        if self.traffic_per_interval:
            self.traffic_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_per_interval is not None:
            result['RequestPerInterval'] = self.request_per_interval.to_map()
        if self.traffic_per_interval is not None:
            result['TrafficPerInterval'] = self.traffic_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestPerInterval') is not None:
            temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval()
            self.request_per_interval = temp_model.from_map(m['RequestPerInterval'])
        if m.get('TrafficPerInterval') is not None:
            temp_model = DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval()
            self.traffic_per_interval = temp_model.from_map(m['TrafficPerInterval'])
        return self


class DescribeDcdnDomainMultiUsageDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainMultiUsageDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainMultiUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainOriginBpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        dynamic_http_origin_bps: float = None,
        static_http_origin_bps: float = None,
        time_stamp: str = None,
        static_https_origin_bps: float = None,
        origin_bps: float = None,
        dynamic_https_origin_bps: float = None,
    ):
        self.dynamic_http_origin_bps = dynamic_http_origin_bps
        self.static_http_origin_bps = static_http_origin_bps
        self.time_stamp = time_stamp
        self.static_https_origin_bps = static_https_origin_bps
        self.origin_bps = origin_bps
        self.dynamic_https_origin_bps = dynamic_https_origin_bps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_http_origin_bps is not None:
            result['DynamicHttpOriginBps'] = self.dynamic_http_origin_bps
        if self.static_http_origin_bps is not None:
            result['StaticHttpOriginBps'] = self.static_http_origin_bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.static_https_origin_bps is not None:
            result['StaticHttpsOriginBps'] = self.static_https_origin_bps
        if self.origin_bps is not None:
            result['OriginBps'] = self.origin_bps
        if self.dynamic_https_origin_bps is not None:
            result['DynamicHttpsOriginBps'] = self.dynamic_https_origin_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicHttpOriginBps') is not None:
            self.dynamic_http_origin_bps = m.get('DynamicHttpOriginBps')
        if m.get('StaticHttpOriginBps') is not None:
            self.static_http_origin_bps = m.get('StaticHttpOriginBps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('StaticHttpsOriginBps') is not None:
            self.static_https_origin_bps = m.get('StaticHttpsOriginBps')
        if m.get('OriginBps') is not None:
            self.origin_bps = m.get('OriginBps')
        if m.get('DynamicHttpsOriginBps') is not None:
            self.dynamic_https_origin_bps = m.get('DynamicHttpsOriginBps')
        return self


class DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainOriginBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        origin_bps_data_per_interval: DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.origin_bps_data_per_interval = origin_bps_data_per_interval

    def validate(self):
        if self.origin_bps_data_per_interval:
            self.origin_bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.origin_bps_data_per_interval is not None:
            result['OriginBpsDataPerInterval'] = self.origin_bps_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('OriginBpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval()
            self.origin_bps_data_per_interval = temp_model.from_map(m['OriginBpsDataPerInterval'])
        return self


class DescribeDcdnDomainOriginBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainOriginBpsDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainOriginBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainOriginTrafficDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        dynamic_http_origin_traffic: float = None,
        static_https_origin_traffic: float = None,
        origin_traffic: float = None,
        static_http_origin_traffic: float = None,
        dynamic_https_origin_traffic: float = None,
        time_stamp: str = None,
    ):
        self.dynamic_http_origin_traffic = dynamic_http_origin_traffic
        self.static_https_origin_traffic = static_https_origin_traffic
        self.origin_traffic = origin_traffic
        self.static_http_origin_traffic = static_http_origin_traffic
        self.dynamic_https_origin_traffic = dynamic_https_origin_traffic
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_http_origin_traffic is not None:
            result['DynamicHttpOriginTraffic'] = self.dynamic_http_origin_traffic
        if self.static_https_origin_traffic is not None:
            result['StaticHttpsOriginTraffic'] = self.static_https_origin_traffic
        if self.origin_traffic is not None:
            result['OriginTraffic'] = self.origin_traffic
        if self.static_http_origin_traffic is not None:
            result['StaticHttpOriginTraffic'] = self.static_http_origin_traffic
        if self.dynamic_https_origin_traffic is not None:
            result['DynamicHttpsOriginTraffic'] = self.dynamic_https_origin_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicHttpOriginTraffic') is not None:
            self.dynamic_http_origin_traffic = m.get('DynamicHttpOriginTraffic')
        if m.get('StaticHttpsOriginTraffic') is not None:
            self.static_https_origin_traffic = m.get('StaticHttpsOriginTraffic')
        if m.get('OriginTraffic') is not None:
            self.origin_traffic = m.get('OriginTraffic')
        if m.get('StaticHttpOriginTraffic') is not None:
            self.static_http_origin_traffic = m.get('StaticHttpOriginTraffic')
        if m.get('DynamicHttpsOriginTraffic') is not None:
            self.dynamic_https_origin_traffic = m.get('DynamicHttpsOriginTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainOriginTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        origin_traffic_data_per_interval: DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.origin_traffic_data_per_interval = origin_traffic_data_per_interval

    def validate(self):
        if self.origin_traffic_data_per_interval:
            self.origin_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.origin_traffic_data_per_interval is not None:
            result['OriginTrafficDataPerInterval'] = self.origin_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('OriginTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval()
            self.origin_traffic_data_per_interval = temp_model.from_map(m['OriginTrafficDataPerInterval'])
        return self


class DescribeDcdnDomainOriginTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainOriginTrafficDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainOriginTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainPropertyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnDomainPropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        protocol: str = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeDcdnDomainPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainPropertyResponseBody = None,
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
            temp_model = DescribeDcdnDomainPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainPvDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
    def __init__(
        self,
        value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainPvDataResponseBodyPvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DescribeDcdnDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainPvDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        pv_data_interval: DescribeDcdnDomainPvDataResponseBodyPvDataInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.pv_data_interval = pv_data_interval

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('PvDataInterval') is not None:
            temp_model = DescribeDcdnDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        return self


class DescribeDcdnDomainPvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainPvDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainPvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainQpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        dynamic_https_acc: float = None,
        dynamic_http_acc: float = None,
        qps: float = None,
        static_https_acc: float = None,
        static_http_qps: float = None,
        static_http_acc: float = None,
        dynamic_https_qps: float = None,
        acc: float = None,
        static_https_qps: float = None,
        dynamic_http_qps: float = None,
        time_stamp: str = None,
    ):
        self.dynamic_https_acc = dynamic_https_acc
        self.dynamic_http_acc = dynamic_http_acc
        self.qps = qps
        self.static_https_acc = static_https_acc
        self.static_http_qps = static_http_qps
        self.static_http_acc = static_http_acc
        self.dynamic_https_qps = dynamic_https_qps
        self.acc = acc
        self.static_https_qps = static_https_qps
        self.dynamic_http_qps = dynamic_http_qps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_https_acc is not None:
            result['DynamicHttpsAcc'] = self.dynamic_https_acc
        if self.dynamic_http_acc is not None:
            result['DynamicHttpAcc'] = self.dynamic_http_acc
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.static_https_acc is not None:
            result['StaticHttpsAcc'] = self.static_https_acc
        if self.static_http_qps is not None:
            result['StaticHttpQps'] = self.static_http_qps
        if self.static_http_acc is not None:
            result['StaticHttpAcc'] = self.static_http_acc
        if self.dynamic_https_qps is not None:
            result['DynamicHttpsQps'] = self.dynamic_https_qps
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.static_https_qps is not None:
            result['StaticHttpsQps'] = self.static_https_qps
        if self.dynamic_http_qps is not None:
            result['DynamicHttpQps'] = self.dynamic_http_qps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicHttpsAcc') is not None:
            self.dynamic_https_acc = m.get('DynamicHttpsAcc')
        if m.get('DynamicHttpAcc') is not None:
            self.dynamic_http_acc = m.get('DynamicHttpAcc')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('StaticHttpsAcc') is not None:
            self.static_https_acc = m.get('StaticHttpsAcc')
        if m.get('StaticHttpQps') is not None:
            self.static_http_qps = m.get('StaticHttpQps')
        if m.get('StaticHttpAcc') is not None:
            self.static_http_acc = m.get('StaticHttpAcc')
        if m.get('DynamicHttpsQps') is not None:
            self.dynamic_https_qps = m.get('DynamicHttpsQps')
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('StaticHttpsQps') is not None:
            self.static_https_qps = m.get('StaticHttpsQps')
        if m.get('DynamicHttpQps') is not None:
            self.dynamic_http_qps = m.get('DynamicHttpQps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        qps_data_per_interval: DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.qps_data_per_interval = qps_data_per_interval

    def validate(self):
        if self.qps_data_per_interval:
            self.qps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.qps_data_per_interval is not None:
            result['QpsDataPerInterval'] = self.qps_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('QpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval()
            self.qps_data_per_interval = temp_model.from_map(m['QpsDataPerInterval'])
        return self


class DescribeDcdnDomainQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainQpsDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeBpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeBpsDataResponseBodyDataBpsModel(TeaModel):
    def __init__(
        self,
        bps: float = None,
        time_stamp: str = None,
    ):
        self.bps = bps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeBpsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        bps_model: List[DescribeDcdnDomainRealTimeBpsDataResponseBodyDataBpsModel] = None,
    ):
        self.bps_model = bps_model

    def validate(self):
        if self.bps_model:
            for k in self.bps_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BpsModel'] = []
        if self.bps_model is not None:
            for k in self.bps_model:
                result['BpsModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bps_model = []
        if m.get('BpsModel') is not None:
            for k in m.get('BpsModel'):
                temp_model = DescribeDcdnDomainRealTimeBpsDataResponseBodyDataBpsModel()
                self.bps_model.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDcdnDomainRealTimeBpsDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDcdnDomainRealTimeBpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDcdnDomainRealTimeBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeBpsDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel(TeaModel):
    def __init__(
        self,
        byte_hit_rate: float = None,
        time_stamp: str = None,
    ):
        self.byte_hit_rate = byte_hit_rate
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData(TeaModel):
    def __init__(
        self,
        byte_hit_rate_data_model: List[DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel] = None,
    ):
        self.byte_hit_rate_data_model = byte_hit_rate_data_model

    def validate(self):
        if self.byte_hit_rate_data_model:
            for k in self.byte_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ByteHitRateDataModel'] = []
        if self.byte_hit_rate_data_model is not None:
            for k in self.byte_hit_rate_data_model:
                result['ByteHitRateDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.byte_hit_rate_data_model = []
        if m.get('ByteHitRateDataModel') is not None:
            for k in m.get('ByteHitRateDataModel'):
                temp_model = DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel()
                self.byte_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDcdnDomainRealTimeByteHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeByteHitRateDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeByteHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeDetailDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        field: str = None,
        location_name_en: str = None,
        isp_name_en: str = None,
        merge: str = None,
        merge_loc_isp: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.field = field
        self.location_name_en = location_name_en
        self.isp_name_en = isp_name_en
        self.merge = merge
        self.merge_loc_isp = merge_loc_isp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.field is not None:
            result['Field'] = self.field
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.merge is not None:
            result['Merge'] = self.merge
        if self.merge_loc_isp is not None:
            result['MergeLocIsp'] = self.merge_loc_isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('Merge') is not None:
            self.merge = m.get('Merge')
        if m.get('MergeLocIsp') is not None:
            self.merge_loc_isp = m.get('MergeLocIsp')
        return self


class DescribeDcdnDomainRealTimeDetailDataResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnDomainRealTimeDetailDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeDetailDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeDetailDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(TeaModel):
    def __init__(
        self,
        code: str = None,
        proportion: str = None,
        count: str = None,
    ):
        self.code = code
        self.proportion = proportion
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        real_time_code_proportion_data: List[DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData] = None,
    ):
        self.real_time_code_proportion_data = real_time_code_proportion_data

    def validate(self):
        if self.real_time_code_proportion_data:
            for k in self.real_time_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RealTimeCodeProportionData'] = []
        if self.real_time_code_proportion_data is not None:
            for k in self.real_time_code_proportion_data:
                result['RealTimeCodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.real_time_code_proportion_data = []
        if m.get('RealTimeCodeProportionData') is not None:
            for k in m.get('RealTimeCodeProportionData'):
                temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData()
                self.real_time_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        real_time_http_code_data: DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.real_time_http_code_data = real_time_http_code_data

    def validate(self):
        if self.real_time_http_code_data:
            self.real_time_http_code_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_http_code_data is not None:
            result['RealTimeHttpCodeData'] = self.real_time_http_code_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeHttpCodeData') is not None:
            temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(m['RealTimeHttpCodeData'])
        return self


class DescribeDcdnDomainRealTimeHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeHttpCodeDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeQpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeQpsDataResponseBodyDataQpsModel(TeaModel):
    def __init__(
        self,
        qps: float = None,
        time_stamp: str = None,
    ):
        self.qps = qps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeQpsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        qps_model: List[DescribeDcdnDomainRealTimeQpsDataResponseBodyDataQpsModel] = None,
    ):
        self.qps_model = qps_model

    def validate(self):
        if self.qps_model:
            for k in self.qps_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QpsModel'] = []
        if self.qps_model is not None:
            for k in self.qps_model:
                result['QpsModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qps_model = []
        if m.get('QpsModel') is not None:
            for k in m.get('QpsModel'):
                temp_model = DescribeDcdnDomainRealTimeQpsDataResponseBodyDataQpsModel()
                self.qps_model.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDcdnDomainRealTimeQpsDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDcdnDomainRealTimeQpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDcdnDomainRealTimeQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeQpsDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel(TeaModel):
    def __init__(
        self,
        req_hit_rate: float = None,
        time_stamp: str = None,
    ):
        self.req_hit_rate = req_hit_rate
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData(TeaModel):
    def __init__(
        self,
        req_hit_rate_data_model: List[DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel] = None,
    ):
        self.req_hit_rate_data_model = req_hit_rate_data_model

    def validate(self):
        if self.req_hit_rate_data_model:
            for k in self.req_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReqHitRateDataModel'] = []
        if self.req_hit_rate_data_model is not None:
            for k in self.req_hit_rate_data_model:
                result['ReqHitRateDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.req_hit_rate_data_model = []
        if m.get('ReqHitRateDataModel') is not None:
            for k in m.get('ReqHitRateDataModel'):
                temp_model = DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel()
                self.req_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDcdnDomainRealTimeReqHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDcdnDomainRealTimeReqHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeReqHitRateDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        real_time_src_bps_data_per_interval: DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.real_time_src_bps_data_per_interval = real_time_src_bps_data_per_interval

    def validate(self):
        if self.real_time_src_bps_data_per_interval:
            self.real_time_src_bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_src_bps_data_per_interval is not None:
            result['RealTimeSrcBpsDataPerInterval'] = self.real_time_src_bps_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeSrcBpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval()
            self.real_time_src_bps_data_per_interval = temp_model.from_map(m['RealTimeSrcBpsDataPerInterval'])
        return self


class DescribeDcdnDomainRealTimeSrcBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeSrcBpsDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData(TeaModel):
    def __init__(
        self,
        code: str = None,
        proportion: str = None,
        count: str = None,
    ):
        self.code = code
        self.proportion = proportion
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        real_time_src_code_proportion_data: List[DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData] = None,
    ):
        self.real_time_src_code_proportion_data = real_time_src_code_proportion_data

    def validate(self):
        if self.real_time_src_code_proportion_data:
            for k in self.real_time_src_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RealTimeSrcCodeProportionData'] = []
        if self.real_time_src_code_proportion_data is not None:
            for k in self.real_time_src_code_proportion_data:
                result['RealTimeSrcCodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.real_time_src_code_proportion_data = []
        if m.get('RealTimeSrcCodeProportionData') is not None:
            for k in m.get('RealTimeSrcCodeProportionData'):
                temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData()
                self.real_time_src_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        real_time_src_http_code_data: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.real_time_src_http_code_data = real_time_src_http_code_data

    def validate(self):
        if self.real_time_src_http_code_data:
            self.real_time_src_http_code_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_src_http_code_data is not None:
            result['RealTimeSrcHttpCodeData'] = self.real_time_src_http_code_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeSrcHttpCodeData') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData()
            self.real_time_src_http_code_data = temp_model.from_map(m['RealTimeSrcHttpCodeData'])
        return self


class DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeSrcHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        real_time_src_traffic_data_per_interval: DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.real_time_src_traffic_data_per_interval = real_time_src_traffic_data_per_interval

    def validate(self):
        if self.real_time_src_traffic_data_per_interval:
            self.real_time_src_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_src_traffic_data_per_interval is not None:
            result['RealTimeSrcTrafficDataPerInterval'] = self.real_time_src_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeSrcTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval()
            self.real_time_src_traffic_data_per_interval = temp_model.from_map(m['RealTimeSrcTrafficDataPerInterval'])
        return self


class DescribeDcdnDomainRealTimeSrcTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeSrcTrafficDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRealTimeTrafficDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRealTimeTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        real_time_traffic_data_per_interval: DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.real_time_traffic_data_per_interval = real_time_traffic_data_per_interval

    def validate(self):
        if self.real_time_traffic_data_per_interval:
            self.real_time_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_traffic_data_per_interval is not None:
            result['RealTimeTrafficDataPerInterval'] = self.real_time_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeTrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval()
            self.real_time_traffic_data_per_interval = temp_model.from_map(m['RealTimeTrafficDataPerInterval'])
        return self


class DescribeDcdnDomainRealTimeTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRealTimeTrafficDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRealTimeTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainRegionDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(
        self,
        qps: str = None,
        total_query: str = None,
        total_bytes: str = None,
        region_ename: str = None,
        region: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        proportion: str = None,
        avg_object_size: str = None,
        bps: str = None,
        bytes_proportion: str = None,
    ):
        self.qps = qps
        self.total_query = total_query
        self.total_bytes = total_bytes
        self.region_ename = region_ename
        self.region = region
        self.avg_response_rate = avg_response_rate
        self.avg_response_time = avg_response_time
        self.proportion = proportion
        self.avg_object_size = avg_object_size
        self.bps = bps
        self.bytes_proportion = bytes_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.region is not None:
            result['Region'] = self.region
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        return self


class DescribeDcdnDomainRegionDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        region_proportion_data: List[DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData] = None,
    ):
        self.region_proportion_data = region_proportion_data

    def validate(self):
        if self.region_proportion_data:
            for k in self.region_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionProportionData'] = []
        if self.region_proportion_data is not None:
            for k in self.region_proportion_data:
                result['RegionProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_proportion_data = []
        if m.get('RegionProportionData') is not None:
            for k in m.get('RegionProportionData'):
                temp_model = DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainRegionDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        value: DescribeDcdnDomainRegionDataResponseBodyValue = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('Value') is not None:
            temp_model = DescribeDcdnDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDcdnDomainRegionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainRegionDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainRegionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainStagingConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        function_names: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.function_names = function_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        return self


class DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        self.arg_name = arg_name
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        status: str = None,
        config_id: str = None,
        function_name: str = None,
        function_args: List[DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs] = None,
    ):
        self.status = status
        self.config_id = config_id
        self.function_name = function_name
        self.function_args = function_args

    def validate(self):
        if self.function_args:
            for k in self.function_args:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        result['FunctionArgs'] = []
        if self.function_args is not None:
            for k in self.function_args:
                result['FunctionArgs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        self.function_args = []
        if m.get('FunctionArgs') is not None:
            for k in m.get('FunctionArgs'):
                temp_model = DescribeDcdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_configs: List[DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs] = None,
    ):
        self.request_id = request_id
        self.domain_configs = domain_configs

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeDcdnDomainStagingConfigResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainStagingConfigResponseBody = None,
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
            temp_model = DescribeDcdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainTopReferVisitRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        sort_by: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class DescribeDcdnDomainTopReferVisitResponseBodyTopReferListReferList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        visit_data: str = None,
        refer_detail: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.visit_data = visit_data
        self.refer_detail = refer_detail
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.refer_detail is not None:
            result['ReferDetail'] = self.refer_detail
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('ReferDetail') is not None:
            self.refer_detail = m.get('ReferDetail')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopReferVisitResponseBodyTopReferList(TeaModel):
    def __init__(
        self,
        refer_list: List[DescribeDcdnDomainTopReferVisitResponseBodyTopReferListReferList] = None,
    ):
        self.refer_list = refer_list

    def validate(self):
        if self.refer_list:
            for k in self.refer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReferList'] = []
        if self.refer_list is not None:
            for k in self.refer_list:
                result['ReferList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refer_list = []
        if m.get('ReferList') is not None:
            for k in m.get('ReferList'):
                temp_model = DescribeDcdnDomainTopReferVisitResponseBodyTopReferListReferList()
                self.refer_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopReferVisitResponseBody(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        top_refer_list: DescribeDcdnDomainTopReferVisitResponseBodyTopReferList = None,
    ):
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.top_refer_list = top_refer_list

    def validate(self):
        if self.top_refer_list:
            self.top_refer_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.top_refer_list is not None:
            result['TopReferList'] = self.top_refer_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TopReferList') is not None:
            temp_model = DescribeDcdnDomainTopReferVisitResponseBodyTopReferList()
            self.top_refer_list = temp_model.from_map(m['TopReferList'])
        return self


class DescribeDcdnDomainTopReferVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainTopReferVisitResponseBody = None,
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
            temp_model = DescribeDcdnDomainTopReferVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainTopUrlVisitRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        sort_by: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        url_detail: str = None,
        flow_proportion: float = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.url_detail = url_detail
        self.flow_proportion = flow_proportion
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        url_detail: str = None,
        flow_proportion: float = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.url_detail = url_detail
        self.flow_proportion = flow_proportion
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDcdnDomainTopUrlVisitResponseBodyUrl200ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        url_detail: str = None,
        flow_proportion: float = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.url_detail = url_detail
        self.flow_proportion = flow_proportion
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDcdnDomainTopUrlVisitResponseBodyUrl300ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        url_detail: str = None,
        flow_proportion: float = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.url_detail = url_detail
        self.flow_proportion = flow_proportion
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDcdnDomainTopUrlVisitResponseBodyUrl400ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
    def __init__(
        self,
        flow: str = None,
        url_detail: str = None,
        flow_proportion: float = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.url_detail = url_detail
        self.flow_proportion = flow_proportion
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        return self


class DescribeDcdnDomainTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDcdnDomainTopUrlVisitResponseBodyUrl500ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTopUrlVisitResponseBody(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        all_url_list: DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList = None,
        url_200list: DescribeDcdnDomainTopUrlVisitResponseBodyUrl200List = None,
        url_300list: DescribeDcdnDomainTopUrlVisitResponseBodyUrl300List = None,
        url_400list: DescribeDcdnDomainTopUrlVisitResponseBodyUrl400List = None,
        url_500list: DescribeDcdnDomainTopUrlVisitResponseBodyUrl500List = None,
    ):
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.all_url_list = all_url_list
        self.url_200list = url_200list
        self.url_300list = url_300list
        self.url_400list = url_400list
        self.url_500list = url_500list

    def validate(self):
        if self.all_url_list:
            self.all_url_list.validate()
        if self.url_200list:
            self.url_200list.validate()
        if self.url_300list:
            self.url_300list.validate()
        if self.url_400list:
            self.url_400list.validate()
        if self.url_500list:
            self.url_500list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.all_url_list is not None:
            result['AllUrlList'] = self.all_url_list.to_map()
        if self.url_200list is not None:
            result['Url200List'] = self.url_200list.to_map()
        if self.url_300list is not None:
            result['Url300List'] = self.url_300list.to_map()
        if self.url_400list is not None:
            result['Url400List'] = self.url_400list.to_map()
        if self.url_500list is not None:
            result['Url500List'] = self.url_500list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AllUrlList') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        if m.get('Url200List') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url300List') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('Url500List') is not None:
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        return self


class DescribeDcdnDomainTopUrlVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainTopUrlVisitResponseBody = None,
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
            temp_model = DescribeDcdnDomainTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainTrafficDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        static_http_traffic: float = None,
        dynamic_https_traffic: float = None,
        traffic: float = None,
        dynamic_http_traffic: float = None,
        time_stamp: str = None,
        static_https_traffic: float = None,
    ):
        self.static_http_traffic = static_http_traffic
        self.dynamic_https_traffic = dynamic_https_traffic
        self.traffic = traffic
        self.dynamic_http_traffic = dynamic_http_traffic
        self.time_stamp = time_stamp
        self.static_https_traffic = static_https_traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_http_traffic is not None:
            result['StaticHttpTraffic'] = self.static_http_traffic
        if self.dynamic_https_traffic is not None:
            result['DynamicHttpsTraffic'] = self.dynamic_https_traffic
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.dynamic_http_traffic is not None:
            result['DynamicHttpTraffic'] = self.dynamic_http_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.static_https_traffic is not None:
            result['StaticHttpsTraffic'] = self.static_https_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StaticHttpTraffic') is not None:
            self.static_http_traffic = m.get('StaticHttpTraffic')
        if m.get('DynamicHttpsTraffic') is not None:
            self.dynamic_https_traffic = m.get('DynamicHttpsTraffic')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        if m.get('DynamicHttpTraffic') is not None:
            self.dynamic_http_traffic = m.get('DynamicHttpTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('StaticHttpsTraffic') is not None:
            self.static_https_traffic = m.get('StaticHttpsTraffic')
        return self


class DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        traffic_data_per_interval: DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.traffic_data_per_interval = traffic_data_per_interval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeDcdnDomainTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainTrafficDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainUvDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
    def __init__(
        self,
        value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainUvDataResponseBodyUvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DescribeDcdnDomainUvDataResponseBodyUvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainUvDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        uv_data_interval: DescribeDcdnDomainUvDataResponseBodyUvDataInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.uv_data_interval = uv_data_interval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.uv_data_interval is not None:
            result['UvDataInterval'] = self.uv_data_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('UvDataInterval') is not None:
            temp_model = DescribeDcdnDomainUvDataResponseBodyUvDataInterval()
            self.uv_data_interval = temp_model.from_map(m['UvDataInterval'])
        return self


class DescribeDcdnDomainUvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainUvDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainWebsocketBpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        websocket_bps: float = None,
    ):
        self.time_stamp = time_stamp
        self.websocket_bps = websocket_bps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.websocket_bps is not None:
            result['WebsocketBps'] = self.websocket_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('WebsocketBps') is not None:
            self.websocket_bps = m.get('WebsocketBps')
        return self


class DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        bps_data_per_interval: DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.bps_data_per_interval = bps_data_per_interval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        return self


class DescribeDcdnDomainWebsocketBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainWebsocketBpsDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainWebsocketBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerIntervalHttpCodeDataModule(TeaModel):
    def __init__(
        self,
        code: int = None,
        proportion: float = None,
        count: float = None,
    ):
        self.code = code
        self.proportion = proportion
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerInterval(TeaModel):
    def __init__(
        self,
        http_code_data_module: List[DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerIntervalHttpCodeDataModule] = None,
    ):
        self.http_code_data_module = http_code_data_module

    def validate(self):
        if self.http_code_data_module:
            for k in self.http_code_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HttpCodeDataModule'] = []
        if self.http_code_data_module is not None:
            for k in self.http_code_data_module:
                result['HttpCodeDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.http_code_data_module = []
        if m.get('HttpCodeDataModule') is not None:
            for k in m.get('HttpCodeDataModule'):
                temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerIntervalHttpCodeDataModule()
                self.http_code_data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        websocket_http_code_data_per_interval: DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerInterval = None,
    ):
        self.time_stamp = time_stamp
        self.websocket_http_code_data_per_interval = websocket_http_code_data_per_interval

    def validate(self):
        if self.websocket_http_code_data_per_interval:
            self.websocket_http_code_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.websocket_http_code_data_per_interval is not None:
            result['WebsocketHttpCodeDataPerInterval'] = self.websocket_http_code_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('WebsocketHttpCodeDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModuleWebsocketHttpCodeDataPerInterval()
            self.websocket_http_code_data_per_interval = temp_model.from_map(m['WebsocketHttpCodeDataPerInterval'])
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        data_per_interval: DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.data_per_interval = data_per_interval

    def validate(self):
        if self.data_per_interval:
            self.data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.data_per_interval is not None:
            result['DataPerInterval'] = self.data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBodyDataPerInterval()
            self.data_per_interval = temp_model.from_map(m['DataPerInterval'])
        return self


class DescribeDcdnDomainWebsocketHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainWebsocketHttpCodeDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainWebsocketHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnDomainWebsocketTrafficDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        websocket_traffic: float = None,
        time_stamp: str = None,
    ):
        self.websocket_traffic = websocket_traffic
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.websocket_traffic is not None:
            result['WebsocketTraffic'] = self.websocket_traffic
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebsocketTraffic') is not None:
            self.websocket_traffic = m.get('WebsocketTraffic')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        data_interval: str = None,
        traffic_data_per_interval: DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.data_interval = data_interval
        self.traffic_data_per_interval = traffic_data_per_interval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeDcdnDomainWebsocketTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeDcdnDomainWebsocketTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnDomainWebsocketTrafficDataResponseBody = None,
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
            temp_model = DescribeDcdnDomainWebsocketTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnHttpsDomainListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        keyword: str = None,
    ):
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        cert_start_time: str = None,
        cert_expire_time: str = None,
        cert_update_time: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_status: str = None,
        domain_name: str = None,
        cert_common_name: str = None,
    ):
        self.cert_start_time = cert_start_time
        self.cert_expire_time = cert_expire_time
        self.cert_update_time = cert_update_time
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_status = cert_status
        self.domain_name = domain_name
        self.cert_common_name = cert_common_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        return self


class DescribeDcdnHttpsDomainListResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeDcdnHttpsDomainListResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDcdnHttpsDomainListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        cert_infos: DescribeDcdnHttpsDomainListResponseBodyCertInfos = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.cert_infos = cert_infos

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertInfos') is not None:
            temp_model = DescribeDcdnHttpsDomainListResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        return self


class DescribeDcdnHttpsDomainListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnHttpsDomainListResponseBody = None,
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
            temp_model = DescribeDcdnHttpsDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpaDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        function_names: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.function_names = function_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        return self


class DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        self.arg_name = arg_name
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(
        self,
        function_arg: List[DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg] = None,
    ):
        self.function_arg = function_arg

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k in m.get('FunctionArg'):
                temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(
        self,
        status: str = None,
        config_id: str = None,
        function_name: str = None,
        function_args: DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs = None,
    ):
        self.status = status
        self.config_id = config_id
        self.function_name = function_name
        self.function_args = function_args

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        return self


class DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        domain_config: List[DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfig] = None,
    ):
        self.domain_config = domain_config

    def validate(self):
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfig'] = []
        if self.domain_config is not None:
            for k in self.domain_config:
                result['DomainConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_config = []
        if m.get('DomainConfig') is not None:
            for k in m.get('DomainConfig'):
                temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaDomainConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_configs: DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs = None,
    ):
        self.request_id = request_id
        self.domain_configs = domain_configs

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeDcdnIpaDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        return self


class DescribeDcdnIpaDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnIpaDomainConfigsResponseBody = None,
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
            temp_model = DescribeDcdnIpaDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpaDomainDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: str = None,
        enabled: str = None,
        priority: str = None,
        port: int = None,
        content: str = None,
    ):
        self.type = type
        self.weight = weight
        self.enabled = enabled
        self.priority = priority
        self.port = port
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaDomainDetailResponseBodyDomainDetail(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        sslpub: str = None,
        description: str = None,
        sslprotocol: str = None,
        resource_group_id: str = None,
        cert_name: str = None,
        scope: str = None,
        cname: str = None,
        domain_status: str = None,
        gmt_modified: str = None,
        domain_name: str = None,
        sources: DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources = None,
    ):
        self.gmt_created = gmt_created
        self.sslpub = sslpub
        self.description = description
        self.sslprotocol = sslprotocol
        self.resource_group_id = resource_group_id
        self.cert_name = cert_name
        self.scope = scope
        self.cname = cname
        self.domain_status = domain_status
        self.gmt_modified = gmt_modified
        self.domain_name = domain_name
        self.sources = sources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnIpaDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnIpaDomainDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_detail: DescribeDcdnIpaDomainDetailResponseBodyDomainDetail = None,
    ):
        self.request_id = request_id
        self.domain_detail = domain_detail

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainDetail') is not None:
            temp_model = DescribeDcdnIpaDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m['DomainDetail'])
        return self


class DescribeDcdnIpaDomainDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnIpaDomainDetailResponseBody = None,
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
            temp_model = DescribeDcdnIpaDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpaServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason(TeaModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        return self


class DescribeDcdnIpaServiceResponseBodyOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: List[DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k in self.lock_reason:
                result['LockReason'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k in m.get('LockReason'):
                temp_model = DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaServiceResponseBody(TeaModel):
    def __init__(
        self,
        changing_affect_time: str = None,
        request_id: str = None,
        changing_charge_type: str = None,
        opening_time: str = None,
        internet_charge_type: str = None,
        instance_id: str = None,
        operation_locks: DescribeDcdnIpaServiceResponseBodyOperationLocks = None,
    ):
        self.changing_affect_time = changing_affect_time
        self.request_id = request_id
        self.changing_charge_type = changing_charge_type
        self.opening_time = opening_time
        self.internet_charge_type = internet_charge_type
        self.instance_id = instance_id
        self.operation_locks = operation_locks

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeDcdnIpaServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        return self


class DescribeDcdnIpaServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnIpaServiceResponseBody = None,
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
            temp_model = DescribeDcdnIpaServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpaUserDomainsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        page_size: int = None,
        page_number: int = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_search_type: str = None,
        check_domain_show: bool = None,
        resource_group_id: str = None,
        func_id: str = None,
        func_filter: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.page_size = page_size
        self.page_number = page_number
        self.domain_name = domain_name
        self.domain_status = domain_status
        self.domain_search_type = domain_search_type
        self.check_domain_show = check_domain_show
        self.resource_group_id = resource_group_id
        self.func_id = func_id
        self.func_filter = func_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
        if m.get('FuncFilter') is not None:
            self.func_filter = m.get('FuncFilter')
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: str = None,
        priority: str = None,
        port: int = None,
        content: str = None,
    ):
        self.type = type
        self.weight = weight
        self.priority = priority
        self.port = port
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        description: str = None,
        sslprotocol: str = None,
        resource_group_id: str = None,
        sandbox: str = None,
        domain_status: str = None,
        cname: str = None,
        gmt_modified: str = None,
        domain_name: str = None,
        sources: DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSources = None,
    ):
        self.gmt_created = gmt_created
        self.description = description
        self.sslprotocol = sslprotocol
        self.resource_group_id = resource_group_id
        self.sandbox = sandbox
        self.domain_status = domain_status
        self.cname = cname
        self.gmt_modified = gmt_modified
        self.domain_name = domain_name
        self.sources = sources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnIpaUserDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeDcdnIpaUserDomainsResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnIpaUserDomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        domains: DescribeDcdnIpaUserDomainsResponseBodyDomains = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.domains = domains

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Domains') is not None:
            temp_model = DescribeDcdnIpaUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        return self


class DescribeDcdnIpaUserDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnIpaUserDomainsResponseBody = None,
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
            temp_model = DescribeDcdnIpaUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnIpInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        ip: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.ip is not None:
            result['IP'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class DescribeDcdnIpInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        region_ename: str = None,
        region: str = None,
        isp_ename: str = None,
        dcdn_ip: str = None,
        isp: str = None,
    ):
        self.request_id = request_id
        self.region_ename = region_ename
        self.region = region
        self.isp_ename = isp_ename
        self.dcdn_ip = dcdn_ip
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.dcdn_ip is not None:
            result['DcdnIp'] = self.dcdn_ip
        if self.isp is not None:
            result['ISP'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('DcdnIp') is not None:
            self.dcdn_ip = m.get('DcdnIp')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        return self


class DescribeDcdnIpInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnIpInfoResponseBody = None,
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
            temp_model = DescribeDcdnIpInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnOfflineLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnOfflineLogDeliveryResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
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


class DescribeDcdnOfflineLogDeliveryResponseBodyRegions(TeaModel):
    def __init__(
        self,
        oss_id: int = None,
        oss_path_prefix: str = None,
        region_id: str = None,
        area_name: str = None,
        dla_table_name: str = None,
        dla_vc_name: str = None,
        dla_db_name: str = None,
        region_name: str = None,
        area_id: str = None,
        is_overseas: str = None,
        oss_bucket_name: str = None,
        oss_endpoint: str = None,
    ):
        self.oss_id = oss_id
        self.oss_path_prefix = oss_path_prefix
        self.region_id = region_id
        self.area_name = area_name
        self.dla_table_name = dla_table_name
        self.dla_vc_name = dla_vc_name
        self.dla_db_name = dla_db_name
        self.region_name = region_name
        self.area_id = area_id
        self.is_overseas = is_overseas
        self.oss_bucket_name = oss_bucket_name
        self.oss_endpoint = oss_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_id is not None:
            result['OssId'] = self.oss_id
        if self.oss_path_prefix is not None:
            result['OssPathPrefix'] = self.oss_path_prefix
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.dla_table_name is not None:
            result['DlaTableName'] = self.dla_table_name
        if self.dla_vc_name is not None:
            result['DlaVcName'] = self.dla_vc_name
        if self.dla_db_name is not None:
            result['DlaDbName'] = self.dla_db_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssId') is not None:
            self.oss_id = m.get('OssId')
        if m.get('OssPathPrefix') is not None:
            self.oss_path_prefix = m.get('OssPathPrefix')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('DlaTableName') is not None:
            self.dla_table_name = m.get('DlaTableName')
        if m.get('DlaVcName') is not None:
            self.dla_vc_name = m.get('DlaVcName')
        if m.get('DlaDbName') is not None:
            self.dla_db_name = m.get('DlaDbName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        return self


class DescribeDcdnOfflineLogDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        fields: List[str] = None,
        domains: List[DescribeDcdnOfflineLogDeliveryResponseBodyDomains] = None,
        regions: List[DescribeDcdnOfflineLogDeliveryResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.fields = fields
        self.domains = domains
        self.regions = regions

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.fields is not None:
            result['Fields'] = self.fields
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = DescribeDcdnOfflineLogDeliveryResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeDcdnOfflineLogDeliveryResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeDcdnOfflineLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnOfflineLogDeliveryResponseBody = None,
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
            temp_model = DescribeDcdnOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnOfflineLogDeliveryFieldRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnOfflineLogDeliveryFieldResponseBodyFields(TeaModel):
    def __init__(
        self,
        description: str = None,
        field_id: str = None,
        field_name: str = None,
    ):
        self.description = description
        self.field_id = field_id
        self.field_name = field_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.field_id is not None:
            result['FieldId'] = self.field_id
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        return self


class DescribeDcdnOfflineLogDeliveryFieldResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        fields: List[DescribeDcdnOfflineLogDeliveryFieldResponseBodyFields] = None,
    ):
        self.request_id = request_id
        self.fields = fields

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = DescribeDcdnOfflineLogDeliveryFieldResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        return self


class DescribeDcdnOfflineLogDeliveryFieldResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnOfflineLogDeliveryFieldResponseBody = None,
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
            temp_model = DescribeDcdnOfflineLogDeliveryFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnOfflineLogDeliveryRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreasRegionInfos(TeaModel):
    def __init__(
        self,
        is_overseas: str = None,
        region_name: str = None,
        oss_endpoint: str = None,
        region_id: str = None,
    ):
        self.is_overseas = is_overseas
        self.region_name = region_name
        self.oss_endpoint = oss_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreas(TeaModel):
    def __init__(
        self,
        area_name: str = None,
        area_id: str = None,
        region_infos: List[DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreasRegionInfos] = None,
    ):
        self.area_name = area_name
        self.area_id = area_id
        self.region_infos = region_infos

    def validate(self):
        if self.region_infos:
            for k in self.region_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        result['RegionInfos'] = []
        if self.region_infos is not None:
            for k in self.region_infos:
                result['RegionInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        self.region_infos = []
        if m.get('RegionInfos') is not None:
            for k in m.get('RegionInfos'):
                temp_model = DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreasRegionInfos()
                self.region_infos.append(temp_model.from_map(k))
        return self


class DescribeDcdnOfflineLogDeliveryRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        areas: List[DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreas] = None,
    ):
        self.request_id = request_id
        self.areas = areas

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = DescribeDcdnOfflineLogDeliveryRegionsResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        return self


class DescribeDcdnOfflineLogDeliveryRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnOfflineLogDeliveryRegionsResponseBody = None,
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
            temp_model = DescribeDcdnOfflineLogDeliveryRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnOfflineLogDeliveryStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnOfflineLogDeliveryStatusResponseBody(TeaModel):
    def __init__(
        self,
        open_status: str = None,
        request_id: str = None,
    ):
        self.open_status = open_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_status is not None:
            result['OpenStatus'] = self.open_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnOfflineLogDeliveryStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnOfflineLogDeliveryStatusResponseBody = None,
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
            temp_model = DescribeDcdnOfflineLogDeliveryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRefreshQuotaRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnRefreshQuotaResponseBody(TeaModel):
    def __init__(
        self,
        block_quota: str = None,
        preload_remain: str = None,
        request_id: str = None,
        block_remain: str = None,
        dir_remain: str = None,
        url_remain: str = None,
        dir_quota: str = None,
        url_quota: str = None,
        preload_quota: str = None,
    ):
        self.block_quota = block_quota
        self.preload_remain = preload_remain
        self.request_id = request_id
        self.block_remain = block_remain
        self.dir_remain = dir_remain
        self.url_remain = url_remain
        self.dir_quota = dir_quota
        self.url_quota = url_quota
        self.preload_quota = preload_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.block_remain is not None:
            result['blockRemain'] = self.block_remain
        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain
        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain
        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota
        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('blockRemain') is not None:
            self.block_remain = m.get('blockRemain')
        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        return self


class DescribeDcdnRefreshQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnRefreshQuotaResponseBody = None,
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
            temp_model = DescribeDcdnRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRefreshTaskByIdRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        task_id: str = None,
    ):
        self.owner_id = owner_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDcdnRefreshTaskByIdResponseBodyTasks(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        object_type: str = None,
        process: str = None,
        description: str = None,
        object_path: str = None,
        task_id: str = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.object_type = object_type
        self.process = process
        self.description = description
        self.object_path = object_path
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDcdnRefreshTaskByIdResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        tasks: List[DescribeDcdnRefreshTaskByIdResponseBodyTasks] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
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
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribeDcdnRefreshTaskByIdResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DescribeDcdnRefreshTaskByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnRefreshTaskByIdResponseBody = None,
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
            temp_model = DescribeDcdnRefreshTaskByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRefreshTasksRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        task_id: str = None,
        object_path: str = None,
        page_number: int = None,
        object_type: str = None,
        domain_name: str = None,
        status: str = None,
        page_size: int = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.task_id = task_id
        self.object_path = object_path
        self.page_number = page_number
        self.object_type = object_type
        self.domain_name = domain_name
        self.status = status
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnRefreshTasksResponseBodyTasksTask(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        object_type: str = None,
        process: str = None,
        description: str = None,
        object_path: str = None,
        task_id: str = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.object_type = object_type
        self.process = process
        self.description = description
        self.object_path = object_path
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDcdnRefreshTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        task: List[DescribeDcdnRefreshTasksResponseBodyTasksTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = DescribeDcdnRefreshTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeDcdnRefreshTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        tasks: DescribeDcdnRefreshTasksResponseBodyTasks = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Tasks') is not None:
            temp_model = DescribeDcdnRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        return self


class DescribeDcdnRefreshTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnRefreshTasksResponseBody = None,
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
            temp_model = DescribeDcdnRefreshTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnRegionAndIspRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnRegionAndIspResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        name_en: str = None,
        name_zh: str = None,
    ):
        self.name_en = name_en
        self.name_zh = name_zh

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.name_zh is not None:
            result['NameZh'] = self.name_zh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('NameZh') is not None:
            self.name_zh = m.get('NameZh')
        return self


class DescribeDcdnRegionAndIspResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeDcdnRegionAndIspResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeDcdnRegionAndIspResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeDcdnRegionAndIspResponseBodyIspsIsp(TeaModel):
    def __init__(
        self,
        name_en: str = None,
        name_zh: str = None,
    ):
        self.name_en = name_en
        self.name_zh = name_zh

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.name_zh is not None:
            result['NameZh'] = self.name_zh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('NameZh') is not None:
            self.name_zh = m.get('NameZh')
        return self


class DescribeDcdnRegionAndIspResponseBodyIsps(TeaModel):
    def __init__(
        self,
        isp: List[DescribeDcdnRegionAndIspResponseBodyIspsIsp] = None,
    ):
        self.isp = isp

    def validate(self):
        if self.isp:
            for k in self.isp:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Isp'] = []
        if self.isp is not None:
            for k in self.isp:
                result['Isp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp = []
        if m.get('Isp') is not None:
            for k in m.get('Isp'):
                temp_model = DescribeDcdnRegionAndIspResponseBodyIspsIsp()
                self.isp.append(temp_model.from_map(k))
        return self


class DescribeDcdnRegionAndIspResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeDcdnRegionAndIspResponseBodyRegions = None,
        isps: DescribeDcdnRegionAndIspResponseBodyIsps = None,
    ):
        self.request_id = request_id
        self.regions = regions
        self.isps = isps

    def validate(self):
        if self.regions:
            self.regions.validate()
        if self.isps:
            self.isps.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.isps is not None:
            result['Isps'] = self.isps.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeDcdnRegionAndIspResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('Isps') is not None:
            temp_model = DescribeDcdnRegionAndIspResponseBodyIsps()
            self.isps = temp_model.from_map(m['Isps'])
        return self


class DescribeDcdnRegionAndIspResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnRegionAndIspResponseBody = None,
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
            temp_model = DescribeDcdnRegionAndIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnReportRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        report_id: int = None,
        area: str = None,
        is_overseas: str = None,
        http_code: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.report_id = report_id
        self.area = area
        self.is_overseas = is_overseas
        self.http_code = http_code
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.area is not None:
            result['Area'] = self.area
        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnReportResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnReportResponseBody = None,
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
            temp_model = DescribeDcdnReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnReportListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        report_id: int = None,
        status: str = None,
        permission: str = None,
    ):
        self.owner_id = owner_id
        self.report_id = report_id
        self.status = status
        self.permission = permission

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.status is not None:
            result['Status'] = self.status
        if self.permission is not None:
            result['Permission'] = self.permission
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        return self


class DescribeDcdnReportListResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnReportListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnReportListResponseBody = None,
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
            temp_model = DescribeDcdnReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnSecFuncInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        sec_func_type: str = None,
        lang: str = None,
    ):
        self.owner_id = owner_id
        self.sec_func_type = sec_func_type
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sec_func_type is not None:
            result['SecFuncType'] = self.sec_func_type
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecFuncType') is not None:
            self.sec_func_type = m.get('SecFuncType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeDcdnSecFuncInfoResponseBodyContent(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnSecFuncInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        description: str = None,
        ret_code: str = None,
        http_status: str = None,
        content: List[DescribeDcdnSecFuncInfoResponseBodyContent] = None,
    ):
        self.request_id = request_id
        self.description = description
        self.ret_code = ret_code
        self.http_status = http_status
        self.content = content

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeDcdnSecFuncInfoResponseBodyContent()
                self.content.append(temp_model.from_map(k))
        return self


class DescribeDcdnSecFuncInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnSecFuncInfoResponseBody = None,
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
            temp_model = DescribeDcdnSecFuncInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnServiceResponseBodyOperationLocksLockReason(TeaModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        return self


class DescribeDcdnServiceResponseBodyOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: List[DescribeDcdnServiceResponseBodyOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k in self.lock_reason:
                result['LockReason'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k in m.get('LockReason'):
                temp_model = DescribeDcdnServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeDcdnServiceResponseBody(TeaModel):
    def __init__(
        self,
        websocket_changing_time: str = None,
        websocket_changing_type: str = None,
        changing_affect_time: str = None,
        changing_charge_type: str = None,
        request_id: str = None,
        opening_time: str = None,
        internet_charge_type: str = None,
        websocket_type: str = None,
        instance_id: str = None,
        operation_locks: DescribeDcdnServiceResponseBodyOperationLocks = None,
    ):
        self.websocket_changing_time = websocket_changing_time
        self.websocket_changing_type = websocket_changing_type
        self.changing_affect_time = changing_affect_time
        self.changing_charge_type = changing_charge_type
        self.request_id = request_id
        self.opening_time = opening_time
        self.internet_charge_type = internet_charge_type
        self.websocket_type = websocket_type
        self.instance_id = instance_id
        self.operation_locks = operation_locks

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.websocket_changing_time is not None:
            result['WebsocketChangingTime'] = self.websocket_changing_time
        if self.websocket_changing_type is not None:
            result['WebsocketChangingType'] = self.websocket_changing_type
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.websocket_type is not None:
            result['WebsocketType'] = self.websocket_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebsocketChangingTime') is not None:
            self.websocket_changing_time = m.get('WebsocketChangingTime')
        if m.get('WebsocketChangingType') is not None:
            self.websocket_changing_type = m.get('WebsocketChangingType')
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('WebsocketType') is not None:
            self.websocket_type = m.get('WebsocketType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeDcdnServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        return self


class DescribeDcdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnServiceResponseBody = None,
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
            temp_model = DescribeDcdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnStagingIpRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnStagingIpResponseBodyIPV4s(TeaModel):
    def __init__(
        self,
        ipv4: List[str] = None,
    ):
        self.ipv4 = ipv4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv4 is not None:
            result['IPV4'] = self.ipv4
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPV4') is not None:
            self.ipv4 = m.get('IPV4')
        return self


class DescribeDcdnStagingIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ipv4s: DescribeDcdnStagingIpResponseBodyIPV4s = None,
    ):
        self.request_id = request_id
        self.ipv4s = ipv4s

    def validate(self):
        if self.ipv4s:
            self.ipv4s.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ipv4s is not None:
            result['IPV4s'] = self.ipv4s.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IPV4s') is not None:
            temp_model = DescribeDcdnStagingIpResponseBodyIPV4s()
            self.ipv4s = temp_model.from_map(m['IPV4s'])
        return self


class DescribeDcdnStagingIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnStagingIpResponseBody = None,
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
            temp_model = DescribeDcdnStagingIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnSubListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        status: str = None,
    ):
        self.owner_id = owner_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDcdnSubListResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnSubListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnSubListResponseBody = None,
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
            temp_model = DescribeDcdnSubListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnTagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[DescribeDcdnTagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDcdnTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDcdnTagResourcesResponseBodyTagResourcesTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        tag: List[DescribeDcdnTagResourcesResponseBodyTagResourcesTag] = None,
    ):
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDcdnTagResourcesResponseBodyTagResourcesTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDcdnTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_resources: List[DescribeDcdnTagResourcesResponseBodyTagResources] = None,
    ):
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = DescribeDcdnTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeDcdnTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnTagResourcesResponseBody = None,
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
            temp_model = DescribeDcdnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnTopDomainsByFlowRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        limit: int = None,
    ):
        self.owner_id = owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(
        self,
        max_bps: int = None,
        rank: int = None,
        total_access: int = None,
        traffic_percent: str = None,
        domain_name: str = None,
        total_traffic: str = None,
        max_bps_time: str = None,
    ):
        self.max_bps = max_bps
        self.rank = rank
        self.total_access = total_access
        self.traffic_percent = traffic_percent
        self.domain_name = domain_name
        self.total_traffic = total_traffic
        self.max_bps_time = max_bps_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.traffic_percent is not None:
            result['TrafficPercent'] = self.traffic_percent
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TrafficPercent') is not None:
            self.traffic_percent = m.get('TrafficPercent')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        return self


class DescribeDcdnTopDomainsByFlowResponseBodyTopDomains(TeaModel):
    def __init__(
        self,
        top_domain: List[DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain] = None,
    ):
        self.top_domain = top_domain

    def validate(self):
        if self.top_domain:
            for k in self.top_domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopDomain'] = []
        if self.top_domain is not None:
            for k in self.top_domain:
                result['TopDomain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.top_domain = []
        if m.get('TopDomain') is not None:
            for k in m.get('TopDomain'):
                temp_model = DescribeDcdnTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        return self


class DescribeDcdnTopDomainsByFlowResponseBody(TeaModel):
    def __init__(
        self,
        domain_online_count: int = None,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        domain_count: int = None,
        top_domains: DescribeDcdnTopDomainsByFlowResponseBodyTopDomains = None,
    ):
        self.domain_online_count = domain_online_count
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.domain_count = domain_count
        self.top_domains = top_domains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('TopDomains') is not None:
            temp_model = DescribeDcdnTopDomainsByFlowResponseBodyTopDomains()
            self.top_domains = temp_model.from_map(m['TopDomains'])
        return self


class DescribeDcdnTopDomainsByFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnTopDomainsByFlowResponseBody = None,
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
            temp_model = DescribeDcdnTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserBillHistoryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem(TeaModel):
    def __init__(
        self,
        flow: float = None,
        bandwidth: float = None,
        count: float = None,
        cdn_region: str = None,
        charge_type: str = None,
    ):
        self.flow = flow
        self.bandwidth = bandwidth
        self.count = count
        self.cdn_region = cdn_region
        self.charge_type = charge_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.count is not None:
            result['Count'] = self.count
        if self.cdn_region is not None:
            result['CdnRegion'] = self.cdn_region
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CdnRegion') is not None:
            self.cdn_region = m.get('CdnRegion')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData(TeaModel):
    def __init__(
        self,
        billing_data_item: List[DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem] = None,
    ):
        self.billing_data_item = billing_data_item

    def validate(self):
        if self.billing_data_item:
            for k in self.billing_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillingDataItem'] = []
        if self.billing_data_item is not None:
            for k in self.billing_data_item:
                result['BillingDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.billing_data_item = []
        if m.get('BillingDataItem') is not None:
            for k in m.get('BillingDataItem'):
                temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem()
                self.billing_data_item.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem(TeaModel):
    def __init__(
        self,
        dimension: str = None,
        bill_type: str = None,
        bill_time: str = None,
        billing_data: DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData = None,
    ):
        self.dimension = dimension
        self.bill_type = bill_type
        self.bill_time = bill_time
        self.billing_data = billing_data

    def validate(self):
        if self.billing_data:
            self.billing_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.bill_time is not None:
            result['BillTime'] = self.bill_time
        if self.billing_data is not None:
            result['BillingData'] = self.billing_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BillTime') is not None:
            self.bill_time = m.get('BillTime')
        if m.get('BillingData') is not None:
            temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData()
            self.billing_data = temp_model.from_map(m['BillingData'])
        return self


class DescribeDcdnUserBillHistoryResponseBodyBillHistoryData(TeaModel):
    def __init__(
        self,
        bill_history_data_item: List[DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem] = None,
    ):
        self.bill_history_data_item = bill_history_data_item

    def validate(self):
        if self.bill_history_data_item:
            for k in self.bill_history_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillHistoryDataItem'] = []
        if self.bill_history_data_item is not None:
            for k in self.bill_history_data_item:
                result['BillHistoryDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_history_data_item = []
        if m.get('BillHistoryDataItem') is not None:
            for k in m.get('BillHistoryDataItem'):
                temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem()
                self.bill_history_data_item.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserBillHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bill_history_data: DescribeDcdnUserBillHistoryResponseBodyBillHistoryData = None,
    ):
        self.request_id = request_id
        self.bill_history_data = bill_history_data

    def validate(self):
        if self.bill_history_data:
            self.bill_history_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bill_history_data is not None:
            result['BillHistoryData'] = self.bill_history_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BillHistoryData') is not None:
            temp_model = DescribeDcdnUserBillHistoryResponseBodyBillHistoryData()
            self.bill_history_data = temp_model.from_map(m['BillHistoryData'])
        return self


class DescribeDcdnUserBillHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserBillHistoryResponseBody = None,
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
            temp_model = DescribeDcdnUserBillHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserBillTypeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        billing_cycle: str = None,
        product: str = None,
        bill_type: str = None,
        dimension: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.billing_cycle = billing_cycle
        self.product = product
        self.bill_type = bill_type
        self.dimension = dimension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product is not None:
            result['Product'] = self.product
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        return self


class DescribeDcdnUserBillTypeResponseBodyBillTypeData(TeaModel):
    def __init__(
        self,
        bill_type_data_item: List[DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem] = None,
    ):
        self.bill_type_data_item = bill_type_data_item

    def validate(self):
        if self.bill_type_data_item:
            for k in self.bill_type_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillTypeDataItem'] = []
        if self.bill_type_data_item is not None:
            for k in self.bill_type_data_item:
                result['BillTypeDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_type_data_item = []
        if m.get('BillTypeDataItem') is not None:
            for k in m.get('BillTypeDataItem'):
                temp_model = DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem()
                self.bill_type_data_item.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserBillTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bill_type_data: DescribeDcdnUserBillTypeResponseBodyBillTypeData = None,
    ):
        self.request_id = request_id
        self.bill_type_data = bill_type_data

    def validate(self):
        if self.bill_type_data:
            self.bill_type_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bill_type_data is not None:
            result['BillTypeData'] = self.bill_type_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BillTypeData') is not None:
            temp_model = DescribeDcdnUserBillTypeResponseBodyBillTypeData()
            self.bill_type_data = temp_model.from_map(m['BillTypeData'])
        return self


class DescribeDcdnUserBillTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserBillTypeResponseBody = None,
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
            temp_model = DescribeDcdnUserBillTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserDomainsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnUserDomainsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        page_size: int = None,
        page_number: int = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_search_type: str = None,
        check_domain_show: bool = None,
        resource_group_id: str = None,
        change_start_time: str = None,
        change_end_time: str = None,
        tag: List[DescribeDcdnUserDomainsRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.page_size = page_size
        self.page_number = page_number
        self.domain_name = domain_name
        self.domain_status = domain_status
        self.domain_search_type = domain_search_type
        self.check_domain_show = check_domain_show
        self.resource_group_id = resource_group_id
        self.change_start_time = change_start_time
        self.change_end_time = change_end_time
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDcdnUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: str = None,
        priority: str = None,
        port: int = None,
        content: str = None,
    ):
        self.type = type
        self.weight = weight
        self.priority = priority
        self.port = port
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        description: str = None,
        sslprotocol: str = None,
        resource_group_id: str = None,
        sandbox: str = None,
        domain_status: str = None,
        cname: str = None,
        gmt_modified: str = None,
        domain_name: str = None,
        sources: DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources = None,
    ):
        self.gmt_created = gmt_created
        self.description = description
        self.sslprotocol = sslprotocol
        self.resource_group_id = resource_group_id
        self.sandbox = sandbox
        self.domain_status = domain_status
        self.cname = cname
        self.gmt_modified = gmt_modified
        self.domain_name = domain_name
        self.sources = sources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnUserDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeDcdnUserDomainsResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = DescribeDcdnUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        domains: DescribeDcdnUserDomainsResponseBodyDomains = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.domains = domains

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Domains') is not None:
            temp_model = DescribeDcdnUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        return self


class DescribeDcdnUserDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserDomainsResponseBody = None,
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
            temp_model = DescribeDcdnUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserDomainsByFuncRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        func_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.func_id = func_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: str = None,
        priority: str = None,
        port: int = None,
        content: str = None,
    ):
        self.type = type
        self.weight = weight
        self.priority = priority
        self.port = port
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        ssl_protocol: str = None,
        description: str = None,
        resource_group_id: str = None,
        sandbox: str = None,
        domain_status: str = None,
        cname: str = None,
        gmt_modified: str = None,
        cdn_type: str = None,
        domain_name: str = None,
        sources: DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources = None,
    ):
        self.gmt_created = gmt_created
        self.ssl_protocol = ssl_protocol
        self.description = description
        self.resource_group_id = resource_group_id
        self.sandbox = sandbox
        self.domain_status = domain_status
        self.cname = cname
        self.gmt_modified = gmt_modified
        self.cdn_type = cdn_type
        self.domain_name = domain_name
        self.sources = sources

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        return self


class DescribeDcdnUserDomainsByFuncResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserDomainsByFuncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        domains: DescribeDcdnUserDomainsByFuncResponseBodyDomains = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.domains = domains

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Domains') is not None:
            temp_model = DescribeDcdnUserDomainsByFuncResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        return self


class DescribeDcdnUserDomainsByFuncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserDomainsByFuncResponseBody = None,
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
            temp_model = DescribeDcdnUserDomainsByFuncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserQuotaRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnUserQuotaResponseBody(TeaModel):
    def __init__(
        self,
        block_quota: int = None,
        refresh_url_remain: int = None,
        domain_quota: int = None,
        block_remain: int = None,
        preload_remain: int = None,
        request_id: str = None,
        refresh_url_quota: int = None,
        preload_quota: int = None,
        refresh_dir_quota: int = None,
        refresh_dir_remain: int = None,
    ):
        self.block_quota = block_quota
        self.refresh_url_remain = refresh_url_remain
        self.domain_quota = domain_quota
        self.block_remain = block_remain
        self.preload_remain = preload_remain
        self.request_id = request_id
        self.refresh_url_quota = refresh_url_quota
        self.preload_quota = preload_quota
        self.refresh_dir_quota = refresh_dir_quota
        self.refresh_dir_remain = refresh_dir_remain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.refresh_url_remain is not None:
            result['RefreshUrlRemain'] = self.refresh_url_remain
        if self.domain_quota is not None:
            result['DomainQuota'] = self.domain_quota
        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refresh_url_quota is not None:
            result['RefreshUrlQuota'] = self.refresh_url_quota
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        if self.refresh_dir_quota is not None:
            result['RefreshDirQuota'] = self.refresh_dir_quota
        if self.refresh_dir_remain is not None:
            result['RefreshDirRemain'] = self.refresh_dir_remain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('RefreshUrlRemain') is not None:
            self.refresh_url_remain = m.get('RefreshUrlRemain')
        if m.get('DomainQuota') is not None:
            self.domain_quota = m.get('DomainQuota')
        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefreshUrlQuota') is not None:
            self.refresh_url_quota = m.get('RefreshUrlQuota')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        if m.get('RefreshDirQuota') is not None:
            self.refresh_dir_quota = m.get('RefreshDirQuota')
        if m.get('RefreshDirRemain') is not None:
            self.refresh_dir_remain = m.get('RefreshDirRemain')
        return self


class DescribeDcdnUserQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserQuotaResponseBody = None,
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
            temp_model = DescribeDcdnUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserResourcePackageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        status: str = None,
        display_name: str = None,
        start_time: str = None,
        commodity_code: str = None,
        curr_capacity: str = None,
        init_capacity: str = None,
        instance_id: str = None,
        template_name: str = None,
    ):
        self.end_time = end_time
        self.status = status
        self.display_name = display_name
        self.start_time = start_time
        self.commodity_code = commodity_code
        self.curr_capacity = curr_capacity
        self.init_capacity = init_capacity
        self.instance_id = instance_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfos(TeaModel):
    def __init__(
        self,
        resource_package_info: List[DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo] = None,
    ):
        self.resource_package_info = resource_package_info

    def validate(self):
        if self.resource_package_info:
            for k in self.resource_package_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourcePackageInfo'] = []
        if self.resource_package_info is not None:
            for k in self.resource_package_info:
                result['ResourcePackageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_package_info = []
        if m.get('ResourcePackageInfo') is not None:
            for k in m.get('ResourcePackageInfo'):
                temp_model = DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserResourcePackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_package_infos: DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfos = None,
    ):
        self.request_id = request_id
        self.resource_package_infos = resource_package_infos

    def validate(self):
        if self.resource_package_infos:
            self.resource_package_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_package_infos is not None:
            result['ResourcePackageInfos'] = self.resource_package_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourcePackageInfos') is not None:
            temp_model = DescribeDcdnUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m['ResourcePackageInfos'])
        return self


class DescribeDcdnUserResourcePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserResourcePackageResponseBody = None,
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
            temp_model = DescribeDcdnUserResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserSecDropRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        data: str = None,
        sec_func: str = None,
        metric: str = None,
    ):
        self.owner_id = owner_id
        self.data = data
        self.sec_func = sec_func
        self.metric = metric

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.data is not None:
            result['Data'] = self.data
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        if self.metric is not None:
            result['Metric'] = self.metric
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        return self


class DescribeDcdnUserSecDropResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        request_id: str = None,
        drops: int = None,
        uuid_str: str = None,
    ):
        self.msg = msg
        self.request_id = request_id
        self.drops = drops
        self.uuid_str = uuid_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.drops is not None:
            result['Drops'] = self.drops
        if self.uuid_str is not None:
            result['UuidStr'] = self.uuid_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Drops') is not None:
            self.drops = m.get('Drops')
        if m.get('UuidStr') is not None:
            self.uuid_str = m.get('UuidStr')
        return self


class DescribeDcdnUserSecDropResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserSecDropResponseBody = None,
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
            temp_model = DescribeDcdnUserSecDropResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserSecDropByMinuteRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        sec_func: str = None,
        rule_name: str = None,
        object: str = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        lang: str = None,
    ):
        self.owner_id = owner_id
        self.sec_func = sec_func
        self.rule_name = rule_name
        self.object = object
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.object is not None:
            result['Object'] = self.object
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeDcdnUserSecDropByMinuteResponseBodyRows(TeaModel):
    def __init__(
        self,
        domain: str = None,
        tm_str: str = None,
        drops: int = None,
        object: str = None,
        sec_func: str = None,
        rule_name: str = None,
    ):
        self.domain = domain
        self.tm_str = tm_str
        self.drops = drops
        self.object = object
        self.sec_func = sec_func
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.tm_str is not None:
            result['TmStr'] = self.tm_str
        if self.drops is not None:
            result['Drops'] = self.drops
        if self.object is not None:
            result['Object'] = self.object
        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('TmStr') is not None:
            self.tm_str = m.get('TmStr')
        if m.get('Drops') is not None:
            self.drops = m.get('Drops')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeDcdnUserSecDropByMinuteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        description: str = None,
        len: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        rows: List[DescribeDcdnUserSecDropByMinuteResponseBodyRows] = None,
    ):
        self.request_id = request_id
        self.description = description
        self.len = len
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.rows = rows

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.len is not None:
            result['Len'] = self.len
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['Rows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Len') is not None:
            self.len = m.get('Len')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.rows = []
        if m.get('Rows') is not None:
            for k in m.get('Rows'):
                temp_model = DescribeDcdnUserSecDropByMinuteResponseBodyRows()
                self.rows.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserSecDropByMinuteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserSecDropByMinuteResponseBody = None,
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
            temp_model = DescribeDcdnUserSecDropByMinuteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnUserTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDcdnUserTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDcdnUserTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[DescribeDcdnUserTagsResponseBodyTags] = None,
    ):
        self.request_id = request_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDcdnUserTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeDcdnUserTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnUserTagsResponseBody = None,
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
            temp_model = DescribeDcdnUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnVerifyContentRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnVerifyContentResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDcdnVerifyContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnVerifyContentResponseBody = None,
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
            temp_model = DescribeDcdnVerifyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDcdnWafDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDcdnWafDomainResponseBodyOutPutDomains(TeaModel):
    def __init__(
        self,
        acl_status: int = None,
        status: int = None,
        domain: str = None,
        cc_status: int = None,
        waf_status: int = None,
    ):
        self.acl_status = acl_status
        self.status = status
        self.domain = domain
        self.cc_status = cc_status
        self.waf_status = waf_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cc_status is not None:
            result['CcStatus'] = self.cc_status
        if self.waf_status is not None:
            result['WafStatus'] = self.waf_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CcStatus') is not None:
            self.cc_status = m.get('CcStatus')
        if m.get('WafStatus') is not None:
            self.waf_status = m.get('WafStatus')
        return self


class DescribeDcdnWafDomainResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        out_put_domains: List[DescribeDcdnWafDomainResponseBodyOutPutDomains] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.out_put_domains = out_put_domains

    def validate(self):
        if self.out_put_domains:
            for k in self.out_put_domains:
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
        result['OutPutDomains'] = []
        if self.out_put_domains is not None:
            for k in self.out_put_domains:
                result['OutPutDomains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.out_put_domains = []
        if m.get('OutPutDomains') is not None:
            for k in m.get('OutPutDomains'):
                temp_model = DescribeDcdnWafDomainResponseBodyOutPutDomains()
                self.out_put_domains.append(temp_model.from_map(k))
        return self


class DescribeDcdnWafDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDcdnWafDomainResponseBody = None,
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
            temp_model = DescribeDcdnWafDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
    ):
        self.owner_id = owner_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeRoutineResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRoutineResponseBody = None,
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
            temp_model = DescribeRoutineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineCanaryEnvsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRoutineCanaryEnvsResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineCanaryEnvsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRoutineCanaryEnvsResponseBody = None,
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
            temp_model = DescribeRoutineCanaryEnvsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineCodeRevisionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        select_code_revision: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.select_code_revision = select_code_revision

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        return self


class DescribeRoutineCodeRevisionResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineCodeRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRoutineCodeRevisionResponseBody = None,
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
            temp_model = DescribeRoutineCodeRevisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineSpecRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRoutineSpecResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRoutineSpecResponseBody = None,
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
            temp_model = DescribeRoutineSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoutineUserInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRoutineUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRoutineUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRoutineUserInfoResponseBody = None,
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
            temp_model = DescribeRoutineUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDcdnIpaStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUserDcdnIpaStatusResponseBody(TeaModel):
    def __init__(
        self,
        in_debt: bool = None,
        on_service: bool = None,
        request_id: str = None,
        in_debt_overdue: bool = None,
        enabled: bool = None,
    ):
        self.in_debt = in_debt
        self.on_service = on_service
        self.request_id = request_id
        self.in_debt_overdue = in_debt_overdue
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeUserDcdnIpaStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserDcdnIpaStatusResponseBody = None,
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
            temp_model = DescribeUserDcdnIpaStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDcdnStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUserDcdnStatusResponseBody(TeaModel):
    def __init__(
        self,
        in_debt: bool = None,
        on_service: bool = None,
        request_id: str = None,
        in_debt_overdue: bool = None,
        enabled: bool = None,
    ):
        self.in_debt = in_debt
        self.on_service = on_service
        self.request_id = request_id
        self.in_debt_overdue = in_debt_overdue
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeUserDcdnStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserDcdnStatusResponseBody = None,
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
            temp_model = DescribeUserDcdnStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserErStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUserErStatusResponseBody(TeaModel):
    def __init__(
        self,
        in_debt: bool = None,
        on_service: bool = None,
        request_id: str = None,
        in_debt_overdue: bool = None,
        enabled: bool = None,
    ):
        self.in_debt = in_debt
        self.on_service = on_service
        self.request_id = request_id
        self.in_debt_overdue = in_debt_overdue
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeUserErStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserErStatusResponseBody = None,
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
            temp_model = DescribeUserErStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserLogserviceStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUserLogserviceStatusResponseBody(TeaModel):
    def __init__(
        self,
        in_debt: bool = None,
        on_service: bool = None,
        request_id: str = None,
        in_debt_overdue: bool = None,
        enabled: bool = None,
    ):
        self.in_debt = in_debt
        self.on_service = on_service
        self.request_id = request_id
        self.in_debt_overdue = in_debt_overdue
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.on_service is not None:
            result['OnService'] = self.on_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeUserLogserviceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserLogserviceStatusResponseBody = None,
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
            temp_model = DescribeUserLogserviceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDcdnDomainOfflineLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DisableDcdnDomainOfflineLogDeliveryResponseBody(TeaModel):
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


class DisableDcdnDomainOfflineLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableDcdnDomainOfflineLogDeliveryResponseBody = None,
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
            temp_model = DisableDcdnDomainOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDcdnOfflineLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DisableDcdnOfflineLogDeliveryResponseBody(TeaModel):
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


class DisableDcdnOfflineLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableDcdnOfflineLogDeliveryResponseBody = None,
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
            temp_model = DisableDcdnOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditRoutineConfRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        description: str = None,
        env_conf: Dict[str, Any] = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.description = description
        self.env_conf = env_conf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        return self


class EditRoutineConfShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        description: str = None,
        env_conf_shrink: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.description = description
        self.env_conf_shrink = env_conf_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf_shrink is not None:
            result['EnvConf'] = self.env_conf_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf_shrink = m.get('EnvConf')
        return self


class EditRoutineConfResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditRoutineConfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditRoutineConfResponseBody = None,
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
            temp_model = EditRoutineConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDcdnDomainOfflineLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class EnableDcdnDomainOfflineLogDeliveryResponseBody(TeaModel):
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


class EnableDcdnDomainOfflineLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableDcdnDomainOfflineLogDeliveryResponseBody = None,
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
            temp_model = EnableDcdnDomainOfflineLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDCdnDomainSchdmByPropertyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        property: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.property = property

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.property is not None:
            result['Property'] = self.property
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        return self


class ModifyDCdnDomainSchdmByPropertyResponseBody(TeaModel):
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


class ModifyDCdnDomainSchdmByPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDCdnDomainSchdmByPropertyResponseBody = None,
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
            temp_model = ModifyDCdnDomainSchdmByPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDcdnServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        bill_type: str = None,
        websocket_bill_type: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.bill_type = bill_type
        self.websocket_bill_type = websocket_bill_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.websocket_bill_type is not None:
            result['WebsocketBillType'] = self.websocket_bill_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('WebsocketBillType') is not None:
            self.websocket_bill_type = m.get('WebsocketBillType')
        return self


class OpenDcdnServiceResponseBody(TeaModel):
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


class OpenDcdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenDcdnServiceResponseBody = None,
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
            temp_model = OpenDcdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreloadDcdnObjectCachesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        object_path: str = None,
        area: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.object_path = object_path
        self.area = area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.area is not None:
            result['Area'] = self.area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        return self


class PreloadDcdnObjectCachesResponseBody(TeaModel):
    def __init__(
        self,
        preload_task_id: str = None,
        request_id: str = None,
    ):
        self.preload_task_id = preload_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preload_task_id is not None:
            result['PreloadTaskId'] = self.preload_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreloadTaskId') is not None:
            self.preload_task_id = m.get('PreloadTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreloadDcdnObjectCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PreloadDcdnObjectCachesResponseBody = None,
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
            temp_model = PreloadDcdnObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishDcdnStagingConfigToProductionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        function_name: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class PublishDcdnStagingConfigToProductionResponseBody(TeaModel):
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


class PublishDcdnStagingConfigToProductionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishDcdnStagingConfigToProductionResponseBody = None,
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
            temp_model = PublishDcdnStagingConfigToProductionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRoutineCodeRevisionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        select_code_revision: str = None,
        envs: Dict[str, Any] = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.select_code_revision = select_code_revision
        self.envs = envs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        if self.envs is not None:
            result['Envs'] = self.envs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        return self


class PublishRoutineCodeRevisionShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        select_code_revision: str = None,
        envs_shrink: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.select_code_revision = select_code_revision
        self.envs_shrink = envs_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision
        if self.envs_shrink is not None:
            result['Envs'] = self.envs_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')
        if m.get('Envs') is not None:
            self.envs_shrink = m.get('Envs')
        return self


class PublishRoutineCodeRevisionResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishRoutineCodeRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishRoutineCodeRevisionResponseBody = None,
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
            temp_model = PublishRoutineCodeRevisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDcdnObjectCachesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        object_path: str = None,
        object_type: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.object_path = object_path
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        return self


class RefreshDcdnObjectCachesResponseBody(TeaModel):
    def __init__(
        self,
        refresh_task_id: str = None,
        request_id: str = None,
    ):
        self.refresh_task_id = refresh_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_task_id is not None:
            result['RefreshTaskId'] = self.refresh_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshTaskId') is not None:
            self.refresh_task_id = m.get('RefreshTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshDcdnObjectCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshDcdnObjectCachesResponseBody = None,
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
            temp_model = RefreshDcdnObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackDcdnStagingConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class RollbackDcdnStagingConfigResponseBody(TeaModel):
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


class RollbackDcdnStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackDcdnStagingConfigResponseBody = None,
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
            temp_model = RollbackDcdnStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnConfigOfVersionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        version_id: str = None,
        config_id: str = None,
        function_id: int = None,
        function_name: str = None,
        function_args: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.version_id = version_id
        self.config_id = config_id
        self.function_id = function_id
        self.function_name = function_name
        self.function_args = function_args

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            self.function_args = m.get('FunctionArgs')
        return self


class SetDcdnConfigOfVersionResponseBody(TeaModel):
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


class SetDcdnConfigOfVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDcdnConfigOfVersionResponseBody = None,
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
            temp_model = SetDcdnConfigOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        cert_name: str = None,
        cert_type: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        sslpri: str = None,
        region: str = None,
        force_set: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.cert_name = cert_name
        self.cert_type = cert_type
        self.sslprotocol = sslprotocol
        self.sslpub = sslpub
        self.sslpri = sslpri
        self.region = region
        self.force_set = force_set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.region is not None:
            result['Region'] = self.region
        if self.force_set is not None:
            result['ForceSet'] = self.force_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
        return self


class SetDcdnDomainCertificateResponseBody(TeaModel):
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


class SetDcdnDomainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDcdnDomainCertificateResponseBody = None,
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
            temp_model = SetDcdnDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnDomainCSRCertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        server_certificate: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.server_certificate = server_certificate
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class SetDcdnDomainCSRCertificateResponseBody(TeaModel):
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


class SetDcdnDomainCSRCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDcdnDomainCSRCertificateResponseBody = None,
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
            temp_model = SetDcdnDomainCSRCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDcdnDomainStagingConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        functions: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.functions = functions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        return self


class SetDcdnDomainStagingConfigResponseBody(TeaModel):
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


class SetDcdnDomainStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDcdnDomainStagingConfigResponseBody = None,
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
            temp_model = SetDcdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRoutineSubdomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        subdomains: Dict[str, Any] = None,
    ):
        self.owner_id = owner_id
        self.subdomains = subdomains

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subdomains is not None:
            result['Subdomains'] = self.subdomains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Subdomains') is not None:
            self.subdomains = m.get('Subdomains')
        return self


class SetRoutineSubdomainShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        subdomains_shrink: str = None,
    ):
        self.owner_id = owner_id
        self.subdomains_shrink = subdomains_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subdomains_shrink is not None:
            result['Subdomains'] = self.subdomains_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Subdomains') is not None:
            self.subdomains_shrink = m.get('Subdomains')
        return self


class SetRoutineSubdomainResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetRoutineSubdomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetRoutineSubdomainResponseBody = None,
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
            temp_model = SetRoutineSubdomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDcdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class StartDcdnDomainResponseBody(TeaModel):
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


class StartDcdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDcdnDomainResponseBody = None,
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
            temp_model = StartDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDcdnIpaDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class StartDcdnIpaDomainResponseBody(TeaModel):
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


class StartDcdnIpaDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDcdnIpaDomainResponseBody = None,
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
            temp_model = StartDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDcdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class StopDcdnDomainResponseBody(TeaModel):
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


class StopDcdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDcdnDomainResponseBody = None,
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
            temp_model = StopDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDcdnIpaDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class StopDcdnIpaDomainResponseBody(TeaModel):
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


class StopDcdnIpaDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDcdnIpaDomainResponseBody = None,
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
            temp_model = StopDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagDcdnResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagDcdnResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagDcdnResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagDcdnResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagDcdnResourcesResponseBody(TeaModel):
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


class TagDcdnResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagDcdnResourcesResponseBody = None,
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
            temp_model = TagDcdnResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagDcdnResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagDcdnResourcesResponseBody(TeaModel):
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


class UntagDcdnResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagDcdnResourcesResponseBody = None,
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
            temp_model = UntagDcdnResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnDeliverTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        deliver_id: int = None,
        name: str = None,
        status: str = None,
        reports: str = None,
        domain_name: str = None,
        deliver: Dict[str, Any] = None,
        schedule: Dict[str, Any] = None,
    ):
        self.owner_id = owner_id
        self.deliver_id = deliver_id
        self.name = name
        self.status = status
        self.reports = reports
        self.domain_name = domain_name
        self.deliver = deliver
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.deliver is not None:
            result['Deliver'] = self.deliver
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        return self


class UpdateDcdnDeliverTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        deliver_id: int = None,
        name: str = None,
        status: str = None,
        reports: str = None,
        domain_name: str = None,
        deliver_shrink: str = None,
        schedule_shrink: str = None,
    ):
        self.owner_id = owner_id
        self.deliver_id = deliver_id
        self.name = name
        self.status = status
        self.reports = reports
        self.domain_name = domain_name
        self.deliver_shrink = deliver_shrink
        self.schedule_shrink = schedule_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.deliver_shrink is not None:
            result['Deliver'] = self.deliver_shrink
        if self.schedule_shrink is not None:
            result['Schedule'] = self.schedule_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Deliver') is not None:
            self.deliver_shrink = m.get('Deliver')
        if m.get('Schedule') is not None:
            self.schedule_shrink = m.get('Schedule')
        return self


class UpdateDcdnDeliverTaskResponseBody(TeaModel):
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


class UpdateDcdnDeliverTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDcdnDeliverTaskResponseBody = None,
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
            temp_model = UpdateDcdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        sources: str = None,
        resource_group_id: str = None,
        top_level_domain: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.sources = sources
        self.resource_group_id = resource_group_id
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class UpdateDcdnDomainResponseBody(TeaModel):
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


class UpdateDcdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDcdnDomainResponseBody = None,
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
            temp_model = UpdateDcdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnIpaDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        sources: str = None,
        resource_group_id: str = None,
        top_level_domain: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.sources = sources
        self.resource_group_id = resource_group_id
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class UpdateDcdnIpaDomainResponseBody(TeaModel):
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


class UpdateDcdnIpaDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDcdnIpaDomainResponseBody = None,
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
            temp_model = UpdateDcdnIpaDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDcdnSubTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        status: str = None,
        report_ids: str = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.status = status
        self.report_ids = report_ids
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class UpdateDcdnSubTaskResponseBody(TeaModel):
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


class UpdateDcdnSubTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDcdnSubTaskResponseBody = None,
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
            temp_model = UpdateDcdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRoutineCodeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        code_description: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.code_description = code_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        return self


class UploadRoutineCodeResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadRoutineCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadRoutineCodeResponseBody = None,
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
            temp_model = UploadRoutineCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadStagingRoutineCodeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
        code_description: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.code_description = code_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')
        return self


class UploadStagingRoutineCodeResponseBody(TeaModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadStagingRoutineCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadStagingRoutineCodeResponseBody = None,
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
            temp_model = UploadStagingRoutineCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDcdnDomainOwnerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        verify_type: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class VerifyDcdnDomainOwnerResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyDcdnDomainOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyDcdnDomainOwnerResponseBody = None,
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
            temp_model = VerifyDcdnDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


