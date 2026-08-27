# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalAlidingKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        directory_id: str = None,
        gmt_create: str = None,
        kb_url: str = None,
        message: str = None,
        name: str = None,
        operating_object_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The status code.
        self.code = code
        # The directory ID.
        self.directory_id = directory_id
        # The creation time in ISO 8601 format.
        self.gmt_create = gmt_create
        # The knowledge base URL (echoed from the request parameter for caller alignment).
        self.kb_url = kb_url
        # The response message.
        self.message = message
        # The name of the AI assistant.
        self.name = name
        # The name of the digital employee (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The request ID.
        self.request_id = request_id
        # The status. Valid values:
        # 
        # - 200: Success.
        # - 500: Failure.
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

        if self.kb_url is not None:
            result['kbUrl'] = self.kb_url

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if m.get('kbUrl') is not None:
            self.kb_url = m.get('kbUrl')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

