# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribePluginApisResponseBody(DaraModel):
    def __init__(
        self,
        api_summarys: main_models.DescribePluginApisResponseBodyApiSummarys = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about APIs.
        self.api_summarys = api_summarys
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.api_summarys:
            self.api_summarys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_summarys is not None:
            result['ApiSummarys'] = self.api_summarys.to_map()

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
        if m.get('ApiSummarys') is not None:
            temp_model = main_models.DescribePluginApisResponseBodyApiSummarys()
            self.api_summarys = temp_model.from_map(m.get('ApiSummarys'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePluginApisResponseBodyApiSummarys(DaraModel):
    def __init__(
        self,
        api_plugin_summary: List[main_models.DescribePluginApisResponseBodyApiSummarysApiPluginSummary] = None,
    ):
        self.api_plugin_summary = api_plugin_summary

    def validate(self):
        if self.api_plugin_summary:
            for v1 in self.api_plugin_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiPluginSummary'] = []
        if self.api_plugin_summary is not None:
            for k1 in self.api_plugin_summary:
                result['ApiPluginSummary'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_plugin_summary = []
        if m.get('ApiPluginSummary') is not None:
            for k1 in m.get('ApiPluginSummary'):
                temp_model = main_models.DescribePluginApisResponseBodyApiSummarysApiPluginSummary()
                self.api_plugin_summary.append(temp_model.from_map(k1))

        return self

class DescribePluginApisResponseBodyApiSummarysApiPluginSummary(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        method: str = None,
        path: str = None,
        region_id: str = None,
        stage_alias: str = None,
        stage_name: str = None,
    ):
        # The API ID.
        self.api_id = api_id
        # The API name.
        self.api_name = api_name
        # The API description.
        self.description = description
        # The ID of the API group.
        self.group_id = group_id
        # The API group to which the API belongs.
        self.group_name = group_name
        # The HTTP method of the API.
        self.method = method
        # The request path of the API.
        self.path = path
        # The ID of the region in which the API resides.
        self.region_id = region_id
        # The environment alias.
        self.stage_alias = stage_alias
        # The environment to which the API is published. Valid values:
        # 
        # *   **RELEASE**: the production environment
        # *   **PRE**: the pre-release environment
        # *   **TEST**: the test environment
        self.stage_name = stage_name

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

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.method is not None:
            result['Method'] = self.method

        if self.path is not None:
            result['Path'] = self.path

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stage_alias is not None:
            result['StageAlias'] = self.stage_alias

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StageAlias') is not None:
            self.stage_alias = m.get('StageAlias')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

