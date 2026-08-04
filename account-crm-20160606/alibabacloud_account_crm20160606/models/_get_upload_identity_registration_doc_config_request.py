# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUploadIdentityRegistrationDocConfigRequest(DaraModel):
    def __init__(
        self,
        customer_id: str = None,
        file_path: str = None,
    ):
        # This parameter is required.
        self.customer_id = customer_id
        # This parameter is required.
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        return self

