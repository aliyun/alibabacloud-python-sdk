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
        # The access control information.
        self.acl_info = acl_info
        # The updated instance name.
        self.instance_name = instance_name
        # The updated network information of the instance.
        self.network_info = network_info
        # The extension configurations of the instance.
        self.product_info = product_info
        # The updated remarks for the instance.
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
        adaptive_elasticity: bool = None,
        auto_scaling: bool = None,
        message_retention_time: int = None,
        send_receive_ratio: float = None,
        trace_on: bool = None,
    ):
        # Specifies whether to enable the adaptive elasticity capability. A value of true indicates enabled, and a value of false indicates shutdown.
        self.adaptive_elasticity = adaptive_elasticity
        # Specifies whether to enable the burstable elastic capacity beyond the specification.
        # 
        # After the burstable elastic capacity is enabled, ApsaraMQ for RocketMQ allows the instance to exceed the TPS limit of the base specification within a certain range. The portion that exceeds the base specification incurs additional elastic specification fees. For more information about billing, see [Computing fee](https://help.aliyun.com/document_detail/427237.html).
        # 
        # 
        # > Only instances of specific specifications support the burstable elastic specification capability. For more information about supported instances, see [Instance specifications](https://help.aliyun.com/document_detail/444715.html).
        self.auto_scaling = auto_scaling
        # The message retention period. Unit: hours.
        # 
        # For the valid values, see [Limits](https://help.aliyun.com/document_detail/440347.html) > Resource Quotas > Message retention period limit.
        # 
        # The log broker in ApsaraMQ for RocketMQ is fully serverless and elastic. Fees are charged based on the actual storage space used. You can control the storage capacity of messages by adjusting the message retention period. For more information, see [Storage fee](https://help.aliyun.com/document_detail/427238.html).
        self.message_retention_time = message_retention_time
        # The ratio of messages sent to messages accepted.
        # 
        # Valid values: [0.25, 1]
        self.send_receive_ratio = send_receive_ratio
        # Specifies whether to enable the message trace feature.
        # 
        # <props="intl">This parameter does not take effect. Regardless of whether this parameter is enabled, the instance supports the message trace feature by default.
        # <props="china">This parameter takes effect only for Serverless instances. If the message trace feature is enabled, message trace fees are incurred. For more information about billing, see [Serverless billing](https://help.aliyun.com/document_detail/2586280.html).
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

        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time

        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio

        if self.trace_on is not None:
            result['traceOn'] = self.trace_on

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adaptiveElasticity') is not None:
            self.adaptive_elasticity = m.get('adaptiveElasticity')

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
        # The public network information. This parameter is valid only when the public network access feature is enabled for the instance.
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
        # The public network access IP whitelist.
        # 
        # - If no IP whitelist is configured, all IP address ranges are allowed to access the ApsaraMQ for RocketMQ server over the public network by default.
        # - If an IP whitelist is configured, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ server over the public network.
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
        # Indicates whether password-free access is enabled for VPC connections under the intelligent identity recognition type.
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

