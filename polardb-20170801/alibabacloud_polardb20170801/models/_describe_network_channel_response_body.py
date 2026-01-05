# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkChannelResponseBody(DaraModel):
    def __init__(
        self,
        channel_infos: List[main_models.DescribeNetworkChannelResponseBodyChannelInfos] = None,
        request_id: str = None,
    ):
        self.channel_infos = channel_infos
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.channel_infos:
            for v1 in self.channel_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChannelInfos'] = []
        if self.channel_infos is not None:
            for k1 in self.channel_infos:
                result['ChannelInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel_infos = []
        if m.get('ChannelInfos') is not None:
            for k1 in m.get('ChannelInfos'):
                temp_model = main_models.DescribeNetworkChannelResponseBodyChannelInfos()
                self.channel_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNetworkChannelResponseBodyChannelInfos(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        dbcluster_id: str = None,
        notes: str = None,
        region_id: str = None,
        target_dbcluster_id: str = None,
        target_ip: str = None,
        target_port: str = None,
        target_type: str = None,
        vpc_id: str = None,
    ):
        self.channel_name = channel_name
        self.dbcluster_id = dbcluster_id
        self.notes = notes
        self.region_id = region_id
        self.target_dbcluster_id = target_dbcluster_id
        self.target_ip = target_ip
        self.target_port = target_port
        self.target_type = target_type
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.notes is not None:
            result['Notes'] = self.notes

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_dbcluster_id is not None:
            result['TargetDBClusterId'] = self.target_dbcluster_id

        if self.target_ip is not None:
            result['TargetIp'] = self.target_ip

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Notes') is not None:
            self.notes = m.get('Notes')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetDBClusterId') is not None:
            self.target_dbcluster_id = m.get('TargetDBClusterId')

        if m.get('TargetIp') is not None:
            self.target_ip = m.get('TargetIp')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

