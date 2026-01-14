# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteConsumerGroupSubscriptionRequest(DaraModel):
    def __init__(
        self,
        filter_expression: str = None,
        filter_type: str = None,
        topic_name: str = None,
    ):
        # The filter expression.
        # 
        # This parameter is required.
        self.filter_expression = filter_expression
        # The type of the filter expression. Valid values:
        # 
        # *   SQL: filters messages by using SQL expressions.
        # *   TAG: filters messages by using tags.
        # 
        # This parameter is required.
        self.filter_type = filter_type
        # The topic name.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_expression is not None:
            result['filterExpression'] = self.filter_expression

        if self.filter_type is not None:
            result['filterType'] = self.filter_type

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterExpression') is not None:
            self.filter_expression = m.get('filterExpression')

        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

