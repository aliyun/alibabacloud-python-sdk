# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataSource(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        mount_path: str = None,
        uri: str = None,
    ):
        self.data_source_id = data_source_id
        self.mount_path = mount_path
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

