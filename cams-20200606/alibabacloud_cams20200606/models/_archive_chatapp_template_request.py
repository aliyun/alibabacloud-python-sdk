# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ArchiveChatappTemplateRequest(DaraModel):
    def __init__(
        self,
        archive_type: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        template_list: List[main_models.ArchiveChatappTemplateRequestTemplateList] = None,
    ):
        # The archive type.
        # 
        # This parameter is required.
        self.archive_type = archive_type
        # The channel type. Valid values:
        # 
        # - **WHATSAPP**.
        # 
        # > Only the WhatsApp channel type is supported.
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The space ID of the ISV sub-customer or the instance ID of the direct customer. You can view the Space ID on the <props="china">[Channel Management](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[Channel Management](https://chatapp.console.alibabacloud.com/CustomerList) page.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The template list.
        # 
        # This parameter is required.
        self.template_list = template_list

    def validate(self):
        if self.template_list:
            for v1 in self.template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_type is not None:
            result['ArchiveType'] = self.archive_type

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        result['TemplateList'] = []
        if self.template_list is not None:
            for k1 in self.template_list:
                result['TemplateList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveType') is not None:
            self.archive_type = m.get('ArchiveType')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        self.template_list = []
        if m.get('TemplateList') is not None:
            for k1 in m.get('TemplateList'):
                temp_model = main_models.ArchiveChatappTemplateRequestTemplateList()
                self.template_list.append(temp_model.from_map(k1))

        return self

class ArchiveChatappTemplateRequestTemplateList(DaraModel):
    def __init__(
        self,
        language: str = None,
        template_code: str = None,
    ):
        # The template language. For detailed language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # The template code. You can view the template code on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Template Design** page.
        # 
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

