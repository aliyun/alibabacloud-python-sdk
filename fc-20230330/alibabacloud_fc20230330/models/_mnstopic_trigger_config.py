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
        self.filter_tag = filter_tag
        self.notify_content_format = notify_content_format
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

