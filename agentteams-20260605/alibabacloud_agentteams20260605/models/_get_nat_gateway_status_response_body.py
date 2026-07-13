# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetNatGatewayStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetNatGatewayStatusResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetNatGatewayStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNatGatewayStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        nat_gateway_configured: bool = None,
        nat_gateways: List[main_models.GetNatGatewayStatusResponseBodyDataNatGateways] = None,
        snat_configured: bool = None,
        status: str = None,
        vpc_id: str = None,
        zone_cidr_covered: bool = None,
        zone_cidrs: List[main_models.GetNatGatewayStatusResponseBodyDataZoneCidrs] = None,
    ):
        self.instance_id = instance_id
        self.nat_gateway_configured = nat_gateway_configured
        self.nat_gateways = nat_gateways
        self.snat_configured = snat_configured
        self.status = status
        self.vpc_id = vpc_id
        self.zone_cidr_covered = zone_cidr_covered
        self.zone_cidrs = zone_cidrs

    def validate(self):
        if self.nat_gateways:
            for v1 in self.nat_gateways:
                 if v1:
                    v1.validate()
        if self.zone_cidrs:
            for v1 in self.zone_cidrs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nat_gateway_configured is not None:
            result['NatGatewayConfigured'] = self.nat_gateway_configured

        result['NatGateways'] = []
        if self.nat_gateways is not None:
            for k1 in self.nat_gateways:
                result['NatGateways'].append(k1.to_map() if k1 else None)

        if self.snat_configured is not None:
            result['SnatConfigured'] = self.snat_configured

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_cidr_covered is not None:
            result['ZoneCidrCovered'] = self.zone_cidr_covered

        result['ZoneCidrs'] = []
        if self.zone_cidrs is not None:
            for k1 in self.zone_cidrs:
                result['ZoneCidrs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NatGatewayConfigured') is not None:
            self.nat_gateway_configured = m.get('NatGatewayConfigured')

        self.nat_gateways = []
        if m.get('NatGateways') is not None:
            for k1 in m.get('NatGateways'):
                temp_model = main_models.GetNatGatewayStatusResponseBodyDataNatGateways()
                self.nat_gateways.append(temp_model.from_map(k1))

        if m.get('SnatConfigured') is not None:
            self.snat_configured = m.get('SnatConfigured')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneCidrCovered') is not None:
            self.zone_cidr_covered = m.get('ZoneCidrCovered')

        self.zone_cidrs = []
        if m.get('ZoneCidrs') is not None:
            for k1 in m.get('ZoneCidrs'):
                temp_model = main_models.GetNatGatewayStatusResponseBodyDataZoneCidrs()
                self.zone_cidrs.append(temp_model.from_map(k1))

        return self

class GetNatGatewayStatusResponseBodyDataZoneCidrs(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        covered: bool = None,
        nat_gateway_id: str = None,
        snat_entry_id: str = None,
        snat_source_cidr: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.cidr_block = cidr_block
        self.covered = covered
        self.nat_gateway_id = nat_gateway_id
        self.snat_entry_id = snat_entry_id
        self.snat_source_cidr = snat_source_cidr
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.covered is not None:
            result['Covered'] = self.covered

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_source_cidr is not None:
            result['SnatSourceCidr'] = self.snat_source_cidr

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Covered') is not None:
            self.covered = m.get('Covered')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatSourceCidr') is not None:
            self.snat_source_cidr = m.get('SnatSourceCidr')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetNatGatewayStatusResponseBodyDataNatGateways(DaraModel):
    def __init__(
        self,
        nat_gateway_id: str = None,
        snat_configured: bool = None,
        snat_table_id: str = None,
        status: str = None,
    ):
        self.nat_gateway_id = nat_gateway_id
        self.snat_configured = snat_configured
        self.snat_table_id = snat_table_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.snat_configured is not None:
            result['SnatConfigured'] = self.snat_configured

        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SnatConfigured') is not None:
            self.snat_configured = m.get('SnatConfigured')

        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

