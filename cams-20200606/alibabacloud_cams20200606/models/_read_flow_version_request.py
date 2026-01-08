# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ReadFlowVersionRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow version status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend

        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')

        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

