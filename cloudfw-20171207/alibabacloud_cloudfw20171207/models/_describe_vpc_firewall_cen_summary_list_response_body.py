# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallCenSummaryListResponseBody(DaraModel):
    def __init__(
        self,
        cen_list: List[main_models.DescribeVpcFirewallCenSummaryListResponseBodyCenList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cen_list = cen_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.cen_list:
            for v1 in self.cen_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CenList'] = []
        if self.cen_list is not None:
            for k1 in self.cen_list:
                result['CenList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_list = []
        if m.get('CenList') is not None:
            for k1 in m.get('CenList'):
                temp_model = main_models.DescribeVpcFirewallCenSummaryListResponseBodyCenList()
                self.cen_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcFirewallCenSummaryListResponseBodyCenList(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_name: str = None,
        region_no_list: List[str] = None,
    ):
        self.cen_id = cen_id
        self.cen_name = cen_name
        self.region_no_list = region_no_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_name is not None:
            result['CenName'] = self.cen_name

        if self.region_no_list is not None:
            result['RegionNoList'] = self.region_no_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')

        if m.get('RegionNoList') is not None:
            self.region_no_list = m.get('RegionNoList')

        return self

