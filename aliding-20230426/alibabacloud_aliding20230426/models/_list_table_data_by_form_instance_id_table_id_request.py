# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTableDataByFormInstanceIdTableIdRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        form_instance_id: str = None,
        form_uuid: str = None,
        page_number: int = None,
        page_size: int = None,
        system_token: str = None,
        table_field_id: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.form_instance_id = form_instance_id
        # This parameter is required.
        self.form_uuid = form_uuid
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.system_token = system_token
        # This parameter is required.
        self.table_field_id = table_field_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.form_instance_id is not None:
            result['FormInstanceId'] = self.form_instance_id

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.table_field_id is not None:
            result['TableFieldId'] = self.table_field_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FormInstanceId') is not None:
            self.form_instance_id = m.get('FormInstanceId')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('TableFieldId') is not None:
            self.table_field_id = m.get('TableFieldId')

        return self

