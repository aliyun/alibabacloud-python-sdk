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
    ):
        # The deployment configuration.
        self.deploy_configs = deploy_configs
        # The API description, which cannot exceed 255 bytes in length. If you do not specify a description, a description is extracted from the definition file.
        self.description = description
        # Specifies whether to perform a dry run. If this parameter is set to true, a dry run is performed without importing the file.
        self.dry_run = dry_run
        self.gateway_id = gateway_id
        # The MCP route ID.
        self.mcp_route_id = mcp_route_id
        # The API name. If you do not specify a name, a name is extracted from the definition file. If a name and a versioning configuration already exist, the existing API definition is updated based on the strategy field.
        self.name = name
        # [The resource group ID](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The Base64-encoded API definition. OAS 2.0 and OAS 3.0 specifications are supported. YAML and JSON formats are supported. This parameter precedes over the specFileUrl parameter. However, if the file size exceeds 10 MB, use the specFileUrl parameter to pass the definition.
        self.spec_content_base_64 = spec_content_base_64
        # The download URL of the API definition file. You can download the file over the Internet or by using an Object Storage Service (OSS) internal download URL that belongs to the current region. You must obtain the required permissions to download the file. For OSS URLs that are not publicly readable, refer to [Download objects using presigned URLs](https://help.aliyun.com/document_detail/39607.html) to specify URLs that provide download permissions. Currently, only OSS URLs are supported.
        self.spec_file_url = spec_file_url
        # The OSS information.
        self.spec_oss_config = spec_oss_config
        # The update policy when the API to be imported has the same version and name as an existing one. Valid values:
        # 
        # *   SpectOnly: All configurations in the file take effect.
        # *   SpecFirst: The file takes precedence. New APIs are created and existing ones are updated. APIs not included in the file remain unchanged.
        # *   ExistFirst (default): The existing APIs take precedence. New APIs are created but existing ones remain unchanged. If this parameter is not specified, the ExistFirst policy takes effect.
        self.strategy = strategy
        # The API to be updated. If this parameter is specified, this import updates only the specified API. New APIs are not created and unspecified existing APIs are not updated. Only REST APIs can be specified.
        self.target_http_api_id = target_http_api_id
        # The API versioning configuration. If versioning is enabled for an API and the version and name of an API to be imported are the same as those of the existing API, the existing API is updated by this import. If versioning is not enabled for an API and the name of an API to be imported are the same as that of the existing API, the existing API is updated by this import.
        self.version_config = version_config

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

        return self

class ImportHttpApiRequestSpecOssConfig(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        object_key: str = None,
        region_id: str = None,
    ):
        # The bucket name.
        self.bucket_name = bucket_name
        # The full path of the file.
        self.object_key = object_key
        # The region ID.
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

