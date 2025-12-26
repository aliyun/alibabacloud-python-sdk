# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class GetResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        computing_resource_provider: str = None,
        creator_id: str = None,
        description: str = None,
        gmt_created_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        resource_type: str = None,
        status: str = None,
        support_rdma: bool = None,
        tags: List[main_models.GetResourceGroupResponseBodyTags] = None,
        user_vpc: main_models.UserVpc = None,
        version: str = None,
        workspace_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.computing_resource_provider = computing_resource_provider
        self.creator_id = creator_id
        self.description = description
        self.gmt_created_time = gmt_created_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.request_id = request_id
        self.resource_type = resource_type
        self.status = status
        self.support_rdma = support_rdma
        self.tags = tags
        self.user_vpc = user_vpc
        self.version = version
        self.workspace_id = workspace_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id

        if self.computing_resource_provider is not None:
            result['ComputingResourceProvider'] = self.computing_resource_provider

        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.support_rdma is not None:
            result['SupportRDMA'] = self.support_rdma

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.version is not None:
            result['Version'] = self.version

        if self.workspace_id is not None:
            result['WorkspaceID'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')

        if m.get('ComputingResourceProvider') is not None:
            self.computing_resource_provider = m.get('ComputingResourceProvider')

        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportRDMA') is not None:
            self.support_rdma = m.get('SupportRDMA')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetResourceGroupResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserVpc') is not None:
            temp_model = main_models.UserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkspaceID') is not None:
            self.workspace_id = m.get('WorkspaceID')

        return self

class GetResourceGroupResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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

