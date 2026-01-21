# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeDynamicTagRuleListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: bool = None,
        tag_group_list: main_models.DescribeDynamicTagRuleListResponseBodyTagGroupList = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the call was successful.
        self.code = code
        # The error message.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   true: The call was successful.
        # *   false: The call failed.
        self.success = success
        # The tag rules of application groups.
        self.tag_group_list = tag_group_list
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.tag_group_list:
            self.tag_group_list.validate()

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

        if self.success is not None:
            result['Success'] = self.success

        if self.tag_group_list is not None:
            result['TagGroupList'] = self.tag_group_list.to_map()

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

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TagGroupList') is not None:
            temp_model = main_models.DescribeDynamicTagRuleListResponseBodyTagGroupList()
            self.tag_group_list = temp_model.from_map(m.get('TagGroupList'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDynamicTagRuleListResponseBodyTagGroupList(DaraModel):
    def __init__(
        self,
        tag_group: List[main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroup] = None,
    ):
        self.tag_group = tag_group

    def validate(self):
        if self.tag_group:
            for v1 in self.tag_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagGroup'] = []
        if self.tag_group is not None:
            for k1 in self.tag_group:
                result['TagGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_group = []
        if m.get('TagGroup') is not None:
            for k1 in m.get('TagGroup'):
                temp_model = main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroup()
                self.tag_group.append(temp_model.from_map(k1))

        return self

class DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroup(DaraModel):
    def __init__(
        self,
        contact_group_list: main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupContactGroupList = None,
        dynamic_tag_rule_id: str = None,
        match_express: main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupMatchExpress = None,
        match_express_filter_relation: str = None,
        region_id: str = None,
        status: str = None,
        tag_key: str = None,
        tag_value_blacklist: main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupTagValueBlacklist = None,
        template_id_list: main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupTemplateIdList = None,
    ):
        # The alert contact group.
        self.contact_group_list = contact_group_list
        # The ID of the tag rule.
        self.dynamic_tag_rule_id = dynamic_tag_rule_id
        # The conditional expressions used to create an application group based on the tag.
        self.match_express = match_express
        # The logical operator that is used between conditional expressions. Valid values:
        # 
        # *   `and`
        # *   `or`
        # 
        # >  Only one logical operator can be used in a request.
        self.match_express_filter_relation = match_express_filter_relation
        # The ID of the region to which the tags belong.
        self.region_id = region_id
        # The status of adding instances that meet the tag rule to the application group. Valid values:
        # 
        # *   `RUNNING`
        # *   `FINISH`
        self.status = status
        # The tag key.
        self.tag_key = tag_key
        self.tag_value_blacklist = tag_value_blacklist
        # The IDs of the alert templates.
        self.template_id_list = template_id_list

    def validate(self):
        if self.contact_group_list:
            self.contact_group_list.validate()
        if self.match_express:
            self.match_express.validate()
        if self.tag_value_blacklist:
            self.tag_value_blacklist.validate()
        if self.template_id_list:
            self.template_id_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_list is not None:
            result['ContactGroupList'] = self.contact_group_list.to_map()

        if self.dynamic_tag_rule_id is not None:
            result['DynamicTagRuleId'] = self.dynamic_tag_rule_id

        if self.match_express is not None:
            result['MatchExpress'] = self.match_express.to_map()

        if self.match_express_filter_relation is not None:
            result['MatchExpressFilterRelation'] = self.match_express_filter_relation

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value_blacklist is not None:
            result['TagValueBlacklist'] = self.tag_value_blacklist.to_map()

        if self.template_id_list is not None:
            result['TemplateIdList'] = self.template_id_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupList') is not None:
            temp_model = main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupContactGroupList()
            self.contact_group_list = temp_model.from_map(m.get('ContactGroupList'))

        if m.get('DynamicTagRuleId') is not None:
            self.dynamic_tag_rule_id = m.get('DynamicTagRuleId')

        if m.get('MatchExpress') is not None:
            temp_model = main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupMatchExpress()
            self.match_express = temp_model.from_map(m.get('MatchExpress'))

        if m.get('MatchExpressFilterRelation') is not None:
            self.match_express_filter_relation = m.get('MatchExpressFilterRelation')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValueBlacklist') is not None:
            temp_model = main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupTagValueBlacklist()
            self.tag_value_blacklist = temp_model.from_map(m.get('TagValueBlacklist'))

        if m.get('TemplateIdList') is not None:
            temp_model = main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupTemplateIdList()
            self.template_id_list = temp_model.from_map(m.get('TemplateIdList'))

        return self

class DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupTemplateIdList(DaraModel):
    def __init__(
        self,
        template_id_list: List[str] = None,
    ):
        self.template_id_list = template_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_id_list is not None:
            result['TemplateIdList'] = self.template_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateIdList') is not None:
            self.template_id_list = m.get('TemplateIdList')

        return self

class DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupTagValueBlacklist(DaraModel):
    def __init__(
        self,
        tag_value_blacklist: List[str] = None,
    ):
        self.tag_value_blacklist = tag_value_blacklist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_value_blacklist is not None:
            result['TagValueBlacklist'] = self.tag_value_blacklist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValueBlacklist') is not None:
            self.tag_value_blacklist = m.get('TagValueBlacklist')

        return self

class DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupMatchExpress(DaraModel):
    def __init__(
        self,
        match_express: List[main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupMatchExpressMatchExpress] = None,
    ):
        self.match_express = match_express

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
        result['MatchExpress'] = []
        if self.match_express is not None:
            for k1 in self.match_express:
                result['MatchExpress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match_express = []
        if m.get('MatchExpress') is not None:
            for k1 in m.get('MatchExpress'):
                temp_model = main_models.DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupMatchExpressMatchExpress()
                self.match_express.append(temp_model.from_map(k1))

        return self

class DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupMatchExpressMatchExpress(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
        tag_value_match_function: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        # 
        # The `TagValue` and `TagValueMatchFunction` parameters must be used in pairs.
        self.tag_value = tag_value
        # The method that is used to match tag values. Valid values:
        # 
        # *   all: includes all
        # *   startWith: starts with a prefix
        # *   endWith: ends with a suffix
        # *   contains: contains
        # *   notContains: does not contain
        # *   equals: equals
        self.tag_value_match_function = tag_value_match_function

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

        if self.tag_value_match_function is not None:
            result['TagValueMatchFunction'] = self.tag_value_match_function

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('TagValueMatchFunction') is not None:
            self.tag_value_match_function = m.get('TagValueMatchFunction')

        return self

class DescribeDynamicTagRuleListResponseBodyTagGroupListTagGroupContactGroupList(DaraModel):
    def __init__(
        self,
        contact_group_list: List[str] = None,
    ):
        self.contact_group_list = contact_group_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_list is not None:
            result['ContactGroupList'] = self.contact_group_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupList') is not None:
            self.contact_group_list = m.get('ContactGroupList')

        return self

