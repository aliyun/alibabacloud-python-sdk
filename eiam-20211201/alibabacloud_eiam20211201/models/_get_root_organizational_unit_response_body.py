# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetRootOrganizationalUnitResponseBody(DaraModel):
    def __init__(
        self,
        organizational_unit: main_models.GetRootOrganizationalUnitResponseBodyOrganizationalUnit = None,
        request_id: str = None,
    ):
        # The data object of the organizational unit.
        self.organizational_unit = organizational_unit
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.organizational_unit:
            self.organizational_unit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit is not None:
            result['OrganizationalUnit'] = self.organizational_unit.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationalUnit') is not None:
            temp_model = main_models.GetRootOrganizationalUnitResponseBodyOrganizationalUnit()
            self.organizational_unit = temp_model.from_map(m.get('OrganizationalUnit'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRootOrganizationalUnitResponseBodyOrganizationalUnit(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        organizational_unit_id: str = None,
        organizational_unit_name: str = None,
        update_time: int = None,
    ):
        # The time when the organizational unit was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The description of the organizational unit.
        self.description = description
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id
        # The name of the organization.
        self.organizational_unit_name = organizational_unit_name
        # The time when the organizational unit was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

