# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveKnowledgeBaseResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        knowledge_id: str = None,
        message: str = None,
        request_id: str = None,
        source_directory_id: str = None,
        source_id: str = None,
        target_directory_id: str = None,
    ):
        # The response code.
        self.code = code
        # The target knowledge base ID. This value is echoed from the request parameter.
        self.knowledge_id = knowledge_id
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The source directory ID. This value is echoed from the request parameter.
        self.source_directory_id = source_directory_id
        # The unique identifier on the business system side, that is, the business ID.
        self.source_id = source_id
        # The target directory ID. This value is echoed from the request parameter.
        self.target_directory_id = target_directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.knowledge_id is not None:
            result['knowledgeId'] = self.knowledge_id

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_directory_id is not None:
            result['sourceDirectoryId'] = self.source_directory_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.target_directory_id is not None:
            result['targetDirectoryId'] = self.target_directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('knowledgeId') is not None:
            self.knowledge_id = m.get('knowledgeId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceDirectoryId') is not None:
            self.source_directory_id = m.get('sourceDirectoryId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('targetDirectoryId') is not None:
            self.target_directory_id = m.get('targetDirectoryId')

        return self

