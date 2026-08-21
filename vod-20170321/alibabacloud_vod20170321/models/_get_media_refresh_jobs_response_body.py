# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMediaRefreshJobsResponseBody(DaraModel):
    def __init__(
        self,
        media_refresh_jobs: List[main_models.GetMediaRefreshJobsResponseBodyMediaRefreshJobs] = None,
        request_id: str = None,
    ):
        # The list of audio or video purge or prefetch task information.
        self.media_refresh_jobs = media_refresh_jobs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_refresh_jobs:
            for v1 in self.media_refresh_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaRefreshJobs'] = []
        if self.media_refresh_jobs is not None:
            for k1 in self.media_refresh_jobs:
                result['MediaRefreshJobs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_refresh_jobs = []
        if m.get('MediaRefreshJobs') is not None:
            for k1 in m.get('MediaRefreshJobs'):
                temp_model = main_models.GetMediaRefreshJobsResponseBodyMediaRefreshJobs()
                self.media_refresh_jobs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaRefreshJobsResponseBodyMediaRefreshJobs(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        filter_policy: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        media_id: str = None,
        media_refresh_job_id: str = None,
        status: str = None,
        success_play_urls: str = None,
        task_ids: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # The error code. This field is returned when the purge or prefetch task fails to be submitted.
        self.error_code = error_code
        # The error message. This field is returned when the purge or prefetch task fails to be submitted.
        self.error_message = error_message
        # The filtering policy for playback streams. The value is in JSON format and contains the request parameters of the [SubmitMediaRefreshJob](https://help.aliyun.com/document_detail/431095.html) operation.
        self.filter_policy = filter_policy
        # The time when the task was created.
        self.gmt_create = gmt_create
        # The time when the task was last modified.
        self.gmt_modified = gmt_modified
        # The audio or video ID.
        self.media_id = media_id
        # The ID of the audio or video purge or prefetch task.
        self.media_refresh_job_id = media_refresh_job_id
        # The task status. Valid values:
        # - **success**: succeeded
        # - **fail**: failed
        self.status = status
        # The playback URLs that were successfully purged or prefetched.
        self.success_play_urls = success_play_urls
        # The task IDs for the purge or prefetch of playback URLs. Each URL corresponds to one task ID. You can use the task ID to call the [DescribeVodRefreshTasks](https://help.aliyun.com/document_detail/69214.html) operation to query the purge or prefetch status of each playback URL.
        self.task_ids = task_ids
        # The task type. Valid values:
        # - **Refresh**: purge
        # - **Preload**: prefetch
        self.task_type = task_type
        # The UserData information specified when the purge or prefetch task was submitted.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.filter_policy is not None:
            result['FilterPolicy'] = self.filter_policy

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_refresh_job_id is not None:
            result['MediaRefreshJobId'] = self.media_refresh_job_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success_play_urls is not None:
            result['SuccessPlayUrls'] = self.success_play_urls

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FilterPolicy') is not None:
            self.filter_policy = m.get('FilterPolicy')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaRefreshJobId') is not None:
            self.media_refresh_job_id = m.get('MediaRefreshJobId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuccessPlayUrls') is not None:
            self.success_play_urls = m.get('SuccessPlayUrls')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

