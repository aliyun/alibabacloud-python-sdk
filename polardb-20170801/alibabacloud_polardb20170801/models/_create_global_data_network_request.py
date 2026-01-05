# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGlobalDataNetworkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_file_system_path: str = None,
        destination_id: str = None,
        destination_region: str = None,
        destination_type: str = None,
        freeze_source_during_sync: str = None,
        source_file_system_path: str = None,
        source_id: str = None,
        source_region: str = None,
        source_type: str = None,
    ):
        self.description = description
        self.destination_file_system_path = destination_file_system_path
        self.destination_id = destination_id
        self.destination_region = destination_region
        self.destination_type = destination_type
        self.freeze_source_during_sync = freeze_source_during_sync
        self.source_file_system_path = source_file_system_path
        self.source_id = source_id
        self.source_region = source_region
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_file_system_path is not None:
            result['DestinationFileSystemPath'] = self.destination_file_system_path

        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.freeze_source_during_sync is not None:
            result['FreezeSourceDuringSync'] = self.freeze_source_during_sync

        if self.source_file_system_path is not None:
            result['SourceFileSystemPath'] = self.source_file_system_path

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationFileSystemPath') is not None:
            self.destination_file_system_path = m.get('DestinationFileSystemPath')

        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('FreezeSourceDuringSync') is not None:
            self.freeze_source_during_sync = m.get('FreezeSourceDuringSync')

        if m.get('SourceFileSystemPath') is not None:
            self.source_file_system_path = m.get('SourceFileSystemPath')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

