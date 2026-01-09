# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class PutWebtrackingRequest(DaraModel):
    def __init__(
        self,
        logs: List[Dict[str, str]] = None,
        source: str = None,
        tags: Dict[str, str] = None,
        topic: str = None,
    ):
        # The logs. Each element is a JSON object that indicates a log.
        # 
        # >  **Note**: The time in a log that is collected by using the web tracking feature is the time at which Simple Log Service receives the log. You do not need to configure the __time__ field for each log. If this field exists, it is overwritten by the time at which Simple Log Service receives the log.
        # 
        # This parameter is required.
        self.logs = logs
        # The source of the logs.
        # 
        # This parameter is required.
        self.source = source
        # The tags of the logs.
        self.tags = tags
        # The topic of the logs.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logs is not None:
            result['__logs__'] = self.logs

        if self.source is not None:
            result['__source__'] = self.source

        if self.tags is not None:
            result['__tags__'] = self.tags

        if self.topic is not None:
            result['__topic__'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('__logs__') is not None:
            self.logs = m.get('__logs__')

        if m.get('__source__') is not None:
            self.source = m.get('__source__')

        if m.get('__tags__') is not None:
            self.tags = m.get('__tags__')

        if m.get('__topic__') is not None:
            self.topic = m.get('__topic__')

        return self

