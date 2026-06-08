# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetTemplateScratchResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_scratch: main_models.GetTemplateScratchResponseBodyTemplateScratch = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The resource scenario.
        self.template_scratch = template_scratch

    def validate(self):
        if self.template_scratch:
            self.template_scratch.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_scratch is not None:
            result['TemplateScratch'] = self.template_scratch.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateScratch') is not None:
            temp_model = main_models.GetTemplateScratchResponseBodyTemplateScratch()
            self.template_scratch = temp_model.from_map(m.get('TemplateScratch'))

        return self

class GetTemplateScratchResponseBodyTemplateScratch(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        failed_code: str = None,
        logical_id_strategy: str = None,
        preference_parameters: List[main_models.GetTemplateScratchResponseBodyTemplateScratchPreferenceParameters] = None,
        resource_group_id: str = None,
        source_resource_group: main_models.GetTemplateScratchResponseBodyTemplateScratchSourceResourceGroup = None,
        source_resources: List[main_models.GetTemplateScratchResponseBodyTemplateScratchSourceResources] = None,
        source_tag: main_models.GetTemplateScratchResponseBodyTemplateScratchSourceTag = None,
        stack_provision: main_models.GetTemplateScratchResponseBodyTemplateScratchStackProvision = None,
        stacks: List[main_models.GetTemplateScratchResponseBodyTemplateScratchStacks] = None,
        status: str = None,
        status_reason: str = None,
        template_scratch_data: Dict[str, Any] = None,
        template_scratch_id: str = None,
        template_scratch_type: str = None,
        update_time: str = None,
    ):
        # The time at which the resource scenario was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the resource scenario.
        self.description = description
        # The status code of the resource scenario that fails to be created.
        # 
        # > This parameter is returned only if you set Status to GENERATE_FAILED.
        self.failed_code = failed_code
        # The policy based on which the logical ID is generated. Valid values:
        # 
        # *   LongTypePrefixAndIndexSuffix (default): long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the resource scenario.
        self.preference_parameters = preference_parameters
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        self.source_resource_group = source_resource_group
        # The source resources.
        self.source_resources = source_resources
        # The source tag.
        self.source_tag = source_tag
        # The preset information of the stack.
        self.stack_provision = stack_provision
        # The stacks that are associated with the resource scenario.
        self.stacks = stacks
        # The state of the resource scenario. Valid values:
        # 
        # *   GENERATE_IN_PROGRESS: The resource scenario is being created.
        # *   GENERATE_COMPLETE: The resource scenario is created.
        # *   GENERATE_FAILED: The resource scenario fails to be created.
        self.status = status
        # The reason why the resource scenario fails to be created.
        # 
        # > This parameter is returned only if you set Status to GENERATE_FAILED.
        self.status_reason = status_reason
        # The resource scenario data.
        self.template_scratch_data = template_scratch_data
        # The ID of the resource scenario.
        self.template_scratch_id = template_scratch_id
        # The type of the resource scenario. Valid values:
        # 
        # *   ResourceImport: resource management
        # *   ArchitectureReplication: resource replication
        self.template_scratch_type = template_scratch_type
        # The time at which the resource scenario was updated.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        if self.preference_parameters:
            for v1 in self.preference_parameters:
                 if v1:
                    v1.validate()
        if self.source_resource_group:
            self.source_resource_group.validate()
        if self.source_resources:
            for v1 in self.source_resources:
                 if v1:
                    v1.validate()
        if self.source_tag:
            self.source_tag.validate()
        if self.stack_provision:
            self.stack_provision.validate()
        if self.stacks:
            for v1 in self.stacks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.failed_code is not None:
            result['FailedCode'] = self.failed_code

        if self.logical_id_strategy is not None:
            result['LogicalIdStrategy'] = self.logical_id_strategy

        result['PreferenceParameters'] = []
        if self.preference_parameters is not None:
            for k1 in self.preference_parameters:
                result['PreferenceParameters'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_resource_group is not None:
            result['SourceResourceGroup'] = self.source_resource_group.to_map()

        result['SourceResources'] = []
        if self.source_resources is not None:
            for k1 in self.source_resources:
                result['SourceResources'].append(k1.to_map() if k1 else None)

        if self.source_tag is not None:
            result['SourceTag'] = self.source_tag.to_map()

        if self.stack_provision is not None:
            result['StackProvision'] = self.stack_provision.to_map()

        result['Stacks'] = []
        if self.stacks is not None:
            for k1 in self.stacks:
                result['Stacks'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.template_scratch_data is not None:
            result['TemplateScratchData'] = self.template_scratch_data

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

        if self.template_scratch_type is not None:
            result['TemplateScratchType'] = self.template_scratch_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FailedCode') is not None:
            self.failed_code = m.get('FailedCode')

        if m.get('LogicalIdStrategy') is not None:
            self.logical_id_strategy = m.get('LogicalIdStrategy')

        self.preference_parameters = []
        if m.get('PreferenceParameters') is not None:
            for k1 in m.get('PreferenceParameters'):
                temp_model = main_models.GetTemplateScratchResponseBodyTemplateScratchPreferenceParameters()
                self.preference_parameters.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceResourceGroup') is not None:
            temp_model = main_models.GetTemplateScratchResponseBodyTemplateScratchSourceResourceGroup()
            self.source_resource_group = temp_model.from_map(m.get('SourceResourceGroup'))

        self.source_resources = []
        if m.get('SourceResources') is not None:
            for k1 in m.get('SourceResources'):
                temp_model = main_models.GetTemplateScratchResponseBodyTemplateScratchSourceResources()
                self.source_resources.append(temp_model.from_map(k1))

        if m.get('SourceTag') is not None:
            temp_model = main_models.GetTemplateScratchResponseBodyTemplateScratchSourceTag()
            self.source_tag = temp_model.from_map(m.get('SourceTag'))

        if m.get('StackProvision') is not None:
            temp_model = main_models.GetTemplateScratchResponseBodyTemplateScratchStackProvision()
            self.stack_provision = temp_model.from_map(m.get('StackProvision'))

        self.stacks = []
        if m.get('Stacks') is not None:
            for k1 in m.get('Stacks'):
                temp_model = main_models.GetTemplateScratchResponseBodyTemplateScratchStacks()
                self.stacks.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('TemplateScratchData') is not None:
            self.template_scratch_data = m.get('TemplateScratchData')

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetTemplateScratchResponseBodyTemplateScratchStacks(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        stack_id: str = None,
        usage_type: str = None,
    ):
        # The region ID of the stack.
        self.region_id = region_id
        # The stack ID.
        self.stack_id = stack_id
        # The purpose of the stack. Valid values:
        # 
        # *   ResourceImport: resource management
        # *   ArchitectureReplication: resource replication
        self.usage_type = usage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        return self

class GetTemplateScratchResponseBodyTemplateScratchStackProvision(DaraModel):
    def __init__(
        self,
        creatable: bool = None,
        importable: bool = None,
    ):
        # Indicates whether the resource is replicated by calling the [CreateStack](https://help.aliyun.com/document_detail/132086.html) operation. Valid values:
        # 
        # *   true
        # *   false
        self.creatable = creatable
        # Indicates whether the resource is managed by calling the [CreateChangeSet](https://help.aliyun.com/document_detail/131051.html) operation. Valid values:
        # 
        # *   true
        # *   false
        self.importable = importable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creatable is not None:
            result['Creatable'] = self.creatable

        if self.importable is not None:
            result['Importable'] = self.importable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creatable') is not None:
            self.creatable = m.get('Creatable')

        if m.get('Importable') is not None:
            self.importable = m.get('Importable')

        return self

class GetTemplateScratchResponseBodyTemplateScratchSourceTag(DaraModel):
    def __init__(
        self,
        resource_tags: Dict[str, Any] = None,
        resource_type_filter: List[str] = None,
    ):
        # The source tags.
        self.resource_tags = resource_tags
        # The resource type filters.
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags

        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTags') is not None:
            self.resource_tags = m.get('ResourceTags')

        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')

        return self

class GetTemplateScratchResponseBodyTemplateScratchSourceResources(DaraModel):
    def __init__(
        self,
        related_resource_type_filter: List[str] = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The related resource type filters.
        self.related_resource_type_filter = related_resource_type_filter
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.related_resource_type_filter is not None:
            result['RelatedResourceTypeFilter'] = self.related_resource_type_filter

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelatedResourceTypeFilter') is not None:
            self.related_resource_type_filter = m.get('RelatedResourceTypeFilter')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GetTemplateScratchResponseBodyTemplateScratchSourceResourceGroup(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_type_filter: List[str] = None,
    ):
        # The ID of the source resource group.
        self.resource_group_id = resource_group_id
        # The resource type filters.
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')

        return self

class GetTemplateScratchResponseBodyTemplateScratchPreferenceParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The parameter name.
        self.parameter_key = parameter_key
        # The parameter value.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

