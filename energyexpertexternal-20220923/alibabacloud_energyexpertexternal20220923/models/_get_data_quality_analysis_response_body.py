# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetDataQualityAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataQualityAnalysisResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetDataQualityAnalysisResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDataQualityAnalysisResponseBodyData(DaraModel):
    def __init__(
        self,
        data_quality: List[main_models.GetDataQualityAnalysisResponseBodyDataDataQuality] = None,
        data_quality_result: main_models.GetDataQualityAnalysisResponseBodyDataDataQualityResult = None,
        sensitivity_list: List[main_models.GetDataQualityAnalysisResponseBodyDataSensitivityList] = None,
        uncertainty: str = None,
        uncertainty_values: List[main_models.GetDataQualityAnalysisResponseBodyDataUncertaintyValues] = None,
    ):
        # Score of each inventory.
        self.data_quality = data_quality
        # Data quality result.
        self.data_quality_result = data_quality_result
        # Sensitivity analysis list
        self.sensitivity_list = sensitivity_list
        # Uncertainty value. The model\\"s overall percentage uncertainty results. "10.00%" symbolizes a 10.00% uncertainty, indicating that the carbon footprint lies within ±10.00%. This is derived from a weighted aggregation of individual inventory uncertainties.
        self.uncertainty = uncertainty
        # Uncertainty list
        self.uncertainty_values = uncertainty_values

    def validate(self):
        if self.data_quality:
            for v1 in self.data_quality:
                 if v1:
                    v1.validate()
        if self.data_quality_result:
            self.data_quality_result.validate()
        if self.sensitivity_list:
            for v1 in self.sensitivity_list:
                 if v1:
                    v1.validate()
        if self.uncertainty_values:
            for v1 in self.uncertainty_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dataQuality'] = []
        if self.data_quality is not None:
            for k1 in self.data_quality:
                result['dataQuality'].append(k1.to_map() if k1 else None)

        if self.data_quality_result is not None:
            result['dataQualityResult'] = self.data_quality_result.to_map()

        result['sensitivityList'] = []
        if self.sensitivity_list is not None:
            for k1 in self.sensitivity_list:
                result['sensitivityList'].append(k1.to_map() if k1 else None)

        if self.uncertainty is not None:
            result['uncertainty'] = self.uncertainty

        result['uncertaintyValues'] = []
        if self.uncertainty_values is not None:
            for k1 in self.uncertainty_values:
                result['uncertaintyValues'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality = []
        if m.get('dataQuality') is not None:
            for k1 in m.get('dataQuality'):
                temp_model = main_models.GetDataQualityAnalysisResponseBodyDataDataQuality()
                self.data_quality.append(temp_model.from_map(k1))

        if m.get('dataQualityResult') is not None:
            temp_model = main_models.GetDataQualityAnalysisResponseBodyDataDataQualityResult()
            self.data_quality_result = temp_model.from_map(m.get('dataQualityResult'))

        self.sensitivity_list = []
        if m.get('sensitivityList') is not None:
            for k1 in m.get('sensitivityList'):
                temp_model = main_models.GetDataQualityAnalysisResponseBodyDataSensitivityList()
                self.sensitivity_list.append(temp_model.from_map(k1))

        if m.get('uncertainty') is not None:
            self.uncertainty = m.get('uncertainty')

        self.uncertainty_values = []
        if m.get('uncertaintyValues') is not None:
            for k1 in m.get('uncertaintyValues'):
                temp_model = main_models.GetDataQualityAnalysisResponseBodyDataUncertaintyValues()
                self.uncertainty_values.append(temp_model.from_map(k1))

        return self

class GetDataQualityAnalysisResponseBodyDataUncertaintyValues(DaraModel):
    def __init__(
        self,
        inventory: str = None,
        uncertainty_contribution: str = None,
    ):
        # The name of the inventory. Format: process name / inventory name.
        self.inventory = inventory
        # Inventory uncertainty absolute contribution size. The impact of the quality of each inventory data on the carbon footprint results in the modeling process, when the uncertain contribution of a list is large, please improve its data quality as much as possible to improve the accuracy of carbon footprint analysis. The meaning of "1.4964" is not determined to contribute 1.4964 kgCO₂ e/unit, where unit is the unit of the product.
        self.uncertainty_contribution = uncertainty_contribution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inventory is not None:
            result['inventory'] = self.inventory

        if self.uncertainty_contribution is not None:
            result['uncertaintyContribution'] = self.uncertainty_contribution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')

        if m.get('uncertaintyContribution') is not None:
            self.uncertainty_contribution = m.get('uncertaintyContribution')

        return self

class GetDataQualityAnalysisResponseBodyDataSensitivityList(DaraModel):
    def __init__(
        self,
        id: str = None,
        inventory: str = None,
        reduction_list: List[str] = None,
        sensitivity: float = None,
    ):
        # Inventory id
        self.id = id
        # Name of the inventory item.
        self.inventory = inventory
        # List of emission reduction measures.
        self.reduction_list = reduction_list
        # Sensitivity percentage.
        self.sensitivity = sensitivity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.inventory is not None:
            result['inventory'] = self.inventory

        if self.reduction_list is not None:
            result['reductionList'] = self.reduction_list

        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')

        if m.get('reductionList') is not None:
            self.reduction_list = m.get('reductionList')

        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')

        return self

class GetDataQualityAnalysisResponseBodyDataDataQualityResult(DaraModel):
    def __init__(
        self,
        data_quality_score: float = None,
        g_1: float = None,
        g_2: float = None,
        g_3: float = None,
        g_4: float = None,
    ):
        # The score. This parameter is applicable to DQR results. The distribution ranges from 1 to 5. A value closer to 1 indicates better data quality. The number of valid digits is kept to four decimal places.
        self.data_quality_score = data_quality_score
        # Data quality evaluation indicator 1: activity data credibility.
        self.g_1 = g_1
        # Data quality evaluation indicator 2: data factor reliability.
        self.g_2 = g_2
        # Data quality evaluation indicator 3: time representativeness.
        self.g_3 = g_3
        # Data quality evaluation indicator 4: geographic representativeness.
        self.g_4 = g_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_score is not None:
            result['data_quality_score'] = self.data_quality_score

        if self.g_1 is not None:
            result['g1'] = self.g_1

        if self.g_2 is not None:
            result['g2'] = self.g_2

        if self.g_3 is not None:
            result['g3'] = self.g_3

        if self.g_4 is not None:
            result['g4'] = self.g_4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_quality_score') is not None:
            self.data_quality_score = m.get('data_quality_score')

        if m.get('g1') is not None:
            self.g_1 = m.get('g1')

        if m.get('g2') is not None:
            self.g_2 = m.get('g2')

        if m.get('g3') is not None:
            self.g_3 = m.get('g3')

        if m.get('g4') is not None:
            self.g_4 = m.get('g4')

        return self

class GetDataQualityAnalysisResponseBodyDataDataQuality(DaraModel):
    def __init__(
        self,
        inventory: str = None,
        score: main_models.GetDataQualityAnalysisResponseBodyDataDataQualityScore = None,
    ):
        # Inventory name
        self.inventory = inventory
        # Score. The distribution ranges from 1 to 5. A value closer to 1 indicates better data quality.
        self.score = score

    def validate(self):
        if self.score:
            self.score.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inventory is not None:
            result['inventory'] = self.inventory

        if self.score is not None:
            result['score'] = self.score.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')

        if m.get('score') is not None:
            temp_model = main_models.GetDataQualityAnalysisResponseBodyDataDataQualityScore()
            self.score = temp_model.from_map(m.get('score'))

        return self

class GetDataQualityAnalysisResponseBodyDataDataQualityScore(DaraModel):
    def __init__(
        self,
        g_1: float = None,
        g_2: float = None,
        g_3: float = None,
        g_4: float = None,
    ):
        # Data quality evaluation indicator 1: activity data credibility.
        self.g_1 = g_1
        # Data quality evaluation indicator 2: data factor reliability.
        self.g_2 = g_2
        # Data quality evaluation indicator 3: time representativeness.
        self.g_3 = g_3
        # Data quality evaluation indicator 4: geographic representativeness.
        self.g_4 = g_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.g_1 is not None:
            result['g1'] = self.g_1

        if self.g_2 is not None:
            result['g2'] = self.g_2

        if self.g_3 is not None:
            result['g3'] = self.g_3

        if self.g_4 is not None:
            result['g4'] = self.g_4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('g1') is not None:
            self.g_1 = m.get('g1')

        if m.get('g2') is not None:
            self.g_2 = m.get('g2')

        if m.get('g3') is not None:
            self.g_3 = m.get('g3')

        if m.get('g4') is not None:
            self.g_4 = m.get('g4')

        return self

