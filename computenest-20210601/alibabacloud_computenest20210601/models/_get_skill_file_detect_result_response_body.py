# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillFileDetectResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        hash_key: str = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        score: int = None,
    ):
        self.code = code
        self.hash_key = hash_key
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

