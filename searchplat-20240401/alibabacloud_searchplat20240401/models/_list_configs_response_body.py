# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class ListConfigsResponseBody(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[main_models.ListConfigsResponseBodyResult] = None,
        total: int = None,
    ):
        # The current page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The configuration list.
        self.result = result
        # The total number of configurations.
        self.total = total

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListConfigsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListConfigsResponseBodyResult(DaraModel):
    def __init__(
        self,
        config_data: Dict[str, Any] = None,
        config_type: str = None,
        workspace_id: str = None,
    ):
        # The configuration content.
        self.config_data = config_data
        # The configuration type. Valid values:
        #  * prompt: Prompt configuration.
        #  * lark: Lark configuration.
        self.config_type = config_type
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_data is not None:
            result['configData'] = self.config_data

        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configData') is not None:
            self.config_data = m.get('configData')

        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

