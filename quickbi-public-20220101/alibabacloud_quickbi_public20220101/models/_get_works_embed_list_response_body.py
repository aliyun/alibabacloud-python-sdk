# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class GetWorksEmbedListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetWorksEmbedListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID
        self.request_id = request_id
        # Array of report objects
        self.result = result
        # Whether the request was successful
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetWorksEmbedListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetWorksEmbedListResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetWorksEmbedListResponseBodyResultData] = None,
        page_no: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Array of reports
        self.data = data
        # Page number
        self.page_no = page_no
        # Number of items per page
        self.page_size = page_size
        # Total number of items
        self.total_num = total_num
        # Total number of pages
        self.total_pages = total_pages

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetWorksEmbedListResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class GetWorksEmbedListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        embed_time: str = None,
        works_id: str = None,
        works_name: str = None,
        works_type: str = None,
        workspace_id: str = None,
    ):
        # Embed time
        self.embed_time = embed_time
        # Report ID
        self.works_id = works_id
        # Report name
        self.works_name = works_name
        # Report type
        self.works_type = works_type
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embed_time is not None:
            result['EmbedTime'] = self.embed_time

        if self.works_id is not None:
            result['WorksId'] = self.works_id

        if self.works_name is not None:
            result['WorksName'] = self.works_name

        if self.works_type is not None:
            result['WorksType'] = self.works_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbedTime') is not None:
            self.embed_time = m.get('EmbedTime')

        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        if m.get('WorksName') is not None:
            self.works_name = m.get('WorksName')

        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

