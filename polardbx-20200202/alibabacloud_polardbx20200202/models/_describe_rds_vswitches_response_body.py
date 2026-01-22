# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeRdsVswitchesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeRdsVswitchesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeRdsVswitchesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRdsVswitchesResponseBodyData(DaraModel):
    def __init__(
        self,
        vswitch_list: List[main_models.DescribeRdsVswitchesResponseBodyDataVswitchList] = None,
    ):
        self.vswitch_list = vswitch_list

    def validate(self):
        if self.vswitch_list:
            for v1 in self.vswitch_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VswitchList'] = []
        if self.vswitch_list is not None:
            for k1 in self.vswitch_list:
                result['VswitchList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vswitch_list = []
        if m.get('VswitchList') is not None:
            for k1 in m.get('VswitchList'):
                temp_model = main_models.DescribeRdsVswitchesResponseBodyDataVswitchList()
                self.vswitch_list.append(temp_model.from_map(k1))

        return self

class DescribeRdsVswitchesResponseBodyDataVswitchList(DaraModel):
    def __init__(
        self,
        availabe_ip_count: str = None,
        cidr_block: str = None,
        description: str = None,
        id: int = None,
        instance_id: str = None,
        is_default: str = None,
        iz_no: str = None,
        name: str = None,
        vpc_instance_id: str = None,
    ):
        self.availabe_ip_count = availabe_ip_count
        self.cidr_block = cidr_block
        self.description = description
        self.id = id
        self.instance_id = instance_id
        self.is_default = is_default
        self.iz_no = iz_no
        self.name = name
        # vpc id。
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.availabe_ip_count is not None:
            result['AvailabeIpCount'] = self.availabe_ip_count

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.iz_no is not None:
            result['IzNo'] = self.iz_no

        if self.name is not None:
            result['Name'] = self.name

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabeIpCount') is not None:
            self.availabe_ip_count = m.get('AvailabeIpCount')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

