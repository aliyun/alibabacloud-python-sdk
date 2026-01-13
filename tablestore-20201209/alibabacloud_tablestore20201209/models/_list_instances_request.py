# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_name_list: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[main_models.ListInstancesRequestTag] = None,
    ):
        # The name of the instance. Fuzzy search is supported.
        self.instance_name = instance_name
        # The names of the instances. This parameter is used to specify multiple instances that you want to query at the same time.
        self.instance_name_list = instance_name_list
        # The maximum number of instances that you want to return. Valid values: 0 to 200. If you do not configure this parameter or set this parameter to 0, the default value of 100 is used.
        self.max_results = max_results
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call. Instances are returned in lexicographical order starting from the position that is specified by this parameter. The first time you call the operation, leave this parameter empty.
        self.next_token = next_token
        # The resource group ID. You can query the ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The status of the instance.
        self.status = status
        # The tags of the instance.
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
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_name_list is not None:
            result['InstanceNameList'] = self.instance_name_list

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceNameList') is not None:
            self.instance_name_list = m.get('InstanceNameList')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

