# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetNisNetworkMetricsRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        dimensions: List[main_models.GetNisNetworkMetricsRequestDimensions] = None,
        end_time: int = None,
        metric_name: str = None,
        region_no: str = None,
        resource_type: str = None,
        scan_by: str = None,
        step_minutes: int = None,
        use_cross_account: bool = None,
    ):
        self.account_ids = account_ids
        self.begin_time = begin_time
        # This parameter is required.
        self.dimensions = dimensions
        self.end_time = end_time
        # This parameter is required.
        self.metric_name = metric_name
        # This parameter is required.
        self.region_no = region_no
        # This parameter is required.
        self.resource_type = resource_type
        self.scan_by = scan_by
        self.step_minutes = step_minutes
        self.use_cross_account = use_cross_account

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scan_by is not None:
            result['ScanBy'] = self.scan_by

        if self.step_minutes is not None:
            result['StepMinutes'] = self.step_minutes

        if self.use_cross_account is not None:
            result['UseCrossAccount'] = self.use_cross_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.GetNisNetworkMetricsRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ScanBy') is not None:
            self.scan_by = m.get('ScanBy')

        if m.get('StepMinutes') is not None:
            self.step_minutes = m.get('StepMinutes')

        if m.get('UseCrossAccount') is not None:
            self.use_cross_account = m.get('UseCrossAccount')

        return self

class GetNisNetworkMetricsRequestDimensions(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

