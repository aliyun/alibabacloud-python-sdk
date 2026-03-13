# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MNSTopicTriggerConfig(DaraModel):
    def __init__(
        self,
        filter_tag: str = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
    ):
        # The filtering tag. Function execution is triggered only when a message that contains the specified filter tag is received.
        self.filter_tag = filter_tag
        # The format of the event content. The following two formats are supported:
        # 
        # *   **JSON**
        # *   **STREAM**
        # 
        # >  The default format is STREAM.
        self.notify_content_format = notify_content_format
        # The retry policy.
        # 
        # *   **BACKOFF_RETRY**: a backoff retry policy. A total of 3 retries are made. The interval between 2 retries is a random value between 10 and 20 seconds. This is the default value.
        # *   **EXPONENTIAL_DECAY_RETRY**: an exponential decay retry policy. A total of 176 retries are made, with the interval of each retry increases exponentially to 512 seconds, and the total retry period is 1 day. The interval between two consecutive retries exponentially increases to a maximum of 512 seconds. For example, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 512... 512. The number of 512s is 167.
        self.notify_strategy = notify_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_tag is not None:
            result['filterTag'] = self.filter_tag

        if self.notify_content_format is not None:
            result['notifyContentFormat'] = self.notify_content_format

        if self.notify_strategy is not None:
            result['notifyStrategy'] = self.notify_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterTag') is not None:
            self.filter_tag = m.get('filterTag')

        if m.get('notifyContentFormat') is not None:
            self.notify_content_format = m.get('notifyContentFormat')

        if m.get('notifyStrategy') is not None:
            self.notify_strategy = m.get('notifyStrategy')

        return self

