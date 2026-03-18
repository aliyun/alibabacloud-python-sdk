# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetGroupToInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeAssetGroupToInstanceResponseBodyDataList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The response parameters.
        self.data_list = data_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeAssetGroupToInstanceResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeAssetGroupToInstanceResponseBodyDataList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        member_uid: str = None,
        name: str = None,
        region: str = None,
        type: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance of a paid edition.
        self.instance_id = instance_id
        # The UID of the member to which the asset belongs.
        self.member_uid = member_uid
        # The ID of the asset.
        self.name = name
        # The region ID of the asset.
        self.region = region
        # The type of the asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.name is not None:
            result['Name'] = self.name

        if self.region is not None:
            result['Region'] = self.region

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

