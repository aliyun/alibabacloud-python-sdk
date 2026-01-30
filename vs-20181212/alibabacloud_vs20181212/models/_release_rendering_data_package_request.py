# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseRenderingDataPackageRequest(DaraModel):
    def __init__(
        self,
        data_package_id: str = None,
    ):
        # This parameter is required.
        self.data_package_id = data_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_package_id is not None:
            result['DataPackageId'] = self.data_package_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPackageId') is not None:
            self.data_package_id = m.get('DataPackageId')

        return self

