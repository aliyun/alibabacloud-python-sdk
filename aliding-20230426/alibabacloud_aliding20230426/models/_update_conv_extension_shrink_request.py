# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConvExtensionShrinkRequest(DaraModel):
    def __init__(
        self,
        mobile_url: str = None,
        pc_url: str = None,
        staff_id_list_shrink: str = None,
        system_uid: str = None,
        tenant_context_shrink: str = None,
    ):
        self.mobile_url = mobile_url
        self.pc_url = pc_url
        self.staff_id_list_shrink = staff_id_list_shrink
        self.system_uid = system_uid
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile_url is not None:
            result['MobileUrl'] = self.mobile_url

        if self.pc_url is not None:
            result['PcUrl'] = self.pc_url

        if self.staff_id_list_shrink is not None:
            result['StaffIdList'] = self.staff_id_list_shrink

        if self.system_uid is not None:
            result['SystemUid'] = self.system_uid

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MobileUrl') is not None:
            self.mobile_url = m.get('MobileUrl')

        if m.get('PcUrl') is not None:
            self.pc_url = m.get('PcUrl')

        if m.get('StaffIdList') is not None:
            self.staff_id_list_shrink = m.get('StaffIdList')

        if m.get('SystemUid') is not None:
            self.system_uid = m.get('SystemUid')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

