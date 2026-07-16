# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConnectorProperties(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        dry_run_request_body: str = None,
        model_list: str = None,
        network: str = None,
        protocol: str = None,
        region: str = None,
        response_body_path: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.channel_type = channel_type
        self.dry_run_request_body = dry_run_request_body
        self.model_list = model_list
        self.network = network
        self.protocol = protocol
        self.region = region
        self.response_body_path = response_body_path
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.dry_run_request_body is not None:
            result['dryRunRequestBody'] = self.dry_run_request_body

        if self.model_list is not None:
            result['modelList'] = self.model_list

        if self.network is not None:
            result['network'] = self.network

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.region is not None:
            result['region'] = self.region

        if self.response_body_path is not None:
            result['responseBodyPath'] = self.response_body_path

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('dryRunRequestBody') is not None:
            self.dry_run_request_body = m.get('dryRunRequestBody')

        if m.get('modelList') is not None:
            self.model_list = m.get('modelList')

        if m.get('network') is not None:
            self.network = m.get('network')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('responseBodyPath') is not None:
            self.response_body_path = m.get('responseBodyPath')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

