# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetScenegroupResponseBody(DaraModel):
    def __init__(
        self,
        group_url: str = None,
        icon: str = None,
        management_options: main_models.GetScenegroupResponseBodyManagementOptions = None,
        open_conversation_id: str = None,
        owner_staff_id: str = None,
        request_id: str = None,
        sub_admin_staff_ids: List[str] = None,
        template_id: str = None,
        title: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.group_url = group_url
        self.icon = icon
        self.management_options = management_options
        self.open_conversation_id = open_conversation_id
        self.owner_staff_id = owner_staff_id
        self.request_id = request_id
        self.sub_admin_staff_ids = sub_admin_staff_ids
        self.template_id = template_id
        self.title = title
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.management_options:
            self.management_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_url is not None:
            result['groupUrl'] = self.group_url

        if self.icon is not None:
            result['icon'] = self.icon

        if self.management_options is not None:
            result['managementOptions'] = self.management_options.to_map()

        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id

        if self.owner_staff_id is not None:
            result['ownerStaffId'] = self.owner_staff_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.sub_admin_staff_ids is not None:
            result['subAdminStaffIds'] = self.sub_admin_staff_ids

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.title is not None:
            result['title'] = self.title

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupUrl') is not None:
            self.group_url = m.get('groupUrl')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('managementOptions') is not None:
            temp_model = main_models.GetScenegroupResponseBodyManagementOptions()
            self.management_options = temp_model.from_map(m.get('managementOptions'))

        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')

        if m.get('ownerStaffId') is not None:
            self.owner_staff_id = m.get('ownerStaffId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('subAdminStaffIds') is not None:
            self.sub_admin_staff_ids = m.get('subAdminStaffIds')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetScenegroupResponseBodyManagementOptions(DaraModel):
    def __init__(
        self,
        chat_banned_type: str = None,
        management_type: str = None,
        mention_all_authority: str = None,
        searchable: str = None,
        show_history_type: str = None,
        validation_type: str = None,
    ):
        self.chat_banned_type = chat_banned_type
        self.management_type = management_type
        self.mention_all_authority = mention_all_authority
        self.searchable = searchable
        self.show_history_type = show_history_type
        self.validation_type = validation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_banned_type is not None:
            result['ChatBannedType'] = self.chat_banned_type

        if self.management_type is not None:
            result['ManagementType'] = self.management_type

        if self.mention_all_authority is not None:
            result['MentionAllAuthority'] = self.mention_all_authority

        if self.searchable is not None:
            result['Searchable'] = self.searchable

        if self.show_history_type is not None:
            result['ShowHistoryType'] = self.show_history_type

        if self.validation_type is not None:
            result['ValidationType'] = self.validation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatBannedType') is not None:
            self.chat_banned_type = m.get('ChatBannedType')

        if m.get('ManagementType') is not None:
            self.management_type = m.get('ManagementType')

        if m.get('MentionAllAuthority') is not None:
            self.mention_all_authority = m.get('MentionAllAuthority')

        if m.get('Searchable') is not None:
            self.searchable = m.get('Searchable')

        if m.get('ShowHistoryType') is not None:
            self.show_history_type = m.get('ShowHistoryType')

        if m.get('ValidationType') is not None:
            self.validation_type = m.get('ValidationType')

        return self

