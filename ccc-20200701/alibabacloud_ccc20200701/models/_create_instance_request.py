# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        admin_ram_id_list: str = None,
        description: str = None,
        domain_name: str = None,
        name: str = None,
        number_list: str = None,
    ):
        # This parameter is required.
        self.admin_ram_id_list = admin_ram_id_list
        self.description = description
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.name = name
        self.number_list = number_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_ram_id_list is not None:
            result['AdminRamIdList'] = self.admin_ram_id_list

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.name is not None:
            result['Name'] = self.name

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminRamIdList') is not None:
            self.admin_ram_id_list = m.get('AdminRamIdList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        return self

