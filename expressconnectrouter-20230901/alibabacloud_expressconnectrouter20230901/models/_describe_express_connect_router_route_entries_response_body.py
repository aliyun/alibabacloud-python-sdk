# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressConnectRouterRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        route_entries_list: List[main_models.DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The status code that indicates whether the call is successful. A value of 200 indicates success. Other values indicate failure. For more information about the cause of failure, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace `%s` in the **ErrMessage** error message.
        # 
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of entries returned. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The message returned for the instance operation.
        self.message = message
        # The token for the next query. Valid values:
        # 
        # - If **NextToken** is empty, no subsequent query is required.
        # - If **NextToken** has a return value, the value indicates the token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of route entries.
        self.route_entries_list = route_entries_list
        # Indicates whether the call was successful. Valid values:
        # - **True**: The call was successful.
        # - **False**: The call failed.
        self.success = success
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.route_entries_list:
            for v1 in self.route_entries_list:
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

        result['RouteEntriesList'] = []
        if self.route_entries_list is not None:
            for k1 in self.route_entries_list:
                result['RouteEntriesList'].append(k1.to_map() if k1 else None)

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

        self.route_entries_list = []
        if m.get('RouteEntriesList') is not None:
            for k1 in m.get('RouteEntriesList'):
                temp_model = main_models.DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList()
                self.route_entries_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList(DaraModel):
    def __init__(
        self,
        as_path: str = None,
        community: str = None,
        destination_cidr_block: str = None,
        med: int = None,
        nexthop_instance_id: str = None,
        nexthop_instance_region_id: str = None,
        status: str = None,
    ):
        # The AS path traversed by the route entry.
        self.as_path = as_path
        # The community value carried by the BGP route entry.
        self.community = community
        # The destination CIDR block of the route entry.
        self.destination_cidr_block = destination_cidr_block
        # The MED value carried by the BGP route entry, which takes effect for routing between the Express Connect Router (ECR) and the TR. 
        # - The MED value can be set to 2000. After the configuration, the TR and the Express Connect Router (ECR) serve as the default path. 
        # - For a non-default path, the MED value is empty. 
        # - For TRs in the same Cloud Enterprise Network (CEN), only one associated object can have the MED value set to 2000.
        self.med = med
        # The next hop instance ID.
        self.nexthop_instance_id = nexthop_instance_id
        # The region where the next hop instance resides.
        self.nexthop_instance_region_id = nexthop_instance_region_id
        # The status of the Express Connect Router (ECR) instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_path is not None:
            result['AsPath'] = self.as_path

        if self.community is not None:
            result['Community'] = self.community

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.med is not None:
            result['Med'] = self.med

        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id

        if self.nexthop_instance_region_id is not None:
            result['NexthopInstanceRegionId'] = self.nexthop_instance_region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')

        if m.get('Community') is not None:
            self.community = m.get('Community')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('Med') is not None:
            self.med = m.get('Med')

        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')

        if m.get('NexthopInstanceRegionId') is not None:
            self.nexthop_instance_region_id = m.get('NexthopInstanceRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

