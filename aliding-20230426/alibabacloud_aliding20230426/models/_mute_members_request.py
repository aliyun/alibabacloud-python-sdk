# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class MuteMembersRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.MuteMembersRequestTenantContext = None,
        user_ids: List[str] = None,
        conference_id: str = None,
        mute_action: str = None,
    ):
        self.tenant_context = tenant_context
        # This parameter is required.
        self.user_ids = user_ids
        # This parameter is required.
        self.conference_id = conference_id
        # This parameter is required.
        self.mute_action = mute_action

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

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.mute_action is not None:
            result['muteAction'] = self.mute_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.MuteMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('muteAction') is not None:
            self.mute_action = m.get('muteAction')

        return self

class MuteMembersRequestTenantContext(DaraModel):
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

