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
        # A list of data objects.
        self.data = data
        # The total number of records.
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
        # The time when the organization was created. This is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The description of the organization.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The external ID of the organization. This ID is used to map external data to the organization\\"s data in IDaaS. The default value is the IDaaS organization ID.
        # 
        # Note: The external ID must be unique for the same source type and source ID.
        self.organizational_unit_external_id = organizational_unit_external_id
        # The organization ID.
        self.organizational_unit_id = organizational_unit_id
        # The organization name.
        self.organizational_unit_name = organizational_unit_name
        # The source ID of the organization.
        # 
        # For the \\`build_in\\` type, the default value is the instance ID. For other types, the value is the enterprise ID from the source. For example, if the source is DingTalk, the value is the \\`corpId\\` of the DingTalk enterprise.
        self.organizational_unit_source_id = organizational_unit_source_id
        # The source type of the organization. Valid values:
        # 
        # - \\`build_in\\`: The organization is created in IDaaS.
        # 
        # - \\`ding_talk\\`: The organization is imported from DingTalk.
        # 
        # - \\`ad\\`: The organization is imported from Active Directory (AD).
        # 
        # - \\`ldap\\`: The organization is imported from LDAP.
        self.organizational_unit_source_type = organizational_unit_source_type
        # The parent organization ID.
        self.parent_id = parent_id
        # The time when the organization was last updated. This is a UNIX timestamp. Unit: milliseconds.
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

