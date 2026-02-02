# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel



class AddressDetail(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        access_secret: str = None,
        address_type: str = None,
        agent_list: str = None,
        bucket: str = None,
        data_type: str = None,
        domain: str = None,
        inv_access_id: str = None,
        inv_access_secret: str = None,
        inv_bucket: str = None,
        inv_domain: str = None,
        inv_location: str = None,
        inv_path: str = None,
        inv_region_id: str = None,
        inv_role: str = None,
        prefix: str = None,
        region_id: str = None,
        role: str = None,
    ):
        # This parameter is required.
        self.access_id = access_id
        # This parameter is required.
        self.access_secret = access_secret
        # This parameter is required.
        self.address_type = address_type
        self.agent_list = agent_list
        # This parameter is required.
        self.bucket = bucket
        self.data_type = data_type
        # This parameter is required.
        self.domain = domain
        self.inv_access_id = inv_access_id
        self.inv_access_secret = inv_access_secret
        self.inv_bucket = inv_bucket
        self.inv_domain = inv_domain
        self.inv_location = inv_location
        self.inv_path = inv_path
        self.inv_region_id = inv_region_id
        self.inv_role = inv_role
        self.prefix = prefix
        self.region_id = region_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.agent_list is not None:
            result['AgentList'] = self.agent_list

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.inv_access_id is not None:
            result['InvAccessId'] = self.inv_access_id

        if self.inv_access_secret is not None:
            result['InvAccessSecret'] = self.inv_access_secret

        if self.inv_bucket is not None:
            result['InvBucket'] = self.inv_bucket

        if self.inv_domain is not None:
            result['InvDomain'] = self.inv_domain

        if self.inv_location is not None:
            result['InvLocation'] = self.inv_location

        if self.inv_path is not None:
            result['InvPath'] = self.inv_path

        if self.inv_region_id is not None:
            result['InvRegionId'] = self.inv_region_id

        if self.inv_role is not None:
            result['InvRole'] = self.inv_role

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('AgentList') is not None:
            self.agent_list = m.get('AgentList')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InvAccessId') is not None:
            self.inv_access_id = m.get('InvAccessId')

        if m.get('InvAccessSecret') is not None:
            self.inv_access_secret = m.get('InvAccessSecret')

        if m.get('InvBucket') is not None:
            self.inv_bucket = m.get('InvBucket')

        if m.get('InvDomain') is not None:
            self.inv_domain = m.get('InvDomain')

        if m.get('InvLocation') is not None:
            self.inv_location = m.get('InvLocation')

        if m.get('InvPath') is not None:
            self.inv_path = m.get('InvPath')

        if m.get('InvRegionId') is not None:
            self.inv_region_id = m.get('InvRegionId')

        if m.get('InvRole') is not None:
            self.inv_role = m.get('InvRole')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

