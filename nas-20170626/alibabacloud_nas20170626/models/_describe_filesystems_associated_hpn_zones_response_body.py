# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFilesystemsAssociatedHpnZonesResponseBody(DaraModel):
    def __init__(
        self,
        filesystems: List[main_models.DescribeFilesystemsAssociatedHpnZonesResponseBodyFilesystems] = None,
        request_id: str = None,
    ):
        self.filesystems = filesystems
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filesystems = []
        if m.get('Filesystems') is not None:
            for k1 in m.get('Filesystems'):
                temp_model = main_models.DescribeFilesystemsAssociatedHpnZonesResponseBodyFilesystems()
                self.filesystems.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFilesystemsAssociatedHpnZonesResponseBodyFilesystems(DaraModel):
    def __init__(
        self,
        associated_hpn_zones: List[str] = None,
        file_system_id: str = None,
        zone_id: str = None,
    ):
        self.associated_hpn_zones = associated_hpn_zones
        self.file_system_id = file_system_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_hpn_zones is not None:
            result['AssociatedHpnZones'] = self.associated_hpn_zones

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedHpnZones') is not None:
            self.associated_hpn_zones = m.get('AssociatedHpnZones')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

