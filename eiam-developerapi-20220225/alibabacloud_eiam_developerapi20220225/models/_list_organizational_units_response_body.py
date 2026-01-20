# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class ListOrganizationalUnitsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListOrganizationalUnitsResponseBodyData] = None,
        total_count: int = None,
    ):
        # The queried organizational units.
        self.data = data
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListOrganizationalUnitsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListOrganizationalUnitsResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        organizational_unit_external_id: str = None,
        organizational_unit_id: str = None,
        organizational_unit_name: str = None,
        organizational_unit_source_id: str = None,
        organizational_unit_source_type: str = None,
        parent_id: str = None,
        update_time: int = None,
    ):
        # The time when the organizational unit was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the organizational unit.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The external ID of the organizational unit. The external ID can be used to map external data to the data of the organizational unit in EIAM of Identity as a Service (IDaaS). By default, the external ID is the organizational unit ID.
        # 
        # Note: For organizational units with the same source type and source ID, each organizational unit has a unique external ID.
        self.organizational_unit_external_id = organizational_unit_external_id
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id
        # The name of the organizational unit.
        self.organizational_unit_name = organizational_unit_name
        # The source ID of the organizational unit.
        # 
        # If the organizational unit was created in IDaaS, its source ID is the ID of the IDaaS instance. If the organizational unit was imported, its source ID is the enterprise ID in the source. For example, if the organizational unit was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        self.organizational_unit_source_id = organizational_unit_source_id
        # The source type of the organizational unit. Valid values:
        # 
        # *   build_in: The organizational unit was created in IDaaS.
        # *   ding_talk: The organizational unit was imported from DingTalk.
        # *   ad: The organizational unit was imported from Microsoft Active Directory (AD).
        # *   ldap: The organizational unit was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.organizational_unit_source_type = organizational_unit_source_type
        # The ID of the parent organizational unit.
        self.parent_id = parent_id
        # The time when the organizational unit was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.organizational_unit_external_id is not None:
            result['organizationalUnitExternalId'] = self.organizational_unit_external_id

        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id

        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name

        if self.organizational_unit_source_id is not None:
            result['organizationalUnitSourceId'] = self.organizational_unit_source_id

        if self.organizational_unit_source_type is not None:
            result['organizationalUnitSourceType'] = self.organizational_unit_source_type

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('organizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('organizationalUnitExternalId')

        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')

        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')

        if m.get('organizationalUnitSourceId') is not None:
            self.organizational_unit_source_id = m.get('organizationalUnitSourceId')

        if m.get('organizationalUnitSourceType') is not None:
            self.organizational_unit_source_type = m.get('organizationalUnitSourceType')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

