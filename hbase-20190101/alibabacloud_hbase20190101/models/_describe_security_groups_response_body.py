# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_group_ids: main_models.DescribeSecurityGroupsResponseBodySecurityGroupIds = None,
    ):
        # The request ID.
        self.request_id = request_id
        self.security_group_ids = security_group_ids

    def validate(self):
        if self.security_group_ids:
            self.security_group_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        return self

class DescribeSecurityGroupsResponseBodySecurityGroupIds(DaraModel):
    def __init__(
        self,
        security_group_id: List[str] = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

