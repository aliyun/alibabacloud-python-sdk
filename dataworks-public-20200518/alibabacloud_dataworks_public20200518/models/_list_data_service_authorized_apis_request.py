# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataServiceAuthorizedApisRequest(DaraModel):
    def __init__(
        self,
        api_name_keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The keyword of the API name. This parameter is used to filter APIs whose names contain the specified keyword.
        self.api_name_keyword = api_name_keyword
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The workspace ID. You can obtain this value from the PageResult.ProjectList[].ProjectId field returned by the ListProjects operation.
        # 
        # This parameter is required.
        self.project_id = project_id
        # **[Deprecated]** The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name_keyword is not None:
            result['ApiNameKeyword'] = self.api_name_keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiNameKeyword') is not None:
            self.api_name_keyword = m.get('ApiNameKeyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

