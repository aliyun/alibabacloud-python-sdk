# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class GetTrialAccessChannelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTrialAccessChannelResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business processing status code. A value of OK indicates success. When an exception occurs, the corresponding business error code is returned. The error types and mapping rules follow the current API configuration. No error codes are added or modified in this update.
        self.code = code
        # The channel configuration corresponding to the VisitorToken and its associated scenarios, used for trial page initialization.
        self.data = data
        # The HTTP status code recorded in the business response body. A normal return value is 200. To determine whether the business operation is successful, you must also check the Code field. The presence of this field alone does not indicate a successful call.
        self.http_status_code = http_status_code
        # The business response or error description. It is usually empty or not returned upon success, and a fixed text cannot be required for successful responses. Upon failure, it provides an error description to assist in troubleshooting. Combine it with Code and Params to understand the cause of the error. The example shows an error message when the trial link visitor token expires (corresponding to the Code Expired.VisitorToken) and is for format reference only.
        self.message = message
        # The ID used to associate and troubleshoot this POP request. The value in the response corresponds to the current request. System request parameters are injected by the gateway, and callers do not need to fill in system fields manually.
        self.request_id = request_id
        # Indicates whether the business processing is successful. A value of true indicates success, and false indicates failure. The current general response implementation determines success based on whether the Code is OK.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTrialAccessChannelResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTrialAccessChannelResponseBodyData(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_channel_type: str = None,
        builder_type: str = None,
        channel_scripts: List[main_models.GetTrialAccessChannelResponseBodyDataChannelScripts] = None,
        channel_setting: str = None,
        created_time: int = None,
        expiration_time: int = None,
        instance_id: str = None,
        name: str = None,
        nlu_engine: str = None,
        state: str = None,
        updated_time: int = None,
        visitor_token: str = None,
    ):
        # The ID of the channel associated with the trial link or specific access configuration. When a channel needs to be associated, use the ID actually returned by the channel service. It is not the ChannelId returned by a call, and the two must not be mixed. The configuration layer uses a UUID as the channel ID when creating a new channel.
        self.access_channel_id = access_channel_id
        # Identifies the access source of the current interaction. The configuration layer enumerations are TEST (voice test window or real number outbound call test), TEXT_TEST (text test window), TRIAL (web voice trial link), and TEXT_TRIAL (text trial link). The existing default values and visibility of each API remain unchanged. If the current definition uses the historical value Text, it should be processed according to the existing definition and is not modified in this documentation update.
        self.access_channel_type = access_channel_type
        # The scenario building method. The configuration layer enumerations are FLOW and LITE. This field is not declared in the current business layer channel response object. Therefore, whether it is actually returned depends on the deployment version.
        self.builder_type = builder_type
        # The scenarios associated with this channel and their display, variable, and label configurations. The trial page should use the ScriptId actually returned in the list and must not specify scenarios outside the channel.
        self.channel_scripts = channel_scripts
        # The display configuration of the trial channel, which is a JSON object string. The content is configured during channel creation and agreed upon with the trial page, and may include display information such as Images. The current code does not provide a complete fixed structure, and the empty object in the example only illustrates the serialization format.
        self.channel_setting = channel_setting
        # The creation time of the channel, in Unix timestamp format and measured in milliseconds. It is converted from the creation time of the configuration layer entity.
        self.created_time = created_time
        # The expiration time of the trial channel and the visitor token, in Unix timestamp format and measured in milliseconds. The service compares the validity period with the current system time in milliseconds. Expired tokens cannot continue the trial.
        self.expiration_time = expiration_time
        # The instance identity of the product to which it belongs. You must use an instance that the invoker has permission to access and that actually exists. It must be consistent with the instance to which the scenario, channel, and session belong. The maximum length is subject to the current POP parameter definition.
        self.instance_id = instance_id
        # The name of the trial channel, used for display and identification on the trial page. The content is configured by the channel creator.
        self.name = name
        # The natural language understanding (NLU) engine type defined in the configuration layer. Valid values: BEEBOT, PROMPTS, and FUNCTION. This field is not declared in the current business layer channel response object. Therefore, whether it can be returned through this operation depends on the deployment version and must not be assumed to always exist on the client.
        self.nlu_engine = nlu_engine
        # The channel status. Valid values: Active (effective) and Expired (invalid). Trial access still requires server-side token and validity period verification. You cannot bypass the verification based solely on the status value saved on the client.
        self.state = state
        # The last update time of the channel, in Unix timestamp format and measured in milliseconds. It is converted from the update time of the configuration layer entity.
        self.updated_time = updated_time
        # The visitor token obtained from the trial link. It is used to locate the trial channel and verify access permissions and the validity period. The token is generated by the channel service and must not be constructed manually. It cannot be empty and must be within its validity period. The example is a placeholder value that cannot be used for authentication. Do not disclose actual tokens to unauthorized personnel.
        self.visitor_token = visitor_token

    def validate(self):
        if self.channel_scripts:
            for v1 in self.channel_scripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.access_channel_type is not None:
            result['AccessChannelType'] = self.access_channel_type

        if self.builder_type is not None:
            result['BuilderType'] = self.builder_type

        result['ChannelScripts'] = []
        if self.channel_scripts is not None:
            for k1 in self.channel_scripts:
                result['ChannelScripts'].append(k1.to_map() if k1 else None)

        if self.channel_setting is not None:
            result['ChannelSetting'] = self.channel_setting

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.state is not None:
            result['State'] = self.state

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.visitor_token is not None:
            result['VisitorToken'] = self.visitor_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('BuilderType') is not None:
            self.builder_type = m.get('BuilderType')

        self.channel_scripts = []
        if m.get('ChannelScripts') is not None:
            for k1 in m.get('ChannelScripts'):
                temp_model = main_models.GetTrialAccessChannelResponseBodyDataChannelScripts()
                self.channel_scripts.append(temp_model.from_map(k1))

        if m.get('ChannelSetting') is not None:
            self.channel_setting = m.get('ChannelSetting')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('VisitorToken') is not None:
            self.visitor_token = m.get('VisitorToken')

        return self

class GetTrialAccessChannelResponseBodyDataChannelScripts(DaraModel):
    def __init__(
        self,
        label_configs: str = None,
        script_id: str = None,
        script_name: str = None,
        variable_configs: str = None,
    ):
        # The JSON string of the label configuration exported from the scenario version. The specific fields are determined by the scenario version. The empty JSON array in the example only indicates that there are no configuration items and must not be confused with the call parameter Tags.
        self.label_configs = label_configs
        # The ID of the dialog scenario under the instance. Specify an existing scenario. Subsequent dialogs and end requests for the same text session should use the scenario specified when the session is started.
        self.script_id = script_id
        # The name of the scenario associated with the channel, used for display on the trial page. Use the actual value returned by the service.
        self.script_name = script_name
        # The JSON string of the variable configuration exported from the scenario version. It is not the variable values passed in this interaction. The specific configuration items are determined by the scenario version. The empty JSON array in the example only indicates that there are no configuration items and does not declare unverified internal fields.
        self.variable_configs = variable_configs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_configs is not None:
            result['LabelConfigs'] = self.label_configs

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.variable_configs is not None:
            result['VariableConfigs'] = self.variable_configs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelConfigs') is not None:
            self.label_configs = m.get('LabelConfigs')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('VariableConfigs') is not None:
            self.variable_configs = m.get('VariableConfigs')

        return self

