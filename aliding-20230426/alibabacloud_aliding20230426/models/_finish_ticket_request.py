# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class FinishTicketRequest(DaraModel):
    def __init__(
        self,
        notify: main_models.FinishTicketRequestNotify = None,
        open_team_id: str = None,
        open_ticket_id: str = None,
        tenant_context: main_models.FinishTicketRequestTenantContext = None,
        ticket_memo: main_models.FinishTicketRequestTicketMemo = None,
    ):
        self.notify = notify
        # This parameter is required.
        self.open_team_id = open_team_id
        # This parameter is required.
        self.open_ticket_id = open_ticket_id
        self.tenant_context = tenant_context
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.tenant_context:
            self.tenant_context.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notify is not None:
            result['Notify'] = self.notify.to_map()

        if self.open_team_id is not None:
            result['OpenTeamId'] = self.open_team_id

        if self.open_ticket_id is not None:
            result['OpenTicketId'] = self.open_ticket_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.ticket_memo is not None:
            result['TicketMemo'] = self.ticket_memo.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Notify') is not None:
            temp_model = main_models.FinishTicketRequestNotify()
            self.notify = temp_model.from_map(m.get('Notify'))

        if m.get('OpenTeamId') is not None:
            self.open_team_id = m.get('OpenTeamId')

        if m.get('OpenTicketId') is not None:
            self.open_ticket_id = m.get('OpenTicketId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.FinishTicketRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('TicketMemo') is not None:
            temp_model = main_models.FinishTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m.get('TicketMemo'))

        return self

class FinishTicketRequestTicketMemo(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.FinishTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        self.attachments = attachments
        self.memo = memo

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
        result['Attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['Attachments'].append(k1.to_map() if k1 else None)

        if self.memo is not None:
            result['Memo'] = self.memo

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('Attachments') is not None:
            for k1 in m.get('Attachments'):
                temp_model = main_models.FinishTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        return self

class FinishTicketRequestTicketMemoAttachments(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        self.file_name = file_name
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class FinishTicketRequestTenantContext(DaraModel):
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

class FinishTicketRequestNotify(DaraModel):
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

