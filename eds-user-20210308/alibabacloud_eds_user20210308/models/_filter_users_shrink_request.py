# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class FilterUsersShrinkRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        exclude_end_user_ids: List[str] = None,
        filter: str = None,
        filter_map_shrink: str = None,
        include_desktop_count: bool = None,
        include_desktop_group_count: bool = None,
        include_end_user_ids: List[str] = None,
        include_org_info: bool = None,
        include_support_idps: bool = None,
        is_query_all_sub_orgs: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_param_shrink: str = None,
        org_id: str = None,
        owner_type: str = None,
        property_filter_param: List[main_models.FilterUsersShrinkRequestPropertyFilterParam] = None,
        property_key_value_filter_param: List[main_models.FilterUsersShrinkRequestPropertyKeyValueFilterParam] = None,
        show_extras: Dict[str, str] = None,
        status: int = None,
    ):
        # The channel.
        self.business_channel = business_channel
        # The list of usernames (EndUserIds) to exclude by exact match.
        self.exclude_end_user_ids = exclude_end_user_ids
        # The fuzzy search string. This parameter supports matching the username (EndUserId) and email address (Email). Wildcards (*) are supported. For example, if you set this parameter to a*m, all results where the username or email address starts with a and ends with m are returned.
        self.filter = filter
        # The fuzzy match condition mapping for user information. This parameter supports fields such as the username, remarks, phone number, email address, nickname, and employee ID.
        self.filter_map_shrink = filter_map_shrink
        # Specifies whether to return the number of cloud computers assigned to the user.
        self.include_desktop_count = include_desktop_count
        # Specifies whether to return the number of cloud computer pools assigned to the user.
        self.include_desktop_group_count = include_desktop_group_count
        # The list of convenience account usernames to include in the query results.
        self.include_end_user_ids = include_end_user_ids
        # Specifies whether to include organization information.
        self.include_org_info = include_org_info
        # Specifies whether to include the supported logon types.
        self.include_support_idps = include_support_idps
        # Specifies whether to query all sub-organizations.
        self.is_query_all_sub_orgs = is_query_all_sub_orgs
        # The number of entries per page in a paged query. If the value exceeds 100, it is automatically reset to 100.
        self.max_results = max_results
        # The token for the next query. You do not need to specify this parameter when you call this operation for the first time. If the response does not contain all results, a non-empty NextToken is returned. You can use the returned NextToken in subsequent queries to obtain the remaining results.
        self.next_token = next_token
        # The supported sorting parameters.
        self.order_param_shrink = order_param_shrink
        # The ID of the enterprise organization.
        self.org_id = org_id
        # The account activation type.
        self.owner_type = owner_type
        # The list of user attributes for fuzzy queries.
        self.property_filter_param = property_filter_param
        # The list of attribute names and attribute values.
        self.property_key_value_filter_param = property_key_value_filter_param
        # The switch mapping for additional response information. This parameter controls whether to include desktop policy information.
        self.show_extras = show_extras
        # The user status used to filter results.
        self.status = status

    def validate(self):
        if self.property_filter_param:
            for v1 in self.property_filter_param:
                 if v1:
                    v1.validate()
        if self.property_key_value_filter_param:
            for v1 in self.property_key_value_filter_param:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.filter_map_shrink is not None:
            result['FilterMap'] = self.filter_map_shrink

        if self.include_desktop_count is not None:
            result['IncludeDesktopCount'] = self.include_desktop_count

        if self.include_desktop_group_count is not None:
            result['IncludeDesktopGroupCount'] = self.include_desktop_group_count

        if self.include_end_user_ids is not None:
            result['IncludeEndUserIds'] = self.include_end_user_ids

        if self.include_org_info is not None:
            result['IncludeOrgInfo'] = self.include_org_info

        if self.include_support_idps is not None:
            result['IncludeSupportIdps'] = self.include_support_idps

        if self.is_query_all_sub_orgs is not None:
            result['IsQueryAllSubOrgs'] = self.is_query_all_sub_orgs

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_param_shrink is not None:
            result['OrderParam'] = self.order_param_shrink

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        result['PropertyFilterParam'] = []
        if self.property_filter_param is not None:
            for k1 in self.property_filter_param:
                result['PropertyFilterParam'].append(k1.to_map() if k1 else None)

        result['PropertyKeyValueFilterParam'] = []
        if self.property_key_value_filter_param is not None:
            for k1 in self.property_key_value_filter_param:
                result['PropertyKeyValueFilterParam'].append(k1.to_map() if k1 else None)

        if self.show_extras is not None:
            result['ShowExtras'] = self.show_extras

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('FilterMap') is not None:
            self.filter_map_shrink = m.get('FilterMap')

        if m.get('IncludeDesktopCount') is not None:
            self.include_desktop_count = m.get('IncludeDesktopCount')

        if m.get('IncludeDesktopGroupCount') is not None:
            self.include_desktop_group_count = m.get('IncludeDesktopGroupCount')

        if m.get('IncludeEndUserIds') is not None:
            self.include_end_user_ids = m.get('IncludeEndUserIds')

        if m.get('IncludeOrgInfo') is not None:
            self.include_org_info = m.get('IncludeOrgInfo')

        if m.get('IncludeSupportIdps') is not None:
            self.include_support_idps = m.get('IncludeSupportIdps')

        if m.get('IsQueryAllSubOrgs') is not None:
            self.is_query_all_sub_orgs = m.get('IsQueryAllSubOrgs')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderParam') is not None:
            self.order_param_shrink = m.get('OrderParam')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        self.property_filter_param = []
        if m.get('PropertyFilterParam') is not None:
            for k1 in m.get('PropertyFilterParam'):
                temp_model = main_models.FilterUsersShrinkRequestPropertyFilterParam()
                self.property_filter_param.append(temp_model.from_map(k1))

        self.property_key_value_filter_param = []
        if m.get('PropertyKeyValueFilterParam') is not None:
            for k1 in m.get('PropertyKeyValueFilterParam'):
                temp_model = main_models.FilterUsersShrinkRequestPropertyKeyValueFilterParam()
                self.property_key_value_filter_param.append(temp_model.from_map(k1))

        if m.get('ShowExtras') is not None:
            self.show_extras = m.get('ShowExtras')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class FilterUsersShrinkRequestPropertyKeyValueFilterParam(DaraModel):
    def __init__(
        self,
        property_key: str = None,
        property_values: str = None,
    ):
        # The name of the attribute.
        self.property_key = property_key
        # The values of the attribute.
        self.property_values = property_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key

        if self.property_values is not None:
            result['PropertyValues'] = self.property_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')

        if m.get('PropertyValues') is not None:
            self.property_values = m.get('PropertyValues')

        return self

class FilterUsersShrinkRequestPropertyFilterParam(DaraModel):
    def __init__(
        self,
        property_id: int = None,
        property_value_ids: str = None,
    ):
        # The ID of the attribute.
        self.property_id = property_id
        # The IDs of the attribute values.
        self.property_value_ids = property_value_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_id is not None:
            result['PropertyId'] = self.property_id

        if self.property_value_ids is not None:
            result['PropertyValueIds'] = self.property_value_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        if m.get('PropertyValueIds') is not None:
            self.property_value_ids = m.get('PropertyValueIds')

        return self

