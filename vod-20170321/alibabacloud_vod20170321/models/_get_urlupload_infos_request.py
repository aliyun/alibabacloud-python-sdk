# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetURLUploadInfosRequest(DaraModel):
    def __init__(
        self,
        job_ids: str = None,
        upload_urls: str = None,
    ):
        # The list of upload task IDs (JobId). The list consists of one or more JobId values. A JobId is the value of the JobId parameter returned when you call the [UploadMediaByURL](https://help.aliyun.com/document_detail/86311.html) operation.
        # - A maximum of 10 IDs are supported.
        # - Separate multiple IDs with commas (,).
        # 
        # > You must specify either JobIds or UploadURLs. If both are specified, only JobIds is processed.
        self.job_ids = job_ids
        # The list of source video file URLs. Separate multiple URLs with commas (,). A maximum of 10 URLs are supported.
        # > - URL-encode the URLs before use.
        # > - If the same URL video is uploaded multiple times, pass in a single URL for the query.
        # > - You must specify either JobIds or UploadURLs. If both are specified, only JobIds is processed.
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
            result['UploadURLs'] = self.upload_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('UploadURLs') is not None:
            self.upload_urls = m.get('UploadURLs')

        return self

