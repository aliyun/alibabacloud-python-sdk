# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitUploadTaskRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        site_id: int = None,
        upload_id: int = None,
    ):
        # Specifies whether to refresh resources in the corresponding directory if the requested content is different from that on the origin server. Default value: false. This parameter takes effect for a purge task.
        # 
        # *   **true**: purges all resources in the directory.
        # *   **false**: refresh the changed resources in the directory.
        self.force = force
        # The website ID. You can call the [ListSites](~~ListSites~~) operation to obtain the ID.
        self.site_id = site_id
        # The ID of the file upload task, which is generated when you call [UploadTask](~~UploadTask~~).
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        return self

