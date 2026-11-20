# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigXShrinkRequest(DaraModel):
    def __init__(
        self,
        call_ability: str = None,
        caller_parent_id: int = None,
        customer_pool_key: str = None,
        gnflag: str = None,
        owner_id: int = None,
        req_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sequence_calls_shrink: str = None,
        sequence_mode: str = None,
        sms_ability: str = None,
        sms_sign_mode: str = None,
        tel_x: str = None,
    ):
        # Specifies whether to enable the call capability. Valid values:
        # 
        # - 0: Disable.
        # 
        # - 1: Enable.
        self.call_ability = call_ability
        # The customer UID.
        self.caller_parent_id = caller_parent_id
        # The key of the number pool.
        # 
        # This parameter is required.
        self.customer_pool_key = customer_pool_key
        # Specifies whether to pass through the caller ID to display the actual caller. Valid values:
        # 
        # - 00: No pass-through. The work number is displayed when either party calls the other.
        # 
        # - 10: Pass-through. When Customer A is the caller, the caller ID displayed to Employee B is the number of Customer A. When Employee B is the caller, the caller ID displayed to Customer A is the work number.
        # 
        # Default value: 00.
        self.gnflag = gnflag
        self.owner_id = owner_id
        # The request deduplication ID. The maximum length of reqId is 20 characters. The caller must ensure atomicity.
        # 
        # This parameter is required.
        self.req_id = req_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The sequential ringing control parameters.
        self.sequence_calls_shrink = sequence_calls_shrink
        # The sequential ringing mode. Valid values:
        # 
        # - 0: No sequential ringing. This is the default value.
        # 
        # - 1: Conditional sequential ringing. The system first connects to the callee specified by calledNo. If the callee cannot be connected, the system sequentially rings the numbers in the sequenceCalls list.
        # 
        # - 2: Unconditional sequential ringing. The system does not connect to the callee specified by calledNo and directly sequentially rings the numbers in the sequenceCalls list.
        self.sequence_mode = sequence_mode
        # Specifies whether to enable the SMS feature. Valid values:
        # 
        # - 0: Disable.
        # 
        # - 1: Enable.
        self.sms_ability = sms_ability
        # Specifies whether to pass through the SMS signature to display the actual user. Valid values:
        # 
        # - 0: No pass-through.
        # 
        # - 1: Pass-through.
        # 
        # Default value: 0.
        self.sms_sign_mode = sms_sign_mode
        # The X number.
        # 
        # This parameter is required.
        self.tel_x = tel_x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_ability is not None:
            result['CallAbility'] = self.call_ability

        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id

        if self.customer_pool_key is not None:
            result['CustomerPoolKey'] = self.customer_pool_key

        if self.gnflag is not None:
            result['GNFlag'] = self.gnflag

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sequence_calls_shrink is not None:
            result['SequenceCalls'] = self.sequence_calls_shrink

        if self.sequence_mode is not None:
            result['SequenceMode'] = self.sequence_mode

        if self.sms_ability is not None:
            result['SmsAbility'] = self.sms_ability

        if self.sms_sign_mode is not None:
            result['SmsSignMode'] = self.sms_sign_mode

        if self.tel_x is not None:
            result['TelX'] = self.tel_x

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallAbility') is not None:
            self.call_ability = m.get('CallAbility')

        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')

        if m.get('CustomerPoolKey') is not None:
            self.customer_pool_key = m.get('CustomerPoolKey')

        if m.get('GNFlag') is not None:
            self.gnflag = m.get('GNFlag')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SequenceCalls') is not None:
            self.sequence_calls_shrink = m.get('SequenceCalls')

        if m.get('SequenceMode') is not None:
            self.sequence_mode = m.get('SequenceMode')

        if m.get('SmsAbility') is not None:
            self.sms_ability = m.get('SmsAbility')

        if m.get('SmsSignMode') is not None:
            self.sms_sign_mode = m.get('SmsSignMode')

        if m.get('TelX') is not None:
            self.tel_x = m.get('TelX')

        return self

