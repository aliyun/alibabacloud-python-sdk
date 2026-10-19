# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterAIDBClusterCustomModelShrinkRequest(DaraModel):
    def __init__(
        self,
        container_env_shrink: str = None,
        custom_oss_bucket_name: str = None,
        custom_oss_bucket_path: str = None,
        dbinstance_class: str = None,
        direct_command: str = None,
        display_model_name: str = None,
        image_name: str = None,
        inference_engine: str = None,
        model_name: str = None,
        model_params_shrink: str = None,
        region_id: str = None,
        registry_password: str = None,
        registry_username: str = None,
    ):
        # The container startup environment variables. Variable names cannot be empty or contain whitespace. Variable values can be empty strings.
        self.container_env_shrink = container_env_shrink
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.custom_oss_bucket_name = custom_oss_bucket_name
        # The model path in the OSS bucket.
        # 
        # This parameter is required.
        self.custom_oss_bucket_path = custom_oss_bucket_path
        # The GPU instance type used for model deployment. Required when configuring deployment parameters.
        self.dbinstance_class = dbinstance_class
        # The direct startup command for the model container.
        self.direct_command = direct_command
        # The display name in the candidate list and the initial invocation name for clients.
        self.display_model_name = display_model_name
        # The full reference of the customer-owned inference image, in the format of registry/repository:tag.
        self.image_name = image_name
        # The inference engine. Required when configuring deployment parameters. Valid values: vllm and sglang.
        self.inference_engine = inference_engine
        # The custom model registration key and model directory name.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The model startup parameters. Parameter keys must start with --.
        self.model_params_shrink = model_params_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The password or temporary token for the customer image repository. Required when ImageName is specified.
        self.registry_password = registry_password
        # The username for the customer image repository. Required when ImageName is specified.
        self.registry_username = registry_username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_env_shrink is not None:
            result['ContainerEnv'] = self.container_env_shrink

        if self.custom_oss_bucket_name is not None:
            result['CustomOssBucketName'] = self.custom_oss_bucket_name

        if self.custom_oss_bucket_path is not None:
            result['CustomOssBucketPath'] = self.custom_oss_bucket_path

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.direct_command is not None:
            result['DirectCommand'] = self.direct_command

        if self.display_model_name is not None:
            result['DisplayModelName'] = self.display_model_name

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.inference_engine is not None:
            result['InferenceEngine'] = self.inference_engine

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_params_shrink is not None:
            result['ModelParams'] = self.model_params_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.registry_password is not None:
            result['RegistryPassword'] = self.registry_password

        if self.registry_username is not None:
            result['RegistryUsername'] = self.registry_username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerEnv') is not None:
            self.container_env_shrink = m.get('ContainerEnv')

        if m.get('CustomOssBucketName') is not None:
            self.custom_oss_bucket_name = m.get('CustomOssBucketName')

        if m.get('CustomOssBucketPath') is not None:
            self.custom_oss_bucket_path = m.get('CustomOssBucketPath')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DirectCommand') is not None:
            self.direct_command = m.get('DirectCommand')

        if m.get('DisplayModelName') is not None:
            self.display_model_name = m.get('DisplayModelName')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InferenceEngine') is not None:
            self.inference_engine = m.get('InferenceEngine')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelParams') is not None:
            self.model_params_shrink = m.get('ModelParams')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegistryPassword') is not None:
            self.registry_password = m.get('RegistryPassword')

        if m.get('RegistryUsername') is not None:
            self.registry_username = m.get('RegistryUsername')

        return self

