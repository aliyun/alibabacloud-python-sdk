# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPrivateAccessApplicationsRequest(DaraModel):
    def __init__(
        self,
        access_modes: str = None,
        address: str = None,
        application_ids: List[str] = None,
        connector_id: str = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        policy_id: str = None,
        status: str = None,
        tag_id: str = None,
    ):
        self.access_modes = access_modes
        self.address = address
        self.application_ids = application_ids
        self.connector_id = connector_id
        # This parameter is required.
        self.current_page = current_page
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        self.policy_id = policy_id
        self.status = status
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_modes is not None:
            result['AccessModes'] = self.access_modes

        if self.address is not None:
            result['Address'] = self.address

        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessModes') is not None:
            self.access_modes = m.get('AccessModes')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

