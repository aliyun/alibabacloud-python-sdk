# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class ListRouteMapAssociationsResponseBody(DaraModel):
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
        route_map_association_list: List[main_models.ListRouteMapAssociationsResponseBodyRouteMapAssociationList] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of the access denied error.
        self.access_denied_detail = access_denied_detail
        # The status code that indicates whether the call is successful. A value of 200 indicates success. Other values indicate failure. For more information about the causes of failure, see error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace `%s` in the **ErrMessage** error message.
        # 
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, the **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of entries returned.
        self.max_results = max_results
        # The message returned for the operation.
        self.message = message
        # The token that is used to start the next query. Valid values:
        # 
        # - If **NextToken** is empty, no next query is to be sent.
        # - If **NextToken** has a return value, the value indicates the token used to start the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of route map associations.
        self.route_map_association_list = route_map_association_list
        # Indicates whether the call is successful. Valid values:
        # 
        # - **True**: The call is successful.
        # - **False**: The call fails.
        self.success = success
        # The total number of route map associations.
        self.total_count = total_count

    def validate(self):
        if self.route_map_association_list:
            for v1 in self.route_map_association_list:
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

        result['RouteMapAssociationList'] = []
        if self.route_map_association_list is not None:
            for k1 in self.route_map_association_list:
                result['RouteMapAssociationList'].append(k1.to_map() if k1 else None)

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

        self.route_map_association_list = []
        if m.get('RouteMapAssociationList') is not None:
            for k1 in m.get('RouteMapAssociationList'):
                temp_model = main_models.ListRouteMapAssociationsResponseBodyRouteMapAssociationList()
                self.route_map_association_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRouteMapAssociationsResponseBodyRouteMapAssociationList(DaraModel):
    def __init__(
        self,
        association_id: str = None,
        direction: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        priority: int = None,
        region_id_list: List[str] = None,
        route_map_id: str = None,
        status: str = None,
        version: int = None,
    ):
        # The ID of the route map association.
        self.association_id = association_id
        # The direction in which the routing policy is applied. Valid values:
        # 
        # - **Inbound**: the inbound region gateway direction, indicating the direction in which routing is transmitted to the Express Connect Router (ECR).
        # - **Outbound**: the outbound region gateway direction, indicating the direction in which routing is transmitted from the Express Connect Router (ECR).
        self.direction = direction
        # The instance ID of the Express Connect Router (ECR).
        self.ecr_id = ecr_id
        # The time when the route map association was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the route map association was updated.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The priority of the route map. A smaller value indicates a higher priority.
        self.priority = priority
        # The list of region IDs where the route map is distributed and takes effect.
        self.region_id_list = region_id_list
        # The ID of the route map.
        self.route_map_id = route_map_id
        # The status of the route map association. Valid values:
        # 
        # - **CREATING**: The association is being created.
        # - **ACTIVE**: The association is in a normal state, and no operations are in progress.
        # - **DELETING**: The association is being deleted.
        # - **UPDATING**: The association is being updated.
        # - **DELETED**: The association is deleted.
        self.status = status
        # The version number of the route map. The version number increments when the route map in the CEN is changed.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_id is not None:
            result['AssociationId'] = self.association_id

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id_list is not None:
            result['RegionIdList'] = self.region_id_list

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionIdList') is not None:
            self.region_id_list = m.get('RegionIdList')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

