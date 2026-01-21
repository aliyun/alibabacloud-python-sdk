# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserSlsLogStorageTimeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        log_version: int = None,
        sls_region_id: str = None,
        storage_time: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.log_version = log_version
        self.sls_region_id = sls_region_id
        # This parameter is required.
        self.storage_time = storage_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_version is not None:
            result['LogVersion'] = self.log_version

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        if self.storage_time is not None:
            result['StorageTime'] = self.storage_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogVersion') is not None:
            self.log_version = m.get('LogVersion')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        if m.get('StorageTime') is not None:
            self.storage_time = m.get('StorageTime')

        return self

