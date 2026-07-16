# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFaceVerifyResultRequest(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        delete_after_query: str = None,
    ):
        # The unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Specifies whether deletion depends on having retrieved the relevant data from the corresponding authentication process.
        # 
        # - Y: Required. To successfully delete the relevant data, you must have already obtained the processing result through the DescribeFaceVerify API.
        # - N: Not required (default). You can directly pass N when integrating through the pure server-side API mode.
        self.delete_after_query = delete_after_query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.delete_after_query is not None:
            result['DeleteAfterQuery'] = self.delete_after_query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('DeleteAfterQuery') is not None:
            self.delete_after_query = m.get('DeleteAfterQuery')

        return self

