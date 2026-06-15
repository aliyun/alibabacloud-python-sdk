# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSendMailShrinkRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        click_trace: str = None,
        domain_auth: bool = None,
        headers: str = None,
        ip_pool_id: str = None,
        owner_id: int = None,
        receivers_shrink: str = None,
        receivers_name: str = None,
        reply_address: str = None,
        reply_address_alias: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_name: str = None,
        template_content_shrink: str = None,
        template_name: str = None,
        un_subscribe_filter_level: str = None,
        un_subscribe_link_type: str = None,
    ):
        # The sender address configured in the management console.
        # 
        # This parameter is required.
        self.account_name = account_name
        # Valid values:
        # - 0: random account
        # - 1: sender address.
        # 
        # This parameter is required.
        self.address_type = address_type
        # Valid values:
        # - 1: Enables data tracking.
        # - 0 (default): Disables data tracking.
        self.click_trace = click_trace
        # Specifies whether to enable domain-level authentication.
        # 
        # - true
        # 
        # - false
        # 
        # Use this parameter only for domain-level authentication. Ignore it for sender address-level authentication.
        # 
        # 1. Create the address domain-auth-created-by-system@example.com in the console. Keep the prefix before @ unchanged and replace the suffix with your own domain name.
        # 
        # 2.
        # 
        # **API scenario**
        # 
        # Set AccountName to the domain name. The recipient sees domain-auth-created-by-system@example.com as the sender.
        # 
        # **SMTP scenario**
        # 
        # a. Call the ModifyPWByDomain operation to set the domain password.
        # 
        # b. Authenticate with the domain name and the configured password. Set the actual sender (mailfrom) to a custom address such as user@example.com. The recipient sees user@example.com as the sender.
        self.domain_auth = domain_auth
        # The email header settings.
        # 
        # Both standard and non-standard fields must comply with the syntax requirements for headers defined in the standard. A maximum of 10 headers can be passed through the headers field when sending emails via API. Headers exceeding this limit are ignored. SMTP has no such limit.
        # 
        # 1. Standard fields
        # 
        # Message-ID, List-Unsubscribe, List-Unsubscribe-Post
        # 
        # Standard fields overwrite the original values in the email header.
        # 
        # 2. Non-standard fields
        # 
        # Case-insensitive.
        # 
        # a. Fields prefixed with X-User- (not pushed to EventBridge or Message Service (MNS). This restriction applies to API only. SMTP allows any custom fields.)
        # 
        # b. Fields prefixed with X-User-Notify- (pushed to EventBridge and Message Service (MNS). Both API and SMTP are supported.)
        # 
        # When pushed to EventBridge or MNS, these fields are included under the header field.
        self.headers = headers
        # The ID of the dedicated IP address pool. Users who have purchased dedicated IP addresses can use this parameter to specify the outbound IP address for this email sending.
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        # The recipient list. The number of recipients must not exceed 100. Use this parameter or ReceiversName. If both Receivers and ReceiversName are specified, ReceiversName takes precedence.
        # 
        # Example: [{"To":["Jackie@example.com"],"TemplateData":{"UserName":"Jackie"}},{"To":["Tom@example.com"],"TemplateData":{"UserName":"Tom"}}].
        self.receivers_shrink = receivers_shrink
        # The name of a pre-created recipient list that has recipients uploaded.
        # 
        # > **Note**
        # 
        # > The number of recipients in the list must not exceed the remaining daily quota. Otherwise, the email sending fails.
        # 
        # > Wait at least 10 minutes after triggering the task before deleting the recipient list. Otherwise, the email sending may fail.
        self.receivers_name = receivers_name
        # The reply-to address.
        self.reply_address = reply_address
        # The alias of the reply-to address.
        self.reply_address_alias = reply_address_alias
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the email tag.
        self.tag_name = tag_name
        # The custom email content. Directly specify the content without creating a template in advance. Use this parameter or TemplateName. If both TemplateContent and TemplateName are specified, TemplateName takes precedence.
        self.template_content_shrink = template_content_shrink
        # The name of a pre-created and approved template.
        self.template_name = template_name
        # The filtering level. For more information, see [Unsubscribe link generation and filtering mechanism](https://help.aliyun.com/document_detail/2689048.html).
        # - disabled: No filtering is applied.
        # - default: Uses the default policy. Batch addresses use sender address-level filtering.
        # - mailfrom: Sender address-level filtering.
        # - mailfrom_domain: Sender domain-level filtering.
        # - edm_id: Account-level filtering.
        self.un_subscribe_filter_level = un_subscribe_filter_level
        # The type of the generated unsubscribe link. For more information, see [Unsubscribe link generation and filtering mechanism](https://help.aliyun.com/document_detail/2689048.html).
        # - disabled: No unsubscribe link is generated.
        # - default: Uses the default policy. An unsubscribe link is generated when a batch-type sender address sends emails to specific domains, such as domains containing keywords "gmail", "yahoo", "google", "aol.com", "hotmail", "outlook", or "ymail.com".
        # 
        # The display language is automatically determined based on the recipient\\"s browser settings.
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

        if self.receivers_shrink is not None:
            result['Receivers'] = self.receivers_shrink

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

        if self.template_content_shrink is not None:
            result['TemplateContent'] = self.template_content_shrink

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

        if m.get('Receivers') is not None:
            self.receivers_shrink = m.get('Receivers')

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

        if m.get('TemplateContent') is not None:
            self.template_content_shrink = m.get('TemplateContent')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UnSubscribeFilterLevel') is not None:
            self.un_subscribe_filter_level = m.get('UnSubscribeFilterLevel')

        if m.get('UnSubscribeLinkType') is not None:
            self.un_subscribe_link_type = m.get('UnSubscribeLinkType')

        return self

