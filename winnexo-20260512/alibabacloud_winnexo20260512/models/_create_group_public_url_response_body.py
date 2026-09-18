# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupPublicUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        directory_id: str = None,
        gmt_create: str = None,
        group_id: str = None,
        message: str = None,
        name: str = None,
        original_url: str = None,
        request_id: str = None,
        scope: str = None,
        source_id: str = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The folder ID.
        self.directory_id = directory_id
        # The creation time.
        self.gmt_create = gmt_create
        # The project group ID.
        self.group_id = group_id
        # The description of the status code.
        self.message = message
        # The knowledge base name.
        self.name = name
        # The URL of the web page.
        self.original_url = original_url
        # The request ID.
        self.request_id = request_id
        # The permission scope.
        self.scope = scope
        # The source ID.
        self.source_id = source_id
        # The refund status. If a refund is in progress, query to confirm the refund status. Valid values:
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
        if self.code is not None:
            result['code'] = self.code

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.original_url is not None:
            result['originalUrl'] = self.original_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scope is not None:
            result['scope'] = self.scope

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('originalUrl') is not None:
            self.original_url = m.get('originalUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

