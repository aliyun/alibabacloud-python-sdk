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
        # The description of the dataset. It must not exceed 1,024 characters in length.
        self.comment = comment
        # The data type. Valid values:
        # 
        # *   COMMON: Common (Default)
        # *   PIC
        # *   TEXT
        # *   TABLE
        # *   VIDEO
        # *   AUDIO
        # *   INDEX
        self.data_type = data_type
        # The initial version of the dataset.
        # 
        # This parameter is required.
        self.init_version_shrink = init_version_shrink
        # The name of the dataset. It cannot be an empty string and must not exceed 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The source of the dataset. Currently, only DataWorks is supported.
        self.origin = origin
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The storage type. Currently supported values:
        # 
        # *   OSS
        # *   NAS: General-purpose NAS file systems
        # *   EXTREMENAS: Extreme NAS file systems
        # *   DLF_LANCE: Data Lake Formation
        # 
        # Valid values:
        # 
        # *   NAS: General-purpose NAS file systems
        # *   MAXCOMPUTE: MaxCompute table
        # *   CPFS: Cloud Parallel File Storage
        # *   BMCPFS: CPFS for Lingjun
        # *   EXTREMENAS: Extreme NAS file systems
        # *   OSS: Object Storage Service
        # *   DLF_LANCE: Data Lake Formation.
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

