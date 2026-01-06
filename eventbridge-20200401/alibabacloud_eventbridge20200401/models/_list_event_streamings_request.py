# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListEventStreamingsRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
        sink_arn: str = None,
        source_arn: str = None,
        tags: List[main_models.ListEventStreamingsRequestTags] = None,
    ):
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. A maximum of 100 entries can be returned in a call.
        self.limit = limit
        # The name of the event stream that you want to query.
        self.name_prefix = name_prefix
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The ARN of the event target.
        self.sink_arn = sink_arn
        # The Alibaba Cloud Resource Name (ARN) of the event source.
        self.source_arn = source_arn
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sink_arn is not None:
            result['SinkArn'] = self.sink_arn

        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SinkArn') is not None:
            self.sink_arn = m.get('SinkArn')

        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListEventStreamingsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListEventStreamingsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

