# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        group: main_models.DescribeDefenseResourceGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The information about the protected object group.
        self.group = group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = main_models.DescribeDefenseResourceGroupResponseBodyGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDefenseResourceGroupResponseBodyGroup(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_name: str = None,
        resource_list: str = None,
    ):
        # The description of the protected object group.
        self.description = description
        # The time when the protected object group was created.
        self.gmt_create = gmt_create
        # The most recent time when the protected object group was modified.
        self.gmt_modified = gmt_modified
        # The name of the protected object group.
        self.group_name = group_name
        # The protected objects in the protected object group. The protected objects are separated with commas (,).
        self.resource_list = resource_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.resource_list is not None:
            result['ResourceList'] = self.resource_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ResourceList') is not None:
            self.resource_list = m.get('ResourceList')

        return self

