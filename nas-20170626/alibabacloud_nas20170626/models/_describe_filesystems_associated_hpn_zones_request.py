# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFilesystemsAssociatedHpnZonesRequest(DaraModel):
    def __init__(
        self,
        filesystems: List[main_models.DescribeFilesystemsAssociatedHpnZonesRequestFilesystems] = None,
        region_id: str = None,
    ):
        self.filesystems = filesystems
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.filesystems:
            for v1 in self.filesystems:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filesystems'] = []
        if self.filesystems is not None:
            for k1 in self.filesystems:
                result['Filesystems'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filesystems = []
        if m.get('Filesystems') is not None:
            for k1 in m.get('Filesystems'):
                temp_model = main_models.DescribeFilesystemsAssociatedHpnZonesRequestFilesystems()
                self.filesystems.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeFilesystemsAssociatedHpnZonesRequestFilesystems(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self

