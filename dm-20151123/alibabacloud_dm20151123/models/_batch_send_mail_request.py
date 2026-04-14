# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSendMailRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        click_trace: str = None,
        domain_auth: bool = None,
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
        self.domain_auth = domain_auth
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace

        if self.domain_auth is not None:
            result['DomainAuth'] = self.domain_auth

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

        if m.get('DomainAuth') is not None:
            self.domain_auth = m.get('DomainAuth')

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

