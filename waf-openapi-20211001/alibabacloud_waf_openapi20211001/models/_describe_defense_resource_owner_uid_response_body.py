# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseResourceOwnerUidResponseBody(DaraModel):
    def __init__(
        self,
        owner_infos: List[main_models.DescribeDefenseResourceOwnerUidResponseBodyOwnerInfos] = None,
        request_id: str = None,
    ):
        self.owner_infos = owner_infos
        self.request_id = request_id

    def validate(self):
        if self.owner_infos:
            for v1 in self.owner_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OwnerInfos'] = []
        if self.owner_infos is not None:
            for k1 in self.owner_infos:
                result['OwnerInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.owner_infos = []
        if m.get('OwnerInfos') is not None:
            for k1 in m.get('OwnerInfos'):
                temp_model = main_models.DescribeDefenseResourceOwnerUidResponseBodyOwnerInfos()
                self.owner_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDefenseResourceOwnerUidResponseBodyOwnerInfos(DaraModel):
    def __init__(
        self,
        owner_user_id: str = None,
        resource_name: str = None,
    ):
        self.owner_user_id = owner_user_id
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

