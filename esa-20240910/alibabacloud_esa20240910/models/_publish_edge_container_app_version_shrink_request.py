# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishEdgeContainerAppVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        full_release: bool = None,
        percentage: int = None,
        publish_env: str = None,
        publish_type: str = None,
        regions_shrink: str = None,
        remarks: str = None,
        start_time: str = None,
        version_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.full_release = full_release
        self.percentage = percentage
        # This parameter is required.
        self.publish_env = publish_env
        self.publish_type = publish_type
        self.regions_shrink = regions_shrink
        self.remarks = remarks
        self.start_time = start_time
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.full_release is not None:
            result['FullRelease'] = self.full_release

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.publish_env is not None:
            result['PublishEnv'] = self.publish_env

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.regions_shrink is not None:
            result['Regions'] = self.regions_shrink

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('FullRelease') is not None:
            self.full_release = m.get('FullRelease')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('PublishEnv') is not None:
            self.publish_env = m.get('PublishEnv')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('Regions') is not None:
            self.regions_shrink = m.get('Regions')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

