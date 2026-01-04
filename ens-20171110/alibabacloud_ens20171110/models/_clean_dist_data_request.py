# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CleanDistDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_name: str = None,
        data_version: str = None,
        ens_region_id: str = None,
    ):
        self.app_id = app_id
        self.data_name = data_name
        self.data_version = data_version
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data_name is not None:
            result['DataName'] = self.data_name

        if self.data_version is not None:
            result['DataVersion'] = self.data_version

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')

        if m.get('DataVersion') is not None:
            self.data_version = m.get('DataVersion')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        return self

