# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutExporterOutputRequest(DaraModel):
    def __init__(
        self,
        config_json: str = None,
        desc: str = None,
        dest_name: str = None,
        dest_type: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.config_json = config_json
        self.desc = desc
        # This parameter is required.
        self.dest_name = dest_name
        self.dest_type = dest_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_json is not None:
            result['ConfigJson'] = self.config_json

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.dest_name is not None:
            result['DestName'] = self.dest_name

        if self.dest_type is not None:
            result['DestType'] = self.dest_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigJson') is not None:
            self.config_json = m.get('ConfigJson')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('DestName') is not None:
            self.dest_name = m.get('DestName')

        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

