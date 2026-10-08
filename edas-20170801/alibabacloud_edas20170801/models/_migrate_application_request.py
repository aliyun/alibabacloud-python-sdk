# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MigrateApplicationRequest(DaraModel):
    def __init__(
        self,
        app_ids: List[str] = None,
        cmd: str = None,
        config: str = None,
        raw_data: str = None,
        region_id: str = None,
    ):
        # The list of application IDs.
        self.app_ids = app_ids
        # The operation command. Valid values:
        # - export: Export.
        # - import: Import.
        self.cmd = cmd
        # Specifies whether to export the application binary. Default value: false.
        self.config = config
        # The raw data for the application to be imported, which is sourced from the JSON file of the exported application.
        self.raw_data = raw_data
        # regionId
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['appIds'] = self.app_ids

        if self.cmd is not None:
            result['cmd'] = self.cmd

        if self.config is not None:
            result['config'] = self.config

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appIds') is not None:
            self.app_ids = m.get('appIds')

        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

