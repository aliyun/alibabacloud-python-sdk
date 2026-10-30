# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListRouteMapRulesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        filter: List[main_models.ListRouteMapRulesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        route_map_id: str = None,
        route_map_rule_ids: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value on your client to ensure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # 
        # - **true**: sends a check request and does not query the route map rules. Check items include whether required parameters are specified, request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the error code DryRunOperation is returned.
        # - **false** (default): sends a normal request and directly queries the route map rules after the check succeeds.
        self.dry_run = dry_run
        # The information about the filter conditions.
        # 
        # You can specify up to 5 filter conditions at a time.
        self.filter = filter
        # The number of entries to return on each page in a paginated query.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - You do not need to specify this parameter for the first query or when no next query is available.
        # - If a next query is available, set this parameter to the **NextToken** value returned by the previous API call.
        self.next_token = next_token
        # The ID of the route map to query.
        self.route_map_id = route_map_id
        # The list of route map rule IDs to query. This parameter and filter conditions can be used together for matching, and they have an AND relationship.
        self.route_map_rule_ids = route_map_rule_ids

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

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        if self.route_map_rule_ids is not None:
            result['RouteMapRuleIds'] = self.route_map_rule_ids

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
                temp_model = main_models.ListRouteMapRulesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        if m.get('RouteMapRuleIds') is not None:
            self.route_map_rule_ids = m.get('RouteMapRuleIds')

        return self

class ListRouteMapRulesRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The filter condition. Valid values:
        # 
        # - **Name**: the name of the route map rule.
        # - **Priority**: the priority of the route map rule.
        # 
        # By default, multiple filter conditions have an AND relationship. A match succeeds only when all filter conditions are met.
        # 
        # You can specify up to 5 filter conditions at a time.
        self.key = key
        # The value of the filter condition.
        # 
        # Specify the filter value based on the Key parameter. You can specify multiple filter values for a single key. Multiple filter values have an OR relationship. A match succeeds if any of the filter values is met.
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

