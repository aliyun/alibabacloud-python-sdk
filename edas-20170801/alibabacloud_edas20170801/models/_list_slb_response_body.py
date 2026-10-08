# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListSlbResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        slb_list: main_models.ListSlbResponseBodySlbList = None,
    ):
        # The interface status or POP error code.
        self.code = code
        # The additional information.
        self.message = message
        # The request ID.
        self.request_id = request_id
        self.slb_list = slb_list

    def validate(self):
        if self.slb_list:
            self.slb_list.validate()

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

        if self.slb_list is not None:
            result['SlbList'] = self.slb_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlbList') is not None:
            temp_model = main_models.ListSlbResponseBodySlbList()
            self.slb_list = temp_model.from_map(m.get('SlbList'))

        return self

class ListSlbResponseBodySlbList(DaraModel):
    def __init__(
        self,
        slb_entity: List[main_models.ListSlbResponseBodySlbListSlbEntity] = None,
    ):
        self.slb_entity = slb_entity

    def validate(self):
        if self.slb_entity:
            for v1 in self.slb_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlbEntity'] = []
        if self.slb_entity is not None:
            for k1 in self.slb_entity:
                result['SlbEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slb_entity = []
        if m.get('SlbEntity') is not None:
            for k1 in m.get('SlbEntity'):
                temp_model = main_models.ListSlbResponseBodySlbListSlbEntity()
                self.slb_entity.append(temp_model.from_map(k1))

        return self

class ListSlbResponseBodySlbListSlbEntity(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_type: str = None,
        expired: bool = None,
        group_id: int = None,
        network_type: str = None,
        region_id: str = None,
        reusable: bool = None,
        slb_id: str = None,
        slb_name: str = None,
        slb_status: str = None,
        tags: str = None,
        user_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.address = address
        self.address_type = address_type
        self.expired = expired
        self.group_id = group_id
        self.network_type = network_type
        self.region_id = region_id
        self.reusable = reusable
        self.slb_id = slb_id
        self.slb_name = slb_name
        self.slb_status = slb_status
        self.tags = tags
        self.user_id = user_id
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reusable is not None:
            result['Reusable'] = self.reusable

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_name is not None:
            result['SlbName'] = self.slb_name

        if self.slb_status is not None:
            result['SlbStatus'] = self.slb_status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reusable') is not None:
            self.reusable = m.get('Reusable')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')

        if m.get('SlbStatus') is not None:
            self.slb_status = m.get('SlbStatus')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

