# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitTraceExtractJobRequest(DaraModel):
    def __init__(
        self,
        input: main_models.SubmitTraceExtractJobRequestInput = None,
        params: str = None,
        user_data: str = None,
    ):
        # The input video from which to extract the watermark.
        # 
        # > - The OSS object or media asset must be in the same region as your IMS service.
        # 
        # This parameter is required.
        self.input = input
        # Extraction job parameters, specified as a JSON string. The following parameters are supported:
        # 
        # - `m3u8Type`: The algorithm type. The default value is `v1`.
        # 
        #   - `v1`: Extracts an m3u8 playlist with absolute paths.
        # 
        #   - `v2`: Extracts an m3u8 playlist with relative paths.
        self.params = params
        # The user-defined data. Maximum length: 1,024 bytes.
        self.user_data = user_data

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

        if self.params is not None:
            result['Params'] = self.params

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.SubmitTraceExtractJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitTraceExtractJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The input source. Specify an OSS object URL or a media asset ID.
        # 
        # An OSS object URL can be in one of the following formats:
        # 
        # 1\\. oss\\://bucket/object
        # 
        # In these formats, `bucket` is the name of an OSS bucket in the same region as your IMS service, and `object` is the path of the OSS object.
        # 
        # This parameter is required.
        self.media = media
        # The input type. Valid values:
        # 
        # - OSS: An OSS object URL.
        # 
        # - Media: A media asset ID.
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

