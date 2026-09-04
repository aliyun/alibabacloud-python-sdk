# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAnnouncementResponseBody(DaraModel):
    def __init__(
        self,
        announcement_id: int = None,
        code: str = None,
        created_by: int = None,
        message: str = None,
        published_at: str = None,
        request_id: str = None,
        source_type: str = None,
        status: str = None,
    ):
        # The business ID of the notice.
        self.announcement_id = announcement_id
        # The error code.
        self.code = code
        # The creator.
        self.created_by = created_by
        # The prompt message.
        self.message = message
        # The publish time in ISO 8601 format. This field is empty for drafts.
        self.published_at = published_at
        # The request ID.
        self.request_id = request_id
        # The source type of the dictionary file. Valid values: OSS: Object Storage Service (OSS). ORIGIN: retains the previously uploaded dictionary.
        self.source_type = source_type
        # The refund status. You need to query and confirm the refund status during the refund process. Valid values:
        # - SUCCESS: All succeeded.
        # - FAIL: Failed.
        # - WAIT_PAY: Waiting for refund.
        # - EXPIRE: Expired.
        # - PAYING: Refund in progress.
        # - TERMINATE: Refund terminated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.announcement_id is not None:
            result['announcementId'] = self.announcement_id

        if self.code is not None:
            result['code'] = self.code

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.message is not None:
            result['message'] = self.message

        if self.published_at is not None:
            result['publishedAt'] = self.published_at

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('announcementId') is not None:
            self.announcement_id = m.get('announcementId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('publishedAt') is not None:
            self.published_at = m.get('publishedAt')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

