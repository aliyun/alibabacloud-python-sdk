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
        # The error code returned if the call failed.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
        # The information about access control.
        self.acl_info = acl_info
        # The business ID (BID) of the commodity.
        self.bid = bid
        # The commodity code of the instance. The commodity code of a ApsaraMQ for RocketMQ 5.0 instance has a similar format as ons_rmqsub_public_cn.
        self.commodity_code = commodity_code
        # The time when the instance was created.
        self.create_time = create_time
        # The time when the instance expires.
        self.expire_time = expire_time
        # The extended configurations. We recommend you configure productInfo, internetInfo, or aclInfo instead of this parameter.
        self.ext_config = ext_config
        # The number of groups.
        self.group_count = group_count
        # The ID of the instance
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The instance quotas.
        self.instance_quotas = instance_quotas
        # The network information.
        self.network_info = network_info
        # The billing method of the instance.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The extended configurations of the instance.
        self.product_info = product_info
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The time when the instance was released.
        self.release_time = release_time
        # The description of the instance.
        self.remark = remark
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The primary edition of the instance. For information about the differences between primary edition instances, see [Instance selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        self.series_code = series_code
        # The code of the service to which the instance belongs. The service code of ApsaraMQ for RocketMQ is rmq.
        self.service_code = service_code
        # The instance software information.
        self.software = software
        # The time when the instance was started.
        self.start_time = start_time
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   RELEASED
        # *   RUNNING
        # *   STOPPED
        # *   CHANGING
        # *   CREATING
        self.status = status
        # The sub-category edition of the instance. For information about the differences between sub-category edition instances, see [Instance selection](https://help.aliyun.com/document_detail/444722.html).
        # 
        # Valid values:
        # 
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        self.sub_series_code = sub_series_code
        # The resource tags.
        self.tags = tags
        # The number of topics.
        self.topic_count = topic_count
        # The time when the instance was last modified.
        self.update_time = update_time
        # The ID of the user who owns the instance.
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
        # The tag key of the resource.
        self.key = key
        # The tag value of the resource.
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
        # The period of upgrade time.
        self.maintain_time = maintain_time
        # The version of software.
        self.software_version = software_version
        # The upgrade method.
        # 
        # Valid values:
        # 
        # - Auto: automatic upgrade
        # 
        # - Manual: manual upgrade
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
        auto_scaling: bool = None,
        capacity_type: str = None,
        message_retention_time: int = None,
        msg_process_spec: str = None,
        provisioned_capacity: int = None,
        send_receive_ratio: float = None,
        storage_encryption: bool = None,
        storage_secret_key: str = None,
        support_auto_scaling: bool = None,
        trace_on: bool = None,
    ):
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # This parameter is valid only when the supportAutoScaling parameter is set to enable.
        self.auto_scaling = auto_scaling
        self.capacity_type = capacity_type
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section in [Usage limits](https://help.aliyun.com/document_detail/440347.html).
        # 
        # The storage of messages in ApsaraMQ for RocketMQ is serverless and scalable. You are charged for message storage based on your actual usage. You can change the retention period of messages to adjust storage capacity. For more information, see [Storage fee](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The computing specification that is used to send and receive messages. For information about the upper limit of TPS, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        self.provisioned_capacity = provisioned_capacity
        # The ratio between sent messages and received messages in the instance.
        self.send_receive_ratio = send_receive_ratio
        # Indicates whether storage encryption is enabled.
        self.storage_encryption = storage_encryption
        # The storage encryption key.
        self.storage_secret_key = storage_secret_key
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # After you enable the elastic TPS feature for a ApsaraMQ for RocketMQ instance, you can use a specific amount of TPS that exceeds the specification limit. You are charged for the elastic TPS feature. For more information, see [Computing fee](https://help.aliyun.com/document_detail/427237.html).
        # 
        # > The elastic TPS feature is supported by only specific instance editions. For more information, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.support_auto_scaling = support_auto_scaling
        # Indicates whether the message trace feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is not in use. By default, the message trace feature is enabled for ApsaraMQ for RocketMQ instances, regardless of whether this parameter is configured.
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

        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling

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
        # The endpoints.
        self.endpoints = endpoints
        # The information about the Internet.
        self.internet_info = internet_info
        # The virtual private cloud (VPC) information.
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
        # The ID of the vSwitch with which the instance is associated.
        self.v_switch_id = v_switch_id
        # The vSwitches.
        self.v_switches = v_switches
        # The ID of the VPC with which the instance is associated.
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
        # The Internet bandwidth. Unit: MB/s.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The metering method for Internet usage.
        # 
        # Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth. If the Internet access feature is enabled, specify this value for the parameter.
        # *   uninvolved: N/A. If the Internet access feature is not enabled, specify this value for the parameter.
        self.flow_out_type = flow_out_type
        # Specifies whether to enable the Internet access feature.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, ApsaraMQ for RocketMQ instances are accessed in virtual private clouds (VPCs). If you enable the Internet access feature, you are charged for Internet outbound bandwidth. For more information, see [Internet access fee](https://help.aliyun.com/document_detail/427240.html).
        self.internet_spec = internet_spec
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker.
        # 
        # *   If this parameter is not configured, all IP addresses are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If this parameter is configured, only the IP addresses that are included in the whitelist can access the ApsaraMQ for RocketMQ broker over the Internet.
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
        self.endpoint_id = endpoint_id
        # The type of the endpoint that is used to access the instance.
        # 
        # Valid values:
        # 
        # *   TCP_VPC: VPC endpoint
        # *   TCP_INTERNET: public endpoint
        self.endpoint_type = endpoint_type
        # The endpoint that is used to access the instance.
        self.endpoint_url = endpoint_url
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet. This parameter can be configured only if you use the public endpoint to access the instance.
        # 
        # *   If you do not configure an IP address whitelist, all CIDR blocks are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If you configure an IP address whitelist, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # 
        # We recommend that you configure internetInfo.ipWhitelist instead of this parameter.
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
        # The number of topics that are free of charge on the instance.
        self.free_count = free_count
        # The quota name.
        # 
        # Valid value:
        # 
        # *   TOPIC_COUNT: the number of topics that can be created on the instance
        self.quota_name = quota_name
        # The total number of topics on the instance.
        self.total_count = total_count
        # The number of used topics on the instance.
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
        # 
        # Valid value:
        # 
        # *   default: intelligent authentication
        self.acl_type = acl_type
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # This parameter is valid only when the supportAutoScaling parameter is set to enable.
        self.auto_scaling = auto_scaling
        # The Internet bandwidth. Unit: MB/s.
        self.flow_out_bandwidth = flow_out_bandwidth
        # The metering method of Internet usage.
        # 
        # Valid values:
        # 
        # *   PayByTraffic: pay-by-traffic
        # *   paybybandwidth: pay-by-bandwidth
        # *   uninvolved: N/A
        self.flow_out_type = flow_out_type
        # Indicates whether Internet access is enabled.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, you can access ApsaraMQ for RocketMQ instances in virtual private clouds (VPCs). If you enable the Internet access feature, you are charged for Internet outbound bandwidth. For more information, see [Internet access fees](https://help.aliyun.com/document_detail/427240.html).
        self.internet_spec = internet_spec
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section in [Usage limits](https://help.aliyun.com/document_detail/440347.html).
        # 
        # The storage of messages in ApsaraMQ for RocketMQ is serverless and scalable. You are charged for message storage based on your actual usage. You can change the retention period of messages to adjust storage capacity. For more information, see [Storage fee](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The computing specification that is used to send and receive messages. For information about the upper limit of TPS, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.msg_process_spec = msg_process_spec
        # The ratio between sent messages and received messages in the instance.
        self.send_receive_ratio = send_receive_ratio
        # Specifies whether the elastic TPS feature is supported by the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # After you enable the elastic TPS feature for a ApsaraMQ for RocketMQ instance, you can use a specific amount of TPS that exceeds the specification limit. You are charged for the elastic TPS feature. For more information, see [Computing fee](https://help.aliyun.com/document_detail/427237.html).
        # 
        # > The elastic TPS feature is supported only by specific instance editions. For more information, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
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
        # The authentication type of the instance. This parameter is no longer in use. We recommend that you configure aclTypes.
        # 
        # Valid values:
        # 
        # - default: intelligent identity authentication
        # 
        # - apache_acl:access control list (ACL) identity authentication**
        self.acl_type = acl_type
        # The authentication types of the instance.
        self.acl_types = acl_types
        # Indicates whether the authentication-free in VPCs feature is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
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
        # The username of the instance. If you access a ApsaraMQ for RocketMQ instance over the Internet, you must configure the username and password of the instance in the SDK code for authentication.
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

