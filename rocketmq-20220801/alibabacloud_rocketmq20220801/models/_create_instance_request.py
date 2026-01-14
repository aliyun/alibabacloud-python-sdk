# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
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
        # Specifies whether to enable auto-renewal for the instance. This parameter takes effect only if you set paymentType to Subscription. Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew
        # The auto-renewal cycle of the instance. This parameter takes effect only if you set autoRenew to true. Unit: months.
        # 
        # Valid values:
        # 
        # *   Monthly renewal: 1, 2, 3, 6, and 12
        self.auto_renew_period = auto_renew_period
        # The commodity code. Valid values:
        # 
        # *   ons_rmqpost_public_intl: pay-as-you-go
        # *   ons_rmqsub_public_intl: subscription
        # *   ons_rmqsrvlesspost_public_intl: serverless instance
        # serverless instance requires this parameter
        self.commodity_code = commodity_code
        # The name of the instance that you want to create.
        # 
        # If you leave this parameter empty, the instance ID is used as the instance name.
        self.instance_name = instance_name
        # The information about the network.
        # 
        # This parameter is required.
        self.network_info = network_info
        # The billing method of the instance. ApsaraMQ for RocketMQ supports the subscription and pay-as-you-go billing methods.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo: This billing method allows you to use resources before you pay for the resources.
        # *   Subscription: This billing method allows you to use resources after you pay for the resources.
        # 
        # For more information, see [Billing methods](https://help.aliyun.com/document_detail/427234.html).
        # 
        # This parameter is required.
        self.payment_type = payment_type
        # The subscription duration of the instance. This parameter takes effect only if you set paymentType to Subscription.
        # 
        # Valid values:
        # 
        # *   Monthly subscription: 1, 2, 3, 4, 5, and 6
        # *   Yearly subscription: 1, 2, and 3
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        self.period_unit = period_unit
        # The information about instance specifications.
        self.product_info = product_info
        # The instance description.
        self.remark = remark
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The primary edition of the instance. For information about the differences among primary edition instances, see [Instance selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        # 
        # >  After you create an instance, you can only upgrade the primary edition of the instance. The following editions are sorted in ascending order: Standard Edition, Professional Edition, Enterprise Platinum Edition. For example, you can upgrade an instance from Standard Edition to Professional Edition, but you cannot downgrade an instance from Professional Edition to Standard Edition.
        # 
        # This parameter is required.
        self.series_code = series_code
        # The code of the service to which the instance belongs. The service code of ApsaraMQ for RocketMQ is rmq.
        # 
        # This parameter is required.
        self.service_code = service_code
        # The sub-category edition of the instance. For information about the differences among sub-category edition instances, see [Instance selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # Valid values:
        # 
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        # *   serverless: serverless
        # 
        # If you set seriesCode to ultimate, you can set this parameter only to cluster_ha.
        # 
        # >  After you create an instance, you cannot change the sub-category edition of the instance.
        # 
        # Valid values:
        # 
        # *   serverless: serverless
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        # 
        # This parameter is required.
        self.sub_series_code = sub_series_code
        # The tags that you want to add to the instance.
        self.tags = tags
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value of this parameter, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token

    def validate(self):
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
        # The `key` of the tag.
        self.key = key
        # The `value` of the tag.
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
        auto_scaling: bool = None,
        capacity_type: str = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        provisioned_capacity: int = None,
        send_receive_ratio: float = None,
        storage_encryption: bool = None,
        storage_secret_key: str = None,
        trace_on: bool = None,
    ):
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # After you enable the elastic TPS feature for an ApsaraMQ for RocketMQ instance, you can use a specific amount of TPS that exceeds the specification limit. You are charged for the elastic TPS feature. For more information, see [Computing fees](https://help.aliyun.com/document_detail/427237.html).
        # 
        # >  The elastic TPS feature is supported only by instances of specific editions. For more information, see [Instance editions](https://help.aliyun.com/document_detail/444715.html).
        self.auto_scaling = auto_scaling
        self.capacity_type = capacity_type
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section of the [Limits](https://help.aliyun.com/document_detail/440347.html) topic.
        # 
        # ApsaraMQ for RocketMQ supports serverless scaling of message storage. You are charged storage fees based on your actual storage usage. You can change the retention period of messages to manage storage capacity. For more information, see [Storage fees](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The computing specification that specifies the messaging transactions per second (TPS) of the instance. For more information, see [Instance editions](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        self.provisioned_capacity = provisioned_capacity
        # The ratio of the message sending TPS to the messaging TPS of the instance.
        # 
        # For example, if the maximum messaging TPS of an instance is 1,000 and the ratio of the message sending TPS to the messaging TPS of the instance is 0.8, the maximum message sending TPS of the instance is 800 and the maximum message receiving TPS is 200.
        # 
        # Valid values: 0 to 1. Default value: 0.5.
        self.send_receive_ratio = send_receive_ratio
        # Specifies whether to enable the encryption at rest feature.
        self.storage_encryption = storage_encryption
        # The key for encryption at rest.
        self.storage_secret_key = storage_secret_key
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling

        if self.capacity_type is not None:
            result['capacityType'] = self.capacity_type

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
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')

        if m.get('capacityType') is not None:
            self.capacity_type = m.get('capacityType')

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
        # The Internet-related configurations.
        # 
        # This parameter is required.
        self.internet_info = internet_info
        # The virtual private cloud (VPC)-related configurations.
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
        # The ID of the security group to which the instance belongs.
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch with which the instance is associated. If you want to specify multiple vSwitches, separate the vSwitches with vertical bars (|).
        # 
        # >  After you create an ApsaraMQ for RocketMQ instance, you cannot change the vSwitch with which the instance is associated. If you want to change the vSwitch with which the instance is associated, you must release the instance and purchase a new instance.
        # 
        # >  We recommend that you configure vSwitches instead of this parameter.
        self.v_switch_id = v_switch_id
        # The vSwitches.
        # 
        # >  After you create an ApsaraMQ for RocketMQ instance, you cannot change the vSwitch with which the instance is associated. If you want to change the vSwitch with which the instance is associated, you must release the instance and purchase a new instance.
        # 
        # >  This parameter is required. We recommend that you configure this parameter instead of vSwitchId.
        self.v_switches = v_switches
        # The ID of the VPC with which the instance to be created is associated.
        # 
        # >  After you create an ApsaraMQ for RocketMQ instance, you cannot change the VPC with which the instance is associated. If you want to change the VPC with which the instance is associated, you must release the instance and create a new instance.
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
        # The ID of the vSwitch with which the instance is associated.
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
        # The Internet bandwidth. Unit: MB/s.
        # 
        # This parameter is required only if you set flowOutType to payByBandwidth.
        # 
        # Valid values: 1 to 1000.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The metering method of Internet usage.
        # 
        # Valid values:
        # 
        # *   payByBandwidth: pay-by-bandwidth. This value is valid only if you enable Internet access.
        # *   payByTraffic: pay-by-traffic. This value is valid only if you enable Internet access.
        # *   uninvolved: No metering method is involved. This value is valid only if you disable Internet access.
        # 
        # This parameter is required.
        self.flow_out_type = flow_out_type
        # Specifies whether to enable the Internet access feature.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, ApsaraMQ for RocketMQ allows you to access instances in VPCs. If you enable Internet access for an instance, you can access the instance over the Internet. After you enable this feature, you are charged for outbound Internet traffic. For more information, see [Internet access fees](https://help.aliyun.com/document_detail/427240.html).
        # 
        # This parameter is required.
        self.internet_spec = internet_spec
        # The whitelist that includes the CIDR blocks that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet. This parameter can be configured only if you use the public endpoint to access the instance.
        # 
        # *   If you do not configure an IP address whitelist, all CIDR blocks are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If you configure an IP address whitelist, only the CIDR blocks in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
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

