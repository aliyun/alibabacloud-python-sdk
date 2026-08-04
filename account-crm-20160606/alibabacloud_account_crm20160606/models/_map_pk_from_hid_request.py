# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MapPkFromHidRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        bid: str = None,
        hid: str = None,
        mapping_scenes: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.bid = bid
        # This parameter is required.
        self.hid = hid
        # This parameter is required.
        self.mapping_scenes = mapping_scenes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.bid is not None:
            result['Bid'] = self.bid

        if self.hid is not None:
            result['Hid'] = self.hid

        if self.mapping_scenes is not None:
            result['MappingScenes'] = self.mapping_scenes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Hid') is not None:
            self.hid = m.get('Hid')

        if m.get('MappingScenes') is not None:
            self.mapping_scenes = m.get('MappingScenes')

        return self

