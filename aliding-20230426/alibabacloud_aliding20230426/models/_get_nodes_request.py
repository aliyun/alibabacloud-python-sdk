# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetNodesRequest(DaraModel):
    def __init__(
        self,
        node_ids: List[str] = None,
        option: main_models.GetNodesRequestOption = None,
        tenant_context: main_models.GetNodesRequestTenantContext = None,
    ):
        # This parameter is required.
        self.node_ids = node_ids
        self.option = option
        self.tenant_context = tenant_context

    def validate(self):
        if self.option:
            self.option.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.option is not None:
            result['Option'] = self.option.to_map()

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('Option') is not None:
            temp_model = main_models.GetNodesRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('TenantContext') is not None:
            temp_model = main_models.GetNodesRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class GetNodesRequestTenantContext(DaraModel):
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

class GetNodesRequestOption(DaraModel):
    def __init__(
        self,
        with_permission_role: bool = None,
        with_statistical_info: bool = None,
    ):
        self.with_permission_role = with_permission_role
        self.with_statistical_info = with_statistical_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.with_permission_role is not None:
            result['WithPermissionRole'] = self.with_permission_role

        if self.with_statistical_info is not None:
            result['WithStatisticalInfo'] = self.with_statistical_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WithPermissionRole') is not None:
            self.with_permission_role = m.get('WithPermissionRole')

        if m.get('WithStatisticalInfo') is not None:
            self.with_statistical_info = m.get('WithStatisticalInfo')

        return self

