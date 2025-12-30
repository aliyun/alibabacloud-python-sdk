# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListVscsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_ids: List[str] = None,
        resource_group_id: str = None,
        tag: List[main_models.ListVscsRequestTag] = None,
        vsc_name: str = None,
    ):
        # The maximum number of data entries to return.
        self.max_results = max_results
        # The token that is used in the next request to retrieve a new page of results. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The IDs of the nodes.
        self.node_ids = node_ids
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag = tag
        # The VSC name.
        self.vsc_name = vsc_name

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListVscsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')

        return self

class ListVscsRequestTag(DaraModel):
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

