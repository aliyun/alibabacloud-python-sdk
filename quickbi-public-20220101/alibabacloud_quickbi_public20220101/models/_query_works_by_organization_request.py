# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryWorksByOrganizationRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        status: int = None,
        third_part_auth_flag: int = None,
        works_type: str = None,
    ):
        # Page number.
        # 
        # - Default value is 1.
        self.page_num = page_num
        # Number of items per page.
        # 
        # - Default value is 10.
        self.page_size = page_size
        # The status of the work to query. Possible values:
        # 
        # - 0: Unpublished
        # - 1: Published
        # - 2: Modified but not published
        # - 3: Offline
        self.status = status
        # Third-party embedding status. Possible values:
        # 
        # - 0: Embedding not enabled
        # - 1: Embedding enabled
        self.third_part_auth_flag = third_part_auth_flag
        # The type of work to query. Leave blank to query all types. Possible values:
        # 
        # - DATAPRODUCT: Data Portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        # - dashboardOfflineQuery: Self-service Data Retrieval
        self.works_type = works_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag

        if self.works_type is not None:
            result['WorksType'] = self.works_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')

        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')

        return self

