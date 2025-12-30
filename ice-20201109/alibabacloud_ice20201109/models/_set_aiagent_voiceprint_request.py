# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SetAIAgentVoiceprintRequest(DaraModel):
    def __init__(
        self,
        input: main_models.SetAIAgentVoiceprintRequestInput = None,
        voiceprint_id: str = None,
    ):
        # The input file.
        self.input = input
        # A unique identifier for the voiceprint. Generate this ID based on your own business rules. Requirement: 1 to 127 characters in length.
        self.voiceprint_id = voiceprint_id

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.SetAIAgentVoiceprintRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        return self

class SetAIAgentVoiceprintRequestInput(DaraModel):
    def __init__(
        self,
        data: str = None,
        format: str = None,
        type: str = None,
    ):
        # The media access link.
        self.data = data
        # The audio file format. Only WAV is supported.
        self.format = format
        # Specifies the access type for the audio file. The system will verify file accessibility via HEAD or GET requests. Valid values:
        # 
        # *   url: An HTTP(S) link to the audio file.
        # 
        # *   oss: An OSS object. Supports the following formats:
        # 
        #     1.  OSS URI: oss://bucket-name/object-key
        # 
        #         Example: oss://my-bucket/audio/sample.wav
        # 
        #     2.  OSS public URL: http(s)://${bucket}.oss-${region}.aliyuncs.com/${object}
        # 
        #         Example: https://my-bucket.oss-cn-hangzhou.aliyuncs.com/audio/sample.wav
        # 
        # >  The OSS bucket must be in the same region as the service. Otherwise, the access fails.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.format is not None:
            result['Format'] = self.format

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

