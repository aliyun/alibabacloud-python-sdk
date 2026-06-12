# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ImportHttpApiRequest(DaraModel):
    def __init__(
        self,
        deploy_configs: List[main_models.HttpApiDeployConfig] = None,
        description: str = None,
        dry_run: bool = None,
        gateway_id: str = None,
        mcp_route_id: str = None,
        name: str = None,
        resource_group_id: str = None,
        spec_content_base_64: str = None,
        spec_file_url: str = None,
        spec_oss_config: main_models.ImportHttpApiRequestSpecOssConfig = None,
        strategy: str = None,
        target_http_api_id: str = None,
        version_config: main_models.HttpApiVersionConfig = None,
        with_gateway_extension: bool = None,
    ):
        # The API deployment configurations.
        self.deploy_configs = deploy_configs
        # The description of the API to import. If omitted, the description is taken from the API definition. The maximum length is 255 bytes.
        self.description = description
        # Indicates whether to perform a dry run. If `true`, the system validates the request but does not import the API.
        self.dry_run = dry_run
        # The gateway ID.
        self.gateway_id = gateway_id
        # The MCP route ID.
        self.mcp_route_id = mcp_route_id
        # The name of the API to import. If omitted, the name is taken from the API definition file. If an API with the same name and versioning configuration already exists, the import acts as an update based on the specified `strategy`.
        self.name = name
        # The [resource group ID](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The Base64-encoded API definition. It supports OpenAPI Specification (OAS) 2.0 and 3.0 and can be in either YAML or JSON format. This parameter takes precedence over `specFileUrl`. If the file size is larger than 10 MB, use the `specFileUrl` parameter.
        self.spec_content_base_64 = spec_content_base_64
        # The URL of the API definition file stored in OSS. The URL must be accessible from the public network or be an internal OSS endpoint in the same region. For OSS objects that are not publicly readable, use a presigned URL. For details, see [Download a file by using a presigned URL](https://help.aliyun.com/document_detail/39607.html).
        self.spec_file_url = spec_file_url
        # Configuration for fetching the API definition from an OSS bucket.
        self.spec_oss_config = spec_oss_config
        # The update strategy to apply when an API with the same name and versioning configuration already exists.
        # 
        # - `SpecOnly`: Overwrites the existing API completely with the imported definition.
        # 
        # - `SpecFirst`: Updates existing APIs and creates new ones based on the imported definition. Existing APIs not included in the import file are unaffected.
        # 
        # - `ExistFirst`: Creates new APIs from the imported definition but does not modify any existing APIs. This is the default strategy.
        self.strategy = strategy
        # If you specify this parameter, the import updates the specified API instead of creating a new one or searching for an existing API by name and versioning configuration. The target API must be an HTTP API.
        self.target_http_api_id = target_http_api_id
        # The versioning configuration for the API. If an existing API matches the specified name (and version, if enabled), this import updates that API.
        self.version_config = version_config
        self.with_gateway_extension = with_gateway_extension

    def validate(self):
        if self.deploy_configs:
            for v1 in self.deploy_configs:
                 if v1:
                    v1.validate()
        if self.spec_oss_config:
            self.spec_oss_config.validate()
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k1 in self.deploy_configs:
                result['deployConfigs'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.mcp_route_id is not None:
            result['mcpRouteId'] = self.mcp_route_id

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.spec_content_base_64 is not None:
            result['specContentBase64'] = self.spec_content_base_64

        if self.spec_file_url is not None:
            result['specFileUrl'] = self.spec_file_url

        if self.spec_oss_config is not None:
            result['specOssConfig'] = self.spec_oss_config.to_map()

        if self.strategy is not None:
            result['strategy'] = self.strategy

        if self.target_http_api_id is not None:
            result['targetHttpApiId'] = self.target_http_api_id

        if self.version_config is not None:
            result['versionConfig'] = self.version_config.to_map()

        if self.with_gateway_extension is not None:
            result['withGatewayExtension'] = self.with_gateway_extension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k1 in m.get('deployConfigs'):
                temp_model = main_models.HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('mcpRouteId') is not None:
            self.mcp_route_id = m.get('mcpRouteId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('specContentBase64') is not None:
            self.spec_content_base_64 = m.get('specContentBase64')

        if m.get('specFileUrl') is not None:
            self.spec_file_url = m.get('specFileUrl')

        if m.get('specOssConfig') is not None:
            temp_model = main_models.ImportHttpApiRequestSpecOssConfig()
            self.spec_oss_config = temp_model.from_map(m.get('specOssConfig'))

        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')

        if m.get('targetHttpApiId') is not None:
            self.target_http_api_id = m.get('targetHttpApiId')

        if m.get('versionConfig') is not None:
            temp_model = main_models.HttpApiVersionConfig()
            self.version_config = temp_model.from_map(m.get('versionConfig'))

        if m.get('withGatewayExtension') is not None:
            self.with_gateway_extension = m.get('withGatewayExtension')

        return self

class ImportHttpApiRequestSpecOssConfig(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        object_key: str = None,
        region_id: str = None,
    ):
        # The name of the OSS bucket that contains the API definition file.
        self.bucket_name = bucket_name
        # The object key (file path) of the API definition file within the bucket.
        self.object_key = object_key
        # The ID of the region where the OSS bucket is located.
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

