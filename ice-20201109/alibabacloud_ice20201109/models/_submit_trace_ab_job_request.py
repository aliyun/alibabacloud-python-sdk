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
        # The Base64-encoded encryption key.
        self.cipher_base_64ed = cipher_base_64ed
        # The input video for the A/B stream forensic watermarking job.
        # 
        # > - The Object Storage Service (OSS) file or media asset must be in the same region where Intelligent Media Services (IMS) is deployed.
        # >
        # > - This operation supports only videos that are three minutes or longer. Using a shorter video may cause the API call to fail or produce no output.
        # 
        # This parameter is required.
        self.input = input
        # The watermark level, which specifies the embedding channel. Valid values: `0` (U channel), `1` (UV channels), and `2` (YUV channels).
        self.level = level
        # The output location for the A/B stream job. This must be an OSS directory.
        # 
        # This parameter is required.
        self.output = output
        # The start time for watermark embedding, in seconds.
        self.start_time = start_time
        # The total duration for watermark embedding, in seconds.
        self.total_time = total_time
        # User data to include in the request. The maximum length is 1,024 bytes.
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
        # The output path. Specify an OSS directory URL or a media asset ID. If you specify an OSS URL, use one of the following formats for the output directory:
        # 
        # 1\\. `oss://<bucket>/<dir>/`
        # 
        # 2\\. `http(s)://<bucket>.oss-[regionId].aliyuncs.com/<dir>/`
        # 
        # In these formats, `<bucket>` is the name of the OSS bucket, which must be in the same region as your project, and `<dir>` is the output directory path.
        # 
        # This parameter is required.
        self.media = media
        # The type of the output object.
        # Valid values:
        # 
        # - `OSS`: An OSS object.
        # 
        # - `Media`: A media asset ID.
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
        # The location of the input file. This can be an OSS URL or a media asset ID.
        # The supported OSS URL formats are:
        # 
        # 1\\. `oss://<bucket>/<object>`
        # 
        # 2\\. `http(s)://<bucket>.oss-[regionId].aliyuncs.com/<object>`
        # 
        # In these formats, `<bucket>` is the name of the OSS bucket, which must be in the same region as your project, and `<object>` is the path to the file.
        # 
        # This parameter is required.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1. `OSS`: The file is specified by an OSS URL.
        # 
        # 2. `Media`: The file is specified by a media asset ID.
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

