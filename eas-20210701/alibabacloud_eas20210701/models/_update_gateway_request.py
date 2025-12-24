# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateGatewayRequest(DaraModel):
    def __init__(
        self,
        enable_internet: bool = None,
        enable_intranet: bool = None,
        enable_sslredirection: bool = None,
        instance_type: str = None,
        is_default: bool = None,
        name: str = None,
        replicas: int = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # Specifies whether to enable Internet access. Default value: false.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.enable_internet = enable_internet
        # Specifies whether to enable private access. Default value: true.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.enable_intranet = enable_intranet
        # Specifies whether to enable HTTP to HTTPS redirection. Default value: false.
        self.enable_sslredirection = enable_sslredirection
        # The instance type used by the private gateway. Valid values:
        # 
        # *   2c4g
        # *   4c8g
        # *   8c16g
        # *   16c32g
        self.instance_type = instance_type
        # Specifies whether it is the default private gateway.
        self.is_default = is_default
        # The alias of the private gateway.
        self.name = name
        # The number of nodes in the private gateway.
        self.replicas = replicas
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_internet is not None:
            result['EnableInternet'] = self.enable_internet

        if self.enable_intranet is not None:
            result['EnableIntranet'] = self.enable_intranet

        if self.enable_sslredirection is not None:
            result['EnableSSLRedirection'] = self.enable_sslredirection

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInternet') is not None:
            self.enable_internet = m.get('EnableInternet')

        if m.get('EnableIntranet') is not None:
            self.enable_intranet = m.get('EnableIntranet')

        if m.get('EnableSSLRedirection') is not None:
            self.enable_sslredirection = m.get('EnableSSLRedirection')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

