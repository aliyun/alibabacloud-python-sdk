# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitAIAgentVideoAuditTaskRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        audit_interval: int = None,
        callback_config: main_models.SubmitAIAgentVideoAuditTaskRequestCallbackConfig = None,
        capture_policies: List[main_models.SubmitAIAgentVideoAuditTaskRequestCapturePolicies] = None,
        input: main_models.SubmitAIAgentVideoAuditTaskRequestInput = None,
        user_data: str = None,
    ):
        # The ID of the AI agent.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        # The interval, in milliseconds, at which to submit captured frames to the AI agent. Valid values: 0 to 5000. Default value: 3000. If it is set to 0, all captured frames are sent to the model in a single batch request. Otherwise, frames are sent sequentially with the specified interval between each request.
        self.audit_interval = audit_interval
        # Callback configurations.
        self.callback_config = callback_config
        # An array of frame-capturing policies. Each policy defines a set of frames to be analyzed and will generate a separate result from the model.
        # 
        # This parameter is required.
        self.capture_policies = capture_policies
        # The details of the input file.
        # 
        # This parameter is required.
        self.input = input
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.callback_config:
            self.callback_config.validate()
        if self.capture_policies:
            for v1 in self.capture_policies:
                 if v1:
                    v1.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiagent_id is not None:
            result['AIAgentId'] = self.aiagent_id

        if self.audit_interval is not None:
            result['AuditInterval'] = self.audit_interval

        if self.callback_config is not None:
            result['CallbackConfig'] = self.callback_config.to_map()

        result['CapturePolicies'] = []
        if self.capture_policies is not None:
            for k1 in self.capture_policies:
                result['CapturePolicies'].append(k1.to_map() if k1 else None)

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('AuditInterval') is not None:
            self.audit_interval = m.get('AuditInterval')

        if m.get('CallbackConfig') is not None:
            temp_model = main_models.SubmitAIAgentVideoAuditTaskRequestCallbackConfig()
            self.callback_config = temp_model.from_map(m.get('CallbackConfig'))

        self.capture_policies = []
        if m.get('CapturePolicies') is not None:
            for k1 in m.get('CapturePolicies'):
                temp_model = main_models.SubmitAIAgentVideoAuditTaskRequestCapturePolicies()
                self.capture_policies.append(temp_model.from_map(k1))

        if m.get('Input') is not None:
            temp_model = main_models.SubmitAIAgentVideoAuditTaskRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitAIAgentVideoAuditTaskRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The OSS URL of the input file. Format:
        # 
        # http(s)://{BucketName}.{Endpoint}/{ObjectName}
        self.media = media
        # The type of the input file. Valid values:
        # 
        # *   OSS: an OSS object.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitAIAgentVideoAuditTaskRequestCapturePolicies(DaraModel):
    def __init__(
        self,
        duration: int = None,
        frame_count: int = None,
        prompt: str = None,
        start_time: int = None,
    ):
        # The duration over which to capture the specified number of frames. Unit: seconds.
        self.duration = duration
        # The number of frames to capture.
        self.frame_count = frame_count
        # The text prompt to send to the MLLM along with the captured frames.
        self.prompt = prompt
        # The timestamp in the video at which to start capturing frames. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class SubmitAIAgentVideoAuditTaskRequestCallbackConfig(DaraModel):
    def __init__(
        self,
        token: str = None,
        url: str = None,
    ):
        # The authentication token for callback.
        self.token = token
        # The URL for receiving callback notifications.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.token is not None:
            result['Token'] = self.token

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

