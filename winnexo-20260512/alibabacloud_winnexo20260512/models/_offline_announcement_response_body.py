# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OfflineAnnouncementResponseBody(DaraModel):
    def __init__(
        self,
        announcement_id: int = None,
        changed: bool = None,
        code: str = None,
        gmt_modified: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        updated_by: int = None,
    ):
        # The business ID of the announcement.
        self.announcement_id = announcement_id
        # Indicates whether the status was changed.
        self.changed = changed
        # The status code.
        self.code = code
        # The last update time.
        self.gmt_modified = gmt_modified
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The data source status after re-parsing.
        self.status = status
        # The user who performed the update.
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.announcement_id is not None:
            result['announcementId'] = self.announcement_id

        if self.changed is not None:
            result['changed'] = self.changed

        if self.code is not None:
            result['code'] = self.code

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('announcementId') is not None:
            self.announcement_id = m.get('announcementId')

        if m.get('changed') is not None:
            self.changed = m.get('changed')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

