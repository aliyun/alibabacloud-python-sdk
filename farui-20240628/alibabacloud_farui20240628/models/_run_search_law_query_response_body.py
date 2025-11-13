# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunSearchLawQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RunSearchLawQueryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.RunSearchLawQueryResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class RunSearchLawQueryResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        law_result: List[main_models.RunSearchLawQueryResponseBodyDataLawResult] = None,
        page_size: int = None,
        query: str = None,
        query_keywords: List[str] = None,
        sort_key_and_direction: main_models.RunSearchLawQueryResponseBodyDataSortKeyAndDirection = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.law_result = law_result
        self.page_size = page_size
        self.query = query
        self.query_keywords = query_keywords
        self.sort_key_and_direction = sort_key_and_direction
        self.total_count = total_count

    def validate(self):
        if self.law_result:
            for v1 in self.law_result:
                 if v1:
                    v1.validate()
        if self.sort_key_and_direction:
            self.sort_key_and_direction.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        result['lawResult'] = []
        if self.law_result is not None:
            for k1 in self.law_result:
                result['lawResult'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query is not None:
            result['query'] = self.query

        if self.query_keywords is not None:
            result['queryKeywords'] = self.query_keywords

        if self.sort_key_and_direction is not None:
            result['sortKeyAndDirection'] = self.sort_key_and_direction.to_map()

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        self.law_result = []
        if m.get('lawResult') is not None:
            for k1 in m.get('lawResult'):
                temp_model = main_models.RunSearchLawQueryResponseBodyDataLawResult()
                self.law_result.append(temp_model.from_map(k1))

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('queryKeywords') is not None:
            self.query_keywords = m.get('queryKeywords')

        if m.get('sortKeyAndDirection') is not None:
            temp_model = main_models.RunSearchLawQueryResponseBodyDataSortKeyAndDirection()
            self.sort_key_and_direction = temp_model.from_map(m.get('sortKeyAndDirection'))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class RunSearchLawQueryResponseBodyDataSortKeyAndDirection(DaraModel):
    def __init__(
        self,
        release_year_month_date: str = None,
        similarity: str = None,
    ):
        self.release_year_month_date = release_year_month_date
        self.similarity = similarity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_year_month_date is not None:
            result['releaseYearMonthDate'] = self.release_year_month_date

        if self.similarity is not None:
            result['similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('releaseYearMonthDate') is not None:
            self.release_year_month_date = m.get('releaseYearMonthDate')

        if m.get('similarity') is not None:
            self.similarity = m.get('similarity')

        return self

class RunSearchLawQueryResponseBodyDataLawResult(DaraModel):
    def __init__(
        self,
        law_domain: main_models.RunSearchLawQueryResponseBodyDataLawResultLawDomain = None,
        similarity: str = None,
    ):
        self.law_domain = law_domain
        self.similarity = similarity

    def validate(self):
        if self.law_domain:
            self.law_domain.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.law_domain is not None:
            result['lawDomain'] = self.law_domain.to_map()

        if self.similarity is not None:
            result['similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lawDomain') is not None:
            temp_model = main_models.RunSearchLawQueryResponseBodyDataLawResultLawDomain()
            self.law_domain = temp_model.from_map(m.get('lawDomain'))

        if m.get('similarity') is not None:
            self.similarity = m.get('similarity')

        return self

class RunSearchLawQueryResponseBodyDataLawResultLawDomain(DaraModel):
    def __init__(
        self,
        abolition_basis: str = None,
        implement_year_month_date: str = None,
        invalid_basis: str = None,
        issuing_no: str = None,
        issuing_organ: str = None,
        law_id: str = None,
        law_item_id: str = None,
        law_name: str = None,
        law_order: str = None,
        law_source_content: str = None,
        law_title: str = None,
        modify_basis: str = None,
        potency_level: str = None,
        release_year_month_date: str = None,
        thematic_classify: str = None,
        timeliness: str = None,
    ):
        self.abolition_basis = abolition_basis
        self.implement_year_month_date = implement_year_month_date
        self.invalid_basis = invalid_basis
        self.issuing_no = issuing_no
        self.issuing_organ = issuing_organ
        self.law_id = law_id
        self.law_item_id = law_item_id
        self.law_name = law_name
        self.law_order = law_order
        self.law_source_content = law_source_content
        self.law_title = law_title
        self.modify_basis = modify_basis
        self.potency_level = potency_level
        self.release_year_month_date = release_year_month_date
        self.thematic_classify = thematic_classify
        self.timeliness = timeliness

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abolition_basis is not None:
            result['abolitionBasis'] = self.abolition_basis

        if self.implement_year_month_date is not None:
            result['implementYearMonthDate'] = self.implement_year_month_date

        if self.invalid_basis is not None:
            result['invalidBasis'] = self.invalid_basis

        if self.issuing_no is not None:
            result['issuingNo'] = self.issuing_no

        if self.issuing_organ is not None:
            result['issuingOrgan'] = self.issuing_organ

        if self.law_id is not None:
            result['lawId'] = self.law_id

        if self.law_item_id is not None:
            result['lawItemId'] = self.law_item_id

        if self.law_name is not None:
            result['lawName'] = self.law_name

        if self.law_order is not None:
            result['lawOrder'] = self.law_order

        if self.law_source_content is not None:
            result['lawSourceContent'] = self.law_source_content

        if self.law_title is not None:
            result['lawTitle'] = self.law_title

        if self.modify_basis is not None:
            result['modifyBasis'] = self.modify_basis

        if self.potency_level is not None:
            result['potencyLevel'] = self.potency_level

        if self.release_year_month_date is not None:
            result['releaseYearMonthDate'] = self.release_year_month_date

        if self.thematic_classify is not None:
            result['thematicClassify'] = self.thematic_classify

        if self.timeliness is not None:
            result['timeliness'] = self.timeliness

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abolitionBasis') is not None:
            self.abolition_basis = m.get('abolitionBasis')

        if m.get('implementYearMonthDate') is not None:
            self.implement_year_month_date = m.get('implementYearMonthDate')

        if m.get('invalidBasis') is not None:
            self.invalid_basis = m.get('invalidBasis')

        if m.get('issuingNo') is not None:
            self.issuing_no = m.get('issuingNo')

        if m.get('issuingOrgan') is not None:
            self.issuing_organ = m.get('issuingOrgan')

        if m.get('lawId') is not None:
            self.law_id = m.get('lawId')

        if m.get('lawItemId') is not None:
            self.law_item_id = m.get('lawItemId')

        if m.get('lawName') is not None:
            self.law_name = m.get('lawName')

        if m.get('lawOrder') is not None:
            self.law_order = m.get('lawOrder')

        if m.get('lawSourceContent') is not None:
            self.law_source_content = m.get('lawSourceContent')

        if m.get('lawTitle') is not None:
            self.law_title = m.get('lawTitle')

        if m.get('modifyBasis') is not None:
            self.modify_basis = m.get('modifyBasis')

        if m.get('potencyLevel') is not None:
            self.potency_level = m.get('potencyLevel')

        if m.get('releaseYearMonthDate') is not None:
            self.release_year_month_date = m.get('releaseYearMonthDate')

        if m.get('thematicClassify') is not None:
            self.thematic_classify = m.get('thematicClassify')

        if m.get('timeliness') is not None:
            self.timeliness = m.get('timeliness')

        return self

