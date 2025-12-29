# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class TrafficConfig(DaraModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        created_time: str = None,
        last_modified_time: str = None,
        request_id: str = None,
        resolve_policy: str = None,
        route_policy: main_models.RoutePolicy = None,
        version_id: str = None,
    ):
        self.additional_version_weight = additional_version_weight
        self.created_time = created_time
        self.last_modified_time = last_modified_time
        self.request_id = request_id
        self.resolve_policy = resolve_policy
        self.route_policy = route_policy
        self.version_id = version_id

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy

        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')

        if m.get('routePolicy') is not None:
            temp_model = main_models.RoutePolicy()
            self.route_policy = temp_model.from_map(m.get('routePolicy'))

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self

