# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUploadTaskRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        upload_id: int = None,
    ):
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.site_id = site_id
        # The ID of the file upload task. This field is assigned after you call the [UploadFile](https://help.aliyun.com/document_detail/2850466.html) operation.
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        return self

