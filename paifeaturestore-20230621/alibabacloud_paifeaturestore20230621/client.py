# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paifeaturestore20230621 import models as pai_feature_store_20230621_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('paifeaturestore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_project_feature_entity_hot_id_version_with_options(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        request: pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeProjectFeatureEntityHotIdVersion',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}/action/changehotidversion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_project_feature_entity_hot_id_version_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        request: pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeProjectFeatureEntityHotIdVersion',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}/action/changehotidversion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_project_feature_entity_hot_id_version(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        request: pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionRequest,
    ) -> pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_project_feature_entity_hot_id_version_with_options(instance_id, project_id, feature_entity_name, request, headers, runtime)

    async def change_project_feature_entity_hot_id_version_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        request: pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionRequest,
    ) -> pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_project_feature_entity_hot_id_version_with_options_async(instance_id, project_id, feature_entity_name, request, headers, runtime)

    def check_instance_datasource_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CheckInstanceDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CheckInstanceDatasourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/action/checkdatasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CheckInstanceDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_datasource_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CheckInstanceDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CheckInstanceDatasourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/action/checkdatasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CheckInstanceDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_datasource(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CheckInstanceDatasourceRequest,
    ) -> pai_feature_store_20230621_models.CheckInstanceDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_instance_datasource_with_options(instance_id, request, headers, runtime)

    async def check_instance_datasource_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CheckInstanceDatasourceRequest,
    ) -> pai_feature_store_20230621_models.CheckInstanceDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_instance_datasource_with_options_async(instance_id, request, headers, runtime)

    def create_datasource_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateDatasourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_datasource_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateDatasourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_datasource(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateDatasourceRequest,
    ) -> pai_feature_store_20230621_models.CreateDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_datasource_with_options(instance_id, request, headers, runtime)

    async def create_datasource_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateDatasourceRequest,
    ) -> pai_feature_store_20230621_models.CreateDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_datasource_with_options_async(instance_id, request, headers, runtime)

    def create_feature_entity_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureEntityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateFeatureEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_id):
            body['JoinId'] = request.join_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_entity_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureEntityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateFeatureEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_id):
            body['JoinId'] = request.join_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_entity(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureEntityRequest,
    ) -> pai_feature_store_20230621_models.CreateFeatureEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_entity_with_options(instance_id, request, headers, runtime)

    async def create_feature_entity_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureEntityRequest,
    ) -> pai_feature_store_20230621_models.CreateFeatureEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_feature_entity_with_options_async(instance_id, request, headers, runtime)

    def create_feature_view_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateFeatureViewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.feature_entity_id):
            body['FeatureEntityId'] = request.feature_entity_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.register_datasource_id):
            body['RegisterDatasourceId'] = request.register_datasource_id
        if not UtilClient.is_unset(request.register_table):
            body['RegisterTable'] = request.register_table
        if not UtilClient.is_unset(request.sync_online_table):
            body['SyncOnlineTable'] = request.sync_online_table
        if not UtilClient.is_unset(request.ttl):
            body['TTL'] = request.ttl
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.write_method):
            body['WriteMethod'] = request.write_method
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_view_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateFeatureViewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.feature_entity_id):
            body['FeatureEntityId'] = request.feature_entity_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.register_datasource_id):
            body['RegisterDatasourceId'] = request.register_datasource_id
        if not UtilClient.is_unset(request.register_table):
            body['RegisterTable'] = request.register_table
        if not UtilClient.is_unset(request.sync_online_table):
            body['SyncOnlineTable'] = request.sync_online_table
        if not UtilClient.is_unset(request.ttl):
            body['TTL'] = request.ttl
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.write_method):
            body['WriteMethod'] = request.write_method
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_view(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureViewRequest,
    ) -> pai_feature_store_20230621_models.CreateFeatureViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_view_with_options(instance_id, request, headers, runtime)

    async def create_feature_view_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureViewRequest,
    ) -> pai_feature_store_20230621_models.CreateFeatureViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_feature_view_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: pai_feature_store_20230621_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: pai_feature_store_20230621_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: pai_feature_store_20230621_models.CreateInstanceRequest,
    ) -> pai_feature_store_20230621_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: pai_feature_store_20230621_models.CreateInstanceRequest,
    ) -> pai_feature_store_20230621_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_label_table_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateLabelTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateLabelTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_label_table_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateLabelTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateLabelTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_label_table(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateLabelTableRequest,
    ) -> pai_feature_store_20230621_models.CreateLabelTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_label_table_with_options(instance_id, request, headers, runtime)

    async def create_label_table_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateLabelTableRequest,
    ) -> pai_feature_store_20230621_models.CreateLabelTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_label_table_with_options_async(instance_id, request, headers, runtime)

    def create_model_feature_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateModelFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_feature_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateModelFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_feature(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateModelFeatureRequest,
    ) -> pai_feature_store_20230621_models.CreateModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_feature_with_options(instance_id, request, headers, runtime)

    async def create_model_feature_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateModelFeatureRequest,
    ) -> pai_feature_store_20230621_models.CreateModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_feature_with_options_async(instance_id, request, headers, runtime)

    def create_project_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.offline_datasource_id):
            body['OfflineDatasourceId'] = request.offline_datasource_id
        if not UtilClient.is_unset(request.offline_life_cycle):
            body['OfflineLifeCycle'] = request.offline_life_cycle
        if not UtilClient.is_unset(request.online_datasource_id):
            body['OnlineDatasourceId'] = request.online_datasource_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.offline_datasource_id):
            body['OfflineDatasourceId'] = request.offline_datasource_id
        if not UtilClient.is_unset(request.offline_life_cycle):
            body['OfflineLifeCycle'] = request.offline_life_cycle
        if not UtilClient.is_unset(request.online_datasource_id):
            body['OnlineDatasourceId'] = request.online_datasource_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateProjectRequest,
    ) -> pai_feature_store_20230621_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(instance_id, request, headers, runtime)

    async def create_project_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateProjectRequest,
    ) -> pai_feature_store_20230621_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(instance_id, request, headers, runtime)

    def create_service_identity_role_with_options(
        self,
        request: pai_feature_store_20230621_models.CreateServiceIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/serviceidentityroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_identity_role_with_options_async(
        self,
        request: pai_feature_store_20230621_models.CreateServiceIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/serviceidentityroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_identity_role(
        self,
        request: pai_feature_store_20230621_models.CreateServiceIdentityRoleRequest,
    ) -> pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_identity_role_with_options(request, headers, runtime)

    async def create_service_identity_role_async(
        self,
        request: pai_feature_store_20230621_models.CreateServiceIdentityRoleRequest,
    ) -> pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_identity_role_with_options_async(request, headers, runtime)

    def delete_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteDatasourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteDatasourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_datasource(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> pai_feature_store_20230621_models.DeleteDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_datasource_with_options(instance_id, datasource_id, headers, runtime)

    async def delete_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> pai_feature_store_20230621_models.DeleteDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_datasource_with_options_async(instance_id, datasource_id, headers, runtime)

    def delete_feature_entity_with_options(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteFeatureEntityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_entity_with_options_async(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteFeatureEntityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature_entity(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> pai_feature_store_20230621_models.DeleteFeatureEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_feature_entity_with_options(instance_id, feature_entity_id, headers, runtime)

    async def delete_feature_entity_async(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> pai_feature_store_20230621_models.DeleteFeatureEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_feature_entity_with_options_async(instance_id, feature_entity_id, headers, runtime)

    def delete_feature_view_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteFeatureViewResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_view_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteFeatureViewResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature_view(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.DeleteFeatureViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_feature_view_with_options(instance_id, feature_view_id, headers, runtime)

    async def delete_feature_view_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.DeleteFeatureViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_feature_view_with_options_async(instance_id, feature_view_id, headers, runtime)

    def delete_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteLabelTableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteLabelTableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_label_table(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> pai_feature_store_20230621_models.DeleteLabelTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_label_table_with_options(instance_id, label_table_id, headers, runtime)

    async def delete_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> pai_feature_store_20230621_models.DeleteLabelTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_label_table_with_options_async(instance_id, label_table_id, headers, runtime)

    def delete_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteModelFeatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteModelFeatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.DeleteModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_feature_with_options(instance_id, model_feature_id, headers, runtime)

    async def delete_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.DeleteModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_feature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def delete_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteProjectResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteProjectResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(instance_id, project_id, headers, runtime)

    async def delete_project_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(instance_id, project_id, headers, runtime)

    def export_model_feature_training_set_table_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_view_config):
            body['FeatureViewConfig'] = request.feature_view_config
        if not UtilClient.is_unset(request.label_input_config):
            body['LabelInputConfig'] = request.label_input_config
        if not UtilClient.is_unset(request.training_set_config):
            body['TrainingSetConfig'] = request.training_set_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportModelFeatureTrainingSetTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/action/exporttrainingsettable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_model_feature_training_set_table_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_view_config):
            body['FeatureViewConfig'] = request.feature_view_config
        if not UtilClient.is_unset(request.label_input_config):
            body['LabelInputConfig'] = request.label_input_config
        if not UtilClient.is_unset(request.training_set_config):
            body['TrainingSetConfig'] = request.training_set_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportModelFeatureTrainingSetTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/action/exporttrainingsettable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_model_feature_training_set_table(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableRequest,
    ) -> pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_model_feature_training_set_table_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def export_model_feature_training_set_table_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableRequest,
    ) -> pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.export_model_feature_training_set_table_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def get_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetDatasourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetDatasourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_datasource(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> pai_feature_store_20230621_models.GetDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_datasource_with_options(instance_id, datasource_id, headers, runtime)

    async def get_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> pai_feature_store_20230621_models.GetDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_datasource_with_options_async(instance_id, datasource_id, headers, runtime)

    def get_datasource_table_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetDatasourceTableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasourceTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_datasource_table_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetDatasourceTableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasourceTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_datasource_table(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
    ) -> pai_feature_store_20230621_models.GetDatasourceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_datasource_table_with_options(instance_id, datasource_id, table_name, headers, runtime)

    async def get_datasource_table_async(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
    ) -> pai_feature_store_20230621_models.GetDatasourceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_datasource_table_with_options_async(instance_id, datasource_id, table_name, headers, runtime)

    def get_feature_entity_with_options(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetFeatureEntityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_entity_with_options_async(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetFeatureEntityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_entity(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> pai_feature_store_20230621_models.GetFeatureEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_entity_with_options(instance_id, feature_entity_id, headers, runtime)

    async def get_feature_entity_async(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> pai_feature_store_20230621_models.GetFeatureEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_feature_entity_with_options_async(instance_id, feature_entity_id, headers, runtime)

    def get_feature_view_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetFeatureViewResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_view_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetFeatureViewResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_view(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.GetFeatureViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_view_with_options(instance_id, feature_view_id, headers, runtime)

    async def get_feature_view_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.GetFeatureViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_feature_view_with_options_async(instance_id, feature_view_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> pai_feature_store_20230621_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> pai_feature_store_20230621_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetLabelTableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetLabelTableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_label_table(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> pai_feature_store_20230621_models.GetLabelTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_label_table_with_options(instance_id, label_table_id, headers, runtime)

    async def get_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> pai_feature_store_20230621_models.GetLabelTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_label_table_with_options_async(instance_id, label_table_id, headers, runtime)

    def get_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetModelFeatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetModelFeatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.GetModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_feature_with_options(instance_id, model_feature_id, headers, runtime)

    async def get_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.GetModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_feature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def get_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(instance_id, project_id, headers, runtime)

    async def get_project_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(instance_id, project_id, headers, runtime)

    def get_project_feature_entity_with_options(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_feature_entity_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_feature_entity(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_feature_entity_with_options(instance_id, project_id, feature_entity_name, headers, runtime)

    async def get_project_feature_entity_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_feature_entity_with_options_async(instance_id, project_id, feature_entity_name, headers, runtime)

    def get_project_feature_entity_hot_ids_with_options(
        self,
        instance_id: str,
        project_id: str,
        next_seq_number: str,
        feature_entity_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityHotIdsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureEntityHotIds',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}/hotids/{OpenApiUtilClient.get_encode_param(next_seq_number)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureEntityHotIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_feature_entity_hot_ids_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        next_seq_number: str,
        feature_entity_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityHotIdsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureEntityHotIds',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}/hotids/{OpenApiUtilClient.get_encode_param(next_seq_number)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureEntityHotIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_feature_entity_hot_ids(
        self,
        instance_id: str,
        project_id: str,
        next_seq_number: str,
        feature_entity_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityHotIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_feature_entity_hot_ids_with_options(instance_id, project_id, next_seq_number, feature_entity_name, headers, runtime)

    async def get_project_feature_entity_hot_ids_async(
        self,
        instance_id: str,
        project_id: str,
        next_seq_number: str,
        feature_entity_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityHotIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_feature_entity_hot_ids_with_options_async(instance_id, project_id, next_seq_number, feature_entity_name, headers, runtime)

    def get_project_feature_view_with_options(
        self,
        instance_id: str,
        project_id: str,
        feature_view_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureViewResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_feature_view_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        feature_view_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureViewResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_feature_view(
        self,
        instance_id: str,
        project_id: str,
        feature_view_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_feature_view_with_options(instance_id, project_id, feature_view_name, headers, runtime)

    async def get_project_feature_view_async(
        self,
        instance_id: str,
        project_id: str,
        feature_view_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_feature_view_with_options_async(instance_id, project_id, feature_view_name, headers, runtime)

    def get_project_model_feature_with_options(
        self,
        instance_id: str,
        project_id: str,
        model_feature_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectModelFeatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_model_feature_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        model_feature_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectModelFeatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_model_feature(
        self,
        instance_id: str,
        project_id: str,
        model_feature_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_model_feature_with_options(instance_id, project_id, model_feature_name, headers, runtime)

    async def get_project_model_feature_async(
        self,
        instance_id: str,
        project_id: str,
        model_feature_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_model_feature_with_options_async(instance_id, project_id, model_feature_name, headers, runtime)

    def get_service_identity_role_with_options(
        self,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetServiceIdentityRoleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/serviceidentityroles/{OpenApiUtilClient.get_encode_param(role_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_identity_role_with_options_async(
        self,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetServiceIdentityRoleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/serviceidentityroles/{OpenApiUtilClient.get_encode_param(role_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_identity_role(
        self,
        role_name: str,
    ) -> pai_feature_store_20230621_models.GetServiceIdentityRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_identity_role_with_options(role_name, headers, runtime)

    async def get_service_identity_role_async(
        self,
        role_name: str,
    ) -> pai_feature_store_20230621_models.GetServiceIdentityRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_identity_role_with_options_async(role_name, headers, runtime)

    def get_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        instance_id: str,
        task_id: str,
    ) -> pai_feature_store_20230621_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(instance_id, task_id, headers, runtime)

    async def get_task_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> pai_feature_store_20230621_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(instance_id, task_id, headers, runtime)

    def list_datasource_tables_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.ListDatasourceTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListDatasourceTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasourceTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourceTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasource_tables_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.ListDatasourceTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListDatasourceTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasourceTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourceTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasource_tables(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.ListDatasourceTablesRequest,
    ) -> pai_feature_store_20230621_models.ListDatasourceTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_datasource_tables_with_options(instance_id, datasource_id, request, headers, runtime)

    async def list_datasource_tables_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.ListDatasourceTablesRequest,
    ) -> pai_feature_store_20230621_models.ListDatasourceTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_datasource_tables_with_options_async(instance_id, datasource_id, request, headers, runtime)

    def list_datasources_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListDatasourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListDatasourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasources',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasources_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListDatasourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListDatasourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasources',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasources(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListDatasourcesRequest,
    ) -> pai_feature_store_20230621_models.ListDatasourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_datasources_with_options(instance_id, request, headers, runtime)

    async def list_datasources_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListDatasourcesRequest,
    ) -> pai_feature_store_20230621_models.ListDatasourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_datasources_with_options_async(instance_id, request, headers, runtime)

    def list_feature_entities_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureEntitiesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureEntitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureEntitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_entity_ids):
            request.feature_entity_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_entity_ids, 'FeatureEntityIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_entity_ids_shrink):
            query['FeatureEntityIds'] = request.feature_entity_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureEntities',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_entities_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureEntitiesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureEntitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureEntitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_entity_ids):
            request.feature_entity_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_entity_ids, 'FeatureEntityIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_entity_ids_shrink):
            query['FeatureEntityIds'] = request.feature_entity_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureEntities',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_entities(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListFeatureEntitiesRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_entities_with_options(instance_id, request, headers, runtime)

    async def list_feature_entities_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListFeatureEntitiesRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_entities_with_options_async(instance_id, request, headers, runtime)

    def list_feature_view_field_relationships_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewFieldRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/fields/{OpenApiUtilClient.get_encode_param(field_name)}/relationships',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_view_field_relationships_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewFieldRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/fields/{OpenApiUtilClient.get_encode_param(field_name)}/relationships',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_view_field_relationships(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
    ) -> pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_view_field_relationships_with_options(instance_id, feature_view_id, field_name, headers, runtime)

    async def list_feature_view_field_relationships_async(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
    ) -> pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_view_field_relationships_with_options_async(instance_id, feature_view_id, field_name, headers, runtime)

    def list_feature_view_relationships_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/relationships',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_view_relationships_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/relationships',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_view_relationships(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_view_relationships_with_options(instance_id, feature_view_id, headers, runtime)

    async def list_feature_view_relationships_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_view_relationships_with_options_async(instance_id, feature_view_id, headers, runtime)

    def list_feature_views_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureViewsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureViewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_view_ids):
            request.feature_view_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_view_ids, 'FeatureViewIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_view_ids_shrink):
            query['FeatureViewIds'] = request.feature_view_ids_shrink
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_views_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureViewsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureViewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_view_ids):
            request.feature_view_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_view_ids, 'FeatureViewIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_view_ids_shrink):
            query['FeatureViewIds'] = request.feature_view_ids_shrink
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_views(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListFeatureViewsRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureViewsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_views_with_options(instance_id, request, headers, runtime)

    async def list_feature_views_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListFeatureViewsRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureViewsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_views_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        request: pai_feature_store_20230621_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: pai_feature_store_20230621_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: pai_feature_store_20230621_models.ListInstancesRequest,
    ) -> pai_feature_store_20230621_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: pai_feature_store_20230621_models.ListInstancesRequest,
    ) -> pai_feature_store_20230621_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_label_tables_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListLabelTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListLabelTablesResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListLabelTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_table_ids):
            request.label_table_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_table_ids, 'LabelTableIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_table_ids_shrink):
            query['LabelTableIds'] = request.label_table_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLabelTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListLabelTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_label_tables_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListLabelTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListLabelTablesResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListLabelTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_table_ids):
            request.label_table_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_table_ids, 'LabelTableIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_table_ids_shrink):
            query['LabelTableIds'] = request.label_table_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLabelTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListLabelTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_label_tables(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListLabelTablesRequest,
    ) -> pai_feature_store_20230621_models.ListLabelTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_label_tables_with_options(instance_id, request, headers, runtime)

    async def list_label_tables_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListLabelTablesRequest,
    ) -> pai_feature_store_20230621_models.ListLabelTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_label_tables_with_options_async(instance_id, request, headers, runtime)

    def list_model_features_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListModelFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListModelFeaturesResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListModelFeaturesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model_feature_ids):
            request.model_feature_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_feature_ids, 'ModelFeatureIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.model_feature_ids_shrink):
            query['ModelFeatureIds'] = request.model_feature_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListModelFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_features_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListModelFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListModelFeaturesResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListModelFeaturesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model_feature_ids):
            request.model_feature_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_feature_ids, 'ModelFeatureIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.model_feature_ids_shrink):
            query['ModelFeatureIds'] = request.model_feature_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListModelFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_features(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListModelFeaturesRequest,
    ) -> pai_feature_store_20230621_models.ListModelFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_features_with_options(instance_id, request, headers, runtime)

    async def list_model_features_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListModelFeaturesRequest,
    ) -> pai_feature_store_20230621_models.ListModelFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_model_features_with_options_async(instance_id, request, headers, runtime)

    def list_project_feature_view_owners_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewOwnersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViewOwners',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviewowners',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewOwnersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_feature_view_owners_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewOwnersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViewOwners',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviewowners',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewOwnersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_feature_view_owners(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewOwnersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_feature_view_owners_with_options(instance_id, project_id, headers, runtime)

    async def list_project_feature_view_owners_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewOwnersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_feature_view_owners_with_options_async(instance_id, project_id, headers, runtime)

    def list_project_feature_view_tags_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewTagsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViewTags',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviewtags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_feature_view_tags_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewTagsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViewTags',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviewtags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_feature_view_tags(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_feature_view_tags_with_options(instance_id, project_id, headers, runtime)

    async def list_project_feature_view_tags_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_feature_view_tags_with_options_async(instance_id, project_id, headers, runtime)

    def list_project_feature_views_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviews',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_feature_views_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviews',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_feature_views(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_feature_views_with_options(instance_id, project_id, headers, runtime)

    async def list_project_feature_views_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_feature_views_with_options_async(instance_id, project_id, headers, runtime)

    def list_projects_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.project_ids):
            request.project_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.project_ids, 'ProjectIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids_shrink):
            query['ProjectIds'] = request.project_ids_shrink
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.project_ids):
            request.project_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.project_ids, 'ProjectIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids_shrink):
            query['ProjectIds'] = request.project_ids_shrink
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListProjectsRequest,
    ) -> pai_feature_store_20230621_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(instance_id, request, headers, runtime)

    async def list_projects_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListProjectsRequest,
    ) -> pai_feature_store_20230621_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(instance_id, request, headers, runtime)

    def list_task_logs_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: pai_feature_store_20230621_models.ListTaskLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListTaskLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskLogs',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_logs_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: pai_feature_store_20230621_models.ListTaskLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListTaskLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskLogs',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTaskLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_logs(
        self,
        instance_id: str,
        task_id: str,
        request: pai_feature_store_20230621_models.ListTaskLogsRequest,
    ) -> pai_feature_store_20230621_models.ListTaskLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_logs_with_options(instance_id, task_id, request, headers, runtime)

    async def list_task_logs_async(
        self,
        instance_id: str,
        task_id: str,
        request: pai_feature_store_20230621_models.ListTaskLogsRequest,
    ) -> pai_feature_store_20230621_models.ListTaskLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_task_logs_with_options_async(instance_id, task_id, request, headers, runtime)

    def list_tasks_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListTasksRequest,
    ) -> pai_feature_store_20230621_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(instance_id, request, headers, runtime)

    async def list_tasks_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListTasksRequest,
    ) -> pai_feature_store_20230621_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(instance_id, request, headers, runtime)

    def publish_feature_view_table_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.PublishFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.PublishFeatureViewTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.event_time):
            body['EventTime'] = request.event_time
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.offline_to_online):
            body['OfflineToOnline'] = request.offline_to_online
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/action/publishtable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.PublishFeatureViewTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_feature_view_table_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.PublishFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.PublishFeatureViewTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.event_time):
            body['EventTime'] = request.event_time
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.offline_to_online):
            body['OfflineToOnline'] = request.offline_to_online
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/action/publishtable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.PublishFeatureViewTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_feature_view_table(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.PublishFeatureViewTableRequest,
    ) -> pai_feature_store_20230621_models.PublishFeatureViewTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_feature_view_table_with_options(instance_id, feature_view_id, request, headers, runtime)

    async def publish_feature_view_table_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.PublishFeatureViewTableRequest,
    ) -> pai_feature_store_20230621_models.PublishFeatureViewTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_feature_view_table_with_options_async(instance_id, feature_view_id, request, headers, runtime)

    def update_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.UpdateDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateDatasourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.UpdateDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateDatasourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_datasource(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.UpdateDatasourceRequest,
    ) -> pai_feature_store_20230621_models.UpdateDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_datasource_with_options(instance_id, datasource_id, request, headers, runtime)

    async def update_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.UpdateDatasourceRequest,
    ) -> pai_feature_store_20230621_models.UpdateDatasourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_datasource_with_options_async(instance_id, datasource_id, request, headers, runtime)

    def update_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        request: pai_feature_store_20230621_models.UpdateLabelTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateLabelTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        request: pai_feature_store_20230621_models.UpdateLabelTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateLabelTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_label_table(
        self,
        instance_id: str,
        label_table_id: str,
        request: pai_feature_store_20230621_models.UpdateLabelTableRequest,
    ) -> pai_feature_store_20230621_models.UpdateLabelTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_label_table_with_options(instance_id, label_table_id, request, headers, runtime)

    async def update_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
        request: pai_feature_store_20230621_models.UpdateLabelTableRequest,
    ) -> pai_feature_store_20230621_models.UpdateLabelTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_label_table_with_options_async(instance_id, label_table_id, request, headers, runtime)

    def update_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureRequest,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_feature_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def update_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureRequest,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_model_feature_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def update_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        request: pai_feature_store_20230621_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        request: pai_feature_store_20230621_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        instance_id: str,
        project_id: str,
        request: pai_feature_store_20230621_models.UpdateProjectRequest,
    ) -> pai_feature_store_20230621_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(instance_id, project_id, request, headers, runtime)

    async def update_project_async(
        self,
        instance_id: str,
        project_id: str,
        request: pai_feature_store_20230621_models.UpdateProjectRequest,
    ) -> pai_feature_store_20230621_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(instance_id, project_id, request, headers, runtime)

    def write_feature_view_table_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.WriteFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.WriteFeatureViewTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        if not UtilClient.is_unset(request.url_datasource):
            body['UrlDatasource'] = request.url_datasource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WriteFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/action/writetable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.WriteFeatureViewTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def write_feature_view_table_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.WriteFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.WriteFeatureViewTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        if not UtilClient.is_unset(request.url_datasource):
            body['UrlDatasource'] = request.url_datasource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WriteFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/action/writetable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.WriteFeatureViewTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def write_feature_view_table(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.WriteFeatureViewTableRequest,
    ) -> pai_feature_store_20230621_models.WriteFeatureViewTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.write_feature_view_table_with_options(instance_id, feature_view_id, request, headers, runtime)

    async def write_feature_view_table_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.WriteFeatureViewTableRequest,
    ) -> pai_feature_store_20230621_models.WriteFeatureViewTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.write_feature_view_table_with_options_async(instance_id, feature_view_id, request, headers, runtime)

    def write_project_feature_entity_hot_ids_with_options(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        request: pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hot_ids):
            body['HotIds'] = request.hot_ids
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WriteProjectFeatureEntityHotIds',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}/action/writehotids',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def write_project_feature_entity_hot_ids_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        request: pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hot_ids):
            body['HotIds'] = request.hot_ids
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WriteProjectFeatureEntityHotIds',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}/action/writehotids',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def write_project_feature_entity_hot_ids(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        request: pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsRequest,
    ) -> pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.write_project_feature_entity_hot_ids_with_options(instance_id, project_id, feature_entity_name, request, headers, runtime)

    async def write_project_feature_entity_hot_ids_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        request: pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsRequest,
    ) -> pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.write_project_feature_entity_hot_ids_with_options_async(instance_id, project_id, feature_entity_name, request, headers, runtime)
