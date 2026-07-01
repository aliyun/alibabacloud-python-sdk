# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTraceAbJobShrinkRequest(DaraModel):
    def __init__(
        self,
        cipher_base_64ed: str = None,
        input_shrink: str = None,
        level: int = None,
        output_shrink: str = None,
        start_time: int = None,
        total_time: int = None,
        user_data: str = None,
    ):
        # The Base64-encoded encryption key.
        self.cipher_base_64ed = cipher_base_64ed
        # The input video for the A/B stream forensic watermarking job.
        # 
        # > - The Object Storage Service (OSS) file or media asset must be in the same region where Intelligent Media Services (IMS) is deployed.
        # >
        # > - This operation supports only videos that are three minutes or longer. Using a shorter video may cause the API call to fail or produce no output.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The watermark level, which specifies the embedding channel. Valid values: `0` (U channel), `1` (UV channels), and `2` (YUV channels).
        self.level = level
        # The output location for the A/B stream job. This must be an OSS directory.
        # 
        # This parameter is required.
        self.output_shrink = output_shrink
        # The start time for watermark embedding, in seconds.
        self.start_time = start_time
        # The total duration for watermark embedding, in seconds.
        self.total_time = total_time
        # User data to include in the request. The maximum length is 1,024 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cipher_base_64ed is not None:
            result['CipherBase64ed'] = self.cipher_base_64ed

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.level is not None:
            result['Level'] = self.level

        if self.output_shrink is not None:
            result['Output'] = self.output_shrink

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CipherBase64ed') is not None:
            self.cipher_base_64ed = m.get('CipherBase64ed')

        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Output') is not None:
            self.output_shrink = m.get('Output')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

