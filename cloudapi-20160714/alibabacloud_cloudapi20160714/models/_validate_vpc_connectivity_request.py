# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateVpcConnectivityRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        security_token: str = None,
        vpc_access_id: str = None,
    ):
        # The ID of the API Gateway instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.security_token = security_token
        # The ID of the VPC access authorization.
        # 
        # This parameter is required.
        self.vpc_access_id = vpc_access_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.vpc_access_id is not None:
            result['VpcAccessId'] = self.vpc_access_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('VpcAccessId') is not None:
            self.vpc_access_id = m.get('VpcAccessId')

        return self

