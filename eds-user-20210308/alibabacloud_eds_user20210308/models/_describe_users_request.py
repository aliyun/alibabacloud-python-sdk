# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class DescribeUsersRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        business_channel: str = None,
        end_user_ids: List[str] = None,
        exclude_end_user_ids: List[str] = None,
        exclude_group_id: str = None,
        filter: str = None,
        filter_map: Dict[str, str] = None,
        filter_with_assigned_resource: Dict[str, str] = None,
        filter_with_assigned_resources: Dict[str, bool] = None,
        group_id: str = None,
        is_query_all_sub_orgs: bool = None,
        max_results: int = None,
        next_token: str = None,
        org_id: str = None,
        show_extras: Dict[str, Any] = None,
        solution_id: str = None,
        status: int = None,
    ):
        self.biz_type = biz_type
        self.business_channel = business_channel
        # The usernames that must be exactly matched.
        self.end_user_ids = end_user_ids
        # The usernames that must be exactly excluded.
        self.exclude_end_user_ids = exclude_end_user_ids
        self.exclude_group_id = exclude_group_id
        # The string that is used for fuzzy search. You perform fuzzy search by username (EndUserId) and email address (Email). Wildcard characters (\\*) are supported. For example, if you set this parameter to `a*m`, usernames or email addresses that start with `a` and end with `m` are returned.
        self.filter = filter
        self.filter_map = filter_map
        self.filter_with_assigned_resource = filter_with_assigned_resource
        self.filter_with_assigned_resources = filter_with_assigned_resources
        # The ID of the organization in which you want to query convenience users.
        self.group_id = group_id
        self.is_query_all_sub_orgs = is_query_all_sub_orgs
        # The maximum number of entries per page.
        # 
        # *   Valid values: 1 to 500.
        # *   Default value: 500.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.\\
        # If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the return value of NextToken to perform the next query.
        self.next_token = next_token
        # The ID of the organization in which you want to query users.
        self.org_id = org_id
        self.show_extras = show_extras
        self.solution_id = solution_id
        # The status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids

        if self.exclude_group_id is not None:
            result['ExcludeGroupId'] = self.exclude_group_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.filter_map is not None:
            result['FilterMap'] = self.filter_map

        if self.filter_with_assigned_resource is not None:
            result['FilterWithAssignedResource'] = self.filter_with_assigned_resource

        if self.filter_with_assigned_resources is not None:
            result['FilterWithAssignedResources'] = self.filter_with_assigned_resources

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.is_query_all_sub_orgs is not None:
            result['IsQueryAllSubOrgs'] = self.is_query_all_sub_orgs

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.show_extras is not None:
            result['ShowExtras'] = self.show_extras

        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')

        if m.get('ExcludeGroupId') is not None:
            self.exclude_group_id = m.get('ExcludeGroupId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('FilterMap') is not None:
            self.filter_map = m.get('FilterMap')

        if m.get('FilterWithAssignedResource') is not None:
            self.filter_with_assigned_resource = m.get('FilterWithAssignedResource')

        if m.get('FilterWithAssignedResources') is not None:
            self.filter_with_assigned_resources = m.get('FilterWithAssignedResources')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IsQueryAllSubOrgs') is not None:
            self.is_query_all_sub_orgs = m.get('IsQueryAllSubOrgs')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('ShowExtras') is not None:
            self.show_extras = m.get('ShowExtras')

        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

