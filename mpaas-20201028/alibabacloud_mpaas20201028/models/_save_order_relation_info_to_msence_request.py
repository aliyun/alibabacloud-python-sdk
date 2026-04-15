# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveOrderRelationInfoToMsenceRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        app_id: str = None,
        biz_order_id: str = None,
        biz_order_status: int = None,
        custom_id: str = None,
        mini_program_id: str = None,
        open_uid: str = None,
        platform_id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.amount = amount
        self.app_id = app_id
        self.biz_order_id = biz_order_id
        self.biz_order_status = biz_order_status
        self.custom_id = custom_id
        self.mini_program_id = mini_program_id
        self.open_uid = open_uid
        self.platform_id = platform_id
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.biz_order_id is not None:
            result['BizOrderId'] = self.biz_order_id

        if self.biz_order_status is not None:
            result['BizOrderStatus'] = self.biz_order_status

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.mini_program_id is not None:
            result['MiniProgramId'] = self.mini_program_id

        if self.open_uid is not None:
            result['OpenUid'] = self.open_uid

        if self.platform_id is not None:
            result['PlatformId'] = self.platform_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BizOrderId') is not None:
            self.biz_order_id = m.get('BizOrderId')

        if m.get('BizOrderStatus') is not None:
            self.biz_order_status = m.get('BizOrderStatus')

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('MiniProgramId') is not None:
            self.mini_program_id = m.get('MiniProgramId')

        if m.get('OpenUid') is not None:
            self.open_uid = m.get('OpenUid')

        if m.get('PlatformId') is not None:
            self.platform_id = m.get('PlatformId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

