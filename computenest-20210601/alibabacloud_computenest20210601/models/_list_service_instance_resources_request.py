# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceResourcesRequest(DaraModel):
    def __init__(
        self,
        filters: List[main_models.ListServiceInstanceResourcesRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
        service_instance_resource_type: str = None,
        tag: List[main_models.ListServiceInstanceResourcesRequestTag] = None,
    ):
        # The filter conditions. Vaild values:
        # 
        # - ExpireTimeStart：
        # Query start time for Subscription resource expiration.
        # <notice>Notice Note: Only supports querying service instances on private deployments.>Notice: 
        # 
        # - ExpireTimeEnd：Query end time for Subscription resource expiration.
        # <notice>Notice Note: Only supports querying service instances on private deployments.>Notice: 
        # 
        # - PayType：The billing method of the read-only instance. 
        # <notice>Notice Note: Only supports querying service instances on private deployments.<notice> 
        # 
        #    Valid values:
        # 
        #    - PayAsYouGo
        # 
        #    - Subscription
        # 
        # - ResourceARN：The Alibaba Cloud Resource Name (ARN) of a resource.
        self.filters = filters
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If **NextToken** is not returned, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The region ID. Valid values:
        # 
        # *   cn-hangzhou: China (Hangzhou).
        # *   ap-southeast-1: Singapore.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id
        # Service Instance resource type，include AliyunResource and ContainerResource.
        self.service_instance_resource_type = service_instance_resource_type
        # The tag key and value.
        self.tag = tag

    def validate(self):
        if self.filters:
            for v1 in self.filters:
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
        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_instance_resource_type is not None:
            result['ServiceInstanceResourceType'] = self.service_instance_resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ListServiceInstanceResourcesRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceInstanceResourceType') is not None:
            self.service_instance_resource_type = m.get('ServiceInstanceResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListServiceInstanceResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListServiceInstanceResourcesRequestTag(DaraModel):
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

class ListServiceInstanceResourcesRequestFilters(DaraModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # Vaild values:
        # - ExpireTimeStart
        # - ExpireTimeEnd
        # - PayType
        # - ResourceARN
        self.name = name
        # The value of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

