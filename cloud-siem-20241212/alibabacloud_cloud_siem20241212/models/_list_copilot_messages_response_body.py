# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListCopilotMessagesResponseBody(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        items: List[main_models.ListCopilotMessagesResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The API version.
        # >You can call the [DescribeGroupProductions](~~DescribeGroupProductions~~) operation to obtain this parameter.
        self.api_version = api_version
        # The list of conversation messages.
        self.items = items
        # The maximum amount of data read in this query.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListCopilotMessagesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCopilotMessagesResponseBodyItems(DaraModel):
    def __init__(
        self,
        client_message_id: str = None,
        content: str = None,
        created_at: str = None,
        message_id: str = None,
        message_sequence: int = None,
        role: str = None,
        status: str = None,
        turn_id: str = None,
    ):
        # The client message ID.
        self.client_message_id = client_message_id
        # The sent content.
        self.content = content
        # The creation time.
        self.created_at = created_at
        # The message ID.
        self.message_id = message_id
        # The message sequence number.
        self.message_sequence = message_sequence
        # The message role.
        self.role = role
        # The status.
        self.status = status
        # The primary key ID.
        self.turn_id = turn_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_message_id is not None:
            result['ClientMessageId'] = self.client_message_id

        if self.content is not None:
            result['Content'] = self.content

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.message_sequence is not None:
            result['MessageSequence'] = self.message_sequence

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        if self.turn_id is not None:
            result['TurnId'] = self.turn_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientMessageId') is not None:
            self.client_message_id = m.get('ClientMessageId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('MessageSequence') is not None:
            self.message_sequence = m.get('MessageSequence')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TurnId') is not None:
            self.turn_id = m.get('TurnId')

        return self

