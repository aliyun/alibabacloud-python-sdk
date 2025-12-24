# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeAclEntriesResponseBody(DaraModel):
    def __init__(
        self,
        acl_entries: List[main_models.DescribeAclEntriesResponseBodyAclEntries] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The ACL entries.
        self.acl_entries = acl_entries
        # The token that is used to start the next query. If the value of this parameter is empty, all results are returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.acl_entries:
            for v1 in self.acl_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k1 in self.acl_entries:
                result['AclEntries'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k1 in m.get('AclEntries'):
                temp_model = main_models.DescribeAclEntriesResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAclEntriesResponseBodyAclEntries(DaraModel):
    def __init__(
        self,
        policy: str = None,
        source_id: str = None,
        source_type: str = None,
    ):
        # The ACL type.
        # 
        # Valid values:
        # 
        # *   allow: whitelist
        # *   disable: blacklist
        self.policy = policy
        # The ID of the instance to which the ACL applies. You can specify an office network ID or a cloud computer ID.
        self.source_id = source_id
        # The granularity of the ACL.
        # 
        # Valid values:
        # 
        # *   desktop: cloud computer
        # *   vpc: office network
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

