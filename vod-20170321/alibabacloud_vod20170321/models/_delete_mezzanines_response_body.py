# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteMezzaninesResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_reference_ids: List[str] = None,
        non_exist_video_ids: List[str] = None,
        request_id: str = None,
        un_removeable_video_ids: List[str] = None,
    ):
        # The list of custom IDs that do not exist.
        self.non_exist_reference_ids = non_exist_reference_ids
        # The list of audio or video IDs that do not exist.
        self.non_exist_video_ids = non_exist_video_ids
        # The request ID.
        self.request_id = request_id
        # The list of audio or video IDs that cannot be deleted.
        # 
        # > This is typically because the source file is used as the original stream (if the video transcoding pattern is no transcoding or asynchronous transcoding, the source file is used as the original stream for playback and cannot be deleted by default) or because of insufficient [permissions](https://help.aliyun.com/document_detail/113600.html).
        self.un_removeable_video_ids = un_removeable_video_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_reference_ids is not None:
            result['NonExistReferenceIds'] = self.non_exist_reference_ids

        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.un_removeable_video_ids is not None:
            result['UnRemoveableVideoIds'] = self.un_removeable_video_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistReferenceIds') is not None:
            self.non_exist_reference_ids = m.get('NonExistReferenceIds')

        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UnRemoveableVideoIds') is not None:
            self.un_removeable_video_ids = m.get('UnRemoveableVideoIds')

        return self

