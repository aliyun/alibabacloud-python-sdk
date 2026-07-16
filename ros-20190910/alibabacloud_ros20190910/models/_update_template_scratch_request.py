# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class UpdateTemplateScratchRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execution_mode: str = None,
        logical_id_strategy: str = None,
        preference_parameters: List[main_models.UpdateTemplateScratchRequestPreferenceParameters] = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_resource_group: main_models.UpdateTemplateScratchRequestSourceResourceGroup = None,
        source_resources: List[main_models.UpdateTemplateScratchRequestSourceResources] = None,
        source_tag: main_models.UpdateTemplateScratchRequestSourceTag = None,
        template_scratch_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The description of the scenario.
        self.description = description
        # The execution mode. Valid values:
        # 
        # *   Async (default)
        # *   Sync
        # 
        # > If you have a wide scope of resources, Sync takes longer. If you set ExecutionMode to Sync, we recommend that you specify ClientToken to prevent the execution timeout.
        self.execution_mode = execution_mode
        # The policy based on which the logical ID is generated. Valid values:
        # 
        # *   LongTypePrefixAndIndexSuffix: long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        # 
        # >  If you set TemplateScratchType to ArchitectureDetection, the default value of LogicalIdStrategy is LongTypePrefixAndHashSuffix. In other cases, the default value of LogicalIdStrategy is LongTypePrefixAndIndexSuffix.
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the resource scenario.
        self.preference_parameters = preference_parameters
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        # 
        # >  You must specify only one of the following parameters: SourceResources, SourceTag, and SourceResourceGroup.
        self.source_resource_group = source_resource_group
        # The source resources.
        # 
        # >  You must specify only one of the following parameters: SourceResources, SourceTag, and SourceResourceGroup.
        self.source_resources = source_resources
        # The source tag.
        # 
        # >  You must specify only one of the following parameters: SourceResources, SourceTag, and SourceResourceGroup.
        self.source_tag = source_tag
        # The ID of the resource scenario.
        # 
        # The valid values of the ParameterKey and ParameterValue request parameters vary based on the IDs of different types of resource scenarios. For more information, see the "Additional information about request parameters" section of this topic.
        # 
        # >  You can call the [ListTemplateScratches](https://help.aliyun.com/document_detail/610832.html) operation to query the ID of a resource scenario.
        # 
        # This parameter is required.
        self.template_scratch_id = template_scratch_id

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

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode

        if self.logical_id_strategy is not None:
            result['LogicalIdStrategy'] = self.logical_id_strategy

        result['PreferenceParameters'] = []
        if self.preference_parameters is not None:
            for k1 in self.preference_parameters:
                result['PreferenceParameters'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')

        if m.get('LogicalIdStrategy') is not None:
            self.logical_id_strategy = m.get('LogicalIdStrategy')

        self.preference_parameters = []
        if m.get('PreferenceParameters') is not None:
            for k1 in m.get('PreferenceParameters'):
                temp_model = main_models.UpdateTemplateScratchRequestPreferenceParameters()
                self.preference_parameters.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceResourceGroup') is not None:
            temp_model = main_models.UpdateTemplateScratchRequestSourceResourceGroup()
            self.source_resource_group = temp_model.from_map(m.get('SourceResourceGroup'))

        self.source_resources = []
        if m.get('SourceResources') is not None:
            for k1 in m.get('SourceResources'):
                temp_model = main_models.UpdateTemplateScratchRequestSourceResources()
                self.source_resources.append(temp_model.from_map(k1))

        if m.get('SourceTag') is not None:
            temp_model = main_models.UpdateTemplateScratchRequestSourceTag()
            self.source_tag = temp_model.from_map(m.get('SourceTag'))

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        return self

class UpdateTemplateScratchRequestSourceTag(DaraModel):
    def __init__(
        self,
        resource_tags: Dict[str, Any] = None,
        resource_type_filter: List[str] = None,
    ):
        # The source tags. A tag contains a tag key and a tag value.
        # 
        # If you want to specify only the tag key, you must leave the tag value empty. Example: {"TagKey": ""}.
        # 
        # If you set TemplateScratchType to ArchitectureDetection, you can add up to 5 source tags. In other cases, you can add up to 10 source tags.
        # 
        # This parameter is required.
        self.resource_tags = resource_tags
        # The resource types for filtering resources.
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

class UpdateTemplateScratchRequestSourceResources(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class UpdateTemplateScratchRequestSourceResourceGroup(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_type_filter: List[str] = None,
    ):
        # The ID of the source resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The resource types for filtering resources.
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

class UpdateTemplateScratchRequestPreferenceParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The parameter name.
        # 
        # For more information about the valid values of ParameterKey, see the "**Additional information about request parameters**" section of this topic.
        # 
        # >- PreferenceParameters is optional. If you specify PreferenceParameters, you must specify both ParameterKey and ParameterValue.
        # > - If you set TemplateScratchType to ResourceImport, you must set ParameterKey to DeletionPolicy.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The parameter value. The value of ParameterValue varies based on the value of ParameterKey.
        # 
        # For more information about the valid values of ParameterKey, see the "**Additional information about request parameters**" section of this topic.
        # 
        # >  PreferenceParameters is optional. If you specify PreferenceParameters, you must specify both ParameterKey and ParameterValue.
        # 
        # This parameter is required.
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

