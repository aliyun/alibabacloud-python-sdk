# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddScdnDomainRequest(TeaModel):
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
    ):
        self.owner_id = owner_id
        self.owner_account = owner_account
        self.security_token = security_token
        self.domain_name = domain_name
        self.resource_group_id = resource_group_id
        self.sources = sources
        self.check_url = check_url
        self.scope = scope

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.scope is not None:
            result['Scope'] = self.scope
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
        return self


class AddScdnDomainResponseBody(TeaModel):
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


class AddScdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddScdnDomainResponseBody = None,
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
            temp_model = AddScdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteScdnDomainConfigsRequest(TeaModel):
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


class BatchDeleteScdnDomainConfigsResponseBody(TeaModel):
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


class BatchDeleteScdnDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDeleteScdnDomainConfigsResponseBody = None,
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
            temp_model = BatchDeleteScdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetScdnDomainConfigsRequest(TeaModel):
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


class BatchSetScdnDomainConfigsResponseBody(TeaModel):
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


class BatchSetScdnDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSetScdnDomainConfigsResponseBody = None,
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
            temp_model = BatchSetScdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateScdnDomainRequest(TeaModel):
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


class BatchUpdateScdnDomainResponseBody(TeaModel):
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


class BatchUpdateScdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUpdateScdnDomainResponseBody = None,
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
            temp_model = BatchUpdateScdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckScdnServiceRequest(TeaModel):
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


class CheckScdnServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        in_debt: bool = None,
        enabled: bool = None,
        in_debt_overdue: bool = None,
        on_service: bool = None,
    ):
        self.request_id = request_id
        self.in_debt = in_debt
        self.enabled = enabled
        self.in_debt_overdue = in_debt_overdue
        self.on_service = on_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue
        if self.on_service is not None:
            result['OnService'] = self.on_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')
        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')
        return self


class CheckScdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckScdnServiceResponseBody = None,
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
            temp_model = CheckScdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScdnDomainRequest(TeaModel):
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


class DeleteScdnDomainResponseBody(TeaModel):
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


class DeleteScdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScdnDomainResponseBody = None,
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
            temp_model = DeleteScdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScdnSpecificConfigRequest(TeaModel):
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


class DeleteScdnSpecificConfigResponseBody(TeaModel):
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


class DeleteScdnSpecificConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScdnSpecificConfigResponseBody = None,
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
            temp_model = DeleteScdnSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnCcQpsInfoRequest(TeaModel):
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


class DescribeScdnCcQpsInfoResponseBodyTimeScopesTimeScope(TeaModel):
    def __init__(
        self,
        start: str = None,
        interval: str = None,
    ):
        self.start = start
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeScdnCcQpsInfoResponseBodyTimeScopes(TeaModel):
    def __init__(
        self,
        time_scope: List[DescribeScdnCcQpsInfoResponseBodyTimeScopesTimeScope] = None,
    ):
        self.time_scope = time_scope

    def validate(self):
        if self.time_scope:
            for k in self.time_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TimeScope'] = []
        if self.time_scope is not None:
            for k in self.time_scope:
                result['TimeScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_scope = []
        if m.get('TimeScope') is not None:
            for k in m.get('TimeScope'):
                temp_model = DescribeScdnCcQpsInfoResponseBodyTimeScopesTimeScope()
                self.time_scope.append(temp_model.from_map(k))
        return self


class DescribeScdnCcQpsInfoResponseBodyTotals(TeaModel):
    def __init__(
        self,
        total: List[str] = None,
    ):
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeScdnCcQpsInfoResponseBodyAttacks(TeaModel):
    def __init__(
        self,
        attack: List[str] = None,
    ):
        self.attack = attack

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attack is not None:
            result['Attack'] = self.attack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attack') is not None:
            self.attack = m.get('Attack')
        return self


class DescribeScdnCcQpsInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_scopes: DescribeScdnCcQpsInfoResponseBodyTimeScopes = None,
        totals: DescribeScdnCcQpsInfoResponseBodyTotals = None,
        attacks: DescribeScdnCcQpsInfoResponseBodyAttacks = None,
    ):
        self.request_id = request_id
        self.time_scopes = time_scopes
        self.totals = totals
        self.attacks = attacks

    def validate(self):
        if self.time_scopes:
            self.time_scopes.validate()
        if self.totals:
            self.totals.validate()
        if self.attacks:
            self.attacks.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_scopes is not None:
            result['TimeScopes'] = self.time_scopes.to_map()
        if self.totals is not None:
            result['Totals'] = self.totals.to_map()
        if self.attacks is not None:
            result['Attacks'] = self.attacks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeScopes') is not None:
            temp_model = DescribeScdnCcQpsInfoResponseBodyTimeScopes()
            self.time_scopes = temp_model.from_map(m['TimeScopes'])
        if m.get('Totals') is not None:
            temp_model = DescribeScdnCcQpsInfoResponseBodyTotals()
            self.totals = temp_model.from_map(m['Totals'])
        if m.get('Attacks') is not None:
            temp_model = DescribeScdnCcQpsInfoResponseBodyAttacks()
            self.attacks = temp_model.from_map(m['Attacks'])
        return self


class DescribeScdnCcQpsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnCcQpsInfoResponseBody = None,
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
            temp_model = DescribeScdnCcQpsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnCcTopIpRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        page_size: str = None,
        page_number: str = None,
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


class DescribeScdnCcTopIpResponseBodyAttackIpDataListAttackIpDatas(TeaModel):
    def __init__(
        self,
        ip: str = None,
        attack_count: str = None,
    ):
        self.ip = ip
        self.attack_count = attack_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.attack_count is not None:
            result['AttackCount'] = self.attack_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('AttackCount') is not None:
            self.attack_count = m.get('AttackCount')
        return self


class DescribeScdnCcTopIpResponseBodyAttackIpDataList(TeaModel):
    def __init__(
        self,
        attack_ip_datas: List[DescribeScdnCcTopIpResponseBodyAttackIpDataListAttackIpDatas] = None,
    ):
        self.attack_ip_datas = attack_ip_datas

    def validate(self):
        if self.attack_ip_datas:
            for k in self.attack_ip_datas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AttackIpDatas'] = []
        if self.attack_ip_datas is not None:
            for k in self.attack_ip_datas:
                result['AttackIpDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_ip_datas = []
        if m.get('AttackIpDatas') is not None:
            for k in m.get('AttackIpDatas'):
                temp_model = DescribeScdnCcTopIpResponseBodyAttackIpDataListAttackIpDatas()
                self.attack_ip_datas.append(temp_model.from_map(k))
        return self


class DescribeScdnCcTopIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        total: str = None,
        attack_ip_data_list: DescribeScdnCcTopIpResponseBodyAttackIpDataList = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.total = total
        self.attack_ip_data_list = attack_ip_data_list

    def validate(self):
        if self.attack_ip_data_list:
            self.attack_ip_data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.total is not None:
            result['Total'] = self.total
        if self.attack_ip_data_list is not None:
            result['AttackIpDataList'] = self.attack_ip_data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('AttackIpDataList') is not None:
            temp_model = DescribeScdnCcTopIpResponseBodyAttackIpDataList()
            self.attack_ip_data_list = temp_model.from_map(m['AttackIpDataList'])
        return self


class DescribeScdnCcTopIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnCcTopIpResponseBody = None,
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
            temp_model = DescribeScdnCcTopIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnCcTopUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        page_size: str = None,
        page_number: str = None,
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


class DescribeScdnCcTopUrlResponseBodyAttackUrlDataListAttackUrlDatas(TeaModel):
    def __init__(
        self,
        url: str = None,
        attack_count: str = None,
    ):
        self.url = url
        self.attack_count = attack_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.attack_count is not None:
            result['AttackCount'] = self.attack_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('AttackCount') is not None:
            self.attack_count = m.get('AttackCount')
        return self


class DescribeScdnCcTopUrlResponseBodyAttackUrlDataList(TeaModel):
    def __init__(
        self,
        attack_url_datas: List[DescribeScdnCcTopUrlResponseBodyAttackUrlDataListAttackUrlDatas] = None,
    ):
        self.attack_url_datas = attack_url_datas

    def validate(self):
        if self.attack_url_datas:
            for k in self.attack_url_datas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AttackUrlDatas'] = []
        if self.attack_url_datas is not None:
            for k in self.attack_url_datas:
                result['AttackUrlDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_url_datas = []
        if m.get('AttackUrlDatas') is not None:
            for k in m.get('AttackUrlDatas'):
                temp_model = DescribeScdnCcTopUrlResponseBodyAttackUrlDataListAttackUrlDatas()
                self.attack_url_datas.append(temp_model.from_map(k))
        return self


class DescribeScdnCcTopUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        total: str = None,
        attack_url_data_list: DescribeScdnCcTopUrlResponseBodyAttackUrlDataList = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.total = total
        self.attack_url_data_list = attack_url_data_list

    def validate(self):
        if self.attack_url_data_list:
            self.attack_url_data_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.total is not None:
            result['Total'] = self.total
        if self.attack_url_data_list is not None:
            result['AttackUrlDataList'] = self.attack_url_data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('AttackUrlDataList') is not None:
            temp_model = DescribeScdnCcTopUrlResponseBodyAttackUrlDataList()
            self.attack_url_data_list = temp_model.from_map(m['AttackUrlDataList'])
        return self


class DescribeScdnCcTopUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnCcTopUrlResponseBody = None,
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
            temp_model = DescribeScdnCcTopUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnCertificateDetailRequest(TeaModel):
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


class DescribeScdnCertificateDetailResponseBody(TeaModel):
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


class DescribeScdnCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnCertificateDetailResponseBody = None,
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
            temp_model = DescribeScdnCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnCertificateListRequest(TeaModel):
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


class DescribeScdnCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
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


class DescribeScdnCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(
        self,
        cert: List[DescribeScdnCertificateListResponseBodyCertificateListModelCertListCert] = None,
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
                temp_model = DescribeScdnCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeScdnCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(
        self,
        cert_list: DescribeScdnCertificateListResponseBodyCertificateListModelCertList = None,
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
            temp_model = DescribeScdnCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeScdnCertificateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        certificate_list_model: DescribeScdnCertificateListResponseBodyCertificateListModel = None,
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
            temp_model = DescribeScdnCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        return self


class DescribeScdnCertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnCertificateListResponseBody = None,
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
            temp_model = DescribeScdnCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDDoSInfoRequest(TeaModel):
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


class DescribeScdnDDoSInfoResponseBody(TeaModel):
    def __init__(
        self,
        sec_bandwidth: int = None,
        request_id: str = None,
        elastic_bandwidth: int = None,
    ):
        self.sec_bandwidth = sec_bandwidth
        self.request_id = request_id
        self.elastic_bandwidth = elastic_bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sec_bandwidth is not None:
            result['SecBandwidth'] = self.sec_bandwidth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecBandwidth') is not None:
            self.sec_bandwidth = m.get('SecBandwidth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        return self


class DescribeScdnDDoSInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDDoSInfoResponseBody = None,
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
            temp_model = DescribeScdnDDoSInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDDoSTrafficInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        line: str = None,
    ):
        self.owner_id = owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.line = line

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
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class DescribeScdnDDoSTrafficInfoResponseBodyTimeScopesTimeScope(TeaModel):
    def __init__(
        self,
        start: str = None,
        interval: str = None,
    ):
        self.start = start
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeScdnDDoSTrafficInfoResponseBodyTimeScopes(TeaModel):
    def __init__(
        self,
        time_scope: List[DescribeScdnDDoSTrafficInfoResponseBodyTimeScopesTimeScope] = None,
    ):
        self.time_scope = time_scope

    def validate(self):
        if self.time_scope:
            for k in self.time_scope:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TimeScope'] = []
        if self.time_scope is not None:
            for k in self.time_scope:
                result['TimeScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_scope = []
        if m.get('TimeScope') is not None:
            for k in m.get('TimeScope'):
                temp_model = DescribeScdnDDoSTrafficInfoResponseBodyTimeScopesTimeScope()
                self.time_scope.append(temp_model.from_map(k))
        return self


class DescribeScdnDDoSTrafficInfoResponseBodyBpsDrops(TeaModel):
    def __init__(
        self,
        bps_drop: List[str] = None,
    ):
        self.bps_drop = bps_drop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bps_drop is not None:
            result['BpsDrop'] = self.bps_drop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDrop') is not None:
            self.bps_drop = m.get('BpsDrop')
        return self


class DescribeScdnDDoSTrafficInfoResponseBodyPpsDrops(TeaModel):
    def __init__(
        self,
        pps_drop: List[str] = None,
    ):
        self.pps_drop = pps_drop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pps_drop is not None:
            result['PpsDrop'] = self.pps_drop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PpsDrop') is not None:
            self.pps_drop = m.get('PpsDrop')
        return self


class DescribeScdnDDoSTrafficInfoResponseBodyBpsTotals(TeaModel):
    def __init__(
        self,
        bps_total: List[str] = None,
    ):
        self.bps_total = bps_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bps_total is not None:
            result['BpsTotal'] = self.bps_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsTotal') is not None:
            self.bps_total = m.get('BpsTotal')
        return self


class DescribeScdnDDoSTrafficInfoResponseBodyPpsTotals(TeaModel):
    def __init__(
        self,
        pps_total: List[str] = None,
    ):
        self.pps_total = pps_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pps_total is not None:
            result['PpsTotal'] = self.pps_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PpsTotal') is not None:
            self.pps_total = m.get('PpsTotal')
        return self


class DescribeScdnDDoSTrafficInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_scopes: DescribeScdnDDoSTrafficInfoResponseBodyTimeScopes = None,
        bps_drops: DescribeScdnDDoSTrafficInfoResponseBodyBpsDrops = None,
        pps_drops: DescribeScdnDDoSTrafficInfoResponseBodyPpsDrops = None,
        bps_totals: DescribeScdnDDoSTrafficInfoResponseBodyBpsTotals = None,
        pps_totals: DescribeScdnDDoSTrafficInfoResponseBodyPpsTotals = None,
    ):
        self.request_id = request_id
        self.time_scopes = time_scopes
        self.bps_drops = bps_drops
        self.pps_drops = pps_drops
        self.bps_totals = bps_totals
        self.pps_totals = pps_totals

    def validate(self):
        if self.time_scopes:
            self.time_scopes.validate()
        if self.bps_drops:
            self.bps_drops.validate()
        if self.pps_drops:
            self.pps_drops.validate()
        if self.bps_totals:
            self.bps_totals.validate()
        if self.pps_totals:
            self.pps_totals.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_scopes is not None:
            result['TimeScopes'] = self.time_scopes.to_map()
        if self.bps_drops is not None:
            result['BpsDrops'] = self.bps_drops.to_map()
        if self.pps_drops is not None:
            result['PpsDrops'] = self.pps_drops.to_map()
        if self.bps_totals is not None:
            result['BpsTotals'] = self.bps_totals.to_map()
        if self.pps_totals is not None:
            result['PpsTotals'] = self.pps_totals.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeScopes') is not None:
            temp_model = DescribeScdnDDoSTrafficInfoResponseBodyTimeScopes()
            self.time_scopes = temp_model.from_map(m['TimeScopes'])
        if m.get('BpsDrops') is not None:
            temp_model = DescribeScdnDDoSTrafficInfoResponseBodyBpsDrops()
            self.bps_drops = temp_model.from_map(m['BpsDrops'])
        if m.get('PpsDrops') is not None:
            temp_model = DescribeScdnDDoSTrafficInfoResponseBodyPpsDrops()
            self.pps_drops = temp_model.from_map(m['PpsDrops'])
        if m.get('BpsTotals') is not None:
            temp_model = DescribeScdnDDoSTrafficInfoResponseBodyBpsTotals()
            self.bps_totals = temp_model.from_map(m['BpsTotals'])
        if m.get('PpsTotals') is not None:
            temp_model = DescribeScdnDDoSTrafficInfoResponseBodyPpsTotals()
            self.pps_totals = temp_model.from_map(m['PpsTotals'])
        return self


class DescribeScdnDDoSTrafficInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDDoSTrafficInfoResponseBody = None,
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
            temp_model = DescribeScdnDDoSTrafficInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainBpsDataRequest(TeaModel):
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


class DescribeScdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        https_bps_value: str = None,
        bps_value: str = None,
        time_stamp: str = None,
        http_bps_value: str = None,
    ):
        self.https_bps_value = https_bps_value
        self.bps_value = bps_value
        self.time_stamp = time_stamp
        self.http_bps_value = http_bps_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.https_bps_value is not None:
            result['HttpsBpsValue'] = self.https_bps_value
        if self.bps_value is not None:
            result['BpsValue'] = self.bps_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.http_bps_value is not None:
            result['HttpBpsValue'] = self.http_bps_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsBpsValue') is not None:
            self.https_bps_value = m.get('HttpsBpsValue')
        if m.get('BpsValue') is not None:
            self.bps_value = m.get('BpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('HttpBpsValue') is not None:
            self.http_bps_value = m.get('HttpBpsValue')
        return self


class DescribeScdnDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        bps_data_per_interval: DescribeScdnDomainBpsDataResponseBodyBpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.bps_data_per_interval = bps_data_per_interval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

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
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
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
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeScdnDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        return self


class DescribeScdnDomainBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainBpsDataResponseBody = None,
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
            temp_model = DescribeScdnDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainCertificateInfoRequest(TeaModel):
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


class DescribeScdnDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
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


class DescribeScdnDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeScdnDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
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
                temp_model = DescribeScdnDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainCertificateInfoResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeScdnDomainCertificateInfoResponseBodyCertInfos = None,
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
            temp_model = DescribeScdnDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScdnDomainCertificateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainCertificateInfoResponseBody = None,
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
            temp_model = DescribeScdnDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainCnameRequest(TeaModel):
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


class DescribeScdnDomainCnameResponseBodyCnameDatasData(TeaModel):
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


class DescribeScdnDomainCnameResponseBodyCnameDatas(TeaModel):
    def __init__(
        self,
        data: List[DescribeScdnDomainCnameResponseBodyCnameDatasData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeScdnDomainCnameResponseBodyCnameDatasData()
                self.data.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainCnameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cname_datas: DescribeScdnDomainCnameResponseBodyCnameDatas = None,
    ):
        self.request_id = request_id
        self.cname_datas = cname_datas

    def validate(self):
        if self.cname_datas:
            self.cname_datas.validate()

    def to_map(self):
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
            temp_model = DescribeScdnDomainCnameResponseBodyCnameDatas()
            self.cname_datas = temp_model.from_map(m['CnameDatas'])
        return self


class DescribeScdnDomainCnameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainCnameResponseBody = None,
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
            temp_model = DescribeScdnDomainCnameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainConfigsRequest(TeaModel):
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


class DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
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


class DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(
        self,
        function_arg: List[DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg] = None,
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
                temp_model = DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(
        self,
        status: str = None,
        config_id: str = None,
        function_name: str = None,
        function_args: DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs = None,
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
            temp_model = DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        return self


class DescribeScdnDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        domain_config: List[DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfig] = None,
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
                temp_model = DescribeScdnDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_configs: DescribeScdnDomainConfigsResponseBodyDomainConfigs = None,
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
            temp_model = DescribeScdnDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        return self


class DescribeScdnDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainConfigsResponseBody = None,
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
            temp_model = DescribeScdnDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainDetailRequest(TeaModel):
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


class DescribeScdnDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(
        self,
        type: str = None,
        enabled: str = None,
        priority: str = None,
        port: int = None,
        content: str = None,
    ):
        self.type = type
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
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeScdnDomainDetailResponseBodyDomainDetailSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeScdnDomainDetailResponseBodyDomainDetailSourcesSource] = None,
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
                temp_model = DescribeScdnDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainDetailResponseBodyDomainDetail(TeaModel):
    def __init__(
        self,
        sslpub: str = None,
        sources: DescribeScdnDomainDetailResponseBodyDomainDetailSources = None,
        gmt_modified: str = None,
        domain_name: str = None,
        gmt_created: str = None,
        description: str = None,
        sslprotocol: str = None,
        resource_group_id: str = None,
        cert_name: str = None,
        scope: str = None,
        cname: str = None,
        domain_status: str = None,
    ):
        self.sslpub = sslpub
        self.sources = sources
        self.gmt_modified = gmt_modified
        self.domain_name = domain_name
        self.gmt_created = gmt_created
        self.description = description
        self.sslprotocol = sslprotocol
        self.resource_group_id = resource_group_id
        self.cert_name = cert_name
        self.scope = scope
        self.cname = cname
        self.domain_status = domain_status

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        result = dict()
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Sources') is not None:
            temp_model = DescribeScdnDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
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
        return self


class DescribeScdnDomainDetailResponseBody(TeaModel):
    def __init__(
        self,
        domain_detail: DescribeScdnDomainDetailResponseBodyDomainDetail = None,
        request_id: str = None,
    ):
        self.domain_detail = domain_detail
        self.request_id = request_id

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        result = dict()
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainDetail') is not None:
            temp_model = DescribeScdnDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m['DomainDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScdnDomainDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainDetailResponseBody = None,
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
            temp_model = DescribeScdnDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainHitRateDataRequest(TeaModel):
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


class DescribeScdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule(TeaModel):
    def __init__(
        self,
        byte_hit_rate: str = None,
        req_hit_rate: str = None,
        time_stamp: str = None,
    ):
        self.byte_hit_rate = byte_hit_rate
        self.req_hit_rate = req_hit_rate
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeScdnDomainHitRateDataResponseBodyHitRatePerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainHitRateDataResponseBodyHitRatePerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        hit_rate_per_interval: DescribeScdnDomainHitRateDataResponseBodyHitRatePerInterval = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.hit_rate_per_interval = hit_rate_per_interval
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.hit_rate_per_interval:
            self.hit_rate_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.hit_rate_per_interval is not None:
            result['HitRatePerInterval'] = self.hit_rate_per_interval.to_map()
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
        if m.get('HitRatePerInterval') is not None:
            temp_model = DescribeScdnDomainHitRateDataResponseBodyHitRatePerInterval()
            self.hit_rate_per_interval = temp_model.from_map(m['HitRatePerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeScdnDomainHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainHitRateDataResponseBody = None,
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
            temp_model = DescribeScdnDomainHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainHttpCodeDataRequest(TeaModel):
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


class DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule(TeaModel):
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


class DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval(TeaModel):
    def __init__(
        self,
        http_code_data_module: List[DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule] = None,
    ):
        self.http_code_data_module = http_code_data_module

    def validate(self):
        if self.http_code_data_module:
            for k in self.http_code_data_module:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerIntervalHttpCodeDataModule()
                self.http_code_data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        http_code_data_per_interval: DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval = None,
    ):
        self.time_stamp = time_stamp
        self.http_code_data_per_interval = http_code_data_per_interval

    def validate(self):
        if self.http_code_data_per_interval:
            self.http_code_data_per_interval.validate()

    def to_map(self):
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
            temp_model = DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModuleHttpCodeDataPerInterval()
            self.http_code_data_per_interval = temp_model.from_map(m['HttpCodeDataPerInterval'])
        return self


class DescribeScdnDomainHttpCodeDataResponseBodyDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainHttpCodeDataResponseBodyDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        data_per_interval: DescribeScdnDomainHttpCodeDataResponseBodyDataPerInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.data_per_interval = data_per_interval

    def validate(self):
        if self.data_per_interval:
            self.data_per_interval.validate()

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
        if self.data_per_interval is not None:
            result['DataPerInterval'] = self.data_per_interval.to_map()
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
        if m.get('DataPerInterval') is not None:
            temp_model = DescribeScdnDomainHttpCodeDataResponseBodyDataPerInterval()
            self.data_per_interval = temp_model.from_map(m['DataPerInterval'])
        return self


class DescribeScdnDomainHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainHttpCodeDataResponseBody = None,
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
            temp_model = DescribeScdnDomainHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainIspDataRequest(TeaModel):
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


class DescribeScdnDomainIspDataResponseBodyValueISPProportionData(TeaModel):
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


class DescribeScdnDomainIspDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        ispproportion_data: List[DescribeScdnDomainIspDataResponseBodyValueISPProportionData] = None,
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
                temp_model = DescribeScdnDomainIspDataResponseBodyValueISPProportionData()
                self.ispproportion_data.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainIspDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        value: DescribeScdnDomainIspDataResponseBodyValue = None,
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
            temp_model = DescribeScdnDomainIspDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeScdnDomainIspDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainIspDataResponseBody = None,
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
            temp_model = DescribeScdnDomainIspDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainLogRequest(TeaModel):
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


class DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
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


class DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos(TeaModel):
    def __init__(
        self,
        log_info_detail: List[DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail] = None,
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
                temp_model = DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(
        self,
        page_infos: DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos = None,
        log_count: int = None,
        log_infos: DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos = None,
    ):
        self.page_infos = page_infos
        self.log_count = log_count
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
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfos') is not None:
            temp_model = DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m['PageInfos'])
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('LogInfos') is not None:
            temp_model = DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        return self


class DescribeScdnDomainLogResponseBodyDomainLogDetails(TeaModel):
    def __init__(
        self,
        domain_log_detail: List[DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail] = None,
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
                temp_model = DescribeScdnDomainLogResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        domain_log_details: DescribeScdnDomainLogResponseBodyDomainLogDetails = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.domain_log_details = domain_log_details

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeScdnDomainLogResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        return self


class DescribeScdnDomainLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainLogResponseBody = None,
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
            temp_model = DescribeScdnDomainLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainOriginBpsDataRequest(TeaModel):
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


class DescribeScdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        http_origin_bps_value: str = None,
        time_stamp: str = None,
        https_origin_bps_value: str = None,
        origin_bps_value: str = None,
    ):
        self.http_origin_bps_value = http_origin_bps_value
        self.time_stamp = time_stamp
        self.https_origin_bps_value = https_origin_bps_value
        self.origin_bps_value = origin_bps_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.http_origin_bps_value is not None:
            result['HttpOriginBpsValue'] = self.http_origin_bps_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.https_origin_bps_value is not None:
            result['HttpsOriginBpsValue'] = self.https_origin_bps_value
        if self.origin_bps_value is not None:
            result['OriginBpsValue'] = self.origin_bps_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpOriginBpsValue') is not None:
            self.http_origin_bps_value = m.get('HttpOriginBpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('HttpsOriginBpsValue') is not None:
            self.https_origin_bps_value = m.get('HttpsOriginBpsValue')
        if m.get('OriginBpsValue') is not None:
            self.origin_bps_value = m.get('OriginBpsValue')
        return self


class DescribeScdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainOriginBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        origin_bps_data_per_interval: DescribeScdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.origin_bps_data_per_interval = origin_bps_data_per_interval

    def validate(self):
        if self.origin_bps_data_per_interval:
            self.origin_bps_data_per_interval.validate()

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
        if self.origin_bps_data_per_interval is not None:
            result['OriginBpsDataPerInterval'] = self.origin_bps_data_per_interval.to_map()
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
        if m.get('OriginBpsDataPerInterval') is not None:
            temp_model = DescribeScdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval()
            self.origin_bps_data_per_interval = temp_model.from_map(m['OriginBpsDataPerInterval'])
        return self


class DescribeScdnDomainOriginBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainOriginBpsDataResponseBody = None,
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
            temp_model = DescribeScdnDomainOriginBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainOriginTrafficDataRequest(TeaModel):
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


class DescribeScdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        traffic_value: str = None,
        http_traffic_value: str = None,
        https_traffic_value: str = None,
        time_stamp: str = None,
    ):
        self.traffic_value = traffic_value
        self.http_traffic_value = http_traffic_value
        self.https_traffic_value = https_traffic_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        if self.http_traffic_value is not None:
            result['HttpTrafficValue'] = self.http_traffic_value
        if self.https_traffic_value is not None:
            result['HttpsTrafficValue'] = self.https_traffic_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        if m.get('HttpTrafficValue') is not None:
            self.http_traffic_value = m.get('HttpTrafficValue')
        if m.get('HttpsTrafficValue') is not None:
            self.https_traffic_value = m.get('HttpsTrafficValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeScdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainOriginTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        origin_traffic_data_per_interval: DescribeScdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval
        self.origin_traffic_data_per_interval = origin_traffic_data_per_interval

    def validate(self):
        if self.origin_traffic_data_per_interval:
            self.origin_traffic_data_per_interval.validate()

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
        if self.origin_traffic_data_per_interval is not None:
            result['OriginTrafficDataPerInterval'] = self.origin_traffic_data_per_interval.to_map()
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
        if m.get('OriginTrafficDataPerInterval') is not None:
            temp_model = DescribeScdnDomainOriginTrafficDataResponseBodyOriginTrafficDataPerInterval()
            self.origin_traffic_data_per_interval = temp_model.from_map(m['OriginTrafficDataPerInterval'])
        return self


class DescribeScdnDomainOriginTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainOriginTrafficDataResponseBody = None,
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
            temp_model = DescribeScdnDomainOriginTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainPvDataRequest(TeaModel):
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


class DescribeScdnDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
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


class DescribeScdnDomainPvDataResponseBodyPvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeScdnDomainPvDataResponseBodyPvDataIntervalUsageData] = None,
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
                temp_model = DescribeScdnDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainPvDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        pv_data_interval: DescribeScdnDomainPvDataResponseBodyPvDataInterval = None,
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
            temp_model = DescribeScdnDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        return self


class DescribeScdnDomainPvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainPvDataResponseBody = None,
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
            temp_model = DescribeScdnDomainPvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainQpsDataRequest(TeaModel):
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


class DescribeScdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        https_acc_value: str = None,
        qps_value: str = None,
        acc_value: str = None,
        http_qps_value: str = None,
        time_stamp: str = None,
        https_qps_value: str = None,
        http_acc_value: str = None,
    ):
        self.https_acc_value = https_acc_value
        self.qps_value = qps_value
        self.acc_value = acc_value
        self.http_qps_value = http_qps_value
        self.time_stamp = time_stamp
        self.https_qps_value = https_qps_value
        self.http_acc_value = http_acc_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.https_acc_value is not None:
            result['HttpsAccValue'] = self.https_acc_value
        if self.qps_value is not None:
            result['QpsValue'] = self.qps_value
        if self.acc_value is not None:
            result['AccValue'] = self.acc_value
        if self.http_qps_value is not None:
            result['HttpQpsValue'] = self.http_qps_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.https_qps_value is not None:
            result['HttpsQpsValue'] = self.https_qps_value
        if self.http_acc_value is not None:
            result['HttpAccValue'] = self.http_acc_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsAccValue') is not None:
            self.https_acc_value = m.get('HttpsAccValue')
        if m.get('QpsValue') is not None:
            self.qps_value = m.get('QpsValue')
        if m.get('AccValue') is not None:
            self.acc_value = m.get('AccValue')
        if m.get('HttpQpsValue') is not None:
            self.http_qps_value = m.get('HttpQpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('HttpsQpsValue') is not None:
            self.https_qps_value = m.get('HttpsQpsValue')
        if m.get('HttpAccValue') is not None:
            self.http_acc_value = m.get('HttpAccValue')
        return self


class DescribeScdnDomainQpsDataResponseBodyQpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        qps_data_per_interval: DescribeScdnDomainQpsDataResponseBodyQpsDataPerInterval = None,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
    ):
        self.qps_data_per_interval = qps_data_per_interval
        self.end_time = end_time
        self.request_id = request_id
        self.domain_name = domain_name
        self.start_time = start_time
        self.data_interval = data_interval

    def validate(self):
        if self.qps_data_per_interval:
            self.qps_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.qps_data_per_interval is not None:
            result['QpsDataPerInterval'] = self.qps_data_per_interval.to_map()
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
        if m.get('QpsDataPerInterval') is not None:
            temp_model = DescribeScdnDomainQpsDataResponseBodyQpsDataPerInterval()
            self.qps_data_per_interval = temp_model.from_map(m['QpsDataPerInterval'])
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


class DescribeScdnDomainQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainQpsDataResponseBody = None,
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
            temp_model = DescribeScdnDomainQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRealTimeBpsDataRequest(TeaModel):
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


class DescribeScdnDomainRealTimeBpsDataResponseBodyDataBpsModel(TeaModel):
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


class DescribeScdnDomainRealTimeBpsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        bps_model: List[DescribeScdnDomainRealTimeBpsDataResponseBodyDataBpsModel] = None,
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
                temp_model = DescribeScdnDomainRealTimeBpsDataResponseBodyDataBpsModel()
                self.bps_model.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeScdnDomainRealTimeBpsDataResponseBodyData = None,
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
            temp_model = DescribeScdnDomainRealTimeBpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeScdnDomainRealTimeBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRealTimeBpsDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRealTimeBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRealTimeByteHitRateDataRequest(TeaModel):
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


class DescribeScdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel(TeaModel):
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


class DescribeScdnDomainRealTimeByteHitRateDataResponseBodyData(TeaModel):
    def __init__(
        self,
        byte_hit_rate_data_model: List[DescribeScdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel] = None,
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
                temp_model = DescribeScdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel()
                self.byte_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeByteHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeScdnDomainRealTimeByteHitRateDataResponseBodyData = None,
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
            temp_model = DescribeScdnDomainRealTimeByteHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeScdnDomainRealTimeByteHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRealTimeByteHitRateDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRealTimeByteHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRealTimeHttpCodeDataRequest(TeaModel):
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


class DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(TeaModel):
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


class DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue(TeaModel):
    def __init__(
        self,
        real_time_code_proportion_data: List[DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData] = None,
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
                temp_model = DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData()
                self.real_time_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData(TeaModel):
    def __init__(
        self,
        value: DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue = None,
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
            temp_model = DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData] = None,
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
                temp_model = DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeHttpCodeDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        real_time_http_code_data: DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData = None,
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
            temp_model = DescribeScdnDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(m['RealTimeHttpCodeData'])
        return self


class DescribeScdnDomainRealTimeHttpCodeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRealTimeHttpCodeDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRealTimeHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRealTimeQpsDataRequest(TeaModel):
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


class DescribeScdnDomainRealTimeQpsDataResponseBodyDataQpsModel(TeaModel):
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


class DescribeScdnDomainRealTimeQpsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        qps_model: List[DescribeScdnDomainRealTimeQpsDataResponseBodyDataQpsModel] = None,
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
                temp_model = DescribeScdnDomainRealTimeQpsDataResponseBodyDataQpsModel()
                self.qps_model.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeScdnDomainRealTimeQpsDataResponseBodyData = None,
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
            temp_model = DescribeScdnDomainRealTimeQpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeScdnDomainRealTimeQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRealTimeQpsDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRealTimeQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRealTimeReqHitRateDataRequest(TeaModel):
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


class DescribeScdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel(TeaModel):
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


class DescribeScdnDomainRealTimeReqHitRateDataResponseBodyData(TeaModel):
    def __init__(
        self,
        req_hit_rate_data_model: List[DescribeScdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel] = None,
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
                temp_model = DescribeScdnDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel()
                self.req_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeReqHitRateDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeScdnDomainRealTimeReqHitRateDataResponseBodyData = None,
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
            temp_model = DescribeScdnDomainRealTimeReqHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeScdnDomainRealTimeReqHitRateDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRealTimeReqHitRateDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRealTimeReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRealTimeSrcBpsDataRequest(TeaModel):
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


class DescribeScdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule(TeaModel):
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


class DescribeScdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeSrcBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        real_time_src_bps_data_per_interval: DescribeScdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval = None,
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
            temp_model = DescribeScdnDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval()
            self.real_time_src_bps_data_per_interval = temp_model.from_map(m['RealTimeSrcBpsDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeScdnDomainRealTimeSrcBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRealTimeSrcBpsDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRealTimeSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRealTimeSrcTrafficDataRequest(TeaModel):
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


class DescribeScdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule(TeaModel):
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


class DescribeScdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeSrcTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        real_time_src_traffic_data_per_interval: DescribeScdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval = None,
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
            temp_model = DescribeScdnDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval()
            self.real_time_src_traffic_data_per_interval = temp_model.from_map(m['RealTimeSrcTrafficDataPerInterval'])
        return self


class DescribeScdnDomainRealTimeSrcTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRealTimeSrcTrafficDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRealTimeSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRealTimeTrafficDataRequest(TeaModel):
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


class DescribeScdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule(TeaModel):
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


class DescribeScdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRealTimeTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        real_time_traffic_data_per_interval: DescribeScdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval = None,
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
            temp_model = DescribeScdnDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval()
            self.real_time_traffic_data_per_interval = temp_model.from_map(m['RealTimeTrafficDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeScdnDomainRealTimeTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRealTimeTrafficDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRealTimeTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainRegionDataRequest(TeaModel):
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


class DescribeScdnDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
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


class DescribeScdnDomainRegionDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        region_proportion_data: List[DescribeScdnDomainRegionDataResponseBodyValueRegionProportionData] = None,
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
                temp_model = DescribeScdnDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainRegionDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        data_interval: str = None,
        value: DescribeScdnDomainRegionDataResponseBodyValue = None,
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
            temp_model = DescribeScdnDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeScdnDomainRegionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainRegionDataResponseBody = None,
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
            temp_model = DescribeScdnDomainRegionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainTopReferVisitRequest(TeaModel):
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


class DescribeScdnDomainTopReferVisitResponseBodyTopReferListReferList(TeaModel):
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


class DescribeScdnDomainTopReferVisitResponseBodyTopReferList(TeaModel):
    def __init__(
        self,
        refer_list: List[DescribeScdnDomainTopReferVisitResponseBodyTopReferListReferList] = None,
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
                temp_model = DescribeScdnDomainTopReferVisitResponseBodyTopReferListReferList()
                self.refer_list.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainTopReferVisitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        top_refer_list: DescribeScdnDomainTopReferVisitResponseBodyTopReferList = None,
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
            temp_model = DescribeScdnDomainTopReferVisitResponseBodyTopReferList()
            self.top_refer_list = temp_model.from_map(m['TopReferList'])
        return self


class DescribeScdnDomainTopReferVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainTopReferVisitResponseBody = None,
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
            temp_model = DescribeScdnDomainTopReferVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainTopUrlVisitRequest(TeaModel):
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


class DescribeScdnDomainTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
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


class DescribeScdnDomainTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeScdnDomainTopUrlVisitResponseBodyUrl500ListUrlList] = None,
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
                temp_model = DescribeScdnDomainTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
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


class DescribeScdnDomainTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeScdnDomainTopUrlVisitResponseBodyUrl200ListUrlList] = None,
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
                temp_model = DescribeScdnDomainTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
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


class DescribeScdnDomainTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeScdnDomainTopUrlVisitResponseBodyUrl400ListUrlList] = None,
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
                temp_model = DescribeScdnDomainTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
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


class DescribeScdnDomainTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeScdnDomainTopUrlVisitResponseBodyUrl300ListUrlList] = None,
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
                temp_model = DescribeScdnDomainTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
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


class DescribeScdnDomainTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(
        self,
        url_list: List[DescribeScdnDomainTopUrlVisitResponseBodyAllUrlListUrlList] = None,
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
                temp_model = DescribeScdnDomainTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainTopUrlVisitResponseBody(TeaModel):
    def __init__(
        self,
        url_500list: DescribeScdnDomainTopUrlVisitResponseBodyUrl500List = None,
        url_200list: DescribeScdnDomainTopUrlVisitResponseBodyUrl200List = None,
        url_400list: DescribeScdnDomainTopUrlVisitResponseBodyUrl400List = None,
        request_id: str = None,
        domain_name: str = None,
        start_time: str = None,
        url_300list: DescribeScdnDomainTopUrlVisitResponseBodyUrl300List = None,
        all_url_list: DescribeScdnDomainTopUrlVisitResponseBodyAllUrlList = None,
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
            temp_model = DescribeScdnDomainTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        if m.get('Url200List') is not None:
            temp_model = DescribeScdnDomainTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeScdnDomainTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url300List') is not None:
            temp_model = DescribeScdnDomainTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('AllUrlList') is not None:
            temp_model = DescribeScdnDomainTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        return self


class DescribeScdnDomainTopUrlVisitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainTopUrlVisitResponseBody = None,
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
            temp_model = DescribeScdnDomainTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainTrafficDataRequest(TeaModel):
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


class DescribeScdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        traffic_value: str = None,
        http_traffic_value: str = None,
        https_traffic_value: str = None,
        time_stamp: str = None,
    ):
        self.traffic_value = traffic_value
        self.http_traffic_value = http_traffic_value
        self.https_traffic_value = https_traffic_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        if self.http_traffic_value is not None:
            result['HttpTrafficValue'] = self.http_traffic_value
        if self.https_traffic_value is not None:
            result['HttpsTrafficValue'] = self.https_traffic_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        if m.get('HttpTrafficValue') is not None:
            self.http_traffic_value = m.get('HttpTrafficValue')
        if m.get('HttpsTrafficValue') is not None:
            self.https_traffic_value = m.get('HttpsTrafficValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeScdnDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeScdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
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
                temp_model = DescribeScdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        domain_name: str = None,
        traffic_data_per_interval: DescribeScdnDomainTrafficDataResponseBodyTrafficDataPerInterval = None,
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
            temp_model = DescribeScdnDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeScdnDomainTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainTrafficDataResponseBody = None,
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
            temp_model = DescribeScdnDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnDomainUvDataRequest(TeaModel):
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


class DescribeScdnDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
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


class DescribeScdnDomainUvDataResponseBodyUvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeScdnDomainUvDataResponseBodyUvDataIntervalUsageData] = None,
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
                temp_model = DescribeScdnDomainUvDataResponseBodyUvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeScdnDomainUvDataResponseBody(TeaModel):
    def __init__(
        self,
        uv_data_interval: DescribeScdnDomainUvDataResponseBodyUvDataInterval = None,
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
            temp_model = DescribeScdnDomainUvDataResponseBodyUvDataInterval()
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


class DescribeScdnDomainUvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnDomainUvDataResponseBody = None,
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
            temp_model = DescribeScdnDomainUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnRefreshQuotaRequest(TeaModel):
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


class DescribeScdnRefreshQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url_remain: str = None,
        preload_remain: str = None,
        block_quota: str = None,
        dir_remain: str = None,
        url_quota: str = None,
        dir_quota: str = None,
        block_remain: str = None,
        preload_quota: str = None,
    ):
        self.request_id = request_id
        self.url_remain = url_remain
        self.preload_remain = preload_remain
        self.block_quota = block_quota
        self.dir_remain = dir_remain
        self.url_quota = url_quota
        self.dir_quota = dir_quota
        self.block_remain = block_remain
        self.preload_quota = preload_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain
        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota
        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota
        if self.block_remain is not None:
            result['blockRemain'] = self.block_remain
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')
        if m.get('blockRemain') is not None:
            self.block_remain = m.get('blockRemain')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        return self


class DescribeScdnRefreshQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnRefreshQuotaResponseBody = None,
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
            temp_model = DescribeScdnRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnRefreshTasksRequest(TeaModel):
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


class DescribeScdnRefreshTasksResponseBodyTasksTask(TeaModel):
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


class DescribeScdnRefreshTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        task: List[DescribeScdnRefreshTasksResponseBodyTasksTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeScdnRefreshTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeScdnRefreshTasksResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        tasks: DescribeScdnRefreshTasksResponseBodyTasks = None,
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
            temp_model = DescribeScdnRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeScdnRefreshTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnRefreshTasksResponseBody = None,
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
            temp_model = DescribeScdnRefreshTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnServiceRequest(TeaModel):
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


class DescribeScdnServiceResponseBodyOperationLocksLockReason(TeaModel):
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


class DescribeScdnServiceResponseBodyOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: List[DescribeScdnServiceResponseBodyOperationLocksLockReason] = None,
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
                temp_model = DescribeScdnServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        return self


class DescribeScdnServiceResponseBody(TeaModel):
    def __init__(
        self,
        current_ddo_sbasic_value: str = None,
        current_elastic_protection_value: str = None,
        end_time: str = None,
        pricing_cycle: str = None,
        elastic_protection: str = None,
        domain_count_value: str = None,
        current_domain_count: str = None,
        ddo_sbasic: str = None,
        cc_protection_value: str = None,
        elastic_protection_value: str = None,
        open_time: str = None,
        changing_charge_type: str = None,
        bandwidth: str = None,
        domain_count: str = None,
        current_bandwidth: str = None,
        request_id: str = None,
        current_elastic_protection: str = None,
        instance_id: str = None,
        current_cc_protection_value: str = None,
        current_ddo_sbasic: str = None,
        current_protect_type: str = None,
        current_domain_count_value: str = None,
        current_bandwidth_value: str = None,
        protect_type_value: str = None,
        current_protect_type_value: str = None,
        cc_protection: str = None,
        changing_affect_time: str = None,
        operation_locks: DescribeScdnServiceResponseBodyOperationLocks = None,
        internet_charge_type: str = None,
        ddo_sbasic_value: str = None,
        protect_type: str = None,
        current_cc_protection: str = None,
        price_type: str = None,
        bandwidth_value: str = None,
    ):
        self.current_ddo_sbasic_value = current_ddo_sbasic_value
        self.current_elastic_protection_value = current_elastic_protection_value
        self.end_time = end_time
        self.pricing_cycle = pricing_cycle
        self.elastic_protection = elastic_protection
        self.domain_count_value = domain_count_value
        self.current_domain_count = current_domain_count
        self.ddo_sbasic = ddo_sbasic
        self.cc_protection_value = cc_protection_value
        self.elastic_protection_value = elastic_protection_value
        self.open_time = open_time
        self.changing_charge_type = changing_charge_type
        self.bandwidth = bandwidth
        self.domain_count = domain_count
        self.current_bandwidth = current_bandwidth
        self.request_id = request_id
        self.current_elastic_protection = current_elastic_protection
        self.instance_id = instance_id
        self.current_cc_protection_value = current_cc_protection_value
        self.current_ddo_sbasic = current_ddo_sbasic
        self.current_protect_type = current_protect_type
        self.current_domain_count_value = current_domain_count_value
        self.current_bandwidth_value = current_bandwidth_value
        self.protect_type_value = protect_type_value
        self.current_protect_type_value = current_protect_type_value
        self.cc_protection = cc_protection
        self.changing_affect_time = changing_affect_time
        self.operation_locks = operation_locks
        self.internet_charge_type = internet_charge_type
        self.ddo_sbasic_value = ddo_sbasic_value
        self.protect_type = protect_type
        self.current_cc_protection = current_cc_protection
        self.price_type = price_type
        self.bandwidth_value = bandwidth_value

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        result = dict()
        if self.current_ddo_sbasic_value is not None:
            result['CurrentDDoSBasicValue'] = self.current_ddo_sbasic_value
        if self.current_elastic_protection_value is not None:
            result['CurrentElasticProtectionValue'] = self.current_elastic_protection_value
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.elastic_protection is not None:
            result['ElasticProtection'] = self.elastic_protection
        if self.domain_count_value is not None:
            result['DomainCountValue'] = self.domain_count_value
        if self.current_domain_count is not None:
            result['CurrentDomainCount'] = self.current_domain_count
        if self.ddo_sbasic is not None:
            result['DDoSBasic'] = self.ddo_sbasic
        if self.cc_protection_value is not None:
            result['CcProtectionValue'] = self.cc_protection_value
        if self.elastic_protection_value is not None:
            result['ElasticProtectionValue'] = self.elastic_protection_value
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.current_bandwidth is not None:
            result['CurrentBandwidth'] = self.current_bandwidth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_elastic_protection is not None:
            result['CurrentElasticProtection'] = self.current_elastic_protection
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.current_cc_protection_value is not None:
            result['CurrentCcProtectionValue'] = self.current_cc_protection_value
        if self.current_ddo_sbasic is not None:
            result['CurrentDDoSBasic'] = self.current_ddo_sbasic
        if self.current_protect_type is not None:
            result['CurrentProtectType'] = self.current_protect_type
        if self.current_domain_count_value is not None:
            result['CurrentDomainCountValue'] = self.current_domain_count_value
        if self.current_bandwidth_value is not None:
            result['CurrentBandwidthValue'] = self.current_bandwidth_value
        if self.protect_type_value is not None:
            result['ProtectTypeValue'] = self.protect_type_value
        if self.current_protect_type_value is not None:
            result['CurrentProtectTypeValue'] = self.current_protect_type_value
        if self.cc_protection is not None:
            result['CcProtection'] = self.cc_protection
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ddo_sbasic_value is not None:
            result['DDoSBasicValue'] = self.ddo_sbasic_value
        if self.protect_type is not None:
            result['ProtectType'] = self.protect_type
        if self.current_cc_protection is not None:
            result['CurrentCcProtection'] = self.current_cc_protection
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        if self.bandwidth_value is not None:
            result['BandwidthValue'] = self.bandwidth_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentDDoSBasicValue') is not None:
            self.current_ddo_sbasic_value = m.get('CurrentDDoSBasicValue')
        if m.get('CurrentElasticProtectionValue') is not None:
            self.current_elastic_protection_value = m.get('CurrentElasticProtectionValue')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ElasticProtection') is not None:
            self.elastic_protection = m.get('ElasticProtection')
        if m.get('DomainCountValue') is not None:
            self.domain_count_value = m.get('DomainCountValue')
        if m.get('CurrentDomainCount') is not None:
            self.current_domain_count = m.get('CurrentDomainCount')
        if m.get('DDoSBasic') is not None:
            self.ddo_sbasic = m.get('DDoSBasic')
        if m.get('CcProtectionValue') is not None:
            self.cc_protection_value = m.get('CcProtectionValue')
        if m.get('ElasticProtectionValue') is not None:
            self.elastic_protection_value = m.get('ElasticProtectionValue')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('CurrentBandwidth') is not None:
            self.current_bandwidth = m.get('CurrentBandwidth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentElasticProtection') is not None:
            self.current_elastic_protection = m.get('CurrentElasticProtection')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CurrentCcProtectionValue') is not None:
            self.current_cc_protection_value = m.get('CurrentCcProtectionValue')
        if m.get('CurrentDDoSBasic') is not None:
            self.current_ddo_sbasic = m.get('CurrentDDoSBasic')
        if m.get('CurrentProtectType') is not None:
            self.current_protect_type = m.get('CurrentProtectType')
        if m.get('CurrentDomainCountValue') is not None:
            self.current_domain_count_value = m.get('CurrentDomainCountValue')
        if m.get('CurrentBandwidthValue') is not None:
            self.current_bandwidth_value = m.get('CurrentBandwidthValue')
        if m.get('ProtectTypeValue') is not None:
            self.protect_type_value = m.get('ProtectTypeValue')
        if m.get('CurrentProtectTypeValue') is not None:
            self.current_protect_type_value = m.get('CurrentProtectTypeValue')
        if m.get('CcProtection') is not None:
            self.cc_protection = m.get('CcProtection')
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')
        if m.get('OperationLocks') is not None:
            temp_model = DescribeScdnServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m['OperationLocks'])
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('DDoSBasicValue') is not None:
            self.ddo_sbasic_value = m.get('DDoSBasicValue')
        if m.get('ProtectType') is not None:
            self.protect_type = m.get('ProtectType')
        if m.get('CurrentCcProtection') is not None:
            self.current_cc_protection = m.get('CurrentCcProtection')
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        if m.get('BandwidthValue') is not None:
            self.bandwidth_value = m.get('BandwidthValue')
        return self


class DescribeScdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnServiceResponseBody = None,
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
            temp_model = DescribeScdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnTopDomainsByFlowRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        product: str = None,
        limit: int = None,
    ):
        self.owner_id = owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.product = product
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
        if self.product is not None:
            result['Product'] = self.product
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
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class DescribeScdnTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
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


class DescribeScdnTopDomainsByFlowResponseBodyTopDomains(TeaModel):
    def __init__(
        self,
        top_domain: List[DescribeScdnTopDomainsByFlowResponseBodyTopDomainsTopDomain] = None,
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
                temp_model = DescribeScdnTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        return self


class DescribeScdnTopDomainsByFlowResponseBody(TeaModel):
    def __init__(
        self,
        top_domains: DescribeScdnTopDomainsByFlowResponseBodyTopDomains = None,
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
            temp_model = DescribeScdnTopDomainsByFlowResponseBodyTopDomains()
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


class DescribeScdnTopDomainsByFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnTopDomainsByFlowResponseBody = None,
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
            temp_model = DescribeScdnTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnUserDomainsRequest(TeaModel):
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
        change_start_time: str = None,
        change_end_time: str = None,
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
        self.change_start_time = change_start_time
        self.change_end_time = change_end_time

    def validate(self):
        pass

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
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
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
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        return self


class DescribeScdnUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(
        self,
        type: str = None,
        priority: str = None,
        port: int = None,
        content: str = None,
    ):
        self.type = type
        self.priority = priority
        self.port = port
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
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
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeScdnUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(
        self,
        source: List[DescribeScdnUserDomainsResponseBodyDomainsPageDataSourcesSource] = None,
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
                temp_model = DescribeScdnUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeScdnUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        description: str = None,
        sslprotocol: str = None,
        resource_group_id: str = None,
        sandbox: str = None,
        domain_status: str = None,
        cname: str = None,
        sources: DescribeScdnUserDomainsResponseBodyDomainsPageDataSources = None,
        gmt_modified: str = None,
        domain_name: str = None,
    ):
        self.gmt_created = gmt_created
        self.description = description
        self.sslprotocol = sslprotocol
        self.resource_group_id = resource_group_id
        self.sandbox = sandbox
        self.domain_status = domain_status
        self.cname = cname
        self.sources = sources
        self.gmt_modified = gmt_modified
        self.domain_name = domain_name

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
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
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
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
        if m.get('Sources') is not None:
            temp_model = DescribeScdnUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeScdnUserDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        page_data: List[DescribeScdnUserDomainsResponseBodyDomainsPageData] = None,
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
                temp_model = DescribeScdnUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeScdnUserDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: DescribeScdnUserDomainsResponseBodyDomains = None,
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
            temp_model = DescribeScdnUserDomainsResponseBodyDomains()
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


class DescribeScdnUserDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnUserDomainsResponseBody = None,
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
            temp_model = DescribeScdnUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnUserProtectInfoRequest(TeaModel):
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


class DescribeScdnUserProtectInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_ddo_s: int = None,
    ):
        self.request_id = request_id
        self.service_ddo_s = service_ddo_s

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_ddo_s is not None:
            result['ServiceDDoS'] = self.service_ddo_s
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceDDoS') is not None:
            self.service_ddo_s = m.get('ServiceDDoS')
        return self


class DescribeScdnUserProtectInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnUserProtectInfoResponseBody = None,
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
            temp_model = DescribeScdnUserProtectInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScdnUserQuotaRequest(TeaModel):
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


class DescribeScdnUserQuotaResponseBody(TeaModel):
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


class DescribeScdnUserQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScdnUserQuotaResponseBody = None,
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
            temp_model = DescribeScdnUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenScdnServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        bandwidth: int = None,
        protect_type: str = None,
        ddo_sbasic: int = None,
        elastic_protection: int = None,
        cc_protection: int = None,
        domain_count: int = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.bandwidth = bandwidth
        self.protect_type = protect_type
        self.ddo_sbasic = ddo_sbasic
        self.elastic_protection = elastic_protection
        self.cc_protection = cc_protection
        self.domain_count = domain_count
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.protect_type is not None:
            result['ProtectType'] = self.protect_type
        if self.ddo_sbasic is not None:
            result['DDoSBasic'] = self.ddo_sbasic
        if self.elastic_protection is not None:
            result['ElasticProtection'] = self.elastic_protection
        if self.cc_protection is not None:
            result['CcProtection'] = self.cc_protection
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ProtectType') is not None:
            self.protect_type = m.get('ProtectType')
        if m.get('DDoSBasic') is not None:
            self.ddo_sbasic = m.get('DDoSBasic')
        if m.get('ElasticProtection') is not None:
            self.elastic_protection = m.get('ElasticProtection')
        if m.get('CcProtection') is not None:
            self.cc_protection = m.get('CcProtection')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class OpenScdnServiceResponseBody(TeaModel):
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


class OpenScdnServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenScdnServiceResponseBody = None,
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
            temp_model = OpenScdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreloadScdnObjectCachesRequest(TeaModel):
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


class PreloadScdnObjectCachesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        preload_task_id: str = None,
    ):
        self.request_id = request_id
        self.preload_task_id = preload_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preload_task_id is not None:
            result['PreloadTaskId'] = self.preload_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreloadTaskId') is not None:
            self.preload_task_id = m.get('PreloadTaskId')
        return self


class PreloadScdnObjectCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PreloadScdnObjectCachesResponseBody = None,
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
            temp_model = PreloadScdnObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshScdnObjectCachesRequest(TeaModel):
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


class RefreshScdnObjectCachesResponseBody(TeaModel):
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


class RefreshScdnObjectCachesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshScdnObjectCachesResponseBody = None,
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
            temp_model = RefreshScdnObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetScdnBotInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        domain_name: str = None,
        enable: str = None,
        status: str = None,
    ):
        self.owner_id = owner_id
        self.domain_name = domain_name
        self.enable = enable
        self.status = status

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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetScdnBotInfoResponseBody(TeaModel):
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


class SetScdnBotInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetScdnBotInfoResponseBody = None,
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
            temp_model = SetScdnBotInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetScdnCcInfoRequest(TeaModel):
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


class SetScdnCcInfoResponseBody(TeaModel):
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


class SetScdnCcInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetScdnCcInfoResponseBody = None,
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
            temp_model = SetScdnCcInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetScdnDDoSInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        elastic_bandwidth: int = None,
    ):
        self.owner_id = owner_id
        self.elastic_bandwidth = elastic_bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        return self


class SetScdnDDoSInfoResponseBody(TeaModel):
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


class SetScdnDDoSInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetScdnDDoSInfoResponseBody = None,
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
            temp_model = SetScdnDDoSInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetScdnDomainBizInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        biz_name: str = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.biz_name = biz_name
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class SetScdnDomainBizInfoResponseBody(TeaModel):
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


class SetScdnDomainBizInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetScdnDomainBizInfoResponseBody = None,
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
            temp_model = SetScdnDomainBizInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetScdnDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        cert_type: str = None,
        cert_name: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        sslpri: str = None,
        region: str = None,
        force_set: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.cert_type = cert_type
        self.cert_name = cert_name
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
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
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
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
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


class SetScdnDomainCertificateResponseBody(TeaModel):
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


class SetScdnDomainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetScdnDomainCertificateResponseBody = None,
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
            temp_model = SetScdnDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartScdnDomainRequest(TeaModel):
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


class StartScdnDomainResponseBody(TeaModel):
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


class StartScdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartScdnDomainResponseBody = None,
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
            temp_model = StartScdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopScdnDomainRequest(TeaModel):
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


class StopScdnDomainResponseBody(TeaModel):
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


class StopScdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopScdnDomainResponseBody = None,
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
            temp_model = StopScdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateScdnDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        domain_name: str = None,
        sources: str = None,
        resource_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        self.domain_name = domain_name
        self.sources = sources
        self.resource_group_id = resource_group_id

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
        return self


class UpdateScdnDomainResponseBody(TeaModel):
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


class UpdateScdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateScdnDomainResponseBody = None,
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
            temp_model = UpdateScdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


