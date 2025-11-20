# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, BinaryIO


class AddIpfilterRequest(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # IP Address/IP Range/IP Segment
        # 
        # This parameter is required.
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
        # ID corresponding to the IP
        self.ip_filter_id = ip_filter_id
        # Request ID
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
        # Email address Ticket credential, part of the string in the verification email\\"s URL.
        # 
        # This parameter is required.
        self.ticket = ticket

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
        # Request ID
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


class ApproveReplyMailAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApproveReplyMailAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ApproveReplyMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSendMailRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        click_trace: str = None,
        headers: str = None,
        ip_pool_id: str = None,
        owner_id: int = None,
        receivers_name: str = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_name: str = None,
        template_name: str = None,
        un_subscribe_filter_level: str = None,
        un_subscribe_link_type: str = None,
    ):
        # The sending address configured in the management console.
        # 
        # This parameter is required.
        self.account_name = account_name
        # - 0: Random account
        # - 1: Sending address
        # 
        # This parameter is required.
        self.address_type = address_type
        # - 1: Enable data tracking function
        # - 0 (default): Disable data tracking function
        self.click_trace = click_trace
        # Currently, the standard fields that can be added to the email header are Message-ID, List-Unsubscribe, and List-Unsubscribe-Post. Standard fields will overwrite the existing values in the email header, while non-standard fields must start with X-User- and will be appended to the email header. Currently, up to 10 headers can be passed in JSON format, and both standard and non-standard fields must comply with the syntax requirements for headers.
        self.headers = headers
        # dedicated IP pool ID. Users who have purchased an dedicated IP can use this parameter to specify the outgoing IP for this send operation.
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        # The name of the recipient list that has been created and uploaded with recipients. Note: The recipient list should not be deleted until at least 10 minutes after the task is triggered, otherwise it may cause sending failure.
        # 
        # This parameter is required.
        self.receivers_name = receivers_name
        # Reply address
        self.reply_address = reply_address
        # Alias for the reply address
        self.reply_address_alias = reply_address_alias
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Email tag name.
        self.tag_name = tag_name
        # The name of the template that has been created and approved in advance.
        # 
        # This parameter is required.
        self.template_name = template_name
        # Filtering level. Refer to the [Unsubscribe Function Link Generation and Filtering Mechanism](https://help.aliyun.com/document_detail/2689048.html) document.
        # - disabled: No filtering
        # - default: Use the default strategy, bulk addresses use sender address-level filtering
        # - mailfrom: Sender address-level filtering
        # - mailfrom_domain: Sender domain-level filtering
        # - edm_id: Account-level filtering
        self.un_subscribe_filter_level = un_subscribe_filter_level
        # The type of generated unsubscribe link. Refer to the [Unsubscribe Function Link Generation and Filtering Mechanism](https://help.aliyun.com/document_detail/2689048.html) document.
        # - disabled: Do not generate
        # - default: Use the default strategy: Generate an unsubscribe link when a bulk-type sending address sends to specific domains, such as those containing keywords like "gmail", "yahoo",
        # "google", "aol.com", "hotmail",
        # "outlook", "ymail.com", etc.
        # - zh-cn: Generate, for future content preparation
        # - en-us: Generate, for future content preparation
        self.un_subscribe_link_type = un_subscribe_link_type

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
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
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
        if self.un_subscribe_filter_level is not None:
            result['UnSubscribeFilterLevel'] = self.un_subscribe_filter_level
        if self.un_subscribe_link_type is not None:
            result['UnSubscribeLinkType'] = self.un_subscribe_link_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
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
        if m.get('UnSubscribeFilterLevel') is not None:
            self.un_subscribe_filter_level = m.get('UnSubscribeFilterLevel')
        if m.get('UnSubscribeLinkType') is not None:
            self.un_subscribe_link_type = m.get('UnSubscribeLinkType')
        return self


class BatchSendMailResponseBody(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        request_id: str = None,
    ):
        # Event ID
        self.env_id = env_id
        # Request ID
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


class ChangeDomainDkimRecordRequest(TeaModel):
    def __init__(
        self,
        dkim_rsa_length: int = None,
        domain: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dkim_rsa_length = dkim_rsa_length
        self.domain = domain
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
        if self.dkim_rsa_length is not None:
            result['DkimRsaLength'] = self.dkim_rsa_length
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DkimRsaLength') is not None:
            self.dkim_rsa_length = m.get('DkimRsaLength')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ChangeDomainDkimRecordResponseBody(TeaModel):
    def __init__(
        self,
        changed: bool = None,
        dkim_public_key: str = None,
        dkim_rsa_length: int = None,
        hostname: str = None,
        request_id: str = None,
    ):
        self.changed = changed
        self.dkim_public_key = dkim_public_key
        self.dkim_rsa_length = dkim_rsa_length
        self.hostname = hostname
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.changed is not None:
            result['Changed'] = self.changed
        if self.dkim_public_key is not None:
            result['DkimPublicKey'] = self.dkim_public_key
        if self.dkim_rsa_length is not None:
            result['DkimRsaLength'] = self.dkim_rsa_length
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Changed') is not None:
            self.changed = m.get('Changed')
        if m.get('DkimPublicKey') is not None:
            self.dkim_public_key = m.get('DkimPublicKey')
        if m.get('DkimRsaLength') is not None:
            self.dkim_rsa_length = m.get('DkimRsaLength')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeDomainDkimRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeDomainDkimRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ChangeDomainDkimRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDisposableRequest(TeaModel):
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


class CheckDisposableResponseBody(TeaModel):
    def __init__(
        self,
        is_disposable: str = None,
        is_format_valid: str = None,
        is_mx_valid: str = None,
        is_ok_to_send: str = None,
        request_id: str = None,
    ):
        self.is_disposable = is_disposable
        self.is_format_valid = is_format_valid
        self.is_mx_valid = is_mx_valid
        self.is_ok_to_send = is_ok_to_send
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_disposable is not None:
            result['IsDisposable'] = self.is_disposable
        if self.is_format_valid is not None:
            result['IsFormatValid'] = self.is_format_valid
        if self.is_mx_valid is not None:
            result['IsMxValid'] = self.is_mx_valid
        if self.is_ok_to_send is not None:
            result['IsOkToSend'] = self.is_ok_to_send
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDisposable') is not None:
            self.is_disposable = m.get('IsDisposable')
        if m.get('IsFormatValid') is not None:
            self.is_format_valid = m.get('IsFormatValid')
        if m.get('IsMxValid') is not None:
            self.is_mx_valid = m.get('IsMxValid')
        if m.get('IsOkToSend') is not None:
            self.is_ok_to_send = m.get('IsOkToSend')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDisposableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDisposableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckDisposableResponseBody()
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
        # Domain ID.
        # 
        # This parameter is required.
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
        domain_status: int = None,
        request_id: str = None,
    ):
        # Domain status. Indicates whether the verification was successful, with values as follows:
        # 
        # - **0**: Available, verified successfully
        # - **1**: Unavailable, verification failed
        self.domain_status = domain_status
        # Request ID
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


class CheckReplyToMailAddressRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        mail_address_id: int = None,
        owner_id: int = None,
        region: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Language.
        # 
        # en is English, and any other value or an empty value defaults to Chinese.
        self.lang = lang
        # Sender Address ID
        # 
        # This parameter is required.
        self.mail_address_id = mail_address_id
        self.owner_id = owner_id
        # Region
        self.region = region
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckReplyToMailAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID
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


class CheckReplyToMailAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckReplyToMailAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckReplyToMailAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSetCancelRelationFromAddressRequest(TeaModel):
    def __init__(
        self,
        from_address: str = None,
        id: str = None,
    ):
        self.from_address = from_address
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_address is not None:
            result['FromAddress'] = self.from_address
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromAddress') is not None:
            self.from_address = m.get('FromAddress')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ConfigSetCancelRelationFromAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ConfigSetCancelRelationFromAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigSetCancelRelationFromAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfigSetCancelRelationFromAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSetCreateRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        ip_pool_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.ip_pool_id = ip_pool_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ConfigSetCreateResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigSetCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigSetCreateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfigSetCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSetDeleteRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        is_force: bool = None,
    ):
        self.ids = ids
        self.is_force = is_force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.is_force is not None:
            result['IsForce'] = self.is_force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('IsForce') is not None:
            self.is_force = m.get('IsForce')
        return self


class ConfigSetDeleteResponseBody(TeaModel):
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


class ConfigSetDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigSetDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfigSetDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSetDetailRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ConfigSetDetailResponseBodyDetailIpPool(TeaModel):
    def __init__(
        self,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
    ):
        self.ip_pool_id = ip_pool_id
        self.ip_pool_name = ip_pool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')
        return self


class ConfigSetDetailResponseBodyDetail(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        ip_pool: ConfigSetDetailResponseBodyDetailIpPool = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.ip_pool = ip_pool
        self.name = name

    def validate(self):
        if self.ip_pool:
            self.ip_pool.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.ip_pool is not None:
            result['IpPool'] = self.ip_pool.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IpPool') is not None:
            temp_model = ConfigSetDetailResponseBodyDetailIpPool()
            self.ip_pool = temp_model.from_map(m['IpPool'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ConfigSetDetailResponseBody(TeaModel):
    def __init__(
        self,
        detail: ConfigSetDetailResponseBodyDetail = None,
        request_id: str = None,
    ):
        self.detail = detail
        self.request_id = request_id

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = ConfigSetDetailResponseBodyDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigSetDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigSetDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfigSetDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSetListRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        keyword: str = None,
        page_index: str = None,
        page_size: str = None,
    ):
        self.all = all
        self.keyword = keyword
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ConfigSetListResponseBodyConfigSetsIpPool(TeaModel):
    def __init__(
        self,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
    ):
        self.ip_pool_id = ip_pool_id
        self.ip_pool_name = ip_pool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')
        return self


class ConfigSetListResponseBodyConfigSets(TeaModel):
    def __init__(
        self,
        description: str = None,
        from_addresses: List[str] = None,
        id: str = None,
        ip_pool: ConfigSetListResponseBodyConfigSetsIpPool = None,
        name: str = None,
    ):
        self.description = description
        self.from_addresses = from_addresses
        self.id = id
        self.ip_pool = ip_pool
        self.name = name

    def validate(self):
        if self.ip_pool:
            self.ip_pool.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.from_addresses is not None:
            result['FromAddresses'] = self.from_addresses
        if self.id is not None:
            result['Id'] = self.id
        if self.ip_pool is not None:
            result['IpPool'] = self.ip_pool.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FromAddresses') is not None:
            self.from_addresses = m.get('FromAddresses')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IpPool') is not None:
            temp_model = ConfigSetListResponseBodyConfigSetsIpPool()
            self.ip_pool = temp_model.from_map(m['IpPool'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ConfigSetListResponseBody(TeaModel):
    def __init__(
        self,
        config_sets: List[ConfigSetListResponseBodyConfigSets] = None,
        current_page: int = None,
        has_more: bool = None,
        page_size: int = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.config_sets = config_sets
        self.current_page = current_page
        self.has_more = has_more
        self.page_size = page_size
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.config_sets:
            for k in self.config_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigSets'] = []
        if self.config_sets is not None:
            for k in self.config_sets:
                result['ConfigSets'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_sets = []
        if m.get('ConfigSets') is not None:
            for k in m.get('ConfigSets'):
                temp_model = ConfigSetListResponseBodyConfigSets()
                self.config_sets.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ConfigSetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigSetListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfigSetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSetRelationFromAddressRequest(TeaModel):
    def __init__(
        self,
        from_address: str = None,
        id: str = None,
    ):
        self.from_address = from_address
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_address is not None:
            result['FromAddress'] = self.from_address
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromAddress') is not None:
            self.from_address = m.get('FromAddress')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ConfigSetRelationFromAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ConfigSetRelationFromAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigSetRelationFromAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfigSetRelationFromAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSetUpdateRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        ip_pool_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.ip_pool_id = ip_pool_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ConfigSetUpdateResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigSetUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigSetUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfigSetUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dkim_selector: str = None,
    ):
        # Domain name, length 1-50, can include numbers, uppercase letters, lowercase letters, ., and -.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The selector field in the DKIM protocol, used to identify a specific public key. It is recommended to leave it blank, as the system will automatically generate it based on cluster information. If the user specifies it manually, for example, if the sending domain is "sub.example.com" and dkimSelector is set to "default", then the host record will be "default._domainkey.sub"
        # Constraints: 
        # 1. The length must not exceed 60 characters. 
        # 2. It must consist of visible characters only. 
        # 3. It cannot start with a hyphen (-). 
        # 4. It cannot end with a hyphen (-). 
        # 5. It cannot contain any of the following characters: _ :;/!*~.@#$%^&()+=[{]}|?<>,\\""
        self.dkim_selector = dkim_selector

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
        if self.dkim_selector is not None:
            result['dkimSelector'] = self.dkim_selector
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
        if m.get('dkimSelector') is not None:
            self.dkim_selector = m.get('dkimSelector')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        request_id: str = None,
    ):
        # Domain ID
        self.domain_id = domain_id
        # Request ID
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
        # Sender\\"s email address
        # 
        # This parameter is required.
        self.account_name = account_name
        self.owner_id = owner_id
        # Reply-to address
        self.reply_address = reply_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Type of sending. Values:
        # 
        # - batch: Bulk emails
        # 
        # - trigger: Triggered emails
        # 
        # This parameter is required.
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
        # Mail address ID
        self.mail_address_id = mail_address_id
        # Request ID
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
        # List description.
        self.desc = desc
        self.owner_id = owner_id
        # List alias, an email address less than 30 characters long.
        # 
        # This parameter is required.
        self.receivers_alias = receivers_alias
        # List name, must be unique, with a length of 1-30 characters.
        # 
        # This parameter is required.
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
        # Receiver list ID
        self.receiver_id = receiver_id
        # Request ID
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
        # Tag description
        self.tag_description = tag_description
        # Tag name. Limitations: 1-50 characters, allowing English letters, numbers, and underscores.
        # 
        # This parameter is required.
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
        # Request ID
        self.request_id = request_id
        # Tag ID
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


class CreateUserSuppressionRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Email address or domain name
        self.address = address
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
        if self.address is not None:
            result['Address'] = self.address
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateUserSuppressionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        suppression_id: str = None,
    ):
        # Request ID
        self.request_id = request_id
        # Invalid address number
        self.suppression_id = suppression_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.suppression_id is not None:
            result['SuppressionId'] = self.suppression_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuppressionId') is not None:
            self.suppression_id = m.get('SuppressionId')
        return self


class CreateUserSuppressionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserSuppressionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateUserSuppressionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DedicatedIpAutoRenewalRequest(TeaModel):
    def __init__(
        self,
        auto_renewal: str = None,
        buy_resource_ids: str = None,
    ):
        # Whether to enable auto-renewal
        # 
        # This parameter is required.
        self.auto_renewal = auto_renewal
        # Purchase instance ID, separated by English commas if multiple.
        # 
        # This parameter is required.
        self.buy_resource_ids = buy_resource_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.buy_resource_ids is not None:
            result['BuyResourceIds'] = self.buy_resource_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('BuyResourceIds') is not None:
            self.buy_resource_ids = m.get('BuyResourceIds')
        return self


class DedicatedIpAutoRenewalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID
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


class DedicatedIpAutoRenewalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DedicatedIpAutoRenewalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DedicatedIpAutoRenewalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DedicatedIpChangeWarmupTypeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        warmup_type: str = None,
    ):
        # Dedicated IP ID
        self.id = id
        # Warmup method
        self.warmup_type = warmup_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.warmup_type is not None:
            result['WarmupType'] = self.warmup_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('WarmupType') is not None:
            self.warmup_type = m.get('WarmupType')
        return self


class DedicatedIpChangeWarmupTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID
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


class DedicatedIpChangeWarmupTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DedicatedIpChangeWarmupTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DedicatedIpChangeWarmupTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DedicatedIpListRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # IP search keyword
        self.keyword = keyword
        # Pagination index, starting from 1
        self.page_index = page_index
        # Page size
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DedicatedIpListResponseBodyIpsIpExt(TeaModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        has_send_mail: bool = None,
        last_warm_up_type_changed_time: str = None,
    ):
        # Whether auto-renewal is enabled
        self.auto_renewal = auto_renewal
        # Whether an email has been sent
        self.has_send_mail = has_send_mail
        self.last_warm_up_type_changed_time = last_warm_up_type_changed_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.has_send_mail is not None:
            result['HasSendMail'] = self.has_send_mail
        if self.last_warm_up_type_changed_time is not None:
            result['LastWarmUpTypeChangedTime'] = self.last_warm_up_type_changed_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('HasSendMail') is not None:
            self.has_send_mail = m.get('HasSendMail')
        if m.get('LastWarmUpTypeChangedTime') is not None:
            self.last_warm_up_type_changed_time = m.get('LastWarmUpTypeChangedTime')
        return self


class DedicatedIpListResponseBodyIps(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        id: str = None,
        instance_id: str = None,
        ip: str = None,
        ip_ext: DedicatedIpListResponseBodyIpsIpExt = None,
        ip_pool_name: str = None,
        start_time: str = None,
        status: str = None,
        warmup_status: str = None,
        warmup_type: str = None,
        zone_id: str = None,
    ):
        # Expiration time
        self.expired_time = expired_time
        # IP ID, consistent with the purchased instance ID
        self.id = id
        # Purchased instance ID
        self.instance_id = instance_id
        # IP address
        self.ip = ip
        # Extended information
        self.ip_ext = ip_ext
        # Name of the IP pool
        self.ip_pool_name = ip_pool_name
        # Purchase time
        self.start_time = start_time
        # IP status
        self.status = status
        # Warm-up status
        self.warmup_status = warmup_status
        # Warm-up method
        self.warmup_type = warmup_type
        self.zone_id = zone_id

    def validate(self):
        if self.ip_ext:
            self.ip_ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_ext is not None:
            result['IpExt'] = self.ip_ext.to_map()
        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.warmup_status is not None:
            result['WarmupStatus'] = self.warmup_status
        if self.warmup_type is not None:
            result['WarmupType'] = self.warmup_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpExt') is not None:
            temp_model = DedicatedIpListResponseBodyIpsIpExt()
            self.ip_ext = temp_model.from_map(m['IpExt'])
        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WarmupStatus') is not None:
            self.warmup_status = m.get('WarmupStatus')
        if m.get('WarmupType') is not None:
            self.warmup_type = m.get('WarmupType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DedicatedIpListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        has_more: bool = None,
        ips: List[DedicatedIpListResponseBodyIps] = None,
        page_size: int = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # Current page
        self.current_page = current_page
        # Whether there is a next page
        self.has_more = has_more
        # IP list
        self.ips = ips
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total amount of purchased IP data
        self.total_counts = total_counts

    def validate(self):
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['Ips'] = []
        if self.ips is not None:
            for k in self.ips:
                result['Ips'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.ips = []
        if m.get('Ips') is not None:
            for k in m.get('Ips'):
                temp_model = DedicatedIpListResponseBodyIps()
                self.ips.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class DedicatedIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DedicatedIpListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DedicatedIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DedicatedIpNonePoolListResponseBodyIps(TeaModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        zone_id: str = None,
    ):
        # Purchased instance ID
        self.id = id
        # IP address
        self.ip = ip
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DedicatedIpNonePoolListResponseBody(TeaModel):
    def __init__(
        self,
        ips: List[DedicatedIpNonePoolListResponseBodyIps] = None,
        request_id: str = None,
    ):
        # Information on IPs not added to the IP pool
        self.ips = ips
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Ips'] = []
        if self.ips is not None:
            for k in self.ips:
                result['Ips'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ips = []
        if m.get('Ips') is not None:
            for k in m.get('Ips'):
                temp_model = DedicatedIpNonePoolListResponseBodyIps()
                self.ips.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DedicatedIpNonePoolListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DedicatedIpNonePoolListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DedicatedIpNonePoolListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DedicatedIpPoolCreateRequest(TeaModel):
    def __init__(
        self,
        buy_resource_ids: str = None,
        name: str = None,
    ):
        # Purchased IP instance IDs, separated by commas; derived from the IP purchase instance IDs returned by the DedicatedIpNonePoolList interface.
        self.buy_resource_ids = buy_resource_ids
        # IP pool name;
        # Length should be 1-50 characters, allowing English letters, numbers, _, and -. The name cannot be modified after the IP pool is created.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_resource_ids is not None:
            result['BuyResourceIds'] = self.buy_resource_ids
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResourceIds') is not None:
            self.buy_resource_ids = m.get('BuyResourceIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DedicatedIpPoolCreateResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # IP pool ID
        self.id = id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DedicatedIpPoolCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DedicatedIpPoolCreateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DedicatedIpPoolCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DedicatedIpPoolDeleteRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DedicatedIpPoolDeleteResponseBody(TeaModel):
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


class DedicatedIpPoolDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DedicatedIpPoolDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DedicatedIpPoolDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DedicatedIpPoolListRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        keyword: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.all = all
        # Search keyword for the name
        self.keyword = keyword
        # Page index, starting from 1
        self.page_index = page_index
        # Number of items per page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DedicatedIpPoolListResponseBodyIpPoolsIps(TeaModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        zone_id: str = None,
    ):
        # Instance purchase ID
        self.id = id
        # IP address
        self.ip = ip
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DedicatedIpPoolListResponseBodyIpPools(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        ip_count: int = None,
        ips: List[DedicatedIpPoolListResponseBodyIpPoolsIps] = None,
        name: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # IP pool ID
        self.id = id
        # Number of source IP addresses
        self.ip_count = ip_count
        # List of IPs
        self.ips = ips
        # IP pool name
        self.name = name

    def validate(self):
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        result['Ips'] = []
        if self.ips is not None:
            for k in self.ips:
                result['Ips'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        self.ips = []
        if m.get('Ips') is not None:
            for k in m.get('Ips'):
                temp_model = DedicatedIpPoolListResponseBodyIpPoolsIps()
                self.ips.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DedicatedIpPoolListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        has_more: bool = None,
        ip_pools: List[DedicatedIpPoolListResponseBodyIpPools] = None,
        page_size: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # Current page
        self.current_page = current_page
        # Whether there is a next page
        self.has_more = has_more
        # List of IP pools
        self.ip_pools = ip_pools
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total number of data under the current request conditions
        self.total_counts = total_counts

    def validate(self):
        if self.ip_pools:
            for k in self.ip_pools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['IpPools'] = []
        if self.ip_pools is not None:
            for k in self.ip_pools:
                result['IpPools'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.ip_pools = []
        if m.get('IpPools') is not None:
            for k in m.get('IpPools'):
                temp_model = DedicatedIpPoolListResponseBodyIpPools()
                self.ip_pools.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class DedicatedIpPoolListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DedicatedIpPoolListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DedicatedIpPoolListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DedicatedIpPoolUpdateRequest(TeaModel):
    def __init__(
        self,
        buy_resource_ids: str = None,
        id: str = None,
        update_resource: bool = None,
    ):
        # Purchased IP instance IDs, separated by commas; sourced from the DedicatedIpNonePoolList API\\"s returned IP purchase instance IDs
        self.buy_resource_ids = buy_resource_ids
        # IP pool ID
        self.id = id
        # Whether to change the associated IP, enter true
        self.update_resource = update_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_resource_ids is not None:
            result['BuyResourceIds'] = self.buy_resource_ids
        if self.id is not None:
            result['Id'] = self.id
        if self.update_resource is not None:
            result['UpdateResource'] = self.update_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResourceIds') is not None:
            self.buy_resource_ids = m.get('BuyResourceIds')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UpdateResource') is not None:
            self.update_resource = m.get('UpdateResource')
        return self


class DedicatedIpPoolUpdateResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # IP pool ID
        self.id = id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DedicatedIpPoolUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DedicatedIpPoolUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DedicatedIpPoolUpdateResponseBody()
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
        # Domain ID.
        # 
        # This parameter is required.
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
        # Request ID.
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
        # Target address
        self.to_address = to_address

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
        # Request ID
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


class DeleteInvalidAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInvalidAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteInvalidAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpfilterByEdmIdRequest(TeaModel):
    def __init__(
        self,
        from_type: int = None,
        id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Deprecated, kept for historical compatibility.
        self.from_type = from_type
        # Record ID
        self.id = id
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
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteIpfilterByEdmIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID.
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


class DeleteIpfilterByEdmIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpfilterByEdmIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteIpfilterByEdmIdResponseBody()
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
        # Mail Address ID
        # 
        # This parameter is required.
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
        # Request ID
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
        # Receiver list ID
        # 
        # This parameter is required.
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
        # Request ID
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
        # The single recipient to be deleted from the recipient list
        self.email = email
        self.owner_id = owner_id
        # Recipient list ID
        # 
        # This parameter is required.
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
        # Request ID
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
        # The ID of the tag
        # 
        # This parameter is required.
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
        # Request ID
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


class DeleteValidateFileRequest(TeaModel):
    def __init__(
        self,
        file_id: str = None,
    ):
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class DeleteValidateFileResponseBody(TeaModel):
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


class DeleteValidateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteValidateFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteValidateFileResponseBody()
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
        daily_remain_free_quota: int = None,
        dayu_status: int = None,
        domains: int = None,
        enable_times: int = None,
        ip_channel_type: str = None,
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
        # Daily quota
        self.daily_quota = daily_quota
        # remaining amount of daily free quota
        self.daily_remain_free_quota = daily_remain_free_quota
        # Dayu status (deprecated, retained for compatibility reasons.)
        self.dayu_status = dayu_status
        # Number of domains
        self.domains = domains
        # Effective time
        self.enable_times = enable_times
        self.ip_channel_type = ip_channel_type
        # Number of sending addresses
        self.mail_addresses = mail_addresses
        # Maximum level
        self.max_quota_level = max_quota_level
        # Monthly quota
        self.month_quota = month_quota
        # Credit level
        self.quota_level = quota_level
        # Number of recipients
        self.receivers = receivers
        # Remaining amount of total free quota
        self.remain_free_quota = remain_free_quota
        # Request ID
        self.request_id = request_id
        # Deprecated, retained for compatibility reasons.
        self.sms_record = sms_record
        # Deprecated, retained for compatibility reasons.
        self.sms_sign = sms_sign
        # Deprecated, retained for compatibility reasons.
        self.sms_templates = sms_templates
        # Number of tags
        self.tags = tags
        # Number of templates
        self.templates = templates
        # User status:
        # 1 Frozen
        # 2 In arrears
        # 4 Restricted from sending
        # 8 Logically deleted
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
        if self.daily_remain_free_quota is not None:
            result['DailyRemainFreeQuota'] = self.daily_remain_free_quota
        if self.dayu_status is not None:
            result['DayuStatus'] = self.dayu_status
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.enable_times is not None:
            result['EnableTimes'] = self.enable_times
        if self.ip_channel_type is not None:
            result['IpChannelType'] = self.ip_channel_type
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
        if m.get('DailyRemainFreeQuota') is not None:
            self.daily_remain_free_quota = m.get('DailyRemainFreeQuota')
        if m.get('DayuStatus') is not None:
            self.dayu_status = m.get('DayuStatus')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('EnableTimes') is not None:
            self.enable_times = m.get('EnableTimes')
        if m.get('IpChannelType') is not None:
            self.ip_channel_type = m.get('IpChannelType')
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
        # Domain ID. Can be obtained through QueryDomainByParam.
        # 
        # This parameter is required.
        self.domain_id = domain_id
        self.owner_id = owner_id
        # Determines whether to perform real-time DNS resolution
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
        dkim_rsa_length: int = None,
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
        # CNAME verification flag, 0 for success, 1 for failure.
        self.cname_auth_status = cname_auth_status
        # Indicates whether the CNAME host record has been modified, 1 for modified (reverting to the original value also counts as modification), 0 for not modified.
        self.cname_confirm_status = cname_confirm_status
        # Custom part of the CNAME host record
        self.cname_record = cname_record
        # Creation time
        self.create_time = create_time
        # Whether it is the default domain,
        # 
        # Value: 0 No (this field is deprecated)
        self.default_domain = default_domain
        # DKIM verification flag, indicating whether the DKIM record set by the user in DNS has passed validation, 0: Passed, 1: Not passed
        self.dkim_auth_status = dkim_auth_status
        # DKIM public key value, the value that users need to set for the DKIM record in DNS
        self.dkim_public_key = dkim_public_key
        # DKIM host record, the key that the user needs to set in the DNS for the DKIM record
        self.dkim_rr = dkim_rr
        self.dkim_rsa_length = dkim_rsa_length
        # DMARC verification flag, indicating whether the DMARC record set by the user in DNS has passed validation, 0: Passed, 1: Not passed
        self.dmarc_auth_status = dmarc_auth_status
        # DMARC host record value
        self.dmarc_host_record = dmarc_host_record
        # DMARC record value
        self.dmarc_record = dmarc_record
        # DMARC record value resolved through the public domain name
        self.dns_dmarc = dns_dmarc
        # MX record value resolved from the public network domain
        self.dns_mx = dns_mx
        # SPF record value resolved from the public network domain
        self.dns_spf = dns_spf
        # Ownership record value resolved from the public network domain
        self.dns_txt = dns_txt
        # Domain ID
        self.domain_id = domain_id
        # Domain name
        self.domain_name = domain_name
        # Domain status. Indicates whether the verification was successful, with values:
        # 
        # - **0**: Available, verified successfully
        # - **1**: Unavailable, verification failed
        self.domain_status = domain_status
        # Ownership record provided by the email push console
        self.domain_type = domain_type
        # Host record
        self.host_record = host_record
        # Filing status. **1** indicates filed, **0** indicates not filed.
        self.icp_status = icp_status
        # MX verification flag, 0 for success, 1 for failure.
        self.mx_auth_status = mx_auth_status
        # MX record value provided by the email push console
        self.mx_record = mx_record
        # Request ID
        self.request_id = request_id
        # SPF verification flag, 0 for success, 1 for failure.
        self.spf_auth_status = spf_auth_status
        # SPF record value provided by the email push console
        self.spf_record = spf_record
        # SPF record. Previously, the SPF display content needed to be calculated by the calling end based on the spfRecord in the response. The new field spfRecordV2 replaces spfRecord, and the calling end can directly display this field after obtaining it;
        self.spf_record_v2 = spf_record_v2
        # Primary domain
        self.tl_domain_name = tl_domain_name
        # CNAME record value provided by the email push console
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
        if self.dkim_rsa_length is not None:
            result['DkimRsaLength'] = self.dkim_rsa_length
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
        if m.get('DkimRsaLength') is not None:
            self.dkim_rsa_length = m.get('DkimRsaLength')
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
        # This parameter is required.
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


class GetDedicatedIpWarmUpDetailRequest(TeaModel):
    def __init__(
        self,
        dedicated_ip: str = None,
        end_day_mark: int = None,
        esp: str = None,
        start_day_mark: int = None,
    ):
        self.dedicated_ip = dedicated_ip
        self.end_day_mark = end_day_mark
        self.esp = esp
        self.start_day_mark = start_day_mark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip
        if self.end_day_mark is not None:
            result['EndDayMark'] = self.end_day_mark
        if self.esp is not None:
            result['Esp'] = self.esp
        if self.start_day_mark is not None:
            result['StartDayMark'] = self.start_day_mark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')
        if m.get('EndDayMark') is not None:
            self.end_day_mark = m.get('EndDayMark')
        if m.get('Esp') is not None:
            self.esp = m.get('Esp')
        if m.get('StartDayMark') is not None:
            self.start_day_mark = m.get('StartDayMark')
        return self


class GetDedicatedIpWarmUpDetailResponseBodyDetail(TeaModel):
    def __init__(
        self,
        day_mark: int = None,
        deliver_counts: int = None,
        esp: str = None,
        send_counts: int = None,
    ):
        self.day_mark = day_mark
        self.deliver_counts = deliver_counts
        self.esp = esp
        self.send_counts = send_counts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_mark is not None:
            result['DayMark'] = self.day_mark
        if self.deliver_counts is not None:
            result['DeliverCounts'] = self.deliver_counts
        if self.esp is not None:
            result['Esp'] = self.esp
        if self.send_counts is not None:
            result['SendCounts'] = self.send_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayMark') is not None:
            self.day_mark = m.get('DayMark')
        if m.get('DeliverCounts') is not None:
            self.deliver_counts = m.get('DeliverCounts')
        if m.get('Esp') is not None:
            self.esp = m.get('Esp')
        if m.get('SendCounts') is not None:
            self.send_counts = m.get('SendCounts')
        return self


class GetDedicatedIpWarmUpDetailResponseBody(TeaModel):
    def __init__(
        self,
        detail: List[GetDedicatedIpWarmUpDetailResponseBodyDetail] = None,
        request_id: str = None,
    ):
        self.detail = detail
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = GetDedicatedIpWarmUpDetailResponseBodyDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDedicatedIpWarmUpDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDedicatedIpWarmUpDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetDedicatedIpWarmUpDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDedicatedIpWarmUpInfoRequest(TeaModel):
    def __init__(
        self,
        dedicated_ip: str = None,
    ):
        self.dedicated_ip = dedicated_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')
        return self


class GetDedicatedIpWarmUpInfoResponseBodyInfo(TeaModel):
    def __init__(
        self,
        esp: str = None,
        finished: bool = None,
    ):
        self.esp = esp
        self.finished = finished

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esp is not None:
            result['Esp'] = self.esp
        if self.finished is not None:
            result['Finished'] = self.finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Esp') is not None:
            self.esp = m.get('Esp')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        return self


class GetDedicatedIpWarmUpInfoResponseBody(TeaModel):
    def __init__(
        self,
        info: List[GetDedicatedIpWarmUpInfoResponseBodyInfo] = None,
        request_id: str = None,
    ):
        self.info = info
        self.request_id = request_id

    def validate(self):
        if self.info:
            for k in self.info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Info'] = []
        if self.info is not None:
            for k in self.info:
                result['Info'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info = []
        if m.get('Info') is not None:
            for k in m.get('Info'):
                temp_model = GetDedicatedIpWarmUpInfoResponseBodyInfo()
                self.info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDedicatedIpWarmUpInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDedicatedIpWarmUpInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetDedicatedIpWarmUpInfoResponseBody()
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


class GetIpProtectionResponseBody(TeaModel):
    def __init__(
        self,
        ip_protection: str = None,
        request_id: str = None,
    ):
        # IP protection switch, On: 1 Off: 0
        self.ip_protection = ip_protection
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protection is not None:
            result['IpProtection'] = self.ip_protection
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtection') is not None:
            self.ip_protection = m.get('IpProtection')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIpProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIpProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetIpProtectionResponseBody()
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


class GetIpfilterListResponseBodyDataIpfilters(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        ip_address: str = None,
    ):
        # timestamp
        self.create_time = create_time
        # Record ID
        self.id = id
        # IP address/IP range/IP segment
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: GetIpfilterListResponseBodyData = None,
    ):
        # Current page number
        self.page_number = page_number
        # Number of items per page
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Data records
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
            temp_model = GetIpfilterListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetIpfilterListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIpfilterListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetIpfilterListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSuppressionListLevelRequest(TeaModel):
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


class GetSuppressionListLevelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        suppression_list_level: str = None,
    ):
        self.request_id = request_id
        self.suppression_list_level = suppression_list_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.suppression_list_level is not None:
            result['SuppressionListLevel'] = self.suppression_list_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuppressionListLevel') is not None:
            self.suppression_list_level = m.get('SuppressionListLevel')
        return self


class GetSuppressionListLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSuppressionListLevelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetSuppressionListLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrackListRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        config_set_id: str = None,
        dedicated_ip: str = None,
        dedicated_ip_pool_id: str = None,
        end_time: str = None,
        esp: str = None,
        offset: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        owner_id: int = None,
        page_number: str = None,
        page_size: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag_name: str = None,
        total: str = None,
    ):
        # Sender address.
        # 
        # > If not filled, it represents all addresses; if TagName is provided, this parameter must not be empty.
        self.account_name = account_name
        self.config_set_id = config_set_id
        self.dedicated_ip = dedicated_ip
        self.dedicated_ip_pool_id = dedicated_ip_pool_id
        # End time, the span between start and end time cannot exceed 7 days. Format: yyyy-MM-dd.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.esp = esp
        # For the first query, set to 0; for subsequent queries, fixed at 1. 1 indicates pagination in ascending order by time. (This field is deprecated)
        self.offset = offset
        # Used for pagination. Not set for the first query, but for subsequent queries, it should be set to the value of OffsetCreateTime from the previous response. (This field is deprecated)
        self.offset_create_time = offset_create_time
        # (This field is deprecated)
        self.offset_create_time_desc = offset_create_time_desc
        self.owner_id = owner_id
        # Page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time, which cannot be earlier than 30 days. Format: yyyy-MM-dd.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Tag name
        self.tag_name = tag_name
        # (This field is deprecated)
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id
        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip
        if self.dedicated_ip_pool_id is not None:
            result['DedicatedIpPoolId'] = self.dedicated_ip_pool_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.esp is not None:
            result['Esp'] = self.esp
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
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')
        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')
        if m.get('DedicatedIpPoolId') is not None:
            self.dedicated_ip_pool_id = m.get('DedicatedIpPoolId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Esp') is not None:
            self.esp = m.get('Esp')
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
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTrackListResponseBodyDataStat(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        rcpt_click_count: str = None,
        rcpt_click_rate: str = None,
        rcpt_open_count: str = None,
        rcpt_open_rate: str = None,
        rcpt_unique_click_count: str = None,
        rcpt_unique_click_rate: str = None,
        rcpt_unique_open_count: str = None,
        rcpt_unique_open_rate: str = None,
        total_number: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # Click count
        self.rcpt_click_count = rcpt_click_count
        # Click rate
        self.rcpt_click_rate = rcpt_click_rate
        # Number of Opens
        self.rcpt_open_count = rcpt_open_count
        # Open rate
        self.rcpt_open_rate = rcpt_open_rate
        # Unique click count
        self.rcpt_unique_click_count = rcpt_unique_click_count
        # Unique click rate
        self.rcpt_unique_click_rate = rcpt_unique_click_rate
        # Unique open count
        self.rcpt_unique_open_count = rcpt_unique_open_count
        # Unique open rate
        self.rcpt_unique_open_rate = rcpt_unique_open_rate
        # Total number
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
        total_pages: int = None,
        data: GetTrackListResponseBodyData = None,
    ):
        # Used for pagination. Not set for the first query, but for subsequent queries, it should be set to the value of OffsetCreateTime from the previous response. (This field is deprecated)
        self.offset_create_time = offset_create_time
        # (This field is deprecated)
        self.offset_create_time_desc = offset_create_time_desc
        # Current page number
        self.page_no = page_no
        # Number of items per page
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total number of items
        self.total = total
        self.total_pages = total_pages
        # Tracking data records
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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
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
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
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


class GetTrackListByMailFromAndTagNameRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        config_set_id: str = None,
        dedicated_ip: str = None,
        dedicated_ip_pool_id: str = None,
        end_time: str = None,
        esp: str = None,
        offset: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        owner_id: int = None,
        page_number: str = None,
        page_size: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag_name: str = None,
        total: str = None,
    ):
        # Sender address.
        # 
        # > If not filled, it represents all addresses; if there is a TagName, this parameter must not be empty.
        self.account_name = account_name
        self.config_set_id = config_set_id
        self.dedicated_ip = dedicated_ip
        self.dedicated_ip_pool_id = dedicated_ip_pool_id
        # End time, with a span from the start time that cannot exceed 15 days. Format: yyyy-MM-dd.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.esp = esp
        # For the first query, set to 0; for subsequent queries, fixed at 1. 1 indicates pagination in ascending order by time. (This field is deprecated)
        self.offset = offset
        # Used for pagination. Not set for the first query; for subsequent queries, set to the value of OffsetCreateTime from the previous response. (This field is deprecated)
        self.offset_create_time = offset_create_time
        # (This field is deprecated)
        self.offset_create_time_desc = offset_create_time_desc
        self.owner_id = owner_id
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time, which cannot be earlier than 30 days. Format: yyyy-MM-dd.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Email tag. If not filled, it represents all tags.
        self.tag_name = tag_name
        # (This field is deprecated)
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id
        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip
        if self.dedicated_ip_pool_id is not None:
            result['DedicatedIpPoolId'] = self.dedicated_ip_pool_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.esp is not None:
            result['Esp'] = self.esp
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
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')
        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')
        if m.get('DedicatedIpPoolId') is not None:
            self.dedicated_ip_pool_id = m.get('DedicatedIpPoolId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Esp') is not None:
            self.esp = m.get('Esp')
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
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTrackListByMailFromAndTagNameResponseBodyTrackListStat(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        rcpt_click_count: str = None,
        rcpt_click_rate: str = None,
        rcpt_open_count: str = None,
        rcpt_open_rate: str = None,
        rcpt_unique_click_count: str = None,
        rcpt_unique_click_rate: str = None,
        rcpt_unique_open_count: str = None,
        rcpt_unique_open_rate: str = None,
        total_number: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # Click count
        self.rcpt_click_count = rcpt_click_count
        # Click rate
        self.rcpt_click_rate = rcpt_click_rate
        # Number of opens
        self.rcpt_open_count = rcpt_open_count
        # Open rate
        self.rcpt_open_rate = rcpt_open_rate
        # Unique click count
        self.rcpt_unique_click_count = rcpt_unique_click_count
        # Unique click rate
        self.rcpt_unique_click_rate = rcpt_unique_click_rate
        # Unique open count
        self.rcpt_unique_open_count = rcpt_unique_open_count
        # Unique open rate
        self.rcpt_unique_open_rate = rcpt_unique_open_rate
        # Total number
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        offset_create_time_desc: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        total_pages: str = None,
        track_list: GetTrackListByMailFromAndTagNameResponseBodyTrackList = None,
    ):
        # Used for pagination. Not set for the first query; for subsequent queries, set to the value of OffsetCreateTime from the previous response. (This field is deprecated)
        self.offset_create_time = offset_create_time
        # (This field is deprecated)
        self.offset_create_time_desc = offset_create_time_desc
        # Current page number
        self.page_no = page_no
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # (This field is deprecated)
        self.total = total
        self.total_pages = total_pages
        # Tracking data records
        self.track_list = track_list

    def validate(self):
        if self.track_list:
            self.track_list.validate()

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.track_list is not None:
            result['TrackList'] = self.track_list.to_map()
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
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TrackList') is not None:
            temp_model = GetTrackListByMailFromAndTagNameResponseBodyTrackList()
            self.track_list = temp_model.from_map(m['TrackList'])
        return self


class GetTrackListByMailFromAndTagNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrackListByMailFromAndTagNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetTrackListByMailFromAndTagNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(
        self,
        enable_eventbridge: bool = None,
    ):
        # Whether EventBridge is enabled
        self.enable_eventbridge = enable_eventbridge

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_eventbridge is not None:
            result['EnableEventbridge'] = self.enable_eventbridge
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableEventbridge') is not None:
            self.enable_eventbridge = m.get('EnableEventbridge')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        data: GetUserResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned Content
        self.data = data
        # Request ID
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetValidateFileRequest(TeaModel):
    def __init__(
        self,
        file_id: str = None,
    ):
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class GetValidateFileResponseBody(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        request_id: str = None,
    ):
        self.file_url = file_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetValidateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetValidateFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetValidateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetValidateFileStatusRequest(TeaModel):
    def __init__(
        self,
        file_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class GetValidateFileStatusResponseBody(TeaModel):
    def __init__(
        self,
        catch_all_num: str = None,
        complete_time: str = None,
        do_not_mail_num: str = None,
        file_name: str = None,
        invalid_num: str = None,
        percentage: str = None,
        processed_num: str = None,
        request_id: str = None,
        status: str = None,
        total_num: str = None,
        unknown_num: str = None,
        upload_time: str = None,
        valid_num: str = None,
    ):
        self.catch_all_num = catch_all_num
        self.complete_time = complete_time
        self.do_not_mail_num = do_not_mail_num
        self.file_name = file_name
        self.invalid_num = invalid_num
        self.percentage = percentage
        self.processed_num = processed_num
        self.request_id = request_id
        self.status = status
        self.total_num = total_num
        self.unknown_num = unknown_num
        self.upload_time = upload_time
        self.valid_num = valid_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catch_all_num is not None:
            result['CatchAllNum'] = self.catch_all_num
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.do_not_mail_num is not None:
            result['DoNotMailNum'] = self.do_not_mail_num
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.invalid_num is not None:
            result['InvalidNum'] = self.invalid_num
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.processed_num is not None:
            result['ProcessedNum'] = self.processed_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.unknown_num is not None:
            result['UnknownNum'] = self.unknown_num
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        if self.valid_num is not None:
            result['ValidNum'] = self.valid_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatchAllNum') is not None:
            self.catch_all_num = m.get('CatchAllNum')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('DoNotMailNum') is not None:
            self.do_not_mail_num = m.get('DoNotMailNum')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('InvalidNum') is not None:
            self.invalid_num = m.get('InvalidNum')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('ProcessedNum') is not None:
            self.processed_num = m.get('ProcessedNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('UnknownNum') is not None:
            self.unknown_num = m.get('UnknownNum')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        if m.get('ValidNum') is not None:
            self.valid_num = m.get('ValidNum')
        return self


class GetValidateFileStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetValidateFileStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetValidateFileStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetValidationQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_quota: int = None,
        used_quota: int = None,
    ):
        self.request_id = request_id
        self.total_quota = total_quota
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')
        return self


class GetValidationQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetValidationQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetValidationQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBlockSendingRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        block_email: str = None,
        block_type: str = None,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        sender_email: str = None,
    ):
        self.begin_time = begin_time
        self.block_email = block_email
        # This parameter is required.
        self.block_type = block_type
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.sender_email = sender_email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.block_email is not None:
            result['BlockEmail'] = self.block_email
        if self.block_type is not None:
            result['BlockType'] = self.block_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sender_email is not None:
            result['SenderEmail'] = self.sender_email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('BlockEmail') is not None:
            self.block_email = m.get('BlockEmail')
        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SenderEmail') is not None:
            self.sender_email = m.get('SenderEmail')
        return self


class ListBlockSendingResponseBodyData(TeaModel):
    def __init__(
        self,
        block_email: str = None,
        block_time: int = None,
        reason: int = None,
        send_time: int = None,
        sender_email: str = None,
    ):
        self.block_email = block_email
        self.block_time = block_time
        self.reason = reason
        self.send_time = send_time
        self.sender_email = sender_email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_email is not None:
            result['BlockEmail'] = self.block_email
        if self.block_time is not None:
            result['BlockTime'] = self.block_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.sender_email is not None:
            result['SenderEmail'] = self.sender_email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockEmail') is not None:
            self.block_email = m.get('BlockEmail')
        if m.get('BlockTime') is not None:
            self.block_time = m.get('BlockTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SenderEmail') is not None:
            self.sender_email = m.get('SenderEmail')
        return self


class ListBlockSendingResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListBlockSendingResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBlockSendingResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBlockSendingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBlockSendingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListBlockSendingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserSuppressionRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        end_bounce_time: int = None,
        end_create_time: int = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_bounce_time: int = None,
        start_create_time: int = None,
    ):
        # Email address or domain name
        self.address = address
        # End time of the last bounce hit, timestamp, accurate to the second. The span between start and end times cannot exceed 7 days.
        self.end_bounce_time = end_bounce_time
        # End creation time, timestamp, accurate to the second. The span between start and end times cannot exceed 7 days.
        self.end_create_time = end_create_time
        self.owner_id = owner_id
        # Current page number
        self.page_no = page_no
        # Page size
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time of the last bounce hit, timestamp, accurate to the second.
        self.start_bounce_time = start_bounce_time
        # Start creation time, timestamp, accurate to the second.
        self.start_create_time = start_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.end_bounce_time is not None:
            result['EndBounceTime'] = self.end_bounce_time
        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time
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
        if self.start_bounce_time is not None:
            result['StartBounceTime'] = self.start_bounce_time
        if self.start_create_time is not None:
            result['StartCreateTime'] = self.start_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndBounceTime') is not None:
            self.end_bounce_time = m.get('EndBounceTime')
        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')
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
        if m.get('StartBounceTime') is not None:
            self.start_bounce_time = m.get('StartBounceTime')
        if m.get('StartCreateTime') is not None:
            self.start_create_time = m.get('StartCreateTime')
        return self


class ListUserSuppressionResponseBodyDataUserSuppressions(TeaModel):
    def __init__(
        self,
        address: str = None,
        create_time: int = None,
        last_bounce_time: int = None,
        suppression_id: int = None,
        type: str = None,
    ):
        # Email address or domain name
        self.address = address
        # Creation time, timestamp, accurate to the second.
        self.create_time = create_time
        # Last bounce hit time, timestamp, accurate to the second.
        self.last_bounce_time = last_bounce_time
        # Invalid address ID
        self.suppression_id = suppression_id
        # Source of entry, invalid address type
        # - system
        # - user
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_bounce_time is not None:
            result['LastBounceTime'] = self.last_bounce_time
        if self.suppression_id is not None:
            result['SuppressionId'] = self.suppression_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastBounceTime') is not None:
            self.last_bounce_time = m.get('LastBounceTime')
        if m.get('SuppressionId') is not None:
            self.suppression_id = m.get('SuppressionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListUserSuppressionResponseBodyData(TeaModel):
    def __init__(
        self,
        user_suppressions: List[ListUserSuppressionResponseBodyDataUserSuppressions] = None,
    ):
        self.user_suppressions = user_suppressions

    def validate(self):
        if self.user_suppressions:
            for k in self.user_suppressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserSuppressions'] = []
        if self.user_suppressions is not None:
            for k in self.user_suppressions:
                result['UserSuppressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_suppressions = []
        if m.get('UserSuppressions') is not None:
            for k in m.get('UserSuppressions'):
                temp_model = ListUserSuppressionResponseBodyDataUserSuppressions()
                self.user_suppressions.append(temp_model.from_map(k))
        return self


class ListUserSuppressionResponseBody(TeaModel):
    def __init__(
        self,
        data: ListUserSuppressionResponseBodyData = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Returned results.
        self.data = data
        # Page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListUserSuppressionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserSuppressionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserSuppressionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListUserSuppressionResponseBody()
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
        # Sending address ID
        # 
        # This parameter is required.
        self.mail_address_id = mail_address_id
        self.owner_id = owner_id
        # - Length should be 10 to 20 characters, and must include numbers, uppercase letters, and lowercase letters.
        # 
        # - Must contain at least 2 digits, 2 uppercase letters, and 2 lowercase letters, and neither the digits nor the letters can consist of a single character repeated.
        # 
        # - Cannot be the same as the last set password.
        self.password = password
        # Reply address
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
        # Request ID
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
        owner_id: int = None,
        password: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Domain name, length 1-50, can include numbers, uppercase letters, lowercase letters, ., and -.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # - Length should be between 10 to 20 characters, and must contain numbers, uppercase letters, and lowercase letters.
        # 
        # - At least 2 digits, 2 uppercase letters, and 2 lowercase letters are required, and neither digits nor letters can consist of a single character repeated.
        # 
        # - Cannot be the same as the last set password.
        # 
        # This parameter is required.
        self.password = password
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
        if self.password is not None:
            result['Password'] = self.password
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
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
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
        # Status code
        self.code = code
        # Description of the status code
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether it was successful
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
        # Tag Description
        self.tag_description = tag_description
        # Tag ID
        # 
        # This parameter is required.
        self.tag_id = tag_id
        # Tag Name
        # 
        # This parameter is required.
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
        # Request ID
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
        # Domain name, length 1-50, can include numbers, uppercase and lowercase letters, ., -.
        self.key_word = key_word
        self.owner_id = owner_id
        # Current page number. Default: 1
        self.page_no = page_no
        # Number of items per page, default: 10
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # - 0 indicates normal
        # - 1 indicates abnormal
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
        # Track verification
        self.cname_auth_status = cname_auth_status
        # CName verification status, success: 0; failure: 1
        self.confirm_status = confirm_status
        # Creation time
        self.create_time = create_time
        # Domain ID
        self.domain_id = domain_id
        # Domain name
        self.domain_name = domain_name
        # Domain record
        self.domain_record = domain_record
        # Domain status.
        # 
        # - 0: Available, verified
        # - 1: Unavailable, verification failed
        self.domain_status = domain_status
        # ICP filing status.
        # 
        # - 1 indicates filed
        # - 0 indicates not filed
        self.icp_status = icp_status
        # MX authentication status, success: 0, failure: 1.
        self.mx_auth_status = mx_auth_status
        # SPF authentication status, success: 0, failure: 1.
        self.spf_auth_status = spf_auth_status
        # Creation time in UTC format.
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
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # List of domains
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
        # End time, with a span from the start time that cannot exceed 30 days, in the format yyyy-MM-dd.
        self.end_time = end_time
        # Keyword. If not provided, it represents all invalid addresses.
        self.key_word = key_word
        # Number of items per request.
        self.length = length
        # Request starting position.
        self.next_start = next_start
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time, which cannot be earlier than 30 days ago, in the format yyyy-MM-dd.
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
        # Update time.
        self.last_update_time = last_update_time
        # Recipient address.
        self.to_address = to_address
        # Update time (in timestamp format).
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
        next_start: str = None,
        request_id: str = None,
        total_count: int = None,
        data: QueryInvalidAddressResponseBodyData = None,
    ):
        # Next request starting position.
        self.next_start = next_start
        # Request ID.
        self.request_id = request_id
        # Total count.
        self.total_count = total_count
        # Records.
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
        # Email address, length 1-60, supports numbers, letters, ., -, @.
        self.key_word = key_word
        self.owner_id = owner_id
        # Current page number, default: 1
        self.page_no = page_no
        # Page size, default: 10
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Sending address type. Values:
        # 
        # - batch: bulk email
        # - trigger: triggered email
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
        config_set_id: str = None,
        config_set_name: str = None,
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
        # Sending address
        self.account_name = account_name
        # Account status, frozen: 1, normal: 0.
        self.account_status = account_status
        self.config_set_id = config_set_id
        self.config_set_name = config_set_name
        # Creation time
        self.create_time = create_time
        # Daily quota limit
        self.daily_count = daily_count
        # Daily quota
        self.daily_req_count = daily_req_count
        # Domain status, 0 indicates normal, 1 indicates abnormal.
        self.domain_status = domain_status
        # Sending address ID
        self.mail_address_id = mail_address_id
        # Monthly quota limit
        self.month_count = month_count
        # Monthly quota
        self.month_req_count = month_req_count
        # Reply address
        self.reply_address = reply_address
        # Reply address status
        self.reply_status = reply_status
        # Sending address type. Values:
        # 
        # - batch: bulk email
        # - trigger: triggered email
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
        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id
        if self.config_set_name is not None:
            result['ConfigSetName'] = self.config_set_name
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
        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')
        if m.get('ConfigSetName') is not None:
            self.config_set_name = m.get('ConfigSetName')
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
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # List of sending addresses
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
        # Keyword, defaults to all information if not specified
        self.key_word = key_word
        self.owner_id = owner_id
        # Current page number
        self.page_no = page_no
        # Number of items per page, default: 10
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Delivery result. If not filled, it represents all statuses. Values:
        # 
        # - 0: Success
        # - 2: Invalid address
        # - 3: Spam
        # - 4: Failure
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
        # Total number of recipient addresses
        self.count = count
        # Creation time
        self.create_time = create_time
        # Description
        self.desc = desc
        # Recipient list ID
        self.receiver_id = receiver_id
        # Recipient list alias
        self.receivers_alias = receivers_alias
        # Recipient list name
        self.receivers_name = receivers_name
        # List status. Values:
        # 
        # - 0: Uploading
        # - 1: Upload completed
        self.receivers_status = receivers_status
        # UTC formatted creation time
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
        # Used for pagination. If there are more results, set this returned value to the NextStart in the next request.
        self.next_start = next_start
        # Number of items displayed per page.
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Detailed information of the recipient list
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
        # Recipient address, length 0-50
        self.key_word = key_word
        # Starting position for the next item, default: 0
        self.next_start = next_start
        self.owner_id = owner_id
        # Number of items per page, default: 10
        self.page_size = page_size
        # Recipient list ID (returned when creating a recipient list using the CreateReceiver API).
        # 
        # This parameter is required.
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
        # Creation Time
        self.create_time = create_time
        # Content
        self.data = data
        # Recipient address
        self.email = email
        # Creation time in UTC format
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
        # Field name for the Data of recipients
        self.data_schema = data_schema
        # Used for pagination. If there are more results, set this returned value to the NextStart in the next request.
        self.next_start = next_start
        # Request ID
        self.request_id = request_id
        # Total count (deprecated field, kept for historical compatibility)
        self.total_count = total_count
        # Detailed information
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
        # Tag name, length 1-50, defaults to all tags if not specified.
        self.key_word = key_word
        self.owner_id = owner_id
        # Page number
        self.page_no = page_no
        # Page size
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
        # Tag description
        self.tag_description = tag_description
        # Tag ID
        self.tag_id = tag_id
        # Tag name
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
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Data records
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
        # Keyword, defaults to all information
        self.key_word = key_word
        self.owner_id = owner_id
        # Current page number, default is 1
        self.page_no = page_no
        # Page size, default is 10
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Status, defaults to all statuses
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
        config_set_id: str = None,
        config_set_name: str = None,
        create_time: str = None,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
        receivers_name: str = None,
        request_count: str = None,
        tag_name: str = None,
        task_id: str = None,
        task_status: str = None,
        template_name: str = None,
        utc_create_time: int = None,
    ):
        # Address type, sending address: 1; random address: 0;
        self.address_type = address_type
        self.config_set_id = config_set_id
        self.config_set_name = config_set_name
        # Creation time
        self.create_time = create_time
        # dedicated IP pool ID.
        self.ip_pool_id = ip_pool_id
        # dedicated IP pool name.
        self.ip_pool_name = ip_pool_name
        # Receiver\\"s name
        self.receivers_name = receivers_name
        # Request count
        self.request_count = request_count
        # Tag
        self.tag_name = tag_name
        # Task ID
        self.task_id = task_id
        # Task status, sent successfully: 1
        self.task_status = task_status
        # Template name
        self.template_name = template_name
        # Creation time in UTC format
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
        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id
        if self.config_set_name is not None:
            result['ConfigSetName'] = self.config_set_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name
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
        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')
        if m.get('ConfigSetName') is not None:
            self.config_set_name = m.get('ConfigSetName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')
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
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Returned results
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


class RemoveUserSuppressionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        suppression_ids: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.suppression_ids = suppression_ids

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
        if self.suppression_ids is not None:
            result['SuppressionIds'] = self.suppression_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SuppressionIds') is not None:
            self.suppression_ids = m.get('SuppressionIds')
        return self


class RemoveUserSuppressionResponseBody(TeaModel):
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


class RemoveUserSuppressionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveUserSuppressionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveUserSuppressionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveReceiverDetailRequest(TeaModel):
    def __init__(
        self,
        custom_detail: str = None,
        detail: str = None,
        owner_id: int = None,
        receiver_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.custom_detail = custom_detail
        # Content, supports uploading multiple recipients at once, with a limit of 500 records per upload. Each record is separated by {} and commas, example:
        # 
        # [{ },{ },{ }...], the format within {} is as follows:
        # 
        # [{"b":"birthday","e":"xxx@example.net","g":"gender","m":"mobile","n":"nickname","u":"name"}], when passing values, pass it as a string, not a list.
        # 
        # If a duplicate recipient address is inserted, it will return "ErrorCount": 1
        self.detail = detail
        self.owner_id = owner_id
        # Recipient list ID
        # 
        # This parameter is required.
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
        if self.custom_detail is not None:
            result['CustomDetail'] = self.custom_detail
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
        if m.get('CustomDetail') is not None:
            self.custom_detail = m.get('CustomDetail')
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
        err_message: str = None,
    ):
        # Recipient address.
        self.email = email
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
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
        # List of recipient addresses that failed to upload.
        self.data = data
        # Number of errors.
        self.error_count = error_count
        # Request ID
        self.request_id = request_id
        # Number of successes.
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


class SendTestByTemplateRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        birthday: str = None,
        email: str = None,
        gender: str = None,
        mobile: str = None,
        nick_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        template_params: str = None,
        user_name: str = None,
    ):
        # Sender address, with a maximum length of 60 characters
        # 
        # This parameter is required.
        self.account_name = account_name
        # Birthday, with a maximum length of 30 characters
        self.birthday = birthday
        # Recipient address, with a maximum length of 60 characters
        # 
        # This parameter is required.
        self.email = email
        # Gender, with a maximum length of 30 characters
        self.gender = gender
        # Mobile, with a maximum length of 30 characters
        self.mobile = mobile
        # NickName, with a maximum length of 30 characters
        self.nick_name = nick_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Template ID
        # 
        # This parameter is required.
        self.template_id = template_id
        self.template_params = template_params
        # UserName, with a maximum length of 30 characters
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.email is not None:
            result['Email'] = self.email
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class SendTestByTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID
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


class SendTestByTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendTestByTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SendTestByTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendValidateFileRequest(TeaModel):
    def __init__(
        self,
        address_column: int = None,
        file_name: str = None,
        file_url: str = None,
        has_header_row: bool = None,
        remove_duplicate: bool = None,
    ):
        # This parameter is required.
        self.address_column = address_column
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.has_header_row = has_header_row
        # This parameter is required.
        self.remove_duplicate = remove_duplicate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_column is not None:
            result['AddressColumn'] = self.address_column
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.has_header_row is not None:
            result['HasHeaderRow'] = self.has_header_row
        if self.remove_duplicate is not None:
            result['RemoveDuplicate'] = self.remove_duplicate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressColumn') is not None:
            self.address_column = m.get('AddressColumn')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('HasHeaderRow') is not None:
            self.has_header_row = m.get('HasHeaderRow')
        if m.get('RemoveDuplicate') is not None:
            self.remove_duplicate = m.get('RemoveDuplicate')
        return self


class SendValidateFileAdvanceRequest(TeaModel):
    def __init__(
        self,
        address_column: int = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        has_header_row: bool = None,
        remove_duplicate: bool = None,
    ):
        # This parameter is required.
        self.address_column = address_column
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_url_object = file_url_object
        # This parameter is required.
        self.has_header_row = has_header_row
        # This parameter is required.
        self.remove_duplicate = remove_duplicate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_column is not None:
            result['AddressColumn'] = self.address_column
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.has_header_row is not None:
            result['HasHeaderRow'] = self.has_header_row
        if self.remove_duplicate is not None:
            result['RemoveDuplicate'] = self.remove_duplicate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressColumn') is not None:
            self.address_column = m.get('AddressColumn')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('HasHeaderRow') is not None:
            self.has_header_row = m.get('HasHeaderRow')
        if m.get('RemoveDuplicate') is not None:
            self.remove_duplicate = m.get('RemoveDuplicate')
        return self


class SendValidateFileResponseBody(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        request_id: str = None,
    ):
        self.file_id = file_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendValidateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendValidateFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SendValidateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SenderStatisticsByTagNameAndBatchIDRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dedicated_ip: str = None,
        dedicated_ip_pool_id: str = None,
        end_time: str = None,
        esp: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag_name: str = None,
    ):
        # Sending address. If not filled, it represents all addresses.
        self.account_name = account_name
        self.dedicated_ip = dedicated_ip
        self.dedicated_ip_pool_id = dedicated_ip_pool_id
        # End time, which cannot exceed 7 days from the start time, in the format yyyy-MM-dd.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.esp = esp
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time, in the format yyyy-MM-dd.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Email tag. If not filled, it represents all tags.
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
        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip
        if self.dedicated_ip_pool_id is not None:
            result['DedicatedIpPoolId'] = self.dedicated_ip_pool_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.esp is not None:
            result['Esp'] = self.esp
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
        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')
        if m.get('DedicatedIpPoolId') is not None:
            self.dedicated_ip_pool_id = m.get('DedicatedIpPoolId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Esp') is not None:
            self.esp = m.get('Esp')
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
        # Creation time
        self.create_time = create_time
        # Failure count
        self.faild_count = faild_count
        # Request count
        self.request_count = request_count
        # Success rate
        self.succeeded_percent = succeeded_percent
        # Success count
        self.success_count = success_count
        # Invalid count
        self.unavailable_count = unavailable_count
        # Unavailability rate
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
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Data records
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
        config_set_id: str = None,
        end_time: str = None,
        ip_pool_id: str = None,
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
        # Sending address. If not filled, it represents all addresses.
        # 
        # > **AccountName**, **TagName**, and **ToAddress** can all be left unfilled. If any are filled, only one of these parameters can be passed; you cannot pass a combination of two or more.
        self.account_name = account_name
        self.config_set_id = config_set_id
        # End time. The span between start and end times cannot exceed 30 days, format: yyyy-MM-dd HH:mm.
        self.end_time = end_time
        self.ip_pool_id = ip_pool_id
        # Specifies the number of results to return in this request. Range is 1~100.
        self.length = length
        # Used for pagination. Specifies the offset for this request. If there are more results, set this returned value to the NextStart in the next request.
        self.next_start = next_start
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time. The span between start and end times cannot exceed 30 days, format: yyyy-MM-dd HH:mm
        self.start_time = start_time
        # Delivery result. If not filled, it represents all statuses. Values:
        # 
        # - 0: Success
        # - 2: Invalid Address
        # - 3: Spam
        # - 4: Failure
        self.status = status
        # Email tag. If not filled, it represents all tags.
        self.tag_name = tag_name
        # Recipient address. If not filled, it represents all recipient addresses.
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
        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
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
        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
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
        config_set_id: str = None,
        config_set_name: str = None,
        error_classification: str = None,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
        last_update_time: str = None,
        message: str = None,
        status: int = None,
        subject: str = None,
        to_address: str = None,
        utc_last_update_time: str = None,
    ):
        # Sending address
        self.account_name = account_name
        self.config_set_id = config_set_id
        self.config_set_name = config_set_name
        # Detailed classification of error reasons: - SendOk - SmtpNxBox
        # etc.
        self.error_classification = error_classification
        self.ip_pool_id = ip_pool_id
        self.ip_pool_name = ip_pool_name
        # Update time
        self.last_update_time = last_update_time
        # Delivery detail information
        self.message = message
        # Delivery status: 0 Success, 2 Invalid Address, 3 Spam, 4 Other Failures
        self.status = status
        # Email subject
        self.subject = subject
        # Recipient address
        self.to_address = to_address
        # UTC formatted update time
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
        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id
        if self.config_set_name is not None:
            result['ConfigSetName'] = self.config_set_name
        if self.error_classification is not None:
            result['ErrorClassification'] = self.error_classification
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.utc_last_update_time is not None:
            result['UtcLastUpdateTime'] = self.utc_last_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')
        if m.get('ConfigSetName') is not None:
            self.config_set_name = m.get('ConfigSetName')
        if m.get('ErrorClassification') is not None:
            self.error_classification = m.get('ErrorClassification')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
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
        next_start: str = None,
        request_id: str = None,
        data: SenderStatisticsDetailByParamResponseBodyData = None,
    ):
        # Used for pagination. If there are more results, set this returned value to the NextStart in the next request.
        self.next_start = next_start
        # Request ID
        self.request_id = request_id
        # Detailed records
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


class SetSuppressionListLevelRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        suppression_list_level: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.suppression_list_level = suppression_list_level

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
        if self.suppression_list_level is not None:
            result['SuppressionListLevel'] = self.suppression_list_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SuppressionListLevel') is not None:
            self.suppression_list_level = m.get('SuppressionListLevel')
        return self


class SetSuppressionListLevelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        suppression_list_level: str = None,
    ):
        self.request_id = request_id
        self.suppression_list_level = suppression_list_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.suppression_list_level is not None:
            result['SuppressionListLevel'] = self.suppression_list_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuppressionListLevel') is not None:
            self.suppression_list_level = m.get('SuppressionListLevel')
        return self


class SetSuppressionListLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSuppressionListLevelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetSuppressionListLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleSendMailRequestAttachments(TeaModel):
    def __init__(
        self,
        attachment_name: str = None,
        attachment_url: str = None,
    ):
        self.attachment_name = attachment_name
        self.attachment_url = attachment_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.attachment_url is not None:
            result['AttachmentUrl'] = self.attachment_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('AttachmentUrl') is not None:
            self.attachment_url = m.get('AttachmentUrl')
        return self


class SingleSendMailRequestTemplate(TeaModel):
    def __init__(
        self,
        template_data: Dict[str, str] = None,
        template_id: str = None,
    ):
        self.template_data = template_data
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_data is not None:
            result['TemplateData'] = self.template_data
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateData') is not None:
            self.template_data = m.get('TemplateData')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SingleSendMailRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        attachments: List[SingleSendMailRequestAttachments] = None,
        click_trace: str = None,
        from_alias: str = None,
        headers: str = None,
        html_body: str = None,
        ip_pool_id: str = None,
        owner_id: int = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        reply_to_address: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
        tag_name: str = None,
        template: SingleSendMailRequestTemplate = None,
        text_body: str = None,
        to_address: str = None,
        un_subscribe_filter_level: str = None,
        un_subscribe_link_type: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.address_type = address_type
        self.attachments = attachments
        self.click_trace = click_trace
        self.from_alias = from_alias
        self.headers = headers
        self.html_body = html_body
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        # This parameter is required.
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.subject = subject
        self.tag_name = tag_name
        self.template = template
        self.text_body = text_body
        # This parameter is required.
        self.to_address = to_address
        self.un_subscribe_filter_level = un_subscribe_filter_level
        self.un_subscribe_link_type = un_subscribe_link_type

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        result['Attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['Attachments'].append(k.to_map() if k else None)
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.from_alias is not None:
            result['FromAlias'] = self.from_alias
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.html_body is not None:
            result['HtmlBody'] = self.html_body
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
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
        if self.template is not None:
            result['Template'] = self.template.to_map()
        if self.text_body is not None:
            result['TextBody'] = self.text_body
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.un_subscribe_filter_level is not None:
            result['UnSubscribeFilterLevel'] = self.un_subscribe_filter_level
        if self.un_subscribe_link_type is not None:
            result['UnSubscribeLinkType'] = self.un_subscribe_link_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        self.attachments = []
        if m.get('Attachments') is not None:
            for k in m.get('Attachments'):
                temp_model = SingleSendMailRequestAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('FromAlias') is not None:
            self.from_alias = m.get('FromAlias')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('HtmlBody') is not None:
            self.html_body = m.get('HtmlBody')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
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
        if m.get('Template') is not None:
            temp_model = SingleSendMailRequestTemplate()
            self.template = temp_model.from_map(m['Template'])
        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('UnSubscribeFilterLevel') is not None:
            self.un_subscribe_filter_level = m.get('UnSubscribeFilterLevel')
        if m.get('UnSubscribeLinkType') is not None:
            self.un_subscribe_link_type = m.get('UnSubscribeLinkType')
        return self


class SingleSendMailAdvanceRequestAttachments(TeaModel):
    def __init__(
        self,
        attachment_name: str = None,
        attachment_url_object: BinaryIO = None,
    ):
        self.attachment_name = attachment_name
        self.attachment_url_object = attachment_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.attachment_url_object is not None:
            result['AttachmentUrl'] = self.attachment_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('AttachmentUrl') is not None:
            self.attachment_url_object = m.get('AttachmentUrl')
        return self


class SingleSendMailAdvanceRequestTemplate(TeaModel):
    def __init__(
        self,
        template_data: Dict[str, str] = None,
        template_id: str = None,
    ):
        self.template_data = template_data
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_data is not None:
            result['TemplateData'] = self.template_data
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateData') is not None:
            self.template_data = m.get('TemplateData')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SingleSendMailAdvanceRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        attachments: List[SingleSendMailAdvanceRequestAttachments] = None,
        click_trace: str = None,
        from_alias: str = None,
        headers: str = None,
        html_body: str = None,
        ip_pool_id: str = None,
        owner_id: int = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        reply_to_address: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
        tag_name: str = None,
        template: SingleSendMailAdvanceRequestTemplate = None,
        text_body: str = None,
        to_address: str = None,
        un_subscribe_filter_level: str = None,
        un_subscribe_link_type: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.address_type = address_type
        self.attachments = attachments
        self.click_trace = click_trace
        self.from_alias = from_alias
        self.headers = headers
        self.html_body = html_body
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        # This parameter is required.
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.subject = subject
        self.tag_name = tag_name
        self.template = template
        self.text_body = text_body
        # This parameter is required.
        self.to_address = to_address
        self.un_subscribe_filter_level = un_subscribe_filter_level
        self.un_subscribe_link_type = un_subscribe_link_type

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        result['Attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['Attachments'].append(k.to_map() if k else None)
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.from_alias is not None:
            result['FromAlias'] = self.from_alias
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.html_body is not None:
            result['HtmlBody'] = self.html_body
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
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
        if self.template is not None:
            result['Template'] = self.template.to_map()
        if self.text_body is not None:
            result['TextBody'] = self.text_body
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.un_subscribe_filter_level is not None:
            result['UnSubscribeFilterLevel'] = self.un_subscribe_filter_level
        if self.un_subscribe_link_type is not None:
            result['UnSubscribeLinkType'] = self.un_subscribe_link_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        self.attachments = []
        if m.get('Attachments') is not None:
            for k in m.get('Attachments'):
                temp_model = SingleSendMailAdvanceRequestAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('FromAlias') is not None:
            self.from_alias = m.get('FromAlias')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('HtmlBody') is not None:
            self.html_body = m.get('HtmlBody')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
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
        if m.get('Template') is not None:
            temp_model = SingleSendMailAdvanceRequestTemplate()
            self.template = temp_model.from_map(m['Template'])
        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('UnSubscribeFilterLevel') is not None:
            self.un_subscribe_filter_level = m.get('UnSubscribeFilterLevel')
        if m.get('UnSubscribeLinkType') is not None:
            self.un_subscribe_link_type = m.get('UnSubscribeLinkType')
        return self


class SingleSendMailShrinkRequestAttachments(TeaModel):
    def __init__(
        self,
        attachment_name: str = None,
        attachment_url: str = None,
    ):
        self.attachment_name = attachment_name
        self.attachment_url = attachment_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.attachment_url is not None:
            result['AttachmentUrl'] = self.attachment_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('AttachmentUrl') is not None:
            self.attachment_url = m.get('AttachmentUrl')
        return self


class SingleSendMailShrinkRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        attachments: List[SingleSendMailShrinkRequestAttachments] = None,
        click_trace: str = None,
        from_alias: str = None,
        headers: str = None,
        html_body: str = None,
        ip_pool_id: str = None,
        owner_id: int = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        reply_to_address: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
        tag_name: str = None,
        template_shrink: str = None,
        text_body: str = None,
        to_address: str = None,
        un_subscribe_filter_level: str = None,
        un_subscribe_link_type: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.address_type = address_type
        self.attachments = attachments
        self.click_trace = click_trace
        self.from_alias = from_alias
        self.headers = headers
        self.html_body = html_body
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        self.reply_address = reply_address
        self.reply_address_alias = reply_address_alias
        # This parameter is required.
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.subject = subject
        self.tag_name = tag_name
        self.template_shrink = template_shrink
        self.text_body = text_body
        # This parameter is required.
        self.to_address = to_address
        self.un_subscribe_filter_level = un_subscribe_filter_level
        self.un_subscribe_link_type = un_subscribe_link_type

    def validate(self):
        if self.attachments:
            for k in self.attachments:
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
        result['Attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['Attachments'].append(k.to_map() if k else None)
        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace
        if self.from_alias is not None:
            result['FromAlias'] = self.from_alias
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.html_body is not None:
            result['HtmlBody'] = self.html_body
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id
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
        if self.template_shrink is not None:
            result['Template'] = self.template_shrink
        if self.text_body is not None:
            result['TextBody'] = self.text_body
        if self.to_address is not None:
            result['ToAddress'] = self.to_address
        if self.un_subscribe_filter_level is not None:
            result['UnSubscribeFilterLevel'] = self.un_subscribe_filter_level
        if self.un_subscribe_link_type is not None:
            result['UnSubscribeLinkType'] = self.un_subscribe_link_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        self.attachments = []
        if m.get('Attachments') is not None:
            for k in m.get('Attachments'):
                temp_model = SingleSendMailShrinkRequestAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')
        if m.get('FromAlias') is not None:
            self.from_alias = m.get('FromAlias')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('HtmlBody') is not None:
            self.html_body = m.get('HtmlBody')
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')
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
        if m.get('Template') is not None:
            self.template_shrink = m.get('Template')
        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')
        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')
        if m.get('UnSubscribeFilterLevel') is not None:
            self.un_subscribe_filter_level = m.get('UnSubscribeFilterLevel')
        if m.get('UnSubscribeLinkType') is not None:
            self.un_subscribe_link_type = m.get('UnSubscribeLinkType')
        return self


class SingleSendMailResponseBody(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        request_id: str = None,
    ):
        # Event ID
        self.env_id = env_id
        # Request ID
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


class UnblockSendingRequest(TeaModel):
    def __init__(
        self,
        block_email: str = None,
        block_type: str = None,
        sender_email: str = None,
    ):
        # Blacklisted recipient\\"s email address
        # 
        # This parameter is required.
        self.block_email = block_email
        # Blacklist type
        # - UNSUB: Unsubscribe
        # - REPORT: Report
        # 
        # This parameter is required.
        self.block_type = block_type
        # Sender\\"s email address
        # 
        # This parameter is required.
        self.sender_email = sender_email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_email is not None:
            result['BlockEmail'] = self.block_email
        if self.block_type is not None:
            result['BlockType'] = self.block_type
        if self.sender_email is not None:
            result['SenderEmail'] = self.sender_email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockEmail') is not None:
            self.block_email = m.get('BlockEmail')
        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')
        if m.get('SenderEmail') is not None:
            self.sender_email = m.get('SenderEmail')
        return self


class UnblockSendingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID
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


class UnblockSendingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnblockSendingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UnblockSendingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpProtectionRequest(TeaModel):
    def __init__(
        self,
        ip_protection: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # IP protection switch, On: 1 Off: 0
        self.ip_protection = ip_protection
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
        if self.ip_protection is not None:
            result['IpProtection'] = self.ip_protection
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtection') is not None:
            self.ip_protection = m.get('IpProtection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateIpProtectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID
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


class UpdateIpProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIpProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateIpProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequestUser(TeaModel):
    def __init__(
        self,
        enable_eventbridge: bool = None,
    ):
        # Whether EventBridge is enabled
        self.enable_eventbridge = enable_eventbridge

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_eventbridge is not None:
            result['EnableEventbridge'] = self.enable_eventbridge
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableEventbridge') is not None:
            self.enable_eventbridge = m.get('EnableEventbridge')
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        user: UpdateUserRequestUser = None,
    ):
        # User Information
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = UpdateUserRequestUser()
            self.user = temp_model.from_map(m['User'])
        return self


class UpdateUserShrinkRequest(TeaModel):
    def __init__(
        self,
        user_shrink: str = None,
    ):
        # User Information
        self.user_shrink = user_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateEmailRequest(TeaModel):
    def __init__(
        self,
        check_graylist: bool = None,
        email: str = None,
        timeout: int = None,
    ):
        self.check_graylist = check_graylist
        # This parameter is required.
        self.email = email
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_graylist is not None:
            result['CheckGraylist'] = self.check_graylist
        if self.email is not None:
            result['Email'] = self.email
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckGraylist') is not None:
            self.check_graylist = m.get('CheckGraylist')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class ValidateEmailResponseBody(TeaModel):
    def __init__(
        self,
        domain_part: str = None,
        is_free_mail: bool = None,
        local_part: str = None,
        provider: str = None,
        request_id: str = None,
        status: str = None,
        sub_status: str = None,
    ):
        self.domain_part = domain_part
        self.is_free_mail = is_free_mail
        self.local_part = local_part
        self.provider = provider
        self.request_id = request_id
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.sub_status = sub_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_part is not None:
            result['DomainPart'] = self.domain_part
        if self.is_free_mail is not None:
            result['IsFreeMail'] = self.is_free_mail
        if self.local_part is not None:
            result['LocalPart'] = self.local_part
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainPart') is not None:
            self.domain_part = m.get('DomainPart')
        if m.get('IsFreeMail') is not None:
            self.is_free_mail = m.get('IsFreeMail')
        if m.get('LocalPart') is not None:
            self.local_part = m.get('LocalPart')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        return self


class ValidateEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateEmailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ValidateEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


