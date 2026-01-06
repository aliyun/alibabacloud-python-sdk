# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SourceRabbitMQMsgSyncParameters(DaraModel):
    def __init__(
        self,
        body_data_type: str = None,
        endpoint: str = None,
        instance_id: str = None,
        instance_type: str = None,
        network_type: str = None,
        order_consume: str = None,
        password: str = None,
        prefetch_count: str = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_ids: str = None,
        virtual_host_name: str = None,
        vpc_id: str = None,
    ):
        self.body_data_type = body_data_type
        self.endpoint = endpoint
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.network_type = network_type
        self.order_consume = order_consume
        self.password = password
        self.prefetch_count = prefetch_count
        self.security_group_id = security_group_id
        self.username = username
        self.v_switch_ids = v_switch_ids
        self.virtual_host_name = virtual_host_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_data_type is not None:
            result['BodyDataType'] = self.body_data_type

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.order_consume is not None:
            result['OrderConsume'] = self.order_consume

        if self.password is not None:
            result['Password'] = self.password

        if self.prefetch_count is not None:
            result['PrefetchCount'] = self.prefetch_count

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.username is not None:
            result['Username'] = self.username

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyDataType') is not None:
            self.body_data_type = m.get('BodyDataType')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OrderConsume') is not None:
            self.order_consume = m.get('OrderConsume')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PrefetchCount') is not None:
            self.prefetch_count = m.get('PrefetchCount')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

