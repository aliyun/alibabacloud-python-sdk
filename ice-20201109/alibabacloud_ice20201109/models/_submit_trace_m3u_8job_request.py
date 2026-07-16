# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitTraceM3u8JobRequest(DaraModel):
    def __init__(
        self,
        key_uri: str = None,
        output: main_models.SubmitTraceM3u8JobRequestOutput = None,
        params: str = None,
        trace: str = None,
        trace_media_id: str = None,
    ):
        # The URI of the key server.
        self.key_uri = key_uri
        # The OSS destination for the output M3U8 file.
        # 
        # > The OSS bucket must be in the same region as your MPS service.
        # 
        # This parameter is required.
        self.output = output
        # A JSON string that contains parameters for the watermarking job. The following parameter is supported:
        # 
        # - `m3u8Type`: The algorithm type. The default value is `v1`.
        # 
        #   - `v1`: Generates an M3U8 file that uses an absolute path. The file can be played directly. The signature is valid for 24 hours. After expiration, you must submit a new job to get a new M3U8 file.
        # 
        #   - `v2`: Generates an M3U8 file that uses a relative path. This file must be stored in the same directory as the TS files.
        self.params = params
        # The watermark content to embed.
        self.trace = trace
        # The media ID of the processed A/B stream for video watermarking for tracing. This ID is returned in the response when you submit the A/B stream job.
        self.trace_media_id = trace_media_id

    def validate(self):
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_uri is not None:
            result['KeyUri'] = self.key_uri

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.params is not None:
            result['Params'] = self.params

        if self.trace is not None:
            result['Trace'] = self.trace

        if self.trace_media_id is not None:
            result['TraceMediaId'] = self.trace_media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyUri') is not None:
            self.key_uri = m.get('KeyUri')

        if m.get('Output') is not None:
            temp_model = main_models.SubmitTraceM3u8JobRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Trace') is not None:
            self.trace = m.get('Trace')

        if m.get('TraceMediaId') is not None:
            self.trace_media_id = m.get('TraceMediaId')

        return self

class SubmitTraceM3u8JobRequestOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The output file path. Only OSS paths are supported. You can use one of the following formats:
        # 
        # 1\\. `oss://bucket/object`
        # 
        # 2\\. `http(s)://bucket.oss-[regionId].aliyuncs.com/object`. In these formats, `bucket` specifies the name of an OSS bucket in the same region as your project, and `object` specifies the file path.
        # 
        # This parameter is required.
        self.media = media
        # The type of the output destination. Valid values:
        # 
        # 1. `OSS`: an OSS file location.
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

