# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatFlowShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        create_from_flow_code: str = None,
        create_from_flow_version: str = None,
        flow_trigger_type: str = None,
        life_cycle_extend_data_shrink: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        title: str = None,
    ):
        # The business tenant code. Default value: ALICOM_OPAAS.
        self.biz_code = biz_code
        # The business extension information. Default value: an empty collection.
        self.biz_extend_shrink = biz_extend_shrink
        # The source flowCode for creation.
        self.create_from_flow_code = create_from_flow_code
        # The source flowVersion for creation.
        self.create_from_flow_version = create_from_flow_version
        # The flow trigger type. Valid values:
        #  - TriggeredManually
        # - TriggeredByWhatsApp
        # - TriggeredByMessenger
        # - TriggeredByInstagram
        # - TriggeredByViber
        self.flow_trigger_type = flow_trigger_type
        # The lifecycle extension input parameters.
        self.life_cycle_extend_data_shrink = life_cycle_extend_data_shrink
        self.owner_id = owner_id
        # The flow remarks.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The flow title.
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

        if self.create_from_flow_code is not None:
            result['CreateFromFlowCode'] = self.create_from_flow_code

        if self.create_from_flow_version is not None:
            result['CreateFromFlowVersion'] = self.create_from_flow_version

        if self.flow_trigger_type is not None:
            result['FlowTriggerType'] = self.flow_trigger_type

        if self.life_cycle_extend_data_shrink is not None:
            result['LifeCycleExtendData'] = self.life_cycle_extend_data_shrink

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

        if m.get('CreateFromFlowCode') is not None:
            self.create_from_flow_code = m.get('CreateFromFlowCode')

        if m.get('CreateFromFlowVersion') is not None:
            self.create_from_flow_version = m.get('CreateFromFlowVersion')

        if m.get('FlowTriggerType') is not None:
            self.flow_trigger_type = m.get('FlowTriggerType')

        if m.get('LifeCycleExtendData') is not None:
            self.life_cycle_extend_data_shrink = m.get('LifeCycleExtendData')

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

