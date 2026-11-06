# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelGalleryModelsShrinkRequest(DaraModel):
    def __init__(
        self,
        collections: str = None,
        compressible: bool = None,
        conditions_shrink: str = None,
        deep_think: bool = None,
        demonstrable: bool = None,
        deployable: bool = None,
        distillable: bool = None,
        domain: str = None,
        evaluable: bool = None,
        function_call: bool = None,
        model_name: str = None,
        model_series: str = None,
        model_type: str = None,
        order: str = None,
        origin: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        sort_by: str = None,
        supported_compression_resource: str = None,
        supported_distillation_resource: str = None,
        supported_evaluation_resource: str = None,
        supported_inference_resource: str = None,
        supported_training_resource: str = None,
        tag_shrink: str = None,
        task: str = None,
        trainable: bool = None,
    ):
        self.collections = collections
        self.compressible = compressible
        self.conditions_shrink = conditions_shrink
        self.deep_think = deep_think
        self.demonstrable = demonstrable
        self.deployable = deployable
        self.distillable = distillable
        self.domain = domain
        self.evaluable = evaluable
        self.function_call = function_call
        self.model_name = model_name
        self.model_series = model_series
        self.model_type = model_type
        self.order = order
        self.origin = origin
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
        self.sort_by = sort_by
        self.supported_compression_resource = supported_compression_resource
        self.supported_distillation_resource = supported_distillation_resource
        self.supported_evaluation_resource = supported_evaluation_resource
        self.supported_inference_resource = supported_inference_resource
        self.supported_training_resource = supported_training_resource
        self.tag_shrink = tag_shrink
        self.task = task
        self.trainable = trainable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collections is not None:
            result['Collections'] = self.collections

        if self.compressible is not None:
            result['Compressible'] = self.compressible

        if self.conditions_shrink is not None:
            result['Conditions'] = self.conditions_shrink

        if self.deep_think is not None:
            result['DeepThink'] = self.deep_think

        if self.demonstrable is not None:
            result['Demonstrable'] = self.demonstrable

        if self.deployable is not None:
            result['Deployable'] = self.deployable

        if self.distillable is not None:
            result['Distillable'] = self.distillable

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.evaluable is not None:
            result['Evaluable'] = self.evaluable

        if self.function_call is not None:
            result['FunctionCall'] = self.function_call

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_series is not None:
            result['ModelSeries'] = self.model_series

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.order is not None:
            result['Order'] = self.order

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.supported_compression_resource is not None:
            result['SupportedCompressionResource'] = self.supported_compression_resource

        if self.supported_distillation_resource is not None:
            result['SupportedDistillationResource'] = self.supported_distillation_resource

        if self.supported_evaluation_resource is not None:
            result['SupportedEvaluationResource'] = self.supported_evaluation_resource

        if self.supported_inference_resource is not None:
            result['SupportedInferenceResource'] = self.supported_inference_resource

        if self.supported_training_resource is not None:
            result['SupportedTrainingResource'] = self.supported_training_resource

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        if self.task is not None:
            result['Task'] = self.task

        if self.trainable is not None:
            result['Trainable'] = self.trainable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')

        if m.get('Compressible') is not None:
            self.compressible = m.get('Compressible')

        if m.get('Conditions') is not None:
            self.conditions_shrink = m.get('Conditions')

        if m.get('DeepThink') is not None:
            self.deep_think = m.get('DeepThink')

        if m.get('Demonstrable') is not None:
            self.demonstrable = m.get('Demonstrable')

        if m.get('Deployable') is not None:
            self.deployable = m.get('Deployable')

        if m.get('Distillable') is not None:
            self.distillable = m.get('Distillable')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Evaluable') is not None:
            self.evaluable = m.get('Evaluable')

        if m.get('FunctionCall') is not None:
            self.function_call = m.get('FunctionCall')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelSeries') is not None:
            self.model_series = m.get('ModelSeries')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SupportedCompressionResource') is not None:
            self.supported_compression_resource = m.get('SupportedCompressionResource')

        if m.get('SupportedDistillationResource') is not None:
            self.supported_distillation_resource = m.get('SupportedDistillationResource')

        if m.get('SupportedEvaluationResource') is not None:
            self.supported_evaluation_resource = m.get('SupportedEvaluationResource')

        if m.get('SupportedInferenceResource') is not None:
            self.supported_inference_resource = m.get('SupportedInferenceResource')

        if m.get('SupportedTrainingResource') is not None:
            self.supported_training_resource = m.get('SupportedTrainingResource')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('Task') is not None:
            self.task = m.get('Task')

        if m.get('Trainable') is not None:
            self.trainable = m.get('Trainable')

        return self

