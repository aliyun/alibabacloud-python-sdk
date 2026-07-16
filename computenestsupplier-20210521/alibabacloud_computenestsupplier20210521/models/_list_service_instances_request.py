# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstancesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.ListServiceInstancesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        show_deleted: bool = None,
        tag: List[main_models.ListServiceInstancesRequestTag] = None,
    ):
        # The filter.
        self.filter = filter
        # The number of entries to return on each page. Maximum value: 100. Default value: 20.
        self.max_results = max_results
        # The query token. Set it to the NextToken value returned from the previous API call.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to display the deleted service instances. Valid values:
        # 
        # - true: Displays the deleted service instances.
        # 
        # - false: Does not display the deleted service instances.
        self.show_deleted = show_deleted
        # The custom tags.
        self.tag = tag

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show_deleted is not None:
            result['ShowDeleted'] = self.show_deleted

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListServiceInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShowDeleted') is not None:
            self.show_deleted = m.get('ShowDeleted')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListServiceInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListServiceInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListServiceInstancesRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The name of the filter. You can specify one or more filter names to query service instances. Valid values:
        # 
        # - Name: The name of the service. To perform a fuzzy search, enter the content in the \\*xxx\\* format for the value parameter. For example, if the service name is `My Service`, you can enter `*My*` or `*Service*` for a fuzzy search.
        # 
        # - ServiceInstanceId: The ID of the service instance.
        # 
        # - ServiceId: The ID of the service.
        # 
        # - UserId: The ID of the user.
        # 
        # - Version: The version of the service.
        # 
        # - Status: The status of the service instance.
        # 
        # - DeployType: The deployment type.
        # 
        # - ServiceType: The service type.
        # 
        # - OperationStartTimeBefore: The time before the start of the Alibaba Cloud Managed Services.
        # 
        # - OperationStartTimeAfter: The time after the start of the Alibaba Cloud Managed Services.
        # 
        # - OperationEndTimeBefore: The time before the end of the Alibaba Cloud Managed Services.
        # 
        # - OperationEndTimeAfter: The time after the end of the Alibaba Cloud Managed Services.
        # 
        # - OperatedServiceInstanceId: The ID of the managed service instance for a private service.
        # 
        # - OperationServiceInstanceId: The ID of the service instance for a pure Alibaba Cloud Managed Service.
        # 
        # - EnableInstanceOps: Indicates whether Alibaba Cloud Managed Services are enabled for the service instance.
        self.name = name
        # A list of filter values.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

