# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        acl_info: main_models.UpdateInstanceRequestAclInfo = None,
        instance_name: str = None,
        network_info: main_models.UpdateInstanceRequestNetworkInfo = None,
        product_info: main_models.UpdateInstanceRequestProductInfo = None,
        remark: str = None,
    ):
        # The access control list for the instance.
        self.acl_info = acl_info
        # The updated name of the instance.
        self.instance_name = instance_name
        # The updated network information about the instance.
        self.network_info = network_info
        # Additional configurations of the instance.
        self.product_info = product_info
        # The updated description of the instance.
        self.remark = remark

    def validate(self):
        if self.acl_info:
            self.acl_info.validate()
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_info is not None:
            result['aclInfo'] = self.acl_info.to_map()

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()

        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclInfo') is not None:
            temp_model = main_models.UpdateInstanceRequestAclInfo()
            self.acl_info = temp_model.from_map(m.get('aclInfo'))

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('networkInfo') is not None:
            temp_model = main_models.UpdateInstanceRequestNetworkInfo()
            self.network_info = temp_model.from_map(m.get('networkInfo'))

        if m.get('productInfo') is not None:
            temp_model = main_models.UpdateInstanceRequestProductInfo()
            self.product_info = temp_model.from_map(m.get('productInfo'))

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

class UpdateInstanceRequestProductInfo(DaraModel):
    def __init__(
        self,
        auto_scaling: bool = None,
        message_retention_time: int = None,
        send_receive_ratio: float = None,
        trace_on: bool = None,
    ):
        # Specifies whether to enable the elastic transactions per second (TPS) feature for the instance.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # After you enable the elastic TPS feature for an ApsaraMQ for RocketMQ instance, you can use a specific number of TPS that exceeds the specification limit. You are charged for using the elastic TPS feature. For more information, see [Computing fees](https://help.aliyun.com/document_detail/427237.html).
        # 
        # >  The elastic TPS feature is supported only by specific instance editions. For more information, see [Instance editions](https://help.aliyun.com/document_detail/444715.html).
        self.auto_scaling = auto_scaling
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section of the [Limits](https://help.aliyun.com/document_detail/440347.html) topic.
        # 
        # ApsaraMQ for RocketMQ supports serverless scaling of message storage. You are charged storage fees based on your actual storage usage. You can change the retention period of messages to manage storage capacity. For more information, see [Storage fees](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The ratio of the number of messages that you can send to the number of messages that you can receive on the instance.
        # 
        # Value values: 0.25 to 1.
        self.send_receive_ratio = send_receive_ratio
        # Specifies whether to enable the message trace feature.
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

        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time

        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio

        if self.trace_on is not None:
            result['traceOn'] = self.trace_on

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')

        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')

        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')

        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')

        return self

class UpdateInstanceRequestNetworkInfo(DaraModel):
    def __init__(
        self,
        internet_info: main_models.UpdateInstanceRequestNetworkInfoInternetInfo = None,
    ):
        # The information about the Internet over which the instance is accessed. This parameter takes effect only if the Internet access feature is enabled for the instance.
        self.internet_info = internet_info

    def validate(self):
        if self.internet_info:
            self.internet_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internetInfo') is not None:
            temp_model = main_models.UpdateInstanceRequestNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m.get('internetInfo'))

        return self

class UpdateInstanceRequestNetworkInfoInternetInfo(DaraModel):
    def __init__(
        self,
        ip_whitelist: List[str] = None,
    ):
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # 
        # *   If you do not configure an IP address whitelist, all CIDR blocks are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If you configure an IP address whitelist, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')

        return self

class UpdateInstanceRequestAclInfo(DaraModel):
    def __init__(
        self,
        acl_types: List[str] = None,
        default_vpc_auth_free: bool = None,
    ):
        # The authentication type of the instance.
        self.acl_types = acl_types
        # Indicates whether the authentication-free in VPCs feature is enabled.
        # Indicates whether the authentication-free in VPCs feature is enabled.
        # Valid values:
        # - true
        # - false
        self.default_vpc_auth_free = default_vpc_auth_free

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_types is not None:
            result['aclTypes'] = self.acl_types

        if self.default_vpc_auth_free is not None:
            result['defaultVpcAuthFree'] = self.default_vpc_auth_free

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclTypes') is not None:
            self.acl_types = m.get('aclTypes')

        if m.get('defaultVpcAuthFree') is not None:
            self.default_vpc_auth_free = m.get('defaultVpcAuthFree')

        return self

