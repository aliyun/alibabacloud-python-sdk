# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ValidateTemplateResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        outputs: List[main_models.ValidateTemplateResponseBodyOutputs] = None,
        parameters: List[Dict[str, Any]] = None,
        request_id: str = None,
        resource_types: main_models.ValidateTemplateResponseBodyResourceTypes = None,
        resources: List[main_models.ValidateTemplateResponseBodyResources] = None,
        update_info: main_models.ValidateTemplateResponseBodyUpdateInfo = None,
    ):
        # The description of the template.
        self.description = description
        # The outputs of the template.
        self.outputs = outputs
        # The parameters that are defined in the Parameters section of the template.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id
        # The resource types that are used in the template.
        self.resource_types = resource_types
        # The regular resources that are defined in the template.
        # 
        # > - For a Resource Orchestration Service (ROS) template, the resource whose definition contains `Count` is not displayed as a list.
        # > -  For a Terraform template, the resource whose definition contains `count` or `for_each` is not displayed as a list.
        self.resources = resources
        # The information about the stack update. This parameter cannot be returned if the value of UpdateInfoOptions contains Disabled.
        self.update_info = update_info

    def validate(self):
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()
        if self.resource_types:
            self.resource_types.validate()
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()
        if self.update_info:
            self.update_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types.to_map()

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.update_info is not None:
            result['UpdateInfo'] = self.update_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.ValidateTemplateResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k1))

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceTypes') is not None:
            temp_model = main_models.ValidateTemplateResponseBodyResourceTypes()
            self.resource_types = temp_model.from_map(m.get('ResourceTypes'))

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ValidateTemplateResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('UpdateInfo') is not None:
            temp_model = main_models.ValidateTemplateResponseBodyUpdateInfo()
            self.update_info = temp_model.from_map(m.get('UpdateInfo'))

        return self

class ValidateTemplateResponseBodyUpdateInfo(DaraModel):
    def __init__(
        self,
        parameters_allowed_to_be_modified: List[str] = None,
        parameters_cause_interruption_if_modified: List[str] = None,
        parameters_cause_replacement_if_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_cause_interruption_if_modified: List[str] = None,
        parameters_conditionally_cause_replacement_if_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_cause_interruption_if_modified: List[str] = None,
        parameters_uncertainly_cause_replacement_if_modified: List[str] = None,
    ):
        # The parameters that can be modified.
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        # The parameters whose changes cause service interruptions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_cause_interruption_if_modified = parameters_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources.
        # 
        # > -  This parameter can be returned only if the value of UpdateInfoOptions contains EnableReplacement.
        # > -  This parameter is valid only for updates on ROS stacks.
        self.parameters_cause_replacement_if_modified = parameters_cause_replacement_if_modified
        # The parameters that can be modified under specific conditions.
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        # The parameters whose changes cause service interruptions under specific conditions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_conditionally_cause_interruption_if_modified = parameters_conditionally_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources under specific conditions.
        # 
        # > - This parameter can be returned only if the value of UpdateInfoOptions contains EnableReplacement.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_conditionally_cause_replacement_if_modified = parameters_conditionally_cause_replacement_if_modified
        # The parameters that cannot be modified.
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified
        # The parameters that can be modified under uncertain conditions.
        self.parameters_uncertainly_allowed_to_be_modified = parameters_uncertainly_allowed_to_be_modified
        # The parameters whose changes cause service interruptions under uncertain conditions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_uncertainly_cause_interruption_if_modified = parameters_uncertainly_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources under uncertain conditions.
        # 
        # > -  This parameter can be returned only if the value of UpdateInfoOptions contains EnableReplacement.
        # > -  This parameter is valid only for updates on ROS stacks.
        self.parameters_uncertainly_cause_replacement_if_modified = parameters_uncertainly_cause_replacement_if_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified

        if self.parameters_cause_interruption_if_modified is not None:
            result['ParametersCauseInterruptionIfModified'] = self.parameters_cause_interruption_if_modified

        if self.parameters_cause_replacement_if_modified is not None:
            result['ParametersCauseReplacementIfModified'] = self.parameters_cause_replacement_if_modified

        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified

        if self.parameters_conditionally_cause_interruption_if_modified is not None:
            result['ParametersConditionallyCauseInterruptionIfModified'] = self.parameters_conditionally_cause_interruption_if_modified

        if self.parameters_conditionally_cause_replacement_if_modified is not None:
            result['ParametersConditionallyCauseReplacementIfModified'] = self.parameters_conditionally_cause_replacement_if_modified

        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified

        if self.parameters_uncertainly_allowed_to_be_modified is not None:
            result['ParametersUncertainlyAllowedToBeModified'] = self.parameters_uncertainly_allowed_to_be_modified

        if self.parameters_uncertainly_cause_interruption_if_modified is not None:
            result['ParametersUncertainlyCauseInterruptionIfModified'] = self.parameters_uncertainly_cause_interruption_if_modified

        if self.parameters_uncertainly_cause_replacement_if_modified is not None:
            result['ParametersUncertainlyCauseReplacementIfModified'] = self.parameters_uncertainly_cause_replacement_if_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')

        if m.get('ParametersCauseInterruptionIfModified') is not None:
            self.parameters_cause_interruption_if_modified = m.get('ParametersCauseInterruptionIfModified')

        if m.get('ParametersCauseReplacementIfModified') is not None:
            self.parameters_cause_replacement_if_modified = m.get('ParametersCauseReplacementIfModified')

        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')

        if m.get('ParametersConditionallyCauseInterruptionIfModified') is not None:
            self.parameters_conditionally_cause_interruption_if_modified = m.get('ParametersConditionallyCauseInterruptionIfModified')

        if m.get('ParametersConditionallyCauseReplacementIfModified') is not None:
            self.parameters_conditionally_cause_replacement_if_modified = m.get('ParametersConditionallyCauseReplacementIfModified')

        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')

        if m.get('ParametersUncertainlyAllowedToBeModified') is not None:
            self.parameters_uncertainly_allowed_to_be_modified = m.get('ParametersUncertainlyAllowedToBeModified')

        if m.get('ParametersUncertainlyCauseInterruptionIfModified') is not None:
            self.parameters_uncertainly_cause_interruption_if_modified = m.get('ParametersUncertainlyCauseInterruptionIfModified')

        if m.get('ParametersUncertainlyCauseReplacementIfModified') is not None:
            self.parameters_uncertainly_cause_replacement_if_modified = m.get('ParametersUncertainlyCauseReplacementIfModified')

        return self

class ValidateTemplateResponseBodyResources(DaraModel):
    def __init__(
        self,
        logical_resource_id_pattern: str = None,
        resource_path: str = None,
        resource_type: str = None,
    ):
        # The pattern in which the logical IDs of regular resources are formed.
        # 
        # If resources are defined in a ROS template, the following rules apply:
        # 
        # *   Resource whose definition does not contain `Count`: If the resource name defined in the template is `server`, the values of LogicalResourceIdPattern and `ResourcePath` are both `server`.``
        # *   Resource whose definition contains `Count`: If the resource name defined in the template is `server`, the value of LogicalResourceIdPattern is `server[*]`, and the value of `ResourcePath` is `server`.
        # 
        # If resources and [modules](https://www.terraform.io/language/modules) are defined in a Terraform template, the following rules apply:
        # 
        # *   Resource and module whose definitions do not contain [`count`](https://www.terraform.io/language/meta-arguments/count) or [`for_each`](https://www.terraform.io/language/meta-arguments/for_each): If the resource name defined in the template is `server`, the values of LogicalResourceIdPattern and `ResourcePath` are both `server`.``
        # *   Resource and module whose definitions contain [`count`](https://www.terraform.io/language/meta-arguments/count) or [`for_each`](https://www.terraform.io/language/meta-arguments/for_each): If the resource name defined in the template is `server`, the value of LogicalResourceIdPattern is `server[*]`, and the value of `ResourcePath` is `server`.
        # 
        # Examples of LogicalResourceIdPattern for resources in a Terraform template:
        # 
        # *   Valid values of LogicalResourceIdPattern if a resource belongs to the root module:
        # 
        #     *   `server`: In this case, `count` and `for_each` are not contained in the resource. The value of `ResourcePath` is `server`.
        #     *   `server[*]`: In this case, `count` or `for_each` is contained in the resource. The value of `ResourcePath` is `server`.
        # 
        # *   Valid values of LogicalResourceIdPattern if a resource belongs to a child module:
        # 
        #     *   `app.server`: In this case, `count` and `for_each` are not contained in the `app` module and the `server` resource. The value of `ResourcePath` is `app.server`.````
        #     *   `app.server[*]`: In this case, `count` or `for_each` is contained in the `server` resource, but `count` and `for_each` are not contained in the `app` module. The value of `ResourcePath` is `app.server`.
        #     *   `app[*].server`: In this case, `count` or `for_each` is contained in the `app` module, but `count` and `for_each` are not contained in the `server` resource. The value of `ResourcePath` is `app.server`.
        #     *   `app[*].server[*]`: In this case, `count` or `for_each` is contained in the `app` module and the `server` resource. The value of `ResourcePath` is `app.server`.````
        #     *   `app.app_group[*].server`: In this case, `count` or `for_each` is contained in the `app_group` module, but `count` and `for_each` are not contained in the `app` module and the `server` resource. The value of `ResourcePath` is `app.app_group.server`. The `app_group` module is a child module of the `app` module.````
        self.logical_resource_id_pattern = logical_resource_id_pattern
        # The path of the regular resource. In most cases, the path of a regular resource is the same as the resource name.
        self.resource_path = resource_path
        # The regular resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logical_resource_id_pattern is not None:
            result['LogicalResourceIdPattern'] = self.logical_resource_id_pattern

        if self.resource_path is not None:
            result['ResourcePath'] = self.resource_path

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceIdPattern') is not None:
            self.logical_resource_id_pattern = m.get('LogicalResourceIdPattern')

        if m.get('ResourcePath') is not None:
            self.resource_path = m.get('ResourcePath')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class ValidateTemplateResponseBodyResourceTypes(DaraModel):
    def __init__(
        self,
        data_sources: List[str] = None,
        resources: List[str] = None,
    ):
        # The DataSource resource types that are used in the template. The value is deduplicated.
        self.data_sources = data_sources
        # The regular resource types that are used in the template. The value is deduplicated.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_sources is not None:
            result['DataSources'] = self.data_sources

        if self.resources is not None:
            result['Resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        return self

class ValidateTemplateResponseBodyOutputs(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        output_key: str = None,
    ):
        # The description of the template output.
        self.description = description
        # The alias of the template output.
        self.label = label
        # The name of the template output.
        self.output_key = output_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.output_key is not None:
            result['OutputKey'] = self.output_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('OutputKey') is not None:
            self.output_key = m.get('OutputKey')

        return self

