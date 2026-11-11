# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListRightsRequest(DaraModel):
    def __init__(
        self,
        ai_desktop: bool = None,
        business_scene_code: str = None,
        max_results: int = None,
        next_token: str = None,
        order_field: str = None,
        order_type: str = None,
        overseas: int = None,
        rights_active_status: str = None,
        rights_assigned_user: str = None,
        rights_ids: List[str] = None,
        rights_period: str = None,
        rights_resource_id: str = None,
        rights_resource_type: str = None,
        rights_resource_types: List[str] = None,
        rights_spec: str = None,
    ):
        # Optional AI rights filter. Set to true to query only AI rights, or false to query only regular rights, including historical unmarked rights. If you do not specify this parameter, all rights are queried.
        self.ai_desktop = ai_desktop
        # The scenario code for the commercial edition.
        self.business_scene_code = business_scene_code
        # The maximum number of results per page. Specify a positive integer from 1 to 200.
        self.max_results = max_results
        # The pagination token. Do not specify this parameter for the first query. For subsequent queries, pass the NextToken value returned from the previous page exactly as it was returned. The example is for illustration purposes only. Do not construct the token manually.
        self.next_token = next_token
        # The field by which to sort the results, such as gmtCreate, rightsId, or rightsExpireTime. If you do not specify this parameter, the default sorting order of the server is used.
        self.order_field = order_field
        # The sorting order. Valid values: asc and desc (lowercase). Use this parameter together with OrderField.
        self.order_type = order_type
        # Specifies whether the rights apply to regions outside the Chinese mainland, including Hong Kong (China), Macao (China), and Taiwan (China). Valid values:
        # - 0: The Chinese mainland.
        # - 1: Regions outside the Chinese mainland, including Hong Kong (China), Macao (China), and Taiwan (China).
        self.overseas = overseas
        # The rights activation status. Use the returned value to determine whether the activation is complete.
        self.rights_active_status = rights_active_status
        # The end user to whom the rights are assigned. For convenience accounts, use EndUserId.
        self.rights_assigned_user = rights_assigned_user
        # The list of rights IDs to query or activate. Specify the RightsId values returned by ListRights.
        self.rights_ids = rights_ids
        # The rights period code.
        self.rights_period = rights_period
        # The ID of the resource associated with the rights. This value is returned after the resource is created.
        self.rights_resource_id = rights_resource_id
        # The rights resource type. Use Desktop for regular cloud computers. For other commodities, specify the actual rights type.
        self.rights_resource_type = rights_resource_type
        # The list of rights resource types to filter.
        self.rights_resource_types = rights_resource_types
        # The rights specification code. Refer to the rights query results for the actual value.
        self.rights_spec = rights_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_desktop is not None:
            result['AiDesktop'] = self.ai_desktop

        if self.business_scene_code is not None:
            result['BusinessSceneCode'] = self.business_scene_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.overseas is not None:
            result['Overseas'] = self.overseas

        if self.rights_active_status is not None:
            result['RightsActiveStatus'] = self.rights_active_status

        if self.rights_assigned_user is not None:
            result['RightsAssignedUser'] = self.rights_assigned_user

        if self.rights_ids is not None:
            result['RightsIds'] = self.rights_ids

        if self.rights_period is not None:
            result['RightsPeriod'] = self.rights_period

        if self.rights_resource_id is not None:
            result['RightsResourceId'] = self.rights_resource_id

        if self.rights_resource_type is not None:
            result['RightsResourceType'] = self.rights_resource_type

        if self.rights_resource_types is not None:
            result['RightsResourceTypes'] = self.rights_resource_types

        if self.rights_spec is not None:
            result['RightsSpec'] = self.rights_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiDesktop') is not None:
            self.ai_desktop = m.get('AiDesktop')

        if m.get('BusinessSceneCode') is not None:
            self.business_scene_code = m.get('BusinessSceneCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Overseas') is not None:
            self.overseas = m.get('Overseas')

        if m.get('RightsActiveStatus') is not None:
            self.rights_active_status = m.get('RightsActiveStatus')

        if m.get('RightsAssignedUser') is not None:
            self.rights_assigned_user = m.get('RightsAssignedUser')

        if m.get('RightsIds') is not None:
            self.rights_ids = m.get('RightsIds')

        if m.get('RightsPeriod') is not None:
            self.rights_period = m.get('RightsPeriod')

        if m.get('RightsResourceId') is not None:
            self.rights_resource_id = m.get('RightsResourceId')

        if m.get('RightsResourceType') is not None:
            self.rights_resource_type = m.get('RightsResourceType')

        if m.get('RightsResourceTypes') is not None:
            self.rights_resource_types = m.get('RightsResourceTypes')

        if m.get('RightsSpec') is not None:
            self.rights_spec = m.get('RightsSpec')

        return self

