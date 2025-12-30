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
        # The source video file from which to extract the watermark.
        # 
        # > The OSS object or media asset must reside in the same region as the IMS service region.
        # 
        # This parameter is required.
        self.input = input
        # Additional parameters for the watermark job, provided as a JSON string. Supported parameter:
        # 
        # *   algoType: The algorithm type. Defaults to v1. The extraction algorithm must match the one used for embedding.
        # 
        #     *   v1: Copyright watermark extraction algorithm for long videos.
        #     *   v2: Copyright watermark extraction algorithm for short videos.
        self.params = params
        # The custom data, which can be up to 1,024 bytes in size.
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
        # The specific information for the input file, which can be an OSS URL or a media asset ID. OSS URL formats:
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

