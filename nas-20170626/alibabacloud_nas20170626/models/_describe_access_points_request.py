# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessPointsRequest(DaraModel):
    def __init__(
        self,
        access_group: str = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
        tag: List[main_models.DescribeAccessPointsRequestTag] = None,
    ):
        # The permission group name.
        # 
        # This parameter is required if the file system is a General-purpose NAS file system.
        # 
        # Default permission group: DEFAULT_VPC_GROUP_NAME (the default VPC permission group).
        self.access_group = access_group
        # The file system ID.
        self.file_system_id = file_system_id
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The query token. Set the value to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The list of access point tags.
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
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAccessPointsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAccessPointsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # Limits:
        # 
        # - Valid values of N: 1 to 20.
        # - The tag key can be up to 128 characters in length.
        # - The tag key cannot start with aliyun or acs:.
        # - The tag key cannot contain http:// or https://.
        self.key = key
        # The tag value.
        # 
        # Limits:
        # 
        # - Valid values of N: 1 to 20.
        # - The tag value can be up to 128 characters in length.
        # - The tag value cannot start with aliyun or acs:.
        # - The tag value cannot contain http:// or https://.
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

