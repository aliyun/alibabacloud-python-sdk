# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImageComponentsResponseBody(DaraModel):
    def __init__(
        self,
        image_component: main_models.DescribeImageComponentsResponseBodyImageComponent = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the image components.
        self.image_component = image_component
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. For information about how to use the returned value, see the "Usage notes" section of this topic.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of image components returned.
        self.total_count = total_count

    def validate(self):
        if self.image_component:
            self.image_component.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_component is not None:
            result['ImageComponent'] = self.image_component.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageComponent') is not None:
            temp_model = main_models.DescribeImageComponentsResponseBodyImageComponent()
            self.image_component = temp_model.from_map(m.get('ImageComponent'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageComponentsResponseBodyImageComponent(DaraModel):
    def __init__(
        self,
        image_component_set: List[main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSet] = None,
    ):
        self.image_component_set = image_component_set

    def validate(self):
        if self.image_component_set:
            for v1 in self.image_component_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageComponentSet'] = []
        if self.image_component_set is not None:
            for k1 in self.image_component_set:
                result['ImageComponentSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_component_set = []
        if m.get('ImageComponentSet') is not None:
            for k1 in m.get('ImageComponentSet'):
                temp_model = main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSet()
                self.image_component_set.append(temp_model.from_map(k1))

        return self

class DescribeImageComponentsResponseBodyImageComponentImageComponentSet(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        component_version: str = None,
        content: str = None,
        creation_time: str = None,
        description: str = None,
        image_component_id: str = None,
        name: str = None,
        owner: str = None,
        parameters: main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSetParameters = None,
        resource_group_id: str = None,
        system_type: str = None,
        tags: main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSetTags = None,
    ):
        # The type of the image component.
        self.component_type = component_type
        # The version number of the image component.
        self.component_version = component_version
        # The content of the image component.
        self.content = content
        # The time when the image component was created.
        self.creation_time = creation_time
        # The description of the image component.
        self.description = description
        # The ID of the image component.
        self.image_component_id = image_component_id
        # The name of the image component.
        self.name = name
        # The type of the image component. Valid values:
        # 
        # *   SELF: the custom component that you created.
        # *   ALIYUN: the system component provided by Alibaba Cloud.
        self.owner = owner
        # The parameters contained in the image component.
        self.parameters = parameters
        # The ID of the resource group to which the image component belongs.
        self.resource_group_id = resource_group_id
        # The type of the operating system supported by the image component.
        self.system_type = system_type
        # The tags of the image component.
        self.tags = tags

    def validate(self):
        if self.parameters:
            self.parameters.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.component_version is not None:
            result['ComponentVersion'] = self.component_version

        if self.content is not None:
            result['Content'] = self.content

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.image_component_id is not None:
            result['ImageComponentId'] = self.image_component_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('ComponentVersion') is not None:
            self.component_version = m.get('ComponentVersion')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageComponentId') is not None:
            self.image_component_id = m.get('ImageComponentId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Parameters') is not None:
            temp_model = main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSetParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeImageComponentsResponseBodyImageComponentImageComponentSetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSetTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeImageComponentsResponseBodyImageComponentImageComponentSetTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeImageComponentsResponseBodyImageComponentImageComponentSetParameters(DaraModel):
    def __init__(
        self,
        parameter: List[main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSetParametersParameter] = None,
    ):
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            for v1 in self.parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Parameter'] = []
        if self.parameter is not None:
            for k1 in self.parameter:
                result['Parameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter = []
        if m.get('Parameter') is not None:
            for k1 in m.get('Parameter'):
                temp_model = main_models.DescribeImageComponentsResponseBodyImageComponentImageComponentSetParametersParameter()
                self.parameter.append(temp_model.from_map(k1))

        return self

class DescribeImageComponentsResponseBodyImageComponentImageComponentSetParametersParameter(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        name: str = None,
        type: str = None,
    ):
        # The default value of the parameter.
        self.default_value = default_value
        # The name of the parameter.
        self.name = name
        # The type of the parameter.
        # 
        # Valid values:
        # 
        # *   String
        # *   Number
        # *   Boolean
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

