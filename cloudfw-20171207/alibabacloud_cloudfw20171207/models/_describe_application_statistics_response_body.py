# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        category_list: List[main_models.DescribeApplicationStatisticsResponseBodyCategoryList] = None,
        request_id: str = None,
        risk_list: List[main_models.DescribeApplicationStatisticsResponseBodyRiskList] = None,
        technology_list: List[main_models.DescribeApplicationStatisticsResponseBodyTechnologyList] = None,
    ):
        # The list of application counts grouped by application category.
        self.category_list = category_list
        # The request ID.
        self.request_id = request_id
        # The list of application counts grouped by risk level.
        self.risk_list = risk_list
        # The list of application counts grouped by technology type.
        self.technology_list = technology_list

    def validate(self):
        if self.category_list:
            for v1 in self.category_list:
                 if v1:
                    v1.validate()
        if self.risk_list:
            for v1 in self.risk_list:
                 if v1:
                    v1.validate()
        if self.technology_list:
            for v1 in self.technology_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CategoryList'] = []
        if self.category_list is not None:
            for k1 in self.category_list:
                result['CategoryList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskList'] = []
        if self.risk_list is not None:
            for k1 in self.risk_list:
                result['RiskList'].append(k1.to_map() if k1 else None)

        result['TechnologyList'] = []
        if self.technology_list is not None:
            for k1 in self.technology_list:
                result['TechnologyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_list = []
        if m.get('CategoryList') is not None:
            for k1 in m.get('CategoryList'):
                temp_model = main_models.DescribeApplicationStatisticsResponseBodyCategoryList()
                self.category_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_list = []
        if m.get('RiskList') is not None:
            for k1 in m.get('RiskList'):
                temp_model = main_models.DescribeApplicationStatisticsResponseBodyRiskList()
                self.risk_list.append(temp_model.from_map(k1))

        self.technology_list = []
        if m.get('TechnologyList') is not None:
            for k1 in m.get('TechnologyList'):
                temp_model = main_models.DescribeApplicationStatisticsResponseBodyTechnologyList()
                self.technology_list.append(temp_model.from_map(k1))

        return self

class DescribeApplicationStatisticsResponseBodyTechnologyList(DaraModel):
    def __init__(
        self,
        application_count: int = None,
        technology: str = None,
    ):
        # The number of applications of the technology type.
        self.application_count = application_count
        # The name of the technology type. The name is returned in Chinese or English based on the Lang parameter.
        self.technology = technology

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_count is not None:
            result['ApplicationCount'] = self.application_count

        if self.technology is not None:
            result['Technology'] = self.technology

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCount') is not None:
            self.application_count = m.get('ApplicationCount')

        if m.get('Technology') is not None:
            self.technology = m.get('Technology')

        return self

class DescribeApplicationStatisticsResponseBodyRiskList(DaraModel):
    def __init__(
        self,
        application_count: int = None,
        risk: str = None,
    ):
        # The number of applications at the risk level.
        self.application_count = application_count
        # The risk level. Valid values:
        # - **Information**: Informational.
        # - **Low**: Low.
        # - **Medium**: Medium.
        # - **High**: High.
        # - **Critical**: Critical.
        self.risk = risk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_count is not None:
            result['ApplicationCount'] = self.application_count

        if self.risk is not None:
            result['Risk'] = self.risk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCount') is not None:
            self.application_count = m.get('ApplicationCount')

        if m.get('Risk') is not None:
            self.risk = m.get('Risk')

        return self

class DescribeApplicationStatisticsResponseBodyCategoryList(DaraModel):
    def __init__(
        self,
        application_count: int = None,
        category_name: str = None,
    ):
        # The number of applications in the application category.
        self.application_count = application_count
        # The name of the application category. The name is returned in Chinese or English based on the Lang parameter.
        self.category_name = category_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_count is not None:
            result['ApplicationCount'] = self.application_count

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCount') is not None:
            self.application_count = m.get('ApplicationCount')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        return self

