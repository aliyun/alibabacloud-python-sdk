# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMessagesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        message_level: str = None,
        message_time_earlier_than: int = None,
        message_time_later_than: int = None,
        message_type: str = None,
        next_token: str = None,
    ):
        # The maximum number of records to return in this request.
        self.max_results = max_results
        # The message level.
        self.message_level = message_level
        # Filters messages with a time earlier than the specified value.
        self.message_time_earlier_than = message_time_earlier_than
        # Filters messages with a time later than the specified value.
        self.message_time_later_than = message_time_later_than
        # The message type.
        self.message_type = message_type
        # The pagination token. If there is a next page, this field has a return value. This parameter indicates that there is a next page as long as data is returned. You can use the returned NextToken as a request parameter to obtain the next page of data until Null is returned, which indicates that all data has been retrieved.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message_level is not None:
            result['MessageLevel'] = self.message_level

        if self.message_time_earlier_than is not None:
            result['MessageTimeEarlierThan'] = self.message_time_earlier_than

        if self.message_time_later_than is not None:
            result['MessageTimeLaterThan'] = self.message_time_later_than

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MessageLevel') is not None:
            self.message_level = m.get('MessageLevel')

        if m.get('MessageTimeEarlierThan') is not None:
            self.message_time_earlier_than = m.get('MessageTimeEarlierThan')

        if m.get('MessageTimeLaterThan') is not None:
            self.message_time_later_than = m.get('MessageTimeLaterThan')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

