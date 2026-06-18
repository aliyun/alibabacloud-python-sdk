# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListBranchesResponseBody(DaraModel):
    def __init__(
        self,
        branches: main_models.ListBranchesResponseBodyBranches = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.branches = branches
        # The maximum number of records returned in this query.
        self.max_results = max_results
        # The pagination token. It is not required for the first query. For subsequent queries, use the NextToken returned from the previous query.
        self.next_token = next_token
        # The page number. The value must be greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of records per page.
        # 
        # Valid values:
        # - 10
        # - 20
        # - 50
        # - 100
        # 
        # Default value: 20.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of branches that match the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.branches:
            self.branches.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branches is not None:
            result['Branches'] = self.branches.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branches') is not None:
            temp_model = main_models.ListBranchesResponseBodyBranches()
            self.branches = temp_model.from_map(m.get('Branches'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBranchesResponseBodyBranches(DaraModel):
    def __init__(
        self,
        branch: List[main_models.ListBranchesResponseBodyBranchesBranch] = None,
    ):
        self.branch = branch

    def validate(self):
        if self.branch:
            for v1 in self.branch:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Branch'] = []
        if self.branch is not None:
            for k1 in self.branch:
                result['Branch'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.branch = []
        if m.get('Branch') is not None:
            for k1 in m.get('Branch'):
                temp_model = main_models.ListBranchesResponseBodyBranchesBranch()
                self.branch.append(temp_model.from_map(k1))

        return self

class ListBranchesResponseBodyBranchesBranch(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        branch_name: str = None,
        create_time: str = None,
        description: str = None,
        expires_at: str = None,
        init_source: str = None,
        is_default: bool = None,
        parent_branch_id: str = None,
        parent_branch_name: str = None,
        parent_lsn: str = None,
        parent_timestamp: str = None,
        project_id: str = None,
        protected: bool = None,
        service_type: str = None,
        status: str = None,
        tags: main_models.ListBranchesResponseBodyBranchesBranchTags = None,
    ):
        self.branch_id = branch_id
        self.branch_name = branch_name
        self.create_time = create_time
        self.description = description
        self.expires_at = expires_at
        self.init_source = init_source
        self.is_default = is_default
        self.parent_branch_id = parent_branch_id
        self.parent_branch_name = parent_branch_name
        self.parent_lsn = parent_lsn
        self.parent_timestamp = parent_timestamp
        self.project_id = project_id
        self.protected = protected
        self.service_type = service_type
        self.status = status
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.init_source is not None:
            result['InitSource'] = self.init_source

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.parent_branch_id is not None:
            result['ParentBranchId'] = self.parent_branch_id

        if self.parent_branch_name is not None:
            result['ParentBranchName'] = self.parent_branch_name

        if self.parent_lsn is not None:
            result['ParentLSN'] = self.parent_lsn

        if self.parent_timestamp is not None:
            result['ParentTimestamp'] = self.parent_timestamp

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.protected is not None:
            result['Protected'] = self.protected

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('InitSource') is not None:
            self.init_source = m.get('InitSource')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ParentBranchId') is not None:
            self.parent_branch_id = m.get('ParentBranchId')

        if m.get('ParentBranchName') is not None:
            self.parent_branch_name = m.get('ParentBranchName')

        if m.get('ParentLSN') is not None:
            self.parent_lsn = m.get('ParentLSN')

        if m.get('ParentTimestamp') is not None:
            self.parent_timestamp = m.get('ParentTimestamp')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Protected') is not None:
            self.protected = m.get('Protected')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.ListBranchesResponseBodyBranchesBranchTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class ListBranchesResponseBodyBranchesBranchTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.ListBranchesResponseBodyBranchesBranchTagsTag] = None,
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
                temp_model = main_models.ListBranchesResponseBodyBranchesBranchTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListBranchesResponseBodyBranchesBranchTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

