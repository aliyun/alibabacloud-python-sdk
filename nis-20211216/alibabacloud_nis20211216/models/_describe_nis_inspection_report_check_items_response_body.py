# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class DescribeNisInspectionReportCheckItemsResponseBody(DaraModel):
    def __init__(
        self,
        check_item_list: List[main_models.DescribeNisInspectionReportCheckItemsResponseBodyCheckItemList] = None,
        inspection_report_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.check_item_list = check_item_list
        self.inspection_report_id = inspection_report_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.check_item_list:
            for v1 in self.check_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckItemList'] = []
        if self.check_item_list is not None:
            for k1 in self.check_item_list:
                result['CheckItemList'].append(k1.to_map() if k1 else None)

        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_item_list = []
        if m.get('CheckItemList') is not None:
            for k1 in m.get('CheckItemList'):
                temp_model = main_models.DescribeNisInspectionReportCheckItemsResponseBodyCheckItemList()
                self.check_item_list.append(temp_model.from_map(k1))

        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNisInspectionReportCheckItemsResponseBodyCheckItemList(DaraModel):
    def __init__(
        self,
        category_code: str = None,
        check_item_code: str = None,
        check_item_name: str = None,
        check_result_list: List[main_models.DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListCheckResultList] = None,
        description: str = None,
        description_code: str = None,
        recommendation_list: List[main_models.DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListRecommendationList] = None,
        resource_type: str = None,
    ):
        self.category_code = category_code
        self.check_item_code = check_item_code
        self.check_item_name = check_item_name
        self.check_result_list = check_result_list
        self.description = description
        self.description_code = description_code
        self.recommendation_list = recommendation_list
        self.resource_type = resource_type

    def validate(self):
        if self.check_result_list:
            for v1 in self.check_result_list:
                 if v1:
                    v1.validate()
        if self.recommendation_list:
            for v1 in self.recommendation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code

        if self.check_item_code is not None:
            result['CheckItemCode'] = self.check_item_code

        if self.check_item_name is not None:
            result['CheckItemName'] = self.check_item_name

        result['CheckResultList'] = []
        if self.check_result_list is not None:
            for k1 in self.check_result_list:
                result['CheckResultList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.description_code is not None:
            result['DescriptionCode'] = self.description_code

        result['RecommendationList'] = []
        if self.recommendation_list is not None:
            for k1 in self.recommendation_list:
                result['RecommendationList'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')

        if m.get('CheckItemCode') is not None:
            self.check_item_code = m.get('CheckItemCode')

        if m.get('CheckItemName') is not None:
            self.check_item_name = m.get('CheckItemName')

        self.check_result_list = []
        if m.get('CheckResultList') is not None:
            for k1 in m.get('CheckResultList'):
                temp_model = main_models.DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListCheckResultList()
                self.check_result_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionCode') is not None:
            self.description_code = m.get('DescriptionCode')

        self.recommendation_list = []
        if m.get('RecommendationList') is not None:
            for k1 in m.get('RecommendationList'):
                temp_model = main_models.DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListRecommendationList()
                self.recommendation_list.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListRecommendationList(DaraModel):
    def __init__(
        self,
        abnormality: str = None,
        metadata: str = None,
        reason: str = None,
        reason_code: str = None,
        recommendation_code: str = None,
        risk_level: str = None,
        suggestion: str = None,
        suggestion_code: str = None,
    ):
        self.abnormality = abnormality
        self.metadata = metadata
        self.reason = reason
        self.reason_code = reason_code
        self.recommendation_code = recommendation_code
        self.risk_level = risk_level
        self.suggestion = suggestion
        self.suggestion_code = suggestion_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormality is not None:
            result['Abnormality'] = self.abnormality

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.recommendation_code is not None:
            result['RecommendationCode'] = self.recommendation_code

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.suggestion_code is not None:
            result['SuggestionCode'] = self.suggestion_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abnormality') is not None:
            self.abnormality = m.get('Abnormality')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('RecommendationCode') is not None:
            self.recommendation_code = m.get('RecommendationCode')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('SuggestionCode') is not None:
            self.suggestion_code = m.get('SuggestionCode')

        return self

class DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListCheckResultList(DaraModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        self.count = count
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

