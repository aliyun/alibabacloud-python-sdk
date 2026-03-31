# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudClustersResponseBody(DaraModel):
    def __init__(
        self,
        cluster_infos: List[main_models.DescribeHybridCloudClustersResponseBodyClusterInfos] = None,
        request_id: str = None,
    ):
        # The information about the clusters.
        self.cluster_infos = cluster_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cluster_infos:
            for v1 in self.cluster_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterInfos'] = []
        if self.cluster_infos is not None:
            for k1 in self.cluster_infos:
                result['ClusterInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_infos = []
        if m.get('ClusterInfos') is not None:
            for k1 in m.get('ClusterInfos'):
                temp_model = main_models.DescribeHybridCloudClustersResponseBodyClusterInfos()
                self.cluster_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHybridCloudClustersResponseBodyClusterInfos(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        access_region: str = None,
        cluster_name: str = None,
        cluster_resource_id: str = None,
        http_ports: str = None,
        https_ports: str = None,
        id: int = None,
        protection_server_count: int = None,
        proxy_status: str = None,
        proxy_type: str = None,
        remark: str = None,
        rule_config: str = None,
        rule_status: str = None,
        rule_type: str = None,
    ):
        # The network access mode. Valid values:
        # 
        # *   **internet**: Internet access.
        # *   **vpc**: internal network access by using Express Connect circuits.
        self.access_mode = access_mode
        # The region where the virtual private cloud (VPC) resides. Valid values:
        # 
        # *   **cn-hangzhou**: China (Hangzhou).
        # *   **cn-beiijng**: China (Beijing).
        # *   **cn-shanghai**: China (Shanghai).
        self.access_region = access_region
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The ID of the hybrid cloud cluster resource.
        self.cluster_resource_id = cluster_resource_id
        # The HTTP ports. The value is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.http_ports = http_ports
        # The HTTPS ports. The value is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.https_ports = https_ports
        # The ID of the cluster.
        self.id = id
        # The number of protection nodes that can be added to the cluster.
        self.protection_server_count = protection_server_count
        # The status of the proxy gateway. Valid values:
        # 
        # *   **on**: enabled.
        # *   **off**: disabled.
        self.proxy_status = proxy_status
        # The type of the cluster. Valid values:
        # 
        # *   **cname**: reverse proxy cluster.
        # *   **service**: SDK-based traffic mirroring cluster.
        self.proxy_type = proxy_type
        # The remarks about the cluster.
        self.remark = remark
        # The configurations of the rule.
        self.rule_config = rule_config
        # The status of manual bypass. Valid values:
        # 
        # *   **on**: enabled.
        # *   **off**: disabled.
        self.rule_status = rule_status
        # The type of the rule. Valid value:
        # 
        # *   **bypass**: Requests are allowed without security checks.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        if self.access_region is not None:
            result['AccessRegion'] = self.access_region

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_resource_id is not None:
            result['ClusterResourceId'] = self.cluster_resource_id

        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        if self.id is not None:
            result['Id'] = self.id

        if self.protection_server_count is not None:
            result['ProtectionServerCount'] = self.protection_server_count

        if self.proxy_status is not None:
            result['ProxyStatus'] = self.proxy_status

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        if m.get('AccessRegion') is not None:
            self.access_region = m.get('AccessRegion')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterResourceId') is not None:
            self.cluster_resource_id = m.get('ClusterResourceId')

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProtectionServerCount') is not None:
            self.protection_server_count = m.get('ProtectionServerCount')

        if m.get('ProxyStatus') is not None:
            self.proxy_status = m.get('ProxyStatus')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

