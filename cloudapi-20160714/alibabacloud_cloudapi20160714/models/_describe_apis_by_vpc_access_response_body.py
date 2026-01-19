# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApisByVpcAccessResponseBody(DaraModel):
    def __init__(
        self,
        api_vpc_access_infos: main_models.DescribeApisByVpcAccessResponseBodyApiVpcAccessInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned API information. It is an array consisting of ApiInfo data.
        self.api_vpc_access_infos = api_vpc_access_infos
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.api_vpc_access_infos:
            self.api_vpc_access_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_vpc_access_infos is not None:
            result['ApiVpcAccessInfos'] = self.api_vpc_access_infos.to_map()

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
        if m.get('ApiVpcAccessInfos') is not None:
            temp_model = main_models.DescribeApisByVpcAccessResponseBodyApiVpcAccessInfos()
            self.api_vpc_access_infos = temp_model.from_map(m.get('ApiVpcAccessInfos'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisByVpcAccessResponseBodyApiVpcAccessInfos(DaraModel):
    def __init__(
        self,
        api_vpc_access_info: List[main_models.DescribeApisByVpcAccessResponseBodyApiVpcAccessInfosApiVpcAccessInfo] = None,
    ):
        self.api_vpc_access_info = api_vpc_access_info

    def validate(self):
        if self.api_vpc_access_info:
            for v1 in self.api_vpc_access_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiVpcAccessInfo'] = []
        if self.api_vpc_access_info is not None:
            for k1 in self.api_vpc_access_info:
                result['ApiVpcAccessInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_vpc_access_info = []
        if m.get('ApiVpcAccessInfo') is not None:
            for k1 in m.get('ApiVpcAccessInfo'):
                temp_model = main_models.DescribeApisByVpcAccessResponseBodyApiVpcAccessInfosApiVpcAccessInfo()
                self.api_vpc_access_info.append(temp_model.from_map(k1))

        return self

class DescribeApisByVpcAccessResponseBodyApiVpcAccessInfosApiVpcAccessInfo(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        method: str = None,
        path: str = None,
        port: int = None,
        region_id: str = None,
        stage_id: str = None,
        stage_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The API ID.
        self.api_id = api_id
        # The API name.
        self.api_name = api_name
        # The description, which can be up to 200 characters in length.
        self.description = description
        # The ID of the API group to which the API belongs.
        self.group_id = group_id
        # The name of the API group to which the API belongs.
        self.group_name = group_name
        # The instance ID or IP address in the VPC access authorization.
        self.instance_id = instance_id
        # The HTTP request method of the API.
        self.method = method
        # The request path of the API.
        self.path = path
        # The port number.
        self.port = port
        # The region ID.
        self.region_id = region_id
        # The environment ID.
        self.stage_id = stage_id
        # The environment to which the API is published. Valid values:
        # 
        # *   **RELEASE**: the production environment
        # *   **PRE**: the staging environment
        # *   **TEST**: the test environment
        self.stage_name = stage_name
        # vpc id
        self.vpc_id = vpc_id
        # The name of the VPC access authorization.
        self.vpc_name = vpc_name

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.method is not None:
            result['Method'] = self.method

        if self.path is not None:
            result['Path'] = self.path

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

