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
        # The production studio ID.
        # >This ID can be used as a request parameter for querying production studio stream URLs, starting the production studio, adding video resources to the production studio, adding layouts to the production studio, querying the layout list of the production studio, adding components to the production studio, and adding programs to the production studio.
        self.caster_id = caster_id
        # The request ID.
        self.request_id = request_id
        # The list of output addresses of the production studio.
        # 
        # - videoFormat: the streaming URL format.
        # 
        # - outputStreamUrl: the stream pulling URL.
        # 
        # - transcodeConfig: the transcoding resolution description of the stream pulling URL.
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

