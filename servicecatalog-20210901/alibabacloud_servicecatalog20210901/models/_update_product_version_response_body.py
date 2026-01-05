# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProductVersionResponseBody(DaraModel):
    def __init__(
        self,
        product_version_id: str = None,
        request_id: str = None,
    ):
        # The ID of the product version.
        self.product_version_id = product_version_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

