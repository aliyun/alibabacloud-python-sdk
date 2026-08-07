# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_paimodelgallery20260603 import models as main_models
from darabonba.model import DaraModel

class ModelGalleryModel(DaraModel):
    def __init__(
        self,
        collection: str = None,
        compressible: bool = None,
        deep_think: bool = None,
        demonstrable: bool = None,
        deployable: bool = None,
        distillable: bool = None,
        domain: str = None,
        evaluable: bool = None,
        extra_info: Dict[str, Any] = None,
        function_call: bool = None,
        gmt_create_time: str = None,
        gmt_latest_version_modified: str = None,
        gmt_modified_time: str = None,
        latest_version_name: str = None,
        model_description: str = None,
        model_doc: str = None,
        model_id: str = None,
        model_name: str = None,
        model_series: str = None,
        model_type: str = None,
        order_number: int = None,
        origin: str = None,
        parameter_size: int = None,
        search_words: str = None,
        supported_compression_methods: Dict[str, Any] = None,
        supported_compression_resources: str = None,
        supported_distillation_methods: Dict[str, Any] = None,
        supported_distillation_resources: str = None,
        supported_evaluation_methods: Dict[str, Any] = None,
        supported_evaluation_resources: str = None,
        supported_inference_methods: Dict[str, Any] = None,
        supported_inference_resources: str = None,
        supported_training_methods: Dict[str, Any] = None,
        supported_training_resources: str = None,
        tags: main_models.ModelGalleryModelTags = None,
        task: str = None,
        trainable: bool = None,
    ):
        self.collection = collection
        self.compressible = compressible
        self.deep_think = deep_think
        self.demonstrable = demonstrable
        self.deployable = deployable
        self.distillable = distillable
        self.domain = domain
        self.evaluable = evaluable
        self.extra_info = extra_info
        self.function_call = function_call
        self.gmt_create_time = gmt_create_time
        self.gmt_latest_version_modified = gmt_latest_version_modified
        self.gmt_modified_time = gmt_modified_time
        self.latest_version_name = latest_version_name
        self.model_description = model_description
        self.model_doc = model_doc
        self.model_id = model_id
        self.model_name = model_name
        self.model_series = model_series
        self.model_type = model_type
        self.order_number = order_number
        self.origin = origin
        self.parameter_size = parameter_size
        self.search_words = search_words
        self.supported_compression_methods = supported_compression_methods
        self.supported_compression_resources = supported_compression_resources
        self.supported_distillation_methods = supported_distillation_methods
        self.supported_distillation_resources = supported_distillation_resources
        self.supported_evaluation_methods = supported_evaluation_methods
        self.supported_evaluation_resources = supported_evaluation_resources
        self.supported_inference_methods = supported_inference_methods
        self.supported_inference_resources = supported_inference_resources
        self.supported_training_methods = supported_training_methods
        self.supported_training_resources = supported_training_resources
        self.tags = tags
        self.task = task
        self.trainable = trainable

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        if self.compressible is not None:
            result['Compressible'] = self.compressible

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

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.function_call is not None:
            result['FunctionCall'] = self.function_call

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_latest_version_modified is not None:
            result['GmtLatestVersionModified'] = self.gmt_latest_version_modified

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.latest_version_name is not None:
            result['LatestVersionName'] = self.latest_version_name

        if self.model_description is not None:
            result['ModelDescription'] = self.model_description

        if self.model_doc is not None:
            result['ModelDoc'] = self.model_doc

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_series is not None:
            result['ModelSeries'] = self.model_series

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.parameter_size is not None:
            result['ParameterSize'] = self.parameter_size

        if self.search_words is not None:
            result['SearchWords'] = self.search_words

        if self.supported_compression_methods is not None:
            result['SupportedCompressionMethods'] = self.supported_compression_methods

        if self.supported_compression_resources is not None:
            result['SupportedCompressionResources'] = self.supported_compression_resources

        if self.supported_distillation_methods is not None:
            result['SupportedDistillationMethods'] = self.supported_distillation_methods

        if self.supported_distillation_resources is not None:
            result['SupportedDistillationResources'] = self.supported_distillation_resources

        if self.supported_evaluation_methods is not None:
            result['SupportedEvaluationMethods'] = self.supported_evaluation_methods

        if self.supported_evaluation_resources is not None:
            result['SupportedEvaluationResources'] = self.supported_evaluation_resources

        if self.supported_inference_methods is not None:
            result['SupportedInferenceMethods'] = self.supported_inference_methods

        if self.supported_inference_resources is not None:
            result['SupportedInferenceResources'] = self.supported_inference_resources

        if self.supported_training_methods is not None:
            result['SupportedTrainingMethods'] = self.supported_training_methods

        if self.supported_training_resources is not None:
            result['SupportedTrainingResources'] = self.supported_training_resources

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.task is not None:
            result['Task'] = self.task

        if self.trainable is not None:
            result['Trainable'] = self.trainable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('Compressible') is not None:
            self.compressible = m.get('Compressible')

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

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('FunctionCall') is not None:
            self.function_call = m.get('FunctionCall')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtLatestVersionModified') is not None:
            self.gmt_latest_version_modified = m.get('GmtLatestVersionModified')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LatestVersionName') is not None:
            self.latest_version_name = m.get('LatestVersionName')

        if m.get('ModelDescription') is not None:
            self.model_description = m.get('ModelDescription')

        if m.get('ModelDoc') is not None:
            self.model_doc = m.get('ModelDoc')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelSeries') is not None:
            self.model_series = m.get('ModelSeries')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('ParameterSize') is not None:
            self.parameter_size = m.get('ParameterSize')

        if m.get('SearchWords') is not None:
            self.search_words = m.get('SearchWords')

        if m.get('SupportedCompressionMethods') is not None:
            self.supported_compression_methods = m.get('SupportedCompressionMethods')

        if m.get('SupportedCompressionResources') is not None:
            self.supported_compression_resources = m.get('SupportedCompressionResources')

        if m.get('SupportedDistillationMethods') is not None:
            self.supported_distillation_methods = m.get('SupportedDistillationMethods')

        if m.get('SupportedDistillationResources') is not None:
            self.supported_distillation_resources = m.get('SupportedDistillationResources')

        if m.get('SupportedEvaluationMethods') is not None:
            self.supported_evaluation_methods = m.get('SupportedEvaluationMethods')

        if m.get('SupportedEvaluationResources') is not None:
            self.supported_evaluation_resources = m.get('SupportedEvaluationResources')

        if m.get('SupportedInferenceMethods') is not None:
            self.supported_inference_methods = m.get('SupportedInferenceMethods')

        if m.get('SupportedInferenceResources') is not None:
            self.supported_inference_resources = m.get('SupportedInferenceResources')

        if m.get('SupportedTrainingMethods') is not None:
            self.supported_training_methods = m.get('SupportedTrainingMethods')

        if m.get('SupportedTrainingResources') is not None:
            self.supported_training_resources = m.get('SupportedTrainingResources')

        if m.get('Tags') is not None:
            temp_model = main_models.ModelGalleryModelTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Task') is not None:
            self.task = m.get('Task')

        if m.get('Trainable') is not None:
            self.trainable = m.get('Trainable')

        return self



class ModelGalleryModelTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

