# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCopyrightJobShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        input_shrink: str = None,
        level: int = None,
        message: str = None,
        output_shrink: str = None,
        params: str = None,
        start_time: int = None,
        total_time: int = None,
        user_data: str = None,
    ):
        # A description of the watermark job.
        self.description = description
        # The input video file to be watermarked.
        # 
        # > - The OSS object or media asset must be in the same region as the service call.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The watermark level, which specifies the embedding channel. Valid values are 0, 1, and 2, which correspond to the U, UV, and YUV channels, respectively.
        self.level = level
        # The watermark content to embed.
        # 
        # This parameter is required.
        self.message = message
        # The location of the output file.
        # 
        # > - The OSS bucket must be in the same region as the service call.
        # 
        # This parameter is required.
        self.output_shrink = output_shrink
        # The parameters for the watermark job, specified as a JSON string. The following parameter is supported:
        # 
        # - `algoType`: The algorithm type. Defaults to `v1`.
        # 
        #   - `v1`: For videos 3 minutes or longer.
        # 
        #   - `v2`: For short videos.
        self.params = params
        # The start time of the watermark in seconds. Defaults to 0.
        self.start_time = start_time
        # The end time of the watermark in seconds. If unspecified, the watermark is applied until the video ends.
        self.total_time = total_time
        # The user data. The value can be up to 1,024 bytes in length.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.output_shrink is not None:
            result['Output'] = self.output_shrink

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
            self.input_shrink = m.get('Input')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Output') is not None:
            self.output_shrink = m.get('Output')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

