# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateDynamicTagGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_list: List[str] = None,
        enable_install_agent: bool = None,
        enable_subscribe_event: bool = None,
        match_express: List[main_models.CreateDynamicTagGroupRequestMatchExpress] = None,
        match_express_filter_relation: str = None,
        region_id: str = None,
        tag_key: str = None,
        tag_region_id: str = None,
        template_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.contact_group_list = contact_group_list
        # Specifies whether the CloudMonitor agent is automatically installed for the application group. CloudMonitor determines whether to automatically install the CloudMonitor agent for the hosts in an application group based on the value of this parameter. Valid values:
        # 
        # *   true: The CloudMonitor agent is automatically installed.
        # *   false (default value): The CloudMonitor agent is not automatically installed.
        self.enable_install_agent = enable_install_agent
        # Specifies whether the application group automatically subscribes to event notifications. If events whose severity level is critical or warning occur on resources in an application group, CloudMonitor sends alert notifications. Valid values:
        # 
        # *   true: The application group automatically subscribes to event notifications.
        # *   false (default value): The application group does not automatically subscribe to event notifications.
        self.enable_subscribe_event = enable_subscribe_event
        # The conditional expressions used to create an application group based on the tag.
        # 
        # This parameter is required.
        self.match_express = match_express
        # The relationship between the conditional expressions for the tag values of the cloud resources. Valid values:
        # 
        # *   and (default)
        # *   or
        self.match_express_filter_relation = match_express_filter_relation
        self.region_id = region_id
        # The tag keys of the cloud resources.
        # 
        # For more information about how to obtain tag keys, see [DescribeTagKeyList](https://help.aliyun.com/document_detail/145558.html).
        # 
        # This parameter is required.
        self.tag_key = tag_key
        # The ID of the region to which the tags belong.
        self.tag_region_id = tag_region_id
        self.template_id_list = template_id_list

    def validate(self):
        if self.match_express:
            for v1 in self.match_express:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_list is not None:
            result['ContactGroupList'] = self.contact_group_list

        if self.enable_install_agent is not None:
            result['EnableInstallAgent'] = self.enable_install_agent

        if self.enable_subscribe_event is not None:
            result['EnableSubscribeEvent'] = self.enable_subscribe_event

        result['MatchExpress'] = []
        if self.match_express is not None:
            for k1 in self.match_express:
                result['MatchExpress'].append(k1.to_map() if k1 else None)

        if self.match_express_filter_relation is not None:
            result['MatchExpressFilterRelation'] = self.match_express_filter_relation

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_region_id is not None:
            result['TagRegionId'] = self.tag_region_id

        if self.template_id_list is not None:
            result['TemplateIdList'] = self.template_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupList') is not None:
            self.contact_group_list = m.get('ContactGroupList')

        if m.get('EnableInstallAgent') is not None:
            self.enable_install_agent = m.get('EnableInstallAgent')

        if m.get('EnableSubscribeEvent') is not None:
            self.enable_subscribe_event = m.get('EnableSubscribeEvent')

        self.match_express = []
        if m.get('MatchExpress') is not None:
            for k1 in m.get('MatchExpress'):
                temp_model = main_models.CreateDynamicTagGroupRequestMatchExpress()
                self.match_express.append(temp_model.from_map(k1))

        if m.get('MatchExpressFilterRelation') is not None:
            self.match_express_filter_relation = m.get('MatchExpressFilterRelation')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagRegionId') is not None:
            self.tag_region_id = m.get('TagRegionId')

        if m.get('TemplateIdList') is not None:
            self.template_id_list = m.get('TemplateIdList')

        return self

class CreateDynamicTagGroupRequestMatchExpress(DaraModel):
    def __init__(
        self,
        tag_name: str = None,
        tag_value: str = None,
        tag_value_match_function: str = None,
    ):
        # The keys of the tags that are used to create the application group. If a specified key is attached to multiple resources, the resources that have the same key-value pair are added to the same group.
        self.tag_name = tag_name
        # The tag values of the cloud resources. Set the value of N to 1.
        # 
        # >  If you set the `MatchExpress.N.TagValueMatchFunction` parameter, you must also set the `MatchExpress.N.TagValue` parameter.
        self.tag_value = tag_value
        # The method that is used to match the tag values of the cloud resources. Set the value of N to 1. Valid values:
        # 
        # *   contains: contains
        # *   startWith: starts with a prefix
        # *   endWith: ends with a suffix
        # *   notContains: does not contain
        # *   equals: equals
        # *   all: matches all
        # 
        # >  If you set the `MatchExpress.N.TagValueMatchFunction` parameter, you must also set the `MatchExpress.N.TagValue` parameter.
        self.tag_value_match_function = tag_value_match_function

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.tag_value_match_function is not None:
            result['TagValueMatchFunction'] = self.tag_value_match_function

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('TagValueMatchFunction') is not None:
            self.tag_value_match_function = m.get('TagValueMatchFunction')

        return self

