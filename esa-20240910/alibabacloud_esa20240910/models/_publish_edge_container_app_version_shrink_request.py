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
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to fully release the version. This parameter takes effect only when PublishType is set to region.
        self.full_release = full_release
        # The release percentage. Valid values: 1 to 100. Default value: 100.
        self.percentage = percentage
        # The environment to which you want to release the version. Valid values:
        # 
        # *   prod: the production environment.
        # *   staging: the staging environment.
        # 
        # This parameter is required.
        self.publish_env = publish_env
        # Specifies how the version is released. Valid values:
        # 
        # *   percentage: releases the version by percentage.
        # *   region: releases the version by region.
        # 
        # If you do not specify this parameter, the version is released by percentage by default.
        self.publish_type = publish_type
        # The regions to which the version is released.
        self.regions_shrink = regions_shrink
        # The remarks. This parameter is empty by default.
        self.remarks = remarks
        # The time when the application version starts to be released. If you do not specify this parameter, the current time is used by default.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The version ID.
        # 
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

