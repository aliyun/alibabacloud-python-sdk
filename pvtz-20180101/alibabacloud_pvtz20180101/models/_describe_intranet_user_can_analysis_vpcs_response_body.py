# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeIntranetUserCanAnalysisVpcsResponseBody(DaraModel):
    def __init__(
        self,
        cur_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_page: int = None,
        total_size: int = None,
        user_can_analysis_vpcs_pop_results: main_models.DescribeIntranetUserCanAnalysisVpcsResponseBodyUserCanAnalysisVpcsPopResults = None,
    ):
        self.cur_page = cur_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_page = total_page
        self.total_size = total_size
        self.user_can_analysis_vpcs_pop_results = user_can_analysis_vpcs_pop_results

    def validate(self):
        if self.user_can_analysis_vpcs_pop_results:
            self.user_can_analysis_vpcs_pop_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_page is not None:
            result['CurPage'] = self.cur_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        if self.user_can_analysis_vpcs_pop_results is not None:
            result['UserCanAnalysisVpcsPopResults'] = self.user_can_analysis_vpcs_pop_results.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPage') is not None:
            self.cur_page = m.get('CurPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        if m.get('UserCanAnalysisVpcsPopResults') is not None:
            temp_model = main_models.DescribeIntranetUserCanAnalysisVpcsResponseBodyUserCanAnalysisVpcsPopResults()
            self.user_can_analysis_vpcs_pop_results = temp_model.from_map(m.get('UserCanAnalysisVpcsPopResults'))

        return self

class DescribeIntranetUserCanAnalysisVpcsResponseBodyUserCanAnalysisVpcsPopResults(DaraModel):
    def __init__(
        self,
        user_can_analysis_vpcs_pop_result: List[main_models.DescribeIntranetUserCanAnalysisVpcsResponseBodyUserCanAnalysisVpcsPopResultsUserCanAnalysisVpcsPopResult] = None,
    ):
        self.user_can_analysis_vpcs_pop_result = user_can_analysis_vpcs_pop_result

    def validate(self):
        if self.user_can_analysis_vpcs_pop_result:
            for v1 in self.user_can_analysis_vpcs_pop_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserCanAnalysisVpcsPopResult'] = []
        if self.user_can_analysis_vpcs_pop_result is not None:
            for k1 in self.user_can_analysis_vpcs_pop_result:
                result['UserCanAnalysisVpcsPopResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_can_analysis_vpcs_pop_result = []
        if m.get('UserCanAnalysisVpcsPopResult') is not None:
            for k1 in m.get('UserCanAnalysisVpcsPopResult'):
                temp_model = main_models.DescribeIntranetUserCanAnalysisVpcsResponseBodyUserCanAnalysisVpcsPopResultsUserCanAnalysisVpcsPopResult()
                self.user_can_analysis_vpcs_pop_result.append(temp_model.from_map(k1))

        return self

class DescribeIntranetUserCanAnalysisVpcsResponseBodyUserCanAnalysisVpcsPopResultsUserCanAnalysisVpcsPopResult(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        authorized_user_id: int = None,
        network_type: str = None,
        region_id: str = None,
        tree_level: int = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        self.auth_type = auth_type
        self.authorized_user_id = authorized_user_id
        self.network_type = network_type
        self.region_id = region_id
        self.tree_level = tree_level
        self.vpc_id = vpc_id
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tree_level is not None:
            result['TreeLevel'] = self.tree_level

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TreeLevel') is not None:
            self.tree_level = m.get('TreeLevel')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

