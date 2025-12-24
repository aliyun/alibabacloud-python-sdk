# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitializeAutoShowListTaskResponseBody(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        request_id: str = None,
        stream_list: str = None,
    ):
        # The ID of the production studio.
        # 
        # >  The value of this parameter can be used as the value of a request parameter to query the streaming URL of the production studio, start the production studio, add video resources to the production studio, add a production studio layout, query production studio layouts, add a production studio component, and add a production studio playlist.
        self.caster_id = caster_id
        # The request ID.
        self.request_id = request_id
        # The list of output video streams.
        # 
        # *   videoFormat: the format of the streaming URL.
        # *   outputStreamUrl: the source URL.
        # *   transcodeConfig: the output resolution specified for video transcoding of the source URL.
        self.stream_list = stream_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_list is not None:
            result['StreamList'] = self.stream_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamList') is not None:
            self.stream_list = m.get('StreamList')

        return self

