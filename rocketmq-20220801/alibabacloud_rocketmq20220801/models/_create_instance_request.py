# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        acl_info: main_models.CreateInstanceRequestAclInfo = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        commodity_code: str = None,
        instance_name: str = None,
        network_info: main_models.CreateInstanceRequestNetworkInfo = None,
        payment_type: str = None,
        period: int = None,
        period_unit: str = None,
        product_info: main_models.CreateInstanceRequestProductInfo = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        sub_series_code: str = None,
        tags: List[main_models.CreateInstanceRequestTags] = None,
        client_token: str = None,
    ):
        # The access control information.
        self.acl_info = acl_info
        # Specifies whether to enable auto-renewal. This parameter takes effect only when the billing method of the instance is set to Subscription.
        self.auto_renew = auto_renew
        # The Unified Auto Renewal Cycle. This parameter takes effect only when auto-renewal is enabled. Unit: months.
        # 
        # Valid values:
        # 
        # - Monthly renewal: 1, 2, 3, 6, 12
        self.auto_renew_period = auto_renew_period
        # The commodity code.
        # 
        # <props="china">- ons_rmqsub_public_cn: subscription instance.
        # 
        # <props="china">- ons_rmqpost_public_cn: pay-as-you-go instance.
        # 
        # <props="china">- ons_rmqsrvlesspost_public_cn: serverless instance.
        # 
        # <props="intl">- ons_rmqpost_public_intl: pay-as-you-go.
        # 
        # <props="intl">- ons_rmqsub_public_intl: subscription.
        # <props="intl">- ons_rmqsrvlesspost_public_intl: serverless instance.
        # This parameter is required for serverless instances.
        self.commodity_code = commodity_code
        # The name of the instance to be created.
        # 
        # If you do not specify this parameter, the instance ID is used as the instance name.
        self.instance_name = instance_name
        # The network configuration information.
        # 
        # This parameter is required.
        self.network_info = network_info
        # The billing method of the instance. ApsaraMQ for RocketMQ supports subscription and pay-as-you-go billing methods.
        # 
        # For more information, see [Billable methods](https://help.aliyun.com/document_detail/427234.html).
        # 
        # This parameter is required.
        self.payment_type = payment_type
        # The subscription duration. This parameter takes effect only when the billing method of the instance is set to Subscription.
        # 
        # Valid values:
        # 
        # - Monthly subscription: 1, 2, 3, 4, 5, 6
        # 
        # - Yearly subscription: 1, 2, 3
        self.period = period
        # The minimum epoch unit of the subscription duration.
        self.period_unit = period_unit
        # The instance specification information.
        self.product_info = product_info
        # The remarks of the instance.
        self.remark = remark
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The primary series encoding of the instance. For more information about the differences between primary series, see [Product selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # This parameter is required.
        self.series_code = series_code
        # The service encoding of the instance. The service encoding for MSMQ for RocketMQ is rmq.
        # 
        # This parameter is required.
        self.service_code = service_code
        # The sub-series encoding of the instance. For more information about the differences between sub-series, see [Product selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # If the primary series is set to ultimate (Platinum Edition), the sub-series can only be set to cluster_ha (Cluster High Availability Edition).
        # >Notice: After the instance is created, the sub-series cannot be changed.
        # 
        # This parameter is required.
        self.sub_series_code = sub_series_code
        # The list of resource tags.
        self.tags = tags
        # The client token that is used to ensure the idempotence of the request. The client generates the value of this parameter, which must be unique among different requests. The token can be up to 64 ASCII characters in length.
        self.client_token = client_token

    def validate(self):
        if self.acl_info:
            self.acl_info.validate()
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_info is not None:
            result['aclInfo'] = self.acl_info.to_map()

        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.period is not None:
            result['period'] = self.period

        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit

        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()

        if self.remark is not None:
            result['remark'] = self.remark

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.series_code is not None:
            result['seriesCode'] = self.series_code

        if self.service_code is not None:
            result['serviceCode'] = self.service_code

        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclInfo') is not None:
            temp_model = main_models.CreateInstanceRequestAclInfo()
            self.acl_info = temp_model.from_map(m.get('aclInfo'))

        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('networkInfo') is not None:
            temp_model = main_models.CreateInstanceRequestNetworkInfo()
            self.network_info = temp_model.from_map(m.get('networkInfo'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')

        if m.get('productInfo') is not None:
            temp_model = main_models.CreateInstanceRequestProductInfo()
            self.product_info = temp_model.from_map(m.get('productInfo'))

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')

        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')

        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateInstanceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the resource tag.
        self.key = key
        # The value of the resource tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreateInstanceRequestProductInfo(DaraModel):
    def __init__(
        self,
        adaptive_elasticity: bool = None,
        auto_scaling: bool = None,
        capacity_type: str = None,
        dr_replication_mode: str = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        provisioned_capacity: int = None,
        send_receive_ratio: float = None,
        storage_encryption: bool = None,
        storage_secret_key: str = None,
        trace_on: bool = None,
    ):
        # Specifies whether to enable adaptive elasticity. A value of true indicates that adaptive elasticity is enabled. A value of false indicates that adaptive elasticity is shutdown.
        self.adaptive_elasticity = adaptive_elasticity
        # Specifies whether to enable burstable elastic capacity beyond the specification.
        # 
        # After burstable elastic capacity is enabled, MSMQ for RocketMQ allows the instance to exceed the TPS limit of the base specification within a certain range. The portion that exceeds the base specification incurs additional elastic specification fees. For more information about billing, see [Computing fees](https://help.aliyun.com/document_detail/427237.html).
        # 
        # 
        # > Only instances of certain specifications support burstable elastic capacity. For more information about supported instances, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.auto_scaling = auto_scaling
        # The capacity pattern.
        self.capacity_type = capacity_type
        # The cross-region replication pattern.
        self.dr_replication_mode = dr_replication_mode
        # The message retention period. Unit: hours.
        # 
        # For the valid value range, see [Limits](https://help.aliyun.com/document_detail/440347.html) > Resource Quotas > Message Retention Period.
        # 
        # The log broker in MSMQ for RocketMQ is fully serverless and elastic. Fees are charged based on the actual storage space used. You can control the storage capacity by adjusting the message retention period. For more information, see [Storage fees](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The message sending and receiving computing specification. For more information about the TPS upper limit for message sending and receiving, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        # The provisioned capacity.
        self.provisioned_capacity = provisioned_capacity
        # The ratio of message sending TPS to the total message sending and accepting TPS of the instance.
        # 
        # For example, if the TPS upper limit for message sending and accepting of the instance is 1000 per second and the message sending ratio is 0.8, the TPS upper limit for message sending is 800 per second and the TPS upper limit for message accepting is 200 per second.
        # 
        # Valid values: [0.05, 0.95]. Default value: 0.5.
        self.send_receive_ratio = send_receive_ratio
        # Indicates whether storage encryption is enabled.
        self.storage_encryption = storage_encryption
        # The key for storage encryption.
        self.storage_secret_key = storage_secret_key
        # Specifies whether to enable the message trace feature.
        # 
        # true: Enable the message trace feature.
        # false: Shutdown the message trace feature.
        # This parameter takes effect only for Serverless instances. If the message trace feature is enabled, message trace fees are incurred. For more information about billing, see the Serverless billing description. For pay-as-you-go and subscription instances, this parameter does not take effect. The message trace feature is supported by default regardless of whether this parameter is enabled.
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptive_elasticity is not None:
            result['adaptiveElasticity'] = self.adaptive_elasticity

        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling

        if self.capacity_type is not None:
            result['capacityType'] = self.capacity_type

        if self.dr_replication_mode is not None:
            result['drReplicationMode'] = self.dr_replication_mode

        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time

        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec

        if self.provisioned_capacity is not None:
            result['provisionedCapacity'] = self.provisioned_capacity

        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio

        if self.storage_encryption is not None:
            result['storageEncryption'] = self.storage_encryption

        if self.storage_secret_key is not None:
            result['storageSecretKey'] = self.storage_secret_key

        if self.trace_on is not None:
            result['traceOn'] = self.trace_on

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adaptiveElasticity') is not None:
            self.adaptive_elasticity = m.get('adaptiveElasticity')

        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')

        if m.get('capacityType') is not None:
            self.capacity_type = m.get('capacityType')

        if m.get('drReplicationMode') is not None:
            self.dr_replication_mode = m.get('drReplicationMode')

        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')

        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')

        if m.get('provisionedCapacity') is not None:
            self.provisioned_capacity = m.get('provisionedCapacity')

        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')

        if m.get('storageEncryption') is not None:
            self.storage_encryption = m.get('storageEncryption')

        if m.get('storageSecretKey') is not None:
            self.storage_secret_key = m.get('storageSecretKey')

        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')

        return self

class CreateInstanceRequestNetworkInfo(DaraModel):
    def __init__(
        self,
        internet_info: main_models.CreateInstanceRequestNetworkInfoInternetInfo = None,
        vpc_info: main_models.CreateInstanceRequestNetworkInfoVpcInfo = None,
    ):
        # The Internet configuration information.
        # 
        # This parameter is required.
        self.internet_info = internet_info
        # The VPC configuration information.
        # 
        # This parameter is required.
        self.vpc_info = vpc_info

    def validate(self):
        if self.internet_info:
            self.internet_info.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()

        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internetInfo') is not None:
            temp_model = main_models.CreateInstanceRequestNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m.get('internetInfo'))

        if m.get('vpcInfo') is not None:
            temp_model = main_models.CreateInstanceRequestNetworkInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m.get('vpcInfo'))

        return self

class CreateInstanceRequestNetworkInfoVpcInfo(DaraModel):
    def __init__(
        self,
        security_group_ids: str = None,
        v_switch_id: str = None,
        v_switches: List[main_models.CreateInstanceRequestNetworkInfoVpcInfoVSwitches] = None,
        vpc_id: str = None,
    ):
        # The security group ID.
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch associated with the instance. If multiple vSwitches exist, separate them with vertical bars (|).
        # 
        # > After an ApsaraMQ for RocketMQ instance is created, the selected vSwitch cannot be changed. To modify the associated vSwitch, release the existing ApsaraMQ for RocketMQ instance and purchase a new one.
        # 
        # <notice>This field is not recommended. Use the vSwitches field instead.</notice>
        self.v_switch_id = v_switch_id
        # The list of vSwitches.
        # 
        # > After an ApsaraMQ for RocketMQ instance is created, the selected vSwitch cannot be changed. To modify the associated vSwitch, release the existing ApsaraMQ for RocketMQ instance and purchase a new one.
        # 
        # <notice>This is a required field. Because the vSwitchId field is no longer recommended, use this field to configure vSwitches.</notice>
        self.v_switches = v_switches
        # The ID of the VPC to associate with the instance.
        # 
        # > After an ApsaraMQ for RocketMQ instance is created, the selected VPC cannot be changed. To modify the associated VPC, release the existing ApsaraMQ for RocketMQ instance and purchase a new one.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        result['vSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['vSwitches'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        self.v_switches = []
        if m.get('vSwitches') is not None:
            for k1 in m.get('vSwitches'):
                temp_model = main_models.CreateInstanceRequestNetworkInfoVpcInfoVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class CreateInstanceRequestNetworkInfoVpcInfoVSwitches(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
    ):
        # The ID of the vSwitch associated with the instance.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        return self

class CreateInstanceRequestNetworkInfoInternetInfo(DaraModel):
    def __init__(
        self,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        ip_whitelist: List[str] = None,
    ):
        # The Internet bandwidth specification. Unit: Mb/s.
        # 
        # This parameter is required only when the Internet billing type is set to fixed bandwidth billing.
        # 
        # Valid values: 1 to 1000.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The Internet billing type.
        # 
        # This parameter is required.
        self.flow_out_type = flow_out_type
        # Specifies whether to enable public network access.
        # 
        # By default, instances support VPC access. If you enable public network access, ApsaraMQ for RocketMQ charges fees for public network downstream bandwidth. For more information about billing, see [Public network access fees](https://help.aliyun.com/document_detail/427240.html).
        # 
        # This parameter is required.
        self.internet_spec = internet_spec
        # The public network access IP whitelist. Only public endpoints support IP whitelist configuration. VPC endpoints do not support this feature.
        # 
        # - If no IP whitelist is configured, all IP address ranges are allowed to access the ApsaraMQ for RocketMQ server over the Internet by default.
        # - If an IP whitelist is configured, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ server over the Internet.
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth

        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type

        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec

        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')

        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')

        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')

        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')

        return self

class CreateInstanceRequestAclInfo(DaraModel):
    def __init__(
        self,
        default_vpc_auth_free: bool = None,
    ):
        # Specifies whether to enable authentication-free access for VPC endpoints when the intelligent identity recognition type is used. Valid values:
        # - true: Enable authentication-free access.
        # - false: Disable authentication-free access.
        self.default_vpc_auth_free = default_vpc_auth_free

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_vpc_auth_free is not None:
            result['defaultVpcAuthFree'] = self.default_vpc_auth_free

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultVpcAuthFree') is not None:
            self.default_vpc_auth_free = m.get('defaultVpcAuthFree')

        return self

