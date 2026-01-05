# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasetsShrinkRequest(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        data_type_list_shrink: str = None,
        name: str = None,
        order: str = None,
        origin: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        storage_type_list_shrink: str = None,
    ):
        # The creator ID.
        self.creator_id = creator_id
        # The data type. Multiple selections are allowed. Valid values:
        # 
        # *   COMMON
        # *   PIC
        # *   TEXT
        # *   TABLE
        # *   VIDEO
        # *   AUDIO
        # *   INDEX
        self.data_type_list_shrink = data_type_list_shrink
        # The dataset name. Supports fuzzy search.
        self.name = name
        # The sort order. Default: Desc.
        # 
        # Valid values:
        # 
        # *   Asc: Ascending.
        # *   Desc: Descending.
        self.order = order
        # The dataset source. Valid values:
        # 
        # *   DataWorks
        # *   PAI
        self.origin = origin
        # The page number. Default: 1.
        self.page_number = page_number
        # The number of entries per page. Default: 10. Maximum: 100.
        self.page_size = page_size
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The sort field. Default: CreateTime.
        # 
        # Valid values:
        # 
        # *   ModifyTime: Modification time.
        # *   CreateTime: Creation time.
        # *   Name
        self.sort_by = sort_by
        # The storage type. Multiple selections are allowed. Supported values:
        # 
        # *   OSS
        # *   NAS: General-purpose NAS file systems
        # *   EXTREMENAS: Extreme NAS file systems
        # *   DLF_LANCE: Data Lake Formation
        # *   CPFS: Cloud Parallel File Storage
        # *   BMCPFS: CPFS for Lingjun
        # *   MAXCOMPUTE: MaxCompute table
        self.storage_type_list_shrink = storage_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.data_type_list_shrink is not None:
            result['DataTypeList'] = self.data_type_list_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.storage_type_list_shrink is not None:
            result['StorageTypeList'] = self.storage_type_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('DataTypeList') is not None:
            self.data_type_list_shrink = m.get('DataTypeList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StorageTypeList') is not None:
            self.storage_type_list_shrink = m.get('StorageTypeList')

        return self

