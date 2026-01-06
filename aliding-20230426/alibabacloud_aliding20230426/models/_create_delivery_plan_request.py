# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateDeliveryPlanRequest(DaraModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        end_time: int = None,
        res_id: str = None,
        start_time: int = None,
        tenant_context: main_models.CreateDeliveryPlanRequestTenantContext = None,
        user_id_list: List[str] = None,
    ):
        self.content = content
        self.end_time = end_time
        self.res_id = res_id
        self.start_time = start_time
        self.tenant_context = tenant_context
        self.user_id_list = user_id_list

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.res_id is not None:
            result['ResId'] = self.res_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ResId') is not None:
            self.res_id = m.get('ResId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TenantContext') is not None:
            temp_model = main_models.CreateDeliveryPlanRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        return self

class CreateDeliveryPlanRequestTenantContext(DaraModel):
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

