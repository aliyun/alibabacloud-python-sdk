# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TableConsumer(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        last_modified_time: int = None,
        next_snapshot: int = None,
    ):
        # Consumer ID
        self.consumer_id = consumer_id
        # The last modified time of the consumer file in Unix milliseconds.
        self.last_modified_time = last_modified_time
        # The ID of the next snapshot to be consumed.
        self.next_snapshot = next_snapshot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.next_snapshot is not None:
            result['nextSnapshot'] = self.next_snapshot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('nextSnapshot') is not None:
            self.next_snapshot = m.get('nextSnapshot')

        return self

