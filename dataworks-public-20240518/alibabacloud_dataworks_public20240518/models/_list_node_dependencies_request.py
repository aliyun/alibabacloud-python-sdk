# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodeDependenciesRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
    ):
        # The ID of the node.
        # 
        # >Notice: 
        # 
        # The data type of this parameter is Long in SDKs earlier than V8.0.0, and is String in SDKs of V8.0.0 and later versions. **The change does not affect the normal use of the SDKs. The parameter is still returned as the type defined in the SDKs.** When you upgrade an SDK to a version later than V8.0.0, a compilation error may occur due to the type change. In this case, you must manually change the data type.
        # 
        # This parameter is required.
        self.id = id
        # The number of the page to return. The value of this parameter must be a positive integer. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can go to the Workspace Management page in the [DataWorks console](https://workbench.data.aliyun.com/console) to obtain the workspace ID.
        # 
        # This parameter is used to specify the DataWorks workspace for the API call.
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
        if self.id is not None:
            result['Id'] = self.id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

