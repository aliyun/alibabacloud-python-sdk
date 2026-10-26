# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEngineConfigResponseBody(DaraModel):
    def __init__(
        self,
        config_value: str = None,
        description: str = None,
        environment: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        gmt_released_time: str = None,
        name: str = None,
        request_id: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The content of the engine configuration.
        self.config_value = config_value
        # The description.
        self.description = description
        # The runtime environment. Valid values:
        # - Daily: daily environment
        # - Pre: staging environment
        # - Prod: production environment
        self.environment = environment
        # The creation time. The time is in ISO 8601 format, where Z indicates the UTC time zone.
        self.gmt_create_time = gmt_create_time
        # The update time. The time is in ISO 8601 format, where Z indicates the UTC time zone.
        self.gmt_modified_time = gmt_modified_time
        # The release time. The time is in the YYYY-MM-DD HH:mm:ss format.
        self.gmt_released_time = gmt_released_time
        # The name of the engine configuration.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The scenario.
        self.scene_id = scene_id
        # The status. Valid values:
        # - Released: released
        # - UnReleased: unreleased
        self.status = status
        # The type of the engine configuration.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.description is not None:
            result['Description'] = self.description

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_released_time is not None:
            result['GmtReleasedTime'] = self.gmt_released_time

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtReleasedTime') is not None:
            self.gmt_released_time = m.get('GmtReleasedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

