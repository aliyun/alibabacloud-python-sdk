# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorGroupsRequest(DaraModel):
    def __init__(
        self,
        dynamic_tag_rule_id: str = None,
        group_founder_tag_key: str = None,
        group_founder_tag_value: str = None,
        group_id: str = None,
        group_name: str = None,
        include_template_history: bool = None,
        instance_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        select_contact_groups: bool = None,
        tag: List[main_models.DescribeMonitorGroupsRequestTag] = None,
        type: str = None,
        types: str = None,
    ):
        # The ID of the tag rule.
        self.dynamic_tag_rule_id = dynamic_tag_rule_id
        # The tag key that is created for the application group by using the tag rule.
        self.group_founder_tag_key = group_founder_tag_key
        # The tag value that is created for the application group by using the tag rule.
        self.group_founder_tag_value = group_founder_tag_value
        # The ID of the application group. Separate multiple application group IDs with commas (,).
        self.group_id = group_id
        # The name of the application group.
        self.group_name = group_name
        # Specifies whether to include the historical alert templates that are applied to the application group in the response. Valid values:
        # 
        # *   true
        # *   false
        self.include_template_history = include_template_history
        # The instance ID. This parameter is used to query the application group to which the specified instance belongs.
        self.instance_id = instance_id
        # The keyword that is used for the search.
        self.keyword = keyword
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Pages start from page 1. Default value: 30.
        self.page_size = page_size
        self.region_id = region_id
        # Specifies whether to include the alert contact groups in the response. Valid values:
        # 
        # *   true
        # *   false
        self.select_contact_groups = select_contact_groups
        # The tags of the application group.
        self.tag = tag
        # The type of the application group. Valid values:
        # 
        # *   custom: a self-managed application group
        # *   ehpc_cluster: an application group that is synchronized from an E-HPC cluster
        # *   kubernetes: an application group that is synchronized from an ACK cluster
        self.type = type
        # The type of the application group. Valid values:
        # 
        # *   custom: a self-managed application group
        # *   ehpc_cluster: an application group that is synchronized from an Elastic High Performance Computing (E-HPC) cluster
        # *   kubernetes: an application group that is synchronized from a Container Service for Kubernetes (ACK) cluster
        # *   tag: an application group that is automatically created by using tags
        # *   resMgr: an application group that is created by using resource groups
        # *   ess: an application group that is synchronized from Auto Scaling (ESS)
        self.types = types

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
        if self.dynamic_tag_rule_id is not None:
            result['DynamicTagRuleId'] = self.dynamic_tag_rule_id

        if self.group_founder_tag_key is not None:
            result['GroupFounderTagKey'] = self.group_founder_tag_key

        if self.group_founder_tag_value is not None:
            result['GroupFounderTagValue'] = self.group_founder_tag_value

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.include_template_history is not None:
            result['IncludeTemplateHistory'] = self.include_template_history

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.select_contact_groups is not None:
            result['SelectContactGroups'] = self.select_contact_groups

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicTagRuleId') is not None:
            self.dynamic_tag_rule_id = m.get('DynamicTagRuleId')

        if m.get('GroupFounderTagKey') is not None:
            self.group_founder_tag_key = m.get('GroupFounderTagKey')

        if m.get('GroupFounderTagValue') is not None:
            self.group_founder_tag_value = m.get('GroupFounderTagValue')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IncludeTemplateHistory') is not None:
            self.include_template_history = m.get('IncludeTemplateHistory')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SelectContactGroups') is not None:
            self.select_contact_groups = m.get('SelectContactGroups')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeMonitorGroupsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

class DescribeMonitorGroupsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the application group. Valid values of N: 1 to 5.
        self.key = key
        # The tag value of the application group. Valid values of N: 1 to 5.
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

