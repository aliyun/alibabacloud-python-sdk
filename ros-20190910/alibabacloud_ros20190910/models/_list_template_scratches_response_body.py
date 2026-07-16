# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListTemplateScratchesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        template_scratches: List[main_models.ListTemplateScratchesResponseBodyTemplateScratches] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The resource scenarios.
        self.template_scratches = template_scratches
        # The total number of scenarios.
        self.total_count = total_count

    def validate(self):
        if self.template_scratches:
            for v1 in self.template_scratches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TemplateScratches'] = []
        if self.template_scratches is not None:
            for k1 in self.template_scratches:
                result['TemplateScratches'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.template_scratches = []
        if m.get('TemplateScratches') is not None:
            for k1 in m.get('TemplateScratches'):
                temp_model = main_models.ListTemplateScratchesResponseBodyTemplateScratches()
                self.template_scratches.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTemplateScratchesResponseBodyTemplateScratches(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        failed_code: str = None,
        logical_id_strategy: str = None,
        preference_parameters: List[main_models.ListTemplateScratchesResponseBodyTemplateScratchesPreferenceParameters] = None,
        resource_group_id: str = None,
        source_resource_group: main_models.ListTemplateScratchesResponseBodyTemplateScratchesSourceResourceGroup = None,
        source_resources: List[main_models.ListTemplateScratchesResponseBodyTemplateScratchesSourceResources] = None,
        source_tag: main_models.ListTemplateScratchesResponseBodyTemplateScratchesSourceTag = None,
        status: str = None,
        status_reason: str = None,
        tags: List[main_models.ListTemplateScratchesResponseBodyTemplateScratchesTags] = None,
        template_scratch_id: str = None,
        template_scratch_type: str = None,
        update_time: str = None,
    ):
        # The time when the resource scenario was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the resource scenario.
        self.description = description
        # The status code of the resource scenario that failed to be generated.
        # 
        # >  This parameter is returned only if the value of Status is GENERATE_FAILED.
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
        # The state of the resource scenario.
        self.status = status
        # The reason why the resource scenario failed to be generated.
        # 
        # >  This parameter is returned only if the value of Status is GENERATE_FAILED.
        self.status_reason = status_reason
        # The tags of the resource scenario.
        self.tags = tags
        # The ID of the resource scenario.
        self.template_scratch_id = template_scratch_id
        # The type of the resource scenario. Valid values:
        # 
        # *   ResourceImport: resource management
        # *   ArchitectureReplication: resource replication
        self.template_scratch_type = template_scratch_type
        # The time when the resource scenario was updated.
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
        if self.tags:
            for v1 in self.tags:
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

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.ListTemplateScratchesResponseBodyTemplateScratchesPreferenceParameters()
                self.preference_parameters.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceResourceGroup') is not None:
            temp_model = main_models.ListTemplateScratchesResponseBodyTemplateScratchesSourceResourceGroup()
            self.source_resource_group = temp_model.from_map(m.get('SourceResourceGroup'))

        self.source_resources = []
        if m.get('SourceResources') is not None:
            for k1 in m.get('SourceResources'):
                temp_model = main_models.ListTemplateScratchesResponseBodyTemplateScratchesSourceResources()
                self.source_resources.append(temp_model.from_map(k1))

        if m.get('SourceTag') is not None:
            temp_model = main_models.ListTemplateScratchesResponseBodyTemplateScratchesSourceTag()
            self.source_tag = temp_model.from_map(m.get('SourceTag'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTemplateScratchesResponseBodyTemplateScratchesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListTemplateScratchesResponseBodyTemplateScratchesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource scenario.
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

class ListTemplateScratchesResponseBodyTemplateScratchesSourceTag(DaraModel):
    def __init__(
        self,
        resource_tags: Dict[str, Any] = None,
        resource_type_filter: List[str] = None,
    ):
        # The source tags.
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

class ListTemplateScratchesResponseBodyTemplateScratchesSourceResources(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
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

class ListTemplateScratchesResponseBodyTemplateScratchesSourceResourceGroup(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_type_filter: List[str] = None,
    ):
        # The ID of the source resource group.
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

class ListTemplateScratchesResponseBodyTemplateScratchesPreferenceParameters(DaraModel):
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

