# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateScratchShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execution_mode: str = None,
        logical_id_strategy: str = None,
        preference_parameters_shrink: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_resource_group_shrink: str = None,
        source_resources_shrink: str = None,
        source_tag_shrink: str = None,
        tags: List[main_models.CreateTemplateScratchShrinkRequestTags] = None,
        template_scratch_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The description of the resource scenario.
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
        # *   LongTypePrefixAndIndexSuffix (default): long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the resource scenario.
        self.preference_parameters_shrink = preference_parameters_shrink
        # The region ID of the resource scenario.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        self.source_resource_group_shrink = source_resource_group_shrink
        # The source resources.
        # 
        # When you set TemplateScratchType to ArchitectureDetection, you can specify SourceResources to detect the architecture data of all resources associated with the specified source resources. For example, if you set SourceResources to the ID of a Classic Load Balancer (CLB) instance, the architecture data of all resources, such as the Elastic Compute Service (ECS) instance, vSwitch, and VPC, associated with the CLB instance is detected.
        # 
        # If you set TemplateScratchType to ArchitectureDetection, you can specify up to 20 source resources. In other cases, you can specify up to 200 source resources.
        self.source_resources_shrink = source_resources_shrink
        # The source tag.
        self.source_tag_shrink = source_tag_shrink
        # The tags of the resource scenario.
        self.tags = tags
        # The type of the resource scenario. Valid values:
        # 
        # *   ArchitectureReplication: resource replication
        # *   ArchitectureDetection: resource detection
        # *   ResourceImport: resource management
        # *   ResourceMigration: resource migration
        # 
        # >  The valid values of the ParameterKey and ParameterValue request parameters vary based on the value of TemplateScratchType. For more information, see the "**Additional information about request parameters**" section of this topic.
        # 
        # This parameter is required.
        self.template_scratch_type = template_scratch_type

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

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

        if self.preference_parameters_shrink is not None:
            result['PreferenceParameters'] = self.preference_parameters_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_resource_group_shrink is not None:
            result['SourceResourceGroup'] = self.source_resource_group_shrink

        if self.source_resources_shrink is not None:
            result['SourceResources'] = self.source_resources_shrink

        if self.source_tag_shrink is not None:
            result['SourceTag'] = self.source_tag_shrink

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_scratch_type is not None:
            result['TemplateScratchType'] = self.template_scratch_type

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

        if m.get('PreferenceParameters') is not None:
            self.preference_parameters_shrink = m.get('PreferenceParameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceResourceGroup') is not None:
            self.source_resource_group_shrink = m.get('SourceResourceGroup')

        if m.get('SourceResources') is not None:
            self.source_resources_shrink = m.get('SourceResources')

        if m.get('SourceTag') is not None:
            self.source_tag_shrink = m.get('SourceTag')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateTemplateScratchShrinkRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')

        return self

class CreateTemplateScratchShrinkRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource scenario.
        # 
        # > Tags is optional. If you want to specify Tags, you must specify Key.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource scenario.
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

