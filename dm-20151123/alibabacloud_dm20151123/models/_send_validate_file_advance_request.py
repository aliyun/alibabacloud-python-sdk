# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class SendValidateFileAdvanceRequest(DaraModel):
    def __init__(
        self,
        address_column: int = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        has_header_row: bool = None,
        remove_duplicate: bool = None,
    ):
        # This parameter is required.
        self.address_column = address_column
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_url_object = file_url_object
        # This parameter is required.
        self.has_header_row = has_header_row
        # This parameter is required.
        self.remove_duplicate = remove_duplicate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_column is not None:
            result['AddressColumn'] = self.address_column

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object

        if self.has_header_row is not None:
            result['HasHeaderRow'] = self.has_header_row

        if self.remove_duplicate is not None:
            result['RemoveDuplicate'] = self.remove_duplicate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressColumn') is not None:
            self.address_column = m.get('AddressColumn')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')

        if m.get('HasHeaderRow') is not None:
            self.has_header_row = m.get('HasHeaderRow')

        if m.get('RemoveDuplicate') is not None:
            self.remove_duplicate = m.get('RemoveDuplicate')

        return self

