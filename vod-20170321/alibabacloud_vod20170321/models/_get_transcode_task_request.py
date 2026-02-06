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
        # Transcoding job ID. Supports up to 10 IDs, and multiple IDs should be separated by a comma (,). You can obtain this value in the following ways:
        # 
        # When initiating a transcoding task through the [SubmitTranscodeJobs](https://help.aliyun.com/document_detail/454920.html) interface, it is the value of the returned parameter JobId.
        self.job_ids = job_ids
        # The ID of the transcoding task. You can use one of the following methods to obtain the ID:
        # 
        # *   Obtain the value of TranscodeTaskId from the response to the [SubmitTranscodeJobs](https://help.aliyun.com/document_detail/68570.html) operation.
        # *   Obtain the value of TranscodeTaskId from the response to the [ListTranscodeTask](https://help.aliyun.com/document_detail/109120.html) operation.
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

