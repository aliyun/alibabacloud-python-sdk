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
        # The OSS URL of the output M3U8 file.
        # 
        # > The OSS bucket must reside in the same region as the service region.
        # 
        # This parameter is required.
        self.output = output
        # Additional parameters for the watermark job, provided as a JSON string. Supported parameter:
        # 
        # *   m3u8Type: The type of M3U8 to generate. Defaults to v1.
        # 
        #     *   v1: Generates an M3U8 with absolute paths, playable directly. The signed URL for access is valid for 24 hours. If you need to use it after expiration, you must call this API again.
        #     *   v2: Generates an M3U8 with relative paths. It must be placed in the same directory as the TS segment files to be playable.
        self.params = params
        # The specific trace watermark information.
        self.trace = trace
        # The media ID for the trace watermark. You can obtain this from the response of the SubmitTraceAbJob operation.
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
        # The OSS path where the output file is saved. You can specify the path in one of the following formats:
        # 
        # 1\\. oss://bucket/object
        # 
        # 2\\. http(s)://bucket.oss-[regionId].aliyuncs.com/object where bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object path in OSS.
        # 
        # This parameter is required.
        self.media = media
        # The type of the output file. Valid value:
        # 
        # 1.  OSS: an OSS object.
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

