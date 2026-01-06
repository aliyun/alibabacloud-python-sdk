# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdateConvExtensionRequest(DaraModel):
    def __init__(
        self,
        mobile_url: str = None,
        pc_url: str = None,
        staff_id_list: List[str] = None,
        system_uid: str = None,
        tenant_context: main_models.UpdateConvExtensionRequestTenantContext = None,
    ):
        self.mobile_url = mobile_url
        self.pc_url = pc_url
        self.staff_id_list = staff_id_list
        self.system_uid = system_uid
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile_url is not None:
            result['MobileUrl'] = self.mobile_url

        if self.pc_url is not None:
            result['PcUrl'] = self.pc_url

        if self.staff_id_list is not None:
            result['StaffIdList'] = self.staff_id_list

        if self.system_uid is not None:
            result['SystemUid'] = self.system_uid

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MobileUrl') is not None:
            self.mobile_url = m.get('MobileUrl')

        if m.get('PcUrl') is not None:
            self.pc_url = m.get('PcUrl')

        if m.get('StaffIdList') is not None:
            self.staff_id_list = m.get('StaffIdList')

        if m.get('SystemUid') is not None:
            self.system_uid = m.get('SystemUid')

        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdateConvExtensionRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class UpdateConvExtensionRequestTenantContext(DaraModel):
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

