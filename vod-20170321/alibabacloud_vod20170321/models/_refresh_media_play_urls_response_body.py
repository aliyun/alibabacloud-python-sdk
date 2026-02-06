# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshMediaPlayUrlsResponseBody(DaraModel):
    def __init__(
        self,
        forbidden_media_ids: str = None,
        media_refresh_job_id: str = None,
        non_exist_media_ids: str = None,
        request_id: str = None,
    ):
        # The IDs of the media files that cannot be operated on. In most cases, media files cannot be operated on because you are not authorized to perform the operations. For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.forbidden_media_ids = forbidden_media_ids
        # The ID of the refresh or prefetch task.
        self.media_refresh_job_id = media_refresh_job_id
        # The IDs of the media files that do not exist.
        self.non_exist_media_ids = non_exist_media_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forbidden_media_ids is not None:
            result['ForbiddenMediaIds'] = self.forbidden_media_ids

        if self.media_refresh_job_id is not None:
            result['MediaRefreshJobId'] = self.media_refresh_job_id

        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbiddenMediaIds') is not None:
            self.forbidden_media_ids = m.get('ForbiddenMediaIds')

        if m.get('MediaRefreshJobId') is not None:
            self.media_refresh_job_id = m.get('MediaRefreshJobId')

        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

