# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkTrafficTopRatioRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        asset_ip: str = None,
        asset_region: str = None,
        data_type: str = None,
        direction: str = None,
        dst_ip: str = None,
        dst_port: str = None,
        end_time: str = None,
        ip_property: str = None,
        isp: str = None,
        lang: str = None,
        location: str = None,
        rule_result: str = None,
        sort: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        start_time: str = None,
    ):
        self.app_name = app_name
        self.asset_ip = asset_ip
        self.asset_region = asset_region
        # This parameter is required.
        self.data_type = data_type
        self.direction = direction
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        # This parameter is required.
        self.end_time = end_time
        self.ip_property = ip_property
        self.isp = isp
        self.lang = lang
        self.location = location
        self.rule_result = rule_result
        self.sort = sort
        # This parameter is required.
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.asset_ip is not None:
            result['AssetIP'] = self.asset_ip

        if self.asset_region is not None:
            result['AssetRegion'] = self.asset_region

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip_property is not None:
            result['IpProperty'] = self.ip_property

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.location is not None:
            result['Location'] = self.location

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AssetIP') is not None:
            self.asset_ip = m.get('AssetIP')

        if m.get('AssetRegion') is not None:
            self.asset_region = m.get('AssetRegion')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IpProperty') is not None:
            self.ip_property = m.get('IpProperty')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

