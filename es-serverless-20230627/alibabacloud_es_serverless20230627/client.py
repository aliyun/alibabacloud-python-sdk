# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_es_serverless20230627 import models as es_serverless_20230627_models
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
        self._endpoint = self.get_endpoint('es-serverless', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_spec_review_task_with_options(
        self,
        app_name: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CancelSpecReviewTaskResponse:
        """
        @summary 撤销规格审批
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSpecReviewTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelSpecReviewTask',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/spec-review-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.CancelSpecReviewTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.CancelSpecReviewTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_spec_review_task_with_options_async(
        self,
        app_name: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CancelSpecReviewTaskResponse:
        """
        @summary 撤销规格审批
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSpecReviewTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelSpecReviewTask',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/spec-review-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.CancelSpecReviewTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.CancelSpecReviewTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_spec_review_task(
        self,
        app_name: str,
        task_id: str,
    ) -> es_serverless_20230627_models.CancelSpecReviewTaskResponse:
        """
        @summary 撤销规格审批
        
        @return: CancelSpecReviewTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_spec_review_task_with_options(app_name, task_id, headers, runtime)

    async def cancel_spec_review_task_async(
        self,
        app_name: str,
        task_id: str,
    ) -> es_serverless_20230627_models.CancelSpecReviewTaskResponse:
        """
        @summary 撤销规格审批
        
        @return: CancelSpecReviewTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_spec_review_task_with_options_async(app_name, task_id, headers, runtime)

    def create_app_with_options(
        self,
        request: es_serverless_20230627_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateAppResponse:
        """
        @summary 创建Serverless应用
        
        @param request: CreateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.private_network):
            body['privateNetwork'] = request.private_network
        if not UtilClient.is_unset(request.quota_info):
            body['quotaInfo'] = request.quota_info
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateAppResponse(),
                self.execute(params, req, runtime)
            )

    async def create_app_with_options_async(
        self,
        request: es_serverless_20230627_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateAppResponse:
        """
        @summary 创建Serverless应用
        
        @param request: CreateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.private_network):
            body['privateNetwork'] = request.private_network
        if not UtilClient.is_unset(request.quota_info):
            body['quotaInfo'] = request.quota_info
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_app(
        self,
        request: es_serverless_20230627_models.CreateAppRequest,
    ) -> es_serverless_20230627_models.CreateAppResponse:
        """
        @summary 创建Serverless应用
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_with_options(request, headers, runtime)

    async def create_app_async(
        self,
        request: es_serverless_20230627_models.CreateAppRequest,
    ) -> es_serverless_20230627_models.CreateAppResponse:
        """
        @summary 创建Serverless应用
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_with_options_async(request, headers, runtime)

    def create_endpoint_with_options(
        self,
        request: es_serverless_20230627_models.CreateEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateEndpointResponse:
        """
        @summary 创建端点
        
        @param request: CreateEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.endpoint_zones):
            body['endpointZones'] = request.endpoint_zones
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateEndpointResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateEndpointResponse(),
                self.execute(params, req, runtime)
            )

    async def create_endpoint_with_options_async(
        self,
        request: es_serverless_20230627_models.CreateEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateEndpointResponse:
        """
        @summary 创建端点
        
        @param request: CreateEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.endpoint_zones):
            body['endpointZones'] = request.endpoint_zones
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateEndpointResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateEndpointResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_endpoint(
        self,
        request: es_serverless_20230627_models.CreateEndpointRequest,
    ) -> es_serverless_20230627_models.CreateEndpointResponse:
        """
        @summary 创建端点
        
        @param request: CreateEndpointRequest
        @return: CreateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_endpoint_with_options(request, headers, runtime)

    async def create_endpoint_async(
        self,
        request: es_serverless_20230627_models.CreateEndpointRequest,
    ) -> es_serverless_20230627_models.CreateEndpointResponse:
        """
        @summary 创建端点
        
        @param request: CreateEndpointRequest
        @return: CreateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_endpoint_with_options_async(request, headers, runtime)

    def create_snapshot_with_options(
        self,
        app_name: str,
        repository: str,
        request: es_serverless_20230627_models.CreateSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateSnapshotResponse:
        """
        @summary 创建快照
        
        @param request: CreateSnapshotRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.indices):
            body['indices'] = request.indices
        if not UtilClient.is_unset(request.snapshot):
            body['snapshot'] = request.snapshot
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/snapshot-repositories/{OpenApiUtilClient.get_encode_param(repository)}/snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateSnapshotResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateSnapshotResponse(),
                self.execute(params, req, runtime)
            )

    async def create_snapshot_with_options_async(
        self,
        app_name: str,
        repository: str,
        request: es_serverless_20230627_models.CreateSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateSnapshotResponse:
        """
        @summary 创建快照
        
        @param request: CreateSnapshotRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.indices):
            body['indices'] = request.indices
        if not UtilClient.is_unset(request.snapshot):
            body['snapshot'] = request.snapshot
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/snapshot-repositories/{OpenApiUtilClient.get_encode_param(repository)}/snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateSnapshotResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.CreateSnapshotResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_snapshot(
        self,
        app_name: str,
        repository: str,
        request: es_serverless_20230627_models.CreateSnapshotRequest,
    ) -> es_serverless_20230627_models.CreateSnapshotResponse:
        """
        @summary 创建快照
        
        @param request: CreateSnapshotRequest
        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_snapshot_with_options(app_name, repository, request, headers, runtime)

    async def create_snapshot_async(
        self,
        app_name: str,
        repository: str,
        request: es_serverless_20230627_models.CreateSnapshotRequest,
    ) -> es_serverless_20230627_models.CreateSnapshotResponse:
        """
        @summary 创建快照
        
        @param request: CreateSnapshotRequest
        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_snapshot_with_options_async(app_name, repository, request, headers, runtime)

    def delete_app_with_options(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteAppResponse:
        """
        @summary 删除Serverless应用。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteAppResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_app_with_options_async(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteAppResponse:
        """
        @summary 删除Serverless应用。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_app(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.DeleteAppResponse:
        """
        @summary 删除Serverless应用。
        
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_with_options(app_name, headers, runtime)

    async def delete_app_async(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.DeleteAppResponse:
        """
        @summary 删除Serverless应用。
        
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_app_with_options_async(app_name, headers, runtime)

    def delete_dict_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.DeleteDictRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteDictResponse:
        """
        @summary 删除词典
        
        @param request: DeleteDictRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDictResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDict',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/dicts/actions/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteDictResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteDictResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_dict_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.DeleteDictRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteDictResponse:
        """
        @summary 删除词典
        
        @param request: DeleteDictRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDictResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDict',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/dicts/actions/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteDictResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteDictResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_dict(
        self,
        app_name: str,
        request: es_serverless_20230627_models.DeleteDictRequest,
    ) -> es_serverless_20230627_models.DeleteDictResponse:
        """
        @summary 删除词典
        
        @param request: DeleteDictRequest
        @return: DeleteDictResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dict_with_options(app_name, request, headers, runtime)

    async def delete_dict_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.DeleteDictRequest,
    ) -> es_serverless_20230627_models.DeleteDictResponse:
        """
        @summary 删除词典
        
        @param request: DeleteDictRequest
        @return: DeleteDictResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dict_with_options_async(app_name, request, headers, runtime)

    def delete_endpoint_with_options(
        self,
        endpoint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteEndpointResponse:
        """
        @summary 删除端点
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEndpointResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEndpoint',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteEndpointResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteEndpointResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_endpoint_with_options_async(
        self,
        endpoint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteEndpointResponse:
        """
        @summary 删除端点
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEndpointResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEndpoint',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteEndpointResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteEndpointResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_endpoint(
        self,
        endpoint_id: str,
    ) -> es_serverless_20230627_models.DeleteEndpointResponse:
        """
        @summary 删除端点
        
        @return: DeleteEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_endpoint_with_options(endpoint_id, headers, runtime)

    async def delete_endpoint_async(
        self,
        endpoint_id: str,
    ) -> es_serverless_20230627_models.DeleteEndpointResponse:
        """
        @summary 删除端点
        
        @return: DeleteEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_endpoint_with_options_async(endpoint_id, headers, runtime)

    def delete_snapshot_with_options(
        self,
        app_name: str,
        repository: str,
        snapshot: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteSnapshotResponse:
        """
        @summary 删除快照
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/snapshot-repositories/{OpenApiUtilClient.get_encode_param(repository)}/snapshots/{OpenApiUtilClient.get_encode_param(snapshot)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteSnapshotResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteSnapshotResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_snapshot_with_options_async(
        self,
        app_name: str,
        repository: str,
        snapshot: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteSnapshotResponse:
        """
        @summary 删除快照
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/snapshot-repositories/{OpenApiUtilClient.get_encode_param(repository)}/snapshots/{OpenApiUtilClient.get_encode_param(snapshot)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteSnapshotResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.DeleteSnapshotResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_snapshot(
        self,
        app_name: str,
        repository: str,
        snapshot: str,
    ) -> es_serverless_20230627_models.DeleteSnapshotResponse:
        """
        @summary 删除快照
        
        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_snapshot_with_options(app_name, repository, snapshot, headers, runtime)

    async def delete_snapshot_async(
        self,
        app_name: str,
        repository: str,
        snapshot: str,
    ) -> es_serverless_20230627_models.DeleteSnapshotResponse:
        """
        @summary 删除快照
        
        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_snapshot_with_options_async(app_name, repository, snapshot, headers, runtime)

    def get_app_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.GetAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetAppResponse:
        """
        @summary 获取Serverless应用详情
        
        @param request: GetAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detailed):
            query['detailed'] = request.detailed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetAppResponse(),
                self.execute(params, req, runtime)
            )

    async def get_app_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.GetAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetAppResponse:
        """
        @summary 获取Serverless应用详情
        
        @param request: GetAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detailed):
            query['detailed'] = request.detailed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_app(
        self,
        app_name: str,
        request: es_serverless_20230627_models.GetAppRequest,
    ) -> es_serverless_20230627_models.GetAppResponse:
        """
        @summary 获取Serverless应用详情
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_with_options(app_name, request, headers, runtime)

    async def get_app_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.GetAppRequest,
    ) -> es_serverless_20230627_models.GetAppResponse:
        """
        @summary 获取Serverless应用详情
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_app_with_options_async(app_name, request, headers, runtime)

    def get_app_quota_with_options(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetAppQuotaResponse:
        """
        @summary 获取Serverless应用配额详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppQuotaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppQuota',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetAppQuotaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetAppQuotaResponse(),
                self.execute(params, req, runtime)
            )

    async def get_app_quota_with_options_async(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetAppQuotaResponse:
        """
        @summary 获取Serverless应用配额详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppQuotaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppQuota',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetAppQuotaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetAppQuotaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_app_quota(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.GetAppQuotaResponse:
        """
        @summary 获取Serverless应用配额详情
        
        @return: GetAppQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_quota_with_options(app_name, headers, runtime)

    async def get_app_quota_async(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.GetAppQuotaResponse:
        """
        @summary 获取Serverless应用配额详情
        
        @return: GetAppQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_app_quota_with_options_async(app_name, headers, runtime)

    def get_monitor_data_with_options(
        self,
        request: es_serverless_20230627_models.GetMonitorDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetMonitorDataResponse:
        """
        @summary 获取监控数据
        
        @param request: GetMonitorDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonitorDataResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetMonitorData',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/emon/metrics/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetMonitorDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetMonitorDataResponse(),
                self.execute(params, req, runtime)
            )

    async def get_monitor_data_with_options_async(
        self,
        request: es_serverless_20230627_models.GetMonitorDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetMonitorDataResponse:
        """
        @summary 获取监控数据
        
        @param request: GetMonitorDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonitorDataResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetMonitorData',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/emon/metrics/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetMonitorDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetMonitorDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_monitor_data(
        self,
        request: es_serverless_20230627_models.GetMonitorDataRequest,
    ) -> es_serverless_20230627_models.GetMonitorDataResponse:
        """
        @summary 获取监控数据
        
        @param request: GetMonitorDataRequest
        @return: GetMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_monitor_data_with_options(request, headers, runtime)

    async def get_monitor_data_async(
        self,
        request: es_serverless_20230627_models.GetMonitorDataRequest,
    ) -> es_serverless_20230627_models.GetMonitorDataResponse:
        """
        @summary 获取监控数据
        
        @param request: GetMonitorDataRequest
        @return: GetMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_monitor_data_with_options_async(request, headers, runtime)

    def get_snapshot_setting_with_options(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetSnapshotSettingResponse:
        """
        @summary 获取自动备份配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSnapshotSettingResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSnapshotSetting',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/auto-snapshot-setting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetSnapshotSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetSnapshotSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def get_snapshot_setting_with_options_async(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetSnapshotSettingResponse:
        """
        @summary 获取自动备份配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSnapshotSettingResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSnapshotSetting',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/auto-snapshot-setting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetSnapshotSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetSnapshotSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_snapshot_setting(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.GetSnapshotSettingResponse:
        """
        @summary 获取自动备份配置
        
        @return: GetSnapshotSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_setting_with_options(app_name, headers, runtime)

    async def get_snapshot_setting_async(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.GetSnapshotSettingResponse:
        """
        @summary 获取自动备份配置
        
        @return: GetSnapshotSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_snapshot_setting_with_options_async(app_name, headers, runtime)

    def get_spec_review_task_with_options(
        self,
        app_name: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetSpecReviewTaskResponse:
        """
        @summary 获取配额审批详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSpecReviewTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSpecReviewTask',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/spec-review-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetSpecReviewTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetSpecReviewTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def get_spec_review_task_with_options_async(
        self,
        app_name: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetSpecReviewTaskResponse:
        """
        @summary 获取配额审批详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSpecReviewTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSpecReviewTask',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/spec-review-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.GetSpecReviewTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.GetSpecReviewTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_spec_review_task(
        self,
        app_name: str,
        task_id: str,
    ) -> es_serverless_20230627_models.GetSpecReviewTaskResponse:
        """
        @summary 获取配额审批详情
        
        @return: GetSpecReviewTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_spec_review_task_with_options(app_name, task_id, headers, runtime)

    async def get_spec_review_task_async(
        self,
        app_name: str,
        task_id: str,
    ) -> es_serverless_20230627_models.GetSpecReviewTaskResponse:
        """
        @summary 获取配额审批详情
        
        @return: GetSpecReviewTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_spec_review_task_with_options_async(app_name, task_id, headers, runtime)

    def list_apps_with_options(
        self,
        request: es_serverless_20230627_models.ListAppsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListAppsResponse:
        """
        @summary 查看Serverless应用列表
        
        @param request: ListAppsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['appName'] = request.app_name
        if not UtilClient.is_unset(request.create_time):
            query['createTime'] = request.create_time
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.order_type):
            query['orderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListAppsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListAppsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_apps_with_options_async(
        self,
        request: es_serverless_20230627_models.ListAppsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListAppsResponse:
        """
        @summary 查看Serverless应用列表
        
        @param request: ListAppsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['appName'] = request.app_name
        if not UtilClient.is_unset(request.create_time):
            query['createTime'] = request.create_time
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.order_type):
            query['orderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListAppsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListAppsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_apps(
        self,
        request: es_serverless_20230627_models.ListAppsRequest,
    ) -> es_serverless_20230627_models.ListAppsResponse:
        """
        @summary 查看Serverless应用列表
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apps_with_options(request, headers, runtime)

    async def list_apps_async(
        self,
        request: es_serverless_20230627_models.ListAppsRequest,
    ) -> es_serverless_20230627_models.ListAppsResponse:
        """
        @summary 查看Serverless应用列表
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_apps_with_options_async(request, headers, runtime)

    def list_dicts_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListDictsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListDictsResponse:
        """
        @summary 获取词典列表
        
        @param request: ListDictsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDictsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDicts',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/dicts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListDictsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListDictsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_dicts_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListDictsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListDictsResponse:
        """
        @summary 获取词典列表
        
        @param request: ListDictsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDictsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDicts',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/dicts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListDictsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListDictsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_dicts(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListDictsRequest,
    ) -> es_serverless_20230627_models.ListDictsResponse:
        """
        @summary 获取词典列表
        
        @param request: ListDictsRequest
        @return: ListDictsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dicts_with_options(app_name, request, headers, runtime)

    async def list_dicts_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListDictsRequest,
    ) -> es_serverless_20230627_models.ListDictsResponse:
        """
        @summary 获取词典列表
        
        @param request: ListDictsRequest
        @return: ListDictsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dicts_with_options_async(app_name, request, headers, runtime)

    def list_endpoints_with_options(
        self,
        request: es_serverless_20230627_models.ListEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListEndpointsResponse:
        """
        @summary 获取端点信息列表
        
        @param request: ListEndpointsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEndpoints',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListEndpointsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListEndpointsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_endpoints_with_options_async(
        self,
        request: es_serverless_20230627_models.ListEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListEndpointsResponse:
        """
        @summary 获取端点信息列表
        
        @param request: ListEndpointsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEndpoints',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListEndpointsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListEndpointsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_endpoints(
        self,
        request: es_serverless_20230627_models.ListEndpointsRequest,
    ) -> es_serverless_20230627_models.ListEndpointsResponse:
        """
        @summary 获取端点信息列表
        
        @param request: ListEndpointsRequest
        @return: ListEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_endpoints_with_options(request, headers, runtime)

    async def list_endpoints_async(
        self,
        request: es_serverless_20230627_models.ListEndpointsRequest,
    ) -> es_serverless_20230627_models.ListEndpointsResponse:
        """
        @summary 获取端点信息列表
        
        @param request: ListEndpointsRequest
        @return: ListEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_endpoints_with_options_async(request, headers, runtime)

    def list_indices_with_options(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListIndicesResponse:
        """
        @summary 查看索引列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndicesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIndices',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/indices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListIndicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListIndicesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_indices_with_options_async(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListIndicesResponse:
        """
        @summary 查看索引列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndicesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIndices',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/indices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListIndicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListIndicesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_indices(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.ListIndicesResponse:
        """
        @summary 查看索引列表
        
        @return: ListIndicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_indices_with_options(app_name, headers, runtime)

    async def list_indices_async(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.ListIndicesResponse:
        """
        @summary 查看索引列表
        
        @return: ListIndicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_indices_with_options_async(app_name, headers, runtime)

    def list_snapshot_repositories_with_options(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListSnapshotRepositoriesResponse:
        """
        @summary 获取快照仓库列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSnapshotRepositoriesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSnapshotRepositories',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/snapshot-repositories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSnapshotRepositoriesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSnapshotRepositoriesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_snapshot_repositories_with_options_async(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListSnapshotRepositoriesResponse:
        """
        @summary 获取快照仓库列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSnapshotRepositoriesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSnapshotRepositories',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/snapshot-repositories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSnapshotRepositoriesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSnapshotRepositoriesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_snapshot_repositories(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.ListSnapshotRepositoriesResponse:
        """
        @summary 获取快照仓库列表
        
        @return: ListSnapshotRepositoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_snapshot_repositories_with_options(app_name, headers, runtime)

    async def list_snapshot_repositories_async(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.ListSnapshotRepositoriesResponse:
        """
        @summary 获取快照仓库列表
        
        @return: ListSnapshotRepositoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_snapshot_repositories_with_options_async(app_name, headers, runtime)

    def list_snapshots_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListSnapshotsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListSnapshotsResponse:
        """
        @summary 获取仓库的快照列表
        
        @param request: ListSnapshotsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository):
            query['repository'] = request.repository
        if not UtilClient.is_unset(request.snapshot):
            query['snapshot'] = request.snapshot
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshots',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSnapshotsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSnapshotsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_snapshots_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListSnapshotsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListSnapshotsResponse:
        """
        @summary 获取仓库的快照列表
        
        @param request: ListSnapshotsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository):
            query['repository'] = request.repository
        if not UtilClient.is_unset(request.snapshot):
            query['snapshot'] = request.snapshot
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshots',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSnapshotsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSnapshotsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_snapshots(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListSnapshotsRequest,
    ) -> es_serverless_20230627_models.ListSnapshotsResponse:
        """
        @summary 获取仓库的快照列表
        
        @param request: ListSnapshotsRequest
        @return: ListSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_snapshots_with_options(app_name, request, headers, runtime)

    async def list_snapshots_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListSnapshotsRequest,
    ) -> es_serverless_20230627_models.ListSnapshotsResponse:
        """
        @summary 获取仓库的快照列表
        
        @param request: ListSnapshotsRequest
        @return: ListSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_snapshots_with_options_async(app_name, request, headers, runtime)

    def list_spec_review_tasks_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListSpecReviewTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListSpecReviewTasksResponse:
        """
        @summary 获取规格审批列表
        
        @param request: ListSpecReviewTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSpecReviewTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSpecReviewTasks',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/spec-review-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSpecReviewTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSpecReviewTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def list_spec_review_tasks_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListSpecReviewTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListSpecReviewTasksResponse:
        """
        @summary 获取规格审批列表
        
        @param request: ListSpecReviewTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSpecReviewTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSpecReviewTasks',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/spec-review-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSpecReviewTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.ListSpecReviewTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_spec_review_tasks(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListSpecReviewTasksRequest,
    ) -> es_serverless_20230627_models.ListSpecReviewTasksResponse:
        """
        @summary 获取规格审批列表
        
        @param request: ListSpecReviewTasksRequest
        @return: ListSpecReviewTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_spec_review_tasks_with_options(app_name, request, headers, runtime)

    async def list_spec_review_tasks_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.ListSpecReviewTasksRequest,
    ) -> es_serverless_20230627_models.ListSpecReviewTasksResponse:
        """
        @summary 获取规格审批列表
        
        @param request: ListSpecReviewTasksRequest
        @return: ListSpecReviewTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_spec_review_tasks_with_options_async(app_name, request, headers, runtime)

    def update_app_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateAppResponse:
        """
        @summary 编辑Serverless应用
        
        @param request: UpdateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_reason):
            body['applyReason'] = request.apply_reason
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.limiter_info):
            body['limiterInfo'] = request.limiter_info
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.private_network):
            body['privateNetwork'] = request.private_network
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateAppResponse(),
                self.execute(params, req, runtime)
            )

    async def update_app_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateAppResponse:
        """
        @summary 编辑Serverless应用
        
        @param request: UpdateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_reason):
            body['applyReason'] = request.apply_reason
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.limiter_info):
            body['limiterInfo'] = request.limiter_info
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.private_network):
            body['privateNetwork'] = request.private_network
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_app(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateAppRequest,
    ) -> es_serverless_20230627_models.UpdateAppResponse:
        """
        @summary 编辑Serverless应用
        
        @param request: UpdateAppRequest
        @return: UpdateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_with_options(app_name, request, headers, runtime)

    async def update_app_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateAppRequest,
    ) -> es_serverless_20230627_models.UpdateAppResponse:
        """
        @summary 编辑Serverless应用
        
        @param request: UpdateAppRequest
        @return: UpdateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_app_with_options_async(app_name, request, headers, runtime)

    def update_dict_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateDictRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateDictResponse:
        """
        @summary 创建或更新词典
        
        @param request: UpdateDictRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDictResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_cover):
            query['allowCover'] = request.allow_cover
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDict',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/dicts',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateDictResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateDictResponse(),
                self.execute(params, req, runtime)
            )

    async def update_dict_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateDictRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateDictResponse:
        """
        @summary 创建或更新词典
        
        @param request: UpdateDictRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDictResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_cover):
            query['allowCover'] = request.allow_cover
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDict',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/dicts',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateDictResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateDictResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_dict(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateDictRequest,
    ) -> es_serverless_20230627_models.UpdateDictResponse:
        """
        @summary 创建或更新词典
        
        @param request: UpdateDictRequest
        @return: UpdateDictResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dict_with_options(app_name, request, headers, runtime)

    async def update_dict_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateDictRequest,
    ) -> es_serverless_20230627_models.UpdateDictResponse:
        """
        @summary 创建或更新词典
        
        @param request: UpdateDictRequest
        @return: UpdateDictResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_dict_with_options_async(app_name, request, headers, runtime)

    def update_endpoint_with_options(
        self,
        endpoint_id: str,
        request: es_serverless_20230627_models.UpdateEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateEndpointResponse:
        """
        @summary 修改端点信息
        
        @param request: UpdateEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEndpointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.endpoint_zones):
            body['endpointZones'] = request.endpoint_zones
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEndpoint',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateEndpointResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateEndpointResponse(),
                self.execute(params, req, runtime)
            )

    async def update_endpoint_with_options_async(
        self,
        endpoint_id: str,
        request: es_serverless_20230627_models.UpdateEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateEndpointResponse:
        """
        @summary 修改端点信息
        
        @param request: UpdateEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEndpointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.endpoint_zones):
            body['endpointZones'] = request.endpoint_zones
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEndpoint',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateEndpointResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateEndpointResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_endpoint(
        self,
        endpoint_id: str,
        request: es_serverless_20230627_models.UpdateEndpointRequest,
    ) -> es_serverless_20230627_models.UpdateEndpointResponse:
        """
        @summary 修改端点信息
        
        @param request: UpdateEndpointRequest
        @return: UpdateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_endpoint_with_options(endpoint_id, request, headers, runtime)

    async def update_endpoint_async(
        self,
        endpoint_id: str,
        request: es_serverless_20230627_models.UpdateEndpointRequest,
    ) -> es_serverless_20230627_models.UpdateEndpointResponse:
        """
        @summary 修改端点信息
        
        @param request: UpdateEndpointRequest
        @return: UpdateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_endpoint_with_options_async(endpoint_id, request, headers, runtime)

    def update_snapshot_setting_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateSnapshotSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateSnapshotSettingResponse:
        """
        @summary 修改自动备份配置
        
        @param request: UpdateSnapshotSettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSnapshotSettingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.quartz_regex):
            body['quartzRegex'] = request.quartz_regex
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSnapshotSetting',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/auto-snapshot-setting',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateSnapshotSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateSnapshotSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def update_snapshot_setting_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateSnapshotSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateSnapshotSettingResponse:
        """
        @summary 修改自动备份配置
        
        @param request: UpdateSnapshotSettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSnapshotSettingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.quartz_regex):
            body['quartzRegex'] = request.quartz_regex
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSnapshotSetting',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/auto-snapshot-setting',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateSnapshotSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                es_serverless_20230627_models.UpdateSnapshotSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_snapshot_setting(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateSnapshotSettingRequest,
    ) -> es_serverless_20230627_models.UpdateSnapshotSettingResponse:
        """
        @summary 修改自动备份配置
        
        @param request: UpdateSnapshotSettingRequest
        @return: UpdateSnapshotSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_setting_with_options(app_name, request, headers, runtime)

    async def update_snapshot_setting_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateSnapshotSettingRequest,
    ) -> es_serverless_20230627_models.UpdateSnapshotSettingResponse:
        """
        @summary 修改自动备份配置
        
        @param request: UpdateSnapshotSettingRequest
        @return: UpdateSnapshotSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_snapshot_setting_with_options_async(app_name, request, headers, runtime)
