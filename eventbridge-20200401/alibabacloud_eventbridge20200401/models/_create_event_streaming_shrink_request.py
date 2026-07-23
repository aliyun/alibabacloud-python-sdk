# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateEventStreamingShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        metadata: str = None,
        run_options_shrink: str = None,
        sink_shrink: str = None,
        source_shrink: str = None,
        tags: List[main_models.CreateEventStreamingShrinkRequestTags] = None,
        transforms_shrink: str = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        # 
        # This parameter is required.
        self.event_streaming_name = event_streaming_name
        # The event filtering rule. If not specified, all events are matched.
        self.filter_pattern = filter_pattern
        self.metadata = metadata
        # The runtime environment parameters.
        self.run_options_shrink = run_options_shrink
        # The event target. You must select exactly one Sink type.
        self.sink_shrink = sink_shrink
        # The event provider. You must select exactly one Source type.
        self.source_shrink = source_shrink
        # The tag list. A maximum of 20 items are supported.
        self.tags = tags
        # The Transform-related configurations.
        self.transforms_shrink = transforms_shrink

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
        if self.description is not None:
            result['Description'] = self.description

        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name

        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.run_options_shrink is not None:
            result['RunOptions'] = self.run_options_shrink

        if self.sink_shrink is not None:
            result['Sink'] = self.sink_shrink

        if self.source_shrink is not None:
            result['Source'] = self.source_shrink

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.transforms_shrink is not None:
            result['Transforms'] = self.transforms_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')

        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RunOptions') is not None:
            self.run_options_shrink = m.get('RunOptions')

        if m.get('Sink') is not None:
            self.sink_shrink = m.get('Sink')

        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateEventStreamingShrinkRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Transforms') is not None:
            self.transforms_shrink = m.get('Transforms')

        return self

class CreateEventStreamingShrinkRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

