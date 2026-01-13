# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ReportSampleConsistencyJobResponseBody(DaraModel):
    def __init__(
        self,
        features_difference: List[main_models.ReportSampleConsistencyJobResponseBodyFeaturesDifference] = None,
        reply_table_features: int = None,
        reply_table_lost_features: int = None,
        request_id: int = None,
        sample_table_features: int = None,
        sample_table_lost_features: int = None,
    ):
        self.features_difference = features_difference
        self.reply_table_features = reply_table_features
        self.reply_table_lost_features = reply_table_lost_features
        self.request_id = request_id
        self.sample_table_features = sample_table_features
        self.sample_table_lost_features = sample_table_lost_features

    def validate(self):
        if self.features_difference:
            for v1 in self.features_difference:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeaturesDifference'] = []
        if self.features_difference is not None:
            for k1 in self.features_difference:
                result['FeaturesDifference'].append(k1.to_map() if k1 else None)

        if self.reply_table_features is not None:
            result['ReplyTableFeatures'] = self.reply_table_features

        if self.reply_table_lost_features is not None:
            result['ReplyTableLostFeatures'] = self.reply_table_lost_features

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sample_table_features is not None:
            result['SampleTableFeatures'] = self.sample_table_features

        if self.sample_table_lost_features is not None:
            result['SampleTableLostFeatures'] = self.sample_table_lost_features

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features_difference = []
        if m.get('FeaturesDifference') is not None:
            for k1 in m.get('FeaturesDifference'):
                temp_model = main_models.ReportSampleConsistencyJobResponseBodyFeaturesDifference()
                self.features_difference.append(temp_model.from_map(k1))

        if m.get('ReplyTableFeatures') is not None:
            self.reply_table_features = m.get('ReplyTableFeatures')

        if m.get('ReplyTableLostFeatures') is not None:
            self.reply_table_lost_features = m.get('ReplyTableLostFeatures')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SampleTableFeatures') is not None:
            self.sample_table_features = m.get('SampleTableFeatures')

        if m.get('SampleTableLostFeatures') is not None:
            self.sample_table_lost_features = m.get('SampleTableLostFeatures')

        return self

class ReportSampleConsistencyJobResponseBodyFeaturesDifference(DaraModel):
    def __init__(
        self,
        count: int = None,
        feature_name: str = None,
        feature_type: str = None,
        ratio: str = None,
    ):
        self.count = count
        self.feature_name = feature_name
        self.feature_type = feature_type
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        return self

