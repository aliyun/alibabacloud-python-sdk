# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHybridCloudClusterRequest(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        access_region: str = None,
        cluster_name: str = None,
        http_ports: str = None,
        https_ports: str = None,
        id: int = None,
        instance_id: str = None,
        log_fields_not_returned: str = None,
        protection_server_count: int = None,
        proxy_status: str = None,
        proxy_type: str = None,
        region_id: str = None,
        remark: str = None,
        resource_manager_resource_group_id: str = None,
        rule_config: str = None,
        rule_status: str = None,
        rule_type: str = None,
    ):
        # This parameter is required.
        self.access_mode = access_mode
        self.access_region = access_region
        # The name of the cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The HTTP ports that are supported. Set this parameter to a string. Specify multiple ports in the **port1,port2,port3** format.
        # 
        # This parameter is required.
        self.http_ports = http_ports
        # The HTTPS ports that are supported. Set this parameter to a string. Specify multiple ports in the **port1,port2,port3** format.
        # 
        # This parameter is required.
        self.https_ports = https_ports
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.id = id
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.log_fields_not_returned = log_fields_not_returned
        # The number of protection nodes that can be added to the cluster.
        # 
        # This parameter is required.
        self.protection_server_count = protection_server_count
        self.proxy_status = proxy_status
        self.proxy_type = proxy_type
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The remarks about the cluster.
        self.remark = remark
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        self.rule_config = rule_config
        self.rule_status = rule_status
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

        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_fields_not_returned is not None:
            result['LogFieldsNotReturned'] = self.log_fields_not_returned

        if self.protection_server_count is not None:
            result['ProtectionServerCount'] = self.protection_server_count

        if self.proxy_status is not None:
            result['ProxyStatus'] = self.proxy_status

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

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

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogFieldsNotReturned') is not None:
            self.log_fields_not_returned = m.get('LogFieldsNotReturned')

        if m.get('ProtectionServerCount') is not None:
            self.protection_server_count = m.get('ProtectionServerCount')

        if m.get('ProxyStatus') is not None:
            self.proxy_status = m.get('ProxyStatus')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

