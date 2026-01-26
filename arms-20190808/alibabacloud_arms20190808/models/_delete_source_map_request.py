# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteSourceMapRequest(DaraModel):
    def __init__(
        self,
        fid_list: List[str] = None,
        pid: str = None,
        region_id: str = None,
    ):
        # The IDs of the SourceMap files.
        # 
        # This parameter is required.
        self.fid_list = fid_list
        # The process identifier (PID) of the application.
        # 
        # This parameter is required.
        self.pid = pid
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fid_list is not None:
            result['FidList'] = self.fid_list

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FidList') is not None:
            self.fid_list = m.get('FidList')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

