# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetDingtalkMeetingMetricDataRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.GetDingtalkMeetingMetricDataRequestTenantContext = None,
        begin_time: int = None,
        conference_id: str = None,
        end_time: int = None,
        org_id: str = None,
        type_name: str = None,
        work_no: str = None,
    ):
        self.tenant_context = tenant_context
        self.begin_time = begin_time
        # This parameter is required.
        self.conference_id = conference_id
        self.end_time = end_time
        self.org_id = org_id
        self.type_name = type_name
        self.work_no = work_no

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

        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.type_name is not None:
            result['typeName'] = self.type_name

        if self.work_no is not None:
            result['workNo'] = self.work_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.GetDingtalkMeetingMetricDataRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('typeName') is not None:
            self.type_name = m.get('typeName')

        if m.get('workNo') is not None:
            self.work_no = m.get('workNo')

        return self

class GetDingtalkMeetingMetricDataRequestTenantContext(DaraModel):
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

