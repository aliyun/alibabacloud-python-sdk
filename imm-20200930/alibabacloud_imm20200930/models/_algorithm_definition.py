# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class AlgorithmDefinition(DaraModel):
    def __init__(
        self,
        algorithm_definition_id: str = None,
        create_time: str = None,
        custom_labels: List[Dict[str, str]] = None,
        description: str = None,
        name: str = None,
        owner_id: str = None,
        project_name: str = None,
        training_specification: main_models.TrainingSpecification = None,
        update_time: str = None,
    ):
        # The ID of the algorithm definition.
        self.algorithm_definition_id = algorithm_definition_id
        # The creation time.
        self.create_time = create_time
        # Custom labels.
        self.custom_labels = custom_labels
        # The description.
        self.description = description
        # The name of the algorithm.
        self.name = name
        # The ID of the Alibaba Cloud account.
        self.owner_id = owner_id
        # The name of the project.
        self.project_name = project_name
        # The model training parameters.
        self.training_specification = training_specification
        # The update time.
        self.update_time = update_time

    def validate(self):
        if self.training_specification:
            self.training_specification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_definition_id is not None:
            result['AlgorithmDefinitionId'] = self.algorithm_definition_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.training_specification is not None:
            result['TrainingSpecification'] = self.training_specification.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmDefinitionId') is not None:
            self.algorithm_definition_id = m.get('AlgorithmDefinitionId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TrainingSpecification') is not None:
            temp_model = main_models.TrainingSpecification()
            self.training_specification = temp_model.from_map(m.get('TrainingSpecification'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

