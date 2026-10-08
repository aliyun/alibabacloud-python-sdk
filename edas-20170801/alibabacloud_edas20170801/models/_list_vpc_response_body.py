# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListVpcResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        vpc_list: main_models.ListVpcResponseBodyVpcList = None,
    ):
        # The ID of the request.
        self.code = code
        # The information about VPCs.
        self.message = message
        # The name of the VPC.
        self.request_id = request_id
        self.vpc_list = vpc_list

    def validate(self):
        if self.vpc_list:
            self.vpc_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vpc_list is not None:
            result['VpcList'] = self.vpc_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VpcList') is not None:
            temp_model = main_models.ListVpcResponseBodyVpcList()
            self.vpc_list = temp_model.from_map(m.get('VpcList'))

        return self

class ListVpcResponseBodyVpcList(DaraModel):
    def __init__(
        self,
        vpc_entity: List[main_models.ListVpcResponseBodyVpcListVpcEntity] = None,
    ):
        self.vpc_entity = vpc_entity

    def validate(self):
        if self.vpc_entity:
            for v1 in self.vpc_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VpcEntity'] = []
        if self.vpc_entity is not None:
            for k1 in self.vpc_entity:
                result['VpcEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_entity = []
        if m.get('VpcEntity') is not None:
            for k1 in m.get('VpcEntity'):
                temp_model = main_models.ListVpcResponseBodyVpcListVpcEntity()
                self.vpc_entity.append(temp_model.from_map(k1))

        return self

class ListVpcResponseBodyVpcListVpcEntity(DaraModel):
    def __init__(
        self,
        ecs_num: int = None,
        expired: bool = None,
        region_id: str = None,
        user_id: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.ecs_num = ecs_num
        self.expired = expired
        self.region_id = region_id
        self.user_id = user_id
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_num is not None:
            result['EcsNum'] = self.ecs_num

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsNum') is not None:
            self.ecs_num = m.get('EcsNum')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

