# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDingtalkProjectionListShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        code: str = None,
        current_page: int = None,
        org_id: int = None,
        page_size: int = None,
        projector_work_no: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.code = code
        self.current_page = current_page
        self.org_id = org_id
        self.page_size = page_size
        self.projector_work_no = projector_work_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.code is not None:
            result['code'] = self.code

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.projector_work_no is not None:
            result['projectorWorkNo'] = self.projector_work_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('projectorWorkNo') is not None:
            self.projector_work_no = m.get('projectorWorkNo')

        return self

