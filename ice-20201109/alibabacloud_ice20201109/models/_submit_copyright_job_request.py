# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitCopyrightJobRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        input: main_models.SubmitCopyrightJobRequestInput = None,
        level: int = None,
        message: str = None,
        output: main_models.SubmitCopyrightJobRequestOutput = None,
        params: str = None,
        start_time: int = None,
        total_time: int = None,
        user_data: str = None,
    ):
        # The description of the watermark.
        self.description = description
        # The source video file that you want to add a watermark to.
        # 
        # > The OSS object or media asset must reside in the same region as the IMS service region.
        # 
        # This parameter is required.
        self.input = input
        # The watermark level, which specifies the channel to embed watermarks. Valid values: 0 specifies the 0u channel, 1 specifies the 1uv channel, and 2 specifies the 2yuv channel.
        self.level = level
        # The information about the watermark to be added.
        # 
        # This parameter is required.
        self.message = message
        # The URL of the output file.
        # 
        # > The OSS bucket must reside in the same region as the IMS service region.
        # 
        # This parameter is required.
        self.output = output
        # The parameters related to watermark jobs. The value is a JSON string. Supported parameter:
        # 
        # *   algoType: the algorithm type. Default value: v1.
        # 
        #     *   v1: watermarking for long videos that last at least 3 minutes.
        #     *   v2: watermarking for videos shorter than 3 minutes.
        self.params = params
        # The start time of the watermark. Unit: seconds. If you do not specify this parameter, the default value 0 is used.
        self.start_time = start_time
        # The end time of the watermark. Unit: seconds. If you do not specify this parameter, the default value is the video duration.
        self.total_time = total_time
        # The custom data, which can be up to 1,024 bytes in size.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.params is not None:
            result['Params'] = self.params

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Input') is not None:
            temp_model = main_models.SubmitCopyrightJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Output') is not None:
            temp_model = main_models.SubmitCopyrightJobRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitCopyrightJobRequestOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.media = media
        # This parameter is required.
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

class SubmitCopyrightJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.media = media
        # This parameter is required.
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

