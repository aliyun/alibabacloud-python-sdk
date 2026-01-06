# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdateScheduleConferenceRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        schedule_conference_id: str = None,
        start_time: int = None,
        tenant_context: main_models.UpdateScheduleConferenceRequestTenantContext = None,
        title: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.schedule_conference_id = schedule_conference_id
        # This parameter is required.
        self.start_time = start_time
        self.tenant_context = tenant_context
        # This parameter is required.
        self.title = title

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.schedule_conference_id is not None:
            result['ScheduleConferenceId'] = self.schedule_conference_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ScheduleConferenceId') is not None:
            self.schedule_conference_id = m.get('ScheduleConferenceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdateScheduleConferenceRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class UpdateScheduleConferenceRequestTenantContext(DaraModel):
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

