# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkspacesRequest(DaraModel):
    def __init__(
        self,
        already_joined: bool = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        search_key: str = None,
        service_account_id: int = None,
        vpc_id: str = None,
        workspace_id: int = None,
    ):
        # Specifies whether the current user has joined the workspace.
        self.already_joined = already_joined
        self.owner_id = owner_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region in which the bucket is located.
        self.region = region
        # The search keyword. Fuzzy match is supported.
        self.search_key = search_key
        # The service account ID.
        self.service_account_id = service_account_id
        # The virtual private cloud (VPC) ID.
        # 
        # > This parameter cannot be used as a filter.
        self.vpc_id = vpc_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_joined is not None:
            result['AlreadyJoined'] = self.already_joined

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.service_account_id is not None:
            result['ServiceAccountId'] = self.service_account_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlreadyJoined') is not None:
            self.already_joined = m.get('AlreadyJoined')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('ServiceAccountId') is not None:
            self.service_account_id = m.get('ServiceAccountId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

