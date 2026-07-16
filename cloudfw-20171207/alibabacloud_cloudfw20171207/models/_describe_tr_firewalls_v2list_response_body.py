# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeTrFirewallsV2ListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: str = None,
        vpc_tr_firewalls: List[main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The list of VPC firewalls.
        self.vpc_tr_firewalls = vpc_tr_firewalls

    def validate(self):
        if self.vpc_tr_firewalls:
            for v1 in self.vpc_tr_firewalls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VpcTrFirewalls'] = []
        if self.vpc_tr_firewalls is not None:
            for k1 in self.vpc_tr_firewalls:
                result['VpcTrFirewalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vpc_tr_firewalls = []
        if m.get('VpcTrFirewalls') is not None:
            for k1 in m.get('VpcTrFirewalls'):
                temp_model = main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls()
                self.vpc_tr_firewalls.append(temp_model.from_map(k1))

        return self

class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls(DaraModel):
    def __init__(
        self,
        acl_config: main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsAclConfig = None,
        cen_id: str = None,
        cen_name: str = None,
        cloud_firewall_vpc_order_type: str = None,
        firewall_id: str = None,
        firewall_switch_status: str = None,
        ips_config: main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig = None,
        owner_id: int = None,
        precheck_status: str = None,
        protected_resource: main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource = None,
        region_no: str = None,
        region_status: str = None,
        result_code: str = None,
        route_mode: str = None,
        transit_router_id: str = None,
        unprotected_resource: main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource = None,
        vpc_firewall_name: str = None,
    ):
        # The mode of the access control list (ACL) engine.
        self.acl_config = acl_config
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The name of the CEN instance.
        self.cen_name = cen_name
        # The payer for the transit router (TR) instance that is created for the VPC firewall. Valid values:
        # 
        # - **PayByCloudFirewall**: Cloud Firewall
        # 
        # - **PayByCenOwner**: The account that owns the CEN instance
        self.cloud_firewall_vpc_order_type = cloud_firewall_vpc_order_type
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The status of the VPC firewall. Valid values:
        # 
        # - **opened**: Enabled
        # 
        # - **closed**: Disabled
        # 
        # - **notconfigured**: The VPC firewall is not configured.
        # 
        # - **configured**: The VPC firewall is configured.
        # 
        # - **creating**: The VPC firewall is being created.
        # 
        # - **opening**: The VPC firewall is being enabled.
        # 
        # - **deleting**: The VPC firewall is being deleted.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The configurations of the intrusion prevention system (IPS).
        self.ips_config = ips_config
        # The ID of the Alibaba Cloud account that owns the VPC.
        self.owner_id = owner_id
        # Indicates whether the VPC firewall can be automatically created. Valid values:
        # 
        # - **passed**: The VPC firewall can be automatically created.
        # 
        # - **failed**: The VPC firewall cannot be automatically created.
        # 
        # - **unknown**: The status is unknown.
        self.precheck_status = precheck_status
        # The list of protected resources.
        self.protected_resource = protected_resource
        # The region ID of the transit router instance.
        self.region_no = region_no
        # The status of the region. Valid values:
        # 
        # - **enable**: The VPC firewall is available in the region.
        # 
        # - **disable**: The VPC firewall is not available in the region.
        self.region_status = region_status
        # The result code of the operation to create the VPC firewall. Valid values:
        # 
        # - **RegionDisable**: The VPC firewall is not supported in the region where the network instance resides. The VPC firewall cannot be created.
        # 
        # - An empty string: The VPC firewall can be created for the network instance.
        self.result_code = result_code
        # The routing mode. Valid values:
        # 
        # - **managed**: automatic mode
        # 
        # - **manual**: manual mode
        self.route_mode = route_mode
        # The instance ID of the transit router.
        self.transit_router_id = transit_router_id
        # The list of unprotected resources.
        self.unprotected_resource = unprotected_resource
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.acl_config:
            self.acl_config.validate()
        if self.ips_config:
            self.ips_config.validate()
        if self.protected_resource:
            self.protected_resource.validate()
        if self.unprotected_resource:
            self.unprotected_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_config is not None:
            result['AclConfig'] = self.acl_config.to_map()

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_name is not None:
            result['CenName'] = self.cen_name

        if self.cloud_firewall_vpc_order_type is not None:
            result['CloudFirewallVpcOrderType'] = self.cloud_firewall_vpc_order_type

        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status

        if self.ips_config is not None:
            result['IpsConfig'] = self.ips_config.to_map()

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status

        if self.protected_resource is not None:
            result['ProtectedResource'] = self.protected_resource.to_map()

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.region_status is not None:
            result['RegionStatus'] = self.region_status

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.unprotected_resource is not None:
            result['UnprotectedResource'] = self.unprotected_resource.to_map()

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclConfig') is not None:
            temp_model = main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsAclConfig()
            self.acl_config = temp_model.from_map(m.get('AclConfig'))

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')

        if m.get('CloudFirewallVpcOrderType') is not None:
            self.cloud_firewall_vpc_order_type = m.get('CloudFirewallVpcOrderType')

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('IpsConfig') is not None:
            temp_model = main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m.get('IpsConfig'))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrecheckStatus') is not None:
            self.precheck_status = m.get('PrecheckStatus')

        if m.get('ProtectedResource') is not None:
            temp_model = main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource()
            self.protected_resource = temp_model.from_map(m.get('ProtectedResource'))

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('UnprotectedResource') is not None:
            temp_model = main_models.DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource()
            self.unprotected_resource = temp_model.from_map(m.get('UnprotectedResource'))

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource(DaraModel):
    def __init__(
        self,
        count: int = None,
        ecr_list: List[str] = None,
        peer_tr_list: List[str] = None,
        vbr_list: List[str] = None,
        vpc_list: List[str] = None,
        vpn_list: List[str] = None,
    ):
        # The number of unprotected resources.
        self.count = count
        # The list of unprotected Express Connect Router (ECR) instances.
        self.ecr_list = ecr_list
        # The list of unprotected peer transit routers.
        self.peer_tr_list = peer_tr_list
        # The list of unprotected virtual border routers (VBRs).
        self.vbr_list = vbr_list
        # The list of unprotected VPCs.
        self.vpc_list = vpc_list
        # The list of unprotected VPN gateways.
        self.vpn_list = vpn_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.ecr_list is not None:
            result['EcrList'] = self.ecr_list

        if self.peer_tr_list is not None:
            result['PeerTrList'] = self.peer_tr_list

        if self.vbr_list is not None:
            result['VbrList'] = self.vbr_list

        if self.vpc_list is not None:
            result['VpcList'] = self.vpc_list

        if self.vpn_list is not None:
            result['VpnList'] = self.vpn_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('EcrList') is not None:
            self.ecr_list = m.get('EcrList')

        if m.get('PeerTrList') is not None:
            self.peer_tr_list = m.get('PeerTrList')

        if m.get('VbrList') is not None:
            self.vbr_list = m.get('VbrList')

        if m.get('VpcList') is not None:
            self.vpc_list = m.get('VpcList')

        if m.get('VpnList') is not None:
            self.vpn_list = m.get('VpnList')

        return self

class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource(DaraModel):
    def __init__(
        self,
        count: int = None,
        ecr_list: List[str] = None,
        peer_tr_list: List[str] = None,
        vbr_list: List[str] = None,
        vpc_list: List[str] = None,
        vpn_list: List[str] = None,
    ):
        # The number of protected resources.
        self.count = count
        # The list of protected Express Connect Router (ECR) instances.
        self.ecr_list = ecr_list
        # The list of protected peer transit routers.
        self.peer_tr_list = peer_tr_list
        # The list of protected virtual border routers (VBRs).
        self.vbr_list = vbr_list
        # The list of protected VPCs.
        self.vpc_list = vpc_list
        # The list of protected VPN gateways.
        self.vpn_list = vpn_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.ecr_list is not None:
            result['EcrList'] = self.ecr_list

        if self.peer_tr_list is not None:
            result['PeerTrList'] = self.peer_tr_list

        if self.vbr_list is not None:
            result['VbrList'] = self.vbr_list

        if self.vpc_list is not None:
            result['VpcList'] = self.vpc_list

        if self.vpn_list is not None:
            result['VpnList'] = self.vpn_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('EcrList') is not None:
            self.ecr_list = m.get('EcrList')

        if m.get('PeerTrList') is not None:
            self.peer_tr_list = m.get('PeerTrList')

        if m.get('VbrList') is not None:
            self.vbr_list = m.get('VbrList')

        if m.get('VpcList') is not None:
            self.vpc_list = m.get('VpcList')

        if m.get('VpnList') is not None:
            self.vpn_list = m.get('VpnList')

        return self

class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig(DaraModel):
    def __init__(
        self,
        basic_rules: int = None,
        enable_all_patch: int = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Indicates whether to enable the basic protection feature. Valid values:
        # 
        # - **1**: enabled
        # 
        # - **0**: disabled
        self.basic_rules = basic_rules
        # Indicates whether to enable virtual patching. Valid values:
        # 
        # - **1**: enabled
        # 
        # - **0**: disabled
        self.enable_all_patch = enable_all_patch
        # The IPS rule group. Valid values:
        # 
        # - **1**: loose
        # 
        # - **2**: medium
        # 
        # - **3**: strict
        self.rule_class = rule_class
        # The IPS mode. Valid values:
        # 
        # - **1**: block mode
        # 
        # - **0**: monitor mode
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules

        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')

        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        return self

class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsAclConfig(DaraModel):
    def __init__(
        self,
        strict_mode: int = None,
    ):
        # Indicates whether the strict mode is enabled.
        # 
        # - 1: enabled
        # 
        # - 0: disabled
        self.strict_mode = strict_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        return self

