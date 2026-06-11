# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetWorkspaceQuotaRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        client_token: str = None,
        cu_quota: int = None,
        region: str = None,
        workspace_id: str = None,
    ):
        # Specifies whether to enable auto-payment for the order.
        self.auto_pay = auto_pay
        # A unique, client-generated token to ensure request idempotence. The token can contain only ASCII characters and must be no longer than 64 characters. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The compute unit (CU) quota for the workspace.
        # 
        # This parameter is required.
        self.cu_quota = cu_quota
        # The ID of the region.
        # 
        # This parameter is required.
        self.region = region
        # The ID of the Data Management Service (DMS) workspace.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cu_quota is not None:
            result['CuQuota'] = self.cu_quota

        if self.region is not None:
            result['Region'] = self.region

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CuQuota') is not None:
            self.cu_quota = m.get('CuQuota')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

