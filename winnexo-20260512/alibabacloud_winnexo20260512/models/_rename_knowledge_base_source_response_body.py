# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenameKnowledgeBaseSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        gmt_modified: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        source_id: str = None,
        status: str = None,
    ):
        # The status code.
        self.code = code
        # The last modified time.
        self.gmt_modified = gmt_modified
        # The description of the status code.
        self.message = message
        # The file name.
        self.name = name
        # The request trace ID.
        self.request_id = request_id
        # The data source ID.
        self.source_id = source_id
        # The data source status after re-parsing.
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

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

