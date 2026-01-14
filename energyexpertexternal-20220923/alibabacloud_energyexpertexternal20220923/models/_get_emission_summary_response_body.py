# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetEmissionSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetEmissionSummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # Details of summarized data
        self.data = data
        # Id of the request.
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
            temp_model = main_models.GetEmissionSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetEmissionSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        actual_emission_ratio: float = None,
        carbon_save_conversion: float = None,
        current_period_carbon_emission_data: float = None,
        is_weighting: bool = None,
        last_period_carbon_emission_data: float = None,
        last_period_weighting_carbon_emission_data: float = None,
        ratio: float = None,
        total_carbon_emission_data: float = None,
        weighting_carbon_emission_data: float = None,
        weighting_ratio: float = None,
    ):
        # Percentage of scheduled.
        self.actual_emission_ratio = actual_emission_ratio
        # Carbon emissions reduction.
        self.carbon_save_conversion = carbon_save_conversion
        # Statistical indicators for this cycle.
        self.current_period_carbon_emission_data = current_period_carbon_emission_data
        # Whether to show the weighting ratio carbon emission.
        self.is_weighting = is_weighting
        # Last period statistical indicators.
        self.last_period_carbon_emission_data = last_period_carbon_emission_data
        # Calculation of carbon emissions based on shareholding ratio in the last cycle.
        self.last_period_weighting_carbon_emission_data = last_period_weighting_carbon_emission_data
        # Year-on-year.
        self.ratio = ratio
        # Total carbon emissions.
        self.total_carbon_emission_data = total_carbon_emission_data
        # Calculate carbon emissions by share ratio
        self.weighting_carbon_emission_data = weighting_carbon_emission_data
        # Year-on-year of weighting ratio carbon emissions.
        self.weighting_ratio = weighting_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_emission_ratio is not None:
            result['actualEmissionRatio'] = self.actual_emission_ratio

        if self.carbon_save_conversion is not None:
            result['carbonSaveConversion'] = self.carbon_save_conversion

        if self.current_period_carbon_emission_data is not None:
            result['currentPeriodCarbonEmissionData'] = self.current_period_carbon_emission_data

        if self.is_weighting is not None:
            result['isWeighting'] = self.is_weighting

        if self.last_period_carbon_emission_data is not None:
            result['lastPeriodCarbonEmissionData'] = self.last_period_carbon_emission_data

        if self.last_period_weighting_carbon_emission_data is not None:
            result['lastPeriodWeightingCarbonEmissionData'] = self.last_period_weighting_carbon_emission_data

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.total_carbon_emission_data is not None:
            result['totalCarbonEmissionData'] = self.total_carbon_emission_data

        if self.weighting_carbon_emission_data is not None:
            result['weightingCarbonEmissionData'] = self.weighting_carbon_emission_data

        if self.weighting_ratio is not None:
            result['weightingRatio'] = self.weighting_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualEmissionRatio') is not None:
            self.actual_emission_ratio = m.get('actualEmissionRatio')

        if m.get('carbonSaveConversion') is not None:
            self.carbon_save_conversion = m.get('carbonSaveConversion')

        if m.get('currentPeriodCarbonEmissionData') is not None:
            self.current_period_carbon_emission_data = m.get('currentPeriodCarbonEmissionData')

        if m.get('isWeighting') is not None:
            self.is_weighting = m.get('isWeighting')

        if m.get('lastPeriodCarbonEmissionData') is not None:
            self.last_period_carbon_emission_data = m.get('lastPeriodCarbonEmissionData')

        if m.get('lastPeriodWeightingCarbonEmissionData') is not None:
            self.last_period_weighting_carbon_emission_data = m.get('lastPeriodWeightingCarbonEmissionData')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('totalCarbonEmissionData') is not None:
            self.total_carbon_emission_data = m.get('totalCarbonEmissionData')

        if m.get('weightingCarbonEmissionData') is not None:
            self.weighting_carbon_emission_data = m.get('weightingCarbonEmissionData')

        if m.get('weightingRatio') is not None:
            self.weighting_ratio = m.get('weightingRatio')

        return self

