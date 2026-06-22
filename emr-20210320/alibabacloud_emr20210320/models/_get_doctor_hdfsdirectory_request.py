# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDoctorHDFSDirectoryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        date_time: str = None,
        dir_path: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specify the date in the ISO 8601 standard. For example, 2023-01-01 represents January 1, 2023.
        # 
        # This parameter is required.
        self.date_time = date_time
        # The directory name. The depth of the directory is not greater than five.
        # 
        # This parameter is required.
        self.dir_path = dir_path
        # The region ID.
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.dir_path is not None:
            result['DirPath'] = self.dir_path

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('DirPath') is not None:
            self.dir_path = m.get('DirPath')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

