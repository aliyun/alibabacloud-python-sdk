# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ArchiveChatappTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        archive_type: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        template_list_shrink: str = None,
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
        self.template_list_shrink = template_list_shrink

    def validate(self):
        pass

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

        if self.template_list_shrink is not None:
            result['TemplateList'] = self.template_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveType') is not None:
            self.archive_type = m.get('ArchiveType')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('TemplateList') is not None:
            self.template_list_shrink = m.get('TemplateList')

        return self

