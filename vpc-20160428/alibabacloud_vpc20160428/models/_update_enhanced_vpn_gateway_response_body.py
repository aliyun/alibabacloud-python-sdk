# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class UpdateEnhancedVpnGatewayResponseBody(DaraModel):
    def __init__(
        self,
        auto_propagate: bool = None,
        create_time: int = None,
        description: str = None,
        disaster_recovery_vswitch_id: str = None,
        enable_bgp: bool = None,
        eni_instance_ids: main_models.UpdateEnhancedVpnGatewayResponseBodyEniInstanceIds = None,
        gateway_type: str = None,
        name: str = None,
        network_type: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: str = None,
        tags: main_models.UpdateEnhancedVpnGatewayResponseBodyTags = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpn_gateway_id: str = None,
        vpn_type: str = None,
    ):
        # Indicates whether BGP route automatic propagation to the VPC is enabled. Valid values:
        # - **true**: Automatic propagation is enabled.
        # 
        # - **false**: Automatic propagation is not enabled.
        self.auto_propagate = auto_propagate
        # The timestamp when the enhanced VPN gateway instance was created. Unit: milliseconds.<br>
        # The timestamp follows the UNIX time format, which represents the total number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the enhanced VPN gateway instance.
        self.description = description
        # The ID of the second vSwitch associated with the enhanced VPN gateway instance.
        self.disaster_recovery_vswitch_id = disaster_recovery_vswitch_id
        # The enabling status of the BGP feature for the enhanced VPN gateway. Valid values:<br>
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.enable_bgp = enable_bgp
        self.eni_instance_ids = eni_instance_ids
        # The type of the enhanced VPN gateway. Valid values:
        # 
        # - **Enhanced.SiteToSite**: enhanced site-to-cloud VPN that supports only IPsec functionality.
        self.gateway_type = gateway_type
        # The name of the enhanced VPN gateway instance.
        self.name = name
        # The network type of the enhanced VPN gateway. Valid values:
        # - **public** (default): public VPN gateway.
        self.network_type = network_type
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the enhanced VPN gateway instance belongs.<br>
        # You can call [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) to query resource group information.
        self.resource_group_id = resource_group_id
        # The status of the enhanced VPN gateway.
        # - **init**: initializing.
        # - **provisioning**: preparing.
        # - **active**: normal.
        # - **updating**: updating.
        # - **deleting**: deleting.
        self.status = status
        # The list of features supported by the enhanced VPN gateway.
        self.tag = tag
        self.tags = tags
        # The ID of the vSwitch associated with the enhanced VPN gateway instance.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the enhanced VPN gateway instance belongs.
        self.vpc_id = vpc_id
        # The ID of the enhanced VPN gateway instance.
        self.vpn_gateway_id = vpn_gateway_id
        # The type of the enhanced VPN gateway.
        # 
        # - **Normal** (default): standard.
        self.vpn_type = vpn_type

    def validate(self):
        if self.eni_instance_ids:
            self.eni_instance_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_propagate is not None:
            result['AutoPropagate'] = self.auto_propagate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.disaster_recovery_vswitch_id is not None:
            result['DisasterRecoveryVSwitchId'] = self.disaster_recovery_vswitch_id

        if self.enable_bgp is not None:
            result['EnableBgp'] = self.enable_bgp

        if self.eni_instance_ids is not None:
            result['EniInstanceIds'] = self.eni_instance_ids.to_map()

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        if self.vpn_type is not None:
            result['VpnType'] = self.vpn_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPropagate') is not None:
            self.auto_propagate = m.get('AutoPropagate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisasterRecoveryVSwitchId') is not None:
            self.disaster_recovery_vswitch_id = m.get('DisasterRecoveryVSwitchId')

        if m.get('EnableBgp') is not None:
            self.enable_bgp = m.get('EnableBgp')

        if m.get('EniInstanceIds') is not None:
            temp_model = main_models.UpdateEnhancedVpnGatewayResponseBodyEniInstanceIds()
            self.eni_instance_ids = temp_model.from_map(m.get('EniInstanceIds'))

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Tags') is not None:
            temp_model = main_models.UpdateEnhancedVpnGatewayResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        if m.get('VpnType') is not None:
            self.vpn_type = m.get('VpnType')

        return self

class UpdateEnhancedVpnGatewayResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.UpdateEnhancedVpnGatewayResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.UpdateEnhancedVpnGatewayResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class UpdateEnhancedVpnGatewayResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class UpdateEnhancedVpnGatewayResponseBodyEniInstanceIds(DaraModel):
    def __init__(
        self,
        eni_instance_id: List[str] = None,
    ):
        self.eni_instance_id = eni_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')

        return self

