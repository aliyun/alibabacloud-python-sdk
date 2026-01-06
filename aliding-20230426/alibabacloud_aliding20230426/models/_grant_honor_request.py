# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GrantHonorRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.GrantHonorRequestTenantContext = None,
        expiration_time: int = None,
        grant_reason: str = None,
        granter_name: str = None,
        honor_id: str = None,
        notice_announcer: bool = None,
        notice_single: bool = None,
        open_conversation_ids: List[str] = None,
        org_id: int = None,
        receiver_user_ids: List[str] = None,
        sender_user_id: str = None,
    ):
        self.tenant_context = tenant_context
        self.expiration_time = expiration_time
        # This parameter is required.
        self.grant_reason = grant_reason
        # This parameter is required.
        self.granter_name = granter_name
        # This parameter is required.
        self.honor_id = honor_id
        self.notice_announcer = notice_announcer
        self.notice_single = notice_single
        self.open_conversation_ids = open_conversation_ids
        # This parameter is required.
        self.org_id = org_id
        # This parameter is required.
        self.receiver_user_ids = receiver_user_ids
        # This parameter is required.
        self.sender_user_id = sender_user_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        if self.grant_reason is not None:
            result['grantReason'] = self.grant_reason

        if self.granter_name is not None:
            result['granterName'] = self.granter_name

        if self.honor_id is not None:
            result['honorId'] = self.honor_id

        if self.notice_announcer is not None:
            result['noticeAnnouncer'] = self.notice_announcer

        if self.notice_single is not None:
            result['noticeSingle'] = self.notice_single

        if self.open_conversation_ids is not None:
            result['openConversationIds'] = self.open_conversation_ids

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.receiver_user_ids is not None:
            result['receiverUserIds'] = self.receiver_user_ids

        if self.sender_user_id is not None:
            result['senderUserId'] = self.sender_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.GrantHonorRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        if m.get('grantReason') is not None:
            self.grant_reason = m.get('grantReason')

        if m.get('granterName') is not None:
            self.granter_name = m.get('granterName')

        if m.get('honorId') is not None:
            self.honor_id = m.get('honorId')

        if m.get('noticeAnnouncer') is not None:
            self.notice_announcer = m.get('noticeAnnouncer')

        if m.get('noticeSingle') is not None:
            self.notice_single = m.get('noticeSingle')

        if m.get('openConversationIds') is not None:
            self.open_conversation_ids = m.get('openConversationIds')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('receiverUserIds') is not None:
            self.receiver_user_ids = m.get('receiverUserIds')

        if m.get('senderUserId') is not None:
            self.sender_user_id = m.get('senderUserId')

        return self

class GrantHonorRequestTenantContext(DaraModel):
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

