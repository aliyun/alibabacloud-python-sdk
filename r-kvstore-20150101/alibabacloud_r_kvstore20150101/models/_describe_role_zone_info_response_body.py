# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeRoleZoneInfoResponseBody(DaraModel):
    def __init__(
        self,
        node: main_models.DescribeRoleZoneInfoResponseBodyNode = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.node = node
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node is not None:
            result['Node'] = self.node.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Node') is not None:
            temp_model = main_models.DescribeRoleZoneInfoResponseBodyNode()
            self.node = temp_model.from_map(m.get('Node'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRoleZoneInfoResponseBodyNode(DaraModel):
    def __init__(
        self,
        node_info: List[main_models.DescribeRoleZoneInfoResponseBodyNodeNodeInfo] = None,
    ):
        self.node_info = node_info

    def validate(self):
        if self.node_info:
            for v1 in self.node_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k1 in self.node_info:
                result['NodeInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k1 in m.get('NodeInfo'):
                temp_model = main_models.DescribeRoleZoneInfoResponseBodyNodeNodeInfo()
                self.node_info.append(temp_model.from_map(k1))

        return self

class DescribeRoleZoneInfoResponseBodyNodeNodeInfo(DaraModel):
    def __init__(
        self,
        current_band_width: int = None,
        current_minor_version: str = None,
        custins_id: str = None,
        default_band_width: int = None,
        ins_name: str = None,
        ins_type: int = None,
        is_latest_version: int = None,
        is_open_band_width_service: bool = None,
        node_id: str = None,
        node_type: str = None,
        role: str = None,
        zone_id: str = None,
    ):
        self.current_band_width = current_band_width
        self.current_minor_version = current_minor_version
        self.custins_id = custins_id
        self.default_band_width = default_band_width
        self.ins_name = ins_name
        self.ins_type = ins_type
        self.is_latest_version = is_latest_version
        self.is_open_band_width_service = is_open_band_width_service
        self.node_id = node_id
        self.node_type = node_type
        self.role = role
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width

        if self.current_minor_version is not None:
            result['CurrentMinorVersion'] = self.current_minor_version

        if self.custins_id is not None:
            result['CustinsId'] = self.custins_id

        if self.default_band_width is not None:
            result['DefaultBandWidth'] = self.default_band_width

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        if self.ins_type is not None:
            result['InsType'] = self.ins_type

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        if self.is_open_band_width_service is not None:
            result['IsOpenBandWidthService'] = self.is_open_band_width_service

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.role is not None:
            result['Role'] = self.role

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')

        if m.get('CurrentMinorVersion') is not None:
            self.current_minor_version = m.get('CurrentMinorVersion')

        if m.get('CustinsId') is not None:
            self.custins_id = m.get('CustinsId')

        if m.get('DefaultBandWidth') is not None:
            self.default_band_width = m.get('DefaultBandWidth')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        if m.get('IsOpenBandWidthService') is not None:
            self.is_open_band_width_service = m.get('IsOpenBandWidthService')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

