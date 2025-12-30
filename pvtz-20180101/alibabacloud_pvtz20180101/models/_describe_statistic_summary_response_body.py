# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeStatisticSummaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vpc_request_tops: main_models.DescribeStatisticSummaryResponseBodyVpcRequestTops = None,
        zone_request_tops: main_models.DescribeStatisticSummaryResponseBodyZoneRequestTops = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The top three VPCs with the largest number of DNS requests.
        self.vpc_request_tops = vpc_request_tops
        # The top three zones with the largest number of DNS requests.
        self.zone_request_tops = zone_request_tops

    def validate(self):
        if self.vpc_request_tops:
            self.vpc_request_tops.validate()
        if self.zone_request_tops:
            self.zone_request_tops.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpc_request_tops is not None:
            result['VpcRequestTops'] = self.vpc_request_tops.to_map()

        if self.zone_request_tops is not None:
            result['ZoneRequestTops'] = self.zone_request_tops.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VpcRequestTops') is not None:
            temp_model = main_models.DescribeStatisticSummaryResponseBodyVpcRequestTops()
            self.vpc_request_tops = temp_model.from_map(m.get('VpcRequestTops'))

        if m.get('ZoneRequestTops') is not None:
            temp_model = main_models.DescribeStatisticSummaryResponseBodyZoneRequestTops()
            self.zone_request_tops = temp_model.from_map(m.get('ZoneRequestTops'))

        return self

class DescribeStatisticSummaryResponseBodyZoneRequestTops(DaraModel):
    def __init__(
        self,
        zone_request_top: List[main_models.DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop] = None,
    ):
        self.zone_request_top = zone_request_top

    def validate(self):
        if self.zone_request_top:
            for v1 in self.zone_request_top:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ZoneRequestTop'] = []
        if self.zone_request_top is not None:
            for k1 in self.zone_request_top:
                result['ZoneRequestTop'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone_request_top = []
        if m.get('ZoneRequestTop') is not None:
            for k1 in m.get('ZoneRequestTop'):
                temp_model = main_models.DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop()
                self.zone_request_top.append(temp_model.from_map(k1))

        return self

class DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        request_count: int = None,
        zone_name: str = None,
    ):
        # The business type. Valid values:
        # 
        # *   AUTH_ZONE: authoritative zone
        # *   RESOLVER_RULE: forwarding rule
        # *   INBOUND: inbound endpoint
        self.biz_type = biz_type
        # The number of DNS requests on the previous day.
        self.request_count = request_count
        # The zone name.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.request_count is not None:
            result['RequestCount'] = self.request_count

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

class DescribeStatisticSummaryResponseBodyVpcRequestTops(DaraModel):
    def __init__(
        self,
        vpc_request_top: List[main_models.DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop] = None,
    ):
        self.vpc_request_top = vpc_request_top

    def validate(self):
        if self.vpc_request_top:
            for v1 in self.vpc_request_top:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VpcRequestTop'] = []
        if self.vpc_request_top is not None:
            for k1 in self.vpc_request_top:
                result['VpcRequestTop'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_request_top = []
        if m.get('VpcRequestTop') is not None:
            for k1 in m.get('VpcRequestTop'):
                temp_model = main_models.DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop()
                self.vpc_request_top.append(temp_model.from_map(k1))

        return self

class DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        request_count: int = None,
        tunnel_id: str = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The name of the region.
        self.region_name = region_name
        # The number of DNS requests on the previous day.
        self.request_count = request_count
        # The tunnel ID.
        self.tunnel_id = tunnel_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
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

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.request_count is not None:
            result['RequestCount'] = self.request_count

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

