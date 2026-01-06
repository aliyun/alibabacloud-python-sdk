# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdateVideoConferenceSettingRequest(DaraModel):
    def __init__(
        self,
        allow_unmute_self: bool = None,
        auto_transfer_host: bool = None,
        forbidden_share_screen: bool = None,
        lock_conference: bool = None,
        mute_all: bool = None,
        only_internal_employees_join: bool = None,
        tenant_context: main_models.UpdateVideoConferenceSettingRequestTenantContext = None,
        conference_id: str = None,
    ):
        self.allow_unmute_self = allow_unmute_self
        self.auto_transfer_host = auto_transfer_host
        self.forbidden_share_screen = forbidden_share_screen
        self.lock_conference = lock_conference
        self.mute_all = mute_all
        self.only_internal_employees_join = only_internal_employees_join
        self.tenant_context = tenant_context
        # This parameter is required.
        self.conference_id = conference_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_unmute_self is not None:
            result['AllowUnmuteSelf'] = self.allow_unmute_self

        if self.auto_transfer_host is not None:
            result['AutoTransferHost'] = self.auto_transfer_host

        if self.forbidden_share_screen is not None:
            result['ForbiddenShareScreen'] = self.forbidden_share_screen

        if self.lock_conference is not None:
            result['LockConference'] = self.lock_conference

        if self.mute_all is not None:
            result['MuteAll'] = self.mute_all

        if self.only_internal_employees_join is not None:
            result['OnlyInternalEmployeesJoin'] = self.only_internal_employees_join

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUnmuteSelf') is not None:
            self.allow_unmute_self = m.get('AllowUnmuteSelf')

        if m.get('AutoTransferHost') is not None:
            self.auto_transfer_host = m.get('AutoTransferHost')

        if m.get('ForbiddenShareScreen') is not None:
            self.forbidden_share_screen = m.get('ForbiddenShareScreen')

        if m.get('LockConference') is not None:
            self.lock_conference = m.get('LockConference')

        if m.get('MuteAll') is not None:
            self.mute_all = m.get('MuteAll')

        if m.get('OnlyInternalEmployeesJoin') is not None:
            self.only_internal_employees_join = m.get('OnlyInternalEmployeesJoin')

        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdateVideoConferenceSettingRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        return self

class UpdateVideoConferenceSettingRequestTenantContext(DaraModel):
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

