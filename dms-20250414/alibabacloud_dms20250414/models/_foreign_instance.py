# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ForeignInstance(DaraModel):
    def __init__(
        self,
        data_link_name: str = None,
        host: str = None,
        instance_source: str = None,
        instance_type: str = None,
        port: int = None,
        properties: Dict[str, str] = None,
        region_id: str = None,
        sid: str = None,
    ):
        # The name of the data link.
        self.data_link_name = data_link_name
        # The endpoint that is used to connect to the database instance.
        self.host = host
        # The source of the database instance. Valid values:
        # 
        # *   **PUBLIC_OWN:** a self-managed database instance that is deployed on the Internet.
        # *   **RDS**: an ApsaraDB RDS instance.
        # *   **ECS_OWN**: a self-managed database that is hosted on an Elastic Compute Service (ECS) instance.
        # *   **VPC_IDC**: a self-managed database instance that is deployed in the data center over a virtual private cloud (VPC).
        self.instance_source = instance_source
        # The type of the instance.
        self.instance_type = instance_type
        # The port number that is used to connect to the database instance.
        self.port = port
        # The information of the properties.
        self.properties = properties
        # The region ID.
        self.region_id = region_id
        # The system identifier (SID) of the database.
        # 
        # >  The SID uniquely identifies an Oracle database. After a database is created, a SID is generated for the database.
        self.sid = sid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.port is not None:
            result['Port'] = self.port

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sid is not None:
            result['Sid'] = self.sid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        return self

