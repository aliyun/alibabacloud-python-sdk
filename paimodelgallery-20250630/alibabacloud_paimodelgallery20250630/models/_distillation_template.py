# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paimodelgallery20250630 import models as main_models
from darabonba.model import DaraModel

class DistillationTemplate(DaraModel):
    def __init__(
        self,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        algorithm_version: str = None,
        capability_tags: List[str] = None,
        category: str = None,
        default_config: str = None,
        description: str = None,
        input_dataset_must_be_directory: bool = None,
        input_example_uri: str = None,
        job_type: str = None,
        model_slots: List[main_models.DistillationTemplateModelSlots] = None,
        order_number: int = None,
        pipeline_stages: List[main_models.DistillationTemplatePipelineStages] = None,
        preset_config: List[main_models.DistillationTemplatePresetConfig] = None,
        template_id: str = None,
        template_name: str = None,
        training_options: List[main_models.DistillationTemplateTrainingOptions] = None,
    ):
        # The algorithm name.
        self.algorithm_name = algorithm_name
        # The algorithm provider.
        self.algorithm_provider = algorithm_provider
        # The algorithm version.
        self.algorithm_version = algorithm_version
        # The list of capability tags used for displaying scenario cards.
        self.capability_tags = capability_tags
        # The template category. The frontend uses this value to filter scenario cards.
        self.category = category
        # The raw YAML content of the EasyDistill default configurations. The frontend uses this content for rendering the configuration form and supports recovering to default configurations. The model and credential fields are intentionally left empty and are populated by the user in the form upon commit.
        self.default_config = default_config
        # The template description, localized based on the requested language. The description specifies the applicable scenarios and outputs.
        self.description = description
        # Specifies whether the input data must be an entire directory. If this parameter is set to true, only a directory can be selected on the form, not a single file. If this parameter is absent or set to false, either a file or a directory can be selected. This value is true when seed files reference other files in the same directory by relative path.
        self.input_dataset_must_be_directory = input_dataset_must_be_directory
        # The OSS address of the sample input data, rendered based on the region. Users can download the sample and prepare their own data in the same format. An empty value indicates that the template does not provide a sample.
        self.input_example_uri = input_example_uri
        # The algorithm job type. The value is the same as TemplateId.
        self.job_type = job_type
        # The list of model slots that require user selection. The frontend uses this list to render the model selection form.
        self.model_slots = model_slots
        # The display order. A smaller value indicates a higher priority.
        self.order_number = order_number
        # The list of pipeline stages. The order of the stages represents the execution order.
        self.pipeline_stages = pipeline_stages
        # The content of the preset configuration card, displayed in order to show the key default configurations of the template.
        self.preset_config = preset_config
        # The distillation template ID, which is the same as the algorithm job_type. Pass this value as TemplateId when creating a task plan.
        self.template_id = template_id
        # The template display name, localized based on the requested language.
        self.template_name = template_name
        # The capability declaration for the second stage (training the student model with the distilled data). An empty value indicates that the template supports only the distillation stage.
        self.training_options = training_options

    def validate(self):
        if self.model_slots:
            for v1 in self.model_slots:
                 if v1:
                    v1.validate()
        if self.pipeline_stages:
            for v1 in self.pipeline_stages:
                 if v1:
                    v1.validate()
        if self.preset_config:
            for v1 in self.preset_config:
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
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name

        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider

        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version

        if self.capability_tags is not None:
            result['CapabilityTags'] = self.capability_tags

        if self.category is not None:
            result['Category'] = self.category

        if self.default_config is not None:
            result['DefaultConfig'] = self.default_config

        if self.description is not None:
            result['Description'] = self.description

        if self.input_dataset_must_be_directory is not None:
            result['InputDatasetMustBeDirectory'] = self.input_dataset_must_be_directory

        if self.input_example_uri is not None:
            result['InputExampleUri'] = self.input_example_uri

        if self.job_type is not None:
            result['JobType'] = self.job_type

        result['ModelSlots'] = []
        if self.model_slots is not None:
            for k1 in self.model_slots:
                result['ModelSlots'].append(k1.to_map() if k1 else None)

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        result['PipelineStages'] = []
        if self.pipeline_stages is not None:
            for k1 in self.pipeline_stages:
                result['PipelineStages'].append(k1.to_map() if k1 else None)

        result['PresetConfig'] = []
        if self.preset_config is not None:
            for k1 in self.preset_config:
                result['PresetConfig'].append(k1.to_map() if k1 else None)

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
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')

        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')

        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')

        if m.get('CapabilityTags') is not None:
            self.capability_tags = m.get('CapabilityTags')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DefaultConfig') is not None:
            self.default_config = m.get('DefaultConfig')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputDatasetMustBeDirectory') is not None:
            self.input_dataset_must_be_directory = m.get('InputDatasetMustBeDirectory')

        if m.get('InputExampleUri') is not None:
            self.input_example_uri = m.get('InputExampleUri')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        self.model_slots = []
        if m.get('ModelSlots') is not None:
            for k1 in m.get('ModelSlots'):
                temp_model = main_models.DistillationTemplateModelSlots()
                self.model_slots.append(temp_model.from_map(k1))

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        self.pipeline_stages = []
        if m.get('PipelineStages') is not None:
            for k1 in m.get('PipelineStages'):
                temp_model = main_models.DistillationTemplatePipelineStages()
                self.pipeline_stages.append(temp_model.from_map(k1))

        self.preset_config = []
        if m.get('PresetConfig') is not None:
            for k1 in m.get('PresetConfig'):
                temp_model = main_models.DistillationTemplatePresetConfig()
                self.preset_config.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        self.training_options = []
        if m.get('TrainingOptions') is not None:
            for k1 in m.get('TrainingOptions'):
                temp_model = main_models.DistillationTemplateTrainingOptions()
                self.training_options.append(temp_model.from_map(k1))

        return self

class DistillationTemplateTrainingOptions(DaraModel):
    def __init__(
        self,
        model_tasks: List[str] = None,
        training_methods: List[str] = None,
        training_type: str = None,
    ):
        # The range of Model Gallery tasks available for the student model.
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

class DistillationTemplatePresetConfig(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        # The configuration item name, localized based on the requested language. Names are matched by position across languages, so the same row can have different names in different languages.
        self.label = label
        # The configuration item value, localized based on the requested language.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DistillationTemplatePipelineStages(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        name: str = None,
    ):
        # The stage description, localized based on the requested language.
        self.description = description
        # The stage identifier, which corresponds to the value of pipeline[].stage in the algorithm configuration.
        self.key = key
        # The stage display name, localized based on the requested language.
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

class DistillationTemplateModelSlots(DaraModel):
    def __init__(
        self,
        backends: List[main_models.DistillationTemplateModelSlotsBackends] = None,
        description: str = None,
        key: str = None,
        name: str = None,
        required: bool = None,
    ):
        # The list of model access methods supported by this slot.
        self.backends = backends
        # The slot description, localized based on the requested language.
        self.description = description
        # The slot identifier, which corresponds to the backend section name in the submitted configuration.
        self.key = key
        # The slot display name, localized based on the requested language.
        self.name = name
        # Specifies whether this slot is required. If this parameter is set to false, the user can skip the selection, and the algorithm falls back to other slots.
        self.required = required

    def validate(self):
        if self.backends:
            for v1 in self.backends:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backends'] = []
        if self.backends is not None:
            for k1 in self.backends:
                result['Backends'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backends = []
        if m.get('Backends') is not None:
            for k1 in m.get('Backends'):
                temp_model = main_models.DistillationTemplateModelSlotsBackends()
                self.backends.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self



class DistillationTemplateModelSlotsBackends(DaraModel):
    def __init__(
        self,
        channel: str = None,
        type: str = None,
    ):
        # The channel name of the PAI-Token gateway. The frontend uses this value to retrieve the list of available models for the channel. This value must be passed back as-is upon submission. This parameter is returned only when Type is pai_token.
        self.channel = channel
        # The model access method. pai_token indicates the PAI-Token gateway, where the user selects from the list of available models for the channel. pai_eas indicates the user\\"s own PAI-EAS service instance, which requires the service address and token.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

