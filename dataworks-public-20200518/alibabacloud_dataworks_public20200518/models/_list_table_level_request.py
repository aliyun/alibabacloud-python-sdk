# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTableLevelRequest(DaraModel):
    def __init__(
        self,
        level_type: int = None,
        page_num: int = None,
        page_size: int = None,
        project_id: int = None,
    ):
        # The table level type. Valid values: 1 and 2. The value 1 indicates the logical level. The value 2 indicates the physical level.
        # 
        # This parameter is required.
        self.level_type = level_type
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can log on to the DataWorks console to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level_type is not None:
            result['LevelType'] = self.level_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

