# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListComputeClustersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page_result: main_models.ListComputeClustersResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The page size. Valid values: 1 to 50. Default value: 50.
        self.max_results = max_results
        # The details of the backend exception.
        self.message = message
        # Indicates whether a token for the next query exists. If NextToken is empty, no more results are available. If NextToken is returned, the value indicates the token used to start the next query.
        self.next_token = next_token
        # The paged query result.
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListComputeClustersResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListComputeClustersResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        cluster_list: List[main_models.ListComputeClustersResponseBodyPageResultClusterList] = None,
        total_count: int = None,
    ):
        # The paged list of clusters.
        self.cluster_list = cluster_list
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.cluster_list:
            for v1 in self.cluster_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterList'] = []
        if self.cluster_list is not None:
            for k1 in self.cluster_list:
                result['ClusterList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_list = []
        if m.get('ClusterList') is not None:
            for k1 in m.get('ClusterList'):
                temp_model = main_models.ListComputeClustersResponseBodyPageResultClusterList()
                self.cluster_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListComputeClustersResponseBodyPageResultClusterList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        creator_name: str = None,
        des: str = None,
        id: int = None,
        modifier: str = None,
        modifier_name: str = None,
        modify_time: str = None,
        name: str = None,
        type_version: str = None,
    ):
        # The time when the cluster was created.
        self.create_time = create_time
        # The creator.
        self.creator = creator
        # The creator.
        self.creator_name = creator_name
        # The cluster description.
        self.des = des
        # The cluster ID.
        self.id = id
        # The user who last modified the cluster.
        self.modifier = modifier
        # The user who last modified the cluster.
        self.modifier_name = modifier_name
        # The time when the cluster was last updated.
        self.modify_time = modify_time
        # The cluster name.
        self.name = name
        # The cluster version.
        self.type_version = type_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.des is not None:
            result['Des'] = self.des

        if self.id is not None:
            result['Id'] = self.id

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.type_version is not None:
            result['TypeVersion'] = self.type_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Des') is not None:
            self.des = m.get('Des')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TypeVersion') is not None:
            self.type_version = m.get('TypeVersion')

        return self

