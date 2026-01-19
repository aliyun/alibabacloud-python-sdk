# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApisByAppResponseBody(DaraModel):
    def __init__(
        self,
        app_api_relation_infos: main_models.DescribeApisByAppResponseBodyAppApiRelationInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The API authorizations.
        self.app_api_relation_infos = app_api_relation_infos
        # The number of pages to return the results on.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.app_api_relation_infos:
            self.app_api_relation_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_api_relation_infos is not None:
            result['AppApiRelationInfos'] = self.app_api_relation_infos.to_map()

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
        if m.get('AppApiRelationInfos') is not None:
            temp_model = main_models.DescribeApisByAppResponseBodyAppApiRelationInfos()
            self.app_api_relation_infos = temp_model.from_map(m.get('AppApiRelationInfos'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisByAppResponseBodyAppApiRelationInfos(DaraModel):
    def __init__(
        self,
        app_api_relation_info: List[main_models.DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo] = None,
    ):
        self.app_api_relation_info = app_api_relation_info

    def validate(self):
        if self.app_api_relation_info:
            for v1 in self.app_api_relation_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppApiRelationInfo'] = []
        if self.app_api_relation_info is not None:
            for k1 in self.app_api_relation_info:
                result['AppApiRelationInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_api_relation_info = []
        if m.get('AppApiRelationInfo') is not None:
            for k1 in m.get('AppApiRelationInfo'):
                temp_model = main_models.DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo()
                self.app_api_relation_info.append(temp_model.from_map(k1))

        return self

class DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_vaild_time: str = None,
        authorization_source: str = None,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        method: str = None,
        operator: str = None,
        path: str = None,
        region_id: str = None,
        stage_alias: str = None,
        stage_name: str = None,
    ):
        # The API ID.
        self.api_id = api_id
        # The API name.
        self.api_name = api_name
        # The validity period of the authorization.
        self.auth_vaild_time = auth_vaild_time
        # The authorization source.
        self.authorization_source = authorization_source
        # The time when the authorization was created.
        self.created_time = created_time
        # The authorization description.
        self.description = description
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # The HTTP method of the API.
        self.method = method
        # The authorizer. Valid values:
        # 
        # *   **PROVIDER**: API owner
        # *   **CONSUMER**: API caller
        self.operator = operator
        # The request path of the API.
        self.path = path
        # The region ID.
        self.region_id = region_id
        # The environment alias.
        self.stage_alias = stage_alias
        # The environment name.
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

        if self.auth_vaild_time is not None:
            result['AuthVaildTime'] = self.auth_vaild_time

        if self.authorization_source is not None:
            result['AuthorizationSource'] = self.authorization_source

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.method is not None:
            result['Method'] = self.method

        if self.operator is not None:
            result['Operator'] = self.operator

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

        if m.get('AuthVaildTime') is not None:
            self.auth_vaild_time = m.get('AuthVaildTime')

        if m.get('AuthorizationSource') is not None:
            self.authorization_source = m.get('AuthorizationSource')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StageAlias') is not None:
            self.stage_alias = m.get('StageAlias')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

