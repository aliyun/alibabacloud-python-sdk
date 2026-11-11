# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListRouteMapsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        filter: List[main_models.ListRouteMapsRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        route_map_ids: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The actual query is not performed. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the dry run, the corresponding error is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # - **false**: performs a normal request. This is the default value.
        self.dry_run = dry_run
        # The filter conditions.
        # 
        # You can specify up to 5 filter conditions at a time.
        self.filter = filter
        # The number of entries to return on each page. Valid values: 1 to 100.
        # If you do not specify the MaxResults parameter, pagination is not used. After you call the operation, the value of MaxResults indicates the total number of entries. If you specify the MaxResults parameter, pagination is used. After you call the operation, the value of MaxResults indicates the number of entries returned in the current query. We recommend that you set the MaxResults parameter to 20.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. Valid values:
        # 
        # - If this is the first query or no subsequent query is to be sent, you do not need to specify this parameter.
        # - If a subsequent query is to be sent, set the value to the NextToken value returned from the previous API call.
        self.next_token = next_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The IDs of the route maps to query. If you do not specify this parameter, all route maps are queried.
        self.route_map_ids = route_map_ids

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_map_ids is not None:
            result['RouteMapIds'] = self.route_map_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListRouteMapsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteMapIds') is not None:
            self.route_map_ids = m.get('RouteMapIds')

        return self

class ListRouteMapsRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The filter condition. Valid values:
        # 
        # - **Direction**: the direction of the route map.
        # - **Name**: the name of the route map.
        # - **Priority**: the priority of the route map.
        # 
        # By default, multiple filter conditions have a logical AND relationship. A route map is returned only when it meets all filter conditions.
        # 
        # You can specify up to 5 filter conditions at a time.
        self.key = key
        # The value of the filter condition.
        # 
        # Specify the filter value based on the Key. You can specify multiple filter values for a single Key. Multiple filter values have a logical OR relationship. A route map is returned when it meets any of the filter values.
        # 
        # You can specify up to 5 filter values for a single filter condition.
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

