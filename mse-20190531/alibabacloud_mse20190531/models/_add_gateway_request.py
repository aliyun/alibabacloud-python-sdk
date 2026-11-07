# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class AddGatewayRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        charge_type: str = None,
        clb_network_type: str = None,
        enable_hardware_acceleration: bool = None,
        enable_sls: bool = None,
        enable_xtrace: bool = None,
        enterprise_security_group: bool = None,
        internet_slb_spec: str = None,
        managed_entry_network_type: str = None,
        mser_version: str = None,
        name: str = None,
        nlb_network_type: str = None,
        region: str = None,
        replica: int = None,
        request_pars: str = None,
        resource_group_id: str = None,
        slb_spec: str = None,
        spec: str = None,
        tag: List[main_models.AddGatewayRequestTag] = None,
        v_switch_id: str = None,
        v_switch_id_2: str = None,
        vpc: str = None,
        xtrace_ratio: str = None,
        zone_info: List[main_models.AddGatewayRequestZoneInfo] = None,
    ):
        # The language of the response. Valid values:
        # - zh: Chinese.
        # - en: English.
        self.accept_language = accept_language
        # The billing method. This parameter is specified when you purchase a traditional instance.
        self.charge_type = charge_type
        # The network type of the pay-by-LCU Classic Load Balancer (CLB) to be purchased. Valid values:
        # - pubnet: Internet.
        # - privatenet: Internal network.
        # - privatepubnet: Internet and internal network.
        # 
        # > Traditional instance: When you create a traditional instance, you can purchase only one of the following load balancers: an NLB, a pay-by-LCU CLB, or a pay-by-specification CLB.
        # 
        # > Serverless instance: When you create a Serverless instance, you can purchase only one of the following load balancers: an NLB or a pay-by-LCU CLB.
        self.clb_network_type = clb_network_type
        # Specifies whether to enable hardware acceleration.
        self.enable_hardware_acceleration = enable_hardware_acceleration
        # Specifies whether to enable log delivery to Simple Log Service (SLS).
        self.enable_sls = enable_sls
        # Specifies whether to enable Tracing Analysis.
        self.enable_xtrace = enable_xtrace
        # Specifies whether the security group is an advanced security group.
        self.enterprise_security_group = enterprise_security_group
        # The specifications of the Internet-facing SLB instance. This parameter is applicable to traditional instances. Valid values:
        # - Basic (slb.s1.small)
        # - Standard 1 (slb.s2.small)
        # - Standard I (slb.s2.medium)
        # - Advanced 1 (slb.s3.small)
        # - Advanced I (slb.s3.medium)
        # - Ultra-high I (slb.s3.large)
        # 
        # > Traditional instance: When you create a traditional instance, you can purchase only one of the following load balancers: an NLB, a pay-by-LCU CLB, or a pay-by-specification CLB.
        # 
        # > Serverless instance: When you create a Serverless instance, you can purchase only one of the following load balancers: an NLB or a pay-by-LCU CLB.
        self.internet_slb_spec = internet_slb_spec
        # The gateway ingress type. This parameter is applicable to the Professional Edition of a standard instance. Valid values:
        # - pubnet: Internet.
        # - privatenet: Internal network.
        # - privatepubnet: Internet and internal network.
        self.managed_entry_network_type = managed_entry_network_type
        # The gateway product type. Valid values:
        # - mse_premium: Professional Edition of a standard instance.
        # - mse_pro: Standard Edition of a standard instance.
        # - mse_serverless: Serverless.
        self.mser_version = mser_version
        # The name of the gateway.
        self.name = name
        # The network type of the Network Load Balancer (NLB) to be purchased. Valid values:
        # - pubnet: Internet.
        # - privatenet: Internal network.
        # - privatepubnet: Internet and internal network.
        # 
        # > Traditional instance: When you create a traditional instance, you can purchase only one of the following load balancers: an NLB, a pay-by-LCU Classic Load Balancer (CLB), or a pay-by-specification CLB.
        # 
        # > Serverless instance: When you create a Serverless instance, you can purchase only one of the following load balancers: an NLB or a pay-by-LCU CLB.
        self.nlb_network_type = nlb_network_type
        # The region.
        # 
        # This parameter is required.
        self.region = region
        # The number of nodes. This parameter is specified when you purchase a traditional instance.
        self.replica = replica
        # The extended fields.
        self.request_pars = request_pars
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The specifications of the internal-facing Server Load Balancer (SLB) instance. This parameter is applicable to traditional instances. Valid values:
        # - Basic (slb.s1.small)
        # - Standard 1 (slb.s2.small)
        # - Standard I (slb.s2.medium)
        # - Advanced 1 (slb.s3.small)
        # - Advanced I (slb.s3.medium)
        # - Ultra-high I (slb.s3.large)
        # 
        # > Traditional instance: When you create a traditional instance, you can purchase only one of the following load balancers: an NLB, a pay-by-LCU CLB, or a pay-by-specification CLB.
        # 
        # > Serverless instance: When you create a Serverless instance, you can purchase only one of the following load balancers: an NLB or a pay-by-LCU CLB.
        self.slb_spec = slb_spec
        # The node specifications. This parameter is specified when you purchase a traditional instance. Valid values:
        # - MSE_GTW_16_32_200_c(16C32G)
        # - MSE_GTW_2_4_200_c(2C4G)
        # - MSE_GTW_4_8_200_c(4C8G)
        # - MSE_GTW_8_16_200_c(8C16G)
        self.spec = spec
        # The tags of the gateway.
        self.tag = tag
        # The ID of the primary vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the secondary vSwitch.
        self.v_switch_id_2 = v_switch_id_2
        # The ID of the virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.vpc = vpc
        # The sampling rate for Tracing Analysis. Valid values: 1 to 100.
        self.xtrace_ratio = xtrace_ratio
        # The zone information.
        self.zone_info = zone_info

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.zone_info:
            for v1 in self.zone_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.clb_network_type is not None:
            result['ClbNetworkType'] = self.clb_network_type

        if self.enable_hardware_acceleration is not None:
            result['EnableHardwareAcceleration'] = self.enable_hardware_acceleration

        if self.enable_sls is not None:
            result['EnableSls'] = self.enable_sls

        if self.enable_xtrace is not None:
            result['EnableXtrace'] = self.enable_xtrace

        if self.enterprise_security_group is not None:
            result['EnterpriseSecurityGroup'] = self.enterprise_security_group

        if self.internet_slb_spec is not None:
            result['InternetSlbSpec'] = self.internet_slb_spec

        if self.managed_entry_network_type is not None:
            result['ManagedEntryNetworkType'] = self.managed_entry_network_type

        if self.mser_version is not None:
            result['MserVersion'] = self.mser_version

        if self.name is not None:
            result['Name'] = self.name

        if self.nlb_network_type is not None:
            result['NlbNetworkType'] = self.nlb_network_type

        if self.region is not None:
            result['Region'] = self.region

        if self.replica is not None:
            result['Replica'] = self.replica

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec

        if self.spec is not None:
            result['Spec'] = self.spec

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_id_2 is not None:
            result['VSwitchId2'] = self.v_switch_id_2

        if self.vpc is not None:
            result['Vpc'] = self.vpc

        if self.xtrace_ratio is not None:
            result['XtraceRatio'] = self.xtrace_ratio

        result['ZoneInfo'] = []
        if self.zone_info is not None:
            for k1 in self.zone_info:
                result['ZoneInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClbNetworkType') is not None:
            self.clb_network_type = m.get('ClbNetworkType')

        if m.get('EnableHardwareAcceleration') is not None:
            self.enable_hardware_acceleration = m.get('EnableHardwareAcceleration')

        if m.get('EnableSls') is not None:
            self.enable_sls = m.get('EnableSls')

        if m.get('EnableXtrace') is not None:
            self.enable_xtrace = m.get('EnableXtrace')

        if m.get('EnterpriseSecurityGroup') is not None:
            self.enterprise_security_group = m.get('EnterpriseSecurityGroup')

        if m.get('InternetSlbSpec') is not None:
            self.internet_slb_spec = m.get('InternetSlbSpec')

        if m.get('ManagedEntryNetworkType') is not None:
            self.managed_entry_network_type = m.get('ManagedEntryNetworkType')

        if m.get('MserVersion') is not None:
            self.mser_version = m.get('MserVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NlbNetworkType') is not None:
            self.nlb_network_type = m.get('NlbNetworkType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Replica') is not None:
            self.replica = m.get('Replica')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.AddGatewayRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchId2') is not None:
            self.v_switch_id_2 = m.get('VSwitchId2')

        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')

        if m.get('XtraceRatio') is not None:
            self.xtrace_ratio = m.get('XtraceRatio')

        self.zone_info = []
        if m.get('ZoneInfo') is not None:
            for k1 in m.get('ZoneInfo'):
                temp_model = main_models.AddGatewayRequestZoneInfo()
                self.zone_info.append(temp_model.from_map(k1))

        return self

class AddGatewayRequestZoneInfo(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class AddGatewayRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

