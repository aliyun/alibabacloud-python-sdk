# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paimodelgallery20250630 import models as main_models
from darabonba.model import DaraModel

class DistillationTemplateSummary(DaraModel):
    def __init__(
        self,
        capability_tags: List[str] = None,
        category: str = None,
        description: str = None,
        job_type: str = None,
        order_number: int = None,
        pipeline_stages: List[main_models.DistillationTemplateSummaryPipelineStages] = None,
        template_id: str = None,
        template_name: str = None,
        training_options: List[main_models.DistillationTemplateSummaryTrainingOptions] = None,
    ):
        # The list of capability tags, used for scenario card display.
        self.capability_tags = capability_tags
        # The template category. The frontend uses this value to filter scenario cards.
        self.category = category
        # The template description, localized based on the language specified in the request. The description specifies applicable scenarios and outputs.
        self.description = description
        # The algorithm job type. The value is the same as TemplateId.
        self.job_type = job_type
        # The display order. A smaller value indicates a higher position.
        self.order_number = order_number
        # The list of pipeline stages. The order of the stages represents the execution order.
        self.pipeline_stages = pipeline_stages
        # The distillation template ID, which is the same as the algorithm job_type. Pass this value as TemplateId when creating a task plan.
        self.template_id = template_id
        # The template display name, localized based on the language specified in the request.
        self.template_name = template_name
        # The capability declaration for the second stage, in which the distilled data is used to train the student model. An empty value indicates that the template supports only the distillation stage.
        self.training_options = training_options

    def validate(self):
        if self.pipeline_stages:
            for v1 in self.pipeline_stages:
                 if v1:
                    v1.validate()
        if self.training_options:
            for v1 in self.training_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capability_tags is not None:
            result['CapabilityTags'] = self.capability_tags

        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        result['PipelineStages'] = []
        if self.pipeline_stages is not None:
            for k1 in self.pipeline_stages:
                result['PipelineStages'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        result['TrainingOptions'] = []
        if self.training_options is not None:
            for k1 in self.training_options:
                result['TrainingOptions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapabilityTags') is not None:
            self.capability_tags = m.get('CapabilityTags')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        self.pipeline_stages = []
        if m.get('PipelineStages') is not None:
            for k1 in m.get('PipelineStages'):
                temp_model = main_models.DistillationTemplateSummaryPipelineStages()
                self.pipeline_stages.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        self.training_options = []
        if m.get('TrainingOptions') is not None:
            for k1 in m.get('TrainingOptions'):
                temp_model = main_models.DistillationTemplateSummaryTrainingOptions()
                self.training_options.append(temp_model.from_map(k1))

        return self

class DistillationTemplateSummaryTrainingOptions(DaraModel):
    def __init__(
        self,
        model_tasks: List[str] = None,
        training_methods: List[str] = None,
        training_type: str = None,
    ):
        # The available Model Gallery Task values for the student model.
        self.model_tasks = model_tasks
        # The list of supported training method families.
        self.training_methods = training_methods
        # The training type. The frontend uses this value to select the training workflow and display text.
        self.training_type = training_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_tasks is not None:
            result['ModelTasks'] = self.model_tasks

        if self.training_methods is not None:
            result['TrainingMethods'] = self.training_methods

        if self.training_type is not None:
            result['TrainingType'] = self.training_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelTasks') is not None:
            self.model_tasks = m.get('ModelTasks')

        if m.get('TrainingMethods') is not None:
            self.training_methods = m.get('TrainingMethods')

        if m.get('TrainingType') is not None:
            self.training_type = m.get('TrainingType')

        return self

class DistillationTemplateSummaryPipelineStages(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        name: str = None,
    ):
        # The stage description, localized based on the language specified in the request.
        self.description = description
        # The stage identifier, which corresponds to the pipeline[].stage value in the algorithm configuration.
        self.key = key
        # The stage display name, localized based on the language specified in the request.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

