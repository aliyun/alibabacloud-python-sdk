# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEventStreamingShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        metadata: str = None,
        run_options_shrink: str = None,
        sink_shrink: str = None,
        source_shrink: str = None,
        transforms_shrink: str = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        # 
        # This parameter is required.
        self.event_streaming_name = event_streaming_name
        # The event filtering rule. If you do not specify this parameter, all events are matched. For more information, see [https://www.alibabacloud.com/help/en/eventbridge/user-guide/event-patterns](https://www.alibabacloud.com/help/en/eventbridge/user-guide/event-patterns)
        self.filter_pattern = filter_pattern
        self.metadata = metadata
        # The runtime parameters.
        self.run_options_shrink = run_options_shrink
        # The event target. You must select one and only one Sink type.
        self.sink_shrink = sink_shrink
        # The event provider. You must select one and only one Source type.
        self.source_shrink = source_shrink
        # The Transform-related configurations.
        self.transforms_shrink = transforms_shrink

    def validate(self):
        pass

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

        if m.get('Transforms') is not None:
            self.transforms_shrink = m.get('Transforms')

        return self

