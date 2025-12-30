# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateVodPackagingGroupResponseBody(DaraModel):
    def __init__(
        self,
        packaging_group: main_models.VodPackagingGroup = None,
        request_id: str = None,
    ):
        # The packaging group information.
        self.packaging_group = packaging_group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.packaging_group:
            self.packaging_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.packaging_group is not None:
            result['PackagingGroup'] = self.packaging_group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackagingGroup') is not None:
            temp_model = main_models.VodPackagingGroup()
            self.packaging_group = temp_model.from_map(m.get('PackagingGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

