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
        # The declared occurrence time of the event, usually the time when the request was constructed, in milliseconds timestamp.
        self.claim_time_millis = claim_time_millis
        # Input parameters in Key-Value format. The Key must match the input strategy configured at the start node of your flow.
        self.data_shrink = data_shrink
        # The time when the event should be discarded, i.e., the expiration time. If this field is specified, the message will be discarded if it exceeds this time, in milliseconds timestamp.
        self.discard_time_millis = discard_time_millis
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # External system transaction number, used to associate with external business system transactions. You can retrieve this parameter within the flow after triggering.
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Unique event ID used for idempotent triggers. Do not include any business semantics; you can retrieve this parameter within the flow after triggering.
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

