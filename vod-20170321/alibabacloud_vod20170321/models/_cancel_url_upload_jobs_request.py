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
        # The IDs of the upload jobs. You can obtain the job IDs from PlayInfo in the response to the [GetPlayInfo](https://help.aliyun.com/document_detail/56124.html) operation.
        # 
        # *   You can specify a maximum of 10 IDs.
        # *   Separate multiple IDs with commas (,).
        # 
        # >  You must specify either JobIds or UploadUrls. If you specify both the JobIds and UploadUrls parameters, only the value of the JobIds parameter takes effect.
        self.job_ids = job_ids
        # The upload URLs of source video files. Separate multiple URLs with commas (,). You can specify a maximum of 10 URLs.
        # 
        # > *   You must encode the URLs before you use the URLs.
        # > *   You must specify either JobIds or UploadUrls. If you specify both the JobIds and UploadUrls parameters, only the value of the JobIds parameter takes effect.
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

