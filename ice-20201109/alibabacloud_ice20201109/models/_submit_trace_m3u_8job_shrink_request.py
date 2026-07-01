# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTraceM3u8JobShrinkRequest(DaraModel):
    def __init__(
        self,
        key_uri: str = None,
        output_shrink: str = None,
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
        self.output_shrink = output_shrink
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_uri is not None:
            result['KeyUri'] = self.key_uri

        if self.output_shrink is not None:
            result['Output'] = self.output_shrink

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
            self.output_shrink = m.get('Output')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Trace') is not None:
            self.trace = m.get('Trace')

        if m.get('TraceMediaId') is not None:
            self.trace_media_id = m.get('TraceMediaId')

        return self

