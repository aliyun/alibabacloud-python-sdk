# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeVscsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        vscs: List[main_models.DescribeVscsResponseBodyVscs] = None,
    ):
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # VSC
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Vscs'] = []
        if self.vscs is not None:
            for k1 in self.vscs:
                result['Vscs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vscs = []
        if m.get('Vscs') is not None:
            for k1 in m.get('Vscs'):
                temp_model = main_models.DescribeVscsResponseBodyVscs()
                self.vscs.append(temp_model.from_map(k1))

        return self

class DescribeVscsResponseBodyVscs(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.DescribeVscsResponseBodyVscsTags] = None,
        vsc_id: str = None,
        vsc_name: str = None,
        vsc_type: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.tags = tags
        # VSC ID。
        self.vsc_id = vsc_id
        self.vsc_name = vsc_name
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
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeVscsResponseBodyVscsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')

        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')

        return self

class DescribeVscsResponseBodyVscsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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

