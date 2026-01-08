# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInternetOpenServiceResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeInternetOpenServiceResponseBodyDataList] = None,
        page_info: main_models.DescribeInternetOpenServiceResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeInternetOpenServiceResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeInternetOpenServiceResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInternetOpenServiceResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInternetOpenServiceResponseBodyDataList(DaraModel):
    def __init__(
        self,
        detail_num: int = None,
        in_bytes: int = None,
        out_bytes: int = None,
        port_list: List[str] = None,
        prob_risk: str = None,
        prob_risk_desc: str = None,
        protocol: str = None,
        public_ip_num: int = None,
        risk_level: int = None,
        risk_reason: str = None,
        service_name: int = None,
        suggest_level: int = None,
        total_bytes: int = None,
        traffic_percent_1day: str = None,
        traffic_percent_30day: str = None,
        traffic_percent_7day: str = None,
        unknown_reason: List[str] = None,
    ):
        self.detail_num = detail_num
        self.in_bytes = in_bytes
        self.out_bytes = out_bytes
        self.port_list = port_list
        self.prob_risk = prob_risk
        self.prob_risk_desc = prob_risk_desc
        self.protocol = protocol
        self.public_ip_num = public_ip_num
        self.risk_level = risk_level
        self.risk_reason = risk_reason
        self.service_name = service_name
        self.suggest_level = suggest_level
        self.total_bytes = total_bytes
        self.traffic_percent_1day = traffic_percent_1day
        self.traffic_percent_30day = traffic_percent_30day
        self.traffic_percent_7day = traffic_percent_7day
        self.unknown_reason = unknown_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_num is not None:
            result['DetailNum'] = self.detail_num

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.port_list is not None:
            result['PortList'] = self.port_list

        if self.prob_risk is not None:
            result['ProbRisk'] = self.prob_risk

        if self.prob_risk_desc is not None:
            result['ProbRiskDesc'] = self.prob_risk_desc

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.public_ip_num is not None:
            result['PublicIpNum'] = self.public_ip_num

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_reason is not None:
            result['RiskReason'] = self.risk_reason

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.suggest_level is not None:
            result['SuggestLevel'] = self.suggest_level

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.traffic_percent_1day is not None:
            result['TrafficPercent1Day'] = self.traffic_percent_1day

        if self.traffic_percent_30day is not None:
            result['TrafficPercent30Day'] = self.traffic_percent_30day

        if self.traffic_percent_7day is not None:
            result['TrafficPercent7Day'] = self.traffic_percent_7day

        if self.unknown_reason is not None:
            result['UnknownReason'] = self.unknown_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailNum') is not None:
            self.detail_num = m.get('DetailNum')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('PortList') is not None:
            self.port_list = m.get('PortList')

        if m.get('ProbRisk') is not None:
            self.prob_risk = m.get('ProbRisk')

        if m.get('ProbRiskDesc') is not None:
            self.prob_risk_desc = m.get('ProbRiskDesc')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('PublicIpNum') is not None:
            self.public_ip_num = m.get('PublicIpNum')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskReason') is not None:
            self.risk_reason = m.get('RiskReason')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SuggestLevel') is not None:
            self.suggest_level = m.get('SuggestLevel')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TrafficPercent1Day') is not None:
            self.traffic_percent_1day = m.get('TrafficPercent1Day')

        if m.get('TrafficPercent30Day') is not None:
            self.traffic_percent_30day = m.get('TrafficPercent30Day')

        if m.get('TrafficPercent7Day') is not None:
            self.traffic_percent_7day = m.get('TrafficPercent7Day')

        if m.get('UnknownReason') is not None:
            self.unknown_reason = m.get('UnknownReason')

        return self

