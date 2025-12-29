# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeRdsVSwitchsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        v_switches: main_models.DescribeRdsVSwitchsResponseBodyVSwitches = None,
    ):
        self.request_id = request_id
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VSwitches') is not None:
            temp_model = main_models.DescribeRdsVSwitchsResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m.get('VSwitches'))

        return self

class DescribeRdsVSwitchsResponseBodyVSwitches(DaraModel):
    def __init__(
        self,
        v_switch: List[main_models.DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch] = None,
    ):
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for v1 in self.v_switch:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k1 in self.v_switch:
                result['VSwitch'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k1 in m.get('VSwitch'):
                temp_model = main_models.DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k1))

        return self

class DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        bid: str = None,
        cidr_block: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_default: bool = None,
        iz_no: str = None,
        region_no: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.bid = bid
        self.cidr_block = cidr_block
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.is_default = is_default
        self.iz_no = iz_no
        self.region_no = region_no
        self.status = status
        # VSwitch ID。
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bid is not None:
            result['Bid'] = self.bid

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.iz_no is not None:
            result['IzNo'] = self.iz_no

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        return self

