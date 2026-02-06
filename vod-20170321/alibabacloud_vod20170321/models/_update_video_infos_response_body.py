# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateVideoInfosResponseBody(DaraModel):
    def __init__(
        self,
        forbidden_video_ids: List[str] = None,
        non_exist_reference_ids: List[str] = None,
        non_exist_video_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the videos that cannot be modified. Generally, videos cannot be modified if you do not have required [permissions](https://help.aliyun.com/document_detail/113600.html).
        self.forbidden_video_ids = forbidden_video_ids
        self.non_exist_reference_ids = non_exist_reference_ids
        # The IDs of the videos that do not exist.
        self.non_exist_video_ids = non_exist_video_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forbidden_video_ids is not None:
            result['ForbiddenVideoIds'] = self.forbidden_video_ids

        if self.non_exist_reference_ids is not None:
            result['NonExistReferenceIds'] = self.non_exist_reference_ids

        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbiddenVideoIds') is not None:
            self.forbidden_video_ids = m.get('ForbiddenVideoIds')

        if m.get('NonExistReferenceIds') is not None:
            self.non_exist_reference_ids = m.get('NonExistReferenceIds')

        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

