# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeAppInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        components: List[main_models.DescribeAppInstanceAttributeResponseBodyComponents] = None,
        dbinstance_name: str = None,
        eip_id: str = None,
        eip_status: str = None,
        instance_class: str = None,
        instance_minor_version: str = None,
        instance_name: str = None,
        nat_created_by: str = None,
        nat_gateway_id: str = None,
        nat_status: str = None,
        public_connection_string: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_connection_string: str = None,
        zone_id: str = None,
    ):
        # The name of the AI application.
        self.app_name = app_name
        # The application type. Only **supabase** is supported. For more information, see [RDS Supabase](https://help.aliyun.com/document_detail/2938735.html).
        self.app_type = app_type
        self.components = components
        # The ID of the RDS for PostgreSQL instance with which the RDS Supabase instances are associated.
        self.dbinstance_name = dbinstance_name
        self.eip_id = eip_id
        self.eip_status = eip_status
        # The instance type of the RDS Supabase instance.
        self.instance_class = instance_class
        # The minor version number of RDS Supabase instance.
        self.instance_minor_version = instance_minor_version
        # The ID of the RDS Supabase instance.
        self.instance_name = instance_name
        self.nat_created_by = nat_created_by
        self.nat_gateway_id = nat_gateway_id
        self.nat_status = nat_status
        # The public endpoint of the AI application.
        self.public_connection_string = public_connection_string
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The status of the instance. For more information, see [Instance state table](https://help.aliyun.com/document_detail/2623972.html).
        self.status = status
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The internal endpoint of the AI application.
        self.vpc_connection_string = vpc_connection_string
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.eip_id is not None:
            result['EipId'] = self.eip_id

        if self.eip_status is not None:
            result['EipStatus'] = self.eip_status

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_minor_version is not None:
            result['InstanceMinorVersion'] = self.instance_minor_version

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.nat_created_by is not None:
            result['NatCreatedBy'] = self.nat_created_by

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_status is not None:
            result['NatStatus'] = self.nat_status

        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_connection_string is not None:
            result['VpcConnectionString'] = self.vpc_connection_string

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.DescribeAppInstanceAttributeResponseBodyComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')

        if m.get('EipStatus') is not None:
            self.eip_status = m.get('EipStatus')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceMinorVersion') is not None:
            self.instance_minor_version = m.get('InstanceMinorVersion')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('NatCreatedBy') is not None:
            self.nat_created_by = m.get('NatCreatedBy')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatStatus') is not None:
            self.nat_status = m.get('NatStatus')

        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcConnectionString') is not None:
            self.vpc_connection_string = m.get('VpcConnectionString')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAppInstanceAttributeResponseBodyComponents(DaraModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
    ):
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

