# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class QuerySampleConsistencyJobDifferenceResponseBody(DaraModel):
    def __init__(
        self,
        difference_histogram: List[main_models.QuerySampleConsistencyJobDifferenceResponseBodyDifferenceHistogram] = None,
        number_feature_differences: List[main_models.QuerySampleConsistencyJobDifferenceResponseBodyNumberFeatureDifferences] = None,
        request_id: str = None,
        string_feature_differences: List[main_models.QuerySampleConsistencyJobDifferenceResponseBodyStringFeatureDifferences] = None,
    ):
        self.difference_histogram = difference_histogram
        self.number_feature_differences = number_feature_differences
        self.request_id = request_id
        self.string_feature_differences = string_feature_differences

    def validate(self):
        if self.difference_histogram:
            for v1 in self.difference_histogram:
                 if v1:
                    v1.validate()
        if self.number_feature_differences:
            for v1 in self.number_feature_differences:
                 if v1:
                    v1.validate()
        if self.string_feature_differences:
            for v1 in self.string_feature_differences:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DifferenceHistogram'] = []
        if self.difference_histogram is not None:
            for k1 in self.difference_histogram:
                result['DifferenceHistogram'].append(k1.to_map() if k1 else None)

        result['NumberFeatureDifferences'] = []
        if self.number_feature_differences is not None:
            for k1 in self.number_feature_differences:
                result['NumberFeatureDifferences'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StringFeatureDifferences'] = []
        if self.string_feature_differences is not None:
            for k1 in self.string_feature_differences:
                result['StringFeatureDifferences'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.difference_histogram = []
        if m.get('DifferenceHistogram') is not None:
            for k1 in m.get('DifferenceHistogram'):
                temp_model = main_models.QuerySampleConsistencyJobDifferenceResponseBodyDifferenceHistogram()
                self.difference_histogram.append(temp_model.from_map(k1))

        self.number_feature_differences = []
        if m.get('NumberFeatureDifferences') is not None:
            for k1 in m.get('NumberFeatureDifferences'):
                temp_model = main_models.QuerySampleConsistencyJobDifferenceResponseBodyNumberFeatureDifferences()
                self.number_feature_differences.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.string_feature_differences = []
        if m.get('StringFeatureDifferences') is not None:
            for k1 in m.get('StringFeatureDifferences'):
                temp_model = main_models.QuerySampleConsistencyJobDifferenceResponseBodyStringFeatureDifferences()
                self.string_feature_differences.append(temp_model.from_map(k1))

        return self

class QuerySampleConsistencyJobDifferenceResponseBodyStringFeatureDifferences(DaraModel):
    def __init__(
        self,
        item_id: str = None,
        reply_table_feature_value: str = None,
        request_id: str = None,
        sample_table_feature_value: str = None,
        user_id: str = None,
    ):
        self.item_id = item_id
        self.reply_table_feature_value = reply_table_feature_value
        self.request_id = request_id
        self.sample_table_feature_value = sample_table_feature_value
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.reply_table_feature_value is not None:
            result['ReplyTableFeatureValue'] = self.reply_table_feature_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sample_table_feature_value is not None:
            result['SampleTableFeatureValue'] = self.sample_table_feature_value

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ReplyTableFeatureValue') is not None:
            self.reply_table_feature_value = m.get('ReplyTableFeatureValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SampleTableFeatureValue') is not None:
            self.sample_table_feature_value = m.get('SampleTableFeatureValue')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QuerySampleConsistencyJobDifferenceResponseBodyNumberFeatureDifferences(DaraModel):
    def __init__(
        self,
        diff_value: float = None,
        item_id: str = None,
        reply_table_feature_value: float = None,
        request_id: str = None,
        sample_table_feature_value: float = None,
        user_id: str = None,
    ):
        self.diff_value = diff_value
        self.item_id = item_id
        self.reply_table_feature_value = reply_table_feature_value
        self.request_id = request_id
        self.sample_table_feature_value = sample_table_feature_value
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diff_value is not None:
            result['DiffValue'] = self.diff_value

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.reply_table_feature_value is not None:
            result['ReplyTableFeatureValue'] = self.reply_table_feature_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sample_table_feature_value is not None:
            result['SampleTableFeatureValue'] = self.sample_table_feature_value

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiffValue') is not None:
            self.diff_value = m.get('DiffValue')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ReplyTableFeatureValue') is not None:
            self.reply_table_feature_value = m.get('ReplyTableFeatureValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SampleTableFeatureValue') is not None:
            self.sample_table_feature_value = m.get('SampleTableFeatureValue')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QuerySampleConsistencyJobDifferenceResponseBodyDifferenceHistogram(DaraModel):
    def __init__(
        self,
        abscissa: str = None,
        value: int = None,
    ):
        self.abscissa = abscissa
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abscissa is not None:
            result['Abscissa'] = self.abscissa

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abscissa') is not None:
            self.abscissa = m.get('Abscissa')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

