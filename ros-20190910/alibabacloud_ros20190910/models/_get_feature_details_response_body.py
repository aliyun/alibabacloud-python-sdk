# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetFeatureDetailsResponseBody(DaraModel):
    def __init__(
        self,
        drift_detection: main_models.GetFeatureDetailsResponseBodyDriftDetection = None,
        request_id: str = None,
        resource_cleaner: main_models.GetFeatureDetailsResponseBodyResourceCleaner = None,
        resource_import: main_models.GetFeatureDetailsResponseBodyResourceImport = None,
        template_parameter_constraints: main_models.GetFeatureDetailsResponseBodyTemplateParameterConstraints = None,
        template_scratch: main_models.GetFeatureDetailsResponseBodyTemplateScratch = None,
        terraform: main_models.GetFeatureDetailsResponseBodyTerraform = None,
    ):
        # Details of the drift detection feature.
        self.drift_detection = drift_detection
        # The ID of the request.
        self.request_id = request_id
        # Details of the resource cleaner feature.
        self.resource_cleaner = resource_cleaner
        # Details of the resource import feature.
        self.resource_import = resource_import
        # Details of the template parameter constraint feature.
        self.template_parameter_constraints = template_parameter_constraints
        # Details of the scenario feature.
        self.template_scratch = template_scratch
        # Details of the Terraform hosting feature.
        self.terraform = terraform

    def validate(self):
        if self.drift_detection:
            self.drift_detection.validate()
        if self.resource_cleaner:
            self.resource_cleaner.validate()
        if self.resource_import:
            self.resource_import.validate()
        if self.template_parameter_constraints:
            self.template_parameter_constraints.validate()
        if self.template_scratch:
            self.template_scratch.validate()
        if self.terraform:
            self.terraform.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drift_detection is not None:
            result['DriftDetection'] = self.drift_detection.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_cleaner is not None:
            result['ResourceCleaner'] = self.resource_cleaner.to_map()

        if self.resource_import is not None:
            result['ResourceImport'] = self.resource_import.to_map()

        if self.template_parameter_constraints is not None:
            result['TemplateParameterConstraints'] = self.template_parameter_constraints.to_map()

        if self.template_scratch is not None:
            result['TemplateScratch'] = self.template_scratch.to_map()

        if self.terraform is not None:
            result['Terraform'] = self.terraform.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetection') is not None:
            temp_model = main_models.GetFeatureDetailsResponseBodyDriftDetection()
            self.drift_detection = temp_model.from_map(m.get('DriftDetection'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceCleaner') is not None:
            temp_model = main_models.GetFeatureDetailsResponseBodyResourceCleaner()
            self.resource_cleaner = temp_model.from_map(m.get('ResourceCleaner'))

        if m.get('ResourceImport') is not None:
            temp_model = main_models.GetFeatureDetailsResponseBodyResourceImport()
            self.resource_import = temp_model.from_map(m.get('ResourceImport'))

        if m.get('TemplateParameterConstraints') is not None:
            temp_model = main_models.GetFeatureDetailsResponseBodyTemplateParameterConstraints()
            self.template_parameter_constraints = temp_model.from_map(m.get('TemplateParameterConstraints'))

        if m.get('TemplateScratch') is not None:
            temp_model = main_models.GetFeatureDetailsResponseBodyTemplateScratch()
            self.template_scratch = temp_model.from_map(m.get('TemplateScratch'))

        if m.get('Terraform') is not None:
            temp_model = main_models.GetFeatureDetailsResponseBodyTerraform()
            self.terraform = temp_model.from_map(m.get('Terraform'))

        return self

class GetFeatureDetailsResponseBodyTerraform(DaraModel):
    def __init__(
        self,
        supported_resource_types: main_models.GetFeatureDetailsResponseBodyTerraformSupportedResourceTypes = None,
        supported_versions: List[main_models.GetFeatureDetailsResponseBodyTerraformSupportedVersions] = None,
    ):
        # The resource types that support the scenario feature.
        self.supported_resource_types = supported_resource_types
        # The Terraform versions.
        self.supported_versions = supported_versions

    def validate(self):
        if self.supported_resource_types:
            self.supported_resource_types.validate()
        if self.supported_versions:
            for v1 in self.supported_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_resource_types is not None:
            result['SupportedResourceTypes'] = self.supported_resource_types.to_map()

        result['SupportedVersions'] = []
        if self.supported_versions is not None:
            for k1 in self.supported_versions:
                result['SupportedVersions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedResourceTypes') is not None:
            temp_model = main_models.GetFeatureDetailsResponseBodyTerraformSupportedResourceTypes()
            self.supported_resource_types = temp_model.from_map(m.get('SupportedResourceTypes'))

        self.supported_versions = []
        if m.get('SupportedVersions') is not None:
            for k1 in m.get('SupportedVersions'):
                temp_model = main_models.GetFeatureDetailsResponseBodyTerraformSupportedVersions()
                self.supported_versions.append(temp_model.from_map(k1))

        return self

class GetFeatureDetailsResponseBodyTerraformSupportedVersions(DaraModel):
    def __init__(
        self,
        provider_versions: List[main_models.GetFeatureDetailsResponseBodyTerraformSupportedVersionsProviderVersions] = None,
        terraform_version: str = None,
        transform: str = None,
        update_allowed_transforms: List[str] = None,
    ):
        # The names and versions of the providers that correspond to the Terraform versions.
        self.provider_versions = provider_versions
        # The Terraform version.
        self.terraform_version = terraform_version
        # The Terraform version that is supported by ROS. The parameter value is the same as the value of the Transform parameter in a Terraform template.
        self.transform = transform
        # The Terraform versions that can be updated in ROS.
        self.update_allowed_transforms = update_allowed_transforms

    def validate(self):
        if self.provider_versions:
            for v1 in self.provider_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProviderVersions'] = []
        if self.provider_versions is not None:
            for k1 in self.provider_versions:
                result['ProviderVersions'].append(k1.to_map() if k1 else None)

        if self.terraform_version is not None:
            result['TerraformVersion'] = self.terraform_version

        if self.transform is not None:
            result['Transform'] = self.transform

        if self.update_allowed_transforms is not None:
            result['UpdateAllowedTransforms'] = self.update_allowed_transforms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.provider_versions = []
        if m.get('ProviderVersions') is not None:
            for k1 in m.get('ProviderVersions'):
                temp_model = main_models.GetFeatureDetailsResponseBodyTerraformSupportedVersionsProviderVersions()
                self.provider_versions.append(temp_model.from_map(k1))

        if m.get('TerraformVersion') is not None:
            self.terraform_version = m.get('TerraformVersion')

        if m.get('Transform') is not None:
            self.transform = m.get('Transform')

        if m.get('UpdateAllowedTransforms') is not None:
            self.update_allowed_transforms = m.get('UpdateAllowedTransforms')

        return self

class GetFeatureDetailsResponseBodyTerraformSupportedVersionsProviderVersions(DaraModel):
    def __init__(
        self,
        provider_name: str = None,
        supported_versions: List[str] = None,
    ):
        # The name of the provider.
        self.provider_name = provider_name
        # The provider versions.
        self.supported_versions = supported_versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.supported_versions is not None:
            result['SupportedVersions'] = self.supported_versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('SupportedVersions') is not None:
            self.supported_versions = m.get('SupportedVersions')

        return self

class GetFeatureDetailsResponseBodyTerraformSupportedResourceTypes(DaraModel):
    def __init__(
        self,
        custom_tag: List[str] = None,
        estimate_cost: List[str] = None,
        resource_group: List[str] = None,
        stack_operation_risk: main_models.GetFeatureDetailsResponseBodyTerraformSupportedResourceTypesStackOperationRisk = None,
        system_tag: List[str] = None,
    ):
        # The resource types that support the custom tag feature.
        self.custom_tag = custom_tag
        # The resource types that support the price inquiry feature.
        self.estimate_cost = estimate_cost
        # The resource types that support the resource group feature.
        self.resource_group = resource_group
        # The resource type that support the risk check feature.
        self.stack_operation_risk = stack_operation_risk
        # The resource types that support the system tag `acs:ros:stackId`.
        self.system_tag = system_tag

    def validate(self):
        if self.stack_operation_risk:
            self.stack_operation_risk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_tag is not None:
            result['CustomTag'] = self.custom_tag

        if self.estimate_cost is not None:
            result['EstimateCost'] = self.estimate_cost

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.stack_operation_risk is not None:
            result['StackOperationRisk'] = self.stack_operation_risk.to_map()

        if self.system_tag is not None:
            result['SystemTag'] = self.system_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTag') is not None:
            self.custom_tag = m.get('CustomTag')

        if m.get('EstimateCost') is not None:
            self.estimate_cost = m.get('EstimateCost')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('StackOperationRisk') is not None:
            temp_model = main_models.GetFeatureDetailsResponseBodyTerraformSupportedResourceTypesStackOperationRisk()
            self.stack_operation_risk = temp_model.from_map(m.get('StackOperationRisk'))

        if m.get('SystemTag') is not None:
            self.system_tag = m.get('SystemTag')

        return self

class GetFeatureDetailsResponseBodyTerraformSupportedResourceTypesStackOperationRisk(DaraModel):
    def __init__(
        self,
        delete_stack: List[str] = None,
    ):
        # The resource types that support the risk check performed to detect risks caused by a stack deletion operation.
        self.delete_stack = delete_stack

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_stack is not None:
            result['DeleteStack'] = self.delete_stack

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteStack') is not None:
            self.delete_stack = m.get('DeleteStack')

        return self

class GetFeatureDetailsResponseBodyTemplateScratch(DaraModel):
    def __init__(
        self,
        supported_resource_types: List[main_models.GetFeatureDetailsResponseBodyTemplateScratchSupportedResourceTypes] = None,
    ):
        # The resource types that are supported by the scenario feature.
        self.supported_resource_types = supported_resource_types

    def validate(self):
        if self.supported_resource_types:
            for v1 in self.supported_resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedResourceTypes'] = []
        if self.supported_resource_types is not None:
            for k1 in self.supported_resource_types:
                result['SupportedResourceTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource_types = []
        if m.get('SupportedResourceTypes') is not None:
            for k1 in m.get('SupportedResourceTypes'):
                temp_model = main_models.GetFeatureDetailsResponseBodyTemplateScratchSupportedResourceTypes()
                self.supported_resource_types.append(temp_model.from_map(k1))

        return self

class GetFeatureDetailsResponseBodyTemplateScratchSupportedResourceTypes(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        source_resource_group_supported: bool = None,
        source_resources_supported: bool = None,
        source_supported: bool = None,
        source_tag_supported: bool = None,
        supported_template_scratch_types: List[str] = None,
    ):
        # The resource type.
        self.resource_type = resource_type
        # Indicates whether the resource scope can be specified by source resource group. Valid values:
        # 
        # *   true
        # *   false
        self.source_resource_group_supported = source_resource_group_supported
        # Indicates whether the resource scope can be specified by source resource. Valid values:
        # 
        # *   true
        # *   false
        self.source_resources_supported = source_resources_supported
        # Indicates whether the resource scope can be specified by source tag, resource group, or resource. Valid values:
        # 
        # *   true
        # *   false
        self.source_supported = source_supported
        # Indicates whether the resource scope can be specified by source tag. Valid values:
        # 
        # *   true
        # *   false
        self.source_tag_supported = source_tag_supported
        # The scenario types that are supported.
        self.supported_template_scratch_types = supported_template_scratch_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.source_resource_group_supported is not None:
            result['SourceResourceGroupSupported'] = self.source_resource_group_supported

        if self.source_resources_supported is not None:
            result['SourceResourcesSupported'] = self.source_resources_supported

        if self.source_supported is not None:
            result['SourceSupported'] = self.source_supported

        if self.source_tag_supported is not None:
            result['SourceTagSupported'] = self.source_tag_supported

        if self.supported_template_scratch_types is not None:
            result['SupportedTemplateScratchTypes'] = self.supported_template_scratch_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SourceResourceGroupSupported') is not None:
            self.source_resource_group_supported = m.get('SourceResourceGroupSupported')

        if m.get('SourceResourcesSupported') is not None:
            self.source_resources_supported = m.get('SourceResourcesSupported')

        if m.get('SourceSupported') is not None:
            self.source_supported = m.get('SourceSupported')

        if m.get('SourceTagSupported') is not None:
            self.source_tag_supported = m.get('SourceTagSupported')

        if m.get('SupportedTemplateScratchTypes') is not None:
            self.supported_template_scratch_types = m.get('SupportedTemplateScratchTypes')

        return self

class GetFeatureDetailsResponseBodyTemplateParameterConstraints(DaraModel):
    def __init__(
        self,
        supported_resource_types: List[main_models.GetFeatureDetailsResponseBodyTemplateParameterConstraintsSupportedResourceTypes] = None,
    ):
        # The resource types that support the template parameter constraint feature.
        self.supported_resource_types = supported_resource_types

    def validate(self):
        if self.supported_resource_types:
            for v1 in self.supported_resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedResourceTypes'] = []
        if self.supported_resource_types is not None:
            for k1 in self.supported_resource_types:
                result['SupportedResourceTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource_types = []
        if m.get('SupportedResourceTypes') is not None:
            for k1 in m.get('SupportedResourceTypes'):
                temp_model = main_models.GetFeatureDetailsResponseBodyTemplateParameterConstraintsSupportedResourceTypes()
                self.supported_resource_types.append(temp_model.from_map(k1))

        return self

class GetFeatureDetailsResponseBodyTemplateParameterConstraintsSupportedResourceTypes(DaraModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        # The names of properties that are supported by the resource type.
        self.properties = properties
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.properties is not None:
            result['Properties'] = self.properties

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GetFeatureDetailsResponseBodyResourceImport(DaraModel):
    def __init__(
        self,
        supported_resource_types: List[main_models.GetFeatureDetailsResponseBodyResourceImportSupportedResourceTypes] = None,
    ):
        # The resource types that are supported by the resource import feature.
        self.supported_resource_types = supported_resource_types

    def validate(self):
        if self.supported_resource_types:
            for v1 in self.supported_resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedResourceTypes'] = []
        if self.supported_resource_types is not None:
            for k1 in self.supported_resource_types:
                result['SupportedResourceTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource_types = []
        if m.get('SupportedResourceTypes') is not None:
            for k1 in m.get('SupportedResourceTypes'):
                temp_model = main_models.GetFeatureDetailsResponseBodyResourceImportSupportedResourceTypes()
                self.supported_resource_types.append(temp_model.from_map(k1))

        return self

class GetFeatureDetailsResponseBodyResourceImportSupportedResourceTypes(DaraModel):
    def __init__(
        self,
        resource_identifiers: List[str] = None,
        resource_type: str = None,
    ):
        # The resource identifiers.
        self.resource_identifiers = resource_identifiers
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_identifiers is not None:
            result['ResourceIdentifiers'] = self.resource_identifiers

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIdentifiers') is not None:
            self.resource_identifiers = m.get('ResourceIdentifiers')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GetFeatureDetailsResponseBodyResourceCleaner(DaraModel):
    def __init__(
        self,
        supported_resource_types: List[main_models.GetFeatureDetailsResponseBodyResourceCleanerSupportedResourceTypes] = None,
    ):
        # The resource types that can be cleaned up.
        self.supported_resource_types = supported_resource_types

    def validate(self):
        if self.supported_resource_types:
            for v1 in self.supported_resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedResourceTypes'] = []
        if self.supported_resource_types is not None:
            for k1 in self.supported_resource_types:
                result['SupportedResourceTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource_types = []
        if m.get('SupportedResourceTypes') is not None:
            for k1 in m.get('SupportedResourceTypes'):
                temp_model = main_models.GetFeatureDetailsResponseBodyResourceCleanerSupportedResourceTypes()
                self.supported_resource_types.append(temp_model.from_map(k1))

        return self

class GetFeatureDetailsResponseBodyResourceCleanerSupportedResourceTypes(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        side_effects: List[str] = None,
        supported_filters: List[str] = None,
    ):
        # The resource type that supports the resource cleaner feature.
        self.resource_type = resource_type
        # The names of the side effects that may be caused by the cleanup operation performed on the resources of the specified type.
        self.side_effects = side_effects
        # The names of the filters that are supported by the resource type.
        self.supported_filters = supported_filters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.side_effects is not None:
            result['SideEffects'] = self.side_effects

        if self.supported_filters is not None:
            result['SupportedFilters'] = self.supported_filters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SideEffects') is not None:
            self.side_effects = m.get('SideEffects')

        if m.get('SupportedFilters') is not None:
            self.supported_filters = m.get('SupportedFilters')

        return self

class GetFeatureDetailsResponseBodyDriftDetection(DaraModel):
    def __init__(
        self,
        supported_resource_types: List[str] = None,
    ):
        # The resource types that are supported by the drift detection feature.
        self.supported_resource_types = supported_resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_resource_types is not None:
            result['SupportedResourceTypes'] = self.supported_resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedResourceTypes') is not None:
            self.supported_resource_types = m.get('SupportedResourceTypes')

        return self

