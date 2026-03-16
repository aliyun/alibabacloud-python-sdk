# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetServiceRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_name: str = None,
        service_version: str = None,
        show_details: List[str] = None,
    ):
        # Region Id.
        self.region_id = region_id
        # The service ID.
        self.service_id = service_id
        # The service instance id.
        self.service_instance_id = service_instance_id
        # The service name.
        self.service_name = service_name
        # The service version.
        self.service_version = service_version
        # Whether to disclose service details.
        self.show_details = show_details

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.show_details is not None:
            result['ShowDetails'] = self.show_details

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('ShowDetails') is not None:
            self.show_details = m.get('ShowDetails')

        return self

