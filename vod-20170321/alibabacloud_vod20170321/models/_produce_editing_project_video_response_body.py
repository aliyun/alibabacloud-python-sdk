# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProduceEditingProjectVideoResponseBody(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        project_id: str = None,
        request_id: str = None,
    ):
        # The ID of the produced video.
        # 
        # > *   This parameter is returned for each request.
        # > *   If a value is returned for this parameter, the video production task is being asynchronously processed.
        self.media_id = media_id
        # The ID of the online editing project.
        self.project_id = project_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

