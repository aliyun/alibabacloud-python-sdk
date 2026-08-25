# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        data_type: str = None,
        init_version_shrink: str = None,
        name: str = None,
        origin: str = None,
        project_id: int = None,
        storage_type: str = None,
    ):
        # The description of the dataset. The value can be up to 1024 characters in length.
        self.comment = comment
        # The data type. Valid values:
        # - COMMON: general-purpose (default).
        # - PIC: image.
        # - TEXT: text.
        # - TABLE: table.
        # - VIDEO: video.
        # - AUDIO: audio.
        # - INDEX: index.
        self.data_type = data_type
        # The initial version of the dataset.
        # 
        # This parameter is required.
        self.init_version_shrink = init_version_shrink
        # The name of the dataset. The value must be a non-empty string that is up to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The origin of the dataset. Only DataWorks is supported.
        self.origin = origin
        # The ID of the DataWorks workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The storage type. Valid values:
        # - OSS: Object Storage Service.
        # - NAS: general-purpose NAS file storage.
        # - EXTREMENAS: extreme NAS file storage.
        # - DLF_LANCE: Data Lake Formation.
        # 
        # This parameter is required.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.init_version_shrink is not None:
            result['InitVersion'] = self.init_version_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('InitVersion') is not None:
            self.init_version_shrink = m.get('InitVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

