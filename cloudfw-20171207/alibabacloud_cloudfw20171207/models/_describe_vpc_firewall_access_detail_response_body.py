# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallAccessDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeVpcFirewallAccessDetailResponseBodyDataList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeVpcFirewallAccessDetailResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcFirewallAccessDetailResponseBodyDataList(DaraModel):
    def __init__(
        self,
        in_bytes: int = None,
        out_bytes: int = None,
        peer_asset_ip: str = None,
        peer_asset_instance_id: str = None,
        peer_asset_instance_name: str = None,
        peer_vpc_id: str = None,
        region_no: str = None,
        session_count: int = None,
        peer_vpc_name: str = None,
    ):
        self.in_bytes = in_bytes
        self.out_bytes = out_bytes
        self.peer_asset_ip = peer_asset_ip
        self.peer_asset_instance_id = peer_asset_instance_id
        self.peer_asset_instance_name = peer_asset_instance_name
        self.peer_vpc_id = peer_vpc_id
        self.region_no = region_no
        self.session_count = session_count
        self.peer_vpc_name = peer_vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.peer_asset_ip is not None:
            result['PeerAssetIP'] = self.peer_asset_ip

        if self.peer_asset_instance_id is not None:
            result['PeerAssetInstanceId'] = self.peer_asset_instance_id

        if self.peer_asset_instance_name is not None:
            result['PeerAssetInstanceName'] = self.peer_asset_instance_name

        if self.peer_vpc_id is not None:
            result['PeerVpcId'] = self.peer_vpc_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.peer_vpc_name is not None:
            result['peerVpcName'] = self.peer_vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('PeerAssetIP') is not None:
            self.peer_asset_ip = m.get('PeerAssetIP')

        if m.get('PeerAssetInstanceId') is not None:
            self.peer_asset_instance_id = m.get('PeerAssetInstanceId')

        if m.get('PeerAssetInstanceName') is not None:
            self.peer_asset_instance_name = m.get('PeerAssetInstanceName')

        if m.get('PeerVpcId') is not None:
            self.peer_vpc_id = m.get('PeerVpcId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('peerVpcName') is not None:
            self.peer_vpc_name = m.get('peerVpcName')

        return self

