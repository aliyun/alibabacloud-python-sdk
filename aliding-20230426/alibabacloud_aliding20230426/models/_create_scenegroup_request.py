# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScenegroupRequest(DaraModel):
    def __init__(
        self,
        add_friend_forbidden: int = None,
        all_members_can_create_calendar: int = None,
        all_members_can_create_mcs_conf: int = None,
        chat_banned_type: int = None,
        group_email_disabled: int = None,
        group_live_switch: int = None,
        icon: str = None,
        management_type: int = None,
        members_to_admin_chat: int = None,
        mention_all_authority: int = None,
        only_admin_can_ding: int = None,
        only_admin_can_set_msg_top: int = None,
        searchable: int = None,
        show_history_type: int = None,
        subadmin_ids: str = None,
        template_id: str = None,
        title: str = None,
        user_ids: str = None,
        uuid: str = None,
        validation_type: int = None,
    ):
        self.add_friend_forbidden = add_friend_forbidden
        self.all_members_can_create_calendar = all_members_can_create_calendar
        self.all_members_can_create_mcs_conf = all_members_can_create_mcs_conf
        self.chat_banned_type = chat_banned_type
        self.group_email_disabled = group_email_disabled
        self.group_live_switch = group_live_switch
        self.icon = icon
        self.management_type = management_type
        self.members_to_admin_chat = members_to_admin_chat
        self.mention_all_authority = mention_all_authority
        self.only_admin_can_ding = only_admin_can_ding
        self.only_admin_can_set_msg_top = only_admin_can_set_msg_top
        self.searchable = searchable
        self.show_history_type = show_history_type
        self.subadmin_ids = subadmin_ids
        # This parameter is required.
        self.template_id = template_id
        # This parameter is required.
        self.title = title
        self.user_ids = user_ids
        self.uuid = uuid
        self.validation_type = validation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_friend_forbidden is not None:
            result['AddFriendForbidden'] = self.add_friend_forbidden

        if self.all_members_can_create_calendar is not None:
            result['AllMembersCanCreateCalendar'] = self.all_members_can_create_calendar

        if self.all_members_can_create_mcs_conf is not None:
            result['AllMembersCanCreateMcsConf'] = self.all_members_can_create_mcs_conf

        if self.chat_banned_type is not None:
            result['ChatBannedType'] = self.chat_banned_type

        if self.group_email_disabled is not None:
            result['GroupEmailDisabled'] = self.group_email_disabled

        if self.group_live_switch is not None:
            result['GroupLiveSwitch'] = self.group_live_switch

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.management_type is not None:
            result['ManagementType'] = self.management_type

        if self.members_to_admin_chat is not None:
            result['MembersToAdminChat'] = self.members_to_admin_chat

        if self.mention_all_authority is not None:
            result['MentionAllAuthority'] = self.mention_all_authority

        if self.only_admin_can_ding is not None:
            result['OnlyAdminCanDing'] = self.only_admin_can_ding

        if self.only_admin_can_set_msg_top is not None:
            result['OnlyAdminCanSetMsgTop'] = self.only_admin_can_set_msg_top

        if self.searchable is not None:
            result['Searchable'] = self.searchable

        if self.show_history_type is not None:
            result['ShowHistoryType'] = self.show_history_type

        if self.subadmin_ids is not None:
            result['SubadminIds'] = self.subadmin_ids

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.validation_type is not None:
            result['ValidationType'] = self.validation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddFriendForbidden') is not None:
            self.add_friend_forbidden = m.get('AddFriendForbidden')

        if m.get('AllMembersCanCreateCalendar') is not None:
            self.all_members_can_create_calendar = m.get('AllMembersCanCreateCalendar')

        if m.get('AllMembersCanCreateMcsConf') is not None:
            self.all_members_can_create_mcs_conf = m.get('AllMembersCanCreateMcsConf')

        if m.get('ChatBannedType') is not None:
            self.chat_banned_type = m.get('ChatBannedType')

        if m.get('GroupEmailDisabled') is not None:
            self.group_email_disabled = m.get('GroupEmailDisabled')

        if m.get('GroupLiveSwitch') is not None:
            self.group_live_switch = m.get('GroupLiveSwitch')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('ManagementType') is not None:
            self.management_type = m.get('ManagementType')

        if m.get('MembersToAdminChat') is not None:
            self.members_to_admin_chat = m.get('MembersToAdminChat')

        if m.get('MentionAllAuthority') is not None:
            self.mention_all_authority = m.get('MentionAllAuthority')

        if m.get('OnlyAdminCanDing') is not None:
            self.only_admin_can_ding = m.get('OnlyAdminCanDing')

        if m.get('OnlyAdminCanSetMsgTop') is not None:
            self.only_admin_can_set_msg_top = m.get('OnlyAdminCanSetMsgTop')

        if m.get('Searchable') is not None:
            self.searchable = m.get('Searchable')

        if m.get('ShowHistoryType') is not None:
            self.show_history_type = m.get('ShowHistoryType')

        if m.get('SubadminIds') is not None:
            self.subadmin_ids = m.get('SubadminIds')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('ValidationType') is not None:
            self.validation_type = m.get('ValidationType')

        return self

