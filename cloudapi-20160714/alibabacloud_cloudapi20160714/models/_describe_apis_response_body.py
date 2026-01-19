# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApisResponseBody(DaraModel):
    def __init__(
        self,
        api_summarys: main_models.DescribeApisResponseBodyApiSummarys = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried API definitions.
        self.api_summarys = api_summarys
        # The page number of the returned page.
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
            temp_model = main_models.DescribeApisResponseBodyApiSummarys()
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

class DescribeApisResponseBodyApiSummarys(DaraModel):
    def __init__(
        self,
        api_summary: List[main_models.DescribeApisResponseBodyApiSummarysApiSummary] = None,
    ):
        self.api_summary = api_summary

    def validate(self):
        if self.api_summary:
            for v1 in self.api_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiSummary'] = []
        if self.api_summary is not None:
            for k1 in self.api_summary:
                result['ApiSummary'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_summary = []
        if m.get('ApiSummary') is not None:
            for k1 in m.get('ApiSummary'):
                temp_model = main_models.DescribeApisResponseBodyApiSummarysApiSummary()
                self.api_summary.append(temp_model.from_map(k1))

        return self

class DescribeApisResponseBodyApiSummarysApiSummary(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_method: str = None,
        api_name: str = None,
        api_path: str = None,
        created_time: str = None,
        deployed_infos: main_models.DescribeApisResponseBodyApiSummarysApiSummaryDeployedInfos = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        region_id: str = None,
        tag_list: main_models.DescribeApisResponseBodyApiSummarysApiSummaryTagList = None,
        visibility: str = None,
    ):
        # The API ID.
        self.api_id = api_id
        # The HTTP method of the API request.
        self.api_method = api_method
        # The API name.
        self.api_name = api_name
        # The request path of the API.
        self.api_path = api_path
        # The time when the API was created. The time is displayed in UTC.
        self.created_time = created_time
        # The API publishing statuses.
        self.deployed_infos = deployed_infos
        # The API description.
        self.description = description
        # The API group ID.
        self.group_id = group_id
        # The name of the API group to which the API belongs.
        self.group_name = group_name
        # The time when the API was modified. The time is displayed in UTC.
        self.modified_time = modified_time
        # The ID of the region to which the API belongs.
        self.region_id = region_id
        # The tags that are added to the APIs.
        self.tag_list = tag_list
        # Indicates whether the API is public. Valid values:
        # 
        # *   **PUBLIC**: The API is public.
        # *   **PRIVATE**: The API is private.
        self.visibility = visibility

    def validate(self):
        if self.deployed_infos:
            self.deployed_infos.validate()
        if self.tag_list:
            self.tag_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_method is not None:
            result['ApiMethod'] = self.api_method

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_path is not None:
            result['ApiPath'] = self.api_path

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.deployed_infos is not None:
            result['DeployedInfos'] = self.deployed_infos.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tag_list is not None:
            result['TagList'] = self.tag_list.to_map()

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiMethod') is not None:
            self.api_method = m.get('ApiMethod')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiPath') is not None:
            self.api_path = m.get('ApiPath')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DeployedInfos') is not None:
            temp_model = main_models.DescribeApisResponseBodyApiSummarysApiSummaryDeployedInfos()
            self.deployed_infos = temp_model.from_map(m.get('DeployedInfos'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TagList') is not None:
            temp_model = main_models.DescribeApisResponseBodyApiSummarysApiSummaryTagList()
            self.tag_list = temp_model.from_map(m.get('TagList'))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

class DescribeApisResponseBodyApiSummarysApiSummaryTagList(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeApisResponseBodyApiSummarysApiSummaryTagListTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeApisResponseBodyApiSummarysApiSummaryTagListTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeApisResponseBodyApiSummarysApiSummaryTagListTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeApisResponseBodyApiSummarysApiSummaryDeployedInfos(DaraModel):
    def __init__(
        self,
        deployed_info: List[main_models.DescribeApisResponseBodyApiSummarysApiSummaryDeployedInfosDeployedInfo] = None,
    ):
        self.deployed_info = deployed_info

    def validate(self):
        if self.deployed_info:
            for v1 in self.deployed_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeployedInfo'] = []
        if self.deployed_info is not None:
            for k1 in self.deployed_info:
                result['DeployedInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployed_info = []
        if m.get('DeployedInfo') is not None:
            for k1 in m.get('DeployedInfo'):
                temp_model = main_models.DescribeApisResponseBodyApiSummarysApiSummaryDeployedInfosDeployedInfo()
                self.deployed_info.append(temp_model.from_map(k1))

        return self

class DescribeApisResponseBodyApiSummarysApiSummaryDeployedInfosDeployedInfo(DaraModel):
    def __init__(
        self,
        deployed_status: str = None,
        effective_version: str = None,
        stage_name: str = None,
    ):
        # The deployment status. Valid values: DEPLOYED and NONDEPLOYED.
        self.deployed_status = deployed_status
        # The deployed version.
        self.effective_version = effective_version
        # Stage Name:
        # 
        # *   **RELEASE**: production environment
        # *   **PRE**: staging environment
        # *   **TEST**: test environment
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployed_status is not None:
            result['DeployedStatus'] = self.deployed_status

        if self.effective_version is not None:
            result['EffectiveVersion'] = self.effective_version

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployedStatus') is not None:
            self.deployed_status = m.get('DeployedStatus')

        if m.get('EffectiveVersion') is not None:
            self.effective_version = m.get('EffectiveVersion')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

