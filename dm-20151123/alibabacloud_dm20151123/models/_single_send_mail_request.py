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
        # The sending address configured in the management console.
        # 
        # This parameter is required.
        self.account_name = account_name
        # Address type. Values:
        # 
        # 0: Random account
        # 
        # 1: Sending address
        # 
        # This parameter is required.
        self.address_type = address_type
        # Only supported for use with the new version of the SDK; not currently supported by openapi and signature mechanisms.
        self.attachments = attachments
        self.bcc_address = bcc_address
        # 1: Enable data tracking function
        # 
        # 0 (default): Disable data tracking function.
        self.click_trace = click_trace
        self.domain_auth = domain_auth
        # Sender alias, with a maximum length of 15 characters.
        # 
        # For example, if the sender alias is set to "Xiaohong" and the sending address is test***@example.net, the recipient will see the sending address as "Xiaohong" <test***@example.net>.
        self.from_alias = from_alias
        # Currently, the standard fields that can be added to the email header are Message-ID, List-Unsubscribe, and List-Unsubscribe-Post. Standard fields will overwrite the existing values in the email header, while non-standard fields need to start with X-User- and will be appended to the email header.
        # Currently, up to 10 headers can be passed in JSON format, and both standard and non-standard fields must comply with the syntax requirements for headers.
        self.headers = headers
        # Email HTML body, limited to 80K by the SDK. Note: HtmlBody and TextBody are for different types of email content, and one of them must be provided.
        self.html_body = html_body
        # dedicated IP pool ID. Users who have purchased an dedicated IP can use this parameter to specify the outgoing IP for this email.
        self.ip_pool_id = ip_pool_id
        self.owner_id = owner_id
        # Reply-to address
        self.reply_address = reply_address
        # Reply-to address alias
        self.reply_address_alias = reply_address_alias
        # Whether to enable the reply-to address configured in the management console (the status must be verified). The value range is the string `true` or `false` (not a boolean value).
        # 
        # This parameter is required.
        self.reply_to_address = reply_to_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Email subject, with a maximum length of 100 characters.
        # 
        # This parameter is required.
        self.subject = subject
        # A tag created in the email push console, used to categorize batches of sent emails. You can use tags to query the sending status of each batch. Additionally, if the email tracking feature is enabled, you must use an email tag when sending emails.
        self.tag_name = tag_name
        self.template = template
        # Email text body, limited to 80K by the SDK. Note: HtmlBody and TextBody are for different types of email content, and one of them must be provided.
        self.text_body = text_body
        # Recipient addresses. Multiple email addresses can be separated by commas, with a maximum of 100 addresses (supports mailing lists).
        # 
        # This parameter is required.
        self.to_address = to_address
        # Filtering level. Refer to the [Unsubscribe Function Link Generation and Filtering Mechanism](https://help.aliyun.com/document_detail/2689048.html) document.
        # 
        # disabled: Do not filter
        # 
        # default: Use the default strategy, bulk addresses use the sending address level filtering
        # 
        # mailfrom: Sending address level filtering
        # 
        # mailfrom_domain: Sending domain level filtering
        # 
        # edm_id: Account level filtering
        self.un_subscribe_filter_level = un_subscribe_filter_level
        # Type of generated unsubscribe link. Refer to the [Unsubscribe Function Link Generation and Filtering Mechanism](https://help.aliyun.com/document_detail/2689048.html) document.
        # 
        # disabled: Do not generate
        # 
        # default: Use the default strategy: Generate unsubscribe links for bulk-type sending addresses to specific domains, such as those containing the keywords "gmail", "yahoo",
        # 
        # "google", "aol.com", "hotmail",
        # 
        # "outlook", "ymail.com", etc.
        # 
        # zh-cn: Generate, for future content preparation
        # 
        # en-us: Generate, for future content preparation
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
        self.template_data = template_data
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
        # Only supported for use with the new version of the SDK; not currently supported by openapi and signature mechanisms.
        self.attachment_name = attachment_name
        # Only supported for use with the new version of the SDK; not currently supported by openapi and signature mechanisms.
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

