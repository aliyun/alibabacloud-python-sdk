# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListVscsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vscs: List[main_models.ListVscsResponseBodyVscs] = None,
    ):
        # No response is returned. The TotalCount parameter is used.
        self.max_results = max_results
        # The token. It can be used in the next request to retrieve a new page of results. If this parameter is empty, no next page exists.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of VSCs.
        self.total_count = total_count
        # The VSCs.
        self.vscs = vscs

    def validate(self):
        if self.vscs:
            for v1 in self.vscs:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Vscs'] = []
        if self.vscs is not None:
            for k1 in self.vscs:
                result['Vscs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vscs = []
        if m.get('Vscs') is not None:
            for k1 in m.get('Vscs'):
                temp_model = main_models.ListVscsResponseBodyVscs()
                self.vscs.append(temp_model.from_map(k1))

        return self

class ListVscsResponseBodyVscs(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListVscsResponseBodyVscsTags] = None,
        vsc_id: str = None,
        vsc_name: str = None,
        vsc_type: str = None,
    ):
        # The ID of the Lingjun node.
        self.node_id = node_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The VSC status.
        # 
        # Valid values:
        # 
        # *   Creating
        # *   Normal
        # *   Deleting
        self.status = status
        # The tags.
        self.tags = tags
        # The VSC ID.
        self.vsc_id = vsc_id
        # The custom name of the VSC.
        self.vsc_name = vsc_name
        # The VSC type. Valid values: primary and standard.
        self.vsc_type = vsc_type

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name

        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListVscsResponseBodyVscsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')

        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')

        return self

class ListVscsResponseBodyVscsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

