# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribePvtzStatisticsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        cur_page: int = None,
        page_data: List[main_models.DescribePvtzStatisticsSummaryResponseBodyPageData] = None,
        page_size: int = None,
        request_id: str = None,
        total_page: int = None,
        total_size: int = None,
    ):
        self.cur_page = cur_page
        self.page_data = page_data
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_page = total_page
        self.total_size = total_size

    def validate(self):
        if self.page_data:
            for v1 in self.page_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_page is not None:
            result['CurPage'] = self.cur_page

        result['PageData'] = []
        if self.page_data is not None:
            for k1 in self.page_data:
                result['PageData'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPage') is not None:
            self.cur_page = m.get('CurPage')

        self.page_data = []
        if m.get('PageData') is not None:
            for k1 in m.get('PageData'):
                temp_model = main_models.DescribePvtzStatisticsSummaryResponseBodyPageData()
                self.page_data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribePvtzStatisticsSummaryResponseBodyPageData(DaraModel):
    def __init__(
        self,
        aggr_timestamp: int = None,
        count: int = None,
        domain_name: str = None,
        fluctuation_value: int = None,
        latency: int = None,
        line: str = None,
        module: str = None,
        previous_count: int = None,
        protocol: str = None,
        qtype: str = None,
        ratio: int = None,
        rcode: str = None,
        source_ip: str = None,
        source_isp: str = None,
        source_region: str = None,
        vpc_id: str = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        self.aggr_timestamp = aggr_timestamp
        self.count = count
        self.domain_name = domain_name
        self.fluctuation_value = fluctuation_value
        self.latency = latency
        self.line = line
        self.module = module
        self.previous_count = previous_count
        self.protocol = protocol
        self.qtype = qtype
        self.ratio = ratio
        self.rcode = rcode
        self.source_ip = source_ip
        self.source_isp = source_isp
        self.source_region = source_region
        # VPC ID。
        self.vpc_id = vpc_id
        self.zone_id = zone_id
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggr_timestamp is not None:
            result['AggrTimestamp'] = self.aggr_timestamp

        if self.count is not None:
            result['Count'] = self.count

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.fluctuation_value is not None:
            result['FluctuationValue'] = self.fluctuation_value

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.line is not None:
            result['Line'] = self.line

        if self.module is not None:
            result['Module'] = self.module

        if self.previous_count is not None:
            result['PreviousCount'] = self.previous_count

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.qtype is not None:
            result['Qtype'] = self.qtype

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.rcode is not None:
            result['Rcode'] = self.rcode

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.source_isp is not None:
            result['SourceIsp'] = self.source_isp

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggrTimestamp') is not None:
            self.aggr_timestamp = m.get('AggrTimestamp')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FluctuationValue') is not None:
            self.fluctuation_value = m.get('FluctuationValue')

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('PreviousCount') is not None:
            self.previous_count = m.get('PreviousCount')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Qtype') is not None:
            self.qtype = m.get('Qtype')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('Rcode') is not None:
            self.rcode = m.get('Rcode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SourceIsp') is not None:
            self.source_isp = m.get('SourceIsp')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

