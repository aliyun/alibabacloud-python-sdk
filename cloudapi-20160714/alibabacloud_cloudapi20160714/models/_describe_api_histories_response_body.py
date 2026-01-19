# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiHistoriesResponseBody(DaraModel):
    def __init__(
        self,
        api_his_items: main_models.DescribeApiHistoriesResponseBodyApiHisItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned API information. It is an array consisting of ApiHisItem data.
        self.api_his_items = api_his_items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.api_his_items:
            self.api_his_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_his_items is not None:
            result['ApiHisItems'] = self.api_his_items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiHisItems') is not None:
            temp_model = main_models.DescribeApiHistoriesResponseBodyApiHisItems()
            self.api_his_items = temp_model.from_map(m.get('ApiHisItems'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApiHistoriesResponseBodyApiHisItems(DaraModel):
    def __init__(
        self,
        api_his_item: List[main_models.DescribeApiHistoriesResponseBodyApiHisItemsApiHisItem] = None,
    ):
        self.api_his_item = api_his_item

    def validate(self):
        if self.api_his_item:
            for v1 in self.api_his_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiHisItem'] = []
        if self.api_his_item is not None:
            for k1 in self.api_his_item:
                result['ApiHisItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_his_item = []
        if m.get('ApiHisItem') is not None:
            for k1 in m.get('ApiHisItem'):
                temp_model = main_models.DescribeApiHistoriesResponseBodyApiHisItemsApiHisItem()
                self.api_his_item.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoriesResponseBodyApiHisItemsApiHisItem(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        deployed_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        history_version: str = None,
        region_id: str = None,
        stage_name: str = None,
        status: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # The publishing time (UTC) of the API.
        self.deployed_time = deployed_time
        # The description of the API.
        self.description = description
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # The historical version of the API.
        self.history_version = history_version
        # The region in which the API is located.
        self.region_id = region_id
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **TEST**
        self.stage_name = stage_name
        # Indicates whether an API version is effective. Valid values: **ONLINE** and **OFFLINE**.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

