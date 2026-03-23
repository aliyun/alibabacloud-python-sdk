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
        # The sender address configured in the console.
        # 
        # This parameter is required.
        self.account_name = account_name
        # - 0: Random account
        # 
        # - 1: Sender address
        # 
        # This parameter is required.
        self.address_type = address_type
        # - 1: Enables the data tracking feature.
        # 
        # - 0 (default): Disables the data tracking feature.
        self.click_trace = click_trace
        # Enables domain-level authentication.
        # 
        # - true
        # 
        # - false
        # 
        # Use this parameter only for domain-level authentication. Ignore it for sender address-level authentication.
        # 
        # 1\\. The console creates the address \\`domain-auth-created-by-system\\@example.com\\`. Do not change the prefix before the at sign (@). Replace the domain suffix with your own domain.
        # 
        # 2\\.
        # 
        # **API scenario**
        # 
        # Set \\`AccountName\\` to your domain. Recipients see \\`domain-auth-created-by-system\\@example.com\\` as the sender.
        # 
        # **SMTP scenario**
        # 
        # a. Use the \\`ModifyPWByDomain\\` API to set a password for your domain.
        # 
        # b. Authenticate using your domain and the password. Set the actual sender address (\\`mailfrom\\`) to a custom address, such as \\`user\\@example.com\\`. Recipients see \\`user\\@example.com\\` as the sender.
        self.domain_auth = domain_auth
        # Message header settings.
        # 
        # All fields, standard or non-standard, must follow standard header syntax. For API calls, the \\`headers\\` field supports up to 10 headers. Any headers beyond this limit are ignored. SMTP does not have a header limit.
        # 
        # 1\\. Standard fields
        # 
        # \\`Message-ID\\`, \\`List-Unsubscribe\\`, \\`List-Unsubscribe-Post\\`
        # 
        # Standard fields overwrite existing values in the message header.
        # 
        # 2\\. Non-standard fields
        # 
        # Case-insensitive
        # 
        # a. Start with \\`X-User-\\`. These fields are not pushed to EventBridge or Message Service. They are required only for API calls. SMTP supports any custom header.
        # 
        # b. Start with \\`X-User-Notify-\\`. These fields are pushed to EventBridge and Message Service. They are supported by both API and SMTP.
        # 
        # When pushed to EventBridge or Message Service, these fields appear under the \\`headers\\` object.
        self.headers = headers
        # The ID of the dedicated IP address pool. If you purchased dedicated IP addresses, use this parameter to specify the egress IP address for sending the email.
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        # The name of a pre-created recipient list to which recipients have been uploaded.
        # 
        # Note:
        # 
        # The number of recipients in the list must not exceed your remaining daily quota. Otherwise, email sending fails.
        # 
        # Do not delete the recipient list for at least 10 minutes after triggering the task. Otherwise, email sending may fail.
        # 
        # This parameter is required.
        self.receivers_name = receivers_name
        # The reply-to address.
        self.reply_address = reply_address
        # The alias for the reply-to address.
        self.reply_address_alias = reply_address_alias
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the email tag.
        self.tag_name = tag_name
        # The name of a pre-created and approved template.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The filtering level. For more information, see [Unsubscribe link generation and filtering mechanism](https://help.aliyun.com/document_detail/2689048.html).
        # 
        # - disabled: No filtering.
        # 
        # - default: Uses the default policy. Batch emails are filtered at the sender address level.
        # 
        # - mailfrom: Filters at the sender address level.
        # 
        # - mailfrom_domain: Filters at the email domain level.
        # 
        # - edm_id: Filters at the account level.
        self.un_subscribe_filter_level = un_subscribe_filter_level
        # The type of unsubscribe link to generate. For more information, see [Unsubscribe link generation and filtering mechanism](https://help.aliyun.com/document_detail/2689048.html).
        # 
        # - disabled: Does not generate a link.
        # 
        # - default: Uses the default policy. An unsubscribe link is generated when batch emails are sent from a sender address to specific domains, such as those containing the keywords "gmail", "yahoo", "google", "aol.com", "hotmail", "outlook", or "ymail.com".
        # 
        # The language of the unsubscribe link matches the recipient\\"s browser language setting.
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

