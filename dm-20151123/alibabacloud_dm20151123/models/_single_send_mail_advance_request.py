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
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.address_type = address_type
        self.attachments = attachments
        self.bcc_address = bcc_address
        self.click_trace = click_trace
        self.domain_auth = domain_auth
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

class SingleSendMailAdvanceRequestAttachments(DaraModel):
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

