# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MakeCallRequest(DaraModel):
    def __init__(
        self,
        callee: str = None,
        caller: str = None,
        device_id: str = None,
        flash_sms_variables: str = None,
        instance_id: str = None,
        masked_callee: str = None,
        media_type: str = None,
        tags: str = None,
        timeout_seconds: int = None,
        user_id: str = None,
    ):
        # Callee number. For internal calls, specify the target agent\\"s extension number in this field. For outbound calls, specify the customer\\"s phone number.
        # 
        # This parameter is required.
        self.callee = callee
        # Caller number. This parameter is invalid for internal calls. For outbound calls, specify an outbound number available to the current agent. Ensure that the number supports outbound calling and that the agent has permission to use it. Permission can be granted in two ways: either by attaching the number to the skill group the agent signed into, or by setting the number as the agent\\"s personal outbound number.
        self.caller = caller
        # Device ID. This field is meaningless and can be filled with any value.
        self.device_id = device_id
        # Flash SMS configuration
        self.flash_sms_variables = flash_sms_variables
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The desensitized callee number. If this field is not empty, it indicates that the callee number must be desensitized. The desensitization rule is defined by the customer. You only need to enter the desensitized callee number here. Using a desensitized callee number means that in certain scenarios, you will see the desensitized callee number and cannot view the real callee number.
        self.masked_callee = masked_callee
        # Media type. The default value is AUDIO. Other valid values include VIDEO.
        self.media_type = media_type
        # Ingest endpoint data. The customer does not need to concern themselves with this.
        self.tags = tags
        # Timeout. If the call is not answered within the time specified by this parameter, the system automatically hangs up. Valid values range from 30 to 300 seconds.
        self.timeout_seconds = timeout_seconds
        # Agent ID initiating the outbound call. This field is optional. If not specified, the system uses the agent mapped to the current RAM user by default.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.flash_sms_variables is not None:
            result['FlashSmsVariables'] = self.flash_sms_variables

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.masked_callee is not None:
            result['MaskedCallee'] = self.masked_callee

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('FlashSmsVariables') is not None:
            self.flash_sms_variables = m.get('FlashSmsVariables')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaskedCallee') is not None:
            self.masked_callee = m.get('MaskedCallee')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

