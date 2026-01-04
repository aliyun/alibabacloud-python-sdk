# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApplicationsForOrganizationalUnitRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        instance_id: str = None,
        organizational_unit_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The IDs of the applications that the EIAM organization can access. You can query a maximum of 100 application IDs at a time.
        self.application_ids = application_ids
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the EIAM organization.
        # 
        # This parameter is required.
        self.organizational_unit_id = organizational_unit_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

