# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateTicketRequest(DaraModel):
    def __init__(
        self,
        custom_fields: str = None,
        notify: main_models.CreateTicketRequestNotify = None,
        open_team_id: str = None,
        open_template_biz_id: str = None,
        processor_user_ids: List[str] = None,
        scene: str = None,
        scene_context: main_models.CreateTicketRequestSceneContext = None,
        tenant_context: main_models.CreateTicketRequestTenantContext = None,
        title: str = None,
    ):
        self.custom_fields = custom_fields
        self.notify = notify
        # This parameter is required.
        self.open_team_id = open_team_id
        # This parameter is required.
        self.open_template_biz_id = open_template_biz_id
        # This parameter is required.
        self.processor_user_ids = processor_user_ids
        # This parameter is required.
        self.scene = scene
        self.scene_context = scene_context
        self.tenant_context = tenant_context
        # This parameter is required.
        self.title = title

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.scene_context:
            self.scene_context.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_fields is not None:
            result['CustomFields'] = self.custom_fields

        if self.notify is not None:
            result['Notify'] = self.notify.to_map()

        if self.open_team_id is not None:
            result['OpenTeamId'] = self.open_team_id

        if self.open_template_biz_id is not None:
            result['OpenTemplateBizId'] = self.open_template_biz_id

        if self.processor_user_ids is not None:
            result['ProcessorUserIds'] = self.processor_user_ids

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.scene_context is not None:
            result['SceneContext'] = self.scene_context.to_map()

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomFields') is not None:
            self.custom_fields = m.get('CustomFields')

        if m.get('Notify') is not None:
            temp_model = main_models.CreateTicketRequestNotify()
            self.notify = temp_model.from_map(m.get('Notify'))

        if m.get('OpenTeamId') is not None:
            self.open_team_id = m.get('OpenTeamId')

        if m.get('OpenTemplateBizId') is not None:
            self.open_template_biz_id = m.get('OpenTemplateBizId')

        if m.get('ProcessorUserIds') is not None:
            self.processor_user_ids = m.get('ProcessorUserIds')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SceneContext') is not None:
            temp_model = main_models.CreateTicketRequestSceneContext()
            self.scene_context = temp_model.from_map(m.get('SceneContext'))

        if m.get('TenantContext') is not None:
            temp_model = main_models.CreateTicketRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CreateTicketRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class CreateTicketRequestSceneContext(DaraModel):
    def __init__(
        self,
        group_msgs: List[main_models.CreateTicketRequestSceneContextGroupMsgs] = None,
        open_conversation_id: str = None,
        relevantor_user_ids: List[str] = None,
        topic_id: str = None,
    ):
        self.group_msgs = group_msgs
        self.open_conversation_id = open_conversation_id
        self.relevantor_user_ids = relevantor_user_ids
        self.topic_id = topic_id

    def validate(self):
        if self.group_msgs:
            for v1 in self.group_msgs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GroupMsgs'] = []
        if self.group_msgs is not None:
            for k1 in self.group_msgs:
                result['GroupMsgs'].append(k1.to_map() if k1 else None)

        if self.open_conversation_id is not None:
            result['OpenConversationId'] = self.open_conversation_id

        if self.relevantor_user_ids is not None:
            result['RelevantorUserIds'] = self.relevantor_user_ids

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_msgs = []
        if m.get('GroupMsgs') is not None:
            for k1 in m.get('GroupMsgs'):
                temp_model = main_models.CreateTicketRequestSceneContextGroupMsgs()
                self.group_msgs.append(temp_model.from_map(k1))

        if m.get('OpenConversationId') is not None:
            self.open_conversation_id = m.get('OpenConversationId')

        if m.get('RelevantorUserIds') is not None:
            self.relevantor_user_ids = m.get('RelevantorUserIds')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self

class CreateTicketRequestSceneContextGroupMsgs(DaraModel):
    def __init__(
        self,
        anchor: bool = None,
        open_msg_id: str = None,
    ):
        self.anchor = anchor
        self.open_msg_id = open_msg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.open_msg_id is not None:
            result['OpenMsgId'] = self.open_msg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('OpenMsgId') is not None:
            self.open_msg_id = m.get('OpenMsgId')

        return self

class CreateTicketRequestNotify(DaraModel):
    def __init__(
        self,
        group_notice_receiver_user_ids: List[str] = None,
        notice_all_group_member: bool = None,
        work_notice_receiver_user_ids: List[str] = None,
    ):
        self.group_notice_receiver_user_ids = group_notice_receiver_user_ids
        self.notice_all_group_member = notice_all_group_member
        self.work_notice_receiver_user_ids = work_notice_receiver_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_notice_receiver_user_ids is not None:
            result['GroupNoticeReceiverUserIds'] = self.group_notice_receiver_user_ids

        if self.notice_all_group_member is not None:
            result['NoticeAllGroupMember'] = self.notice_all_group_member

        if self.work_notice_receiver_user_ids is not None:
            result['WorkNoticeReceiverUserIds'] = self.work_notice_receiver_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupNoticeReceiverUserIds') is not None:
            self.group_notice_receiver_user_ids = m.get('GroupNoticeReceiverUserIds')

        if m.get('NoticeAllGroupMember') is not None:
            self.notice_all_group_member = m.get('NoticeAllGroupMember')

        if m.get('WorkNoticeReceiverUserIds') is not None:
            self.work_notice_receiver_user_ids = m.get('WorkNoticeReceiverUserIds')

        return self

