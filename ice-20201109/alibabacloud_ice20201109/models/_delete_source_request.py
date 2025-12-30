# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSourceRequest(DaraModel):
    def __init__(
        self,
        soft_delete: bool = None,
        source_location_name: str = None,
        source_name: str = None,
        source_type: str = None,
    ):
        # Specifies whether to use delete markers.
        self.soft_delete = soft_delete
        # The name of the source location.
        # 
        # This parameter is required.
        self.source_location_name = source_location_name
        # The name of the source.
        # 
        # This parameter is required.
        self.source_name = source_name
        # The source type. Valid values: vodSource and liveSource.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.soft_delete is not None:
            result['SoftDelete'] = self.soft_delete

        if self.source_location_name is not None:
            result['SourceLocationName'] = self.source_location_name

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SoftDelete') is not None:
            self.soft_delete = m.get('SoftDelete')

        if m.get('SourceLocationName') is not None:
            self.source_location_name = m.get('SourceLocationName')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

