# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddIpfilterRequest(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.ip_address = ip_address
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AddIpfilterResponseBody(TeaModel):
    def __init__(
        self,
        ip_filter_id: str = None,
        request_id: str = None,
    ):
        self.ip_filter_id = ip_filter_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_filter_id is not None:
            result['IpFilterId'] = self.ip_filter_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpFilterId') is not None:
            self.ip_filter_id = m.get('IpFilterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddIpfilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddIpfilterResponseBody = None,
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
            temp_model = AddIpfilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSendMailRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        click_trace: str = None,
        owner_id: int = None,
        receivers_name: str = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_name: str = None,
        template_name: str = None,
    ):
        self.account_name = account_name
        self.address_type = address_type
        self.click_trace = click_trace
        self.owner_id = owner_id
        self.receivers_name = receivers_name
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag_name = tag_name
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_address_alias is not None:
            result['ReplyAddressAlias'] = self.reply_address_alias
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyAddressAlias') is not None:
            self.reply_address_alias = m.get('ReplyAddressAlias')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class BatchSendMailResponseBody(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        request_id: str = None,
    ):
        self.env_id = env_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchSendMailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSendMailResponseBody = None,
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
            temp_model = BatchSendMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.domain_id = domain_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_status: str = None,
        request_id: str = None,
    ):
        self.domain_status = domain_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDomainResponseBody = None,
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
            temp_model = CheckDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainDnsRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        type: str = None,
    ):
        self.domain_id = domain_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckDomainDnsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: int = None,
    ):
        self.request_id = request_id
        self.status = status

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckDomainDnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDomainDnsResponseBody = None,
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
            temp_model = CheckDomainDnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        request_id: str = None,
    ):
        self.domain_id = domain_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDomainResponseBody = None,
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
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMailAddressRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        owner_id: int = None,
        reply_address: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sendtype: str = None,
    ):
        self.account_name = account_name
        self.owner_id = owner_id
        self.reply_address = reply_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sendtype = sendtype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')
        return self


class CreateMailAddressResponseBody(TeaModel):
    def __init__(
        self,
        mail_address_id: str = None,
        request_id: str = None,
    ):
        self.mail_address_id = mail_address_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMailAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMailAddressResponseBody = None,
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
            temp_model = CreateMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReceiverRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        owner_id: int = None,
        receivers_alias: str = None,
        receivers_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.desc = desc
        self.owner_id = owner_id
        self.receivers_alias = receivers_alias
        self.receivers_name = receivers_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receivers_alias is not None:
            result['ReceiversAlias'] = self.receivers_alias
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiversAlias') is not None:
            self.receivers_alias = m.get('ReceiversAlias')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateReceiverResponseBody(TeaModel):
    def __init__(
        self,
        receiver_id: str = None,
        request_id: str = None,
    ):
        self.receiver_id = receiver_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateReceiverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateReceiverResponseBody = None,
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
            temp_model = CreateReceiverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_description: str = None,
        tag_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag_description = tag_description
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class CreateTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_id: str = None,
    ):
        self.request_id = request_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class CreateTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTagResponseBody = None,
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
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        from_type: int = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sms_content: str = None,
        sms_type: int = None,
        template_name: str = None,
        template_nick_name: str = None,
        template_subject: str = None,
        template_text: str = None,
        template_type: int = None,
    ):
        self.from_type = from_type
        self.owner_id = owner_id
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sms_content = sms_content
        self.sms_type = sms_type
        self.template_name = template_name
        self.template_nick_name = template_nick_name
        self.template_subject = template_subject
        self.template_text = template_text
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name
        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject
        if self.template_text is not None:
            result['TemplateText'] = self.template_text
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')
        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')
        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: int = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.domain_id = domain_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDomainResponseBody(TeaModel):
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


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainResponseBody = None,
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMailAddressRequest(TeaModel):
    def __init__(
        self,
        mail_address_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.mail_address_id = mail_address_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteMailAddressResponseBody(TeaModel):
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


class DeleteMailAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMailAddressResponseBody = None,
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
            temp_model = DeleteMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReceiverRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        receiver_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.receiver_id = receiver_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteReceiverResponseBody(TeaModel):
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


class DeleteReceiverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteReceiverResponseBody = None,
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
            temp_model = DeleteReceiverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReceiverDetailRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        owner_id: int = None,
        receiver_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.email = email
        self.owner_id = owner_id
        self.receiver_id = receiver_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteReceiverDetailResponseBody(TeaModel):
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


class DeleteReceiverDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteReceiverDetailResponseBody = None,
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
            temp_model = DeleteReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DeleteTagResponseBody(TeaModel):
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


class DeleteTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTagResponseBody = None,
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
            temp_model = DeleteTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        from_type: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
    ):
        self.from_type = from_type
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteTemplateResponseBody(TeaModel):
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


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateResponseBody = None,
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescAccountSummaryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescAccountSummaryResponseBody(TeaModel):
    def __init__(
        self,
        daily_quota: int = None,
        dayu_status: int = None,
        domains: int = None,
        enable_times: int = None,
        mail_addresses: int = None,
        max_quota_level: int = None,
        month_quota: int = None,
        quota_level: int = None,
        receivers: int = None,
        remain_free_quota: int = None,
        request_id: str = None,
        sms_record: int = None,
        sms_sign: int = None,
        sms_templates: int = None,
        tags: int = None,
        templates: int = None,
        user_status: int = None,
    ):
        self.daily_quota = daily_quota
        self.dayu_status = dayu_status
        self.domains = domains
        self.enable_times = enable_times
        self.mail_addresses = mail_addresses
        self.max_quota_level = max_quota_level
        self.month_quota = month_quota
        self.quota_level = quota_level
        self.receivers = receivers
        self.remain_free_quota = remain_free_quota
        self.request_id = request_id
        self.sms_record = sms_record
        self.sms_sign = sms_sign
        self.sms_templates = sms_templates
        self.tags = tags
        self.templates = templates
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_quota is not None:
            result['DailyQuota'] = self.daily_quota
        if self.dayu_status is not None:
            result['DayuStatus'] = self.dayu_status
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.enable_times is not None:
            result['EnableTimes'] = self.enable_times
        if self.mail_addresses is not None:
            result['MailAddresses'] = self.mail_addresses
        if self.max_quota_level is not None:
            result['MaxQuotaLevel'] = self.max_quota_level
        if self.month_quota is not None:
            result['MonthQuota'] = self.month_quota
        if self.quota_level is not None:
            result['QuotaLevel'] = self.quota_level
        if self.receivers is not None:
            result['Receivers'] = self.receivers
        if self.remain_free_quota is not None:
            result['RemainFreeQuota'] = self.remain_free_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sms_record is not None:
            result['SmsRecord'] = self.sms_record
        if self.sms_sign is not None:
            result['SmsSign'] = self.sms_sign
        if self.sms_templates is not None:
            result['SmsTemplates'] = self.sms_templates
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.templates is not None:
            result['Templates'] = self.templates
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyQuota') is not None:
            self.daily_quota = m.get('DailyQuota')
        if m.get('DayuStatus') is not None:
            self.dayu_status = m.get('DayuStatus')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('EnableTimes') is not None:
            self.enable_times = m.get('EnableTimes')
        if m.get('MailAddresses') is not None:
            self.mail_addresses = m.get('MailAddresses')
        if m.get('MaxQuotaLevel') is not None:
            self.max_quota_level = m.get('MaxQuotaLevel')
        if m.get('MonthQuota') is not None:
            self.month_quota = m.get('MonthQuota')
        if m.get('QuotaLevel') is not None:
            self.quota_level = m.get('QuotaLevel')
        if m.get('Receivers') is not None:
            self.receivers = m.get('Receivers')
        if m.get('RemainFreeQuota') is not None:
            self.remain_free_quota = m.get('RemainFreeQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SmsRecord') is not None:
            self.sms_record = m.get('SmsRecord')
        if m.get('SmsSign') is not None:
            self.sms_sign = m.get('SmsSign')
        if m.get('SmsTemplates') is not None:
            self.sms_templates = m.get('SmsTemplates')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class DescAccountSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescAccountSummaryResponseBody = None,
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
            temp_model = DescAccountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        owner_id: int = None,
        require_real_time_dns_records: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.domain_id = domain_id
        self.owner_id = owner_id
        self.require_real_time_dns_records = require_real_time_dns_records
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.require_real_time_dns_records is not None:
            result['RequireRealTimeDnsRecords'] = self.require_real_time_dns_records
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequireRealTimeDnsRecords') is not None:
            self.require_real_time_dns_records = m.get('RequireRealTimeDnsRecords')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescDomainResponseBody(TeaModel):
    def __init__(
        self,
        cname_auth_status: str = None,
        cname_confirm_status: str = None,
        cname_record: str = None,
        create_time: str = None,
        default_domain: str = None,
        dkim_auth_status: str = None,
        dkim_public_key: str = None,
        dkim_rr: str = None,
        dmarc_auth_status: int = None,
        dmarc_host_record: str = None,
        dmarc_record: str = None,
        dns_dmarc: str = None,
        dns_mx: str = None,
        dns_spf: str = None,
        dns_txt: str = None,
        domain_id: str = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_type: str = None,
        host_record: str = None,
        icp_status: str = None,
        mx_auth_status: str = None,
        mx_record: str = None,
        request_id: str = None,
        spf_auth_status: str = None,
        spf_record: str = None,
        spf_record_v2: str = None,
        tl_domain_name: str = None,
        tracef_record: str = None,
    ):
        self.cname_auth_status = cname_auth_status
        self.cname_confirm_status = cname_confirm_status
        self.cname_record = cname_record
        self.create_time = create_time
        self.default_domain = default_domain
        self.dkim_auth_status = dkim_auth_status
        self.dkim_public_key = dkim_public_key
        self.dkim_rr = dkim_rr
        self.dmarc_auth_status = dmarc_auth_status
        self.dmarc_host_record = dmarc_host_record
        self.dmarc_record = dmarc_record
        self.dns_dmarc = dns_dmarc
        self.dns_mx = dns_mx
        self.dns_spf = dns_spf
        self.dns_txt = dns_txt
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.domain_status = domain_status
        self.domain_type = domain_type
        self.host_record = host_record
        self.icp_status = icp_status
        self.mx_auth_status = mx_auth_status
        self.mx_record = mx_record
        self.request_id = request_id
        self.spf_auth_status = spf_auth_status
        self.spf_record = spf_record
        self.spf_record_v2 = spf_record_v2
        self.tl_domain_name = tl_domain_name
        self.tracef_record = tracef_record

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname_auth_status is not None:
            result['CnameAuthStatus'] = self.cname_auth_status
        if self.cname_confirm_status is not None:
            result['CnameConfirmStatus'] = self.cname_confirm_status
        if self.cname_record is not None:
            result['CnameRecord'] = self.cname_record
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.dkim_auth_status is not None:
            result['DkimAuthStatus'] = self.dkim_auth_status
        if self.dkim_public_key is not None:
            result['DkimPublicKey'] = self.dkim_public_key
        if self.dkim_rr is not None:
            result['DkimRR'] = self.dkim_rr
        if self.dmarc_auth_status is not None:
            result['DmarcAuthStatus'] = self.dmarc_auth_status
        if self.dmarc_host_record is not None:
            result['DmarcHostRecord'] = self.dmarc_host_record
        if self.dmarc_record is not None:
            result['DmarcRecord'] = self.dmarc_record
        if self.dns_dmarc is not None:
            result['DnsDmarc'] = self.dns_dmarc
        if self.dns_mx is not None:
            result['DnsMx'] = self.dns_mx
        if self.dns_spf is not None:
            result['DnsSpf'] = self.dns_spf
        if self.dns_txt is not None:
            result['DnsTxt'] = self.dns_txt
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.host_record is not None:
            result['HostRecord'] = self.host_record
        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status
        if self.mx_auth_status is not None:
            result['MxAuthStatus'] = self.mx_auth_status
        if self.mx_record is not None:
            result['MxRecord'] = self.mx_record
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spf_auth_status is not None:
            result['SpfAuthStatus'] = self.spf_auth_status
        if self.spf_record is not None:
            result['SpfRecord'] = self.spf_record
        if self.spf_record_v2 is not None:
            result['SpfRecordV2'] = self.spf_record_v2
        if self.tl_domain_name is not None:
            result['TlDomainName'] = self.tl_domain_name
        if self.tracef_record is not None:
            result['TracefRecord'] = self.tracef_record
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnameAuthStatus') is not None:
            self.cname_auth_status = m.get('CnameAuthStatus')
        if m.get('CnameConfirmStatus') is not None:
            self.cname_confirm_status = m.get('CnameConfirmStatus')
        if m.get('CnameRecord') is not None:
            self.cname_record = m.get('CnameRecord')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('DkimAuthStatus') is not None:
            self.dkim_auth_status = m.get('DkimAuthStatus')
        if m.get('DkimPublicKey') is not None:
            self.dkim_public_key = m.get('DkimPublicKey')
        if m.get('DkimRR') is not None:
            self.dkim_rr = m.get('DkimRR')
        if m.get('DmarcAuthStatus') is not None:
            self.dmarc_auth_status = m.get('DmarcAuthStatus')
        if m.get('DmarcHostRecord') is not None:
            self.dmarc_host_record = m.get('DmarcHostRecord')
        if m.get('DmarcRecord') is not None:
            self.dmarc_record = m.get('DmarcRecord')
        if m.get('DnsDmarc') is not None:
            self.dns_dmarc = m.get('DnsDmarc')
        if m.get('DnsMx') is not None:
            self.dns_mx = m.get('DnsMx')
        if m.get('DnsSpf') is not None:
            self.dns_spf = m.get('DnsSpf')
        if m.get('DnsTxt') is not None:
            self.dns_txt = m.get('DnsTxt')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('HostRecord') is not None:
            self.host_record = m.get('HostRecord')
        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')
        if m.get('MxAuthStatus') is not None:
            self.mx_auth_status = m.get('MxAuthStatus')
        if m.get('MxRecord') is not None:
            self.mx_record = m.get('MxRecord')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpfAuthStatus') is not None:
            self.spf_auth_status = m.get('SpfAuthStatus')
        if m.get('SpfRecord') is not None:
            self.spf_record = m.get('SpfRecord')
        if m.get('SpfRecordV2') is not None:
            self.spf_record_v2 = m.get('SpfRecordV2')
        if m.get('TlDomainName') is not None:
            self.tl_domain_name = m.get('TlDomainName')
        if m.get('TracefRecord') is not None:
            self.tracef_record = m.get('TracefRecord')
        return self


class DescDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescDomainResponseBody = None,
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
            temp_model = DescDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescTemplateRequest(TeaModel):
    def __init__(
        self,
        from_type: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
    ):
        self.from_type = from_type
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescTemplateResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        remark: str = None,
        request_id: str = None,
        sms_content: str = None,
        sms_type: str = None,
        template_name: str = None,
        template_nick_name: str = None,
        template_status: str = None,
        template_subject: str = None,
        template_text: str = None,
        template_type: str = None,
    ):
        self.create_time = create_time
        self.remark = remark
        self.request_id = request_id
        self.sms_content = sms_content
        self.sms_type = sms_type
        self.template_name = template_name
        self.template_nick_name = template_nick_name
        self.template_status = template_status
        self.template_subject = template_subject
        self.template_text = template_text
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject
        if self.template_text is not None:
            result['TemplateText'] = self.template_text
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')
        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class DescTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescTemplateResponseBody = None,
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
            temp_model = DescTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountListRequest(TeaModel):
    def __init__(
        self,
        offset: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        owner_id: int = None,
        page_number: str = None,
        page_size: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        total: str = None,
    ):
        self.offset = offset
        self.offset_create_time = offset_create_time
        self.offset_create_time_desc = offset_create_time_desc
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAccountListResponseBodyDataAccountNotificationInfo(TeaModel):
    def __init__(
        self,
        region: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.region = region
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetAccountListResponseBodyData(TeaModel):
    def __init__(
        self,
        account_notification_info: List[GetAccountListResponseBodyDataAccountNotificationInfo] = None,
    ):
        self.account_notification_info = account_notification_info

    def validate(self):
        if self.account_notification_info:
            for k in self.account_notification_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['accountNotificationInfo'] = []
        if self.account_notification_info is not None:
            for k in self.account_notification_info:
                result['accountNotificationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_notification_info = []
        if m.get('accountNotificationInfo') is not None:
            for k in m.get('accountNotificationInfo'):
                temp_model = GetAccountListResponseBodyDataAccountNotificationInfo()
                self.account_notification_info.append(temp_model.from_map(k))
        return self


class GetAccountListResponseBody(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        data: GetAccountListResponseBodyData = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total = total
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('data') is not None:
            temp_model = GetAccountListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetAccountListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountListResponseBody = None,
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
            temp_model = GetAccountListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMailAddressMsgCallBackUrlRequest(TeaModel):
    def __init__(
        self,
        mail_from: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.mail_from = mail_from
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_from is not None:
            result['MailFrom'] = self.mail_from
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailFrom') is not None:
            self.mail_from = m.get('MailFrom')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetMailAddressMsgCallBackUrlResponseBody(TeaModel):
    def __init__(
        self,
        notify_url: int = None,
        notify_url_status: int = None,
        request_id: str = None,
    ):
        self.notify_url = notify_url
        self.notify_url_status = notify_url_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.notify_url_status is not None:
            result['NotifyUrlStatus'] = self.notify_url_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('NotifyUrlStatus') is not None:
            self.notify_url_status = m.get('NotifyUrlStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMailAddressMsgCallBackUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMailAddressMsgCallBackUrlResponseBody = None,
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
            temp_model = GetMailAddressMsgCallBackUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrackListRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        offset: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        owner_id: int = None,
        page_number: str = None,
        page_size: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        total: str = None,
    ):
        self.end_time = end_time
        self.offset = offset
        self.offset_create_time = offset_create_time
        self.offset_create_time_desc = offset_create_time_desc
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTrackListResponseBodyDataStat(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        rcpt_click_count: int = None,
        rcpt_click_rate: str = None,
        rcpt_open_count: int = None,
        rcpt_open_rate: str = None,
        rcpt_unique_click_count: int = None,
        rcpt_unique_click_rate: str = None,
        rcpt_unique_open_count: int = None,
        rcpt_unique_open_rate: str = None,
        total_number: int = None,
    ):
        self.create_time = create_time
        self.rcpt_click_count = rcpt_click_count
        self.rcpt_click_rate = rcpt_click_rate
        self.rcpt_open_count = rcpt_open_count
        self.rcpt_open_rate = rcpt_open_rate
        self.rcpt_unique_click_count = rcpt_unique_click_count
        self.rcpt_unique_click_rate = rcpt_unique_click_rate
        self.rcpt_unique_open_count = rcpt_unique_open_count
        self.rcpt_unique_open_rate = rcpt_unique_open_rate
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rcpt_click_count is not None:
            result['RcptClickCount'] = self.rcpt_click_count
        if self.rcpt_click_rate is not None:
            result['RcptClickRate'] = self.rcpt_click_rate
        if self.rcpt_open_count is not None:
            result['RcptOpenCount'] = self.rcpt_open_count
        if self.rcpt_open_rate is not None:
            result['RcptOpenRate'] = self.rcpt_open_rate
        if self.rcpt_unique_click_count is not None:
            result['RcptUniqueClickCount'] = self.rcpt_unique_click_count
        if self.rcpt_unique_click_rate is not None:
            result['RcptUniqueClickRate'] = self.rcpt_unique_click_rate
        if self.rcpt_unique_open_count is not None:
            result['RcptUniqueOpenCount'] = self.rcpt_unique_open_count
        if self.rcpt_unique_open_rate is not None:
            result['RcptUniqueOpenRate'] = self.rcpt_unique_open_rate
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RcptClickCount') is not None:
            self.rcpt_click_count = m.get('RcptClickCount')
        if m.get('RcptClickRate') is not None:
            self.rcpt_click_rate = m.get('RcptClickRate')
        if m.get('RcptOpenCount') is not None:
            self.rcpt_open_count = m.get('RcptOpenCount')
        if m.get('RcptOpenRate') is not None:
            self.rcpt_open_rate = m.get('RcptOpenRate')
        if m.get('RcptUniqueClickCount') is not None:
            self.rcpt_unique_click_count = m.get('RcptUniqueClickCount')
        if m.get('RcptUniqueClickRate') is not None:
            self.rcpt_unique_click_rate = m.get('RcptUniqueClickRate')
        if m.get('RcptUniqueOpenCount') is not None:
            self.rcpt_unique_open_count = m.get('RcptUniqueOpenCount')
        if m.get('RcptUniqueOpenRate') is not None:
            self.rcpt_unique_open_rate = m.get('RcptUniqueOpenRate')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class GetTrackListResponseBodyData(TeaModel):
    def __init__(
        self,
        stat: List[GetTrackListResponseBodyDataStat] = None,
    ):
        self.stat = stat

    def validate(self):
        if self.stat:
            for k in self.stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['stat'] = []
        if self.stat is not None:
            for k in self.stat:
                result['stat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stat = []
        if m.get('stat') is not None:
            for k in m.get('stat'):
                temp_model = GetTrackListResponseBodyDataStat()
                self.stat.append(temp_model.from_map(k))
        return self


class GetTrackListResponseBody(TeaModel):
    def __init__(
        self,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        data: GetTrackListResponseBodyData = None,
    ):
        self.offset_create_time = offset_create_time
        self.offset_create_time_desc = offset_create_time_desc
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total = total
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('data') is not None:
            temp_model = GetTrackListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetTrackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrackListResponseBody = None,
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
            temp_model = GetTrackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMailAddressRequest(TeaModel):
    def __init__(
        self,
        mail_address_id: int = None,
        owner_id: int = None,
        password: str = None,
        reply_address: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.mail_address_id = mail_address_id
        self.owner_id = owner_id
        self.password = password
        self.reply_address = reply_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyMailAddressResponseBody(TeaModel):
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


class ModifyMailAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMailAddressResponseBody = None,
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
            temp_model = ModifyMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPWByDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        password: str = None,
        resource_owner_id: str = None,
    ):
        self.domain_name = domain_name
        self.password = password
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyPWByDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyPWByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPWByDomainResponseBody = None,
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
            temp_model = ModifyPWByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTagRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_description: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag_description = tag_description
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ModifyTagResponseBody(TeaModel):
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


class ModifyTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTagResponseBody = None,
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
            temp_model = ModifyTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTemplateRequest(TeaModel):
    def __init__(
        self,
        from_type: int = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sms_content: str = None,
        sms_type: int = None,
        template_id: int = None,
        template_name: str = None,
        template_nick_name: str = None,
        template_subject: str = None,
        template_text: str = None,
    ):
        self.from_type = from_type
        self.owner_id = owner_id
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sms_content = sms_content
        self.sms_type = sms_type
        self.template_id = template_id
        self.template_name = template_name
        self.template_nick_name = template_nick_name
        self.template_subject = template_subject
        self.template_text = template_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name
        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject
        if self.template_text is not None:
            result['TemplateText'] = self.template_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')
        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')
        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')
        return self


class ModifyTemplateResponseBody(TeaModel):
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


class ModifyTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTemplateResponseBody = None,
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
            temp_model = ModifyTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainByParamRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: int = None,
    ):
        self.key_word = key_word
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDomainByParamResponseBodyDataDomain(TeaModel):
    def __init__(
        self,
        cname_auth_status: str = None,
        confirm_status: str = None,
        create_time: str = None,
        domain_id: str = None,
        domain_name: str = None,
        domain_record: str = None,
        domain_status: str = None,
        icp_status: str = None,
        mx_auth_status: str = None,
        spf_auth_status: str = None,
        utc_create_time: int = None,
    ):
        self.cname_auth_status = cname_auth_status
        self.confirm_status = confirm_status
        self.create_time = create_time
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.domain_record = domain_record
        self.domain_status = domain_status
        self.icp_status = icp_status
        self.mx_auth_status = mx_auth_status
        self.spf_auth_status = spf_auth_status
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname_auth_status is not None:
            result['CnameAuthStatus'] = self.cname_auth_status
        if self.confirm_status is not None:
            result['ConfirmStatus'] = self.confirm_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_record is not None:
            result['DomainRecord'] = self.domain_record
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status
        if self.mx_auth_status is not None:
            result['MxAuthStatus'] = self.mx_auth_status
        if self.spf_auth_status is not None:
            result['SpfAuthStatus'] = self.spf_auth_status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnameAuthStatus') is not None:
            self.cname_auth_status = m.get('CnameAuthStatus')
        if m.get('ConfirmStatus') is not None:
            self.confirm_status = m.get('ConfirmStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainRecord') is not None:
            self.domain_record = m.get('DomainRecord')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')
        if m.get('MxAuthStatus') is not None:
            self.mx_auth_status = m.get('MxAuthStatus')
        if m.get('SpfAuthStatus') is not None:
            self.spf_auth_status = m.get('SpfAuthStatus')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        return self


class QueryDomainByParamResponseBodyData(TeaModel):
    def __init__(
        self,
        domain: List[QueryDomainByParamResponseBodyDataDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        if self.domain:
            for k in self.domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['domain'] = []
        if self.domain is not None:
            for k in self.domain:
                result['domain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('domain') is not None:
            for k in m.get('domain'):
                temp_model = QueryDomainByParamResponseBodyDataDomain()
                self.domain.append(temp_model.from_map(k))
        return self


class QueryDomainByParamResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryDomainByParamResponseBodyData = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryDomainByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryDomainByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDomainByParamResponseBody = None,
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
            temp_model = QueryDomainByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInvalidAddressRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        key_word: str = None,
        length: int = None,
        next_start: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.key_word = key_word
        self.length = length
        self.next_start = next_start
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.length is not None:
            result['Length'] = self.length
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryInvalidAddressResponseBodyDataMailDetail(TeaModel):
    def __init__(
        self,
        last_update_time: str = None,
        to_address: str = None,
        utc_last_update_time: int = None,
    ):
        self.last_update_time = last_update_time
        self.to_address = to_address
        self.utc_last_update_time = utc_last_update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.utc_last_update_time is not None:
            result['UtcLastUpdateTime'] = self.utc_last_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('UtcLastUpdateTime') is not None:
            self.utc_last_update_time = m.get('UtcLastUpdateTime')
        return self


class QueryInvalidAddressResponseBodyData(TeaModel):
    def __init__(
        self,
        mail_detail: List[QueryInvalidAddressResponseBodyDataMailDetail] = None,
    ):
        self.mail_detail = mail_detail

    def validate(self):
        if self.mail_detail:
            for k in self.mail_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mailDetail'] = []
        if self.mail_detail is not None:
            for k in self.mail_detail:
                result['mailDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mail_detail = []
        if m.get('mailDetail') is not None:
            for k in m.get('mailDetail'):
                temp_model = QueryInvalidAddressResponseBodyDataMailDetail()
                self.mail_detail.append(temp_model.from_map(k))
        return self


class QueryInvalidAddressResponseBody(TeaModel):
    def __init__(
        self,
        next_start: int = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryInvalidAddressResponseBodyData = None,
    ):
        self.next_start = next_start
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryInvalidAddressResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryInvalidAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInvalidAddressResponseBody = None,
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
            temp_model = QueryInvalidAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMailAddressByParamRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sendtype: str = None,
    ):
        self.key_word = key_word
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sendtype = sendtype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')
        return self


class QueryMailAddressByParamResponseBodyDataMailAddress(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_status: str = None,
        create_time: str = None,
        daily_count: str = None,
        daily_req_count: str = None,
        domain_status: str = None,
        mail_address_id: str = None,
        month_count: str = None,
        month_req_count: str = None,
        reply_address: str = None,
        reply_status: str = None,
        sendtype: str = None,
    ):
        self.account_name = account_name
        self.account_status = account_status
        self.create_time = create_time
        self.daily_count = daily_count
        self.daily_req_count = daily_req_count
        self.domain_status = domain_status
        self.mail_address_id = mail_address_id
        self.month_count = month_count
        self.month_req_count = month_req_count
        self.reply_address = reply_address
        self.reply_status = reply_status
        self.sendtype = sendtype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.daily_count is not None:
            result['DailyCount'] = self.daily_count
        if self.daily_req_count is not None:
            result['DailyReqCount'] = self.daily_req_count
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.month_count is not None:
            result['MonthCount'] = self.month_count
        if self.month_req_count is not None:
            result['MonthReqCount'] = self.month_req_count
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_status is not None:
            result['ReplyStatus'] = self.reply_status
        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DailyCount') is not None:
            self.daily_count = m.get('DailyCount')
        if m.get('DailyReqCount') is not None:
            self.daily_req_count = m.get('DailyReqCount')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('MonthCount') is not None:
            self.month_count = m.get('MonthCount')
        if m.get('MonthReqCount') is not None:
            self.month_req_count = m.get('MonthReqCount')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyStatus') is not None:
            self.reply_status = m.get('ReplyStatus')
        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')
        return self


class QueryMailAddressByParamResponseBodyData(TeaModel):
    def __init__(
        self,
        mail_address: List[QueryMailAddressByParamResponseBodyDataMailAddress] = None,
    ):
        self.mail_address = mail_address

    def validate(self):
        if self.mail_address:
            for k in self.mail_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mailAddress'] = []
        if self.mail_address is not None:
            for k in self.mail_address:
                result['mailAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mail_address = []
        if m.get('mailAddress') is not None:
            for k in m.get('mailAddress'):
                temp_model = QueryMailAddressByParamResponseBodyDataMailAddress()
                self.mail_address.append(temp_model.from_map(k))
        return self


class QueryMailAddressByParamResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryMailAddressByParamResponseBodyData = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryMailAddressByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryMailAddressByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMailAddressByParamResponseBody = None,
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
            temp_model = QueryMailAddressByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReceiverByParamRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: int = None,
    ):
        self.key_word = key_word
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryReceiverByParamResponseBodyDataReceiver(TeaModel):
    def __init__(
        self,
        count: str = None,
        create_time: str = None,
        desc: str = None,
        receiver_id: str = None,
        receivers_alias: str = None,
        receivers_name: str = None,
        receivers_status: str = None,
        utc_create_time: int = None,
    ):
        self.count = count
        self.create_time = create_time
        self.desc = desc
        self.receiver_id = receiver_id
        self.receivers_alias = receivers_alias
        self.receivers_name = receivers_name
        self.receivers_status = receivers_status
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.receivers_alias is not None:
            result['ReceiversAlias'] = self.receivers_alias
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.receivers_status is not None:
            result['ReceiversStatus'] = self.receivers_status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ReceiversAlias') is not None:
            self.receivers_alias = m.get('ReceiversAlias')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('ReceiversStatus') is not None:
            self.receivers_status = m.get('ReceiversStatus')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        return self


class QueryReceiverByParamResponseBodyData(TeaModel):
    def __init__(
        self,
        receiver: List[QueryReceiverByParamResponseBodyDataReceiver] = None,
    ):
        self.receiver = receiver

    def validate(self):
        if self.receiver:
            for k in self.receiver:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['receiver'] = []
        if self.receiver is not None:
            for k in self.receiver:
                result['receiver'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.receiver = []
        if m.get('receiver') is not None:
            for k in m.get('receiver'):
                temp_model = QueryReceiverByParamResponseBodyDataReceiver()
                self.receiver.append(temp_model.from_map(k))
        return self


class QueryReceiverByParamResponseBody(TeaModel):
    def __init__(
        self,
        next_start: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryReceiverByParamResponseBodyData = None,
    ):
        self.next_start = next_start
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryReceiverByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryReceiverByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryReceiverByParamResponseBody = None,
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
            temp_model = QueryReceiverByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReceiverDetailRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        next_start: str = None,
        owner_id: int = None,
        page_size: int = None,
        receiver_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.key_word = key_word
        self.next_start = next_start
        self.owner_id = owner_id
        self.page_size = page_size
        self.receiver_id = receiver_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryReceiverDetailResponseBodyDataDetail(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data: str = None,
        email: str = None,
        utc_create_time: int = None,
    ):
        self.create_time = create_time
        self.data = data
        self.email = email
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.email is not None:
            result['Email'] = self.email
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        return self


class QueryReceiverDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        detail: List[QueryReceiverDetailResponseBodyDataDetail] = None,
    ):
        self.detail = detail

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = QueryReceiverDetailResponseBodyDataDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class QueryReceiverDetailResponseBody(TeaModel):
    def __init__(
        self,
        data_schema: str = None,
        next_start: str = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryReceiverDetailResponseBodyData = None,
    ):
        self.data_schema = data_schema
        self.next_start = next_start
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_schema is not None:
            result['DataSchema'] = self.data_schema
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSchema') is not None:
            self.data_schema = m.get('DataSchema')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryReceiverDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryReceiverDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryReceiverDetailResponseBody = None,
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
            temp_model = QueryReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagByParamRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.key_word = key_word
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTagByParamResponseBodyDataTag(TeaModel):
    def __init__(
        self,
        tag_description: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        self.tag_description = tag_description
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class QueryTagByParamResponseBodyData(TeaModel):
    def __init__(
        self,
        tag: List[QueryTagByParamResponseBodyDataTag] = None,
    ):
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
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = QueryTagByParamResponseBodyDataTag()
                self.tag.append(temp_model.from_map(k))
        return self


class QueryTagByParamResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryTagByParamResponseBodyData = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryTagByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryTagByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTagByParamResponseBody = None,
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
            temp_model = QueryTagByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskByParamRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: int = None,
    ):
        self.key_word = key_word
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryTaskByParamResponseBodyDataTask(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        create_time: str = None,
        receivers_name: str = None,
        request_count: str = None,
        tag_name: str = None,
        task_id: str = None,
        task_status: str = None,
        template_name: str = None,
        utc_create_time: int = None,
    ):
        self.address_type = address_type
        self.create_time = create_time
        self.receivers_name = receivers_name
        self.request_count = request_count
        self.tag_name = tag_name
        self.task_id = task_id
        self.task_status = task_status
        self.template_name = template_name
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        return self


class QueryTaskByParamResponseBodyData(TeaModel):
    def __init__(
        self,
        task: List[QueryTaskByParamResponseBodyDataTask] = None,
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
        result['task'] = []
        if self.task is not None:
            for k in self.task:
                result['task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('task') is not None:
            for k in m.get('task'):
                temp_model = QueryTaskByParamResponseBodyDataTask()
                self.task.append(temp_model.from_map(k))
        return self


class QueryTaskByParamResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryTaskByParamResponseBodyData = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryTaskByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryTaskByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskByParamResponseBody = None,
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
            temp_model = QueryTaskByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTemplateByParamRequest(TeaModel):
    def __init__(
        self,
        from_type: int = None,
        key_word: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: int = None,
    ):
        self.from_type = from_type
        self.key_word = key_word
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryTemplateByParamResponseBodyDataTemplate(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        sms_status: int = None,
        sms_template_code: int = None,
        smsrejectinfo: int = None,
        template_comment: str = None,
        template_id: str = None,
        template_name: str = None,
        template_status: str = None,
        template_type: int = None,
        utc_createtime: int = None,
    ):
        self.create_time = create_time
        self.sms_status = sms_status
        self.sms_template_code = sms_template_code
        self.smsrejectinfo = smsrejectinfo
        self.template_comment = template_comment
        self.template_id = template_id
        self.template_name = template_name
        self.template_status = template_status
        self.template_type = template_type
        self.utc_createtime = utc_createtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.smsrejectinfo is not None:
            result['Smsrejectinfo'] = self.smsrejectinfo
        if self.template_comment is not None:
            result['TemplateComment'] = self.template_comment
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.utc_createtime is not None:
            result['UtcCreatetime'] = self.utc_createtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('Smsrejectinfo') is not None:
            self.smsrejectinfo = m.get('Smsrejectinfo')
        if m.get('TemplateComment') is not None:
            self.template_comment = m.get('TemplateComment')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('UtcCreatetime') is not None:
            self.utc_createtime = m.get('UtcCreatetime')
        return self


class QueryTemplateByParamResponseBodyData(TeaModel):
    def __init__(
        self,
        template: List[QueryTemplateByParamResponseBodyDataTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for k in self.template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['template'] = []
        if self.template is not None:
            for k in self.template:
                result['template'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('template') is not None:
            for k in m.get('template'):
                temp_model = QueryTemplateByParamResponseBodyDataTemplate()
                self.template.append(temp_model.from_map(k))
        return self


class QueryTemplateByParamResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryTemplateByParamResponseBodyData = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = QueryTemplateByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryTemplateByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTemplateByParamResponseBody = None,
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
            temp_model = QueryTemplateByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveReceiverDetailRequest(TeaModel):
    def __init__(
        self,
        detail: str = None,
        owner_id: int = None,
        receiver_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.detail = detail
        self.owner_id = owner_id
        self.receiver_id = receiver_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SaveReceiverDetailResponseBodyDataDetail(TeaModel):
    def __init__(
        self,
        email: str = None,
    ):
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class SaveReceiverDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        detail: List[SaveReceiverDetailResponseBodyDataDetail] = None,
    ):
        self.detail = detail

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = SaveReceiverDetailResponseBodyDataDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class SaveReceiverDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: SaveReceiverDetailResponseBodyData = None,
        error_count: int = None,
        request_id: str = None,
        success_count: int = None,
    ):
        self.data = data
        self.error_count = error_count
        self.request_id = request_id
        self.success_count = success_count

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
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SaveReceiverDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class SaveReceiverDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveReceiverDetailResponseBody = None,
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
            temp_model = SaveReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SenderStatisticsByTagNameAndBatchIDRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag_name: str = None,
    ):
        self.account_name = account_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        faild_count: str = None,
        request_count: str = None,
        succeeded_percent: str = None,
        success_count: str = None,
        unavailable_count: str = None,
        unavailable_percent: str = None,
    ):
        self.create_time = create_time
        self.faild_count = faild_count
        self.request_count = request_count
        self.succeeded_percent = succeeded_percent
        self.success_count = success_count
        self.unavailable_count = unavailable_count
        self.unavailable_percent = unavailable_percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.faild_count is not None:
            result['faildCount'] = self.faild_count
        if self.request_count is not None:
            result['requestCount'] = self.request_count
        if self.succeeded_percent is not None:
            result['succeededPercent'] = self.succeeded_percent
        if self.success_count is not None:
            result['successCount'] = self.success_count
        if self.unavailable_count is not None:
            result['unavailableCount'] = self.unavailable_count
        if self.unavailable_percent is not None:
            result['unavailablePercent'] = self.unavailable_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('faildCount') is not None:
            self.faild_count = m.get('faildCount')
        if m.get('requestCount') is not None:
            self.request_count = m.get('requestCount')
        if m.get('succeededPercent') is not None:
            self.succeeded_percent = m.get('succeededPercent')
        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')
        if m.get('unavailableCount') is not None:
            self.unavailable_count = m.get('unavailableCount')
        if m.get('unavailablePercent') is not None:
            self.unavailable_percent = m.get('unavailablePercent')
        return self


class SenderStatisticsByTagNameAndBatchIDResponseBodyData(TeaModel):
    def __init__(
        self,
        stat: List[SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat] = None,
    ):
        self.stat = stat

    def validate(self):
        if self.stat:
            for k in self.stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['stat'] = []
        if self.stat is not None:
            for k in self.stat:
                result['stat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stat = []
        if m.get('stat') is not None:
            for k in m.get('stat'):
                temp_model = SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat()
                self.stat.append(temp_model.from_map(k))
        return self


class SenderStatisticsByTagNameAndBatchIDResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        data: SenderStatisticsByTagNameAndBatchIDResponseBodyData = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('data') is not None:
            temp_model = SenderStatisticsByTagNameAndBatchIDResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class SenderStatisticsByTagNameAndBatchIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SenderStatisticsByTagNameAndBatchIDResponseBody = None,
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
            temp_model = SenderStatisticsByTagNameAndBatchIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SenderStatisticsDetailByParamRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        end_time: str = None,
        length: int = None,
        next_start: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        status: int = None,
        tag_name: str = None,
        to_address: str = None,
    ):
        self.account_name = account_name
        self.end_time = end_time
        self.length = length
        self.next_start = next_start
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.status = status
        self.tag_name = tag_name
        self.to_address = to_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.length is not None:
            result['Length'] = self.length
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class SenderStatisticsDetailByParamResponseBodyDataMailDetail(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        last_update_time: str = None,
        message: str = None,
        status: int = None,
        to_address: str = None,
        utc_last_update_time: str = None,
    ):
        self.account_name = account_name
        self.last_update_time = last_update_time
        self.message = message
        self.status = status
        self.to_address = to_address
        self.utc_last_update_time = utc_last_update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.utc_last_update_time is not None:
            result['UtcLastUpdateTime'] = self.utc_last_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('UtcLastUpdateTime') is not None:
            self.utc_last_update_time = m.get('UtcLastUpdateTime')
        return self


class SenderStatisticsDetailByParamResponseBodyData(TeaModel):
    def __init__(
        self,
        mail_detail: List[SenderStatisticsDetailByParamResponseBodyDataMailDetail] = None,
    ):
        self.mail_detail = mail_detail

    def validate(self):
        if self.mail_detail:
            for k in self.mail_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mailDetail'] = []
        if self.mail_detail is not None:
            for k in self.mail_detail:
                result['mailDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mail_detail = []
        if m.get('mailDetail') is not None:
            for k in m.get('mailDetail'):
                temp_model = SenderStatisticsDetailByParamResponseBodyDataMailDetail()
                self.mail_detail.append(temp_model.from_map(k))
        return self


class SenderStatisticsDetailByParamResponseBody(TeaModel):
    def __init__(
        self,
        next_start: int = None,
        request_id: str = None,
        data: SenderStatisticsDetailByParamResponseBodyData = None,
    ):
        self.next_start = next_start
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
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = SenderStatisticsDetailByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class SenderStatisticsDetailByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SenderStatisticsDetailByParamResponseBody = None,
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
            temp_model = SenderStatisticsDetailByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleSendMailRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        click_trace: str = None,
        from_alias: str = None,
        html_body: str = None,
        owner_id: int = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        reply_to_address: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
        tag_name: str = None,
        text_body: str = None,
        to_address: str = None,
    ):
        self.account_name = account_name
        self.address_type = address_type
        self.click_trace = click_trace
        self.from_alias = from_alias
        self.html_body = html_body
        self.owner_id = owner_id
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject = subject
        self.tag_name = tag_name
        self.text_body = text_body
        self.to_address = to_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.from_alias is not None:
            result['FromAlias'] = self.from_alias
        if self.html_body is not None:
            result['HtmlBody'] = self.html_body
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_address_alias is not None:
            result['ReplyAddressAlias'] = self.reply_address_alias
        if self.reply_to_address is not None:
            result['ReplyToAddress'] = self.reply_to_address
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.text_body is not None:
            result['TextBody'] = self.text_body
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('FromAlias') is not None:
            self.from_alias = m.get('FromAlias')
        if m.get('HtmlBody') is not None:
            self.html_body = m.get('HtmlBody')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyAddressAlias') is not None:
            self.reply_address_alias = m.get('ReplyAddressAlias')
        if m.get('ReplyToAddress') is not None:
            self.reply_to_address = m.get('ReplyToAddress')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class SingleSendMailResponseBody(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        request_id: str = None,
    ):
        self.env_id = env_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SingleSendMailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SingleSendMailResponseBody = None,
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
            temp_model = SingleSendMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleSendMailV2RequestHtmlBodyPlaceHolders(TeaModel):
    def __init__(
        self,
        place_holders: Dict[str, str] = None,
        to_address: str = None,
    ):
        self.place_holders = place_holders
        self.to_address = to_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.place_holders is not None:
            result['PlaceHolders'] = self.place_holders
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaceHolders') is not None:
            self.place_holders = m.get('PlaceHolders')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class SingleSendMailV2Request(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        click_trace: str = None,
        from_alias: str = None,
        html_body: str = None,
        html_body_place_holders: List[SingleSendMailV2RequestHtmlBodyPlaceHolders] = None,
        owner_id: int = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        reply_to_address: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
        tag_name: str = None,
        text_body: str = None,
        to_address: str = None,
    ):
        self.account_name = account_name
        self.address_type = address_type
        self.click_trace = click_trace
        self.from_alias = from_alias
        self.html_body = html_body
        self.html_body_place_holders = html_body_place_holders
        self.owner_id = owner_id
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject = subject
        self.tag_name = tag_name
        self.text_body = text_body
        self.to_address = to_address

    def validate(self):
        if self.html_body_place_holders:
            for k in self.html_body_place_holders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.from_alias is not None:
            result['FromAlias'] = self.from_alias
        if self.html_body is not None:
            result['HtmlBody'] = self.html_body
        result['HtmlBodyPlaceHolders'] = []
        if self.html_body_place_holders is not None:
            for k in self.html_body_place_holders:
                result['HtmlBodyPlaceHolders'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_address_alias is not None:
            result['ReplyAddressAlias'] = self.reply_address_alias
        if self.reply_to_address is not None:
            result['ReplyToAddress'] = self.reply_to_address
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.text_body is not None:
            result['TextBody'] = self.text_body
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('FromAlias') is not None:
            self.from_alias = m.get('FromAlias')
        if m.get('HtmlBody') is not None:
            self.html_body = m.get('HtmlBody')
        self.html_body_place_holders = []
        if m.get('HtmlBodyPlaceHolders') is not None:
            for k in m.get('HtmlBodyPlaceHolders'):
                temp_model = SingleSendMailV2RequestHtmlBodyPlaceHolders()
                self.html_body_place_holders.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyAddressAlias') is not None:
            self.reply_address_alias = m.get('ReplyAddressAlias')
        if m.get('ReplyToAddress') is not None:
            self.reply_to_address = m.get('ReplyToAddress')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class SingleSendMailV2ShrinkRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        click_trace: str = None,
        from_alias: str = None,
        html_body: str = None,
        html_body_place_holders_shrink: str = None,
        owner_id: int = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        reply_to_address: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
        tag_name: str = None,
        text_body: str = None,
        to_address: str = None,
    ):
        self.account_name = account_name
        self.address_type = address_type
        self.click_trace = click_trace
        self.from_alias = from_alias
        self.html_body = html_body
        self.html_body_place_holders_shrink = html_body_place_holders_shrink
        self.owner_id = owner_id
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject = subject
        self.tag_name = tag_name
        self.text_body = text_body
        self.to_address = to_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.from_alias is not None:
            result['FromAlias'] = self.from_alias
        if self.html_body is not None:
            result['HtmlBody'] = self.html_body
        if self.html_body_place_holders_shrink is not None:
            result['HtmlBodyPlaceHolders'] = self.html_body_place_holders_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_address_alias is not None:
            result['ReplyAddressAlias'] = self.reply_address_alias
        if self.reply_to_address is not None:
            result['ReplyToAddress'] = self.reply_to_address
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.text_body is not None:
            result['TextBody'] = self.text_body
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('FromAlias') is not None:
            self.from_alias = m.get('FromAlias')
        if m.get('HtmlBody') is not None:
            self.html_body = m.get('HtmlBody')
        if m.get('HtmlBodyPlaceHolders') is not None:
            self.html_body_place_holders_shrink = m.get('HtmlBodyPlaceHolders')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyAddressAlias') is not None:
            self.reply_address_alias = m.get('ReplyAddressAlias')
        if m.get('ReplyToAddress') is not None:
            self.reply_to_address = m.get('ReplyToAddress')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class SingleSendMailV2ResponseBody(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        request_id: str = None,
    ):
        self.env_id = env_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SingleSendMailV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SingleSendMailV2ResponseBody = None,
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
            temp_model = SingleSendMailV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


