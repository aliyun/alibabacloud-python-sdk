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
        # The alert contact groups. The value of N can be from 1 to 100. Alert notifications for the application group are sent to the alert contacts in these alert contact groups.
        # 
        # An alert contact group can contain one or more alert contacts. For more information about how to create alert contacts and alert contact groups, see [PutContact](https://help.aliyun.com/document_detail/114923.html) and [PutContactGroup](https://help.aliyun.com/document_detail/114929.html). For more information about how to obtain alert contact groups, see [DescribeContactGroupList](https://help.aliyun.com/document_detail/114922.html).
        # 
        # This parameter is required.
        self.contact_group_list = contact_group_list
        # Specifies whether to automatically install the CloudMonitor agent for the application group. CloudMonitor automatically installs the agent on the hosts in the application group. Valid values:
        # 
        # - true: enabled.
        # 
        # - false (default): disabled.
        self.enable_install_agent = enable_install_agent
        # Specifies whether to automatically subscribe to event notifications for the application group. When a critical or warning event occurs on a resource in the application group, CloudMonitor sends an alert notification. Valid values:
        # 
        # - true: enabled.
        # 
        # - false (default): disabled.
        self.enable_subscribe_event = enable_subscribe_event
        # The match expressions that are used to create an application group from tags.
        # 
        # This parameter is required.
        self.match_express = match_express
        # The relationship between the conditional expressions for the tag values. Valid values:
        # 
        # - and (default)
        # 
        # - or
        self.match_express_filter_relation = match_express_filter_relation
        self.region_id = region_id
        # The tag key of the resource.
        # 
        # For more information about how to query the tag keys of resources, see [DescribeTagKeyList](https://help.aliyun.com/document_detail/145558.html).
        # 
        # This parameter is required.
        self.tag_key = tag_key
        # The ID of the region to which the tag belongs.
        self.tag_region_id = tag_region_id
        # The ID of the alert template.
        # 
        # For more information about how to query the IDs of alert templates, see [DescribeMetricRuleTemplateList](https://help.aliyun.com/document_detail/114982.html).
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
        # The key of the tag that is used to create the group. If multiple resources have this tag key, the resources that meet the filter conditions are added to the same group based on the same key-value pair.
        self.tag_name = tag_name
        # The value of the resource tag. The value of N is 1.
        # 
        # > You must specify both the `MatchExpress.N.TagValueMatchFunction` and `MatchExpress.N.TagValue` parameters.
        self.tag_value = tag_value
        # The method that is used to match the values of resource tags. The value of N is 1. Valid values:
        # 
        # - contains: includes.
        # 
        # - startWith: prefix.
        # 
        # - endWith: suffix.
        # 
        # - notContains: does not include.
        # 
        # - equals: equals.
        # 
        # - all: all.
        # 
        # > You must specify both the `MatchExpress.N.TagValueMatchFunction` and `MatchExpress.N.TagValue` parameters.
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

