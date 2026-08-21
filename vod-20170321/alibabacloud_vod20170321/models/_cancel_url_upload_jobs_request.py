# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelUrlUploadJobsRequest(DaraModel):
    def __init__(
        self,
        job_ids: str = None,
        upload_urls: str = None,
    ):
        # The list of task IDs. You can obtain the task ID (JobId) from the PlayInfo struct returned by the [GetPlayInfo](https://help.aliyun.com/document_detail/56124.html) operation.
        # - A maximum of 10 IDs are supported.
        # - Separate multiple IDs with commas (,).
        # 
        # > You must specify either JobIds or UploadUrls. If both are specified, only JobIds is processed.
        self.job_ids = job_ids
        # The list of source video upload URLs. Separate multiple URLs with commas (,). A maximum of 10 URLs are supported.
        # 
        # > - URL-encode the URLs before use.
        # > - You must specify either JobIds or UploadUrls. If both are specified, only JobIds is processed.
        self.upload_urls = upload_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        if self.upload_urls is not None:
            result['UploadUrls'] = self.upload_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('UploadUrls') is not None:
            self.upload_urls = m.get('UploadUrls')

        return self

