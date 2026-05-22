# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeDistributionProductsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        results: List[main_models.DescribeDistributionProductsResponseBodyResults] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.results = results
        self.total_count = total_count

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DescribeDistributionProductsResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDistributionProductsResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        first_category_name: str = None,
        image_url: str = None,
        name: str = None,
        price: str = None,
        score: str = None,
        second_category_name: str = None,
        short_description: str = None,
        submission_radio: str = None,
        supplier_name: str = None,
        supplier_uid: str = None,
        trade_count: str = None,
        type: str = None,
        user_comment_count: str = None,
    ):
        self.code = code
        self.first_category_name = first_category_name
        self.image_url = image_url
        self.name = name
        self.price = price
        self.score = score
        self.second_category_name = second_category_name
        self.short_description = short_description
        self.submission_radio = submission_radio
        self.supplier_name = supplier_name
        self.supplier_uid = supplier_uid
        self.trade_count = trade_count
        self.type = type
        self.user_comment_count = user_comment_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.first_category_name is not None:
            result['FirstCategoryName'] = self.first_category_name

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.name is not None:
            result['Name'] = self.name

        if self.price is not None:
            result['Price'] = self.price

        if self.score is not None:
            result['Score'] = self.score

        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name

        if self.short_description is not None:
            result['ShortDescription'] = self.short_description

        if self.submission_radio is not None:
            result['SubmissionRadio'] = self.submission_radio

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_uid is not None:
            result['SupplierUId'] = self.supplier_uid

        if self.trade_count is not None:
            result['TradeCount'] = self.trade_count

        if self.type is not None:
            result['Type'] = self.type

        if self.user_comment_count is not None:
            result['UserCommentCount'] = self.user_comment_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('FirstCategoryName') is not None:
            self.first_category_name = m.get('FirstCategoryName')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')

        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')

        if m.get('SubmissionRadio') is not None:
            self.submission_radio = m.get('SubmissionRadio')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierUId') is not None:
            self.supplier_uid = m.get('SupplierUId')

        if m.get('TradeCount') is not None:
            self.trade_count = m.get('TradeCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserCommentCount') is not None:
            self.user_comment_count = m.get('UserCommentCount')

        return self

