# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTranscodeTaskRequest(DaraModel):
    def __init__(
        self,
        job_ids: str = None,
        transcode_task_id: str = None,
    ):
        # The transcoding job IDs. You can specify a maximum of 10 IDs. Separate multiple IDs with commas (,). You can obtain the IDs by using the following method:
        # - Call the [SubmitTranscodeJobs](https://help.aliyun.com/document_detail/68570.html) operation to submit a transcoding task. The value of JobId in the response is the transcoding job ID.
        self.job_ids = job_ids
        # The transcoding task ID. You can obtain the ID by using one of the following methods:
        # - Call the [SubmitTranscodeJobs](https://help.aliyun.com/document_detail/68570.html) operation to submit a transcoding task. The value of TranscodeTaskId in the response is the transcoding task ID.
        # - Call the [ListTranscodeTask](https://help.aliyun.com/document_detail/109120.html) operation. The value of TranscodeTaskId in the response is the transcoding task ID.
        self.transcode_task_id = transcode_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')

        return self

