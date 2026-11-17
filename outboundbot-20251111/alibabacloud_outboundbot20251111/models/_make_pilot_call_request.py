# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MakePilotCallRequest(DaraModel):
    def __init__(
        self,
        call_variables: str = None,
        device_id: str = None,
        draft_version: bool = None,
        instance_id: str = None,
        number: str = None,
        script_id: str = None,
        tags: str = None,
        verification_code: str = None,
    ):
        # The variables passed to the phone call link. The value is a JSON object string, and variable values are processed as strings. Specific variable names are agreed upon by the call link and business scenario. This parameter is not semicolon-separated Tags. The example uses an empty object when no custom variables are defined.
        self.call_variables = call_variables
        # The ID of the client device that initiates the web voice or receives data channel events. The same client must use the same DeviceId when obtaining data channel credentials and initiating a call. The example is only a business device ID and not a real credential assigned by the platform.
        # 
        # This parameter is required.
        self.device_id = device_id
        # Specifies whether to use the draft version. Valid values:
        # - true: Uses the draft version.
        # - false: Uses the published version.
        # This parameter does not publish the scenario. Ensure that the selected scenario version exists before you call this operation.
        # 
        # This parameter is required.
        self.draft_version = draft_version
        # The instance identity of the product. You must use an instance that the invoker has access to and that actually exists. The instance must be consistent with the instance to which the scenario, channel, and session belong. The maximum length is subject to the current POP parameter definition.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The called phone number for the current real-number outbound call test. The number must be the same as the one used to obtain the SMS verification code. Specify a number that is actually supported by the business and authorized. The current request object only requires this parameter to be non-empty. This document does not fabricate number formats or international number support scopes.
        # 
        # This parameter is required.
        self.number = number
        # The dialog scenario ID of the instance. Specify an existing scenario. Subsequent dialog and end requests for the same text session must use the scenario specified when the session is started.
        # 
        # This parameter is required.
        self.script_id = script_id
        # The attached data string passed to the call link. Use the key=value format. Separate multiple key-value pairs with semicolons. Do not use JSON. For example, the Callee key can be used by the web call service to read the called party information. The example number is a placeholder value. Specify the actual value based on the access conventions of your business. Do not overwrite internal tags that do not belong to the business custom scope.
        self.tags = tags
        # The SMS verification code sent to the number specified by Number for the verification of the OutboundCallTest scenario. The request must use a valid verification code actually received by the number. The example only demonstrates a string parameter and cannot be used to pass the verification. It also does not declare undefined length rules for the code.
        # 
        # This parameter is required.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_variables is not None:
            result['CallVariables'] = self.call_variables

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.draft_version is not None:
            result['DraftVersion'] = self.draft_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number is not None:
            result['Number'] = self.number

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallVariables') is not None:
            self.call_variables = m.get('CallVariables')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DraftVersion') is not None:
            self.draft_version = m.get('DraftVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')

        return self

