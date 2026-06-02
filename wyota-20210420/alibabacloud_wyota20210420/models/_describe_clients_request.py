# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeClientsRequest(DaraModel):
    def __init__(
        self,
        caller_ali_uid: str = None,
        client_type: int = None,
        custom_resource_id: str = None,
        custom_resource_status: bool = None,
        in_manage: bool = None,
        include_sub_groups: bool = None,
        max_results: int = None,
        model: str = None,
        next_token: str = None,
        online_status: bool = None,
        platform: str = None,
        search_keyword: str = None,
        terminal_group_id: str = None,
        uuids: List[str] = None,
        with_bind_user: bool = None,
    ):
        # aliuid
        self.caller_ali_uid = caller_ali_uid
        # This parameter is required.
        self.client_type = client_type
        self.custom_resource_id = custom_resource_id
        self.custom_resource_status = custom_resource_status
        self.in_manage = in_manage
        self.include_sub_groups = include_sub_groups
        self.max_results = max_results
        self.model = model
        self.next_token = next_token
        self.online_status = online_status
        self.platform = platform
        self.search_keyword = search_keyword
        self.terminal_group_id = terminal_group_id
        self.uuids = uuids
        self.with_bind_user = with_bind_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_ali_uid is not None:
            result['CallerAliUid'] = self.caller_ali_uid

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.custom_resource_id is not None:
            result['CustomResourceId'] = self.custom_resource_id

        if self.custom_resource_status is not None:
            result['CustomResourceStatus'] = self.custom_resource_status

        if self.in_manage is not None:
            result['InManage'] = self.in_manage

        if self.include_sub_groups is not None:
            result['IncludeSubGroups'] = self.include_sub_groups

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.model is not None:
            result['Model'] = self.model

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.search_keyword is not None:
            result['SearchKeyword'] = self.search_keyword

        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        if self.with_bind_user is not None:
            result['WithBindUser'] = self.with_bind_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerAliUid') is not None:
            self.caller_ali_uid = m.get('CallerAliUid')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('CustomResourceId') is not None:
            self.custom_resource_id = m.get('CustomResourceId')

        if m.get('CustomResourceStatus') is not None:
            self.custom_resource_status = m.get('CustomResourceStatus')

        if m.get('InManage') is not None:
            self.in_manage = m.get('InManage')

        if m.get('IncludeSubGroups') is not None:
            self.include_sub_groups = m.get('IncludeSubGroups')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SearchKeyword') is not None:
            self.search_keyword = m.get('SearchKeyword')

        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        if m.get('WithBindUser') is not None:
            self.with_bind_user = m.get('WithBindUser')

        return self

