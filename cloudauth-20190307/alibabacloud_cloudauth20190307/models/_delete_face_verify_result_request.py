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
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Whether deletion depends on having already obtained relevant data from the corresponding authentication process.
        # 
        # - Y: Required. To successfully delete the related data, you must have obtained the processing result through the DescribeFaceVerify interface.
        # - N: Not required (default). For pure server-side API integration, you can directly pass N.
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

