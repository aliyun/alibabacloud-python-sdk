# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateMultimodalLabelStudioServiceWhiteListRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        source_region_id: str = None,
        white_list: List[str] = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.source_region_id = source_region_id
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

