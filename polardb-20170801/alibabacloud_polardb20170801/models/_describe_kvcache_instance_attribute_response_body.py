# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKVCacheInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        creation_time: str = None,
        expire_time: str = None,
        expired: str = None,
        kvcache_instance_id: str = None,
        kvcache_instance_status: str = None,
        kvcache_space: str = None,
        pay_type: str = None,
        port: str = None,
        region_id: str = None,
        request_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The endpoint of the instance.
        self.connection_string = connection_string
        # The time when the instance was created, in ISO 8601 format.
        self.creation_time = creation_time
        # The time when the instance expires, in ISO 8601 format. An empty string is returned for pay-as-you-go instances.
        self.expire_time = expire_time
        # Indicates whether the instance has expired.
        self.expired = expired
        # The KVCache instance ID.
        self.kvcache_instance_id = kvcache_instance_id
        # The KVCache instance status.
        self.kvcache_instance_status = kvcache_instance_status
        # The storage capacity of the KVCache instance.
        self.kvcache_space = kvcache_space
        # The billing method.
        self.pay_type = pay_type
        # The port.
        self.port = port
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The VPC ID.
        self.vpcid = vpcid
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
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.kvcache_instance_id is not None:
            result['KVCacheInstanceId'] = self.kvcache_instance_id

        if self.kvcache_instance_status is not None:
            result['KVCacheInstanceStatus'] = self.kvcache_instance_status

        if self.kvcache_space is not None:
            result['KVCacheSpace'] = self.kvcache_space

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('KVCacheInstanceId') is not None:
            self.kvcache_instance_id = m.get('KVCacheInstanceId')

        if m.get('KVCacheInstanceStatus') is not None:
            self.kvcache_instance_status = m.get('KVCacheInstanceStatus')

        if m.get('KVCacheSpace') is not None:
            self.kvcache_space = m.get('KVCacheSpace')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

