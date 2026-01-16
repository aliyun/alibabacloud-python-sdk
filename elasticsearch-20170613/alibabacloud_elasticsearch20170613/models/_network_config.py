# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class NetworkConfig(DaraModel):
    def __init__(
        self,
        lb_replica: int = None,
        load_balance_config: List[main_models.NetworkConfigLoadBalanceConfig] = None,
        load_balance_type: str = None,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
        white_ip_group_list: List[main_models.WhiteIpGroup] = None,
    ):
        self.lb_replica = lb_replica
        self.load_balance_config = load_balance_config
        self.load_balance_type = load_balance_type
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id
        self.white_ip_group_list = white_ip_group_list

    def validate(self):
        if self.load_balance_config:
            for v1 in self.load_balance_config:
                 if v1:
                    v1.validate()
        if self.white_ip_group_list:
            for v1 in self.white_ip_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lb_replica is not None:
            result['lbReplica'] = self.lb_replica

        result['loadBalanceConfig'] = []
        if self.load_balance_config is not None:
            for k1 in self.load_balance_config:
                result['loadBalanceConfig'].append(k1.to_map() if k1 else None)

        if self.load_balance_type is not None:
            result['loadBalanceType'] = self.load_balance_type

        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vs_area is not None:
            result['vsArea'] = self.vs_area

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        result['whiteIpGroupList'] = []
        if self.white_ip_group_list is not None:
            for k1 in self.white_ip_group_list:
                result['whiteIpGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lbReplica') is not None:
            self.lb_replica = m.get('lbReplica')

        self.load_balance_config = []
        if m.get('loadBalanceConfig') is not None:
            for k1 in m.get('loadBalanceConfig'):
                temp_model = main_models.NetworkConfigLoadBalanceConfig()
                self.load_balance_config.append(temp_model.from_map(k1))

        if m.get('loadBalanceType') is not None:
            self.load_balance_type = m.get('loadBalanceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        self.white_ip_group_list = []
        if m.get('whiteIpGroupList') is not None:
            for k1 in m.get('whiteIpGroupList'):
                temp_model = main_models.WhiteIpGroup()
                self.white_ip_group_list.append(temp_model.from_map(k1))

        return self

class NetworkConfigLoadBalanceConfig(DaraModel):
    def __init__(
        self,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        return self

