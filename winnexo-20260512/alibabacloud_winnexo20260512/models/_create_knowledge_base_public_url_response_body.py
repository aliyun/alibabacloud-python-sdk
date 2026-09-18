# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBasePublicUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        directory_id: str = None,
        gmt_create: str = None,
        message: str = None,
        name: str = None,
        original_url: str = None,
        request_id: str = None,
        scope: str = None,
        source_id: str = None,
        status: str = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The ID of the destination folder in the enterprise knowledge base that was specified in the request.
        self.directory_id = directory_id
        # The creation time in ISO 8601 format.
        self.gmt_create = gmt_create
        # The error description. This value is empty if the request is successful.
        self.message = message
        # The resource name.
        self.name = name
        # The submitted public web page URL.
        self.original_url = original_url
        # The request trace ID.
        self.request_id = request_id
        # The resource scope. The value is fixed to TENANT.
        self.scope = scope
        # The ID of the newly created source.
        self.source_id = source_id
        # The resource status. A value of RUNNING indicates that the request has been accepted but the crawling and parsing are not yet complete.
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

