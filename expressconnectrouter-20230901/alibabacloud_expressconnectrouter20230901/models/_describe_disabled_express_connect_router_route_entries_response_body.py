# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeDisabledExpressConnectRouterRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        disabled_route_entry_list: List[main_models.DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The status code. A value of 200 indicates that the call was successful. Other values indicate that the call failed. For more information about the causes of failure, see error codes.
        self.code = code
        # The list of queried route entries.
        self.disabled_route_entry_list = disabled_route_entry_list
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace `%s` in the **ErrMessage** error message.
        # 
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsInstanceId**, it indicates that the **DtsInstanceId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of entries to return. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The message returned by the operation.
        self.message = message
        # The token for the next query. Valid values:
        # 
        # - If NextToken is empty, no next query is required.
        # - If NextToken is returned, the value indicates the token for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the disabled Express Connect Router (ECR) routing is successfully queried. Valid values:
        # - **True**: The query was successful.
        # - **False**: The query failed.
        self.success = success
        # The total number of route entry.
        self.total_count = total_count

    def validate(self):
        if self.disabled_route_entry_list:
            for v1 in self.disabled_route_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['DisabledRouteEntryList'] = []
        if self.disabled_route_entry_list is not None:
            for k1 in self.disabled_route_entry_list:
                result['DisabledRouteEntryList'].append(k1.to_map() if k1 else None)

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.disabled_route_entry_list = []
        if m.get('DisabledRouteEntryList') is not None:
            for k1 in m.get('DisabledRouteEntryList'):
                temp_model = main_models.DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList()
                self.disabled_route_entry_list.append(temp_model.from_map(k1))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        nexthop_instance_id: str = None,
        nexthop_instance_region_id: str = None,
    ):
        # The destination CIDR block of the route entry.
        self.destination_cidr_block = destination_cidr_block
        # The instance ID of the Express Connect Router (ECR).
        self.ecr_id = ecr_id
        # The time when the route entry was created.
        self.gmt_create = gmt_create
        # The instance ID of the next hop.
        self.nexthop_instance_id = nexthop_instance_id
        # The region ID of the next hop instance.
        self.nexthop_instance_region_id = nexthop_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id

        if self.nexthop_instance_region_id is not None:
            result['NexthopInstanceRegionId'] = self.nexthop_instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')

        if m.get('NexthopInstanceRegionId') is not None:
            self.nexthop_instance_region_id = m.get('NexthopInstanceRegionId')

        return self

