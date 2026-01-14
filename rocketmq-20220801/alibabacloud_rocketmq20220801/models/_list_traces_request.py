# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTracesRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        lite_topic_name: str = None,
        message_id: str = None,
        message_key: str = None,
        page_number: int = None,
        page_size: int = None,
        query_type: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.lite_topic_name = lite_topic_name
        # The message ID.
        # 
        # This parameter is required if you set queryType to MESSAGE_ID.
        self.message_id = message_id
        # The message key.
        # 
        # This parameter is required if you set queryType to MESSAGE_ID.
        self.message_key = message_key
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The query type.
        # 
        # Valid values:
        # 
        # *   MESSAGE_ID
        # *   MESSAGE_KEY
        # *   TOPIC
        # 
        # This parameter is required.
        self.query_type = query_type
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.lite_topic_name is not None:
            result['liteTopicName'] = self.lite_topic_name

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.message_key is not None:
            result['messageKey'] = self.message_key

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query_type is not None:
            result['queryType'] = self.query_type

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('liteTopicName') is not None:
            self.lite_topic_name = m.get('liteTopicName')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('messageKey') is not None:
            self.message_key = m.get('messageKey')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

