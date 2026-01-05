# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListLaunchOptionsResponseBody(DaraModel):
    def __init__(
        self,
        launch_option_summaries: List[main_models.ListLaunchOptionsResponseBodyLaunchOptionSummaries] = None,
        request_id: str = None,
    ):
        # The launch options.
        self.launch_option_summaries = launch_option_summaries
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.launch_option_summaries:
            for v1 in self.launch_option_summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LaunchOptionSummaries'] = []
        if self.launch_option_summaries is not None:
            for k1 in self.launch_option_summaries:
                result['LaunchOptionSummaries'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.launch_option_summaries = []
        if m.get('LaunchOptionSummaries') is not None:
            for k1 in m.get('LaunchOptionSummaries'):
                temp_model = main_models.ListLaunchOptionsResponseBodyLaunchOptionSummaries()
                self.launch_option_summaries.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLaunchOptionsResponseBodyLaunchOptionSummaries(DaraModel):
    def __init__(
        self,
        constraint_summaries: List[main_models.ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries] = None,
        portfolio_id: str = None,
        portfolio_name: str = None,
    ):
        # The constraints.
        self.constraint_summaries = constraint_summaries
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id
        # The name of the product portfolio.
        self.portfolio_name = portfolio_name

    def validate(self):
        if self.constraint_summaries:
            for v1 in self.constraint_summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConstraintSummaries'] = []
        if self.constraint_summaries is not None:
            for k1 in self.constraint_summaries:
                result['ConstraintSummaries'].append(k1.to_map() if k1 else None)

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constraint_summaries = []
        if m.get('ConstraintSummaries') is not None:
            for k1 in m.get('ConstraintSummaries'):
                temp_model = main_models.ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries()
                self.constraint_summaries.append(temp_model.from_map(k1))

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')

        return self

class ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries(DaraModel):
    def __init__(
        self,
        constraint_type: str = None,
        description: str = None,
        operation_types: List[str] = None,
        stack_regions: List[str] = None,
    ):
        # The type of the constraint. Valid values:
        # 
        # 1.  Launch
        # 2.  Template
        # 3.  Approval
        # 4.  StackRegion
        self.constraint_type = constraint_type
        # The description of the constraint.
        self.description = description
        # The types of operations that require approval. If the type of the constraint is Approval, this parameter is not empty.
        self.operation_types = operation_types
        # The regions in which users can launch the service. If the type of the constraint is StackRegion, this parameter is not empty.
        self.stack_regions = stack_regions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type

        if self.description is not None:
            result['Description'] = self.description

        if self.operation_types is not None:
            result['OperationTypes'] = self.operation_types

        if self.stack_regions is not None:
            result['StackRegions'] = self.stack_regions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OperationTypes') is not None:
            self.operation_types = m.get('OperationTypes')

        if m.get('StackRegions') is not None:
            self.stack_regions = m.get('StackRegions')

        return self

