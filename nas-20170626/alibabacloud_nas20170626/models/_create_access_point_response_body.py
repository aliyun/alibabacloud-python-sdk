# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateAccessPointResponseBody(DaraModel):
    def __init__(
        self,
        access_point: main_models.CreateAccessPointResponseBodyAccessPoint = None,
        request_id: str = None,
    ):
        # The access point.
        self.access_point = access_point
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_point:
            self.access_point.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point is not None:
            result['AccessPoint'] = self.access_point.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPoint') is not None:
            temp_model = main_models.CreateAccessPointResponseBodyAccessPoint()
            self.access_point = temp_model.from_map(m.get('AccessPoint'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAccessPointResponseBodyAccessPoint(DaraModel):
    def __init__(
        self,
        access_point_domain: str = None,
        access_point_id: str = None,
    ):
        # The domain name of the access point.
        self.access_point_domain = access_point_domain
        # The ID of the access point.
        self.access_point_id = access_point_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_domain is not None:
            result['AccessPointDomain'] = self.access_point_domain

        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointDomain') is not None:
            self.access_point_domain = m.get('AccessPointDomain')

        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        return self

