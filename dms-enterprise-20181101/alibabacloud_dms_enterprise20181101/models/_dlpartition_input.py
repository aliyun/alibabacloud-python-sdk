# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class DLPartitionInput(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        last_access_time: int = None,
        parameters: Dict[str, str] = None,
        storage_descriptor: main_models.DLStorageDescriptor = None,
        values: List[str] = None,
    ):
        self.create_time = create_time
        self.last_access_time = last_access_time
        self.parameters = parameters
        self.storage_descriptor = storage_descriptor
        self.values = values

    def validate(self):
        if self.storage_descriptor:
            self.storage_descriptor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.storage_descriptor is not None:
            result['StorageDescriptor'] = self.storage_descriptor.to_map()

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('StorageDescriptor') is not None:
            temp_model = main_models.DLStorageDescriptor()
            self.storage_descriptor = temp_model.from_map(m.get('StorageDescriptor'))

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

