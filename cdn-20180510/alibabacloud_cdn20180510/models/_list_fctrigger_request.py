# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFCTriggerRequest(DaraModel):
    def __init__(
        self,
        event_meta_name: str = None,
        event_meta_version: str = None,
    ):
        # The name of the event. You can specify only one name.
        # 
        # This parameter is required.
        self.event_meta_name = event_meta_name
        # The version number of the event. You can specify only one version number.
        # 
        # This parameter is required.
        self.event_meta_version = event_meta_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name

        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')

        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')

        return self

