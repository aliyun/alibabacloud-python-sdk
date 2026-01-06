# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class SetConferenceHostsRequest(DaraModel):
    def __init__(
        self,
        operation_type: str = None,
        tenant_context: main_models.SetConferenceHostsRequestTenantContext = None,
        user_ids: List[str] = None,
        conference_id: str = None,
    ):
        # This parameter is required.
        self.operation_type = operation_type
        self.tenant_context = tenant_context
        # This parameter is required.
        self.user_ids = user_ids
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
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('TenantContext') is not None:
            temp_model = main_models.SetConferenceHostsRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        return self

class SetConferenceHostsRequestTenantContext(DaraModel):
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

