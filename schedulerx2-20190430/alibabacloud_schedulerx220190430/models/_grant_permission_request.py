# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantPermissionRequest(DaraModel):
    def __init__(
        self,
        grant_option: bool = None,
        group_id: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # Specifies whether to grant the permissions with the GRANT option. Valid values: -**true** -**false**
        self.grant_option = grant_option
        # The application group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The namespace ID.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source
        # The region ID.
        self.region_id = region_id
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The username.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

