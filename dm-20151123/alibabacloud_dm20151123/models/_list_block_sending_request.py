# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBlockSendingRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        block_email: str = None,
        block_type: str = None,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        sender_email: str = None,
    ):
        self.begin_time = begin_time
        self.block_email = block_email
        # This parameter is required.
        self.block_type = block_type
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.sender_email = sender_email

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.block_email is not None:
            result['BlockEmail'] = self.block_email

        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sender_email is not None:
            result['SenderEmail'] = self.sender_email

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('BlockEmail') is not None:
            self.block_email = m.get('BlockEmail')

        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SenderEmail') is not None:
            self.sender_email = m.get('SenderEmail')

        return self

