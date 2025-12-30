# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitTraceAbJobRequest(DaraModel):
    def __init__(
        self,
        cipher_base_64ed: str = None,
        input: main_models.SubmitTraceAbJobRequestInput = None,
        level: int = None,
        output: main_models.SubmitTraceAbJobRequestOutput = None,
        start_time: int = None,
        total_time: int = None,
        user_data: str = None,
    ):
        # The key that is encoded by using the Base64 algorithm.
        self.cipher_base_64ed = cipher_base_64ed
        # The source video file for A/B watermarking.
        # 
        # > OSS object or media asset must reside in the same region as the IMS service region. This API supports only videos that last at least 3 minutes. If the video is too short, the call may fail, or no output may be returned.
        # 
        # This parameter is required.
        self.input = input
        # The watermark level, which specifies the channel to embed watermarks. Valid values: 0 specifies the 0u channel, 1 specifies the 1uv channel, and 2 specifies the 2yuv channel.
        self.level = level
        # The output directory path.
        # 
        # This parameter is required.
        self.output = output
        # The start point of watermark embedding. Unit: seconds.
        self.start_time = start_time
        # The duration of the watermark embedding. Unit: seconds.
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
        if self.cipher_base_64ed is not None:
            result['CipherBase64ed'] = self.cipher_base_64ed

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.level is not None:
            result['Level'] = self.level

        if self.output is not None:
            result['Output'] = self.output.to_map()

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
            temp_model = main_models.SubmitTraceAbJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Output') is not None:
            temp_model = main_models.SubmitTraceAbJobRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitTraceAbJobRequestOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The output file. The file can be an OSS object or a media asset. OSS URL formats:
        # 
        # 1\\. oss://bucket/dir/
        # 
        # 2\\. http(s)://bucket.oss-[regionId].aliyuncs.com/dir/
        # 
        # In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and dir specifies the object path in OSS.
        # 
        # This parameter is required.
        self.media = media
        # The type of the output file. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        # 
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

class SubmitTraceAbJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The source file. The file can be an OSS object or a media asset. You can specify the path of an OSS object in one of the following formats:
        # 
        # 1\\. oss://bucket/object
        # 
        # 2\\. http(s)://bucket.oss-[regionId].aliyuncs.com/object
        # 
        # where bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object path in OSS.
        # 
        # This parameter is required.
        self.media = media
        # The type of the source file. Valid values:
        # 
        # 1.  OSS: an OSS object.
        # 2.  Media: a media asset.
        # 
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

