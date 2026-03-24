# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class ListUserCustomLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        config_ids: main_models.ListUserCustomLogConfigResponseBodyConfigIds = None,
        request_id: str = None,
    ):
        self.config_ids = config_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.config_ids:
            self.config_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_ids is not None:
            result['ConfigIds'] = self.config_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigIds') is not None:
            temp_model = main_models.ListUserCustomLogConfigResponseBodyConfigIds()
            self.config_ids = temp_model.from_map(m.get('ConfigIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUserCustomLogConfigResponseBodyConfigIds(DaraModel):
    def __init__(
        self,
        config_id: List[str] = None,
    ):
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        return self

