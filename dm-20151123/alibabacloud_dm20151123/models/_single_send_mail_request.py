# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class SingleSendMailRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: int = None,
        attachments: List[main_models.SingleSendMailRequestAttachments] = None,
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
        template: main_models.SingleSendMailRequestTemplate = None,
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
        # 0: Random account
        # 
        # 1: Sender address
        # 
        # This parameter is required.
        self.address_type = address_type
        # This feature is available only in the latest software development kit (SDK). It is not supported by OpenAPI or signature mechanisms. For more information, see [How do I send an email with attachments using an SDK?]().
        self.attachments = attachments
        # - The list of blind carbon copy (BCC) recipients.
        # 
        # - A copy of the email is sent to each BCC address. The BCC information is not visible to any recipient, including those in the ToAddress and BccAddress fields.
        # 
        # - To protect the privacy of BCC recipients, email tracking is disabled by default for emails sent to BCC addresses. This means that behavioral data, such as open rates and click-through rates, is not recorded for BCC emails. However, billing, sending details, and sending status statistics are the same as for regular emails.
        # 
        # - You can specify up to two BCC recipients for each email.
        self.bcc_address = bcc_address
        # 1: Enables data tracking.
        # 
        # 0 (default): Disables data tracking.
        self.click_trace = click_trace
        # Enable domain-level authentication.
        # 
        # - true
        # 
        # - false
        # 
        # Use this only for domain-level authentication. Ignore it for sender address-level authentication.
        # 
        # 1\\. Create the \\`domain-auth-created-by-system\\@example.com\\` address in the console. Keep the prefix before the at sign (@) fixed and use your own domain as the suffix.
        # 
        # 2\\.
        # 
        # **API scenario**
        # 
        # Set \\`AccountName\\` to your domain. The recipient sees the sender as \\`domain-auth-created-by-system\\@example.com\\`.
        # 
        # **SMTP scenario**
        # 
        # a. Set the domain password using the \\`ModifyPWByDomain\\` API.
        # 
        # b. Authenticate using the domain and the set password. For the actual sender, pass a custom address, such as \\`user\\@example.com\\`, in the \\`mailfrom\\` field. The recipient sees the sender as \\`user\\@example.com\\`.
        self.domain_auth = domain_auth
        # The nickname of the sender. The nickname must be fewer than 15 characters.
        # 
        # For example, if you set the nickname to "Xiao Hong" and the sender address is test\\*\\*\\*@example.net, the recipient sees the sender as "Xiao Hong" \\<test\\*\\*\\*@example.net>.
        self.from_alias = from_alias
        # Message header settings
        # 
        # Both standard and non-standard fields must follow the syntax rules for message headers. The API supports a maximum of 10 headers in the headers field. Any headers exceeding this limit are ignored. SMTP, however, does not have this limit.
        # 
        # 1\\. Standard fields
        # 
        # Message-ID, List-Unsubscribe, List-Unsubscribe-Post
        # 
        # Standard fields overwrite existing values in the message header.
        # 
        # 2\\. Non-standard fields
        # 
        # Case-insensitive
        # 
        # a. Fields that start with X-User- (These are not pushed to the EventBridge event bus or Message Service MNS. They are required only for the API, whereas SMTP supports any custom header.)
        # 
        # b. Fields that start with X-User-Notify- (These are pushed to the EventBridge event bus and Message Service MNS, and are supported by both the API and SMTP.)
        # 
        # When pushed to EventBridge or MNS, these fields appear in the header field.
        self.headers = headers
        # The HTML body of the email.
        # 
        # Note: Specify HtmlBody or TextBody.
        # 
        # - The size of the parameter passed in a URL is limited to approximately 80 KB.
        # 
        # - The new SDK limits the body parameter to approximately 8 MB (Java 1.4.0 and later, Python 3 1.4.0 and later, PHP 1.4.0 and later).
        self.html_body = html_body
        # The ID of the dedicated IP address pool. If you purchased dedicated IP addresses, use this parameter to specify the outbound IP address for the current email. For more information, see [Dedicated IPs]().
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        # The reply-to address.
        self.reply_address = reply_address
        # The nickname of the reply-to address.
        self.reply_address_alias = reply_address_alias
        # Specifies whether to use the reply-to address configured in the console. The reply-to address must be verified. Valid values: true and false.
        # 
        # This parameter is required.
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The subject of the email. The subject cannot exceed 256 characters in length.
        # 
        # This parameter is required.
        self.subject = subject
        # The email tag that you create in the Direct Mail console. Use tags to classify email batches and query the sending status of each batch. If email tracking is enabled, you must specify an email tag.
        # The tag can be 1 to 128 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        self.tag_name = tag_name
        # The template information for sending template-based emails.
        self.template = template
        # The text body of the email.
        # 
        # Note: Specify HtmlBody or TextBody.
        # 
        # - The size of the parameter passed in a URL is limited to approximately 80 KB.
        # 
        # - The new SDK limits the body parameter to approximately 8 MB (Java 1.4.0 and later, Python 3 1.4.0 and later, PHP 1.4.0 and later).
        self.text_body = text_body
        # The destination address. To specify multiple addresses, separate them with commas (,). You can specify a maximum of 100 addresses. Recipient groups are supported.
        # 
        # This parameter is required.
        self.to_address = to_address
        # The filtering level. For more information, see [Unsubscribe link generation and filtering mechanism]().
        # 
        # disabled: No filtering.
        # 
        # default: The default policy is used. Batch addresses are filtered at the sender address level.
        # 
        # mailfrom: Filters at the sender address level.
        # 
        # mailfrom_domain: Filters at the email domain level.
        # 
        # edm_id: Filters at the account level.
        self.un_subscribe_filter_level = un_subscribe_filter_level
        # disabled: No link is generated.
        # 
        # default: The default policy is used. An unsubscribe link is generated for batch emails sent to specific domains, such as domains that contain keywords like "gmail", "yahoo",
        # "google", "aol.com", "hotmail",
        # "outlook", or "ymail.com". For more information, see [Unsubscribe link generation and filtering mechanism]().
        # 
        # The display language is automatically detected based on the recipient\\"s browser settings.
        # 
        # "outlook", or "ymail.com". For more information, see [Unsubscribe link generation and filtering mechanism]().
        # 
        # The display language is automatically detected based on the recipient\\"s browser settings.
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
                temp_model = main_models.SingleSendMailRequestAttachments()
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
            temp_model = main_models.SingleSendMailRequestTemplate()
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

class SingleSendMailRequestTemplate(DaraModel):
    def __init__(
        self,
        template_data: Dict[str, str] = None,
        template_id: str = None,
    ):
        # The variables and their values in the template.
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

class SingleSendMailRequestAttachments(DaraModel):
    def __init__(
        self,
        attachment_name: str = None,
        attachment_url: str = None,
    ):
        # This feature is available only in the latest SDK. It is not supported by OpenAPI or signature mechanisms.
        self.attachment_name = attachment_name
        # This feature is available only in the latest SDK. It is not supported by OpenAPI or signature mechanisms.
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

