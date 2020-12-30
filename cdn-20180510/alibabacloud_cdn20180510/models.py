# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddCdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        cdn_type: str = None,
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
        self.cdn_type = cdn_type
        self.domain_name = domain_name
        self.resource_group_id = resource_group_id
        self.sources = sources
        self.check_url = check_url
        self.scope = scope
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
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
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
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


class AddCdnDomainResponseBody(TeaModel):
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


class AddCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddCdnDomainResponseBody = None,
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
            temp_model = AddCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFCTriggerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        trigger_arn: str = None,
        event_meta_name: str = None,
        event_meta_version: str = None,
        source_arn: str = None,
        function_arn: str = None,
        role_arn: str = None,
        notes: str = None,
    ):
        self.owner_id = owner_id
        self.trigger_arn = trigger_arn
        self.event_meta_name = event_meta_name
        self.event_meta_version = event_meta_version
        self.source_arn = source_arn
        self.function_arn = function_arn
        self.role_arn = role_arn
        self.notes = notes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        if self.source_arn is not None:
            result['SourceARN'] = self.source_arn
        if self.function_arn is not None:
            result['FunctionARN'] = self.function_arn
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.notes is not None:
            result['Notes'] = self.notes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        if m.get('SourceARN') is not None:
            self.source_arn = m.get('SourceARN')
        if m.get('FunctionARN') is not None:
            self.function_arn = m.get('FunctionARN')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        return self


class AddFCTriggerResponseBody(TeaModel):
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


class AddFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFCTriggerResponseBody = None,
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
            temp_model = AddFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddCdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        owner_account: str = None,
        security_token: str = None,
        cdn_type: str = None,
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
        self.cdn_type = cdn_type
        self.domain_name = domain_name
        self.resource_group_id = resource_group_id
        self.sources = sources
        self.check_url = check_url
        self.scope = scope
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
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
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
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


class BatchAddCdnDomainResponseBody(TeaModel):
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


class BatchAddCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchAddCdnDomainResponseBody = None,
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
            temp_model = BatchAddCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetCdnDomainConfigRequest(TeaModel):
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


class BatchSetCdnDomainConfigResponseBody(TeaModel):
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


class BatchSetCdnDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSetCdnDomainConfigResponseBody = None,
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
            temp_model = BatchSetCdnDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetCdnDomainServerCertificateRequest(TeaModel):
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


class BatchSetCdnDomainServerCertificateResponseBody(TeaModel):
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


class BatchSetCdnDomainServerCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSetCdnDomainServerCertificateResponseBody = None,
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
            temp_model = BatchSetCdnDomainServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartCdnDomainRequest(TeaModel):
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


class BatchStartCdnDomainResponseBody(TeaModel):
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


class BatchStartCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStartCdnDomainResponseBody = None,
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
            temp_model = BatchStartCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopCdnDomainRequest(TeaModel):
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


class BatchStopCdnDomainResponseBody(TeaModel):
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


class BatchStopCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStopCdnDomainResponseBody = None,
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
            temp_model = BatchStopCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateCdnDomainRequest(TeaModel):
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


class BatchUpdateCdnDomainResponseBody(TeaModel):
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


class BatchUpdateCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUpdateCdnDomainResponseBody = None,
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
            temp_model = BatchUpdateCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnCertificateSigningRequestRequest(TeaModel):
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


class CreateCdnCertificateSigningRequestResponseBody(TeaModel):
    def __init__(
        self,
        pub_md_5: str = None,
        csr: str = None,
        request_id: str = None,
        common_name: str = None,
    ):
        self.pub_md_5 = pub_md_5
        self.csr = csr
        self.request_id = request_id
        self.common_name = common_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pub_md_5 is not None:
            result['PubMd5'] = self.pub_md_5
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PubMd5') is not None:
            self.pub_md_5 = m.get('PubMd5')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        return self


class CreateCdnCertificateSigningRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCdnCertificateSigningRequestResponseBody = None,
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
            temp_model = CreateCdnCertificateSigningRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIllegalUrlExportTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        time_point: str = None,
        task_name: str = None,
    ):
        self.owner_id = owner_id
        self.time_point = time_point
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateIllegalUrlExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIllegalUrlExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIllegalUrlExportTaskResponseBody = None,
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
            temp_model = CreateIllegalUrlExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRealTimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        project: str = None,
        logstore: str = None,
        region: str = None,
        domain: str = None,
    ):
        self.owner_id = owner_id
        self.project = project
        self.logstore = logstore
        self.region = region
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.region is not None:
            result['Region'] = self.region
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CreateRealTimeLogDeliveryResponseBody(TeaModel):
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


class CreateRealTimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRealTimeLogDeliveryResponseBody = None,
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
            temp_model = CreateRealTimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUsageDetailDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        group: str = None,
        domain_names: str = None,
        type: str = None,
        task_name: str = None,
        language: str = None,
    ):
        self.owner_id = owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.group = group
        self.domain_names = domain_names
        self.type = type
        self.task_name = task_name
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group is not None:
            result['Group'] = self.group
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.type is not None:
            result['Type'] = self.type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class CreateUsageDetailDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.task_id = task_id
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUsageDetailDataExportTaskResponseBody = None,
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
            temp_model = CreateUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserUsageDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        task_name: str = None,
        language: str = None,
    ):
        self.owner_id = owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.task_name = task_name
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class CreateUserUsageDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.task_id = task_id
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateUserUsageDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserUsageDataExportTaskResponseBody = None,
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
            temp_model = CreateUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnDomainRequest(TeaModel):
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


class DeleteCdnDomainResponseBody(TeaModel):
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


class DeleteCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCdnDomainResponseBody = None,
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
            temp_model = DeleteCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFCTriggerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        trigger_arn: str = None,
    ):
        self.owner_id = owner_id
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class DeleteFCTriggerResponseBody(TeaModel):
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


class DeleteFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFCTriggerResponseBody = None,
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
            temp_model = DeleteFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain: str = None,
        project: str = None,
        logstore: str = None,
        region: str = None,
    ):
        self.owner_id = owner_id
        self.domain = domain
        self.project = project
        self.logstore = logstore
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.project is not None:
            result['Project'] = self.project
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteRealtimeLogDeliveryResponseBody(TeaModel):
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


class DeleteRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRealtimeLogDeliveryResponseBody = None,
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
            temp_model = DeleteRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpecificConfigRequest(TeaModel):
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


class DeleteSpecificConfigResponseBody(TeaModel):
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


class DeleteSpecificConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSpecificConfigResponseBody = None,
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
            temp_model = DeleteSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpecificStagingConfigRequest(TeaModel):
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


class DeleteSpecificStagingConfigResponseBody(TeaModel):
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


class DeleteSpecificStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSpecificStagingConfigResponseBody = None,
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
            temp_model = DeleteSpecificStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUsageDetailDataExportTaskRequest(TeaModel):
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


class DeleteUsageDetailDataExportTaskResponseBody(TeaModel):
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


class DeleteUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUsageDetailDataExportTaskResponseBody = None,
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
            temp_model = DeleteUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserUsageDataExportTaskRequest(TeaModel):
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


class DeleteUserUsageDataExportTaskResponseBody(TeaModel):
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


class DeleteUserUsageDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserUsageDataExportTaskResponseBody = None,
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
            temp_model = DeleteUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeActiveVersionOfConfigGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        config_group_id: str = None,
        env: str = None,
    ):
        self.owner_id = owner_id
        self.config_group_id = config_group_id
        self.env = env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.config_group_id is not None:
            result['ConfigGroupId'] = self.config_group_id
        if self.env is not None:
            result['Env'] = self.env
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ConfigGroupId') is not None:
            self.config_group_id = m.get('ConfigGroupId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        return self


class DescribeActiveVersionOfConfigGroupResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        version_id: str = None,
        operator: str = None,
        config_group_id: str = None,
        base_version_id: str = None,
        description: str = None,
        request_id: str = None,
        create_time: str = None,
        update_time: str = None,
        seq_id: int = None,
    ):
        self.status = status
        self.version_id = version_id
        self.operator = operator
        self.config_group_id = config_group_id
        self.base_version_id = base_version_id
        self.description = description
        self.request_id = request_id
        self.create_time = create_time
        self.update_time = update_time
        self.seq_id = seq_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.config_group_id is not None:
            result['ConfigGroupId'] = self.config_group_id
        if self.base_version_id is not None:
            result['BaseVersionId'] = self.base_version_id
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.seq_id is not None:
            result['SeqId'] = self.seq_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('ConfigGroupId') is not None:
            self.config_group_id = m.get('ConfigGroupId')
        if m.get('BaseVersionId') is not None:
            self.base_version_id = m.get('BaseVersionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('SeqId') is not None:
            self.seq_id = m.get('SeqId')
        return self


class DescribeActiveVersionOfConfigGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeActiveVersionOfConfigGroupResponseBody = None,
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
            temp_model = DescribeActiveVersionOfConfigGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnCertificateDetailRequest(TeaModel):
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


class DescribeCdnCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cert_id: int = None,
        cert_name: str = None,
        cert: str = None,
        key: str = None,
    ):
        self.request_id = request_id
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.cert = cert
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class DescribeCdnCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnCertificateDetailResponseBody = None,
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
            temp_model = DescribeCdnCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnCertificateListRequest(TeaModel):
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


class DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
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


class DescribeCdnCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(
        self,
        cert: List[DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert] = None,
    ):
        self.cert = cert

    def validate(self):
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeCdnCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(
        self,
        cert_list: DescribeCdnCertificateListResponseBodyCertificateListModelCertList = None,
        count: int = None,
    ):
        self.cert_list = cert_list
        self.count = count

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        result = dict()
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertList') is not None:
            temp_model = DescribeCdnCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeCdnCertificateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        certificate_list_model: DescribeCdnCertificateListResponseBodyCertificateListModel = None,
    ):
        self.request_id = request_id
        self.certificate_list_model = certificate_list_model

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
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
            temp_model = DescribeCdnCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        return self


class DescribeCdnCertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnCertificateListResponseBody = None,
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
            temp_model = DescribeCdnCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainByCertificateRequest(TeaModel):
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


class DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo(TeaModel):
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


class DescribeCdnDomainByCertificateResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainByCertificateResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeCdnDomainByCertificateResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        self.cert_infos = cert_infos
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeCdnDomainByCertificateResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainByCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnDomainByCertificateResponseBody = None,
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
            temp_model = DescribeCdnDomainByCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainConfigsRequest(TeaModel):
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


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
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


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(
        self,
        function_arg: List[DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg] = None,
    ):
        self.function_arg = function_arg

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(
        self,
        status: str = None,
        config_id: str = None,
        function_name: str = None,
        function_args: DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs = None,
    ):
        self.status = status
        self.config_id = config_id
        self.function_name = function_name
        self.function_args = function_args

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
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
            temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        return self


class DescribeCdnDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        domain_config: List[DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig] = None,
    ):
        self.domain_config = domain_config

    def validate(self):
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_configs: DescribeCdnDomainConfigsResponseBodyDomainConfigs = None,
    ):
        self.request_id = request_id
        self.domain_configs = domain_configs

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
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
            temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        return self


class DescribeCdnDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnDomainConfigsResponseBody = None,
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
            temp_model = DescribeCdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainDetailRequest(TeaModel):
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


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel(TeaModel):
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


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels(TeaModel):
    def __init__(
        self,
        source_model: List[DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel] = None,
    ):
        self.source_model = source_model

    def validate(self):
        if self.source_model:
            for k in self.source_model:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SourceModel'] = []
        if self.source_model is not None:
            for k in self.source_model:
                result['SourceModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_model = []
        if m.get('SourceModel') is not None:
            for k in m.get('SourceModel'):
                temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel()
                self.source_model.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModel(TeaModel):
    def __init__(
        self,
        https_cname: str = None,
        server_certificate_status: str = None,
        gmt_modified: str = None,
        domain_name: str = None,
        gmt_created: str = None,
        description: str = None,
        resource_group_id: str = None,
        scope: str = None,
        domain_status: str = None,
        cname: str = None,
        cdn_type: str = None,
        source_models: DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels = None,
    ):
        self.https_cname = https_cname
        self.server_certificate_status = server_certificate_status
        self.gmt_modified = gmt_modified
        self.domain_name = domain_name
        self.gmt_created = gmt_created
        self.description = description
        self.resource_group_id = resource_group_id
        self.scope = scope
        self.domain_status = domain_status
        self.cname = cname
        self.cdn_type = cdn_type
        self.source_models = source_models

    def validate(self):
        if self.source_models:
            self.source_models.validate()

    def to_map(self):
        result = dict()
        if self.https_cname is not None:
            result['HttpsCname'] = self.https_cname
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.source_models is not None:
            result['SourceModels'] = self.source_models.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsCname') is not None:
            self.https_cname = m.get('HttpsCname')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('SourceModels') is not None:
            temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels()
            self.source_models = temp_model.from_map(m['SourceModels'])
        return self


class DescribeCdnDomainDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        get_domain_detail_model: DescribeCdnDomainDetailResponseBodyGetDomainDetailModel = None,
    ):
        self.request_id = request_id
        self.get_domain_detail_model = get_domain_detail_model

    def validate(self):
        if self.get_domain_detail_model:
            self.get_domain_detail_model.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.get_domain_detail_model is not None:
            result['GetDomainDetailModel'] = self.get_domain_detail_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GetDomainDetailModel') is not None:
            temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModel()
            self.get_domain_detail_model = temp_model.from_map(m['GetDomainDetailModel'])
        return self


class DescribeCdnDomainDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnDomainDetailResponseBody = None,
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
            temp_model = DescribeCdnDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainLogsRequest(TeaModel):
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


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfosPageInfoDetail(TeaModel):
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


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos(TeaModel):
    def __init__(
        self,
        page_info_detail: List[DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfosPageInfoDetail] = None,
    ):
        self.page_info_detail = page_info_detail

    def validate(self):
        if self.page_info_detail:
            for k in self.page_info_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PageInfoDetail'] = []
        if self.page_info_detail is not None:
            for k in self.page_info_detail:
                result['PageInfoDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_info_detail = []
        if m.get('PageInfoDetail') is not None:
            for k in m.get('PageInfoDetail'):
                temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfosPageInfoDetail()
                self.page_info_detail.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        log_path: str = None,
        log_size: int = None,
        log_name: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.log_path = log_path
        self.log_size = log_size
        self.log_name = log_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.log_name is not None:
            result['LogName'] = self.log_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos(TeaModel):
    def __init__(
        self,
        log_info_detail: List[DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail] = None,
    ):
        self.log_info_detail = log_info_detail

    def validate(self):
        if self.log_info_detail:
            for k in self.log_info_detail:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(
        self,
        page_infos: DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos = None,
        log_count: int = None,
        domain_name: str = None,
        log_infos: DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos = None,
    ):
        self.page_infos = page_infos
        self.log_count = log_count
        self.domain_name = domain_name
        self.log_infos = log_infos

    def validate(self):
        if self.page_infos:
            self.page_infos.validate()
        if self.log_infos:
            self.log_infos.validate()

    def to_map(self):
        result = dict()
        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfos') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m['PageInfos'])
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LogInfos') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetails(TeaModel):
    def __init__(
        self,
        domain_log_detail: List[DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail] = None,
    ):
        self.domain_log_detail = domain_log_detail

    def validate(self):
        if self.domain_log_detail:
            for k in self.domain_log_detail:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_log_details: DescribeCdnDomainLogsResponseBodyDomainLogDetails = None,
    ):
        self.request_id = request_id
        self.domain_log_details = domain_log_details

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        return self


class DescribeCdnDomainLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnDomainLogsResponseBody = None,
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
            temp_model = DescribeCdnDomainLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainStagingConfigRequest(TeaModel):
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


class DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs(TeaModel):
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


class DescribeCdnDomainStagingConfigResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        status: str = None,
        config_id: str = None,
        function_name: str = None,
        function_args: List[DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs] = None,
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
                temp_model = DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_configs: List[DescribeCdnDomainStagingConfigResponseBodyDomainConfigs] = None,
    ):
        self.request_id = request_id
        self.domain_configs = domain_configs

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnDomainStagingConfigResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnDomainStagingConfigResponseBody = None,
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
            temp_model = DescribeCdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnHttpsDomainListRequest(TeaModel):
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


class DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo(TeaModel):
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


class DescribeCdnHttpsDomainListResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCdnHttpsDomainListResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeCdnHttpsDomainListResponseBodyCertInfos = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.cert_infos = cert_infos
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeCdnHttpsDomainListResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnHttpsDomainListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnHttpsDomainListResponseBody = None,
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
            temp_model = DescribeCdnHttpsDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnRegionAndIspRequest(TeaModel):
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


class DescribeCdnRegionAndIspResponseBodyRegionsRegion(TeaModel):
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


class DescribeCdnRegionAndIspResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeCdnRegionAndIspResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnRegionAndIspResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeCdnRegionAndIspResponseBodyIspsIsp(TeaModel):
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


class DescribeCdnRegionAndIspResponseBodyIsps(TeaModel):
    def __init__(
        self,
        isp: List[DescribeCdnRegionAndIspResponseBodyIspsIsp] = None,
    ):
        self.isp = isp

    def validate(self):
        if self.isp:
            for k in self.isp:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnRegionAndIspResponseBodyIspsIsp()
                self.isp.append(temp_model.from_map(k))
        return self


class DescribeCdnRegionAndIspResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeCdnRegionAndIspResponseBodyRegions = None,
        isps: DescribeCdnRegionAndIspResponseBodyIsps = None,
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
            temp_model = DescribeCdnRegionAndIspResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('Isps') is not None:
            temp_model = DescribeCdnRegionAndIspResponseBodyIsps()
            self.isps = temp_model.from_map(m['Isps'])
        return self


class DescribeCdnRegionAndIspResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnRegionAndIspResponseBody = None,
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
            temp_model = DescribeCdnRegionAndIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnServiceRequest(TeaModel):
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


class DescribeCdnServiceResponseBodyOperationLocksLockReason(TeaModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        return self


class DescribeCdnServiceResponseBodyOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: List[DescribeCdnServiceResponseBodyOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeCdnServiceResponseBody(TeaModel):
    def __init__(
        self,
        changing_charge_type: str = None,
        request_id: str = None,
        instance_id: str = None,
        opening_time: str = None,
        changing_affect_time: str = None,
        operation_locks: DescribeCdnServiceResponseBodyOperationLocks = None,
        internet_charge_type: str = None,
    ):
        self.changing_charge_type = changing_charge_type
        self.request_id = request_id
        self.instance_id = instance_id
        self.opening_time = opening_time
        self.changing_affect_time = changing_affect_time
        self.operation_locks = operation_locks
        self.internet_charge_type = internet_charge_type

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        result = dict()
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeCdnServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        return self


class DescribeCdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnServiceResponseBody = None,
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
            temp_model = DescribeCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillHistoryRequest(TeaModel):
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


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem(TeaModel):
    def __init__(
        self,
        bandwidth: float = None,
        charge_type: str = None,
        flow: float = None,
        count: float = None,
        cdn_region: str = None,
    ):
        self.bandwidth = bandwidth
        self.charge_type = charge_type
        self.flow = flow
        self.count = count
        self.cdn_region = cdn_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.count is not None:
            result['Count'] = self.count
        if self.cdn_region is not None:
            result['CdnRegion'] = self.cdn_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CdnRegion') is not None:
            self.cdn_region = m.get('CdnRegion')
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData(TeaModel):
    def __init__(
        self,
        billing_data_item: List[DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem] = None,
    ):
        self.billing_data_item = billing_data_item

    def validate(self):
        if self.billing_data_item:
            for k in self.billing_data_item:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem()
                self.billing_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem(TeaModel):
    def __init__(
        self,
        billing_data: DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData = None,
        bill_type: str = None,
        dimension: str = None,
        bill_time: str = None,
    ):
        self.billing_data = billing_data
        self.bill_type = bill_type
        self.dimension = dimension
        self.bill_time = bill_time

    def validate(self):
        if self.billing_data:
            self.billing_data.validate()

    def to_map(self):
        result = dict()
        if self.billing_data is not None:
            result['BillingData'] = self.billing_data.to_map()
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.bill_time is not None:
            result['BillTime'] = self.bill_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingData') is not None:
            temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData()
            self.billing_data = temp_model.from_map(m['BillingData'])
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('BillTime') is not None:
            self.bill_time = m.get('BillTime')
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryData(TeaModel):
    def __init__(
        self,
        bill_history_data_item: List[DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem] = None,
    ):
        self.bill_history_data_item = bill_history_data_item

    def validate(self):
        if self.bill_history_data_item:
            for k in self.bill_history_data_item:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem()
                self.bill_history_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bill_history_data: DescribeCdnUserBillHistoryResponseBodyBillHistoryData = None,
    ):
        self.request_id = request_id
        self.bill_history_data = bill_history_data

    def validate(self):
        if self.bill_history_data:
            self.bill_history_data.validate()

    def to_map(self):
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
            temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryData()
            self.bill_history_data = temp_model.from_map(m['BillHistoryData'])
        return self


class DescribeCdnUserBillHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnUserBillHistoryResponseBody = None,
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
            temp_model = DescribeCdnUserBillHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillPredictionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        dimension: str = None,
        area: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.dimension = dimension
        self.area = area
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.area is not None:
            result['Area'] = self.area
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem(TeaModel):
    def __init__(
        self,
        value: float = None,
        time_stp: str = None,
        area: str = None,
    ):
        self.value = value
        self.time_stp = time_stp
        self.area = area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stp is not None:
            result['TimeStp'] = self.time_stp
        if self.area is not None:
            result['Area'] = self.area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStp') is not None:
            self.time_stp = m.get('TimeStp')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        return self


class DescribeCdnUserBillPredictionResponseBodyBillPredictionData(TeaModel):
    def __init__(
        self,
        bill_prediction_data_item: List[DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem] = None,
    ):
        self.bill_prediction_data_item = bill_prediction_data_item

    def validate(self):
        if self.bill_prediction_data_item:
            for k in self.bill_prediction_data_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BillPredictionDataItem'] = []
        if self.bill_prediction_data_item is not None:
            for k in self.bill_prediction_data_item:
                result['BillPredictionDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_prediction_data_item = []
        if m.get('BillPredictionDataItem') is not None:
            for k in m.get('BillPredictionDataItem'):
                temp_model = DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem()
                self.bill_prediction_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillPredictionResponseBody(TeaModel):
    def __init__(
        self,
        bill_type: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        bill_prediction_data: DescribeCdnUserBillPredictionResponseBodyBillPredictionData = None,
    ):
        self.bill_type = bill_type
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.bill_prediction_data = bill_prediction_data

    def validate(self):
        if self.bill_prediction_data:
            self.bill_prediction_data.validate()

    def to_map(self):
        result = dict()
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.bill_prediction_data is not None:
            result['BillPredictionData'] = self.bill_prediction_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('BillPredictionData') is not None:
            temp_model = DescribeCdnUserBillPredictionResponseBodyBillPredictionData()
            self.bill_prediction_data = temp_model.from_map(m['BillPredictionData'])
        return self


class DescribeCdnUserBillPredictionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnUserBillPredictionResponseBody = None,
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
            temp_model = DescribeCdnUserBillPredictionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillTypeRequest(TeaModel):
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


class DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem(TeaModel):
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


class DescribeCdnUserBillTypeResponseBodyBillTypeData(TeaModel):
    def __init__(
        self,
        bill_type_data_item: List[DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem] = None,
    ):
        self.bill_type_data_item = bill_type_data_item

    def validate(self):
        if self.bill_type_data_item:
            for k in self.bill_type_data_item:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem()
                self.bill_type_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bill_type_data: DescribeCdnUserBillTypeResponseBodyBillTypeData = None,
    ):
        self.request_id = request_id
        self.bill_type_data = bill_type_data

    def validate(self):
        if self.bill_type_data:
            self.bill_type_data.validate()

    def to_map(self):
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
            temp_model = DescribeCdnUserBillTypeResponseBodyBillTypeData()
            self.bill_type_data = temp_model.from_map(m['BillTypeData'])
        return self


class DescribeCdnUserBillTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnUserBillTypeResponseBody = None,
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
            temp_model = DescribeCdnUserBillTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserConfigsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        function_name: str = None,
    ):
        self.owner_id = owner_id
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class DescribeCdnUserConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        function_name: str = None,
        arg_value: str = None,
    ):
        self.arg_name = arg_name
        self.function_name = function_name
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeCdnUserConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        configs: List[DescribeCdnUserConfigsResponseBodyConfigs] = None,
    ):
        self.request_id = request_id
        self.configs = configs

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = DescribeCdnUserConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        return self


class DescribeCdnUserConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnUserConfigsResponseBody = None,
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
            temp_model = DescribeCdnUserConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserDomainsByFuncRequest(TeaModel):
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


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource(TeaModel):
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


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        ssl_protocol: str = None,
        description: str = None,
        resource_group_id: str = None,
        sandbox: str = None,
        domain_status: str = None,
        cname: str = None,
        sources: DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources = None,
        gmt_modified: str = None,
        cdn_type: str = None,
        domain_name: str = None,
    ):
        self.gmt_created = gmt_created
        self.ssl_protocol = ssl_protocol
        self.description = description
        self.resource_group_id = resource_group_id
        self.sandbox = sandbox
        self.domain_status = domain_status
        self.cname = cname
        self.sources = sources
        self.gmt_modified = gmt_modified
        self.cdn_type = cdn_type
        self.domain_name = domain_name

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
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
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
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
        if m.get('Sources') is not None:
            temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeCdnUserDomainsByFuncResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeCdnUserDomainsByFuncResponseBody(TeaModel):
    def __init__(
        self,
        domains: DescribeCdnUserDomainsByFuncResponseBodyDomains = None,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.domains = domains
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeCdnUserDomainsByFuncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnUserDomainsByFuncResponseBody = None,
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
            temp_model = DescribeCdnUserDomainsByFuncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserQuotaRequest(TeaModel):
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


class DescribeCdnUserQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        refresh_url_quota: int = None,
        block_remain: int = None,
        preload_remain: int = None,
        refresh_dir_remain: int = None,
        block_quota: int = None,
        refresh_dir_quota: int = None,
        domain_quota: int = None,
        refresh_url_remain: int = None,
        preload_quota: int = None,
    ):
        self.request_id = request_id
        self.refresh_url_quota = refresh_url_quota
        self.block_remain = block_remain
        self.preload_remain = preload_remain
        self.refresh_dir_remain = refresh_dir_remain
        self.block_quota = block_quota
        self.refresh_dir_quota = refresh_dir_quota
        self.domain_quota = domain_quota
        self.refresh_url_remain = refresh_url_remain
        self.preload_quota = preload_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refresh_url_quota is not None:
            result['RefreshUrlQuota'] = self.refresh_url_quota
        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.refresh_dir_remain is not None:
            result['RefreshDirRemain'] = self.refresh_dir_remain
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.refresh_dir_quota is not None:
            result['RefreshDirQuota'] = self.refresh_dir_quota
        if self.domain_quota is not None:
            result['DomainQuota'] = self.domain_quota
        if self.refresh_url_remain is not None:
            result['RefreshUrlRemain'] = self.refresh_url_remain
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefreshUrlQuota') is not None:
            self.refresh_url_quota = m.get('RefreshUrlQuota')
        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RefreshDirRemain') is not None:
            self.refresh_dir_remain = m.get('RefreshDirRemain')
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('RefreshDirQuota') is not None:
            self.refresh_dir_quota = m.get('RefreshDirQuota')
        if m.get('DomainQuota') is not None:
            self.domain_quota = m.get('DomainQuota')
        if m.get('RefreshUrlRemain') is not None:
            self.refresh_url_remain = m.get('RefreshUrlRemain')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        return self


class DescribeCdnUserQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnUserQuotaResponseBody = None,
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
            temp_model = DescribeCdnUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserResourcePackageRequest(TeaModel):
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


class DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
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


class DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos(TeaModel):
    def __init__(
        self,
        resource_package_info: List[DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo] = None,
    ):
        self.resource_package_info = resource_package_info

    def validate(self):
        if self.resource_package_info:
            for k in self.resource_package_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k))
        return self


class DescribeCdnUserResourcePackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_package_infos: DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos = None,
    ):
        self.request_id = request_id
        self.resource_package_infos = resource_package_infos

    def validate(self):
        if self.resource_package_infos:
            self.resource_package_infos.validate()

    def to_map(self):
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
            temp_model = DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m['ResourcePackageInfos'])
        return self


class DescribeCdnUserResourcePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnUserResourcePackageResponseBody = None,
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
            temp_model = DescribeCdnUserResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnWafDomainRequest(TeaModel):
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


class DescribeCdnWafDomainResponseBodyOutPutDomains(TeaModel):
    def __init__(
        self,
        status: str = None,
        domain: str = None,
        cc_status: str = None,
        acl_status: str = None,
        waf_status: str = None,
    ):
        self.status = status
        self.domain = domain
        self.cc_status = cc_status
        self.acl_status = acl_status
        self.waf_status = waf_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cc_status is not None:
            result['CcStatus'] = self.cc_status
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.waf_status is not None:
            result['WafStatus'] = self.waf_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CcStatus') is not None:
            self.cc_status = m.get('CcStatus')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('WafStatus') is not None:
            self.waf_status = m.get('WafStatus')
        return self


class DescribeCdnWafDomainResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        out_put_domains: List[DescribeCdnWafDomainResponseBodyOutPutDomains] = None,
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
                temp_model = DescribeCdnWafDomainResponseBodyOutPutDomains()
                self.out_put_domains.append(temp_model.from_map(k))
        return self


class DescribeCdnWafDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCdnWafDomainResponseBody = None,
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
            temp_model = DescribeCdnWafDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateInfoByIDRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        cert_id: str = None,
    ):
        self.owner_id = owner_id
        self.cert_id = cert_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        return self


class DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        cert_expire_time: str = None,
        create_time: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_id: str = None,
        domain_list: str = None,
        https_crt: str = None,
    ):
        self.cert_expire_time = cert_expire_time
        self.create_time = create_time
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_id = cert_id
        self.domain_list = domain_list
        self.https_crt = https_crt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.https_crt is not None:
            result['HttpsCrt'] = self.https_crt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('HttpsCrt') is not None:
            self.https_crt = m.get('HttpsCrt')
        return self


class DescribeCertificateInfoByIDResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCertificateInfoByIDResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeCertificateInfoByIDResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        self.cert_infos = cert_infos
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeCertificateInfoByIDResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertificateInfoByIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCertificateInfoByIDResponseBody = None,
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
            temp_model = DescribeCertificateInfoByIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigOfVersionRequest(TeaModel):
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


class DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg(TeaModel):
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


class DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs(TeaModel):
    def __init__(
        self,
        function_arg: List[DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg] = None,
    ):
        self.function_arg = function_arg

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfig(TeaModel):
    def __init__(
        self,
        status: str = None,
        config_id: str = None,
        function_name: str = None,
        function_args: DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs = None,
    ):
        self.status = status
        self.config_id = config_id
        self.function_name = function_name
        self.function_args = function_args

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
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
            temp_model = DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        return self


class DescribeConfigOfVersionResponseBodyVersionConfigs(TeaModel):
    def __init__(
        self,
        version_config: List[DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfig] = None,
    ):
        self.version_config = version_config

    def validate(self):
        if self.version_config:
            for k in self.version_config:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfig()
                self.version_config.append(temp_model.from_map(k))
        return self


class DescribeConfigOfVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_configs: DescribeConfigOfVersionResponseBodyVersionConfigs = None,
    ):
        self.request_id = request_id
        self.version_configs = version_configs

    def validate(self):
        if self.version_configs:
            self.version_configs.validate()

    def to_map(self):
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
            temp_model = DescribeConfigOfVersionResponseBodyVersionConfigs()
            self.version_configs = temp_model.from_map(m['VersionConfigs'])
        return self


class DescribeConfigOfVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigOfVersionResponseBody = None,
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
            temp_model = DescribeConfigOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomLogConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        config_id: str = None,
    ):
        self.owner_id = owner_id
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class DescribeCustomLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sample: str = None,
        tag: str = None,
        remark: str = None,
    ):
        self.request_id = request_id
        self.sample = sample
        self.tag = tag
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DescribeCustomLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCustomLogConfigResponseBody = None,
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
            temp_model = DescribeCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAverageResponseTimeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        time_merge: str = None,
        domain_type: str = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
    ):
        self.owner_id = owner_id
        self.time_merge = time_merge
        self.domain_type = domain_type
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
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
        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
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


class DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule(TeaModel):
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


class DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainAverageResponseTimeResponseBody(TeaModel):
    def __init__(
        self,
        avg_rtper_interval: DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval = None,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.avg_rtper_interval = avg_rtper_interval
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.avg_rtper_interval:
            self.avg_rtper_interval.validate()

    def to_map(self):
        result = dict()
        if self.avg_rtper_interval is not None:
            result['AvgRTPerInterval'] = self.avg_rtper_interval.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgRTPerInterval') is not None:
            temp_model = DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval()
            self.avg_rtper_interval = temp_model.from_map(m['AvgRTPerInterval'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainAverageResponseTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainAverageResponseTimeResponseBody = None,
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
            temp_model = DescribeDomainAverageResponseTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataRequest(TeaModel):
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


class DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        https_domestic_value: str = None,
        value: str = None,
        overseas_value: str = None,
        https_value: str = None,
        https_overseas_value: str = None,
        time_stamp: str = None,
        domestic_value: str = None,
    ):
        self.https_domestic_value = https_domestic_value
        self.value = value
        self.overseas_value = overseas_value
        self.https_value = https_value
        self.https_overseas_value = https_overseas_value
        self.time_stamp = time_stamp
        self.domestic_value = domestic_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.value is not None:
            result['Value'] = self.value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        return self


class DescribeDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        isp_name_en: str = None,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        location_name_en: str = None,
        start_time: str = None,
        data_interval: str = None,
        bps_data_per_interval: DescribeDomainBpsDataResponseBodyBpsDataPerInterval = None,
    ):
        self.isp_name_en = isp_name_en
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.location_name_en = location_name_en
        self.start_time = start_time
        self.data_interval = data_interval
        self.bps_data_per_interval = bps_data_per_interval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        return self


class DescribeDomainBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainBpsDataResponseBody = None,
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
            temp_model = DescribeDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataByLayerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        layer: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.layer = layer

    def validate(self):
        pass

    def to_map(self):
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
        if self.layer is not None:
            result['Layer'] = self.layer
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
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        return self


class DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        traffic_value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.traffic_value = traffic_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataByLayerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data_interval: str = None,
        bps_data_interval: DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval = None,
    ):
        self.request_id = request_id
        self.data_interval = data_interval
        self.bps_data_interval = bps_data_interval

    def validate(self):
        if self.bps_data_interval:
            self.bps_data_interval.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_interval is not None:
            result['BpsDataInterval'] = self.bps_data_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataInterval') is not None:
            temp_model = DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval()
            self.bps_data_interval = temp_model.from_map(m['BpsDataInterval'])
        return self


class DescribeDomainBpsDataByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainBpsDataByLayerResponseBody = None,
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
            temp_model = DescribeDomainBpsDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataByTimeStampRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        time_point: str = None,
        isp_names: str = None,
        location_names: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.time_point = time_point
        self.isp_names = isp_names
        self.location_names = location_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        if self.isp_names is not None:
            result['IspNames'] = self.isp_names
        if self.location_names is not None:
            result['LocationNames'] = self.location_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        if m.get('IspNames') is not None:
            self.isp_names = m.get('IspNames')
        if m.get('LocationNames') is not None:
            self.location_names = m.get('LocationNames')
        return self


class DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel(TeaModel):
    def __init__(
        self,
        location_name: str = None,
        time_stamp: str = None,
        isp_name: str = None,
        bps: int = None,
    ):
        self.location_name = location_name
        self.time_stamp = time_stamp
        self.isp_name = isp_name
        self.bps = bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.bps is not None:
            result['Bps'] = self.bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        return self


class DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList(TeaModel):
    def __init__(
        self,
        bps_data_model: List[DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel] = None,
    ):
        self.bps_data_model = bps_data_model

    def validate(self):
        if self.bps_data_model:
            for k in self.bps_data_model:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BpsDataModel'] = []
        if self.bps_data_model is not None:
            for k in self.bps_data_model:
                result['BpsDataModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bps_data_model = []
        if m.get('BpsDataModel') is not None:
            for k in m.get('BpsDataModel'):
                temp_model = DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel()
                self.bps_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataByTimeStampResponseBody(TeaModel):
    def __init__(
        self,
        bps_data_list: DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList = None,
        request_id: str = None,
        domain_name: str = None,
        time_stamp: str = None,
    ):
        self.bps_data_list = bps_data_list
        self.request_id = request_id
        self.domain_name = domain_name
        self.time_stamp = time_stamp

    def validate(self):
        if self.bps_data_list:
            self.bps_data_list.validate()

    def to_map(self):
        result = dict()
        if self.bps_data_list is not None:
            result['BpsDataList'] = self.bps_data_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDataList') is not None:
            temp_model = DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList()
            self.bps_data_list = temp_model.from_map(m['BpsDataList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainBpsDataByTimeStampResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainBpsDataByTimeStampResponseBody = None,
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
            temp_model = DescribeDomainBpsDataByTimeStampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCcActivityLogRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        trigger_object: str = None,
        value: str = None,
        rule_name: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.trigger_object = trigger_object
        self.value = value
        self.rule_name = rule_name
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.trigger_object is not None:
            result['TriggerObject'] = self.trigger_object
        if self.value is not None:
            result['Value'] = self.value
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
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
        if m.get('TriggerObject') is not None:
            self.trigger_object = m.get('TriggerObject')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeDomainCcActivityLogResponseBodyActivityLog(TeaModel):
    def __init__(
        self,
        value: str = None,
        ttl: int = None,
        action: str = None,
        trigger_object: str = None,
        time_stamp: str = None,
        domain_name: str = None,
        rule_name: str = None,
    ):
        self.value = value
        self.ttl = ttl
        self.action = action
        self.trigger_object = trigger_object
        self.time_stamp = time_stamp
        self.domain_name = domain_name
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.action is not None:
            result['Action'] = self.action
        if self.trigger_object is not None:
            result['TriggerObject'] = self.trigger_object
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('TriggerObject') is not None:
            self.trigger_object = m.get('TriggerObject')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeDomainCcActivityLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        total: int = None,
        activity_log: List[DescribeDomainCcActivityLogResponseBodyActivityLog] = None,
        page_index: int = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.total = total
        self.activity_log = activity_log
        self.page_index = page_index

    def validate(self):
        if self.activity_log:
            for k in self.activity_log:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['ActivityLog'] = []
        if self.activity_log is not None:
            for k in self.activity_log:
                result['ActivityLog'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.activity_log = []
        if m.get('ActivityLog') is not None:
            for k in m.get('ActivityLog'):
                temp_model = DescribeDomainCcActivityLogResponseBodyActivityLog()
                self.activity_log.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class DescribeDomainCcActivityLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainCcActivityLogResponseBody = None,
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
            temp_model = DescribeDomainCcActivityLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCertificateInfoRequest(TeaModel):
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


class DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        cert_life: str = None,
        cert_expire_time: str = None,
        cert_update_time: str = None,
        server_certificate_status: str = None,
        cert_domain_name: str = None,
        cert_org: str = None,
        domain_name: str = None,
        cert_start_time: str = None,
        cert_type: str = None,
        cert_name: str = None,
        domain_cname_status: str = None,
        server_certificate: str = None,
    ):
        self.status = status
        self.cert_life = cert_life
        self.cert_expire_time = cert_expire_time
        self.cert_update_time = cert_update_time
        self.server_certificate_status = server_certificate_status
        self.cert_domain_name = cert_domain_name
        self.cert_org = cert_org
        self.domain_name = domain_name
        self.cert_start_time = cert_start_time
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.domain_cname_status = domain_cname_status
        self.server_certificate = server_certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.domain_cname_status is not None:
            result['DomainCnameStatus'] = self.domain_cname_status
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('DomainCnameStatus') is not None:
            self.domain_cname_status = m.get('DomainCnameStatus')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        return self


class DescribeDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDomainCertificateInfoResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeDomainCertificateInfoResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        self.cert_infos = cert_infos
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainCertificateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainCertificateInfoResponseBody = None,
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
            temp_model = DescribeDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCustomLogConfigRequest(TeaModel):
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


class DescribeDomainCustomLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sample: str = None,
        config_id: str = None,
        tag: str = None,
        remark: str = None,
    ):
        self.request_id = request_id
        self.sample = sample
        self.config_id = config_id
        self.tag = tag
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DescribeDomainCustomLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainCustomLogConfigResponseBody = None,
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
            temp_model = DescribeDomainCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainDetailDataByLayerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        field: str = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        layer: str = None,
    ):
        self.owner_id = owner_id
        self.field = field
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.layer = layer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.field is not None:
            result['Field'] = self.field
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
        if self.layer is not None:
            result['Layer'] = self.layer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Field') is not None:
            self.field = m.get('Field')
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
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        return self


class DescribeDomainDetailDataByLayerResponseBodyDataDataModule(TeaModel):
    def __init__(
        self,
        traf: int = None,
        qps: float = None,
        ipv_6qps: float = None,
        ipv_6bps: float = None,
        acc: int = None,
        ipv_6traf: int = None,
        ipv_6acc: int = None,
        time_stamp: str = None,
        http_code: str = None,
        bps: float = None,
        domain_name: str = None,
    ):
        self.traf = traf
        self.qps = qps
        self.ipv_6qps = ipv_6qps
        self.ipv_6bps = ipv_6bps
        self.acc = acc
        self.ipv_6traf = ipv_6traf
        self.ipv_6acc = ipv_6acc
        self.time_stamp = time_stamp
        self.http_code = http_code
        self.bps = bps
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.traf is not None:
            result['Traf'] = self.traf
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.ipv_6qps is not None:
            result['Ipv6Qps'] = self.ipv_6qps
        if self.ipv_6bps is not None:
            result['Ipv6Bps'] = self.ipv_6bps
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.ipv_6traf is not None:
            result['Ipv6Traf'] = self.ipv_6traf
        if self.ipv_6acc is not None:
            result['Ipv6Acc'] = self.ipv_6acc
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Traf') is not None:
            self.traf = m.get('Traf')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Ipv6Qps') is not None:
            self.ipv_6qps = m.get('Ipv6Qps')
        if m.get('Ipv6Bps') is not None:
            self.ipv_6bps = m.get('Ipv6Bps')
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('Ipv6Traf') is not None:
            self.ipv_6traf = m.get('Ipv6Traf')
        if m.get('Ipv6Acc') is not None:
            self.ipv_6acc = m.get('Ipv6Acc')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainDetailDataByLayerResponseBodyData(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainDetailDataByLayerResponseBodyDataDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainDetailDataByLayerResponseBodyDataDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainDetailDataByLayerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDomainDetailDataByLayerResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
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
            temp_model = DescribeDomainDetailDataByLayerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDomainDetailDataByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainDetailDataByLayerResponseBody = None,
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
            temp_model = DescribeDomainDetailDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainFileSizeProportionDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValueFileSizeProportionData(TeaModel):
    def __init__(
        self,
        proportion: str = None,
        file_size: str = None,
    ):
        self.proportion = proportion
        self.file_size = file_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValue(TeaModel):
    def __init__(
        self,
        file_size_proportion_data: List[DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValueFileSizeProportionData] = None,
    ):
        self.file_size_proportion_data = file_size_proportion_data

    def validate(self):
        if self.file_size_proportion_data:
            for k in self.file_size_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FileSizeProportionData'] = []
        if self.file_size_proportion_data is not None:
            for k in self.file_size_proportion_data:
                result['FileSizeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_size_proportion_data = []
        if m.get('FileSizeProportionData') is not None:
            for k in m.get('FileSizeProportionData'):
                temp_model = DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValueFileSizeProportionData()
                self.file_size_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageData(TeaModel):
    def __init__(
        self,
        value: DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValue = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            temp_model = DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageData] = None,
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
                temp_model = DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainFileSizeProportionDataResponseBody(TeaModel):
    def __init__(
        self,
        file_size_proportion_data_interval: DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataInterval = None,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.file_size_proportion_data_interval = file_size_proportion_data_interval
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.file_size_proportion_data_interval:
            self.file_size_proportion_data_interval.validate()

    def to_map(self):
        result = dict()
        if self.file_size_proportion_data_interval is not None:
            result['FileSizeProportionDataInterval'] = self.file_size_proportion_data_interval.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSizeProportionDataInterval') is not None:
            temp_model = DescribeDomainFileSizeProportionDataResponseBodyFileSizeProportionDataInterval()
            self.file_size_proportion_data_interval = temp_model.from_map(m['FileSizeProportionDataInterval'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainFileSizeProportionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainFileSizeProportionDataResponseBody = None,
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
            temp_model = DescribeDomainFileSizeProportionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHitRateDataRequest(TeaModel):
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


class DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        https_value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.https_value = https_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainHitRateDataResponseBodyHitRateInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        hit_rate_interval: DescribeDomainHitRateDataResponseBodyHitRateInterval = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.hit_rate_interval = hit_rate_interval
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.hit_rate_interval:
            self.hit_rate_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.hit_rate_interval is not None:
            result['HitRateInterval'] = self.hit_rate_interval.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HitRateInterval') is not None:
            temp_model = DescribeDomainHitRateDataResponseBodyHitRateInterval()
            self.hit_rate_interval = temp_model.from_map(m['HitRateInterval'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainHitRateDataResponseBody = None,
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
            temp_model = DescribeDomainHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHttpCodeDataRequest(TeaModel):
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


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData(TeaModel):
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


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        code_proportion_data: List[DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData] = None,
    ):
        self.code_proportion_data = code_proportion_data

    def validate(self):
        if self.code_proportion_data:
            for k in self.code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CodeProportionData'] = []
        if self.code_proportion_data is not None:
            for k in self.code_proportion_data:
                result['CodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_proportion_data = []
        if m.get('CodeProportionData') is not None:
            for k in m.get('CodeProportionData'):
                temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData()
                self.code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        value: DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainHttpCodeDataResponseBodyHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData] = None,
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
                temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        http_code_data: DescribeDomainHttpCodeDataResponseBodyHttpCodeData = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.http_code_data = http_code_data

    def validate(self):
        if self.http_code_data:
            self.http_code_data.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.http_code_data is not None:
            result['HttpCodeData'] = self.http_code_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('HttpCodeData') is not None:
            temp_model = DescribeDomainHttpCodeDataResponseBodyHttpCodeData()
            self.http_code_data = temp_model.from_map(m['HttpCodeData'])
        return self


class DescribeDomainHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainHttpCodeDataResponseBody = None,
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
            temp_model = DescribeDomainHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHttpCodeDataByLayerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        layer: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.layer = layer

    def validate(self):
        pass

    def to_map(self):
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
        if self.layer is not None:
            result['Layer'] = self.layer
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
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        return self


class DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        time_stamp: str = None,
        total_value: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp
        self.total_value = total_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_value is not None:
            result['TotalValue'] = self.total_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalValue') is not None:
            self.total_value = m.get('TotalValue')
        return self


class DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataByLayerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data_interval: str = None,
        http_code_data_interval: DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval = None,
    ):
        self.request_id = request_id
        self.data_interval = data_interval
        self.http_code_data_interval = http_code_data_interval

    def validate(self):
        if self.http_code_data_interval:
            self.http_code_data_interval.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.http_code_data_interval is not None:
            result['HttpCodeDataInterval'] = self.http_code_data_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('HttpCodeDataInterval') is not None:
            temp_model = DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval()
            self.http_code_data_interval = temp_model.from_map(m['HttpCodeDataInterval'])
        return self


class DescribeDomainHttpCodeDataByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainHttpCodeDataByLayerResponseBody = None,
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
            temp_model = DescribeDomainHttpCodeDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainISPDataRequest(TeaModel):
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


class DescribeDomainISPDataResponseBodyValueISPProportionData(TeaModel):
    def __init__(
        self,
        total_query: str = None,
        total_bytes: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        req_err_rate: str = None,
        avg_object_size: str = None,
        bps: str = None,
        qps: str = None,
        proportion: str = None,
        isp_ename: str = None,
        isp: str = None,
        bytes_proportion: str = None,
    ):
        self.total_query = total_query
        self.total_bytes = total_bytes
        self.avg_response_rate = avg_response_rate
        self.avg_response_time = avg_response_time
        self.req_err_rate = req_err_rate
        self.avg_object_size = avg_object_size
        self.bps = bps
        self.qps = qps
        self.proportion = proportion
        self.isp_ename = isp_ename
        self.isp = isp
        self.bytes_proportion = bytes_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        return self


class DescribeDomainISPDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        ispproportion_data: List[DescribeDomainISPDataResponseBodyValueISPProportionData] = None,
    ):
        self.ispproportion_data = ispproportion_data

    def validate(self):
        if self.ispproportion_data:
            for k in self.ispproportion_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ISPProportionData'] = []
        if self.ispproportion_data is not None:
            for k in self.ispproportion_data:
                result['ISPProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ispproportion_data = []
        if m.get('ISPProportionData') is not None:
            for k in m.get('ISPProportionData'):
                temp_model = DescribeDomainISPDataResponseBodyValueISPProportionData()
                self.ispproportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainISPDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        value: DescribeDomainISPDataResponseBodyValue = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('Value') is not None:
            temp_model = DescribeDomainISPDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainISPDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainISPDataResponseBody = None,
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
            temp_model = DescribeDomainISPDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainMax95BpsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        time_point: str = None,
        cycle: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.time_point = time_point
        self.cycle = cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        if self.cycle is not None:
            result['Cycle'] = self.cycle
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
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')
        return self


class DescribeDomainMax95BpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        domestic_max_95bps: str = None,
        max_95bps: str = None,
        overseas_max_95bps: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.domestic_max_95bps = domestic_max_95bps
        self.max_95bps = max_95bps
        self.overseas_max_95bps = overseas_max_95bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.domestic_max_95bps is not None:
            result['DomesticMax95Bps'] = self.domestic_max_95bps
        if self.max_95bps is not None:
            result['Max95Bps'] = self.max_95bps
        if self.overseas_max_95bps is not None:
            result['OverseasMax95Bps'] = self.overseas_max_95bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DomesticMax95Bps') is not None:
            self.domestic_max_95bps = m.get('DomesticMax95Bps')
        if m.get('Max95Bps') is not None:
            self.max_95bps = m.get('Max95Bps')
        if m.get('OverseasMax95Bps') is not None:
            self.overseas_max_95bps = m.get('OverseasMax95Bps')
        return self


class DescribeDomainMax95BpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainMax95BpsDataResponseBody = None,
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
            temp_model = DescribeDomainMax95BpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainNamesOfVersionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        version_id: str = None,
        page_index: int = None,
        page_size: str = None,
    ):
        self.owner_id = owner_id
        self.version_id = version_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainNamesOfVersionResponseBodyContents(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_id: str = None,
    ):
        self.domain_name = domain_name
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        return self


class DescribeDomainNamesOfVersionResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        contents: List[DescribeDomainNamesOfVersionResponseBodyContents] = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.contents = contents
        self.request_id = request_id

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = DescribeDomainNamesOfVersionResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainNamesOfVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainNamesOfVersionResponseBody = None,
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
            temp_model = DescribeDomainNamesOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainPathDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        start_time: str = None,
        end_time: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.path = path
        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData(TeaModel):
    def __init__(
        self,
        time: str = None,
        acc: int = None,
        traffic: int = None,
        path: str = None,
    ):
        self.time = time
        self.acc = acc
        self.traffic = traffic
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeDomainPathDataResponseBodyPathDataPerInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData] = None,
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
                temp_model = DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainPathDataResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        domain_name: str = None,
        path_data_per_interval: DescribeDomainPathDataResponseBodyPathDataPerInterval = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.total_count = total_count
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.domain_name = domain_name
        self.path_data_per_interval = path_data_per_interval
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.path_data_per_interval:
            self.path_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.path_data_per_interval is not None:
            result['PathDataPerInterval'] = self.path_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PathDataPerInterval') is not None:
            temp_model = DescribeDomainPathDataResponseBodyPathDataPerInterval()
            self.path_data_per_interval = temp_model.from_map(m['PathDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainPathDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainPathDataResponseBody = None,
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
            temp_model = DescribeDomainPathDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainPvDataRequest(TeaModel):
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


class DescribeDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
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


class DescribeDomainPvDataResponseBodyPvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainPvDataResponseBodyPvDataIntervalUsageData] = None,
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
                temp_model = DescribeDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainPvDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        pv_data_interval: DescribeDomainPvDataResponseBodyPvDataInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.pv_data_interval = pv_data_interval

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('PvDataInterval') is not None:
            temp_model = DescribeDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        return self


class DescribeDomainPvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainPvDataResponseBody = None,
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
            temp_model = DescribeDomainPvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsDataRequest(TeaModel):
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


class DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule(TeaModel):
    def __init__(
        self,
        acc_value: str = None,
        acc_domestic_value: str = None,
        https_value: str = None,
        acc_overseas_value: str = None,
        https_overseas_value: str = None,
        domestic_value: str = None,
        https_acc_overseas_value: str = None,
        https_acc_value: str = None,
        https_domestic_value: str = None,
        value: str = None,
        overseas_value: str = None,
        time_stamp: str = None,
        https_acc_domestic_value: str = None,
    ):
        self.acc_value = acc_value
        self.acc_domestic_value = acc_domestic_value
        self.https_value = https_value
        self.acc_overseas_value = acc_overseas_value
        self.https_overseas_value = https_overseas_value
        self.domestic_value = domestic_value
        self.https_acc_overseas_value = https_acc_overseas_value
        self.https_acc_value = https_acc_value
        self.https_domestic_value = https_domestic_value
        self.value = value
        self.overseas_value = overseas_value
        self.time_stamp = time_stamp
        self.https_acc_domestic_value = https_acc_domestic_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.acc_value is not None:
            result['AccValue'] = self.acc_value
        if self.acc_domestic_value is not None:
            result['AccDomesticValue'] = self.acc_domestic_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.acc_overseas_value is not None:
            result['AccOverseasValue'] = self.acc_overseas_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.https_acc_overseas_value is not None:
            result['HttpsAccOverseasValue'] = self.https_acc_overseas_value
        if self.https_acc_value is not None:
            result['HttpsAccValue'] = self.https_acc_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.value is not None:
            result['Value'] = self.value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.https_acc_domestic_value is not None:
            result['HttpsAccDomesticValue'] = self.https_acc_domestic_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccValue') is not None:
            self.acc_value = m.get('AccValue')
        if m.get('AccDomesticValue') is not None:
            self.acc_domestic_value = m.get('AccDomesticValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('AccOverseasValue') is not None:
            self.acc_overseas_value = m.get('AccOverseasValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('HttpsAccOverseasValue') is not None:
            self.https_acc_overseas_value = m.get('HttpsAccOverseasValue')
        if m.get('HttpsAccValue') is not None:
            self.https_acc_value = m.get('HttpsAccValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('HttpsAccDomesticValue') is not None:
            self.https_acc_domestic_value = m.get('HttpsAccDomesticValue')
        return self


class DescribeDomainQpsDataResponseBodyQpsDataInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        qps_data_interval: DescribeDomainQpsDataResponseBodyQpsDataInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.qps_data_interval = qps_data_interval

    def validate(self):
        if self.qps_data_interval:
            self.qps_data_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.qps_data_interval is not None:
            result['QpsDataInterval'] = self.qps_data_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('QpsDataInterval') is not None:
            temp_model = DescribeDomainQpsDataResponseBodyQpsDataInterval()
            self.qps_data_interval = temp_model.from_map(m['QpsDataInterval'])
        return self


class DescribeDomainQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainQpsDataResponseBody = None,
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
            temp_model = DescribeDomainQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsDataByLayerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        layer: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.layer = layer

    def validate(self):
        pass

    def to_map(self):
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
        if self.layer is not None:
            result['Layer'] = self.layer
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
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        return self


class DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        acc_value: str = None,
        acc_domestic_value: str = None,
        overseas_value: str = None,
        acc_overseas_value: str = None,
        time_stamp: str = None,
        domestic_value: str = None,
    ):
        self.value = value
        self.acc_value = acc_value
        self.acc_domestic_value = acc_domestic_value
        self.overseas_value = overseas_value
        self.acc_overseas_value = acc_overseas_value
        self.time_stamp = time_stamp
        self.domestic_value = domestic_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.acc_value is not None:
            result['AccValue'] = self.acc_value
        if self.acc_domestic_value is not None:
            result['AccDomesticValue'] = self.acc_domestic_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.acc_overseas_value is not None:
            result['AccOverseasValue'] = self.acc_overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('AccValue') is not None:
            self.acc_value = m.get('AccValue')
        if m.get('AccDomesticValue') is not None:
            self.acc_domestic_value = m.get('AccDomesticValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('AccOverseasValue') is not None:
            self.acc_overseas_value = m.get('AccOverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        return self


class DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainQpsDataByLayerResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        qps_data_interval: DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval = None,
        layer: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.qps_data_interval = qps_data_interval
        self.layer = layer

    def validate(self):
        if self.qps_data_interval:
            self.qps_data_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.qps_data_interval is not None:
            result['QpsDataInterval'] = self.qps_data_interval.to_map()
        if self.layer is not None:
            result['Layer'] = self.layer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('QpsDataInterval') is not None:
            temp_model = DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval()
            self.qps_data_interval = temp_model.from_map(m['QpsDataInterval'])
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        return self


class DescribeDomainQpsDataByLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainQpsDataByLayerResponseBody = None,
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
            temp_model = DescribeDomainQpsDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeBpsDataRequest(TeaModel):
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


class DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        bps: float = None,
    ):
        self.time_stamp = time_stamp
        self.bps = bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.bps is not None:
            result['Bps'] = self.bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        return self


class DescribeDomainRealTimeBpsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        bps_model: List[DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel] = None,
    ):
        self.bps_model = bps_model

    def validate(self):
        if self.bps_model:
            for k in self.bps_model:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel()
                self.bps_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDomainRealTimeBpsDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
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
            temp_model = DescribeDomainRealTimeBpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDomainRealTimeBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeBpsDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeByteHitRateDataRequest(TeaModel):
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


class DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel(TeaModel):
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


class DescribeDomainRealTimeByteHitRateDataResponseBodyData(TeaModel):
    def __init__(
        self,
        byte_hit_rate_data_model: List[DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel] = None,
    ):
        self.byte_hit_rate_data_model = byte_hit_rate_data_model

    def validate(self):
        if self.byte_hit_rate_data_model:
            for k in self.byte_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel()
                self.byte_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeByteHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDomainRealTimeByteHitRateDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
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
            temp_model = DescribeDomainRealTimeByteHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDomainRealTimeByteHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeByteHitRateDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeByteHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeDetailDataRequest(TeaModel):
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


class DescribeDomainRealTimeDetailDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DescribeDomainRealTimeDetailDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeDetailDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeDetailDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeHttpCodeDataRequest(TeaModel):
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


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(TeaModel):
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


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        real_time_code_proportion_data: List[DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData] = None,
    ):
        self.real_time_code_proportion_data = real_time_code_proportion_data

    def validate(self):
        if self.real_time_code_proportion_data:
            for k in self.real_time_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData()
                self.real_time_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        value: DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData] = None,
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
                temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        real_time_http_code_data: DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.real_time_http_code_data = real_time_http_code_data

    def validate(self):
        if self.real_time_http_code_data:
            self.real_time_http_code_data.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_http_code_data is not None:
            result['RealTimeHttpCodeData'] = self.real_time_http_code_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeHttpCodeData') is not None:
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(m['RealTimeHttpCodeData'])
        return self


class DescribeDomainRealTimeHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeHttpCodeDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain: str = None,
    ):
        self.owner_id = owner_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        project: str = None,
        request_id: str = None,
        logstore: str = None,
        region: str = None,
    ):
        self.status = status
        self.project = project
        self.request_id = request_id
        self.logstore = logstore
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeDomainRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealtimeLogDeliveryResponseBody = None,
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
            temp_model = DescribeDomainRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeQpsDataRequest(TeaModel):
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


class DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel(TeaModel):
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


class DescribeDomainRealTimeQpsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        qps_model: List[DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel] = None,
    ):
        self.qps_model = qps_model

    def validate(self):
        if self.qps_model:
            for k in self.qps_model:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel()
                self.qps_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDomainRealTimeQpsDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
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
            temp_model = DescribeDomainRealTimeQpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDomainRealTimeQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeQpsDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeReqHitRateDataRequest(TeaModel):
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


class DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel(TeaModel):
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


class DescribeDomainRealTimeReqHitRateDataResponseBodyData(TeaModel):
    def __init__(
        self,
        req_hit_rate_data_model: List[DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel] = None,
    ):
        self.req_hit_rate_data_model = req_hit_rate_data_model

    def validate(self):
        if self.req_hit_rate_data_model:
            for k in self.req_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel()
                self.req_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeReqHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDomainRealTimeReqHitRateDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
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
            temp_model = DescribeDomainRealTimeReqHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDomainRealTimeReqHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeReqHitRateDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcBpsDataRequest(TeaModel):
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


class DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule(TeaModel):
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


class DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        real_time_src_bps_data_per_interval: DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.real_time_src_bps_data_per_interval = real_time_src_bps_data_per_interval
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.real_time_src_bps_data_per_interval:
            self.real_time_src_bps_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.real_time_src_bps_data_per_interval is not None:
            result['RealTimeSrcBpsDataPerInterval'] = self.real_time_src_bps_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RealTimeSrcBpsDataPerInterval') is not None:
            temp_model = DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval()
            self.real_time_src_bps_data_per_interval = temp_model.from_map(m['RealTimeSrcBpsDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainRealTimeSrcBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeSrcBpsDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcHttpCodeDataRequest(TeaModel):
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


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData(TeaModel):
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


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        real_time_src_code_proportion_data: List[DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData] = None,
    ):
        self.real_time_src_code_proportion_data = real_time_src_code_proportion_data

    def validate(self):
        if self.real_time_src_code_proportion_data:
            for k in self.real_time_src_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData()
                self.real_time_src_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        value: DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData] = None,
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
                temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        real_time_src_http_code_data: DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.real_time_src_http_code_data = real_time_src_http_code_data

    def validate(self):
        if self.real_time_src_http_code_data:
            self.real_time_src_http_code_data.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_src_http_code_data is not None:
            result['RealTimeSrcHttpCodeData'] = self.real_time_src_http_code_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeSrcHttpCodeData') is not None:
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData()
            self.real_time_src_http_code_data = temp_model.from_map(m['RealTimeSrcHttpCodeData'])
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeSrcHttpCodeDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcTrafficDataRequest(TeaModel):
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


class DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule(TeaModel):
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


class DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        real_time_src_traffic_data_per_interval: DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.real_time_src_traffic_data_per_interval = real_time_src_traffic_data_per_interval

    def validate(self):
        if self.real_time_src_traffic_data_per_interval:
            self.real_time_src_traffic_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.real_time_src_traffic_data_per_interval is not None:
            result['RealTimeSrcTrafficDataPerInterval'] = self.real_time_src_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RealTimeSrcTrafficDataPerInterval') is not None:
            temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval()
            self.real_time_src_traffic_data_per_interval = temp_model.from_map(m['RealTimeSrcTrafficDataPerInterval'])
        return self


class DescribeDomainRealTimeSrcTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeSrcTrafficDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeTrafficDataRequest(TeaModel):
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


class DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule(TeaModel):
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


class DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        real_time_traffic_data_per_interval: DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.real_time_traffic_data_per_interval = real_time_traffic_data_per_interval
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.real_time_traffic_data_per_interval:
            self.real_time_traffic_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.real_time_traffic_data_per_interval is not None:
            result['RealTimeTrafficDataPerInterval'] = self.real_time_traffic_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RealTimeTrafficDataPerInterval') is not None:
            temp_model = DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval()
            self.real_time_traffic_data_per_interval = temp_model.from_map(m['RealTimeTrafficDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainRealTimeTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRealTimeTrafficDataResponseBody = None,
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
            temp_model = DescribeDomainRealTimeTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRegionDataRequest(TeaModel):
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


class DescribeDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(
        self,
        total_query: str = None,
        total_bytes: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        req_err_rate: str = None,
        avg_object_size: str = None,
        bps: str = None,
        qps: str = None,
        region_ename: str = None,
        region: str = None,
        proportion: str = None,
        bytes_proportion: str = None,
    ):
        self.total_query = total_query
        self.total_bytes = total_bytes
        self.avg_response_rate = avg_response_rate
        self.avg_response_time = avg_response_time
        self.req_err_rate = req_err_rate
        self.avg_object_size = avg_object_size
        self.bps = bps
        self.qps = qps
        self.region_ename = region_ename
        self.region = region
        self.proportion = proportion
        self.bytes_proportion = bytes_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.region is not None:
            result['Region'] = self.region
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        return self


class DescribeDomainRegionDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        region_proportion_data: List[DescribeDomainRegionDataResponseBodyValueRegionProportionData] = None,
    ):
        self.region_proportion_data = region_proportion_data

    def validate(self):
        if self.region_proportion_data:
            for k in self.region_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRegionDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        value: DescribeDomainRegionDataResponseBodyValue = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('Value') is not None:
            temp_model = DescribeDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainRegionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainRegionDataResponseBody = None,
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
            temp_model = DescribeDomainRegionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainReqHitRateDataRequest(TeaModel):
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


class DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        https_value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.https_value = https_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainReqHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        req_hit_rate_interval: DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.req_hit_rate_interval = req_hit_rate_interval
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.req_hit_rate_interval:
            self.req_hit_rate_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.req_hit_rate_interval is not None:
            result['ReqHitRateInterval'] = self.req_hit_rate_interval.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReqHitRateInterval') is not None:
            temp_model = DescribeDomainReqHitRateDataResponseBodyReqHitRateInterval()
            self.req_hit_rate_interval = temp_model.from_map(m['ReqHitRateInterval'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainReqHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainReqHitRateDataResponseBody = None,
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
            temp_model = DescribeDomainReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsBySourceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        sources: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.sources = sources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains(TeaModel):
    def __init__(
        self,
        domain_names: List[str] = None,
    ):
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_names is not None:
            result['domainNames'] = self.domain_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainNames') is not None:
            self.domain_names = m.get('domainNames')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: str = None,
        create_time: str = None,
        domain_cname: str = None,
        domain_name: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.create_time = create_time
        self.domain_cname = domain_cname
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_cname is not None:
            result['DomainCname'] = self.domain_cname
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainCname') is not None:
            self.domain_cname = m.get('DomainCname')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos(TeaModel):
    def __init__(
        self,
        domain_info: List[DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo] = None,
    ):
        self.domain_info = domain_info

    def validate(self):
        if self.domain_info:
            for k in self.domain_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['domainInfo'] = []
        if self.domain_info is not None:
            for k in self.domain_info:
                result['domainInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_info = []
        if m.get('domainInfo') is not None:
            for k in m.get('domainInfo'):
                temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfosDomainInfo()
                self.domain_info.append(temp_model.from_map(k))
        return self


class DescribeDomainsBySourceResponseBodyDomainsListDomainsData(TeaModel):
    def __init__(
        self,
        domains: DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains = None,
        source: str = None,
        domain_infos: DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos = None,
    ):
        self.domains = domains
        self.source = source
        self.domain_infos = domain_infos

    def validate(self):
        if self.domains:
            self.domains.validate()
        if self.domain_infos:
            self.domain_infos.validate()

    def to_map(self):
        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.source is not None:
            result['Source'] = self.source
        if self.domain_infos is not None:
            result['DomainInfos'] = self.domain_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('DomainInfos') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsDataDomainInfos()
            self.domain_infos = temp_model.from_map(m['DomainInfos'])
        return self


class DescribeDomainsBySourceResponseBodyDomainsList(TeaModel):
    def __init__(
        self,
        domains_data: List[DescribeDomainsBySourceResponseBodyDomainsListDomainsData] = None,
    ):
        self.domains_data = domains_data

    def validate(self):
        if self.domains_data:
            for k in self.domains_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainsData'] = []
        if self.domains_data is not None:
            for k in self.domains_data:
                result['DomainsData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains_data = []
        if m.get('DomainsData') is not None:
            for k in m.get('DomainsData'):
                temp_model = DescribeDomainsBySourceResponseBodyDomainsListDomainsData()
                self.domains_data.append(temp_model.from_map(k))
        return self


class DescribeDomainsBySourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domains_list: DescribeDomainsBySourceResponseBodyDomainsList = None,
        sources: str = None,
    ):
        self.request_id = request_id
        self.domains_list = domains_list
        self.sources = sources

    def validate(self):
        if self.domains_list:
            self.domains_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domains_list is not None:
            result['DomainsList'] = self.domains_list.to_map()
        if self.sources is not None:
            result['Sources'] = self.sources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainsList') is not None:
            temp_model = DescribeDomainsBySourceResponseBodyDomainsList()
            self.domains_list = temp_model.from_map(m['DomainsList'])
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        return self


class DescribeDomainsBySourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainsBySourceResponseBody = None,
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
            temp_model = DescribeDomainsBySourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcBpsDataRequest(TeaModel):
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


class DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        https_value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.https_value = https_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        src_bps_data_per_interval: DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval = None,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.src_bps_data_per_interval = src_bps_data_per_interval
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.src_bps_data_per_interval:
            self.src_bps_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.src_bps_data_per_interval is not None:
            result['SrcBpsDataPerInterval'] = self.src_bps_data_per_interval.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SrcBpsDataPerInterval') is not None:
            temp_model = DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerInterval()
            self.src_bps_data_per_interval = temp_model.from_map(m['SrcBpsDataPerInterval'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainSrcBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainSrcBpsDataResponseBody = None,
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
            temp_model = DescribeDomainSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcHttpCodeDataRequest(TeaModel):
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


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData(TeaModel):
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


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        code_proportion_data: List[DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData] = None,
    ):
        self.code_proportion_data = code_proportion_data

    def validate(self):
        if self.code_proportion_data:
            for k in self.code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CodeProportionData'] = []
        if self.code_proportion_data is not None:
            for k in self.code_proportion_data:
                result['CodeProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_proportion_data = []
        if m.get('CodeProportionData') is not None:
            for k in m.get('CodeProportionData'):
                temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData()
                self.code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        value: DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.time_stamp = time_stamp

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData] = None,
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
                temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        http_code_data: DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.http_code_data = http_code_data

    def validate(self):
        if self.http_code_data:
            self.http_code_data.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.http_code_data is not None:
            result['HttpCodeData'] = self.http_code_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('HttpCodeData') is not None:
            temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData()
            self.http_code_data = temp_model.from_map(m['HttpCodeData'])
        return self


class DescribeDomainSrcHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainSrcHttpCodeDataResponseBody = None,
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
            temp_model = DescribeDomainSrcHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcQpsDataRequest(TeaModel):
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


class DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule(TeaModel):
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


class DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        src_qps_data_per_interval: DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.src_qps_data_per_interval = src_qps_data_per_interval

    def validate(self):
        if self.src_qps_data_per_interval:
            self.src_qps_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.src_qps_data_per_interval is not None:
            result['SrcQpsDataPerInterval'] = self.src_qps_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('SrcQpsDataPerInterval') is not None:
            temp_model = DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval()
            self.src_qps_data_per_interval = temp_model.from_map(m['SrcQpsDataPerInterval'])
        return self


class DescribeDomainSrcQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainSrcQpsDataResponseBody = None,
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
            temp_model = DescribeDomainSrcQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcTopUrlVisitRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        sort_by: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBody(TeaModel):
    def __init__(
        self,
        url_500list: DescribeDomainSrcTopUrlVisitResponseBodyUrl500List = None,
        url_200list: DescribeDomainSrcTopUrlVisitResponseBodyUrl200List = None,
        url_400list: DescribeDomainSrcTopUrlVisitResponseBodyUrl400List = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        url_300list: DescribeDomainSrcTopUrlVisitResponseBodyUrl300List = None,
        all_url_list: DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList = None,
    ):
        self.url_500list = url_500list
        self.url_200list = url_200list
        self.url_400list = url_400list
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.url_300list = url_300list
        self.all_url_list = all_url_list

    def validate(self):
        if self.url_500list:
            self.url_500list.validate()
        if self.url_200list:
            self.url_200list.validate()
        if self.url_400list:
            self.url_400list.validate()
        if self.url_300list:
            self.url_300list.validate()
        if self.all_url_list:
            self.all_url_list.validate()

    def to_map(self):
        result = dict()
        if self.url_500list is not None:
            result['Url500List'] = self.url_500list.to_map()
        if self.url_200list is not None:
            result['Url200List'] = self.url_200list.to_map()
        if self.url_400list is not None:
            result['Url400List'] = self.url_400list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.url_300list is not None:
            result['Url300List'] = self.url_300list.to_map()
        if self.all_url_list is not None:
            result['AllUrlList'] = self.all_url_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url500List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        if m.get('Url200List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url300List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('AllUrlList') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        return self


class DescribeDomainSrcTopUrlVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainSrcTopUrlVisitResponseBody = None,
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
            temp_model = DescribeDomainSrcTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcTrafficDataRequest(TeaModel):
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


class DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        https_value: str = None,
        time_stamp: str = None,
    ):
        self.value = value
        self.https_value = https_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        src_traffic_data_per_interval: DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.src_traffic_data_per_interval = src_traffic_data_per_interval

    def validate(self):
        if self.src_traffic_data_per_interval:
            self.src_traffic_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.src_traffic_data_per_interval is not None:
            result['SrcTrafficDataPerInterval'] = self.src_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('SrcTrafficDataPerInterval') is not None:
            temp_model = DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval()
            self.src_traffic_data_per_interval = temp_model.from_map(m['SrcTrafficDataPerInterval'])
        return self


class DescribeDomainSrcTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainSrcTrafficDataResponseBody = None,
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
            temp_model = DescribeDomainSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsUsageByDayRequest(TeaModel):
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


class DescribeDomainsUsageByDayResponseBodyUsageTotal(TeaModel):
    def __init__(
        self,
        max_src_bps_time: str = None,
        request_hit_rate: str = None,
        max_bps: str = None,
        total_access: str = None,
        bytes_hit_rate: str = None,
        total_traffic: str = None,
        max_bps_time: str = None,
        max_src_bps: str = None,
    ):
        self.max_src_bps_time = max_src_bps_time
        self.request_hit_rate = request_hit_rate
        self.max_bps = max_bps
        self.total_access = total_access
        self.bytes_hit_rate = bytes_hit_rate
        self.total_traffic = total_traffic
        self.max_bps_time = max_bps_time
        self.max_src_bps = max_src_bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_src_bps_time is not None:
            result['MaxSrcBpsTime'] = self.max_src_bps_time
        if self.request_hit_rate is not None:
            result['RequestHitRate'] = self.request_hit_rate
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.bytes_hit_rate is not None:
            result['BytesHitRate'] = self.bytes_hit_rate
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.max_src_bps is not None:
            result['MaxSrcBps'] = self.max_src_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSrcBpsTime') is not None:
            self.max_src_bps_time = m.get('MaxSrcBpsTime')
        if m.get('RequestHitRate') is not None:
            self.request_hit_rate = m.get('RequestHitRate')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('BytesHitRate') is not None:
            self.bytes_hit_rate = m.get('BytesHitRate')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('MaxSrcBps') is not None:
            self.max_src_bps = m.get('MaxSrcBps')
        return self


class DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay(TeaModel):
    def __init__(
        self,
        max_src_bps_time: str = None,
        qps: str = None,
        request_hit_rate: str = None,
        max_bps: str = None,
        total_access: str = None,
        time_stamp: str = None,
        bytes_hit_rate: str = None,
        total_traffic: str = None,
        max_src_bps: str = None,
        max_bps_time: str = None,
    ):
        self.max_src_bps_time = max_src_bps_time
        self.qps = qps
        self.request_hit_rate = request_hit_rate
        self.max_bps = max_bps
        self.total_access = total_access
        self.time_stamp = time_stamp
        self.bytes_hit_rate = bytes_hit_rate
        self.total_traffic = total_traffic
        self.max_src_bps = max_src_bps
        self.max_bps_time = max_bps_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_src_bps_time is not None:
            result['MaxSrcBpsTime'] = self.max_src_bps_time
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.request_hit_rate is not None:
            result['RequestHitRate'] = self.request_hit_rate
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.bytes_hit_rate is not None:
            result['BytesHitRate'] = self.bytes_hit_rate
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.max_src_bps is not None:
            result['MaxSrcBps'] = self.max_src_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSrcBpsTime') is not None:
            self.max_src_bps_time = m.get('MaxSrcBpsTime')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RequestHitRate') is not None:
            self.request_hit_rate = m.get('RequestHitRate')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('BytesHitRate') is not None:
            self.bytes_hit_rate = m.get('BytesHitRate')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('MaxSrcBps') is not None:
            self.max_src_bps = m.get('MaxSrcBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        return self


class DescribeDomainsUsageByDayResponseBodyUsageByDays(TeaModel):
    def __init__(
        self,
        usage_by_day: List[DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay] = None,
    ):
        self.usage_by_day = usage_by_day

    def validate(self):
        if self.usage_by_day:
            for k in self.usage_by_day:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UsageByDay'] = []
        if self.usage_by_day is not None:
            for k in self.usage_by_day:
                result['UsageByDay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_by_day = []
        if m.get('UsageByDay') is not None:
            for k in m.get('UsageByDay'):
                temp_model = DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay()
                self.usage_by_day.append(temp_model.from_map(k))
        return self


class DescribeDomainsUsageByDayResponseBody(TeaModel):
    def __init__(
        self,
        usage_total: DescribeDomainsUsageByDayResponseBodyUsageTotal = None,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        usage_by_days: DescribeDomainsUsageByDayResponseBodyUsageByDays = None,
    ):
        self.usage_total = usage_total
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.usage_by_days = usage_by_days

    def validate(self):
        if self.usage_total:
            self.usage_total.validate()
        if self.usage_by_days:
            self.usage_by_days.validate()

    def to_map(self):
        result = dict()
        if self.usage_total is not None:
            result['UsageTotal'] = self.usage_total.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.usage_by_days is not None:
            result['UsageByDays'] = self.usage_by_days.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsageTotal') is not None:
            temp_model = DescribeDomainsUsageByDayResponseBodyUsageTotal()
            self.usage_total = temp_model.from_map(m['UsageTotal'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('UsageByDays') is not None:
            temp_model = DescribeDomainsUsageByDayResponseBodyUsageByDays()
            self.usage_by_days = temp_model.from_map(m['UsageByDays'])
        return self


class DescribeDomainsUsageByDayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainsUsageByDayResponseBody = None,
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
            temp_model = DescribeDomainsUsageByDayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopClientIpVisitRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        location_name_en: str = None,
        start_time: str = None,
        end_time: str = None,
        sort_by: str = None,
        limit: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.location_name_en = location_name_en
        self.start_time = start_time
        self.end_time = end_time
        self.sort_by = sort_by
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class DescribeDomainTopClientIpVisitResponseBodyClientIpList(TeaModel):
    def __init__(
        self,
        acc: int = None,
        traffic: int = None,
        rank: int = None,
        client_ip: str = None,
    ):
        self.acc = acc
        self.traffic = traffic
        self.rank = rank
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        return self


class DescribeDomainTopClientIpVisitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        client_ip_list: List[DescribeDomainTopClientIpVisitResponseBodyClientIpList] = None,
    ):
        self.request_id = request_id
        self.client_ip_list = client_ip_list

    def validate(self):
        if self.client_ip_list:
            for k in self.client_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ClientIpList'] = []
        if self.client_ip_list is not None:
            for k in self.client_ip_list:
                result['ClientIpList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.client_ip_list = []
        if m.get('ClientIpList') is not None:
            for k in m.get('ClientIpList'):
                temp_model = DescribeDomainTopClientIpVisitResponseBodyClientIpList()
                self.client_ip_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopClientIpVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainTopClientIpVisitResponseBody = None,
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
            temp_model = DescribeDomainTopClientIpVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopReferVisitRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        sort_by: str = None,
        percent: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.sort_by = sort_by
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.percent is not None:
            result['Percent'] = self.percent
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
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        return self


class DescribeDomainTopReferVisitResponseBodyTopReferListReferList(TeaModel):
    def __init__(
        self,
        visit_data: str = None,
        refer_detail: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.visit_data = visit_data
        self.refer_detail = refer_detail
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.refer_detail is not None:
            result['ReferDetail'] = self.refer_detail
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('ReferDetail') is not None:
            self.refer_detail = m.get('ReferDetail')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainTopReferVisitResponseBodyTopReferList(TeaModel):
    def __init__(
        self,
        refer_list: List[DescribeDomainTopReferVisitResponseBodyTopReferListReferList] = None,
    ):
        self.refer_list = refer_list

    def validate(self):
        if self.refer_list:
            for k in self.refer_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainTopReferVisitResponseBodyTopReferListReferList()
                self.refer_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopReferVisitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        top_refer_list: DescribeDomainTopReferVisitResponseBodyTopReferList = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.top_refer_list = top_refer_list

    def validate(self):
        if self.top_refer_list:
            self.top_refer_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_refer_list is not None:
            result['TopReferList'] = self.top_refer_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TopReferList') is not None:
            temp_model = DescribeDomainTopReferVisitResponseBodyTopReferList()
            self.top_refer_list = temp_model.from_map(m['TopReferList'])
        return self


class DescribeDomainTopReferVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainTopReferVisitResponseBody = None,
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
            temp_model = DescribeDomainTopReferVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopUrlVisitRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        sort_by: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(
        self,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
        flow: str = None,
        flow_proportion: float = None,
    ):
        self.url_detail = url_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion
        self.flow = flow
        self.flow_proportion = flow_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail
        if self.visit_data is not None:
            result['VisitData'] = self.visit_data
        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')
        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')
        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')
        return self


class DescribeDomainTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBody(TeaModel):
    def __init__(
        self,
        url_500list: DescribeDomainTopUrlVisitResponseBodyUrl500List = None,
        url_200list: DescribeDomainTopUrlVisitResponseBodyUrl200List = None,
        url_400list: DescribeDomainTopUrlVisitResponseBodyUrl400List = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        url_300list: DescribeDomainTopUrlVisitResponseBodyUrl300List = None,
        all_url_list: DescribeDomainTopUrlVisitResponseBodyAllUrlList = None,
    ):
        self.url_500list = url_500list
        self.url_200list = url_200list
        self.url_400list = url_400list
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.url_300list = url_300list
        self.all_url_list = all_url_list

    def validate(self):
        if self.url_500list:
            self.url_500list.validate()
        if self.url_200list:
            self.url_200list.validate()
        if self.url_400list:
            self.url_400list.validate()
        if self.url_300list:
            self.url_300list.validate()
        if self.all_url_list:
            self.all_url_list.validate()

    def to_map(self):
        result = dict()
        if self.url_500list is not None:
            result['Url500List'] = self.url_500list.to_map()
        if self.url_200list is not None:
            result['Url200List'] = self.url_200list.to_map()
        if self.url_400list is not None:
            result['Url400List'] = self.url_400list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.url_300list is not None:
            result['Url300List'] = self.url_300list.to_map()
        if self.all_url_list is not None:
            result['AllUrlList'] = self.all_url_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url500List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        if m.get('Url200List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url300List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('AllUrlList') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        return self


class DescribeDomainTopUrlVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainTopUrlVisitResponseBody = None,
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
            temp_model = DescribeDomainTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTrafficDataRequest(TeaModel):
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


class DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        https_domestic_value: str = None,
        value: str = None,
        overseas_value: str = None,
        https_value: str = None,
        https_overseas_value: str = None,
        time_stamp: str = None,
        domestic_value: str = None,
    ):
        self.https_domestic_value = https_domestic_value
        self.value = value
        self.overseas_value = overseas_value
        self.https_value = https_value
        self.https_overseas_value = https_overseas_value
        self.time_stamp = time_stamp
        self.domestic_value = domestic_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.value is not None:
            result['Value'] = self.value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        return self


class DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        traffic_data_per_interval: DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.traffic_data_per_interval = traffic_data_per_interval
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainTrafficDataResponseBody = None,
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
            temp_model = DescribeDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainUsageDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        data_protocol: str = None,
        domain_name: str = None,
        start_time: str = None,
        end_time: str = None,
        area: str = None,
        field: str = None,
        interval: str = None,
    ):
        self.owner_id = owner_id
        self.data_protocol = data_protocol
        self.domain_name = domain_name
        self.start_time = start_time
        self.end_time = end_time
        self.area = area
        self.field = field
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.data_protocol is not None:
            result['DataProtocol'] = self.data_protocol
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.area is not None:
            result['Area'] = self.area
        if self.field is not None:
            result['Field'] = self.field
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DataProtocol') is not None:
            self.data_protocol = m.get('DataProtocol')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        value: str = None,
        peak_time: str = None,
        time_stamp: str = None,
        special_value: str = None,
    ):
        self.value = value
        self.peak_time = peak_time
        self.time_stamp = time_stamp
        self.special_value = special_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.special_value is not None:
            result['SpecialValue'] = self.special_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('SpecialValue') is not None:
            self.special_value = m.get('SpecialValue')
        return self


class DescribeDomainUsageDataResponseBodyUsageDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainUsageDataResponseBody(TeaModel):
    def __init__(
        self,
        usage_data_per_interval: DescribeDomainUsageDataResponseBodyUsageDataPerInterval = None,
        type: str = None,
        area: str = None,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.usage_data_per_interval = usage_data_per_interval
        self.type = type
        self.area = area
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.usage_data_per_interval:
            self.usage_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.usage_data_per_interval is not None:
            result['UsageDataPerInterval'] = self.usage_data_per_interval.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.area is not None:
            result['Area'] = self.area
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsageDataPerInterval') is not None:
            temp_model = DescribeDomainUsageDataResponseBodyUsageDataPerInterval()
            self.usage_data_per_interval = temp_model.from_map(m['UsageDataPerInterval'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainUsageDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainUsageDataResponseBody = None,
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
            temp_model = DescribeDomainUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainUvDataRequest(TeaModel):
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


class DescribeDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
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


class DescribeDomainUvDataResponseBodyUvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeDomainUvDataResponseBodyUvDataIntervalUsageData] = None,
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
                temp_model = DescribeDomainUvDataResponseBodyUvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainUvDataResponseBody(TeaModel):
    def __init__(
        self,
        uv_data_interval: DescribeDomainUvDataResponseBodyUvDataInterval = None,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.uv_data_interval = uv_data_interval
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        result = dict()
        if self.uv_data_interval is not None:
            result['UvDataInterval'] = self.uv_data_interval.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UvDataInterval') is not None:
            temp_model = DescribeDomainUvDataResponseBodyUvDataInterval()
            self.uv_data_interval = temp_model.from_map(m['UvDataInterval'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeDomainUvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainUvDataResponseBody = None,
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
            temp_model = DescribeDomainUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFCTriggerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        trigger_arn: str = None,
    ):
        self.owner_id = owner_id
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class DescribeFCTriggerResponseBodyFCTrigger(TeaModel):
    def __init__(
        self,
        trigger_arn: str = None,
        role_arn: str = None,
        source_arn: str = None,
        notes: str = None,
        event_meta_name: str = None,
        event_meta_version: str = None,
    ):
        self.trigger_arn = trigger_arn
        self.role_arn = role_arn
        self.source_arn = source_arn
        self.notes = notes
        self.event_meta_name = event_meta_name
        self.event_meta_version = event_meta_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        return self


class DescribeFCTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        fctrigger: DescribeFCTriggerResponseBodyFCTrigger = None,
    ):
        self.request_id = request_id
        self.fctrigger = fctrigger

    def validate(self):
        if self.fctrigger:
            self.fctrigger.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.fctrigger is not None:
            result['FCTrigger'] = self.fctrigger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FCTrigger') is not None:
            temp_model = DescribeFCTriggerResponseBodyFCTrigger()
            self.fctrigger = temp_model.from_map(m['FCTrigger'])
        return self


class DescribeFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFCTriggerResponseBody = None,
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
            temp_model = DescribeFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIllegalUrlExportTaskRequest(TeaModel):
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


class DescribeIllegalUrlExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        download_url: str = None,
    ):
        self.status = status
        self.request_id = request_id
        self.download_url = download_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        return self


class DescribeIllegalUrlExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIllegalUrlExportTaskResponseBody = None,
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
            temp_model = DescribeIllegalUrlExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpInfoRequest(TeaModel):
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


class DescribeIpInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        isp: str = None,
        region: str = None,
        isp_ename: str = None,
        cdn_ip: str = None,
        region_ename: str = None,
    ):
        self.request_id = request_id
        self.isp = isp
        self.region = region
        self.isp_ename = isp_ename
        self.cdn_ip = cdn_ip
        self.region_ename = region_ename

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.region is not None:
            result['Region'] = self.region
        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename
        if self.cdn_ip is not None:
            result['CdnIp'] = self.cdn_ip
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')
        if m.get('CdnIp') is not None:
            self.cdn_ip = m.get('CdnIp')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        return self


class DescribeIpInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIpInfoResponseBody = None,
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
            temp_model = DescribeIpInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeL2VipsByDomainRequest(TeaModel):
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


class DescribeL2VipsByDomainResponseBodyVips(TeaModel):
    def __init__(
        self,
        vip: List[str] = None,
    ):
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeL2VipsByDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        vips: DescribeL2VipsByDomainResponseBodyVips = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.vips = vips

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Vips') is not None:
            temp_model = DescribeL2VipsByDomainResponseBodyVips()
            self.vips = temp_model.from_map(m['Vips'])
        return self


class DescribeL2VipsByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeL2VipsByDomainResponseBody = None,
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
            temp_model = DescribeL2VipsByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRangeDataByLocateAndIspServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_names: str = None,
        start_time: str = None,
        end_time: str = None,
        isp_names: str = None,
        location_names: str = None,
    ):
        self.owner_id = owner_id
        self.domain_names = domain_names
        self.start_time = start_time
        self.end_time = end_time
        self.isp_names = isp_names
        self.location_names = location_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_names is not None:
            result['IspNames'] = self.isp_names
        if self.location_names is not None:
            result['LocationNames'] = self.location_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNames') is not None:
            self.isp_names = m.get('IspNames')
        if m.get('LocationNames') is not None:
            self.location_names = m.get('LocationNames')
        return self


class DescribeRangeDataByLocateAndIspServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        json_result: str = None,
    ):
        self.request_id = request_id
        self.json_result = json_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class DescribeRangeDataByLocateAndIspServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRangeDataByLocateAndIspServiceResponseBody = None,
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
            temp_model = DescribeRangeDataByLocateAndIspServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRealtimeDeliveryAccRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        interval: str = None,
        project: str = None,
        log_store: str = None,
    ):
        self.owner_id = owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.project = project
        self.log_store = log_store

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.project is not None:
            result['Project'] = self.project
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        return self


class DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData(TeaModel):
    def __init__(
        self,
        failed_num: int = None,
        time_stamp: str = None,
        success_num: int = None,
    ):
        self.failed_num = failed_num
        self.time_stamp = time_stamp
        self.success_num = success_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.success_num is not None:
            result['SuccessNum'] = self.success_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('SuccessNum') is not None:
            self.success_num = m.get('SuccessNum')
        return self


class DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData(TeaModel):
    def __init__(
        self,
        acc_data: List[DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData] = None,
    ):
        self.acc_data = acc_data

    def validate(self):
        if self.acc_data:
            for k in self.acc_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AccData'] = []
        if self.acc_data is not None:
            for k in self.acc_data:
                result['AccData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acc_data = []
        if m.get('AccData') is not None:
            for k in m.get('AccData'):
                temp_model = DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData()
                self.acc_data.append(temp_model.from_map(k))
        return self


class DescribeRealtimeDeliveryAccResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        reat_time_delivery_acc_data: DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData = None,
    ):
        self.request_id = request_id
        self.reat_time_delivery_acc_data = reat_time_delivery_acc_data

    def validate(self):
        if self.reat_time_delivery_acc_data:
            self.reat_time_delivery_acc_data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reat_time_delivery_acc_data is not None:
            result['ReatTimeDeliveryAccData'] = self.reat_time_delivery_acc_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReatTimeDeliveryAccData') is not None:
            temp_model = DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData()
            self.reat_time_delivery_acc_data = temp_model.from_map(m['ReatTimeDeliveryAccData'])
        return self


class DescribeRealtimeDeliveryAccResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRealtimeDeliveryAccResponseBody = None,
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
            temp_model = DescribeRealtimeDeliveryAccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshQuotaRequest(TeaModel):
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


class DescribeRefreshQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        block_remain: str = None,
        regex_remain: str = None,
        dir_remain: str = None,
        url_quota: str = None,
        preload_quota: str = None,
        preload_edge_quota: str = None,
        url_remain: str = None,
        preload_edge_remain: str = None,
        preload_remain: str = None,
        block_quota: str = None,
        regex_quota: str = None,
        dir_quota: str = None,
    ):
        self.request_id = request_id
        self.block_remain = block_remain
        self.regex_remain = regex_remain
        self.dir_remain = dir_remain
        self.url_quota = url_quota
        self.preload_quota = preload_quota
        self.preload_edge_quota = preload_edge_quota
        self.url_remain = url_remain
        self.preload_edge_remain = preload_edge_remain
        self.preload_remain = preload_remain
        self.block_quota = block_quota
        self.regex_quota = regex_quota
        self.dir_quota = dir_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain
        if self.regex_remain is not None:
            result['RegexRemain'] = self.regex_remain
        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain
        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        if self.preload_edge_quota is not None:
            result['PreloadEdgeQuota'] = self.preload_edge_quota
        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain
        if self.preload_edge_remain is not None:
            result['PreloadEdgeRemain'] = self.preload_edge_remain
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.regex_quota is not None:
            result['RegexQuota'] = self.regex_quota
        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')
        if m.get('RegexRemain') is not None:
            self.regex_remain = m.get('RegexRemain')
        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        if m.get('PreloadEdgeQuota') is not None:
            self.preload_edge_quota = m.get('PreloadEdgeQuota')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        if m.get('PreloadEdgeRemain') is not None:
            self.preload_edge_remain = m.get('PreloadEdgeRemain')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('RegexQuota') is not None:
            self.regex_quota = m.get('RegexQuota')
        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')
        return self


class DescribeRefreshQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRefreshQuotaResponseBody = None,
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
            temp_model = DescribeRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshTaskByIdRequest(TeaModel):
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


class DescribeRefreshTaskByIdResponseBodyTasks(TeaModel):
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


class DescribeRefreshTaskByIdResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        tasks: List[DescribeRefreshTaskByIdResponseBodyTasks] = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.tasks = tasks
        self.request_id = request_id

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribeRefreshTaskByIdResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRefreshTaskByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRefreshTaskByIdResponseBody = None,
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
            temp_model = DescribeRefreshTaskByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshTasksRequest(TeaModel):
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
        resource_group_id: str = None,
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
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeRefreshTasksResponseBodyTasksCDNTask(TeaModel):
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


class DescribeRefreshTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        cdntask: List[DescribeRefreshTasksResponseBodyTasksCDNTask] = None,
    ):
        self.cdntask = cdntask

    def validate(self):
        if self.cdntask:
            for k in self.cdntask:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CDNTask'] = []
        if self.cdntask is not None:
            for k in self.cdntask:
                result['CDNTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cdntask = []
        if m.get('CDNTask') is not None:
            for k in m.get('CDNTask'):
                temp_model = DescribeRefreshTasksResponseBodyTasksCDNTask()
                self.cdntask.append(temp_model.from_map(k))
        return self


class DescribeRefreshTasksResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        tasks: DescribeRefreshTasksResponseBodyTasks = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.tasks = tasks
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Tasks') is not None:
            temp_model = DescribeRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeRefreshTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRefreshTasksResponseBody = None,
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
            temp_model = DescribeRefreshTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStagingIpRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeStagingIpResponseBodyIPV4s(TeaModel):
    def __init__(
        self,
        ipv4: List[str] = None,
    ):
        self.ipv4 = ipv4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ipv4 is not None:
            result['IPV4'] = self.ipv4
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPV4') is not None:
            self.ipv4 = m.get('IPV4')
        return self


class DescribeStagingIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ipv4s: DescribeStagingIpResponseBodyIPV4s = None,
    ):
        self.request_id = request_id
        self.ipv4s = ipv4s

    def validate(self):
        if self.ipv4s:
            self.ipv4s.validate()

    def to_map(self):
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
            temp_model = DescribeStagingIpResponseBodyIPV4s()
            self.ipv4s = temp_model.from_map(m['IPV4s'])
        return self


class DescribeStagingIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStagingIpResponseBody = None,
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
            temp_model = DescribeStagingIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagResourcesRequestTag(TeaModel):
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


class DescribeTagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_type: str = None,
        scope: str = None,
        resource_id: List[str] = None,
        tag: List[DescribeTagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_type = resource_type
        self.scope = scope
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
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
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBodyTagResourcesTag(TeaModel):
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


class DescribeTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag: List[DescribeTagResourcesResponseBodyTagResourcesTag] = None,
        resource_id: str = None,
    ):
        self.tag = tag
        self.resource_id = resource_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeTagResourcesResponseBodyTagResourcesTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_resources: List[DescribeTagResourcesResponseBodyTagResources] = None,
    ):
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTagResourcesResponseBody = None,
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
            temp_model = DescribeTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopDomainsByFlowRequest(TeaModel):
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


class DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(
        self,
        max_bps: float = None,
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


class DescribeTopDomainsByFlowResponseBodyTopDomains(TeaModel):
    def __init__(
        self,
        top_domain: List[DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain] = None,
    ):
        self.top_domain = top_domain

    def validate(self):
        if self.top_domain:
            for k in self.top_domain:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        return self


class DescribeTopDomainsByFlowResponseBody(TeaModel):
    def __init__(
        self,
        top_domains: DescribeTopDomainsByFlowResponseBodyTopDomains = None,
        end_time: str = None,
        request_id: str = None,
        domain_online_count: int = None,
        start_time: str = None,
        domain_count: int = None,
    ):
        self.top_domains = top_domains
        self.end_time = end_time
        self.request_id = request_id
        self.domain_online_count = domain_online_count
        self.start_time = start_time
        self.domain_count = domain_count

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        result = dict()
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TopDomains') is not None:
            temp_model = DescribeTopDomainsByFlowResponseBodyTopDomains()
            self.top_domains = temp_model.from_map(m['TopDomains'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        return self


class DescribeTopDomainsByFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTopDomainsByFlowResponseBody = None,
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
            temp_model = DescribeTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserCertificateExpireCountRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeUserCertificateExpireCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        expire_within_30days_count: int = None,
        expired_count: int = None,
    ):
        self.request_id = request_id
        self.expire_within_30days_count = expire_within_30days_count
        self.expired_count = expired_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire_within_30days_count is not None:
            result['ExpireWithin30DaysCount'] = self.expire_within_30days_count
        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExpireWithin30DaysCount') is not None:
            self.expire_within_30days_count = m.get('ExpireWithin30DaysCount')
        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')
        return self


class DescribeUserCertificateExpireCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserCertificateExpireCountResponseBody = None,
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
            temp_model = DescribeUserCertificateExpireCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserConfigsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        config: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class DescribeUserConfigsResponseBodyConfigsOssLogConfig(TeaModel):
    def __init__(
        self,
        prefix: str = None,
        enable: str = None,
        bucket: str = None,
    ):
        self.prefix = prefix
        self.enable = enable
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class DescribeUserConfigsResponseBodyConfigsGreenManagerConfig(TeaModel):
    def __init__(
        self,
        quota: str = None,
        ratio: str = None,
    ):
        self.quota = quota
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        return self


class DescribeUserConfigsResponseBodyConfigsWafConfig(TeaModel):
    def __init__(
        self,
        enable: str = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeUserConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        oss_log_config: DescribeUserConfigsResponseBodyConfigsOssLogConfig = None,
        green_manager_config: DescribeUserConfigsResponseBodyConfigsGreenManagerConfig = None,
        waf_config: DescribeUserConfigsResponseBodyConfigsWafConfig = None,
    ):
        self.oss_log_config = oss_log_config
        self.green_manager_config = green_manager_config
        self.waf_config = waf_config

    def validate(self):
        if self.oss_log_config:
            self.oss_log_config.validate()
        if self.green_manager_config:
            self.green_manager_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        result = dict()
        if self.oss_log_config is not None:
            result['OssLogConfig'] = self.oss_log_config.to_map()
        if self.green_manager_config is not None:
            result['GreenManagerConfig'] = self.green_manager_config.to_map()
        if self.waf_config is not None:
            result['WafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssLogConfig') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigsOssLogConfig()
            self.oss_log_config = temp_model.from_map(m['OssLogConfig'])
        if m.get('GreenManagerConfig') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigsGreenManagerConfig()
            self.green_manager_config = temp_model.from_map(m['GreenManagerConfig'])
        if m.get('WafConfig') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigsWafConfig()
            self.waf_config = temp_model.from_map(m['WafConfig'])
        return self


class DescribeUserConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        configs: DescribeUserConfigsResponseBodyConfigs = None,
    ):
        self.request_id = request_id
        self.configs = configs

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Configs') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigs()
            self.configs = temp_model.from_map(m['Configs'])
        return self


class DescribeUserConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserConfigsResponseBody = None,
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
            temp_model = DescribeUserConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDomainsRequestTag(TeaModel):
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


class DescribeUserDomainsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        page_size: int = None,
        page_number: int = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_search_type: str = None,
        cdn_type: str = None,
        check_domain_show: bool = None,
        resource_group_id: str = None,
        change_start_time: str = None,
        change_end_time: str = None,
        func_id: str = None,
        func_filter: str = None,
        coverage: str = None,
        tag: List[DescribeUserDomainsRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.page_size = page_size
        self.page_number = page_number
        self.domain_name = domain_name
        self.domain_status = domain_status
        self.domain_search_type = domain_search_type
        self.cdn_type = cdn_type
        self.check_domain_show = check_domain_show
        self.resource_group_id = resource_group_id
        self.change_start_time = change_start_time
        self.change_end_time = change_end_time
        self.func_id = func_id
        self.func_filter = func_filter
        self.coverage = coverage
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
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
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter
        if self.coverage is not None:
            result['Coverage'] = self.coverage
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
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
        if m.get('FuncFilter') is not None:
            self.func_filter = m.get('FuncFilter')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
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


class DescribeUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource] = None,
    ):
        self.source = source

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        ssl_protocol: str = None,
        sandbox: str = None,
        sources: DescribeUserDomainsResponseBodyDomainsPageDataSources = None,
        gmt_modified: str = None,
        domain_name: str = None,
        gmt_created: str = None,
        description: str = None,
        coverage: str = None,
        resource_group_id: str = None,
        domain_status: str = None,
        cname: str = None,
        cdn_type: str = None,
    ):
        self.ssl_protocol = ssl_protocol
        self.sandbox = sandbox
        self.sources = sources
        self.gmt_modified = gmt_modified
        self.domain_name = domain_name
        self.gmt_created = gmt_created
        self.description = description
        self.coverage = coverage
        self.resource_group_id = resource_group_id
        self.domain_status = domain_status
        self.cname = cname
        self.cdn_type = cdn_type

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        result = dict()
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.description is not None:
            result['Description'] = self.description
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Sources') is not None:
            temp_model = DescribeUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        return self


class DescribeUserDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeUserDomainsResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: DescribeUserDomainsResponseBodyDomains = None,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.domains = domains
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = DescribeUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeUserDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserDomainsResponseBody = None,
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
            temp_model = DescribeUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeUserTagsResponseBodyTags(TeaModel):
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


class DescribeUserTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[DescribeUserTagsResponseBodyTags] = None,
    ):
        self.request_id = request_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeUserTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
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


class DescribeUserUsageDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_size: str = None,
        page_number: str = None,
    ):
        self.owner_id = owner_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: str = None,
        download_url: str = None,
        create_time: str = None,
        task_name: str = None,
        task_config: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig = None,
        task_id: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.download_url = download_url
        self.create_time = create_time
        self.task_name = task_name
        self.task_config = task_config
        self.task_id = task_id

    def validate(self):
        if self.task_config:
            self.task_config.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskConfig') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig()
            self.task_config = temp_model.from_map(m['TaskConfig'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData(TeaModel):
    def __init__(
        self,
        data_item: List[DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem] = None,
    ):
        self.data_item = data_item

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataItem'] = []
        if self.data_item is not None:
            for k in self.data_item:
                result['DataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k in m.get('DataItem'):
                temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem()
                self.data_item.append(temp_model.from_map(k))
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage(TeaModel):
    def __init__(
        self,
        data: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUserUsageDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_data_per_page: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage = None,
    ):
        self.request_id = request_id
        self.usage_data_per_page = usage_data_per_page

    def validate(self):
        if self.usage_data_per_page:
            self.usage_data_per_page.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usage_data_per_page is not None:
            result['UsageDataPerPage'] = self.usage_data_per_page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsageDataPerPage') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage()
            self.usage_data_per_page = temp_model.from_map(m['UsageDataPerPage'])
        return self


class DescribeUserUsageDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserUsageDataExportTaskResponseBody = None,
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
            temp_model = DescribeUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserUsageDetailDataExportTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_size: str = None,
        page_number: str = None,
    ):
        self.owner_id = owner_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: str = None,
        download_url: str = None,
        create_time: str = None,
        task_name: str = None,
        task_config: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig = None,
        task_id: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.download_url = download_url
        self.create_time = create_time
        self.task_name = task_name
        self.task_config = task_config
        self.task_id = task_id

    def validate(self):
        if self.task_config:
            self.task_config.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskConfig') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig()
            self.task_config = temp_model.from_map(m['TaskConfig'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData(TeaModel):
    def __init__(
        self,
        data_item: List[DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem] = None,
    ):
        self.data_item = data_item

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataItem'] = []
        if self.data_item is not None:
            for k in self.data_item:
                result['DataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k in m.get('DataItem'):
                temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem()
                self.data_item.append(temp_model.from_map(k))
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage(TeaModel):
    def __init__(
        self,
        data: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_data_per_page: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage = None,
    ):
        self.request_id = request_id
        self.usage_data_per_page = usage_data_per_page

    def validate(self):
        if self.usage_data_per_page:
            self.usage_data_per_page.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usage_data_per_page is not None:
            result['UsageDataPerPage'] = self.usage_data_per_page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsageDataPerPage') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage()
            self.usage_data_per_page = temp_model.from_map(m['UsageDataPerPage'])
        return self


class DescribeUserUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserUsageDetailDataExportTaskResponseBody = None,
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
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserVipsByDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        available: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.available = available

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.available is not None:
            result['Available'] = self.available
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Available') is not None:
            self.available = m.get('Available')
        return self


class DescribeUserVipsByDomainResponseBodyVips(TeaModel):
    def __init__(
        self,
        vip: List[str] = None,
    ):
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeUserVipsByDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        vips: DescribeUserVipsByDomainResponseBodyVips = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.vips = vips

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Vips') is not None:
            temp_model = DescribeUserVipsByDomainResponseBodyVips()
            self.vips = temp_model.from_map(m['Vips'])
        return self


class DescribeUserVipsByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserVipsByDomainResponseBody = None,
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
            temp_model = DescribeUserVipsByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyContentRequest(TeaModel):
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


class DescribeVerifyContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        content: str = None,
    ):
        self.request_id = request_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeVerifyContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifyContentResponseBody = None,
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
            temp_model = DescribeVerifyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain: str = None,
    ):
        self.owner_id = owner_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableRealtimeLogDeliveryResponseBody(TeaModel):
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


class DisableRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableRealtimeLogDeliveryResponseBody = None,
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
            temp_model = DisableRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain: str = None,
    ):
        self.owner_id = owner_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableRealtimeLogDeliveryResponseBody(TeaModel):
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


class EnableRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableRealtimeLogDeliveryResponseBody = None,
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
            temp_model = EnableRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsByLogConfigIdRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        config_id: str = None,
    ):
        self.owner_id = owner_id
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class ListDomainsByLogConfigIdResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
    ):
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class ListDomainsByLogConfigIdResponseBody(TeaModel):
    def __init__(
        self,
        domains: ListDomainsByLogConfigIdResponseBodyDomains = None,
        request_id: str = None,
    ):
        self.domains = domains
        self.request_id = request_id

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = ListDomainsByLogConfigIdResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDomainsByLogConfigIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDomainsByLogConfigIdResponseBody = None,
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
            temp_model = ListDomainsByLogConfigIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFCTriggerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        event_meta_name: str = None,
        event_meta_version: str = None,
    ):
        self.owner_id = owner_id
        self.event_meta_name = event_meta_name
        self.event_meta_version = event_meta_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        return self


class ListFCTriggerResponseBodyFCTriggers(TeaModel):
    def __init__(
        self,
        trigger_arn: str = None,
        role_arn: str = None,
        source_arn: str = None,
        notes: str = None,
        event_meta_name: str = None,
        event_meta_version: str = None,
    ):
        self.trigger_arn = trigger_arn
        self.role_arn = role_arn
        self.source_arn = source_arn
        self.notes = notes
        self.event_meta_name = event_meta_name
        self.event_meta_version = event_meta_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        return self


class ListFCTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        fctriggers: List[ListFCTriggerResponseBodyFCTriggers] = None,
    ):
        self.request_id = request_id
        self.fctriggers = fctriggers

    def validate(self):
        if self.fctriggers:
            for k in self.fctriggers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FCTriggers'] = []
        if self.fctriggers is not None:
            for k in self.fctriggers:
                result['FCTriggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.fctriggers = []
        if m.get('FCTriggers') is not None:
            for k in m.get('FCTriggers'):
                temp_model = ListFCTriggerResponseBodyFCTriggers()
                self.fctriggers.append(temp_model.from_map(k))
        return self


class ListFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFCTriggerResponseBody = None,
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
            temp_model = ListFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRealtimeLogDeliveryDomainsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        project: str = None,
        logstore: str = None,
        region: str = None,
    ):
        self.owner_id = owner_id
        self.project = project
        self.logstore = logstore
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListRealtimeLogDeliveryDomainsResponseBodyContentDomains(TeaModel):
    def __init__(
        self,
        status: str = None,
        domain_name: str = None,
    ):
        self.status = status
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class ListRealtimeLogDeliveryDomainsResponseBodyContent(TeaModel):
    def __init__(
        self,
        domains: List[ListRealtimeLogDeliveryDomainsResponseBodyContentDomains] = None,
    ):
        self.domains = domains

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListRealtimeLogDeliveryDomainsResponseBodyContentDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class ListRealtimeLogDeliveryDomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        content: ListRealtimeLogDeliveryDomainsResponseBodyContent = None,
    ):
        self.request_id = request_id
        self.content = content

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            temp_model = ListRealtimeLogDeliveryDomainsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        return self


class ListRealtimeLogDeliveryDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRealtimeLogDeliveryDomainsResponseBody = None,
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
            temp_model = ListRealtimeLogDeliveryDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRealtimeLogDeliveryInfosRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos(TeaModel):
    def __init__(
        self,
        region: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.region = region
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class ListRealtimeLogDeliveryInfosResponseBodyContent(TeaModel):
    def __init__(
        self,
        realtime_log_delivery_infos: List[ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos] = None,
    ):
        self.realtime_log_delivery_infos = realtime_log_delivery_infos

    def validate(self):
        if self.realtime_log_delivery_infos:
            for k in self.realtime_log_delivery_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RealtimeLogDeliveryInfos'] = []
        if self.realtime_log_delivery_infos is not None:
            for k in self.realtime_log_delivery_infos:
                result['RealtimeLogDeliveryInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.realtime_log_delivery_infos = []
        if m.get('RealtimeLogDeliveryInfos') is not None:
            for k in m.get('RealtimeLogDeliveryInfos'):
                temp_model = ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos()
                self.realtime_log_delivery_infos.append(temp_model.from_map(k))
        return self


class ListRealtimeLogDeliveryInfosResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        content: ListRealtimeLogDeliveryInfosResponseBodyContent = None,
    ):
        self.request_id = request_id
        self.content = content

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            temp_model = ListRealtimeLogDeliveryInfosResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        return self


class ListRealtimeLogDeliveryInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRealtimeLogDeliveryInfosResponseBody = None,
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
            temp_model = ListRealtimeLogDeliveryInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserCustomLogConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ListUserCustomLogConfigResponseBodyConfigIds(TeaModel):
    def __init__(
        self,
        config_id: List[str] = None,
    ):
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class ListUserCustomLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_ids: ListUserCustomLogConfigResponseBodyConfigIds = None,
    ):
        self.request_id = request_id
        self.config_ids = config_ids

    def validate(self):
        if self.config_ids:
            self.config_ids.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_ids is not None:
            result['ConfigIds'] = self.config_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigIds') is not None:
            temp_model = ListUserCustomLogConfigResponseBodyConfigIds()
            self.config_ids = temp_model.from_map(m['ConfigIds'])
        return self


class ListUserCustomLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserCustomLogConfigResponseBody = None,
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
            temp_model = ListUserCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCdnDomainRequest(TeaModel):
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


class ModifyCdnDomainResponseBody(TeaModel):
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


class ModifyCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCdnDomainResponseBody = None,
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
            temp_model = ModifyCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCdnDomainSchdmByPropertyRequest(TeaModel):
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


class ModifyCdnDomainSchdmByPropertyResponseBody(TeaModel):
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


class ModifyCdnDomainSchdmByPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCdnDomainSchdmByPropertyResponseBody = None,
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
            temp_model = ModifyCdnDomainSchdmByPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCdnServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        internet_charge_type: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.internet_charge_type = internet_charge_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        return self


class ModifyCdnServiceResponseBody(TeaModel):
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


class ModifyCdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCdnServiceResponseBody = None,
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
            temp_model = ModifyCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainCustomLogConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        config_id: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class ModifyDomainCustomLogConfigResponseBody(TeaModel):
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


class ModifyDomainCustomLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDomainCustomLogConfigResponseBody = None,
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
            temp_model = ModifyDomainCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRealtimeLogDeliveryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        project: str = None,
        logstore: str = None,
        region: str = None,
        domain: str = None,
    ):
        self.owner_id = owner_id
        self.project = project
        self.logstore = logstore
        self.region = region
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.region is not None:
            result['Region'] = self.region
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class ModifyRealtimeLogDeliveryResponseBody(TeaModel):
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


class ModifyRealtimeLogDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRealtimeLogDeliveryResponseBody = None,
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
            temp_model = ModifyRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserCustomLogConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        config_id: str = None,
        tag: str = None,
    ):
        self.owner_id = owner_id
        self.config_id = config_id
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ModifyUserCustomLogConfigResponseBody(TeaModel):
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


class ModifyUserCustomLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUserCustomLogConfigResponseBody = None,
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
            temp_model = ModifyUserCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCdnServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        internet_charge_type: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.internet_charge_type = internet_charge_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        return self


class OpenCdnServiceResponseBody(TeaModel):
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


class OpenCdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenCdnServiceResponseBody = None,
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
            temp_model = OpenCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishStagingConfigToProductionRequest(TeaModel):
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


class PublishStagingConfigToProductionResponseBody(TeaModel):
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


class PublishStagingConfigToProductionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishStagingConfigToProductionResponseBody = None,
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
            temp_model = PublishStagingConfigToProductionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushObjectCacheRequest(TeaModel):
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


class PushObjectCacheResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        push_task_id: str = None,
    ):
        self.request_id = request_id
        self.push_task_id = push_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.push_task_id is not None:
            result['PushTaskId'] = self.push_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PushTaskId') is not None:
            self.push_task_id = m.get('PushTaskId')
        return self


class PushObjectCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushObjectCacheResponseBody = None,
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
            temp_model = PushObjectCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshObjectCachesRequest(TeaModel):
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


class RefreshObjectCachesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        refresh_task_id: str = None,
    ):
        self.request_id = request_id
        self.refresh_task_id = refresh_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refresh_task_id is not None:
            result['RefreshTaskId'] = self.refresh_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefreshTaskId') is not None:
            self.refresh_task_id = m.get('RefreshTaskId')
        return self


class RefreshObjectCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshObjectCachesResponseBody = None,
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
            temp_model = RefreshObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackStagingConfigRequest(TeaModel):
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


class RollbackStagingConfigResponseBody(TeaModel):
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


class RollbackStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackStagingConfigResponseBody = None,
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
            temp_model = RollbackStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCcConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        allow_ips: str = None,
        block_ips: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.allow_ips = allow_ips
        self.block_ips = block_ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.allow_ips is not None:
            result['AllowIps'] = self.allow_ips
        if self.block_ips is not None:
            result['BlockIps'] = self.block_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AllowIps') is not None:
            self.allow_ips = m.get('AllowIps')
        if m.get('BlockIps') is not None:
            self.block_ips = m.get('BlockIps')
        return self


class SetCcConfigResponseBody(TeaModel):
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


class SetCcConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetCcConfigResponseBody = None,
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
            temp_model = SetCcConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainCSRCertificateRequest(TeaModel):
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


class SetCdnDomainCSRCertificateResponseBody(TeaModel):
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


class SetCdnDomainCSRCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetCdnDomainCSRCertificateResponseBody = None,
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
            temp_model = SetCdnDomainCSRCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainStagingConfigRequest(TeaModel):
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


class SetCdnDomainStagingConfigResponseBody(TeaModel):
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


class SetCdnDomainStagingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetCdnDomainStagingConfigResponseBody = None,
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
            temp_model = SetCdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetConfigOfVersionRequest(TeaModel):
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
        function_matches: str = None,
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.version_id = version_id
        self.config_id = config_id
        self.function_id = function_id
        self.function_name = function_name
        self.function_args = function_args
        self.function_matches = function_matches

    def validate(self):
        pass

    def to_map(self):
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
        if self.function_matches is not None:
            result['FunctionMatches'] = self.function_matches
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
        if m.get('FunctionMatches') is not None:
            self.function_matches = m.get('FunctionMatches')
        return self


class SetConfigOfVersionResponseBody(TeaModel):
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


class SetConfigOfVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetConfigOfVersionResponseBody = None,
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
            temp_model = SetConfigOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainGreenManagerConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        enable: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class SetDomainGreenManagerConfigResponseBody(TeaModel):
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


class SetDomainGreenManagerConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDomainGreenManagerConfigResponseBody = None,
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
            temp_model = SetDomainGreenManagerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainServerCertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        cert_name: str = None,
        cert_type: str = None,
        server_certificate_status: str = None,
        server_certificate: str = None,
        private_key: str = None,
        force_set: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.cert_name = cert_name
        self.cert_type = cert_type
        self.server_certificate_status = server_certificate_status
        self.server_certificate = server_certificate
        self.private_key = private_key
        self.force_set = force_set

    def validate(self):
        pass

    def to_map(self):
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
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
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
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
        return self


class SetDomainServerCertificateResponseBody(TeaModel):
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


class SetDomainServerCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDomainServerCertificateResponseBody = None,
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
            temp_model = SetDomainServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetErrorPageConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        page_type: str = None,
        custom_page_url: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.page_type = page_type
        self.custom_page_url = custom_page_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.page_type is not None:
            result['PageType'] = self.page_type
        if self.custom_page_url is not None:
            result['CustomPageUrl'] = self.custom_page_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PageType') is not None:
            self.page_type = m.get('PageType')
        if m.get('CustomPageUrl') is not None:
            self.custom_page_url = m.get('CustomPageUrl')
        return self


class SetErrorPageConfigResponseBody(TeaModel):
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


class SetErrorPageConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetErrorPageConfigResponseBody = None,
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
            temp_model = SetErrorPageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFileCacheExpiredConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        cache_content: str = None,
        ttl: str = None,
        weight: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.cache_content = cache_content
        self.ttl = ttl
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cache_content is not None:
            result['CacheContent'] = self.cache_content
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CacheContent') is not None:
            self.cache_content = m.get('CacheContent')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SetFileCacheExpiredConfigResponseBody(TeaModel):
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


class SetFileCacheExpiredConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetFileCacheExpiredConfigResponseBody = None,
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
            temp_model = SetFileCacheExpiredConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetForceRedirectConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        redirect_type: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.redirect_type = redirect_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.redirect_type is not None:
            result['RedirectType'] = self.redirect_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RedirectType') is not None:
            self.redirect_type = m.get('RedirectType')
        return self


class SetForceRedirectConfigResponseBody(TeaModel):
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


class SetForceRedirectConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetForceRedirectConfigResponseBody = None,
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
            temp_model = SetForceRedirectConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetForwardSchemeConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        config_id: int = None,
        enable: str = None,
        scheme_origin: str = None,
        scheme_origin_port: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.config_id = config_id
        self.enable = enable
        self.scheme_origin = scheme_origin
        self.scheme_origin_port = scheme_origin_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.scheme_origin is not None:
            result['SchemeOrigin'] = self.scheme_origin
        if self.scheme_origin_port is not None:
            result['SchemeOriginPort'] = self.scheme_origin_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('SchemeOrigin') is not None:
            self.scheme_origin = m.get('SchemeOrigin')
        if m.get('SchemeOriginPort') is not None:
            self.scheme_origin_port = m.get('SchemeOriginPort')
        return self


class SetForwardSchemeConfigResponseBody(TeaModel):
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


class SetForwardSchemeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetForwardSchemeConfigResponseBody = None,
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
            temp_model = SetForwardSchemeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetHttpErrorPageConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        error_code: str = None,
        page_url: str = None,
        config_id: int = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.error_code = error_code
        self.page_url = page_url
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.page_url is not None:
            result['PageUrl'] = self.page_url
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('PageUrl') is not None:
            self.page_url = m.get('PageUrl')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class SetHttpErrorPageConfigResponseBody(TeaModel):
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


class SetHttpErrorPageConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetHttpErrorPageConfigResponseBody = None,
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
            temp_model = SetHttpErrorPageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetHttpHeaderConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        header_key: str = None,
        header_value: str = None,
        config_id: int = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.header_key = header_key
        self.header_value = header_value
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key
        if self.header_value is not None:
            result['HeaderValue'] = self.header_value
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
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')
        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class SetHttpHeaderConfigResponseBody(TeaModel):
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


class SetHttpHeaderConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetHttpHeaderConfigResponseBody = None,
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
            temp_model = SetHttpHeaderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetHttpsOptionConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        config_id: int = None,
        http_2: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.config_id = config_id
        self.http_2 = http_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.http_2 is not None:
            result['Http2'] = self.http_2
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Http2') is not None:
            self.http_2 = m.get('Http2')
        return self


class SetHttpsOptionConfigResponseBody(TeaModel):
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


class SetHttpsOptionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetHttpsOptionConfigResponseBody = None,
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
            temp_model = SetHttpsOptionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIgnoreQueryStringConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        config_id: int = None,
        enable: str = None,
        hash_key_args: str = None,
        keep_oss_args: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.config_id = config_id
        self.enable = enable
        self.hash_key_args = hash_key_args
        self.keep_oss_args = keep_oss_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.hash_key_args is not None:
            result['HashKeyArgs'] = self.hash_key_args
        if self.keep_oss_args is not None:
            result['KeepOssArgs'] = self.keep_oss_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('HashKeyArgs') is not None:
            self.hash_key_args = m.get('HashKeyArgs')
        if m.get('KeepOssArgs') is not None:
            self.keep_oss_args = m.get('KeepOssArgs')
        return self


class SetIgnoreQueryStringConfigResponseBody(TeaModel):
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


class SetIgnoreQueryStringConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetIgnoreQueryStringConfigResponseBody = None,
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
            temp_model = SetIgnoreQueryStringConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIpAllowListConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        allow_ips: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.allow_ips = allow_ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.allow_ips is not None:
            result['AllowIps'] = self.allow_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AllowIps') is not None:
            self.allow_ips = m.get('AllowIps')
        return self


class SetIpAllowListConfigResponseBody(TeaModel):
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


class SetIpAllowListConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetIpAllowListConfigResponseBody = None,
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
            temp_model = SetIpAllowListConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIpBlackListConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        block_ips: str = None,
        config_id: int = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.block_ips = block_ips
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.block_ips is not None:
            result['BlockIps'] = self.block_ips
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('BlockIps') is not None:
            self.block_ips = m.get('BlockIps')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class SetIpBlackListConfigResponseBody(TeaModel):
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


class SetIpBlackListConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetIpBlackListConfigResponseBody = None,
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
            temp_model = SetIpBlackListConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetOptimizeConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        config_id: int = None,
        enable: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.config_id = config_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class SetOptimizeConfigResponseBody(TeaModel):
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


class SetOptimizeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetOptimizeConfigResponseBody = None,
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
            temp_model = SetOptimizeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPageCompressConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        config_id: int = None,
        enable: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.config_id = config_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class SetPageCompressConfigResponseBody(TeaModel):
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


class SetPageCompressConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetPageCompressConfigResponseBody = None,
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
            temp_model = SetPageCompressConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRangeConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        enable: str = None,
        config_id: int = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.enable = enable
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class SetRangeConfigResponseBody(TeaModel):
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


class SetRangeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetRangeConfigResponseBody = None,
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
            temp_model = SetRangeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRefererConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        refer_type: str = None,
        refer_list: str = None,
        allow_empty: str = None,
        disable_ast: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.refer_type = refer_type
        self.refer_list = refer_list
        self.allow_empty = allow_empty
        self.disable_ast = disable_ast

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.refer_type is not None:
            result['ReferType'] = self.refer_type
        if self.refer_list is not None:
            result['ReferList'] = self.refer_list
        if self.allow_empty is not None:
            result['AllowEmpty'] = self.allow_empty
        if self.disable_ast is not None:
            result['DisableAst'] = self.disable_ast
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ReferType') is not None:
            self.refer_type = m.get('ReferType')
        if m.get('ReferList') is not None:
            self.refer_list = m.get('ReferList')
        if m.get('AllowEmpty') is not None:
            self.allow_empty = m.get('AllowEmpty')
        if m.get('DisableAst') is not None:
            self.disable_ast = m.get('DisableAst')
        return self


class SetRefererConfigResponseBody(TeaModel):
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


class SetRefererConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetRefererConfigResponseBody = None,
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
            temp_model = SetRefererConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRemoveQueryStringConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        config_id: int = None,
        ali_remove_args: str = None,
        keep_oss_args: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.config_id = config_id
        self.ali_remove_args = ali_remove_args
        self.keep_oss_args = keep_oss_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.ali_remove_args is not None:
            result['AliRemoveArgs'] = self.ali_remove_args
        if self.keep_oss_args is not None:
            result['KeepOssArgs'] = self.keep_oss_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('AliRemoveArgs') is not None:
            self.ali_remove_args = m.get('AliRemoveArgs')
        if m.get('KeepOssArgs') is not None:
            self.keep_oss_args = m.get('KeepOssArgs')
        return self


class SetRemoveQueryStringConfigResponseBody(TeaModel):
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


class SetRemoveQueryStringConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetRemoveQueryStringConfigResponseBody = None,
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
            temp_model = SetRemoveQueryStringConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetReqAuthConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        auth_type: str = None,
        key_1: str = None,
        key_2: str = None,
        time_out: str = None,
        auth_remote_desc: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.auth_type = auth_type
        self.key_1 = key_1
        self.key_2 = key_2
        self.time_out = time_out
        self.auth_remote_desc = auth_remote_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.key_1 is not None:
            result['Key1'] = self.key_1
        if self.key_2 is not None:
            result['Key2'] = self.key_2
        if self.time_out is not None:
            result['TimeOut'] = self.time_out
        if self.auth_remote_desc is not None:
            result['AuthRemoteDesc'] = self.auth_remote_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Key1') is not None:
            self.key_1 = m.get('Key1')
        if m.get('Key2') is not None:
            self.key_2 = m.get('Key2')
        if m.get('TimeOut') is not None:
            self.time_out = m.get('TimeOut')
        if m.get('AuthRemoteDesc') is not None:
            self.auth_remote_desc = m.get('AuthRemoteDesc')
        return self


class SetReqAuthConfigResponseBody(TeaModel):
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


class SetReqAuthConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetReqAuthConfigResponseBody = None,
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
            temp_model = SetReqAuthConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetReqHeaderConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        key: str = None,
        value: str = None,
        config_id: int = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.key = key
        self.value = value
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
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
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class SetReqHeaderConfigResponseBody(TeaModel):
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


class SetReqHeaderConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetReqHeaderConfigResponseBody = None,
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
            temp_model = SetReqHeaderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSourceHostConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        enable: str = None,
        back_src_domain: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.enable = enable
        self.back_src_domain = back_src_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.back_src_domain is not None:
            result['BackSrcDomain'] = self.back_src_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('BackSrcDomain') is not None:
            self.back_src_domain = m.get('BackSrcDomain')
        return self


class SetSourceHostConfigResponseBody(TeaModel):
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


class SetSourceHostConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetSourceHostConfigResponseBody = None,
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
            temp_model = SetSourceHostConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetWaitingRoomConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        wait_uri: str = None,
        allow_pct: int = None,
        max_time_wait: int = None,
        gap_time: int = None,
        wait_url: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.wait_uri = wait_uri
        self.allow_pct = allow_pct
        self.max_time_wait = max_time_wait
        self.gap_time = gap_time
        self.wait_url = wait_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.wait_uri is not None:
            result['WaitUri'] = self.wait_uri
        if self.allow_pct is not None:
            result['AllowPct'] = self.allow_pct
        if self.max_time_wait is not None:
            result['MaxTimeWait'] = self.max_time_wait
        if self.gap_time is not None:
            result['GapTime'] = self.gap_time
        if self.wait_url is not None:
            result['WaitUrl'] = self.wait_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('WaitUri') is not None:
            self.wait_uri = m.get('WaitUri')
        if m.get('AllowPct') is not None:
            self.allow_pct = m.get('AllowPct')
        if m.get('MaxTimeWait') is not None:
            self.max_time_wait = m.get('MaxTimeWait')
        if m.get('GapTime') is not None:
            self.gap_time = m.get('GapTime')
        if m.get('WaitUrl') is not None:
            self.wait_url = m.get('WaitUrl')
        return self


class SetWaitingRoomConfigResponseBody(TeaModel):
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


class SetWaitingRoomConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetWaitingRoomConfigResponseBody = None,
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
            temp_model = SetWaitingRoomConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCdnDomainRequest(TeaModel):
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


class StartCdnDomainResponseBody(TeaModel):
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


class StartCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartCdnDomainResponseBody = None,
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
            temp_model = StartCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCdnDomainRequest(TeaModel):
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


class StopCdnDomainResponseBody(TeaModel):
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


class StopCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopCdnDomainResponseBody = None,
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
            temp_model = StopCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
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
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
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


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFCTriggerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        trigger_arn: str = None,
        source_arn: str = None,
        function_arn: str = None,
        role_arn: str = None,
        notes: str = None,
    ):
        self.owner_id = owner_id
        self.trigger_arn = trigger_arn
        self.source_arn = source_arn
        self.function_arn = function_arn
        self.role_arn = role_arn
        self.notes = notes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        if self.source_arn is not None:
            result['SourceARN'] = self.source_arn
        if self.function_arn is not None:
            result['FunctionARN'] = self.function_arn
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.notes is not None:
            result['Notes'] = self.notes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        if m.get('SourceARN') is not None:
            self.source_arn = m.get('SourceARN')
        if m.get('FunctionARN') is not None:
            self.function_arn = m.get('FunctionARN')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        return self


class UpdateFCTriggerResponseBody(TeaModel):
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


class UpdateFCTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFCTriggerResponseBody = None,
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
            temp_model = UpdateFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDomainOwnerRequest(TeaModel):
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


class VerifyDomainOwnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        content: str = None,
    ):
        self.request_id = request_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class VerifyDomainOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyDomainOwnerResponseBody = None,
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
            temp_model = VerifyDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


