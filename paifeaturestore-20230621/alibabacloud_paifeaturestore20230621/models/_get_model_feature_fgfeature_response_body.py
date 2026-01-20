# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class GetModelFeatureFGFeatureResponseBody(DaraModel):
    def __init__(
        self,
        lookup_features: List[main_models.GetModelFeatureFGFeatureResponseBodyLookupFeatures] = None,
        raw_features: List[main_models.GetModelFeatureFGFeatureResponseBodyRawFeatures] = None,
        request_id: str = None,
        reserves: List[str] = None,
        sequence_features: List[main_models.GetModelFeatureFGFeatureResponseBodySequenceFeatures] = None,
    ):
        self.lookup_features = lookup_features
        self.raw_features = raw_features
        self.request_id = request_id
        self.reserves = reserves
        self.sequence_features = sequence_features

    def validate(self):
        if self.lookup_features:
            for v1 in self.lookup_features:
                 if v1:
                    v1.validate()
        if self.raw_features:
            for v1 in self.raw_features:
                 if v1:
                    v1.validate()
        if self.sequence_features:
            for v1 in self.sequence_features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LookupFeatures'] = []
        if self.lookup_features is not None:
            for k1 in self.lookup_features:
                result['LookupFeatures'].append(k1.to_map() if k1 else None)

        result['RawFeatures'] = []
        if self.raw_features is not None:
            for k1 in self.raw_features:
                result['RawFeatures'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reserves is not None:
            result['Reserves'] = self.reserves

        result['SequenceFeatures'] = []
        if self.sequence_features is not None:
            for k1 in self.sequence_features:
                result['SequenceFeatures'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lookup_features = []
        if m.get('LookupFeatures') is not None:
            for k1 in m.get('LookupFeatures'):
                temp_model = main_models.GetModelFeatureFGFeatureResponseBodyLookupFeatures()
                self.lookup_features.append(temp_model.from_map(k1))

        self.raw_features = []
        if m.get('RawFeatures') is not None:
            for k1 in m.get('RawFeatures'):
                temp_model = main_models.GetModelFeatureFGFeatureResponseBodyRawFeatures()
                self.raw_features.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Reserves') is not None:
            self.reserves = m.get('Reserves')

        self.sequence_features = []
        if m.get('SequenceFeatures') is not None:
            for k1 in m.get('SequenceFeatures'):
                temp_model = main_models.GetModelFeatureFGFeatureResponseBodySequenceFeatures()
                self.sequence_features.append(temp_model.from_map(k1))

        return self

class GetModelFeatureFGFeatureResponseBodySequenceFeatures(DaraModel):
    def __init__(
        self,
        attribute_delim: str = None,
        feature_name: str = None,
        sequence_delim: str = None,
        sequence_length: int = None,
        sub_features: List[main_models.GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures] = None,
    ):
        self.attribute_delim = attribute_delim
        self.feature_name = feature_name
        self.sequence_delim = sequence_delim
        self.sequence_length = sequence_length
        self.sub_features = sub_features

    def validate(self):
        if self.sub_features:
            for v1 in self.sub_features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_delim is not None:
            result['AttributeDelim'] = self.attribute_delim

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.sequence_delim is not None:
            result['SequenceDelim'] = self.sequence_delim

        if self.sequence_length is not None:
            result['SequenceLength'] = self.sequence_length

        result['SubFeatures'] = []
        if self.sub_features is not None:
            for k1 in self.sub_features:
                result['SubFeatures'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeDelim') is not None:
            self.attribute_delim = m.get('AttributeDelim')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('SequenceDelim') is not None:
            self.sequence_delim = m.get('SequenceDelim')

        if m.get('SequenceLength') is not None:
            self.sequence_length = m.get('SequenceLength')

        self.sub_features = []
        if m.get('SubFeatures') is not None:
            for k1 in m.get('SubFeatures'):
                temp_model = main_models.GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures()
                self.sub_features.append(temp_model.from_map(k1))

        return self

class GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        feature_domain: str = None,
        feature_name: str = None,
        feature_type: str = None,
        input_feature_name: str = None,
        value_type: str = None,
    ):
        self.default_value = default_value
        self.feature_domain = feature_domain
        self.feature_name = feature_name
        self.feature_type = feature_type
        self.input_feature_name = input_feature_name
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class GetModelFeatureFGFeatureResponseBodyRawFeatures(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        feature_domain: str = None,
        feature_name: str = None,
        feature_type: str = None,
        input_feature_name: str = None,
        value_type: str = None,
    ):
        self.default_value = default_value
        self.feature_domain = feature_domain
        self.feature_name = feature_name
        self.feature_type = feature_type
        self.input_feature_name = input_feature_name
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class GetModelFeatureFGFeatureResponseBodyLookupFeatures(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        feature_name: str = None,
        key_feature_domain: str = None,
        key_feature_name: str = None,
        map_feature_domain: str = None,
        map_feature_name: str = None,
        value_type: str = None,
    ):
        self.default_value = default_value
        self.feature_name = feature_name
        self.key_feature_domain = key_feature_domain
        self.key_feature_name = key_feature_name
        self.map_feature_domain = map_feature_domain
        self.map_feature_name = map_feature_name
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.key_feature_domain is not None:
            result['KeyFeatureDomain'] = self.key_feature_domain

        if self.key_feature_name is not None:
            result['KeyFeatureName'] = self.key_feature_name

        if self.map_feature_domain is not None:
            result['MapFeatureDomain'] = self.map_feature_domain

        if self.map_feature_name is not None:
            result['MapFeatureName'] = self.map_feature_name

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('KeyFeatureDomain') is not None:
            self.key_feature_domain = m.get('KeyFeatureDomain')

        if m.get('KeyFeatureName') is not None:
            self.key_feature_name = m.get('KeyFeatureName')

        if m.get('MapFeatureDomain') is not None:
            self.map_feature_domain = m.get('MapFeatureDomain')

        if m.get('MapFeatureName') is not None:
            self.map_feature_name = m.get('MapFeatureName')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

