# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApisBySignatureResponseBody(DaraModel):
    def __init__(
        self,
        api_infos: main_models.DescribeApisBySignatureResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned API information. It is an array consisting of ApiInfo data.
        self.api_infos = api_infos
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()

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
        if m.get('ApiInfos') is not None:
            temp_model = main_models.DescribeApisBySignatureResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m.get('ApiInfos'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisBySignatureResponseBodyApiInfos(DaraModel):
    def __init__(
        self,
        api_info: List[main_models.DescribeApisBySignatureResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for v1 in self.api_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k1 in self.api_info:
                result['ApiInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k1 in m.get('ApiInfo'):
                temp_model = main_models.DescribeApisBySignatureResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k1))

        return self

class DescribeApisBySignatureResponseBodyApiInfosApiInfo(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        bound_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        region_id: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # The binding time of the API.
        self.bound_time = bound_time
        # The description of the API.
        self.description = description
        # The ID of the API group.
        self.group_id = group_id
        # The name of the group to which the API belongs.
        self.group_name = group_name
        # The region where the API is located.
        self.region_id = region_id
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **TEST**
        self.stage_name = stage_name
        # Indicates whether the API is public. Valid values:
        # 
        # *   **PUBLIC**
        # *   **PRIVATE**
        self.visibility = visibility

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

        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

