# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class PublishFeatureViewTableRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        event_time: str = None,
        mode: str = None,
        offline_to_online: bool = None,
        partitions: Dict[str, dict] = None,
    ):
        self.config = config
        self.event_time = event_time
        # This parameter is required.
        self.mode = mode
        # This parameter is required.
        self.offline_to_online = offline_to_online
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.offline_to_online is not None:
            result['OfflineToOnline'] = self.offline_to_online

        if self.partitions is not None:
            result['Partitions'] = self.partitions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OfflineToOnline') is not None:
            self.offline_to_online = m.get('OfflineToOnline')

        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')

        return self

