# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFlowVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        flow_version: str = None,
        flow_view_model: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        type: str = None,
    ):
        # The business tenant code. Default value: ALICOM_OPAAS.
        self.biz_code = biz_code
        # The business extension information. Default value: an empty collection.
        self.biz_extend_shrink = biz_extend_shrink
        # The flow code. You can view the flow code on the [flow editor](https://chatapp.console.aliyun.com/ChatFlowBuilder) page.
        self.flow_code = flow_code
        # The flow version. You can click a flow name on the [flow editor](https://chatapp.console.aliyun.com/ChatFlowBuilder) page to go to the flow editor canvas page and view the flow version.
        self.flow_version = flow_version
        # The DSL data of the flow version. This is a JSON-formatted data string. You can orchestrate flow components on the flow editor canvas in advance, save the flow, and then click **Settings** > **Export** in the upper-right corner of the canvas orchestration page to export a JSON-formatted data file for viewing.
        self.flow_view_model = flow_view_model
        self.owner_id = owner_id
        # The version remarks.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The save type.
        self.type = type

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

        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        if self.flow_view_model is not None:
            result['FlowViewModel'] = self.flow_view_model

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')

        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        if m.get('FlowViewModel') is not None:
            self.flow_view_model = m.get('FlowViewModel')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

