# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: main_models.DescribeMonitorGroupsResponseBodyResources = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The resources that are associated with the application group.
        self.resources = resources
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            temp_model = main_models.DescribeMonitorGroupsResponseBodyResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMonitorGroupsResponseBodyResources(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeMonitorGroupsResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeMonitorGroupsResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupsResponseBodyResourcesResource(DaraModel):
    def __init__(
        self,
        bind_url: str = None,
        contact_groups: main_models.DescribeMonitorGroupsResponseBodyResourcesResourceContactGroups = None,
        dynamic_tag_rule_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_founder_tag_key: str = None,
        group_founder_tag_value: str = None,
        group_id: int = None,
        group_name: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        tags: main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTags = None,
        template_ids: main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTemplateIds = None,
        template_infos: main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTemplateInfos = None,
        type: str = None,
    ):
        # The URL of the ACK cluster from which the application group is synchronized.
        self.bind_url = bind_url
        # The alert contact groups.
        self.contact_groups = contact_groups
        # The ID of the tag rule.
        self.dynamic_tag_rule_id = dynamic_tag_rule_id
        # The timestamp when the application group was created. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The timestamp when the application group was modified. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The tag key that is created for the application group by using the tag rule.
        self.group_founder_tag_key = group_founder_tag_key
        # The tag value that is created for the application group by using the tag rule.
        self.group_founder_tag_value = group_founder_tag_value
        # The ID of the application group.
        self.group_id = group_id
        # The name of the application group.
        self.group_name = group_name
        # The resource ID.
        self.resource_group_id = resource_group_id
        # The ID of the Alibaba Cloud service.
        self.service_id = service_id
        # The tags that are attached to the application group.
        self.tags = tags
        # The ID of the template.
        self.template_ids = template_ids
        self.template_infos = template_infos
        # The type of the application group. Valid values:
        # 
        # *   custom: a self-managed application group
        # *   ehpc_cluster: an application group that is synchronized from an E-HPC cluster
        # *   kubernetes: an application group that is synchronized from an ACK cluster
        self.type = type

    def validate(self):
        if self.contact_groups:
            self.contact_groups.validate()
        if self.tags:
            self.tags.validate()
        if self.template_ids:
            self.template_ids.validate()
        if self.template_infos:
            self.template_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_url is not None:
            result['BindUrl'] = self.bind_url

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()

        if self.dynamic_tag_rule_id is not None:
            result['DynamicTagRuleId'] = self.dynamic_tag_rule_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_founder_tag_key is not None:
            result['GroupFounderTagKey'] = self.group_founder_tag_key

        if self.group_founder_tag_value is not None:
            result['GroupFounderTagValue'] = self.group_founder_tag_value

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids.to_map()

        if self.template_infos is not None:
            result['TemplateInfos'] = self.template_infos.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrl') is not None:
            self.bind_url = m.get('BindUrl')

        if m.get('ContactGroups') is not None:
            temp_model = main_models.DescribeMonitorGroupsResponseBodyResourcesResourceContactGroups()
            self.contact_groups = temp_model.from_map(m.get('ContactGroups'))

        if m.get('DynamicTagRuleId') is not None:
            self.dynamic_tag_rule_id = m.get('DynamicTagRuleId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupFounderTagKey') is not None:
            self.group_founder_tag_key = m.get('GroupFounderTagKey')

        if m.get('GroupFounderTagValue') is not None:
            self.group_founder_tag_value = m.get('GroupFounderTagValue')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TemplateIds') is not None:
            temp_model = main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTemplateIds()
            self.template_ids = temp_model.from_map(m.get('TemplateIds'))

        if m.get('TemplateInfos') is not None:
            temp_model = main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTemplateInfos()
            self.template_infos = temp_model.from_map(m.get('TemplateInfos'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeMonitorGroupsResponseBodyResourcesResourceTemplateInfos(DaraModel):
    def __init__(
        self,
        template_info: List[main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTemplateInfosTemplateInfo] = None,
    ):
        self.template_info = template_info

    def validate(self):
        if self.template_info:
            for v1 in self.template_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TemplateInfo'] = []
        if self.template_info is not None:
            for k1 in self.template_info:
                result['TemplateInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template_info = []
        if m.get('TemplateInfo') is not None:
            for k1 in m.get('TemplateInfo'):
                temp_model = main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTemplateInfosTemplateInfo()
                self.template_info.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupsResponseBodyResourcesResourceTemplateInfosTemplateInfo(DaraModel):
    def __init__(
        self,
        effect_time: int = None,
        template_id: str = None,
        ver: str = None,
    ):
        self.effect_time = effect_time
        self.template_id = template_id
        self.ver = ver

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.ver is not None:
            result['Ver'] = self.ver

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Ver') is not None:
            self.ver = m.get('Ver')

        return self

class DescribeMonitorGroupsResponseBodyResourcesResourceTemplateIds(DaraModel):
    def __init__(
        self,
        template_id: List[str] = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class DescribeMonitorGroupsResponseBodyResourcesResourceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTagsTag] = None,
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
                temp_model = main_models.DescribeMonitorGroupsResponseBodyResourcesResourceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupsResponseBodyResourcesResourceTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the application group.
        self.key = key
        # The tag value of the application group.
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

class DescribeMonitorGroupsResponseBodyResourcesResourceContactGroups(DaraModel):
    def __init__(
        self,
        contact_group: List[main_models.DescribeMonitorGroupsResponseBodyResourcesResourceContactGroupsContactGroup] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        if self.contact_group:
            for v1 in self.contact_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactGroup'] = []
        if self.contact_group is not None:
            for k1 in self.contact_group:
                result['ContactGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_group = []
        if m.get('ContactGroup') is not None:
            for k1 in m.get('ContactGroup'):
                temp_model = main_models.DescribeMonitorGroupsResponseBodyResourcesResourceContactGroupsContactGroup()
                self.contact_group.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupsResponseBodyResourcesResourceContactGroupsContactGroup(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the alert contact group.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

