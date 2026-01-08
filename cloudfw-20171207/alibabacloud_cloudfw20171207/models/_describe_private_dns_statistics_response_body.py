# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribePrivateDnsStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        abnormal_private_dns_count: int = None,
        created_private_dns_count: int = None,
        domain_name_total_count: int = None,
        new_domain_name_total_count: int = None,
        normal_private_dns_count: int = None,
        private_dns_region_list: List[main_models.DescribePrivateDnsStatisticsResponseBodyPrivateDnsRegionList] = None,
        request_id: str = None,
    ):
        self.abnormal_private_dns_count = abnormal_private_dns_count
        self.created_private_dns_count = created_private_dns_count
        self.domain_name_total_count = domain_name_total_count
        self.new_domain_name_total_count = new_domain_name_total_count
        self.normal_private_dns_count = normal_private_dns_count
        self.private_dns_region_list = private_dns_region_list
        self.request_id = request_id

    def validate(self):
        if self.private_dns_region_list:
            for v1 in self.private_dns_region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_private_dns_count is not None:
            result['AbnormalPrivateDnsCount'] = self.abnormal_private_dns_count

        if self.created_private_dns_count is not None:
            result['CreatedPrivateDnsCount'] = self.created_private_dns_count

        if self.domain_name_total_count is not None:
            result['DomainNameTotalCount'] = self.domain_name_total_count

        if self.new_domain_name_total_count is not None:
            result['NewDomainNameTotalCount'] = self.new_domain_name_total_count

        if self.normal_private_dns_count is not None:
            result['NormalPrivateDnsCount'] = self.normal_private_dns_count

        result['PrivateDnsRegionList'] = []
        if self.private_dns_region_list is not None:
            for k1 in self.private_dns_region_list:
                result['PrivateDnsRegionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalPrivateDnsCount') is not None:
            self.abnormal_private_dns_count = m.get('AbnormalPrivateDnsCount')

        if m.get('CreatedPrivateDnsCount') is not None:
            self.created_private_dns_count = m.get('CreatedPrivateDnsCount')

        if m.get('DomainNameTotalCount') is not None:
            self.domain_name_total_count = m.get('DomainNameTotalCount')

        if m.get('NewDomainNameTotalCount') is not None:
            self.new_domain_name_total_count = m.get('NewDomainNameTotalCount')

        if m.get('NormalPrivateDnsCount') is not None:
            self.normal_private_dns_count = m.get('NormalPrivateDnsCount')

        self.private_dns_region_list = []
        if m.get('PrivateDnsRegionList') is not None:
            for k1 in m.get('PrivateDnsRegionList'):
                temp_model = main_models.DescribePrivateDnsStatisticsResponseBodyPrivateDnsRegionList()
                self.private_dns_region_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePrivateDnsStatisticsResponseBodyPrivateDnsRegionList(DaraModel):
    def __init__(
        self,
        domain_name_count: int = None,
        new_domain_name_count: int = None,
        private_dns_count: int = None,
        region_no: str = None,
    ):
        self.domain_name_count = domain_name_count
        self.new_domain_name_count = new_domain_name_count
        self.private_dns_count = private_dns_count
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name_count is not None:
            result['DomainNameCount'] = self.domain_name_count

        if self.new_domain_name_count is not None:
            result['NewDomainNameCount'] = self.new_domain_name_count

        if self.private_dns_count is not None:
            result['PrivateDnsCount'] = self.private_dns_count

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNameCount') is not None:
            self.domain_name_count = m.get('DomainNameCount')

        if m.get('NewDomainNameCount') is not None:
            self.new_domain_name_count = m.get('NewDomainNameCount')

        if m.get('PrivateDnsCount') is not None:
            self.private_dns_count = m.get('PrivateDnsCount')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

