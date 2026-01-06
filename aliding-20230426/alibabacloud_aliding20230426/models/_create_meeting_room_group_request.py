# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateMeetingRoomGroupRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        parent_group_id: int = None,
        tenant_context: main_models.CreateMeetingRoomGroupRequestTenantContext = None,
    ):
        self.group_name = group_name
        # This parameter is required.
        self.parent_group_id = parent_group_id
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.parent_group_id is not None:
            result['ParentGroupId'] = self.parent_group_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ParentGroupId') is not None:
            self.parent_group_id = m.get('ParentGroupId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.CreateMeetingRoomGroupRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class CreateMeetingRoomGroupRequestTenantContext(DaraModel):
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

