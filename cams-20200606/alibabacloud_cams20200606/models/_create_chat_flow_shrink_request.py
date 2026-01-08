# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatFlowShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_trigger_type: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        title: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow trigger type
        self.flow_trigger_type = flow_trigger_type
        self.owner_id = owner_id
        # Flow remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink

        if self.flow_trigger_type is not None:
            result['FlowTriggerType'] = self.flow_trigger_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')

        if m.get('FlowTriggerType') is not None:
            self.flow_trigger_type = m.get('FlowTriggerType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

