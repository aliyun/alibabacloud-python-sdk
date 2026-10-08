# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCVClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        mysql_operator: main_models.DescribeRCVClusterResponseBodyMysqlOperator = None,
        region: str = None,
        request_id: str = None,
        support_disk_performance_level: List[str] = None,
        vcluster_status: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.mysql_operator = mysql_operator
        self.region = region
        self.request_id = request_id
        self.support_disk_performance_level = support_disk_performance_level
        self.vcluster_status = vcluster_status
        self.vpc_id = vpc_id

    def validate(self):
        if self.mysql_operator:
            self.mysql_operator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.mysql_operator is not None:
            result['MysqlOperator'] = self.mysql_operator.to_map()

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_disk_performance_level is not None:
            result['SupportDiskPerformanceLevel'] = self.support_disk_performance_level

        if self.vcluster_status is not None:
            result['VClusterStatus'] = self.vcluster_status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('MysqlOperator') is not None:
            temp_model = main_models.DescribeRCVClusterResponseBodyMysqlOperator()
            self.mysql_operator = temp_model.from_map(m.get('MysqlOperator'))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportDiskPerformanceLevel') is not None:
            self.support_disk_performance_level = m.get('SupportDiskPerformanceLevel')

        if m.get('VClusterStatus') is not None:
            self.vcluster_status = m.get('VClusterStatus')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeRCVClusterResponseBodyMysqlOperator(DaraModel):
    def __init__(
        self,
        dashboard_public_endpoint: str = None,
        dashboard_username: str = None,
        dashboard_vpc_endpoint: str = None,
        deploy_time: str = None,
        status: str = None,
    ):
        self.dashboard_public_endpoint = dashboard_public_endpoint
        self.dashboard_username = dashboard_username
        self.dashboard_vpc_endpoint = dashboard_vpc_endpoint
        self.deploy_time = deploy_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_public_endpoint is not None:
            result['DashboardPublicEndpoint'] = self.dashboard_public_endpoint

        if self.dashboard_username is not None:
            result['DashboardUsername'] = self.dashboard_username

        if self.dashboard_vpc_endpoint is not None:
            result['DashboardVpcEndpoint'] = self.dashboard_vpc_endpoint

        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardPublicEndpoint') is not None:
            self.dashboard_public_endpoint = m.get('DashboardPublicEndpoint')

        if m.get('DashboardUsername') is not None:
            self.dashboard_username = m.get('DashboardUsername')

        if m.get('DashboardVpcEndpoint') is not None:
            self.dashboard_vpc_endpoint = m.get('DashboardVpcEndpoint')

        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

