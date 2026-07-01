# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitCopyrightExtractJobRequest(DaraModel):
    def __init__(
        self,
        input: main_models.SubmitCopyrightExtractJobRequestInput = None,
        params: str = None,
        user_data: str = None,
    ):
        # The video file for watermark extraction.
        # 
        # > - The region of the Object Storage Service (OSS) file or media asset must match the region of the current Intelligent Media Service (IMS) instance.
        # 
        # This parameter is required.
        self.input = input
        # The watermark job parameters, specified as a JSON string.
        # 
        # - algoType: The algorithm type. Default value: v1. The extraction algorithm type must match the algorithm type used for embedding the watermark.
        # 
        #   - v1: The copyright extraction algorithm for long-form videos.
        # 
        #   - v2: The copyright extraction algorithm for short-form videos.
        self.params = params
        # The user-defined data. The maximum length is 1,024 bytes.
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
            temp_model = main_models.SubmitCopyrightExtractJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitCopyrightExtractJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # Specifies the URL of an Object Storage Service (OSS) object or the ID of a media asset.
        # OSS URLs can be in the following formats:
        # 
        # 1\\. oss\\://bucket/object
        # 
        # 2\\. http(s)://bucket.oss-[regionId].aliyuncs.com/object
        # 
        # In these formats, `bucket` is the name of a bucket in the same region as your IMS instance, and `object` is the file path.
        # 
        # This parameter is required.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1. OSS: The URL of a file in Object Storage Service (OSS).
        # 
        # 2. Media: The ID of a media asset.
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

