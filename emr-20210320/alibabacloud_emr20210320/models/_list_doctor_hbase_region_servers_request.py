# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDoctorHBaseRegionServersRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        date_time: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        order_type: str = None,
        region_id: str = None,
        region_server_hosts: List[str] = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The query date.
        # 
        # This parameter is required.
        self.date_time = date_time
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The field that you use to sort the query results. Valid value:
        # 
        # *   regionCount: the number of regions.
        self.order_by = order_by
        # The order in which you want to sort the query results. Valid value:
        # 
        # *   ASC: in ascending order
        # *   DESC: in descending order
        self.order_type = order_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The RegionServer hosts.
        self.region_server_hosts = region_server_hosts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_server_hosts is not None:
            result['RegionServerHosts'] = self.region_server_hosts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionServerHosts') is not None:
            self.region_server_hosts = m.get('RegionServerHosts')

        return self

