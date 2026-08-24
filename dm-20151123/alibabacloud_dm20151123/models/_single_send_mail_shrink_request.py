# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class SingleSendMailShrinkRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        attachments: List[main_models.SingleSendMailShrinkRequestAttachments] = None,
        bcc_address: str = None,
        click_trace: str = None,
        domain_auth: bool = None,
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
        # The sender address configured in the management console.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The address type. Valid values:
        # 
        # - 0: random account
        # - 1: sender address
        # 
        # This parameter is required.
        self.address_type = address_type
        # Supported only when using the new SDK. Not supported through OpenAPI or signature mechanism methods. For more information, refer to [How do I send emails with attachments through the SDK?](https://help.aliyun.com/document_detail/2937843.html).
        self.attachments = attachments
        # - Specifies the BCC (blind carbon copy) recipient list for the email.
        # - The system sends a copy identical to the main email content to each BCC address. The BCC information is not visible to any recipients (including ToAddress and BccAddress).
        # - To protect the privacy of BCC recipients, email tracking features are disabled by default for BCC emails. This means the system does not record behavioral data such as open rates or click-through rates for BCC emails. However, billing for sending volume, sending details, and sending status statistics remain consistent with regular emails.
        # - A maximum of 2 BCC recipients can be specified per send.
        # 
        # Note: The SingleSendMail operation does not support the Cc (carbon copy) field. Use SMTP if you need this feature.
        self.bcc_address = bcc_address
        # Specifies whether to enable data tracking. Valid values:
        # 
        # - 1: Enable data tracking.
        # - 0 (default): Disable data tracking.
        self.click_trace = click_trace
        # Specifies whether to enable domain-level authentication. Valid values:
        # 
        # - true
        # - false
        # 
        # Use this parameter only for domain-level authentication. Ignore it for sender address-level authentication.
        # 
        # 1. Create the address domain-auth-created-by-system@example.com in the console. Keep the prefix before @ unchanged and use your own domain name as the suffix.
        # 
        # 2.
        # 
        # **API scenario**
        # 
        # Set AccountName to a custom sender address for the domain. The recipient sees the custom sender address as the sender.
        # 
        # **SMTP scenario**
        # 
        # a. Set the domain password through the ModifyPWByDomain operation.
        # 
        # b. Authenticate using the domain name and the configured password. Pass a custom address such as user@example.com as the actual sender (mailfrom). The recipient sees user@example.com as the sender.
        self.domain_auth = domain_auth
        # The sender nickname. The value cannot exceed 15 characters in length.
        # 
        # For example, if the sender nickname is set to "Jane" and the sender address is test***@example.net, the recipient sees the sender address as "Jane" test***@example.net.
        self.from_alias = from_alias
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
        # a. Fields prefixed with X-User- (not pushed to EventBridge or Message Service MNS. This is an API-only requirement. SMTP allows any custom fields.)
        # 
        # b. Fields prefixed with X-User-Notify- (pushed to EventBridge and Message Service MNS. Both API and SMTP are supported.)
        # 
        # When pushed to EventBridge or MNS, these fields are included under the header field.
        self.headers = headers
        # The HTML body of the email.
        # 
        # Note: HtmlBody and TextBody are used for different types of email content. You must specify one of them.
        # 
        # - The size limit for URL-based parameter passing is approximately 80 KB.
        # - The size limit for Body-based parameter passing with the new SDK is approximately 8 MB (Java 1.4.0 or later, Python3 1.4.0 or later, PHP 1.4.0 or later).
        self.html_body = html_body
        # The ID of the dedicated IP address pool. Users who have purchased dedicated IP addresses can use this parameter to specify the outbound IP address for this email. For more information, refer to [Dedicated IP](https://help.aliyun.com/document_detail/2932088.html).
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        # The reply-to address.
        self.reply_address = reply_address
        # The reply-to address nickname.
        self.reply_address_alias = reply_address_alias
        # Specifies whether to use the reply-to address configured in the management console (the address must be verified). Valid values: true or false.
        # 
        # This parameter is required.
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The email subject. The value cannot exceed 256 characters in length.
        # 
        # This parameter is required.
        self.subject = subject
        # The tag created in the DirectMail console. Tags are used to categorize email batches. You can query the sending status of each batch by tag. If the email tracking feature is enabled, you must use an email tag when sending emails.
        # The value must be 1 to 128 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        self.tag_name = tag_name
        # The template information for template-based sending.
        # 
        # When sending with a template, the HtmlBody and TextBody values are ignored.
        self.template_shrink = template_shrink
        # The text body of the email.
        # 
        # Note: HtmlBody and TextBody are used for different types of email content. You must specify one of them.
        # 
        # - The size limit for URL-based parameter passing is approximately 80 KB.
        # - The size limit for Body-based parameter passing with the new SDK is approximately 8 MB (Java 1.4.0 or later, Python3 1.4.0 or later, PHP 1.4.0 or later).
        self.text_body = text_body
        # The destination address. You can specify multiple email addresses separated by commas. A maximum of 100 addresses are supported (mailing lists are supported).
        # 
        # This parameter is required.
        self.to_address = to_address
        # The filtering level. For more information, refer to [Unsubscribe link generation and filtering mechanism](https://help.aliyun.com/document_detail/2689048.html).
        # 
        # Valid values:
        # 
        # - disabled: No filtering is applied.
        # - default: The default policy is used. Batch addresses use sender address-level filtering.
        # - mailfrom: Sender address-level filtering.
        # - mailfrom_domain: Sender domain-level filtering.
        # - edm_id: Account-level filtering.
        self.un_subscribe_filter_level = un_subscribe_filter_level
        # The type of unsubscribe link. Valid values:
        # 
        # - disabled: No unsubscribe link is generated.
        # - default: The default policy is used. An unsubscribe link is generated when emails are sent from batch-type sender addresses to specific domains, such as those containing keywords "gmail", "yahoo", "google", "aol.com", "hotmail", "outlook", or "ymail.com". For more information, refer to [Unsubscribe link generation and filtering mechanism](https://help.aliyun.com/document_detail/2689048.html).
        # 
        # The display language is automatically detected based on the recipient\\"s browser settings.
        self.un_subscribe_link_type = un_subscribe_link_type

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        result['Attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['Attachments'].append(k1.to_map() if k1 else None)

        if self.bcc_address is not None:
            result['BccAddress'] = self.bcc_address

        if self.click_trace is not None:
            result['ClickTrace'] = self.click_trace

        if self.domain_auth is not None:
            result['DomainAuth'] = self.domain_auth

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
            for k1 in m.get('Attachments'):
                temp_model = main_models.SingleSendMailShrinkRequestAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('BccAddress') is not None:
            self.bcc_address = m.get('BccAddress')

        if m.get('ClickTrace') is not None:
            self.click_trace = m.get('ClickTrace')

        if m.get('DomainAuth') is not None:
            self.domain_auth = m.get('DomainAuth')

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

class SingleSendMailShrinkRequestAttachments(DaraModel):
    def __init__(
        self,
        attachment_name: str = None,
        attachment_url: str = None,
    ):
        # Supported only when using the new SDK. Not supported through OpenAPI or signature mechanism methods.
        self.attachment_name = attachment_name
        # Supported only when using the new SDK. Not supported through OpenAPI or signature mechanism methods.
        self.attachment_url = attachment_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

