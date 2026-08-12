# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class E2BVolume(DaraModel):
    def __init__(
        self,
        agentic_fsvolume_config: main_models.AgenticFSVolumeConfig = None,
        created_at: str = None,
        oss_volume_config: main_models.OSSVolumeConfig = None,
        resource_group_id: str = None,
        status: str = None,
        status_reason: str = None,
        storage_class: str = None,
        team_id: str = None,
        updated_at: str = None,
        user_id: str = None,
        volume_id: str = None,
        volume_name: str = None,
    ):
        self.agentic_fsvolume_config = agentic_fsvolume_config
        self.created_at = created_at
        self.oss_volume_config = oss_volume_config
        self.resource_group_id = resource_group_id
        self.status = status
        self.status_reason = status_reason
        self.storage_class = storage_class
        self.team_id = team_id
        self.updated_at = updated_at
        self.user_id = user_id
        self.volume_id = volume_id
        self.volume_name = volume_name

    def validate(self):
        if self.agentic_fsvolume_config:
            self.agentic_fsvolume_config.validate()
        if self.oss_volume_config:
            self.oss_volume_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_fsvolume_config is not None:
            result['agenticFSVolumeConfig'] = self.agentic_fsvolume_config.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.oss_volume_config is not None:
            result['ossVolumeConfig'] = self.oss_volume_config.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.storage_class is not None:
            result['storageClass'] = self.storage_class

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.user_id is not None:
            result['userID'] = self.user_id

        if self.volume_id is not None:
            result['volumeID'] = self.volume_id

        if self.volume_name is not None:
            result['volumeName'] = self.volume_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agenticFSVolumeConfig') is not None:
            temp_model = main_models.AgenticFSVolumeConfig()
            self.agentic_fsvolume_config = temp_model.from_map(m.get('agenticFSVolumeConfig'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('ossVolumeConfig') is not None:
            temp_model = main_models.OSSVolumeConfig()
            self.oss_volume_config = temp_model.from_map(m.get('ossVolumeConfig'))

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('storageClass') is not None:
            self.storage_class = m.get('storageClass')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        if m.get('volumeID') is not None:
            self.volume_id = m.get('volumeID')

        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')

        return self

