# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDashboardsByNameRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        dash_board_name: str = None,
        dash_board_version: str = None,
        data_source_type: str = None,
        group_name: str = None,
        only_query: bool = None,
        product_code: str = None,
        region_id: str = None,
    ):
        # The ID of the cluster. If the ClusterType parameter is not set to `cloud-product-prometheus` or `cms-enterprise-prometheus`, you must specify the ClusterId parameter.
        self.cluster_id = cluster_id
        # The cluster type. Valid values:
        # 
        # *   vpc-prometheus
        # *   cloud-product-prometheus
        # *   cms-enterprise-prometheus
        # *   ExternalKubernetes
        # *   Ask
        # *   Kubernetes
        # *   ManagedKubernetes
        # *   remote-write-prometheus
        # *   GlobalViewV2
        self.cluster_type = cluster_type
        # The name of the dashboard.
        self.dash_board_name = dash_board_name
        # The version of the dashboard.
        self.dash_board_version = dash_board_version
        # The type of the data source. Valid values:
        # 
        # *   loki
        # *   prometheus
        self.data_source_type = data_source_type
        # The name of the dashboard group.
        self.group_name = group_name
        # Specifies whether to display the Grafana dashboard only in the Application Real-Time Monitoring Service (ARMS) console.
        self.only_query = only_query
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.dash_board_name is not None:
            result['DashBoardName'] = self.dash_board_name

        if self.dash_board_version is not None:
            result['DashBoardVersion'] = self.dash_board_version

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.only_query is not None:
            result['OnlyQuery'] = self.only_query

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DashBoardName') is not None:
            self.dash_board_name = m.get('DashBoardName')

        if m.get('DashBoardVersion') is not None:
            self.dash_board_version = m.get('DashBoardVersion')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('OnlyQuery') is not None:
            self.only_query = m.get('OnlyQuery')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

