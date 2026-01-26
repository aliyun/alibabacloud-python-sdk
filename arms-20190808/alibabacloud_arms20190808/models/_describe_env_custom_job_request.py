# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnvCustomJobRequest(DaraModel):
    def __init__(
        self,
        custom_job_name: str = None,
        encrypt_yaml: bool = None,
        environment_id: str = None,
        region_id: str = None,
    ):
        # The name of the custom job.
        # 
        # This parameter is required.
        self.custom_job_name = custom_job_name
        # Specifies whether to return an encrypted YAML string.
        self.encrypt_yaml = encrypt_yaml
        # The ID of the environment instance.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_job_name is not None:
            result['CustomJobName'] = self.custom_job_name

        if self.encrypt_yaml is not None:
            result['EncryptYaml'] = self.encrypt_yaml

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomJobName') is not None:
            self.custom_job_name = m.get('CustomJobName')

        if m.get('EncryptYaml') is not None:
            self.encrypt_yaml = m.get('EncryptYaml')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

