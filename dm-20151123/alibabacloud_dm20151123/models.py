# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddIpfilterRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ip_address: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        return self


class AddIpfilterResponseBody(TeaModel):
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


class AddIpfilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddIpfilterResponseBody = None,
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
            temp_model = AddIpfilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveMailTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class ApproveMailTemplateResponseBody(TeaModel):
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


class ApproveMailTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApproveMailTemplateResponseBody = None,
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
            temp_model = ApproveMailTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveReplyMailAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ticket: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class ApproveReplyMailAddressResponseBody(TeaModel):
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


class ApproveReplyMailAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApproveReplyMailAddressResponseBody = None,
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
            temp_model = ApproveReplyMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class ApproveSmsTemplateResponseBody(TeaModel):
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


class ApproveSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApproveSmsTemplateResponseBody = None,
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
            temp_model = ApproveSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class ApproveTemplateResponseBody(TeaModel):
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


class ApproveTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApproveTemplateResponseBody = None,
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
            temp_model = ApproveTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSendMailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_name: str = None,
        account_name: str = None,
        receivers_name: str = None,
        address_type: int = None,
        tag_name: str = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        click_trace: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_name = template_name
        self.account_name = account_name
        self.receivers_name = receivers_name
        self.address_type = address_type
        self.tag_name = tag_name
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        self.click_trace = click_trace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_address_alias is not None:
            result['ReplyAddressAlias'] = self.reply_address_alias
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyAddressAlias') is not None:
            self.reply_address_alias = m.get('ReplyAddressAlias')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        return self


class BatchSendMailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        env_id: str = None,
    ):
        self.request_id = request_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class BatchSendMailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSendMailResponseBody = None,
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
            temp_model = BatchSendMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        domain_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        return self


class CheckDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_status: int = None,
    ):
        self.request_id = request_id
        self.domain_status = domain_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        return self


class CheckDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckDomainResponseBody = None,
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
            temp_model = CheckDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckInvalidAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to_address: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.to_address = to_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class CheckInvalidAddressResponseBody(TeaModel):
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


class CheckInvalidAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckInvalidAddressResponseBody = None,
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
            temp_model = CheckInvalidAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckReplyToMailAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        region: str = None,
        mail_address_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.region = region
        self.mail_address_id = mail_address_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region is not None:
            result['Region'] = self.region
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        return self


class CheckReplyToMailAddressResponseBody(TeaModel):
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


class CheckReplyToMailAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckReplyToMailAddressResponseBody = None,
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
            temp_model = CheckReplyToMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDayuRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        account_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class CreateDayuResponseBody(TeaModel):
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


class CreateDayuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDayuResponseBody = None,
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
            temp_model = CreateDayuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        domain_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
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
        body: CreateDomainResponseBody = None,
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
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMailAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        account_name: str = None,
        reply_address: str = None,
        sendtype: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.account_name = account_name
        self.reply_address = reply_address
        self.sendtype = sendtype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')
        return self


class CreateMailAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mail_address_id: str = None,
    ):
        self.request_id = request_id
        self.mail_address_id = mail_address_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        return self


class CreateMailAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMailAddressResponseBody = None,
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
            temp_model = CreateMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReceiverRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        receivers_name: str = None,
        receivers_alias: str = None,
        desc: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.receivers_name = receivers_name
        self.receivers_alias = receivers_alias
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.receivers_alias is not None:
            result['ReceiversAlias'] = self.receivers_alias
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('ReceiversAlias') is not None:
            self.receivers_alias = m.get('ReceiversAlias')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
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
        body: CreateReceiverResponseBody = None,
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
            temp_model = CreateReceiverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSignRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        remark: str = None,
        sign_type: int = None,
        file_names: str = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name
        self.remark = remark
        self.sign_type = sign_type
        self.file_names = file_names
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        if self.file_names is not None:
            result['FileNames'] = self.file_names
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        if m.get('FileNames') is not None:
            self.file_names = m.get('FileNames')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class CreateSignResponseBody(TeaModel):
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


class CreateSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSignResponseBody = None,
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
            temp_model = CreateSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        body: CreateTagResponseBody = None,
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
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_type: int = None,
        template_name: str = None,
        template_subject: str = None,
        template_nick_name: str = None,
        template_text: str = None,
        sms_type: int = None,
        sms_content: str = None,
        remark: str = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_type = template_type
        self.template_name = template_name
        self.template_subject = template_subject
        self.template_nick_name = template_nick_name
        self.template_text = template_text
        self.sms_type = sms_type
        self.sms_content = sms_content
        self.remark = remark
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject
        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name
        if self.template_text is not None:
            result['TemplateText'] = self.template_text
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')
        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')
        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
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
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        domain_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
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


class DeleteInvalidAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to_address: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.to_address = to_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        return self


class DeleteInvalidAddressResponseBody(TeaModel):
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


class DeleteInvalidAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInvalidAddressResponseBody = None,
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
            temp_model = DeleteInvalidAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpfilterByEdmIdRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        from_type: int = None,
        id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.from_type = from_type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteIpfilterByEdmIdResponseBody(TeaModel):
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


class DeleteIpfilterByEdmIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIpfilterByEdmIdResponseBody = None,
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
            temp_model = DeleteIpfilterByEdmIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMailAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        mail_address_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.mail_address_id = mail_address_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
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
        body: DeleteMailAddressResponseBody = None,
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
            temp_model = DeleteMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReceiverRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        receiver_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.receiver_id = receiver_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
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
        body: DeleteReceiverResponseBody = None,
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
            temp_model = DeleteReceiverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReceiverDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        receiver_id: str = None,
        email: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.receiver_id = receiver_id
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
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
        body: DeleteReceiverDetailResponseBody = None,
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
            temp_model = DeleteReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSignRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_id: int = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_id = sign_id
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_id is not None:
            result['SignId'] = self.sign_id
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class DeleteSignResponseBody(TeaModel):
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


class DeleteSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSignResponseBody = None,
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
            temp_model = DeleteSignResponseBody()
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
        body: DeleteTagResponseBody = None,
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
            temp_model = DeleteTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
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
        body: DeleteTemplateResponseBody = None,
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
        dayu_status: int = None,
        sms_record: int = None,
        month_quota: int = None,
        request_id: str = None,
        receivers: int = None,
        sms_templates: int = None,
        templates: int = None,
        daily_quota: int = None,
        user_status: int = None,
        domains: int = None,
        quota_level: int = None,
        sms_sign: int = None,
        max_quota_level: int = None,
        enable_times: int = None,
        tags: int = None,
        mail_addresses: int = None,
    ):
        self.dayu_status = dayu_status
        self.sms_record = sms_record
        self.month_quota = month_quota
        self.request_id = request_id
        self.receivers = receivers
        self.sms_templates = sms_templates
        self.templates = templates
        self.daily_quota = daily_quota
        self.user_status = user_status
        self.domains = domains
        self.quota_level = quota_level
        self.sms_sign = sms_sign
        self.max_quota_level = max_quota_level
        self.enable_times = enable_times
        self.tags = tags
        self.mail_addresses = mail_addresses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dayu_status is not None:
            result['DayuStatus'] = self.dayu_status
        if self.sms_record is not None:
            result['SmsRecord'] = self.sms_record
        if self.month_quota is not None:
            result['MonthQuota'] = self.month_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.receivers is not None:
            result['Receivers'] = self.receivers
        if self.sms_templates is not None:
            result['SmsTemplates'] = self.sms_templates
        if self.templates is not None:
            result['Templates'] = self.templates
        if self.daily_quota is not None:
            result['DailyQuota'] = self.daily_quota
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.quota_level is not None:
            result['QuotaLevel'] = self.quota_level
        if self.sms_sign is not None:
            result['SmsSign'] = self.sms_sign
        if self.max_quota_level is not None:
            result['MaxQuotaLevel'] = self.max_quota_level
        if self.enable_times is not None:
            result['EnableTimes'] = self.enable_times
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.mail_addresses is not None:
            result['MailAddresses'] = self.mail_addresses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayuStatus') is not None:
            self.dayu_status = m.get('DayuStatus')
        if m.get('SmsRecord') is not None:
            self.sms_record = m.get('SmsRecord')
        if m.get('MonthQuota') is not None:
            self.month_quota = m.get('MonthQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Receivers') is not None:
            self.receivers = m.get('Receivers')
        if m.get('SmsTemplates') is not None:
            self.sms_templates = m.get('SmsTemplates')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        if m.get('DailyQuota') is not None:
            self.daily_quota = m.get('DailyQuota')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('QuotaLevel') is not None:
            self.quota_level = m.get('QuotaLevel')
        if m.get('SmsSign') is not None:
            self.sms_sign = m.get('SmsSign')
        if m.get('MaxQuotaLevel') is not None:
            self.max_quota_level = m.get('MaxQuotaLevel')
        if m.get('EnableTimes') is not None:
            self.enable_times = m.get('EnableTimes')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('MailAddresses') is not None:
            self.mail_addresses = m.get('MailAddresses')
        return self


class DescAccountSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescAccountSummaryResponseBody = None,
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
            temp_model = DescAccountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescAccountSummary2Request(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class DescAccountSummary2ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mns_force_migrating: int = None,
        mns_bag: int = None,
        mns_migrating: int = None,
    ):
        self.request_id = request_id
        self.mns_force_migrating = mns_force_migrating
        self.mns_bag = mns_bag
        self.mns_migrating = mns_migrating

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mns_force_migrating is not None:
            result['MnsForceMigrating'] = self.mns_force_migrating
        if self.mns_bag is not None:
            result['MnsBag'] = self.mns_bag
        if self.mns_migrating is not None:
            result['MnsMigrating'] = self.mns_migrating
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MnsForceMigrating') is not None:
            self.mns_force_migrating = m.get('MnsForceMigrating')
        if m.get('MnsBag') is not None:
            self.mns_bag = m.get('MnsBag')
        if m.get('MnsMigrating') is not None:
            self.mns_migrating = m.get('MnsMigrating')
        return self


class DescAccountSummary2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescAccountSummary2ResponseBody = None,
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
            temp_model = DescAccountSummary2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescDomainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        domain_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        return self


class DescDomainResponseBody(TeaModel):
    def __init__(
        self,
        spf_record: str = None,
        spf_auth_status: str = None,
        cname_auth_status: str = None,
        request_id: str = None,
        domain_name: str = None,
        dns_mx: str = None,
        create_time: str = None,
        cname_record: str = None,
        dns_txt: str = None,
        cname_confirm_status: str = None,
        icp_status: str = None,
        default_domain: str = None,
        dns_spf: str = None,
        mx_record: str = None,
        domain_id: str = None,
        domain_type: str = None,
        mx_auth_status: str = None,
        tl_domain_name: str = None,
        tracef_record: str = None,
        domain_status: str = None,
    ):
        self.spf_record = spf_record
        self.spf_auth_status = spf_auth_status
        self.cname_auth_status = cname_auth_status
        self.request_id = request_id
        self.domain_name = domain_name
        self.dns_mx = dns_mx
        self.create_time = create_time
        self.cname_record = cname_record
        self.dns_txt = dns_txt
        self.cname_confirm_status = cname_confirm_status
        self.icp_status = icp_status
        self.default_domain = default_domain
        self.dns_spf = dns_spf
        self.mx_record = mx_record
        self.domain_id = domain_id
        self.domain_type = domain_type
        self.mx_auth_status = mx_auth_status
        self.tl_domain_name = tl_domain_name
        self.tracef_record = tracef_record
        self.domain_status = domain_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.spf_record is not None:
            result['SpfRecord'] = self.spf_record
        if self.spf_auth_status is not None:
            result['SpfAuthStatus'] = self.spf_auth_status
        if self.cname_auth_status is not None:
            result['CnameAuthStatus'] = self.cname_auth_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.dns_mx is not None:
            result['DnsMx'] = self.dns_mx
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cname_record is not None:
            result['CnameRecord'] = self.cname_record
        if self.dns_txt is not None:
            result['DnsTxt'] = self.dns_txt
        if self.cname_confirm_status is not None:
            result['CnameConfirmStatus'] = self.cname_confirm_status
        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.dns_spf is not None:
            result['DnsSpf'] = self.dns_spf
        if self.mx_record is not None:
            result['MxRecord'] = self.mx_record
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.mx_auth_status is not None:
            result['MxAuthStatus'] = self.mx_auth_status
        if self.tl_domain_name is not None:
            result['TlDomainName'] = self.tl_domain_name
        if self.tracef_record is not None:
            result['TracefRecord'] = self.tracef_record
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpfRecord') is not None:
            self.spf_record = m.get('SpfRecord')
        if m.get('SpfAuthStatus') is not None:
            self.spf_auth_status = m.get('SpfAuthStatus')
        if m.get('CnameAuthStatus') is not None:
            self.cname_auth_status = m.get('CnameAuthStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DnsMx') is not None:
            self.dns_mx = m.get('DnsMx')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CnameRecord') is not None:
            self.cname_record = m.get('CnameRecord')
        if m.get('DnsTxt') is not None:
            self.dns_txt = m.get('DnsTxt')
        if m.get('CnameConfirmStatus') is not None:
            self.cname_confirm_status = m.get('CnameConfirmStatus')
        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('DnsSpf') is not None:
            self.dns_spf = m.get('DnsSpf')
        if m.get('MxRecord') is not None:
            self.mx_record = m.get('MxRecord')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('MxAuthStatus') is not None:
            self.mx_auth_status = m.get('MxAuthStatus')
        if m.get('TlDomainName') is not None:
            self.tl_domain_name = m.get('TlDomainName')
        if m.get('TracefRecord') is not None:
            self.tracef_record = m.get('TracefRecord')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        return self


class DescDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescDomainResponseBody = None,
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
            temp_model = DescDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class DescTemplateResponseBody(TeaModel):
    def __init__(
        self,
        sms_type: str = None,
        request_id: str = None,
        create_time: str = None,
        template_text: str = None,
        sms_content: str = None,
        template_name: str = None,
        template_nick_name: str = None,
        template_type: str = None,
        template_subject: str = None,
        remark: str = None,
        template_status: str = None,
    ):
        self.sms_type = sms_type
        self.request_id = request_id
        self.create_time = create_time
        self.template_text = template_text
        self.sms_content = sms_content
        self.template_name = template_name
        self.template_nick_name = template_nick_name
        self.template_type = template_type
        self.template_subject = template_subject
        self.remark = remark
        self.template_status = template_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_text is not None:
            result['TemplateText'] = self.template_text
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        return self


class DescTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescTemplateResponseBody = None,
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
            temp_model = DescTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAccountRequest(TeaModel):
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


class EnableAccountResponseBody(TeaModel):
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


class EnableAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableAccountResponseBody = None,
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
            temp_model = EnableAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        total: str = None,
        offset: str = None,
        page_size: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        page_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.total = total
        self.offset = offset
        self.page_size = page_size
        self.offset_create_time = offset_create_time
        self.offset_create_time_desc = offset_create_time_desc
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.total is not None:
            result['Total'] = self.total
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class GetAccountListResponseBodyDataAccountNotificationInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: str = None,
        region: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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
        page_size: int = None,
        request_id: str = None,
        data: GetAccountListResponseBodyData = None,
        total: int = None,
        page_no: int = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.total = total
        self.page_no = page_no

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.total is not None:
            result['Total'] = self.total
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = GetAccountListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class GetAccountListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccountListResponseBody = None,
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
            temp_model = GetAccountListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIpfilterListRequest(TeaModel):
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


class GetIpfilterListResponseBodyDataIpfilters(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        create_time: str = None,
        id: str = None,
    ):
        self.ip_address = ip_address
        self.create_time = create_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetIpfilterListResponseBodyData(TeaModel):
    def __init__(
        self,
        ipfilters: List[GetIpfilterListResponseBodyDataIpfilters] = None,
    ):
        self.ipfilters = ipfilters

    def validate(self):
        if self.ipfilters:
            for k in self.ipfilters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ipfilters'] = []
        if self.ipfilters is not None:
            for k in self.ipfilters:
                result['ipfilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipfilters = []
        if m.get('ipfilters') is not None:
            for k in m.get('ipfilters'):
                temp_model = GetIpfilterListResponseBodyDataIpfilters()
                self.ipfilters.append(temp_model.from_map(k))
        return self


class GetIpfilterListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        data: GetIpfilterListResponseBodyData = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.page_number = page_number

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = GetIpfilterListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class GetIpfilterListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIpfilterListResponseBody = None,
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
            temp_model = GetIpfilterListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIpProtectionRequest(TeaModel):
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


class GetIpProtectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ip_protection: str = None,
    ):
        self.request_id = request_id
        self.ip_protection = ip_protection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_protection is not None:
            result['IpProtection'] = self.ip_protection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpProtection') is not None:
            self.ip_protection = m.get('IpProtection')
        return self


class GetIpProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIpProtectionResponseBody = None,
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
            temp_model = GetIpProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMailAddressMsgCallBackUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        mail_from: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.mail_from = mail_from

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.mail_from is not None:
            result['MailFrom'] = self.mail_from
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('MailFrom') is not None:
            self.mail_from = m.get('MailFrom')
        return self


class GetMailAddressMsgCallBackUrlResponseBody(TeaModel):
    def __init__(
        self,
        notify_url_status: int = None,
        request_id: str = None,
        notify_url: int = None,
    ):
        self.notify_url_status = notify_url_status
        self.request_id = request_id
        self.notify_url = notify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.notify_url_status is not None:
            result['NotifyUrlStatus'] = self.notify_url_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyUrlStatus') is not None:
            self.notify_url_status = m.get('NotifyUrlStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        return self


class GetMailAddressMsgCallBackUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMailAddressMsgCallBackUrlResponseBody = None,
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
            temp_model = GetMailAddressMsgCallBackUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        total: str = None,
        offset: str = None,
        page_size: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        page_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.total = total
        self.offset = offset
        self.page_size = page_size
        self.offset_create_time = offset_create_time
        self.offset_create_time_desc = offset_create_time_desc
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.total is not None:
            result['Total'] = self.total
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class GetRegionListResponseBodyDataRegionList(TeaModel):
    def __init__(
        self,
        region_desc: str = None,
        region: str = None,
    ):
        self.region_desc = region_desc
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_desc is not None:
            result['RegionDesc'] = self.region_desc
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionDesc') is not None:
            self.region_desc = m.get('RegionDesc')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetRegionListResponseBodyData(TeaModel):
    def __init__(
        self,
        region_list: List[GetRegionListResponseBodyDataRegionList] = None,
    ):
        self.region_list = region_list

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['regionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['regionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_list = []
        if m.get('regionList') is not None:
            for k in m.get('regionList'):
                temp_model = GetRegionListResponseBodyDataRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class GetRegionListResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        data: GetRegionListResponseBodyData = None,
        total: int = None,
        page_no: int = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.total = total
        self.page_no = page_no

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.total is not None:
            result['Total'] = self.total
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = GetRegionListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class GetRegionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRegionListResponseBody = None,
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
            temp_model = GetRegionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSenderAddressListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        total: str = None,
        offset: str = None,
        page_size: str = None,
        page_no: str = None,
        keyword: str = None,
        notify_url: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.total = total
        self.offset = offset
        self.page_size = page_size
        self.page_no = page_no
        self.keyword = keyword
        self.notify_url = notify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.total is not None:
            result['Total'] = self.total
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        return self


class GetSenderAddressListResponseBodyDataSenderAddressNotificationInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: str = None,
        sender_address: str = None,
        region: str = None,
        sender_address_id: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.sender_address = sender_address
        self.region = region
        self.sender_address_id = sender_address_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.sender_address is not None:
            result['SenderAddress'] = self.sender_address
        if self.region is not None:
            result['Region'] = self.region
        if self.sender_address_id is not None:
            result['SenderAddressId'] = self.sender_address_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('SenderAddress') is not None:
            self.sender_address = m.get('SenderAddress')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SenderAddressId') is not None:
            self.sender_address_id = m.get('SenderAddressId')
        return self


class GetSenderAddressListResponseBodyData(TeaModel):
    def __init__(
        self,
        sender_address_notification_info: List[GetSenderAddressListResponseBodyDataSenderAddressNotificationInfo] = None,
    ):
        self.sender_address_notification_info = sender_address_notification_info

    def validate(self):
        if self.sender_address_notification_info:
            for k in self.sender_address_notification_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['senderAddressNotificationInfo'] = []
        if self.sender_address_notification_info is not None:
            for k in self.sender_address_notification_info:
                result['senderAddressNotificationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sender_address_notification_info = []
        if m.get('senderAddressNotificationInfo') is not None:
            for k in m.get('senderAddressNotificationInfo'):
                temp_model = GetSenderAddressListResponseBodyDataSenderAddressNotificationInfo()
                self.sender_address_notification_info.append(temp_model.from_map(k))
        return self


class GetSenderAddressListResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        data: GetSenderAddressListResponseBodyData = None,
        total: int = None,
        page_no: int = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.total = total
        self.page_no = page_no

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.total is not None:
            result['Total'] = self.total
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = GetSenderAddressListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class GetSenderAddressListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSenderAddressListResponseBody = None,
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
            temp_model = GetSenderAddressListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrackListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        total: str = None,
        offset: str = None,
        page_size: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        page_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.total = total
        self.offset = offset
        self.page_size = page_size
        self.offset_create_time = offset_create_time
        self.offset_create_time_desc = offset_create_time_desc
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.total is not None:
            result['Total'] = self.total
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class GetTrackListResponseBodyDataStat(TeaModel):
    def __init__(
        self,
        rcpt_click_rate: str = None,
        rcpt_unique_open_count: str = None,
        rcpt_click_count: str = None,
        rcpt_unique_click_count: str = None,
        create_time: str = None,
        rcpt_unique_open_rate: str = None,
        rcpt_unique_click_rate: str = None,
        total_number: str = None,
        rcpt_open_rate: str = None,
        rcpt_open_count: str = None,
    ):
        self.rcpt_click_rate = rcpt_click_rate
        self.rcpt_unique_open_count = rcpt_unique_open_count
        self.rcpt_click_count = rcpt_click_count
        self.rcpt_unique_click_count = rcpt_unique_click_count
        self.create_time = create_time
        self.rcpt_unique_open_rate = rcpt_unique_open_rate
        self.rcpt_unique_click_rate = rcpt_unique_click_rate
        self.total_number = total_number
        self.rcpt_open_rate = rcpt_open_rate
        self.rcpt_open_count = rcpt_open_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rcpt_click_rate is not None:
            result['RcptClickRate'] = self.rcpt_click_rate
        if self.rcpt_unique_open_count is not None:
            result['RcptUniqueOpenCount'] = self.rcpt_unique_open_count
        if self.rcpt_click_count is not None:
            result['RcptClickCount'] = self.rcpt_click_count
        if self.rcpt_unique_click_count is not None:
            result['RcptUniqueClickCount'] = self.rcpt_unique_click_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rcpt_unique_open_rate is not None:
            result['RcptUniqueOpenRate'] = self.rcpt_unique_open_rate
        if self.rcpt_unique_click_rate is not None:
            result['RcptUniqueClickRate'] = self.rcpt_unique_click_rate
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        if self.rcpt_open_rate is not None:
            result['RcptOpenRate'] = self.rcpt_open_rate
        if self.rcpt_open_count is not None:
            result['RcptOpenCount'] = self.rcpt_open_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RcptClickRate') is not None:
            self.rcpt_click_rate = m.get('RcptClickRate')
        if m.get('RcptUniqueOpenCount') is not None:
            self.rcpt_unique_open_count = m.get('RcptUniqueOpenCount')
        if m.get('RcptClickCount') is not None:
            self.rcpt_click_count = m.get('RcptClickCount')
        if m.get('RcptUniqueClickCount') is not None:
            self.rcpt_unique_click_count = m.get('RcptUniqueClickCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RcptUniqueOpenRate') is not None:
            self.rcpt_unique_open_rate = m.get('RcptUniqueOpenRate')
        if m.get('RcptUniqueClickRate') is not None:
            self.rcpt_unique_click_rate = m.get('RcptUniqueClickRate')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        if m.get('RcptOpenRate') is not None:
            self.rcpt_open_rate = m.get('RcptOpenRate')
        if m.get('RcptOpenCount') is not None:
            self.rcpt_open_count = m.get('RcptOpenCount')
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
        request_id: str = None,
        page_size: int = None,
        data: GetTrackListResponseBodyData = None,
        total: int = None,
        page_no: int = None,
        offset_create_time_desc: str = None,
    ):
        self.offset_create_time = offset_create_time
        self.request_id = request_id
        self.page_size = page_size
        self.data = data
        self.total = total
        self.page_no = page_no
        self.offset_create_time_desc = offset_create_time_desc

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.total is not None:
            result['Total'] = self.total
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('data') is not None:
            temp_model = GetTrackListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        return self


class GetTrackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrackListResponseBody = None,
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
            temp_model = GetTrackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrackListByMailFromAndTagNameRequest(TeaModel):
    def __init__(
        self,
        total: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        offset: str = None,
        page_size: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        page_number: str = None,
        account_name: str = None,
        tag_name: str = None,
    ):
        self.total = total
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.offset = offset
        self.page_size = page_size
        self.offset_create_time = offset_create_time
        self.offset_create_time_desc = offset_create_time_desc
        self.page_number = page_number
        self.account_name = account_name
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class GetTrackListByMailFromAndTagNameResponseBodyTrackListStat(TeaModel):
    def __init__(
        self,
        rcpt_click_rate: str = None,
        rcpt_unique_open_count: str = None,
        rcpt_click_count: str = None,
        rcpt_unique_click_count: str = None,
        create_time: str = None,
        rcpt_unique_open_rate: str = None,
        rcpt_unique_click_rate: str = None,
        total_number: str = None,
        rcpt_open_rate: str = None,
        rcpt_open_count: str = None,
    ):
        self.rcpt_click_rate = rcpt_click_rate
        self.rcpt_unique_open_count = rcpt_unique_open_count
        self.rcpt_click_count = rcpt_click_count
        self.rcpt_unique_click_count = rcpt_unique_click_count
        self.create_time = create_time
        self.rcpt_unique_open_rate = rcpt_unique_open_rate
        self.rcpt_unique_click_rate = rcpt_unique_click_rate
        self.total_number = total_number
        self.rcpt_open_rate = rcpt_open_rate
        self.rcpt_open_count = rcpt_open_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rcpt_click_rate is not None:
            result['RcptClickRate'] = self.rcpt_click_rate
        if self.rcpt_unique_open_count is not None:
            result['RcptUniqueOpenCount'] = self.rcpt_unique_open_count
        if self.rcpt_click_count is not None:
            result['RcptClickCount'] = self.rcpt_click_count
        if self.rcpt_unique_click_count is not None:
            result['RcptUniqueClickCount'] = self.rcpt_unique_click_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rcpt_unique_open_rate is not None:
            result['RcptUniqueOpenRate'] = self.rcpt_unique_open_rate
        if self.rcpt_unique_click_rate is not None:
            result['RcptUniqueClickRate'] = self.rcpt_unique_click_rate
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        if self.rcpt_open_rate is not None:
            result['RcptOpenRate'] = self.rcpt_open_rate
        if self.rcpt_open_count is not None:
            result['RcptOpenCount'] = self.rcpt_open_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RcptClickRate') is not None:
            self.rcpt_click_rate = m.get('RcptClickRate')
        if m.get('RcptUniqueOpenCount') is not None:
            self.rcpt_unique_open_count = m.get('RcptUniqueOpenCount')
        if m.get('RcptClickCount') is not None:
            self.rcpt_click_count = m.get('RcptClickCount')
        if m.get('RcptUniqueClickCount') is not None:
            self.rcpt_unique_click_count = m.get('RcptUniqueClickCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RcptUniqueOpenRate') is not None:
            self.rcpt_unique_open_rate = m.get('RcptUniqueOpenRate')
        if m.get('RcptUniqueClickRate') is not None:
            self.rcpt_unique_click_rate = m.get('RcptUniqueClickRate')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        if m.get('RcptOpenRate') is not None:
            self.rcpt_open_rate = m.get('RcptOpenRate')
        if m.get('RcptOpenCount') is not None:
            self.rcpt_open_count = m.get('RcptOpenCount')
        return self


class GetTrackListByMailFromAndTagNameResponseBodyTrackList(TeaModel):
    def __init__(
        self,
        stat: List[GetTrackListByMailFromAndTagNameResponseBodyTrackListStat] = None,
    ):
        self.stat = stat

    def validate(self):
        if self.stat:
            for k in self.stat:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Stat'] = []
        if self.stat is not None:
            for k in self.stat:
                result['Stat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stat = []
        if m.get('Stat') is not None:
            for k in m.get('Stat'):
                temp_model = GetTrackListByMailFromAndTagNameResponseBodyTrackListStat()
                self.stat.append(temp_model.from_map(k))
        return self


class GetTrackListByMailFromAndTagNameResponseBody(TeaModel):
    def __init__(
        self,
        offset_create_time: str = None,
        request_id: str = None,
        page_size: int = None,
        total: int = None,
        track_list: GetTrackListByMailFromAndTagNameResponseBodyTrackList = None,
        page_no: int = None,
        offset_create_time_desc: str = None,
    ):
        self.offset_create_time = offset_create_time
        self.request_id = request_id
        self.page_size = page_size
        self.total = total
        self.track_list = track_list
        self.page_no = page_no
        self.offset_create_time_desc = offset_create_time_desc

    def validate(self):
        if self.track_list:
            self.track_list.validate()

    def to_map(self):
        result = dict()
        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.track_list is not None:
            result['TrackList'] = self.track_list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TrackList') is not None:
            temp_model = GetTrackListByMailFromAndTagNameResponseBodyTrackList()
            self.track_list = temp_model.from_map(m['TrackList'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')
        return self


class GetTrackListByMailFromAndTagNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrackListByMailFromAndTagNameResponseBody = None,
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
            temp_model = GetTrackListByMailFromAndTagNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateMarketRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        version: str = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.version = version
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.version is not None:
            result['Version'] = self.version
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class MigrateMarketResponseBody(TeaModel):
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


class MigrateMarketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MigrateMarketResponseBody = None,
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
            temp_model = MigrateMarketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountNotificationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region: str = None,
        status: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyAccountNotificationResponseBody(TeaModel):
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


class ModifyAccountNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccountNotificationResponseBody = None,
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
            temp_model = ModifyAccountNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMailAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        mail_address_id: int = None,
        reply_address: str = None,
        password: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.mail_address_id = mail_address_id
        self.reply_address = reply_address
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('Password') is not None:
            self.password = m.get('Password')
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
        body: ModifyMailAddressResponseBody = None,
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
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyPWByDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPWByDomainResponseBody = None,
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
            temp_model = ModifyPWByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySenderAddressNotificationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sender_address_id: str = None,
        sender_address: str = None,
        region: str = None,
        status: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sender_address_id = sender_address_id
        self.sender_address = sender_address
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sender_address_id is not None:
            result['SenderAddressId'] = self.sender_address_id
        if self.sender_address is not None:
            result['SenderAddress'] = self.sender_address
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SenderAddressId') is not None:
            self.sender_address_id = m.get('SenderAddressId')
        if m.get('SenderAddress') is not None:
            self.sender_address = m.get('SenderAddress')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifySenderAddressNotificationResponseBody(TeaModel):
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


class ModifySenderAddressNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySenderAddressNotificationResponseBody = None,
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
            temp_model = ModifySenderAddressNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTagRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        body: ModifyTagResponseBody = None,
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
            temp_model = ModifyTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        template_name: str = None,
        template_subject: str = None,
        template_nick_name: str = None,
        template_text: str = None,
        sms_type: int = None,
        sms_content: str = None,
        remark: str = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id
        self.template_name = template_name
        self.template_subject = template_subject
        self.template_nick_name = template_nick_name
        self.template_text = template_text
        self.sms_type = sms_type
        self.sms_content = sms_content
        self.remark = remark
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject
        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name
        if self.template_text is not None:
            result['TemplateText'] = self.template_text
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')
        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')
        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
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
        body: ModifyTemplateResponseBody = None,
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
            temp_model = ModifyTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainByParamRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        key_word: str = None,
        status: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.key_word = key_word
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDomainByParamResponseBodyDataDomain(TeaModel):
    def __init__(
        self,
        domain_record: str = None,
        spf_auth_status: str = None,
        mx_auth_status: str = None,
        create_time: str = None,
        cname_auth_status: str = None,
        confirm_status: str = None,
        icp_status: str = None,
        utc_create_time: int = None,
        domain_status: str = None,
        domain_name: str = None,
        domain_id: str = None,
    ):
        self.domain_record = domain_record
        self.spf_auth_status = spf_auth_status
        self.mx_auth_status = mx_auth_status
        self.create_time = create_time
        self.cname_auth_status = cname_auth_status
        self.confirm_status = confirm_status
        self.icp_status = icp_status
        self.utc_create_time = utc_create_time
        self.domain_status = domain_status
        self.domain_name = domain_name
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_record is not None:
            result['DomainRecord'] = self.domain_record
        if self.spf_auth_status is not None:
            result['SpfAuthStatus'] = self.spf_auth_status
        if self.mx_auth_status is not None:
            result['MxAuthStatus'] = self.mx_auth_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cname_auth_status is not None:
            result['CnameAuthStatus'] = self.cname_auth_status
        if self.confirm_status is not None:
            result['ConfirmStatus'] = self.confirm_status
        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainRecord') is not None:
            self.domain_record = m.get('DomainRecord')
        if m.get('SpfAuthStatus') is not None:
            self.spf_auth_status = m.get('SpfAuthStatus')
        if m.get('MxAuthStatus') is not None:
            self.mx_auth_status = m.get('MxAuthStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CnameAuthStatus') is not None:
            self.cname_auth_status = m.get('CnameAuthStatus')
        if m.get('ConfirmStatus') is not None:
            self.confirm_status = m.get('ConfirmStatus')
        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
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
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        data: QueryDomainByParamResponseBodyData = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.page_number = page_number

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = QueryDomainByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QueryDomainByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDomainByParamResponseBody = None,
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
            temp_model = QueryDomainByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInvalidAddressRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        key_word: str = None,
        length: int = None,
        next_start: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.key_word = key_word
        self.length = length
        self.next_start = next_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.length is not None:
            result['Length'] = self.length
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
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
        total_count: int = None,
        request_id: str = None,
        data: QueryInvalidAddressResponseBodyData = None,
        next_start: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.data = data
        self.next_start = next_start

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = QueryInvalidAddressResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        return self


class QueryInvalidAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryInvalidAddressResponseBody = None,
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
            temp_model = QueryInvalidAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReceiverByParamRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        key_word: str = None,
        status: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.key_word = key_word
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryReceiverByParamResponseBodyDataReceiver(TeaModel):
    def __init__(
        self,
        receivers_alias: str = None,
        receivers_name: str = None,
        create_time: str = None,
        receiver_id: str = None,
        utc_create_time: int = None,
        receivers_status: str = None,
        count: str = None,
        desc: str = None,
    ):
        self.receivers_alias = receivers_alias
        self.receivers_name = receivers_name
        self.create_time = create_time
        self.receiver_id = receiver_id
        self.utc_create_time = utc_create_time
        self.receivers_status = receivers_status
        self.count = count
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.receivers_alias is not None:
            result['ReceiversAlias'] = self.receivers_alias
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.receivers_status is not None:
            result['ReceiversStatus'] = self.receivers_status
        if self.count is not None:
            result['Count'] = self.count
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiversAlias') is not None:
            self.receivers_alias = m.get('ReceiversAlias')
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('ReceiversStatus') is not None:
            self.receivers_status = m.get('ReceiversStatus')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
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
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        data: QueryReceiverByParamResponseBodyData = None,
        next_start: str = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.next_start = next_start

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = QueryReceiverByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        return self


class QueryReceiverByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryReceiverByParamResponseBody = None,
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
            temp_model = QueryReceiverByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReceiverDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        receiver_id: str = None,
        page_size: int = None,
        key_word: str = None,
        next_start: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.receiver_id = receiver_id
        self.page_size = page_size
        self.key_word = key_word
        self.next_start = next_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        return self


class QueryReceiverDetailResponseBodyDataDetail(TeaModel):
    def __init__(
        self,
        data: str = None,
        email: str = None,
        create_time: str = None,
        utc_create_time: int = None,
    ):
        self.data = data
        self.email = email
        self.create_time = create_time
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.email is not None:
            result['Email'] = self.email
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
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
        total_count: int = None,
        request_id: str = None,
        data: QueryReceiverDetailResponseBodyData = None,
        next_start: str = None,
    ):
        self.data_schema = data_schema
        self.total_count = total_count
        self.request_id = request_id
        self.data = data
        self.next_start = next_start

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.data_schema is not None:
            result['DataSchema'] = self.data_schema
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSchema') is not None:
            self.data_schema = m.get('DataSchema')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = QueryReceiverDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        return self


class QueryReceiverDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryReceiverDetailResponseBody = None,
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
            temp_model = QueryReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySignByParamRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        key_word: str = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.key_word = key_word
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class QuerySignByParamResponseBodyDataSign(TeaModel):
    def __init__(
        self,
        remark: str = None,
        audit_state: str = None,
        gmt_create: str = None,
        sign_id: int = None,
        sign_name: str = None,
        order_id: str = None,
        reject_info: str = None,
        sign_type: str = None,
    ):
        self.remark = remark
        self.audit_state = audit_state
        self.gmt_create = gmt_create
        self.sign_id = sign_id
        self.sign_name = sign_name
        self.order_id = order_id
        self.reject_info = reject_info
        self.sign_type = sign_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.audit_state is not None:
            result['AuditState'] = self.audit_state
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.sign_id is not None:
            result['SignId'] = self.sign_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('AuditState') is not None:
            self.audit_state = m.get('AuditState')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        return self


class QuerySignByParamResponseBodyData(TeaModel):
    def __init__(
        self,
        sign: List[QuerySignByParamResponseBodyDataSign] = None,
    ):
        self.sign = sign

    def validate(self):
        if self.sign:
            for k in self.sign:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['sign'] = []
        if self.sign is not None:
            for k in self.sign:
                result['sign'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sign = []
        if m.get('sign') is not None:
            for k in m.get('sign'):
                temp_model = QuerySignByParamResponseBodyDataSign()
                self.sign.append(temp_model.from_map(k))
        return self


class QuerySignByParamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        data: QuerySignByParamResponseBodyData = None,
        page_number: int = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.data = data
        self.page_number = page_number

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('data') is not None:
            temp_model = QuerySignByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QuerySignByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySignByParamResponseBody = None,
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
            temp_model = QuerySignByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsStatisticsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        end_time: str = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.end_time = end_time
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class QuerySmsStatisticsResponseBodyDataStat(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        faild_count: str = None,
        success_count: str = None,
        request_count: str = None,
    ):
        self.create_time = create_time
        self.faild_count = faild_count
        self.success_count = success_count
        self.request_count = request_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.faild_count is not None:
            result['faildCount'] = self.faild_count
        if self.success_count is not None:
            result['successCount'] = self.success_count
        if self.request_count is not None:
            result['requestCount'] = self.request_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('faildCount') is not None:
            self.faild_count = m.get('faildCount')
        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')
        if m.get('requestCount') is not None:
            self.request_count = m.get('requestCount')
        return self


class QuerySmsStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        stat: List[QuerySmsStatisticsResponseBodyDataStat] = None,
    ):
        self.stat = stat

    def validate(self):
        if self.stat:
            for k in self.stat:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = QuerySmsStatisticsResponseBodyDataStat()
                self.stat.append(temp_model.from_map(k))
        return self


class QuerySmsStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        data: QuerySmsStatisticsResponseBodyData = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = QuerySmsStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QuerySmsStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySmsStatisticsResponseBody = None,
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
            temp_model = QuerySmsStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagByParamRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        key_word: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.key_word = key_word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        return self


class QueryTagByParamResponseBodyDataTag(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
        tag_id: str = None,
    ):
        self.tag_name = tag_name
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
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
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        data: QueryTagByParamResponseBodyData = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.page_number = page_number

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = QueryTagByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QueryTagByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTagByParamResponseBody = None,
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
            temp_model = QueryTagByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskByParamRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        key_word: str = None,
        status: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.key_word = key_word
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryTaskByParamResponseBodyDataTask(TeaModel):
    def __init__(
        self,
        receivers_name: str = None,
        tag_name: str = None,
        task_status: str = None,
        create_time: str = None,
        request_count: str = None,
        address_type: str = None,
        utc_create_time: int = None,
        template_name: str = None,
        task_id: str = None,
    ):
        self.receivers_name = receivers_name
        self.tag_name = tag_name
        self.task_status = task_status
        self.create_time = create_time
        self.request_count = request_count
        self.address_type = address_type
        self.utc_create_time = utc_create_time
        self.template_name = template_name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        data: QueryTaskByParamResponseBodyData = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.page_number = page_number

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = QueryTaskByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QueryTaskByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTaskByParamResponseBody = None,
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
            temp_model = QueryTaskByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTemplateByParamRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        key_word: str = None,
        status: int = None,
        from_type: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.key_word = key_word
        self.status = status
        self.from_type = from_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.status is not None:
            result['Status'] = self.status
        if self.from_type is not None:
            result['FromType'] = self.from_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        return self


class QueryTemplateByParamResponseBodyDataTemplate(TeaModel):
    def __init__(
        self,
        template_comment: str = None,
        utc_createtime: int = None,
        smsrejectinfo: int = None,
        sms_template_code: int = None,
        create_time: str = None,
        template_status: str = None,
        template_type: int = None,
        template_name: str = None,
        sms_status: int = None,
        template_id: str = None,
    ):
        self.template_comment = template_comment
        self.utc_createtime = utc_createtime
        self.smsrejectinfo = smsrejectinfo
        self.sms_template_code = sms_template_code
        self.create_time = create_time
        self.template_status = template_status
        self.template_type = template_type
        self.template_name = template_name
        self.sms_status = sms_status
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_comment is not None:
            result['TemplateComment'] = self.template_comment
        if self.utc_createtime is not None:
            result['UtcCreatetime'] = self.utc_createtime
        if self.smsrejectinfo is not None:
            result['Smsrejectinfo'] = self.smsrejectinfo
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateComment') is not None:
            self.template_comment = m.get('TemplateComment')
        if m.get('UtcCreatetime') is not None:
            self.utc_createtime = m.get('UtcCreatetime')
        if m.get('Smsrejectinfo') is not None:
            self.smsrejectinfo = m.get('Smsrejectinfo')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
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
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        data: QueryTemplateByParamResponseBodyData = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.data = data
        self.page_number = page_number

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = QueryTemplateByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QueryTemplateByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTemplateByParamResponseBody = None,
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
            temp_model = QueryTemplateByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveReceiverDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        receiver_id: str = None,
        detail: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.receiver_id = receiver_id
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.detail is not None:
            result['Detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
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
        request_id: str = None,
        data: SaveReceiverDetailResponseBodyData = None,
        error_count: int = None,
        success_count: int = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_count = error_count
        self.success_count = success_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SaveReceiverDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class SaveReceiverDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveReceiverDetailResponseBody = None,
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
            temp_model = SaveReceiverDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SenderStatisticsByTagNameAndBatchIDRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        account_name: str = None,
        start_time: str = None,
        end_time: str = None,
        tag_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.account_name = account_name
        self.start_time = start_time
        self.end_time = end_time
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat(TeaModel):
    def __init__(
        self,
        unavailable_percent: str = None,
        create_time: str = None,
        succeeded_percent: str = None,
        faild_count: str = None,
        unavailable_count: str = None,
        success_count: str = None,
        request_count: str = None,
    ):
        self.unavailable_percent = unavailable_percent
        self.create_time = create_time
        self.succeeded_percent = succeeded_percent
        self.faild_count = faild_count
        self.unavailable_count = unavailable_count
        self.success_count = success_count
        self.request_count = request_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.unavailable_percent is not None:
            result['unavailablePercent'] = self.unavailable_percent
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.succeeded_percent is not None:
            result['succeededPercent'] = self.succeeded_percent
        if self.faild_count is not None:
            result['faildCount'] = self.faild_count
        if self.unavailable_count is not None:
            result['unavailableCount'] = self.unavailable_count
        if self.success_count is not None:
            result['successCount'] = self.success_count
        if self.request_count is not None:
            result['requestCount'] = self.request_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unavailablePercent') is not None:
            self.unavailable_percent = m.get('unavailablePercent')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('succeededPercent') is not None:
            self.succeeded_percent = m.get('succeededPercent')
        if m.get('faildCount') is not None:
            self.faild_count = m.get('faildCount')
        if m.get('unavailableCount') is not None:
            self.unavailable_count = m.get('unavailableCount')
        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')
        if m.get('requestCount') is not None:
            self.request_count = m.get('requestCount')
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
        total_count: int = None,
        request_id: str = None,
        data: SenderStatisticsByTagNameAndBatchIDResponseBodyData = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = SenderStatisticsByTagNameAndBatchIDResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class SenderStatisticsByTagNameAndBatchIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SenderStatisticsByTagNameAndBatchIDResponseBody = None,
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
            temp_model = SenderStatisticsByTagNameAndBatchIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SenderStatisticsDetailByParamRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        account_name: str = None,
        to_address: str = None,
        status: int = None,
        start_time: str = None,
        end_time: str = None,
        tag_name: str = None,
        length: int = None,
        next_start: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.account_name = account_name
        self.to_address = to_address
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.tag_name = tag_name
        self.length = length
        self.next_start = next_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.length is not None:
            result['Length'] = self.length
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        return self


class SenderStatisticsDetailByParamResponseBodyDataMailDetail(TeaModel):
    def __init__(
        self,
        status: int = None,
        last_update_time: str = None,
        message: str = None,
        to_address: str = None,
        utc_last_update_time: str = None,
        account_name: str = None,
    ):
        self.status = status
        self.last_update_time = last_update_time
        self.message = message
        self.to_address = to_address
        self.utc_last_update_time = utc_last_update_time
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.message is not None:
            result['Message'] = self.message
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.utc_last_update_time is not None:
            result['UtcLastUpdateTime'] = self.utc_last_update_time
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('UtcLastUpdateTime') is not None:
            self.utc_last_update_time = m.get('UtcLastUpdateTime')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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
        request_id: str = None,
        data: SenderStatisticsDetailByParamResponseBodyData = None,
        next_start: int = None,
    ):
        self.request_id = request_id
        self.data = data
        self.next_start = next_start

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.next_start is not None:
            result['NextStart'] = self.next_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = SenderStatisticsDetailByParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')
        return self


class SenderStatisticsDetailByParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SenderStatisticsDetailByParamResponseBody = None,
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
            temp_model = SenderStatisticsDetailByParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTestByTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        account_name: str = None,
        user_name: str = None,
        nick_name: str = None,
        birthday: str = None,
        gender: str = None,
        mobile: str = None,
        email: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_id = template_id
        self.account_name = account_name
        self.user_name = user_name
        self.nick_name = nick_name
        self.birthday = birthday
        self.gender = gender
        self.mobile = mobile
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class SendTestByTemplateResponseBody(TeaModel):
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


class SendTestByTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendTestByTemplateResponseBody = None,
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
            temp_model = SendTestByTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleSendMailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        account_name: str = None,
        address_type: int = None,
        tag_name: str = None,
        reply_to_address: bool = None,
        to_address: str = None,
        subject: str = None,
        html_body: str = None,
        text_body: str = None,
        from_alias: str = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        click_trace: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.account_name = account_name
        self.address_type = address_type
        self.tag_name = tag_name
        self.reply_to_address = reply_to_address
        self.to_address = to_address
        self.subject = subject
        self.html_body = html_body
        self.text_body = text_body
        self.from_alias = from_alias
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        self.click_trace = click_trace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.reply_to_address is not None:
            result['ReplyToAddress'] = self.reply_to_address
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.html_body is not None:
            result['HtmlBody'] = self.html_body
        if self.text_body is not None:
            result['TextBody'] = self.text_body
        if self.from_alias is not None:
            result['FromAlias'] = self.from_alias
        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address
        if self.reply_address_alias is not None:
            result['ReplyAddressAlias'] = self.reply_address_alias
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('ReplyToAddress') is not None:
            self.reply_to_address = m.get('ReplyToAddress')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('HtmlBody') is not None:
            self.html_body = m.get('HtmlBody')
        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')
        if m.get('FromAlias') is not None:
            self.from_alias = m.get('FromAlias')
        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')
        if m.get('ReplyAddressAlias') is not None:
            self.reply_address_alias = m.get('ReplyAddressAlias')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        return self


class SingleSendMailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        env_id: str = None,
    ):
        self.request_id = request_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class SingleSendMailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SingleSendMailResponseBody = None,
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
            temp_model = SingleSendMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleSendSmsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        template_code: str = None,
        rec_num: str = None,
        param_string: str = None,
        version: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name
        self.template_code = template_code
        self.rec_num = rec_num
        self.param_string = param_string
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.rec_num is not None:
            result['RecNum'] = self.rec_num
        if self.param_string is not None:
            result['ParamString'] = self.param_string
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('RecNum') is not None:
            self.rec_num = m.get('RecNum')
        if m.get('ParamString') is not None:
            self.param_string = m.get('ParamString')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class SingleSendSmsResponseBody(TeaModel):
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


class SingleSendSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SingleSendSmsResponseBody = None,
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
            temp_model = SingleSendSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDomainTrackNameRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        domain_id: int = None,
        cname_track_record: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.domain_id = domain_id
        self.cname_track_record = cname_track_record

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.cname_track_record is not None:
            result['CnameTrackRecord'] = self.cname_track_record
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('CnameTrackRecord') is not None:
            self.cname_track_record = m.get('CnameTrackRecord')
        return self


class UpdateDomainTrackNameResponseBody(TeaModel):
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


class UpdateDomainTrackNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDomainTrackNameResponseBody = None,
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
            temp_model = UpdateDomainTrackNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpProtectionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ip_protection: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.ip_protection = ip_protection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ip_protection is not None:
            result['IpProtection'] = self.ip_protection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('IpProtection') is not None:
            self.ip_protection = m.get('IpProtection')
        return self


class UpdateIpProtectionResponseBody(TeaModel):
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


class UpdateIpProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIpProtectionResponseBody = None,
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
            temp_model = UpdateIpProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMailAddressMsgCallBackUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        mail_from: str = None,
        notify_url: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.mail_from = mail_from
        self.notify_url = notify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.mail_from is not None:
            result['MailFrom'] = self.mail_from
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('MailFrom') is not None:
            self.mail_from = m.get('MailFrom')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        return self


class UpdateMailAddressMsgCallBackUrlResponseBody(TeaModel):
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


class UpdateMailAddressMsgCallBackUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMailAddressMsgCallBackUrlResponseBody = None,
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
            temp_model = UpdateMailAddressMsgCallBackUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


