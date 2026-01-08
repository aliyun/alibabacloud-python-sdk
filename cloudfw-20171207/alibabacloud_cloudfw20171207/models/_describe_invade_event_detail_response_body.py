# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInvadeEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        assets_instance_id: str = None,
        assets_instance_name: str = None,
        event_desc: str = None,
        event_detail: str = None,
        event_key: str = None,
        event_name: str = None,
        event_uuid: str = None,
        first_time: int = None,
        is_ignore: bool = None,
        last_time: int = None,
        operation_list: List[main_models.DescribeInvadeEventDetailResponseBodyOperationList] = None,
        private_ip: str = None,
        process_status: int = None,
        public_ip: str = None,
        reference: str = None,
        region_no: str = None,
        request_id: str = None,
        risk_level: int = None,
        unhandle_operation_list: List[main_models.DescribeInvadeEventDetailResponseBodyUnhandleOperationList] = None,
    ):
        self.assets_instance_id = assets_instance_id
        self.assets_instance_name = assets_instance_name
        self.event_desc = event_desc
        self.event_detail = event_detail
        self.event_key = event_key
        self.event_name = event_name
        self.event_uuid = event_uuid
        self.first_time = first_time
        self.is_ignore = is_ignore
        self.last_time = last_time
        self.operation_list = operation_list
        self.private_ip = private_ip
        self.process_status = process_status
        self.public_ip = public_ip
        self.reference = reference
        self.region_no = region_no
        self.request_id = request_id
        self.risk_level = risk_level
        self.unhandle_operation_list = unhandle_operation_list

    def validate(self):
        if self.operation_list:
            for v1 in self.operation_list:
                 if v1:
                    v1.validate()
        if self.unhandle_operation_list:
            for v1 in self.unhandle_operation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id

        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name

        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc

        if self.event_detail is not None:
            result['EventDetail'] = self.event_detail

        if self.event_key is not None:
            result['EventKey'] = self.event_key

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.is_ignore is not None:
            result['IsIgnore'] = self.is_ignore

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        result['OperationList'] = []
        if self.operation_list is not None:
            for k1 in self.operation_list:
                result['OperationList'].append(k1.to_map() if k1 else None)

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.reference is not None:
            result['Reference'] = self.reference

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        result['UnhandleOperationList'] = []
        if self.unhandle_operation_list is not None:
            for k1 in self.unhandle_operation_list:
                result['UnhandleOperationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')

        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')

        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')

        if m.get('EventDetail') is not None:
            self.event_detail = m.get('EventDetail')

        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('IsIgnore') is not None:
            self.is_ignore = m.get('IsIgnore')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        self.operation_list = []
        if m.get('OperationList') is not None:
            for k1 in m.get('OperationList'):
                temp_model = main_models.DescribeInvadeEventDetailResponseBodyOperationList()
                self.operation_list.append(temp_model.from_map(k1))

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('Reference') is not None:
            self.reference = m.get('Reference')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        self.unhandle_operation_list = []
        if m.get('UnhandleOperationList') is not None:
            for k1 in m.get('UnhandleOperationList'):
                temp_model = main_models.DescribeInvadeEventDetailResponseBodyUnhandleOperationList()
                self.unhandle_operation_list.append(temp_model.from_map(k1))

        return self

class DescribeInvadeEventDetailResponseBodyUnhandleOperationList(DaraModel):
    def __init__(
        self,
        args: str = None,
        operate: str = None,
    ):
        self.args = args
        self.operate = operate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.operate is not None:
            result['Operate'] = self.operate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        return self

class DescribeInvadeEventDetailResponseBodyOperationList(DaraModel):
    def __init__(
        self,
        args: str = None,
        operate: str = None,
    ):
        self.args = args
        self.operate = operate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.operate is not None:
            result['Operate'] = self.operate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        return self

