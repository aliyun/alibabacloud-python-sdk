# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFailFileRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        upload_id: int = None,
    ):
        # The site ID. You can obtain this value by calling the [ListSites](~~ListSites~~) operation.
        self.site_id = site_id
        # The ID of the file upload task.
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

