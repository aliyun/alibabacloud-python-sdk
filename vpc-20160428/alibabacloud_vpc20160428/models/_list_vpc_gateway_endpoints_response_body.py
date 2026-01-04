# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListVpcGatewayEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        endpoints: List[main_models.ListVpcGatewayEndpointsResponseBodyEndpoints] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of gateway endpoints.
        self.endpoints = endpoints
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next queries are sent.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.ListVpcGatewayEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListVpcGatewayEndpointsResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        associated_route_tables: List[str] = None,
        creation_time: str = None,
        endpoint_description: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        policy_document: str = None,
        resource_group_id: str = None,
        service_name: str = None,
        tags: List[main_models.ListVpcGatewayEndpointsResponseBodyEndpointsTags] = None,
        vpc_id: str = None,
    ):
        # The ID of the route table associated with the gateway endpoint.
        self.associated_route_tables = associated_route_tables
        # The time when the endpoint was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the gateway endpoint.
        self.endpoint_description = endpoint_description
        # The ID of the gateway endpoint.
        self.endpoint_id = endpoint_id
        # The name of the gateway endpoint.
        self.endpoint_name = endpoint_name
        # The status of the gateway endpoint. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Modifying**
        # *   **Associating**
        # *   **Dissociating**
        # *   **Deleting**
        self.endpoint_status = endpoint_status
        # The access policy for the cloud service.
        # 
        # For more information about the syntax and structure of the access policy, see [Policy syntax and structure](https://help.aliyun.com/document_detail/93739.html).
        self.policy_document = policy_document
        # The ID of the resource group to which the gateway endpoint belongs.
        self.resource_group_id = resource_group_id
        # The name of the endpoint service.
        self.service_name = service_name
        # The tag list.
        self.tags = tags
        # The ID of the virtual private cloud (VPC) to which the gateway endpoint belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_route_tables is not None:
            result['AssociatedRouteTables'] = self.associated_route_tables

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedRouteTables') is not None:
            self.associated_route_tables = m.get('AssociatedRouteTables')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListVpcGatewayEndpointsResponseBodyEndpointsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListVpcGatewayEndpointsResponseBodyEndpointsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the resource.
        self.key = key
        # The value of tag N added to the resource.
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

