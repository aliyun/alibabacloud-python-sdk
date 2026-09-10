# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class E2BVolume(DaraModel):
    def __init__(
        self,
        agentic_bucket_volume_config: main_models.AgenticBucketVolumeConfig = None,
        agentic_fsvolume_config: main_models.AgenticFSVolumeConfig = None,
        created_at: str = None,
        mount_config: main_models.E2BVolumeMountConfig = None,
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
        self.agentic_bucket_volume_config = agentic_bucket_volume_config
        # The AgenticFS configuration.
        self.agentic_fsvolume_config = agentic_fsvolume_config
        # The time when the volume was created.
        self.created_at = created_at
        # The mount configuration.
        self.mount_config = mount_config
        # The OSS configuration.
        self.oss_volume_config = oss_volume_config
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status. Valid values:
        # - CREATING
        # - AVAILABLE
        # - ERROR
        # - DELETING
        self.status = status
        # The reason for the status.
        self.status_reason = status_reason
        # The storage type. Valid values:
        # - OSS
        # - AGENTIC_FS
        self.storage_class = storage_class
        # The unique identifier of the team.
        self.team_id = team_id
        # The time when the volume was last updated.
        self.updated_at = updated_at
        # The UID of the creator.
        self.user_id = user_id
        # The unique identifier of the volume.
        self.volume_id = volume_id
        # The name, which is unique within the team.
        self.volume_name = volume_name

    def validate(self):
        if self.agentic_bucket_volume_config:
            self.agentic_bucket_volume_config.validate()
        if self.agentic_fsvolume_config:
            self.agentic_fsvolume_config.validate()
        if self.mount_config:
            self.mount_config.validate()
        if self.oss_volume_config:
            self.oss_volume_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_bucket_volume_config is not None:
            result['agenticBucketVolumeConfig'] = self.agentic_bucket_volume_config.to_map()

        if self.agentic_fsvolume_config is not None:
            result['agenticFSVolumeConfig'] = self.agentic_fsvolume_config.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.mount_config is not None:
            result['mountConfig'] = self.mount_config.to_map()

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
        if m.get('agenticBucketVolumeConfig') is not None:
            temp_model = main_models.AgenticBucketVolumeConfig()
            self.agentic_bucket_volume_config = temp_model.from_map(m.get('agenticBucketVolumeConfig'))

        if m.get('agenticFSVolumeConfig') is not None:
            temp_model = main_models.AgenticFSVolumeConfig()
            self.agentic_fsvolume_config = temp_model.from_map(m.get('agenticFSVolumeConfig'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('mountConfig') is not None:
            temp_model = main_models.E2BVolumeMountConfig()
            self.mount_config = temp_model.from_map(m.get('mountConfig'))

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

class E2BVolumeMountConfig(DaraModel):
    def __init__(
        self,
        role: str = None,
        vpc_config: main_models.E2BVolumeMountConfigVpcConfig = None,
    ):
        # The RAM role that the user grants to the sandboxed container. After this role is set, the sandboxed container assumes the role to generate temporary access credentials. You can use the temporary access credentials of this role to mount storage in the sandboxed container, such as OSS and AgenticFS.
        self.role = role
        # The virtual private cloud (VPC) ID.
        self.vpc_config = vpc_config

    def validate(self):
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role is not None:
            result['role'] = self.role

        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('vpcConfig') is not None:
            temp_model = main_models.E2BVolumeMountConfigVpcConfig()
            self.vpc_config = temp_model.from_map(m.get('vpcConfig'))

        return self

class E2BVolumeMountConfigVpcConfig(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # The security group ID.
        self.security_group_id = security_group_id
        # The list of vSwitches.
        self.v_switch_ids = v_switch_ids
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

