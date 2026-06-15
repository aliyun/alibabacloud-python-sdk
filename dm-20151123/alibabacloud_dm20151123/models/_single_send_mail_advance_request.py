# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, BinaryIO

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class SingleSendMailAdvanceRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        attachments: List[main_models.SingleSendMailAdvanceRequestAttachments] = None,
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
        template: main_models.SingleSendMailAdvanceRequestTemplate = None,
        text_body: str = None,
        to_address: str = None,
        un_subscribe_filter_level: str = None,
        un_subscribe_link_type: str = None,
    ):
        # The sender address configured in the Direct Mail console.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The address type. Valid values:
        # 
        # `0`: A random account.
        # 
        # `1`: A sender address.
        # 
        # This parameter is required.
        self.address_type = address_type
        # This feature is available only through the latest SDKs. It is not supported for OpenAPI calls or signature-based authentication. For more information, see [How do I send an email with an attachment by using an SDK?](https://help.aliyun.com/document_detail/2937843.html).
        self.attachments = attachments
        # - A comma-separated list of BCC recipients.
        # 
        # - The system sends a copy of the email to each BCC recipient. The BCC information is hidden from all recipients, including those specified in `ToAddress` and `BccAddress`.
        # 
        # - To protect privacy, email tracking features (such as open and click tracking) are disabled for emails sent to BCC recipients. However, billing and sending status are still tracked.
        # 
        # - A maximum of two BCC recipients are allowed per request.
        # 
        # Note: The `SingleSendMail` API operation does not support a CC field. To send carbon copies, use SMTP.
        self.bcc_address = bcc_address
        # Specifies whether to enable click tracking. Valid values: `"1"` enables click tracking, and `"0"` disables it (default).
        self.click_trace = click_trace
        # Specifies whether to enable domain-level authentication.
        # 
        # - `true`
        # 
        # - `false`
        # 
        # This parameter is used only for domain-level authentication. Ignore it for sender address-level authentication.
        # 
        # 1\\. Create the address `domain-auth-created-by-system@example.com` in the console. The prefix must be fixed, and the suffix must be your domain.
        # 
        # 2\\.
        # 
        # **API scenario**
        # 
        # Set `AccountName` to your domain. Recipients will see the sender as `domain-auth-created-by-system@example.com`.
        # 
        # **SMTP scenario**
        # 
        # a. Call the `ModifyPWByDomain` API operation to set a password for the domain.
        # 
        # b. Authenticate with the domain and the configured password. Pass a custom address, such as `user@example.com`, as the actual sender in the `MAIL FROM` command. Recipients will see `user@example.com` as the sender.
        self.domain_auth = domain_auth
        # The sender name. It must be 15 characters or shorter.
        # 
        # For example, if you set the sender name to "Xiaohong" and the sender address is `test***@example.net`, the recipient sees the sender as "Xiaohong" \\<test\\*\\*\\*@example.net>.
        self.from_alias = from_alias
        # Custom email header settings.
        # 
        # Both standard and non-standard fields must comply with standard header syntax. You can specify up to 10 headers for an API call. Excess headers are ignored. This limit does not apply to SMTP.
        # 
        # 1\\. Standard fields
        # 
        # `Message-ID`, `List-Unsubscribe`, `List-Unsubscribe-Post`
        # 
        # Standard fields overwrite existing values in the email header.
        # 
        # 2\\. Non-standard fields
        # 
        # Case-insensitive.
        # 
        # a. Fields starting with `X-User-`: These are not pushed to EventBridge or Message Service (MNS). This prefix is required only for API calls, not for SMTP.
        # 
        # b. Fields starting with `X-User-Notify-`: These are pushed to EventBridge and MNS. This is supported for both API and SMTP calls.
        # 
        # When pushed to EventBridge or MNS, the header object will contain these fields.
        self.headers = headers
        # The HTML body of the email.
        # 
        # Note: You must specify either `HtmlBody` or `TextBody`.
        # 
        # - The size of the body is limited to approximately 80 KB when passed as a URL parameter.
        # 
        # - For recent SDKs (Java 1.4.0+, Python 3 1.4.0+, and PHP 1.4.0+), the request body is limited to approximately 8 MB.
        self.html_body = html_body
        # The ID of the dedicated IP pool. If you have purchased dedicated IPs, you can use this parameter to select which dedicated IP pool to use for sending the email. For more information, see [Dedicated IP](https://help.aliyun.com/document_detail/2932088.html).
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        # The reply-to address.
        self.reply_address = reply_address
        # The name displayed for the reply-to address.
        self.reply_address_alias = reply_address_alias
        # Specifies whether to use the default reply-to address configured in the console. This address must be verified. Valid values: true, false.
        # 
        # This parameter is required.
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The subject of the email, with a maximum length of 256 characters.
        # 
        # This parameter is required.
        self.subject = subject
        # A tag for categorizing email batches, which you can create in the Direct Mail console. Tags allow you to query the sending status of each batch and are required if you enable email tracking. The tag must be 1 to 128 characters long and can contain letters, digits, underscores (_), and hyphens (-).
        self.tag_name = tag_name
        # The template information for sending a templated email.
        self.template = template
        # The text body of the email.
        # 
        # Note: You must specify either `HtmlBody` or `TextBody`.
        # 
        # - The size of the body is limited to approximately 80 KB when passed as a URL parameter.
        # 
        # - For recent SDKs (Java 1.4.0+, Python 3 1.4.0+, and PHP 1.4.0+), the request body is limited to approximately 8 MB.
        self.text_body = text_body
        # The destination email address(es). To specify multiple addresses, separate them with commas (up to 100).
        # 
        # This parameter is required.
        self.to_address = to_address
        # The filtering level. For more information, see [Unsubscribe link generation and filtering mechanism](https://help.aliyun.com/document_detail/2689048.html).
        # 
        # `disabled`: No filtering.
        # 
        # `default`: Uses the default policy. For batch addresses, filtering is applied at the sender address level.
        # 
        # `mailfrom`: Filters at the sender address level.
        # 
        # `mailfrom_domain`: Filters at the sender domain level.
        # 
        # `edm_id`: Filters at the account level.
        self.un_subscribe_filter_level = un_subscribe_filter_level
        # `disabled`: Does not generate an unsubscribe link.
        # 
        # `default`: Uses the default policy. For batch sender addresses, an unsubscribe link is generated when sending to specific domains containing keywords such as "gmail", "yahoo",
        # 
        # "google", "aol.com", "hotmail",
        # 
        # "outlook", and "ymail.com". For more information, see [Unsubscribe link generation and filtering mechanism](https://help.aliyun.com/document_detail/2689048.html).
        # 
        # The display language is automatically determined based on the recipient\\"s browser settings.
        self.un_subscribe_link_type = un_subscribe_link_type

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()
        if self.template:
            self.template.validate()

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
            for k1 in m.get('Attachments'):
                temp_model = main_models.SingleSendMailAdvanceRequestAttachments()
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
            temp_model = main_models.SingleSendMailAdvanceRequestTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        if m.get('TextBody') is not None:
            self.text_body = m.get('TextBody')

        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')

        if m.get('UnSubscribeFilterLevel') is not None:
            self.un_subscribe_filter_level = m.get('UnSubscribeFilterLevel')

        if m.get('UnSubscribeLinkType') is not None:
            self.un_subscribe_link_type = m.get('UnSubscribeLinkType')

        return self

class SingleSendMailAdvanceRequestTemplate(DaraModel):
    def __init__(
        self,
        template_data: Dict[str, str] = None,
        template_id: str = None,
    ):
        # The variables and their values for the template.
        self.template_data = template_data
        # The template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class SingleSendMailAdvanceRequestAttachments(DaraModel):
    def __init__(
        self,
        attachment_name: str = None,
        attachment_url_object: BinaryIO = None,
    ):
        # The filename of the attachment.
        self.attachment_name = attachment_name
        # The local file path of the attachment that the SDK will use.
        self.attachment_url_object = attachment_url_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

