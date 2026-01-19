# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcAccessAndUpdateApisRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        need_batch_work: bool = None,
        port: int = None,
        refresh: bool = None,
        security_token: str = None,
        token: str = None,
        vpc_id: str = None,
        vpc_target_host_name: str = None,
    ):
        # The ID of the new instance.
        self.instance_id = instance_id
        # The name of the VPC authorization.
        # 
        # > 
        # 
        # *   The name of a VPC authorization cannot be changed. You cannot use this parameter to change the name of a VPC authorization.
        # 
        # *   You must set this parameter to the name of the current VPC authorization.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to update the associated API.
        # 
        # **
        # 
        # **Warning:** If you want to update the VPC authorization of a published API, you must set this parameter to true. Otherwise, the update will not be synchronized to the backend service of the API.
        self.need_batch_work = need_batch_work
        # The new port number.
        self.port = port
        # Specifies whether to update the VPC authorization.
        # 
        # > 
        # 
        # *   If the ID of the instance in your VPC is changed but the IP address of the instance remains unchanged, you can set this parameter to true to update the VPC authorization.
        self.refresh = refresh
        self.security_token = security_token
        # The token of the request.
        self.token = token
        # The ID of the new VPC.
        self.vpc_id = vpc_id
        # The hostname of the backend service.
        self.vpc_target_host_name = vpc_target_host_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.need_batch_work is not None:
            result['NeedBatchWork'] = self.need_batch_work

        if self.port is not None:
            result['Port'] = self.port

        if self.refresh is not None:
            result['Refresh'] = self.refresh

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.token is not None:
            result['Token'] = self.token

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_target_host_name is not None:
            result['VpcTargetHostName'] = self.vpc_target_host_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedBatchWork') is not None:
            self.need_batch_work = m.get('NeedBatchWork')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Refresh') is not None:
            self.refresh = m.get('Refresh')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcTargetHostName') is not None:
            self.vpc_target_host_name = m.get('VpcTargetHostName')

        return self

