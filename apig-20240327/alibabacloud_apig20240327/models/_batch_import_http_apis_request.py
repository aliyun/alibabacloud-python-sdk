# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class BatchImportHttpApisRequest(DaraModel):
    def __init__(
        self,
        allow_update: bool = None,
        api_type: str = None,
        dry_run: bool = None,
        gateway_id: str = None,
        resource_group_id: str = None,
        spec_file_url: str = None,
        spec_oss_config: main_models.BatchImportHttpApisRequestSpecOssConfig = None,
        strategy: str = None,
        with_gateway_extension: bool = None,
    ):
        self.allow_update = allow_update
        # This parameter is required.
        self.api_type = api_type
        self.dry_run = dry_run
        self.gateway_id = gateway_id
        self.resource_group_id = resource_group_id
        self.spec_file_url = spec_file_url
        self.spec_oss_config = spec_oss_config
        self.strategy = strategy
        self.with_gateway_extension = with_gateway_extension

    def validate(self):
        if self.spec_oss_config:
            self.spec_oss_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_update is not None:
            result['allowUpdate'] = self.allow_update

        if self.api_type is not None:
            result['apiType'] = self.api_type

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.spec_file_url is not None:
            result['specFileUrl'] = self.spec_file_url

        if self.spec_oss_config is not None:
            result['specOssConfig'] = self.spec_oss_config.to_map()

        if self.strategy is not None:
            result['strategy'] = self.strategy

        if self.with_gateway_extension is not None:
            result['withGatewayExtension'] = self.with_gateway_extension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowUpdate') is not None:
            self.allow_update = m.get('allowUpdate')

        if m.get('apiType') is not None:
            self.api_type = m.get('apiType')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('specFileUrl') is not None:
            self.spec_file_url = m.get('specFileUrl')

        if m.get('specOssConfig') is not None:
            temp_model = main_models.BatchImportHttpApisRequestSpecOssConfig()
            self.spec_oss_config = temp_model.from_map(m.get('specOssConfig'))

        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')

        if m.get('withGatewayExtension') is not None:
            self.with_gateway_extension = m.get('withGatewayExtension')

        return self

class BatchImportHttpApisRequestSpecOssConfig(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        object_key: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.bucket_name = bucket_name
        # This parameter is required.
        self.object_key = object_key
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.object_key is not None:
            result['objectKey'] = self.object_key

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('objectKey') is not None:
            self.object_key = m.get('objectKey')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

