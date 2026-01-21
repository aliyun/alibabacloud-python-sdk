# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        instance_attribute: main_models.DescribeInstanceAttributeResponseBodyInstanceAttribute = None,
        request_id: str = None,
    ):
        # The attribute information about the bastion host.
        self.instance_attribute = instance_attribute
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_attribute:
            self.instance_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_attribute is not None:
            result['InstanceAttribute'] = self.instance_attribute.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceAttribute') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyInstanceAttribute()
            self.instance_attribute = temp_model.from_map(m.get('InstanceAttribute'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceAttributeResponseBodyInstanceAttribute(DaraModel):
    def __init__(
        self,
        app_operation_module: str = None,
        authorized_security_groups: List[str] = None,
        bandwidth: str = None,
        bandwidth_package: str = None,
        db_operation_module: str = None,
        description: str = None,
        eni_instance_id: str = None,
        expire_time: int = None,
        hsmmodule: str = None,
        idaa_smodule: str = None,
        instance_id: str = None,
        instance_status: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        kms_secret_module: str = None,
        license_code: str = None,
        modify_password_module: str = None,
        network_proxy_module: str = None,
        ports: List[main_models.DescribeInstanceAttributeResponseBodyInstanceAttributePorts] = None,
        private_export_ips: List[str] = None,
        private_white_list: List[str] = None,
        public_export_ips: List[str] = None,
        public_ips: List[str] = None,
        public_network_access: bool = None,
        public_white_list: List[str] = None,
        rdmodule: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        router_rules: List[str] = None,
        script_deliver_module: str = None,
        security_group_ids: List[str] = None,
        slave_vswitch_id: str = None,
        start_time: int = None,
        storage: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        web_terminal_module: str = None,
        white_list_policies: List[main_models.DescribeInstanceAttributeResponseBodyInstanceAttributeWhiteListPolicies] = None,
    ):
        self.app_operation_module = app_operation_module
        # The IDs of authorized security groups.
        self.authorized_security_groups = authorized_security_groups
        # The total bandwidth of the bastion host.
        self.bandwidth = bandwidth
        # The bandwidth plan ID.
        self.bandwidth_package = bandwidth_package
        # The status of the database O&M feature.
        self.db_operation_module = db_operation_module
        # The description of the instance.
        self.description = description
        # The ID of the Elastic Network Interface (ENI).
        self.eni_instance_id = eni_instance_id
        # The time when the instance expires.
        self.expire_time = expire_time
        self.hsmmodule = hsmmodule
        self.idaa_smodule = idaa_smodule
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the instance. Valid values:
        # 
        # *   PENDING: The instance is not initialized.
        # *   CREATING: The instance is being created.
        # *   RUNNING: The instance is running.
        # *   EXPIRED: The instance expired.
        # *   CREATE_FAILED: The instance fails to be created.
        # *   UPGRADING: The configurations of the instance are being changed.
        # *   UPGRADE_FAILED: The configurations of the instance fail to be changed.
        self.instance_status = instance_status
        # The public endpoint.
        self.internet_endpoint = internet_endpoint
        # The private endpoint.
        self.intranet_endpoint = intranet_endpoint
        self.kms_secret_module = kms_secret_module
        # The license code.
        self.license_code = license_code
        # The status of the automatic password change feature.
        # 
        # - **Enable**
        # - **Disable**
        self.modify_password_module = modify_password_module
        # The status of the network domain feature.
        # 
        # - **Enable**
        # - **Disable**
        self.network_proxy_module = network_proxy_module
        # An array that consists of the O&M ports of the bastion host.
        self.ports = ports
        # An array that consists of the egress private IP addresses of the bastion host.
        self.private_export_ips = private_export_ips
        # The private IP addresses that are allowed to access the instance.
        self.private_white_list = private_white_list
        # An array that consists of the egress public IP addresses of the bastion host.
        self.public_export_ips = public_export_ips
        # The public IP address.
        self.public_ips = public_ips
        # Indicates whether the Bastionhost instance can be accessed over the Internet.
        self.public_network_access = public_network_access
        # The public IP addresses that are allowed to access the instance.
        self.public_white_list = public_white_list
        self.rdmodule = rdmodule
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.router_rules = router_rules
        self.script_deliver_module = script_deliver_module
        # The IDs of the security groups to which the instance belongs.
        self.security_group_ids = security_group_ids
        self.slave_vswitch_id = slave_vswitch_id
        # The time when the instance started.
        self.start_time = start_time
        # The storage capacity of the bastion host. Unit: bytes.
        self.storage = storage
        # The ID of the VPC to which the instance belongs.
        self.vpc_id = vpc_id
        # The ID of the vSwitch to which the instance connects.
        self.vswitch_id = vswitch_id
        # The status of the web terminal.
        # 
        # - **Enable**
        # - **Disable**
        self.web_terminal_module = web_terminal_module
        self.white_list_policies = white_list_policies

    def validate(self):
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()
        if self.white_list_policies:
            for v1 in self.white_list_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_operation_module is not None:
            result['AppOperationModule'] = self.app_operation_module

        if self.authorized_security_groups is not None:
            result['AuthorizedSecurityGroups'] = self.authorized_security_groups

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package is not None:
            result['BandwidthPackage'] = self.bandwidth_package

        if self.db_operation_module is not None:
            result['DbOperationModule'] = self.db_operation_module

        if self.description is not None:
            result['Description'] = self.description

        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.hsmmodule is not None:
            result['HSMModule'] = self.hsmmodule

        if self.idaa_smodule is not None:
            result['IDaaSModule'] = self.idaa_smodule

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint

        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint

        if self.kms_secret_module is not None:
            result['KmsSecretModule'] = self.kms_secret_module

        if self.license_code is not None:
            result['LicenseCode'] = self.license_code

        if self.modify_password_module is not None:
            result['ModifyPasswordModule'] = self.modify_password_module

        if self.network_proxy_module is not None:
            result['NetworkProxyModule'] = self.network_proxy_module

        result['Ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['Ports'].append(k1.to_map() if k1 else None)

        if self.private_export_ips is not None:
            result['PrivateExportIps'] = self.private_export_ips

        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list

        if self.public_export_ips is not None:
            result['PublicExportIps'] = self.public_export_ips

        if self.public_ips is not None:
            result['PublicIps'] = self.public_ips

        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access

        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list

        if self.rdmodule is not None:
            result['RDModule'] = self.rdmodule

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.router_rules is not None:
            result['RouterRules'] = self.router_rules

        if self.script_deliver_module is not None:
            result['ScriptDeliverModule'] = self.script_deliver_module

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.slave_vswitch_id is not None:
            result['SlaveVswitchId'] = self.slave_vswitch_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.web_terminal_module is not None:
            result['WebTerminalModule'] = self.web_terminal_module

        result['WhiteListPolicies'] = []
        if self.white_list_policies is not None:
            for k1 in self.white_list_policies:
                result['WhiteListPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppOperationModule') is not None:
            self.app_operation_module = m.get('AppOperationModule')

        if m.get('AuthorizedSecurityGroups') is not None:
            self.authorized_security_groups = m.get('AuthorizedSecurityGroups')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackage') is not None:
            self.bandwidth_package = m.get('BandwidthPackage')

        if m.get('DbOperationModule') is not None:
            self.db_operation_module = m.get('DbOperationModule')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HSMModule') is not None:
            self.hsmmodule = m.get('HSMModule')

        if m.get('IDaaSModule') is not None:
            self.idaa_smodule = m.get('IDaaSModule')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')

        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')

        if m.get('KmsSecretModule') is not None:
            self.kms_secret_module = m.get('KmsSecretModule')

        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')

        if m.get('ModifyPasswordModule') is not None:
            self.modify_password_module = m.get('ModifyPasswordModule')

        if m.get('NetworkProxyModule') is not None:
            self.network_proxy_module = m.get('NetworkProxyModule')

        self.ports = []
        if m.get('Ports') is not None:
            for k1 in m.get('Ports'):
                temp_model = main_models.DescribeInstanceAttributeResponseBodyInstanceAttributePorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('PrivateExportIps') is not None:
            self.private_export_ips = m.get('PrivateExportIps')

        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')

        if m.get('PublicExportIps') is not None:
            self.public_export_ips = m.get('PublicExportIps')

        if m.get('PublicIps') is not None:
            self.public_ips = m.get('PublicIps')

        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')

        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')

        if m.get('RDModule') is not None:
            self.rdmodule = m.get('RDModule')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouterRules') is not None:
            self.router_rules = m.get('RouterRules')

        if m.get('ScriptDeliverModule') is not None:
            self.script_deliver_module = m.get('ScriptDeliverModule')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SlaveVswitchId') is not None:
            self.slave_vswitch_id = m.get('SlaveVswitchId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('WebTerminalModule') is not None:
            self.web_terminal_module = m.get('WebTerminalModule')

        self.white_list_policies = []
        if m.get('WhiteListPolicies') is not None:
            for k1 in m.get('WhiteListPolicies'):
                temp_model = main_models.DescribeInstanceAttributeResponseBodyInstanceAttributeWhiteListPolicies()
                self.white_list_policies.append(temp_model.from_map(k1))

        return self

class DescribeInstanceAttributeResponseBodyInstanceAttributeWhiteListPolicies(DaraModel):
    def __init__(
        self,
        description: str = None,
        entry: str = None,
    ):
        self.description = description
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.entry is not None:
            result['Entry'] = self.entry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        return self

class DescribeInstanceAttributeResponseBodyInstanceAttributePorts(DaraModel):
    def __init__(
        self,
        custom_port: int = None,
        standard_port: int = None,
    ):
        # The custom port.
        # 
        # > Only the SSH and RDP ports can be changed. If no custom O\\&M port is specified for the bastion host, the value of StandardPort is returned.
        self.custom_port = custom_port
        # The standard port of the bastion host. Valid values:
        # 
        # *   **SSH**: 60022.
        # *   **RDP**: 63389.
        # *   **HTTPS**: 443.
        self.standard_port = standard_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_port is not None:
            result['CustomPort'] = self.custom_port

        if self.standard_port is not None:
            result['StandardPort'] = self.standard_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPort') is not None:
            self.custom_port = m.get('CustomPort')

        if m.get('StandardPort') is not None:
            self.standard_port = m.get('StandardPort')

        return self

