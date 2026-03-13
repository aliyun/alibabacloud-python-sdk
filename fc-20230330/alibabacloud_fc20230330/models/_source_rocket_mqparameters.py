# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SourceRocketMQParameters(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        filter_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        # The authentication type. Set the value to ACL or leave the value empty. The value ACL indicates that authentication is enabled. In this case, you must specify InstanceUsername and InstancePassword.
        self.auth_type = auth_type
        # The message filter type.
        self.filter_type = filter_type
        # The ID of the consumer group of the ApsaraMQ for RocketMQ instance.
        self.group_id = group_id
        # The information about the endpoint of the ApsaraMQ for RocketMQ instance.
        self.instance_endpoint = instance_endpoint
        # The ID of the ApsaraMQ for RocketMQ instance.
        self.instance_id = instance_id
        # The network type.
        self.instance_network = instance_network
        # The password of the ApsaraMQ for RocketMQ instance.
        self.instance_password = instance_password
        # The security group ID.
        self.instance_security_group_id = instance_security_group_id
        # The type of ApsaraMQ for RocketMQ instance.
        self.instance_type = instance_type
        # The username of the ApsaraMQ for RocketMQ instance. If you use the Internet, you must configure the username and password of the instance in the SDK code for authentication.
        self.instance_username = instance_username
        # The ID of the vSwitch associated with the instance.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The ID of the virtual private cloud (VPC) associated with the instance.
        self.instance_vpc_id = instance_vpc_id
        # The consumer offset of the message. CONSUME_FROM_LAST_OFFSET: consumes messages from the latest offset. This is the default value. CONSUME_FROM_FIRST_OFFSET: consumes messages from the earliest offset. CONSUME_FROM_TIMESTAMP: consumes messages from the offset at the specified point in time.
        self.offset = offset
        # The region to which the ApsaraMQ for RocketMQ queue belongs.
        self.region_id = region_id
        # The tags that are used to filter messages.
        self.tag = tag
        # The timestamp. This parameter is valid only when you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The name of the topic in the ApsaraMQ for RocketMQ instance.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.filter_type is not None:
            result['FilterType'] = self.filter_type

        if self.group_id is not None:
            result['GroupID'] = self.group_id

        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network

        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password

        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username

        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids

        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')

        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')

        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')

        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')

        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')

        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')

        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

