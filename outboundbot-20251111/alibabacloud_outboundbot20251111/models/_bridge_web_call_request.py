# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BridgeWebCallRequest(DaraModel):
    def __init__(
        self,
        caller: str = None,
        device_id: str = None,
        draft_version: bool = None,
        instance_id: str = None,
        sample_rate: int = None,
        script_id: str = None,
        tags: str = None,
        timeout_seconds: int = None,
    ):
        # The caller information used to display and associate with the web call. This is not equivalent to the actual outbound caller phone number. If not provided or left empty, the current web call implementation uses the caller identifier as the caller display information.
        self.caller = caller
        # Identifies the client device that initiates the web voice call or receives data channel events. The same client must use the same DeviceId when obtaining data channel credentials and initiating a call. The example is only a business device identifier, not a real credential assigned by the platform.
        self.device_id = device_id
        # Specifies the scenario version. A value of true indicates that the draft version is used. A value of false indicates that the published version is used. This is not a scenario publishing operation. Ensure that the selected scenario version exists before calling the operation.
        self.draft_version = draft_version
        # The instance identity of the associated product. You must use an existing instance that the invoker has permission to access. The instance must be consistent with the instance to which the scenario, channel, and session belong. The maximum length is subject to the current POP parameter definition.
        self.instance_id = instance_id
        # The audio sample rate for the web voice, in Hz. The backend default is 8000. The sample rate must match the client audio and gateway capabilities. The current API code does not define a complete list of allowed values, and other sample rates are not documented as guaranteed supported enumerations.
        self.sample_rate = sample_rate
        # The dialogue scenario ID under the instance. Specify an existing scenario. Subsequent dialogue and end requests for the same text session must use the scenario specified when the session is started.
        self.script_id = script_id
        # The attached data string passed to the call link in key=value format. Separate multiple key-value pairs with semicolons instead of using JSON. For example, the web call service can read the Callee key to obtain the called party information. The example number is a placeholder value. Specify actual values based on your integration agreements. Do not overwrite internal tags that do not belong to the business custom scope.
        self.tags = tags
        # The timeout for waiting for the call to be answered, in seconds. If the call is not answered within this period, it is actively hung up. The default value on the backend is 60 seconds. This does not represent the maximum duration of an answered call. The current request object does not declare additional upper and lower limits, and unverified value ranges are not added to the documentation.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller is not None:
            result['Caller'] = self.caller

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.draft_version is not None:
            result['DraftVersion'] = self.draft_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DraftVersion') is not None:
            self.draft_version = m.get('DraftVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

