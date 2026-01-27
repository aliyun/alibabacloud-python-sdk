# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportEnterpriseAccelerateTargetsRequest(DaraModel):
    def __init__(
        self,
        eap_id: str = None,
        file_url: str = None,
    ):
        # This parameter is required.
        self.eap_id = eap_id
        # This parameter is required.
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eap_id is not None:
            result['EapId'] = self.eap_id

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EapId') is not None:
            self.eap_id = m.get('EapId')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        return self

