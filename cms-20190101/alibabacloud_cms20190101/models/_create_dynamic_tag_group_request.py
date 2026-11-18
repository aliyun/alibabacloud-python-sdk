# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateDynamicTagGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        contact_group_list: List[str] = None,
        dry_run: bool = None,
        enable_install_agent: bool = None,
        enable_subscribe_event: bool = None,
        match_express: List[main_models.CreateDynamicTagGroupRequestMatchExpress] = None,
        match_express_filter_relation: str = None,
        region_id: str = None,
        tag_key: str = None,
        tag_region_id: str = None,
        template_id_list: List[str] = None,
    ):
        # Ensures the idempotence of the request. You can generate a parameter value on your client to ensure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters and can be up to 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The alert contact groups. Valid values of N: 1 to 100. Alert notifications for the application group are sent to the alert contacts in the specified alert contact groups.
        # 
        # An alert contact group contains one or more alert contacts. For more information about how to create alert contacts and alert contact groups, see [PutContact](https://help.aliyun.com/document_detail/114923.html) and [PutContactGroup](https://help.aliyun.com/document_detail/114929.html). For more information about how to query alert contact groups, see [DescribeContactGroupList](https://help.aliyun.com/document_detail/114922.html).
        # 
        # This parameter is required.
        self.contact_group_list = contact_group_list
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: Sends a check request and does not create the queue. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the check fails, the system returns an error. If the check succeeds, the system returns the `DryRunOperation` error code.
        # - **false**: Sends a normal request and creates the queue after the check succeeds. This is the default value.
        self.dry_run = dry_run
        # Specifies whether to enable automatic installation of the CloudMonitor agent for the application group. CloudMonitor automatically installs the CloudMonitor agent on the hosts in the application group. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled. This is the default value.
        self.enable_install_agent = enable_install_agent
        # Specifies whether to enable automatic subscription to event notifications for the application group. When critical or warning events occur on the resources in the application group, CloudMonitor sends alert notifications. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled. This is the default value.
        self.enable_subscribe_event = enable_subscribe_event
        # The match expression used to generate the application group based on tags.
        # 
        # This parameter is required.
        self.match_express = match_express
        # The relationship between the conditional expressions of the resource tag values. Valid values:
        # 
        # - and: AND. This is the default value.
        # - or: OR.
        self.match_express_filter_relation = match_express_filter_relation
        self.region_id = region_id
        # The tag key of the resource.
        # 
        # For more information about how to query the tag keys of resources, see [DescribeTagKeyList](https://help.aliyun.com/document_detail/145558.html).
        # 
        # This parameter is required.
        self.tag_key = tag_key
        # The region ID of the tag.
        self.tag_region_id = tag_region_id
        # The IDs of the alert templates.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.contact_group_list is not None:
            result['ContactGroupList'] = self.contact_group_list

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ContactGroupList') is not None:
            self.contact_group_list = m.get('ContactGroupList')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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
        # The tag key used to create the group. If multiple resources contain this key, the resources that meet the filter conditions are added to the same group based on the same key-value pair.
        self.tag_name = tag_name
        # The resource tag value. Valid values of N: 1.
        # 
        # > You must specify both the `MatchExpress.N.TagValueMatchFunction` and `MatchExpress.N.TagValue` parameters.
        self.tag_value = tag_value
        # The matching method for the resource tag value. Valid values of N: 1. Valid values:
        # - contains: Includes.
        # - startWith: Prefix.
        # - endWith: Suffix.
        # - notContains: Excludes.
        # - equals: Equals.
        # - all: All.
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

