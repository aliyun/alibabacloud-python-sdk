# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_spec: str = None,
        network_type: str = None,
        oss_bucket_name: str = None,
        payment_type: str = None,
        region_id: str = None,
        security_group: str = None,
        status: str = None,
        update_time: str = None,
        vpc_id: str = None,
        zones: List[main_models.GetInstanceResponseBodyDataZones] = None,
    ):
        self.create_time = create_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_spec = instance_spec
        self.network_type = network_type
        self.oss_bucket_name = oss_bucket_name
        self.payment_type = payment_type
        self.region_id = region_id
        self.security_group = security_group
        self.status = status
        self.update_time = update_time
        self.vpc_id = vpc_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.GetInstanceResponseBodyDataZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class GetInstanceResponseBodyDataZones(DaraModel):
    def __init__(
        self,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

