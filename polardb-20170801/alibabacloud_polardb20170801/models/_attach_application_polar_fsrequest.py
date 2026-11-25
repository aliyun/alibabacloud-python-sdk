# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachApplicationPolarFSRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        container_mount_path: str = None,
        polar_fsaccess_key_id: str = None,
        polar_fsaccess_key_secret: str = None,
        polar_fsinstance_id: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The mount point of the file system visible in the application container. If this parameter is not specified, the default value /mnt/<PolarFSInstanceId> is used for the first mount. For subsequent mounts, the current mount point of the instance remains unchanged. The value must be an absolute path that starts with a forward slash (/) but cannot be the root directory (/). It can only contain letters, digits, periods (.), underscores (_), hyphens (-), and forward slashes (/). The total length cannot exceed 128 characters, the directory depth cannot exceed 6 levels, and the length of a single level cannot exceed 63 characters. The mount point cannot be identical to or a subdirectory of the mount points of other file systems under the same application.
        self.container_mount_path = container_mount_path
        # The AccessKey ID of the Alibaba Cloud account or RAM user. Ensure that the account or RAM user is authorized when you create the PolarLakebase instance.
        self.polar_fsaccess_key_id = polar_fsaccess_key_id
        # The AccessKey secret of the Alibaba Cloud account or RAM user.
        self.polar_fsaccess_key_secret = polar_fsaccess_key_secret
        # The PolarLakebase cold storage instance ID.
        # 
        # Currently, only the following applications support cold storage instances:
        # - supabase
        # 
        # This parameter is required.
        self.polar_fsinstance_id = polar_fsinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.container_mount_path is not None:
            result['ContainerMountPath'] = self.container_mount_path

        if self.polar_fsaccess_key_id is not None:
            result['PolarFSAccessKeyId'] = self.polar_fsaccess_key_id

        if self.polar_fsaccess_key_secret is not None:
            result['PolarFSAccessKeySecret'] = self.polar_fsaccess_key_secret

        if self.polar_fsinstance_id is not None:
            result['PolarFSInstanceId'] = self.polar_fsinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ContainerMountPath') is not None:
            self.container_mount_path = m.get('ContainerMountPath')

        if m.get('PolarFSAccessKeyId') is not None:
            self.polar_fsaccess_key_id = m.get('PolarFSAccessKeyId')

        if m.get('PolarFSAccessKeySecret') is not None:
            self.polar_fsaccess_key_secret = m.get('PolarFSAccessKeySecret')

        if m.get('PolarFSInstanceId') is not None:
            self.polar_fsinstance_id = m.get('PolarFSInstanceId')

        return self

