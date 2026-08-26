# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServerIdeInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        cu: int = None,
        datasets_shrink: str = None,
        image_id: str = None,
        image_url: str = None,
        instance_id: str = None,
        instance_name: str = None,
        project_id: int = None,
        user_vpc_shrink: str = None,
    ):
        # The credential injection configuration for the instance. After this feature is enabled, you can use the default RAM role chain or specify a custom RAM role.
        self.credential_config_shrink = credential_config_shrink
        # The number of CUs used by the instance.
        self.cu = cu
        # The list of datasets mounted to the instance.
        self.datasets_shrink = datasets_shrink
        # The image ID. You can call ListServerIdeImages to obtain the ID.
        self.image_id = image_id
        # The image URL. This parameter is required when you use a non-DataWorks official image.
        self.image_url = image_url
        # The personal development environment instance ID. You can call ListServerIdeInstances to obtain the ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the personal development environment instance.
        self.instance_name = instance_name
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The VPC configuration used by the instance.
        self.user_vpc_shrink = user_vpc_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.datasets_shrink is not None:
            result['Datasets'] = self.datasets_shrink

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.user_vpc_shrink is not None:
            result['UserVpc'] = self.user_vpc_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Datasets') is not None:
            self.datasets_shrink = m.get('Datasets')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UserVpc') is not None:
            self.user_vpc_shrink = m.get('UserVpc')

        return self

