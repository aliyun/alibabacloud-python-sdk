# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerChatFlowShrinkRequest(DaraModel):
    def __init__(
        self,
        claim_time_millis: int = None,
        data_shrink: str = None,
        discard_time_millis: int = None,
        flow_code: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uuid: str = None,
    ):
        # The time when the event occurs. This is when the flow is triggered and is typically the time when the request is created. This is a UNIX timestamp in milliseconds.
        self.claim_time_millis = claim_time_millis
        # The input parameters in a key-value format. The keys must match the input parameter policy configured in the start node of the flow. To view the variable names in the start node, go to the [Flow Editor](https://chatapp.console.aliyun.com/ChatFlowBuilder), click the name of the flow, and open the orchestration canvas.
        self.data_shrink = data_shrink
        # The time when the event expires. If you specify this parameter, the trigger is canceled if the request is not processed before this time. This is a UNIX timestamp in milliseconds.
        self.discard_time_millis = discard_time_millis
        # The code of the flow. View the flow code on the [Flow Editor](https://chatapp.console.aliyun.com/ChatFlowBuilder) page.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # A custom serial number from an external system. Use this parameter to associate the trigger with an external business process. After the flow is triggered, you can retrieve this parameter from within the flow.
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A custom unique ID for the event, used to ensure idempotence. Do not include business semantics in the ID. After the flow is triggered, you can retrieve this parameter from within the flow.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.claim_time_millis is not None:
            result['ClaimTimeMillis'] = self.claim_time_millis

        if self.data_shrink is not None:
            result['Data'] = self.data_shrink

        if self.discard_time_millis is not None:
            result['DiscardTimeMillis'] = self.discard_time_millis

        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClaimTimeMillis') is not None:
            self.claim_time_millis = m.get('ClaimTimeMillis')

        if m.get('Data') is not None:
            self.data_shrink = m.get('Data')

        if m.get('DiscardTimeMillis') is not None:
            self.discard_time_millis = m.get('DiscardTimeMillis')

        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

