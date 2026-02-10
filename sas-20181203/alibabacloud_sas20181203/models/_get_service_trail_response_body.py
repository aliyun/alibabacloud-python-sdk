# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetServiceTrailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_trail: main_models.GetServiceTrailResponseBodyServiceTrail = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The configurations of the service trail.
        self.service_trail = service_trail

    def validate(self):
        if self.service_trail:
            self.service_trail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_trail is not None:
            result['ServiceTrail'] = self.service_trail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceTrail') is not None:
            temp_model = main_models.GetServiceTrailResponseBodyServiceTrail()
            self.service_trail = temp_model.from_map(m.get('ServiceTrail'))

        return self

class GetServiceTrailResponseBodyServiceTrail(DaraModel):
    def __init__(
        self,
        config: str = None,
        create_time: int = None,
        update_time: int = None,
    ):
        # The status of the service trail. Valid values:
        # 
        # *   **on:**
        # *   **off:**
        self.config = config
        # The timestamp generated when the service trail was created. Unit: milliseconds.
        self.create_time = create_time
        # The timestamp generated when the service trail was last updated. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

