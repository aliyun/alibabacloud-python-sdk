# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInternetOpenDetailRequest(DaraModel):
    def __init__(
        self,
        assets_instance_id: str = None,
        assets_instance_name: str = None,
        assets_type: str = None,
        current_page: str = None,
        end_time: str = None,
        lang: str = None,
        page_size: str = None,
        port: str = None,
        public_ip: str = None,
        region_no: str = None,
        risk_level: str = None,
        service_name: str = None,
        service_name_fuzzy: str = None,
        sort_list: List[main_models.DescribeInternetOpenDetailRequestSortList] = None,
        source_ip: str = None,
        start_time: str = None,
        suggest_level: str = None,
    ):
        self.assets_instance_id = assets_instance_id
        self.assets_instance_name = assets_instance_name
        self.assets_type = assets_type
        self.current_page = current_page
        self.end_time = end_time
        self.lang = lang
        self.page_size = page_size
        self.port = port
        self.public_ip = public_ip
        self.region_no = region_no
        self.risk_level = risk_level
        self.service_name = service_name
        self.service_name_fuzzy = service_name_fuzzy
        self.sort_list = sort_list
        self.source_ip = source_ip
        self.start_time = start_time
        self.suggest_level = suggest_level

    def validate(self):
        if self.sort_list:
            for v1 in self.sort_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id

        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name

        if self.assets_type is not None:
            result['AssetsType'] = self.assets_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_name_fuzzy is not None:
            result['ServiceNameFuzzy'] = self.service_name_fuzzy

        result['SortList'] = []
        if self.sort_list is not None:
            for k1 in self.sort_list:
                result['SortList'].append(k1.to_map() if k1 else None)

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.suggest_level is not None:
            result['SuggestLevel'] = self.suggest_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')

        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')

        if m.get('AssetsType') is not None:
            self.assets_type = m.get('AssetsType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceNameFuzzy') is not None:
            self.service_name_fuzzy = m.get('ServiceNameFuzzy')

        self.sort_list = []
        if m.get('SortList') is not None:
            for k1 in m.get('SortList'):
                temp_model = main_models.DescribeInternetOpenDetailRequestSortList()
                self.sort_list.append(temp_model.from_map(k1))

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SuggestLevel') is not None:
            self.suggest_level = m.get('SuggestLevel')

        return self

class DescribeInternetOpenDetailRequestSortList(DaraModel):
    def __init__(
        self,
        dir: str = None,
        sort_key: str = None,
    ):
        self.dir = dir
        self.sort_key = sort_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dir is not None:
            result['Dir'] = self.dir

        if self.sort_key is not None:
            result['SortKey'] = self.sort_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')

        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')

        return self

