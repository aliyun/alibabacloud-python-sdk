# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMediaProducingJobResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        media_id: str = None,
        project_id: str = None,
        request_id: str = None,
        vod_media_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The media asset ID of the output file.
        self.media_id = media_id
        # The ID of the editing project.
        self.project_id = project_id
        # The request ID.
        self.request_id = request_id
        # The media asset ID of the output file in ApsaraVideo VOD if the output file is stored in ApsaraVideo VOD.
        self.vod_media_id = vod_media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vod_media_id is not None:
            result['VodMediaId'] = self.vod_media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VodMediaId') is not None:
            self.vod_media_id = m.get('VodMediaId')

        return self

