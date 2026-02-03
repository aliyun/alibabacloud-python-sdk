# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeDBNodeDirectVipInfoResponseBody(DaraModel):
    def __init__(
        self,
        direct_vip_info: main_models.DescribeDBNodeDirectVipInfoResponseBodyDirectVipInfo = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The VIP information of shards in the cluster instance.
        self.direct_vip_info = direct_vip_info
        # The instance ID.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.direct_vip_info:
            self.direct_vip_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direct_vip_info is not None:
            result['DirectVipInfo'] = self.direct_vip_info.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectVipInfo') is not None:
            temp_model = main_models.DescribeDBNodeDirectVipInfoResponseBodyDirectVipInfo()
            self.direct_vip_info = temp_model.from_map(m.get('DirectVipInfo'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBNodeDirectVipInfoResponseBodyDirectVipInfo(DaraModel):
    def __init__(
        self,
        vip_info: List[main_models.DescribeDBNodeDirectVipInfoResponseBodyDirectVipInfoVipInfo] = None,
    ):
        self.vip_info = vip_info

    def validate(self):
        if self.vip_info:
            for v1 in self.vip_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VipInfo'] = []
        if self.vip_info is not None:
            for k1 in self.vip_info:
                result['VipInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vip_info = []
        if m.get('VipInfo') is not None:
            for k1 in m.get('VipInfo'):
                temp_model = main_models.DescribeDBNodeDirectVipInfoResponseBodyDirectVipInfoVipInfo()
                self.vip_info.append(temp_model.from_map(k1))

        return self

class DescribeDBNodeDirectVipInfoResponseBodyDirectVipInfoVipInfo(DaraModel):
    def __init__(
        self,
        net_type: str = None,
        node_id: str = None,
        port: str = None,
        vip: str = None,
    ):
        # The network type of the security group. Valid values:
        # 
        # *   **vpc**: Virtual Private Cloud (VPC)
        self.net_type = net_type
        # The shard ID.
        self.node_id = node_id
        # The port number. Valid values: **1024** to **65535**. Default value: **6379**.
        self.port = port
        # The VIP of the shard.
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.port is not None:
            result['Port'] = self.port

        if self.vip is not None:
            result['Vip'] = self.vip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Vip') is not None:
            self.vip = m.get('Vip')

        return self

