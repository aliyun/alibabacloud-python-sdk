# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUrlUploadInfosRequest(DaraModel):
    def __init__(
        self,
        job_ids: str = None,
        upload_urls: str = None,
    ):
        # The IDs of the upload jobs. You can specify one or more job IDs. You can obtain the job IDs from the response parameter JobId of the [UploadMediaByURL](https://help.aliyun.com/document_detail/86311.html) operation.
        # 
        # *   You can specify a maximum of 10 job IDs.
        # *   Separate the job IDs with commas (,).
        # 
        # >  You must specify either JobIds or UploadURLs. If you specify both parameters, only the value of JobIds takes effect.
        self.job_ids = job_ids
        # The upload URLs of the source files. You can specify a maximum of 10 URLs. Separate the URLs with commas (,).
        # 
        # > 
        # 
        # *   The URLs must be encoded.
        # 
        # *   If a media file is uploaded multiple times, we recommend that you specify the URL of the media file only once in this parameter.
        # 
        # *   You must specify either JobIds or UploadURLs. If you specify both parameters, only the value of JobIds takes effect.
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

