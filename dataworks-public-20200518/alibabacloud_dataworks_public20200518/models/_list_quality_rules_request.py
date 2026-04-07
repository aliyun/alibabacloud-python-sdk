# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQualityRulesRequest(DaraModel):
    def __init__(
        self,
        entity_id: int = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        project_name: str = None,
    ):
        # The ID of the partition filter expression. You can call the [GetQualityEntity](https://help.aliyun.com/document_detail/174003.html) operation to query the ID.
        # 
        # This parameter is required.
        self.entity_id = entity_id
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The name of the compute engine or data source. You can obtain the name from data source configurations.
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

