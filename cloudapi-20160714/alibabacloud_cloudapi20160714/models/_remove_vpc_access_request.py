# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveVpcAccessRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        need_batch_work: bool = None,
        port: int = None,
        security_token: str = None,
        vpc_id: str = None,
    ):
        # The ID of an ECS or SLB instance in the VPC.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether batch work is required.
        self.need_batch_work = need_batch_work
        # The port number that corresponds to the instance.
        # 
        # This parameter is required.
        self.port = port
        self.security_token = security_token
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.need_batch_work is not None:
            result['NeedBatchWork'] = self.need_batch_work

        if self.port is not None:
            result['Port'] = self.port

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NeedBatchWork') is not None:
            self.need_batch_work = m.get('NeedBatchWork')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

