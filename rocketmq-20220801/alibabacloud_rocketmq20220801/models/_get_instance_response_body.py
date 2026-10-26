# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInstanceResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The response result.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID. Each request has a unique ID, which you can use to troubleshoot and locate issues.
        self.request_id = request_id
        # Indicates whether the operation was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        account_info: main_models.GetInstanceResponseBodyDataAccountInfo = None,
        acl_info: main_models.GetInstanceResponseBodyDataAclInfo = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        bid: str = None,
        commodity_code: str = None,
        create_time: str = None,
        expire_time: str = None,
        ext_config: main_models.GetInstanceResponseBodyDataExtConfig = None,
        group_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_quotas: List[main_models.GetInstanceResponseBodyDataInstanceQuotas] = None,
        network_info: main_models.GetInstanceResponseBodyDataNetworkInfo = None,
        payment_type: str = None,
        product_info: main_models.GetInstanceResponseBodyDataProductInfo = None,
        region_id: str = None,
        release_time: str = None,
        remark: str = None,
        resource_group_id: str = None,
        series_code: str = None,
        service_code: str = None,
        software: main_models.GetInstanceResponseBodyDataSoftware = None,
        start_time: str = None,
        status: str = None,
        sub_series_code: str = None,
        tags: List[main_models.GetInstanceResponseBodyDataTags] = None,
        topic_count: int = None,
        update_time: str = None,
        user_id: str = None,
    ):
        # The account information.
        self.account_info = account_info
        # The access control information.
        self.acl_info = acl_info
        # Indicates whether auto-renewal is enabled.
        self.auto_renew = auto_renew
        # Indicates whether auto-renewal is enabled.
        self.auto_renew_period = auto_renew_period
        # The BID of the sales channel for the commodity.
        self.bid = bid
        # The commodity code of an MSMQ for RocketMQ 5.x series instance, such as ons_rmqsub_public_cn.
        self.commodity_code = commodity_code
        # The time when the instance was created. The value is in the YYYY-MM-DD HH:mm:ss format.
        self.create_time = create_time
        # The time when the instance expires. The format is YYYY-MM-DD HH:mm:ss.
        self.expire_time = expire_time
        # **[Deprecated]** The extended configuration. This field is no longer recommended. Use the productInfo, internetInfo, and aclInfo fields instead.
        self.ext_config = ext_config
        # The number of consumer groups.
        self.group_count = group_count
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The capacity information.
        self.instance_quotas = instance_quotas
        # The network information.
        self.network_info = network_info
        # The payment type of the instance.
        self.payment_type = payment_type
        # The extended configuration of the instance.
        self.product_info = product_info
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The time when the instance was released. The format is YYYY-MM-DD HH:mm:ss.
        self.release_time = release_time
        # The remarks for the instance.
        self.remark = remark
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The primary series code of the instance. For differences between primary series, see [Product selection](https://help.aliyun.com/document_detail/444722.html).
        self.series_code = series_code
        # The service code of the instance. The service code for MSMQ for RocketMQ is rmq.
        self.service_code = service_code
        # The instance software information.
        self.software = software
        # The time when the instance was started. The format is YYYY-MM-DD HH:mm:ss.
        self.start_time = start_time
        # The instance status.
        self.status = status
        # The sub-series code of the instance. For differences between sub-series, see [Product selection](https://help.aliyun.com/document_detail/444722.html).
        self.sub_series_code = sub_series_code
        # The resource tags.
        self.tags = tags
        # The number of topics.
        self.topic_count = topic_count
        # The time when the instance was last modified. The value is in the YYYY-MM-DD HH:mm:ss format.
        self.update_time = update_time
        # The ID of the user to whom the instance belongs.
        self.user_id = user_id

    def validate(self):
        if self.account_info:
            self.account_info.validate()
        if self.acl_info:
            self.acl_info.validate()
        if self.ext_config:
            self.ext_config.validate()
        if self.instance_quotas:
            for v1 in self.instance_quotas:
                 if v1:
                    v1.validate()
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()
        if self.software:
            self.software.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_info is not None:
            result['accountInfo'] = self.account_info.to_map()

        if self.acl_info is not None:
            result['aclInfo'] = self.acl_info.to_map()

        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period

        if self.bid is not None:
            result['bid'] = self.bid

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.ext_config is not None:
            result['extConfig'] = self.ext_config.to_map()

        if self.group_count is not None:
            result['groupCount'] = self.group_count

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        result['instanceQuotas'] = []
        if self.instance_quotas is not None:
            for k1 in self.instance_quotas:
                result['instanceQuotas'].append(k1.to_map() if k1 else None)

        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.release_time is not None:
            result['releaseTime'] = self.release_time

        if self.remark is not None:
            result['remark'] = self.remark

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.series_code is not None:
            result['seriesCode'] = self.series_code

        if self.service_code is not None:
            result['serviceCode'] = self.service_code

        if self.software is not None:
            result['software'] = self.software.to_map()

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.topic_count is not None:
            result['topicCount'] = self.topic_count

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountInfo') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataAccountInfo()
            self.account_info = temp_model.from_map(m.get('accountInfo'))

        if m.get('aclInfo') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataAclInfo()
            self.acl_info = temp_model.from_map(m.get('aclInfo'))

        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')

        if m.get('bid') is not None:
            self.bid = m.get('bid')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('extConfig') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataExtConfig()
            self.ext_config = temp_model.from_map(m.get('extConfig'))

        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        self.instance_quotas = []
        if m.get('instanceQuotas') is not None:
            for k1 in m.get('instanceQuotas'):
                temp_model = main_models.GetInstanceResponseBodyDataInstanceQuotas()
                self.instance_quotas.append(temp_model.from_map(k1))

        if m.get('networkInfo') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataNetworkInfo()
            self.network_info = temp_model.from_map(m.get('networkInfo'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('productInfo') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataProductInfo()
            self.product_info = temp_model.from_map(m.get('productInfo'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')

        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')

        if m.get('software') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataSoftware()
            self.software = temp_model.from_map(m.get('software'))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetInstanceResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class GetInstanceResponseBodyDataTags(DaraModel):
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

class GetInstanceResponseBodyDataSoftware(DaraModel):
    def __init__(
        self,
        maintain_time: str = None,
        software_version: str = None,
        upgrade_method: str = None,
    ):
        # The upgrade time window, in the format of HH:mm-HH:mm.
        self.maintain_time = maintain_time
        # The software version.
        self.software_version = software_version
        # The upgrade method.
        self.upgrade_method = upgrade_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maintain_time is not None:
            result['maintainTime'] = self.maintain_time

        if self.software_version is not None:
            result['softwareVersion'] = self.software_version

        if self.upgrade_method is not None:
            result['upgradeMethod'] = self.upgrade_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maintainTime') is not None:
            self.maintain_time = m.get('maintainTime')

        if m.get('softwareVersion') is not None:
            self.software_version = m.get('softwareVersion')

        if m.get('upgradeMethod') is not None:
            self.upgrade_method = m.get('upgradeMethod')

        return self

class GetInstanceResponseBodyDataProductInfo(DaraModel):
    def __init__(
        self,
        adaptive_elasticity: bool = None,
        auto_scaling: bool = None,
        capacity_type: str = None,
        dr_replication_mode: str = None,
        max_delay_time: int = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        provisioned_capacity: int = None,
        send_receive_ratio: float = None,
        storage_encryption: bool = None,
        storage_secret_key: str = None,
        support_auto_scaling: bool = None,
        trace_on: bool = None,
    ):
        # The adaptive elasticity.
        self.adaptive_elasticity = adaptive_elasticity
        # Indicates whether burstable elastic capacity beyond the base specification is enabled for seamless scaling.
        # 
        # This parameter takes effect only when the value of supportAutoScaling is enable, which means the instance supports enabling elastic capacity.
        self.auto_scaling = auto_scaling
        # The capacity mode.
        self.capacity_type = capacity_type
        # The cross-region replication mode.
        self.dr_replication_mode = dr_replication_mode
        # The maximum interval for scheduled messages. Unit: seconds.
        self.max_delay_time = max_delay_time
        # The message retention period. Unit: hours.
        # 
        # For the value range, see [Limits](https://help.aliyun.com/document_detail/440347.html) > Resource Quotas > Message retention period.
        # 
        # The message storage of ApsaraMQ for RocketMQ is fully serverless and elastic. You are charged based on the actual storage space used. You can control the storage capacity by adjusting the message retention period. For more information, see [Storage fees](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The message processing specification. For the TPS upper limit of message sending and receiving, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        # The provisioned capacity.
        self.provisioned_capacity = provisioned_capacity
        # The ratio of message sending to message receiving.
        self.send_receive_ratio = send_receive_ratio
        # Indicates whether storage encryption is enabled.
        self.storage_encryption = storage_encryption
        # The storage encryption key.
        self.storage_secret_key = storage_secret_key
        # Indicates whether the burstable elastic capability beyond the base specification is enabled.
        # 
        # 
        # After the burstable elastic capability is enabled, ApsaraMQ for RocketMQ allows the instance to exceed the TPS limit of the base specification within a certain range. Additional elastic specification fees are charged for the portion that exceeds the base specification. For more information about billing, see [Computing capability fees](https://help.aliyun.com/document_detail/427237.html).
        # 
        # 
        # > Only instances of specific specifications support the burstable elastic capability. For more information about supported instances, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.support_auto_scaling = support_auto_scaling
        # Indicates whether the message trace feature is enabled.
        # - true: The message trace feature is enabled.
        # - false: The message trace feature is disabled.
        # 
        # <props="intl">This parameter does not take effect. Instances support the message trace feature by default regardless of whether this parameter is enabled.
        # <props="china">This parameter takes effect only for Serverless instances. If the message trace feature is enabled, message trace fees are incurred. For more information about billing, see [Serverless billing](https://help.aliyun.com/document_detail/2586280.html).
        # 
        # <props="china">For pay-as-you-go and subscription instances, this parameter does not take effect. The message trace feature is supported by default regardless of whether this parameter is enabled.
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

        if self.max_delay_time is not None:
            result['maxDelayTime'] = self.max_delay_time

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

        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling

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

        if m.get('maxDelayTime') is not None:
            self.max_delay_time = m.get('maxDelayTime')

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

        if m.get('supportAutoScaling') is not None:
            self.support_auto_scaling = m.get('supportAutoScaling')

        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')

        return self

class GetInstanceResponseBodyDataNetworkInfo(DaraModel):
    def __init__(
        self,
        endpoints: List[main_models.GetInstanceResponseBodyDataNetworkInfoEndpoints] = None,
        internet_info: main_models.GetInstanceResponseBodyDataNetworkInfoInternetInfo = None,
        vpc_info: main_models.GetInstanceResponseBodyDataNetworkInfoVpcInfo = None,
    ):
        # The endpoint information.
        self.endpoints = endpoints
        # The public network information of the instance.
        self.internet_info = internet_info
        # The VPC information.
        self.vpc_info = vpc_info

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.internet_info:
            self.internet_info.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['endpoints'].append(k1.to_map() if k1 else None)

        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()

        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('endpoints') is not None:
            for k1 in m.get('endpoints'):
                temp_model = main_models.GetInstanceResponseBodyDataNetworkInfoEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('internetInfo') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m.get('internetInfo'))

        if m.get('vpcInfo') is not None:
            temp_model = main_models.GetInstanceResponseBodyDataNetworkInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m.get('vpcInfo'))

        return self

class GetInstanceResponseBodyDataNetworkInfoVpcInfo(DaraModel):
    def __init__(
        self,
        security_group_ids: str = None,
        v_switch_id: str = None,
        v_switches: List[main_models.GetInstanceResponseBodyDataNetworkInfoVpcInfoVSwitches] = None,
        vpc_id: str = None,
    ):
        # The security group ID.
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch associated with the instance.
        # 
        # <notice>This field is not recommended. Use the vSwitches field instead. For compatibility, this field currently returns only one vSwitch.</notice>
        self.v_switch_id = v_switch_id
        # The list of vSwitches.
        self.v_switches = v_switches
        # The ID of the VPC associated with the instance.
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
                temp_model = main_models.GetInstanceResponseBodyDataNetworkInfoVpcInfoVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class GetInstanceResponseBodyDataNetworkInfoVpcInfoVSwitches(DaraModel):
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
            result['vSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class GetInstanceResponseBodyDataNetworkInfoInternetInfo(DaraModel):
    def __init__(
        self,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        ip_whitelist: List[str] = None,
    ):
        # The Internet bandwidth specification. Unit: Mbit/s.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The billing type for public network usage.
        self.flow_out_type = flow_out_type
        # Indicates whether public network access is enabled.
        # 
        # The instance supports VPC access by default. If public network access is enabled, ApsaraMQ for RocketMQ charges fees for public downstream bandwidth. For more information about billing, see [Public network access fees](https://help.aliyun.com/document_detail/427240.html).
        self.internet_spec = internet_spec
        # The IP whitelist for public network access.
        # 
        # - If the IP whitelist is not configured, all IP address ranges are allowed to access the ApsaraMQ for RocketMQ broker over the public network by default.
        # - If the IP whitelist is configured, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the public network.
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

class GetInstanceResponseBodyDataNetworkInfoEndpoints(DaraModel):
    def __init__(
        self,
        endpoint_id: str = None,
        endpoint_type: str = None,
        endpoint_url: str = None,
        ip_whitelist: List[str] = None,
    ):
        # The associated PrivateLink endpoint instance.
        self.endpoint_id = endpoint_id
        # The endpoint type of the instance.
        self.endpoint_type = endpoint_type
        # The endpoint of the instance.
        self.endpoint_url = endpoint_url
        # The IP whitelist for public network access. IP whitelists are supported only for Internet endpoints and are not supported for VPC endpoints.
        # 
        # - If no IP whitelist is configured, all IP address ranges are allowed to access the MSMQ for RocketMQ queue broker over the Internet by default.
        # - If an IP whitelist is configured, only IP addresses in the whitelist are allowed to access the MSMQ for RocketMQ queue broker over the Internet.
        # 
        # This field is no longer recommended. Use the internetInfo.ipWhitelist field instead.
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id

        if self.endpoint_type is not None:
            result['endpointType'] = self.endpoint_type

        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url

        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')

        if m.get('endpointType') is not None:
            self.endpoint_type = m.get('endpointType')

        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')

        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')

        return self

class GetInstanceResponseBodyDataInstanceQuotas(DaraModel):
    def __init__(
        self,
        free_count: float = None,
        quota_name: str = None,
        total_count: float = None,
        used_count: float = None,
    ):
        # The free quota. Unit: count.
        self.free_count = free_count
        # The quota name of the instance.
        self.quota_name = quota_name
        # The total quota. Unit: count.
        self.total_count = total_count
        # The used quota. Unit: count.
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.free_count is not None:
            result['freeCount'] = self.free_count

        if self.quota_name is not None:
            result['quotaName'] = self.quota_name

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.used_count is not None:
            result['usedCount'] = self.used_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('freeCount') is not None:
            self.free_count = m.get('freeCount')

        if m.get('quotaName') is not None:
            self.quota_name = m.get('quotaName')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('usedCount') is not None:
            self.used_count = m.get('usedCount')

        return self

class GetInstanceResponseBodyDataExtConfig(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        auto_scaling: bool = None,
        flow_out_bandwidth: int = None,
        flow_out_type: str = None,
        internet_spec: str = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        send_receive_ratio: float = None,
        support_auto_scaling: bool = None,
    ):
        # The authentication type of the instance.
        self.acl_type = acl_type
        # Indicates whether burstable elastic capacity beyond the base specification is enabled.
        # 
        # This parameter takes effect only when the value of supportAutoScaling is enable, which means the instance supports enabling elastic capacity.
        self.auto_scaling = auto_scaling
        # The Internet bandwidth specification. Unit: Mbit/s.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The billing type for public network usage.
        self.flow_out_type = flow_out_type
        # Indicates whether public network access is enabled.
        # 
        # The instance supports VPC access by default. If public network access is enabled, ApsaraMQ for RocketMQ charges fees for public downstream bandwidth. For more information about billing, see [Public network access fees](https://help.aliyun.com/document_detail/427240.html).
        self.internet_spec = internet_spec
        # The message retention period. Unit: hours.
        # 
        # For the value range, see [Limits](https://help.aliyun.com/document_detail/440347.html) > Resource Quotas > Message retention period.
        # 
        # The message storage of ApsaraMQ for RocketMQ is fully serverless and elastic. You are charged based on the actual storage space used. You can control the storage capacity by adjusting the message retention period. For more information, see [Storage fees](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The message processing specification. For the TPS upper limit of message sending and receiving, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        # The ratio of message sending to message receiving.
        self.send_receive_ratio = send_receive_ratio
        # Indicates whether the instance supports enabling burstable elastic capacity beyond the base specification.
        # 
        # After burstable elastic capacity is enabled, ApsaraMQ for RocketMQ allows the instance to exceed the TPS limit of the base specification within a certain range. Additional elastic specification fees are charged for the portion that exceeds the base specification. For more information about billing, see [Computing fees](https://help.aliyun.com/document_detail/427237.html).
        # 
        # > Only instances of specific specifications support burstable elastic capacity. For more information about supported instances, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.support_auto_scaling = support_auto_scaling

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['aclType'] = self.acl_type

        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling

        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth

        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type

        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec

        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time

        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec

        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio

        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')

        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')

        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')

        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')

        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')

        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')

        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')

        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')

        if m.get('supportAutoScaling') is not None:
            self.support_auto_scaling = m.get('supportAutoScaling')

        return self

class GetInstanceResponseBodyDataAclInfo(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        acl_types: List[str] = None,
        default_vpc_auth_free: bool = None,
    ):
        # The authentication type of the instance. This parameter is deprecated. Use the aclTypes parameter instead.
        self.acl_type = acl_type
        # The authentication types of the instance.
        self.acl_types = acl_types
        # Indicates whether the authentication-free in VPC feature is enabled.
        self.default_vpc_auth_free = default_vpc_auth_free

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['aclType'] = self.acl_type

        if self.acl_types is not None:
            result['aclTypes'] = self.acl_types

        if self.default_vpc_auth_free is not None:
            result['defaultVpcAuthFree'] = self.default_vpc_auth_free

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')

        if m.get('aclTypes') is not None:
            self.acl_types = m.get('aclTypes')

        if m.get('defaultVpcAuthFree') is not None:
            self.default_vpc_auth_free = m.get('defaultVpcAuthFree')

        return self

class GetInstanceResponseBodyDataAccountInfo(DaraModel):
    def __init__(
        self,
        username: str = None,
    ):
        # The username of the instance. When you use public network access, you must configure the username and password of the instance in the SDK code for identity verification.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')

        return self

