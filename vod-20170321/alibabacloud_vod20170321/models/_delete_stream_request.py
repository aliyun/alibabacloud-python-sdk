# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStreamRequest(DaraModel):
    def __init__(
        self,
        job_ids: str = None,
        reference_id: str = None,
        video_id: str = None,
    ):
        # The job IDs for deleting media streams.
        # 
        # *   Separate multiple IDs with commas (,). A maximum of 20 IDs can be specified for one video.
        # *   You can obtain job IDs from the PlayInfo parameter that is returned after you call the [GetPlayInfo](https://help.aliyun.com/document_detail/56124.html) operation. Each media stream has a unique job ID.
        # 
        # This parameter is required.
        self.job_ids = job_ids
        self.reference_id = reference_id
        # The ID of the video.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

