# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class QueryTagListPageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryTagListPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. **OK** indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryTagListPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryTagListPageResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        records: List[main_models.QueryTagListPageResponseBodyDataRecords] = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The retruned data.
        self.records = records
        # The total number of returned entries.
        self.total_count = total_count
        # The total number of returned pages.
        self.total_page = total_page

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.QueryTagListPageResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class QueryTagListPageResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        code: str = None,
        doc_address: str = None,
        id: int = None,
        industry_id: int = None,
        industry_name: str = None,
        introduction: str = None,
        is_open: int = None,
        name: str = None,
        sale_status_str: str = None,
        scene_id: int = None,
        scene_name: str = None,
    ):
        # The API operation that is called by the frontend.
        self.api_name = api_name
        # Code
        self.code = code
        # The URL for the API documentation.
        self.doc_address = doc_address
        # The tag ID.
        self.id = id
        # The industry ID.
        self.industry_id = industry_id
        # The industry name.
        self.industry_name = industry_name
        # The tag description.
        self.introduction = introduction
        # Indicates whether the number is activated.
        self.is_open = is_open
        # The tag name.
        self.name = name
        # *   0: The number is hidden.
        # *   1: The number is public.
        self.sale_status_str = sale_status_str
        # The scene ID.
        self.scene_id = scene_id
        # The scene name.
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.code is not None:
            result['Code'] = self.code

        if self.doc_address is not None:
            result['DocAddress'] = self.doc_address

        if self.id is not None:
            result['Id'] = self.id

        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id

        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.is_open is not None:
            result['IsOpen'] = self.is_open

        if self.name is not None:
            result['Name'] = self.name

        if self.sale_status_str is not None:
            result['SaleStatusStr'] = self.sale_status_str

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DocAddress') is not None:
            self.doc_address = m.get('DocAddress')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')

        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('IsOpen') is not None:
            self.is_open = m.get('IsOpen')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SaleStatusStr') is not None:
            self.sale_status_str = m.get('SaleStatusStr')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        return self

