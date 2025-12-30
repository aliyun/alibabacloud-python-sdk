# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class BindZoneVpcRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
        user_client_ip: str = None,
        vpcs: List[main_models.BindZoneVpcRequestVpcs] = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The VPCs.
        # 
        # >  If Vpcs is left empty, all VPCs that are associated with the zone are disassociated from the zone.
        self.vpcs = vpcs
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.vpcs:
            for v1 in self.vpcs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        result['Vpcs'] = []
        if self.vpcs is not None:
            for k1 in self.vpcs:
                result['Vpcs'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k1 in m.get('Vpcs'):
                temp_model = main_models.BindZoneVpcRequestVpcs()
                self.vpcs.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class BindZoneVpcRequestVpcs(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        # The region ID of the VPC.
        self.region_id = region_id
        # The VPC ID. If the zone is already associated with VPCs and you do not specify this parameter, the associated VPCs are disassociated from the zone.
        self.vpc_id = vpc_id
        # The VPC type. Valid values:
        # 
        # *   **STANDARD**: standard VPC
        # *   **EDS**: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

