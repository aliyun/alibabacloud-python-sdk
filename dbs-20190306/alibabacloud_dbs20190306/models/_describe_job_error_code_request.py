# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeJobErrorCodeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        language: str = None,
        owner_id: str = None,
        task_id: str = None,
    ):
        # A client token. It is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The language of the error message. Valid values:
        # 
        # - **en**: English (Default)
        # 
        # - **cn**: Chinese
        self.language = language
        self.owner_id = owner_id
        # The ID of the full backup or restore job.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.language is not None:
            result['Language'] = self.language

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

