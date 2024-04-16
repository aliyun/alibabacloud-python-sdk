# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_miniapplcdp20200113 import models as miniapplcdp_20200113_models
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
        self._endpoint = self.get_endpoint('miniapplcdp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_create_model_with_options(
        self,
        request: miniapplcdp_20200113_models.BatchCreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.BatchCreateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_data_json):
            query['ModelDataJson'] = request.model_data_json
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchCreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.BatchCreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.BatchCreateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_data_json):
            query['ModelDataJson'] = request.model_data_json
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchCreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_model(
        self,
        request: miniapplcdp_20200113_models.BatchCreateModelRequest,
    ) -> miniapplcdp_20200113_models.BatchCreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_create_model_with_options(request, runtime)

    async def batch_create_model_async(
        self,
        request: miniapplcdp_20200113_models.BatchCreateModelRequest,
    ) -> miniapplcdp_20200113_models.BatchCreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_model_with_options_async(request, runtime)

    def batch_delete_model_with_options(
        self,
        request: miniapplcdp_20200113_models.BatchDeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.BatchDeleteModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id_list):
            query['ModelIdList'] = request.model_id_list
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchDeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.BatchDeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.BatchDeleteModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id_list):
            query['ModelIdList'] = request.model_id_list
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchDeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_model(
        self,
        request: miniapplcdp_20200113_models.BatchDeleteModelRequest,
    ) -> miniapplcdp_20200113_models.BatchDeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_model_with_options(request, runtime)

    async def batch_delete_model_async(
        self,
        request: miniapplcdp_20200113_models.BatchDeleteModelRequest,
    ) -> miniapplcdp_20200113_models.BatchDeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_model_with_options_async(request, runtime)

    def batch_delete_resources_with_options(
        self,
        request: miniapplcdp_20200113_models.BatchDeleteResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.BatchDeleteResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id_list):
            query['ResourceIdList'] = request.resource_id_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchDeleteResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_resources_with_options_async(
        self,
        request: miniapplcdp_20200113_models.BatchDeleteResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.BatchDeleteResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id_list):
            query['ResourceIdList'] = request.resource_id_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchDeleteResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_resources(
        self,
        request: miniapplcdp_20200113_models.BatchDeleteResourcesRequest,
    ) -> miniapplcdp_20200113_models.BatchDeleteResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_resources_with_options(request, runtime)

    async def batch_delete_resources_async(
        self,
        request: miniapplcdp_20200113_models.BatchDeleteResourcesRequest,
    ) -> miniapplcdp_20200113_models.BatchDeleteResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_resources_with_options_async(request, runtime)

    def batch_restore_model_with_options(
        self,
        request: miniapplcdp_20200113_models.BatchRestoreModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.BatchRestoreModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id_list):
            query['ModelIdList'] = request.model_id_list
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchRestoreModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchRestoreModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_restore_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.BatchRestoreModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.BatchRestoreModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id_list):
            query['ModelIdList'] = request.model_id_list
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchRestoreModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.BatchRestoreModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_restore_model(
        self,
        request: miniapplcdp_20200113_models.BatchRestoreModelRequest,
    ) -> miniapplcdp_20200113_models.BatchRestoreModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_restore_model_with_options(request, runtime)

    async def batch_restore_model_async(
        self,
        request: miniapplcdp_20200113_models.BatchRestoreModelRequest,
    ) -> miniapplcdp_20200113_models.BatchRestoreModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_restore_model_with_options_async(request, runtime)

    def check_domain_with_options(
        self,
        request: miniapplcdp_20200113_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CheckDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CheckDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CheckDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain(
        self,
        request: miniapplcdp_20200113_models.CheckDomainRequest,
    ) -> miniapplcdp_20200113_models.CheckDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: miniapplcdp_20200113_models.CheckDomainRequest,
    ) -> miniapplcdp_20200113_models.CheckDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def clone_app_with_options(
        self,
        request: miniapplcdp_20200113_models.CloneAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CloneAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_app_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CloneAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CloneAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_app(
        self,
        request: miniapplcdp_20200113_models.CloneAppRequest,
    ) -> miniapplcdp_20200113_models.CloneAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_app_with_options(request, runtime)

    async def clone_app_async(
        self,
        request: miniapplcdp_20200113_models.CloneAppRequest,
    ) -> miniapplcdp_20200113_models.CloneAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_app_with_options_async(request, runtime)

    def clone_model_from_commit_with_options(
        self,
        request: miniapplcdp_20200113_models.CloneModelFromCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CloneModelFromCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_commit_id):
            query['SourceCommitId'] = request.source_commit_id
        if not UtilClient.is_unset(request.source_module_id):
            query['SourceModuleId'] = request.source_module_id
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.target_module_id):
            query['TargetModuleId'] = request.target_module_id
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_sub_type):
            query['TargetSubType'] = request.target_sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneModelFromCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneModelFromCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_model_from_commit_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CloneModelFromCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CloneModelFromCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_commit_id):
            query['SourceCommitId'] = request.source_commit_id
        if not UtilClient.is_unset(request.source_module_id):
            query['SourceModuleId'] = request.source_module_id
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.target_module_id):
            query['TargetModuleId'] = request.target_module_id
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_sub_type):
            query['TargetSubType'] = request.target_sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneModelFromCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneModelFromCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_model_from_commit(
        self,
        request: miniapplcdp_20200113_models.CloneModelFromCommitRequest,
    ) -> miniapplcdp_20200113_models.CloneModelFromCommitResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_model_from_commit_with_options(request, runtime)

    async def clone_model_from_commit_async(
        self,
        request: miniapplcdp_20200113_models.CloneModelFromCommitRequest,
    ) -> miniapplcdp_20200113_models.CloneModelFromCommitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_model_from_commit_with_options_async(request, runtime)

    def clone_model_in_module_with_options(
        self,
        request: miniapplcdp_20200113_models.CloneModelInModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CloneModelInModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_sub_type):
            query['TargetSubType'] = request.target_sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneModelInModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneModelInModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_model_in_module_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CloneModelInModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CloneModelInModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_sub_type):
            query['TargetSubType'] = request.target_sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneModelInModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CloneModelInModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_model_in_module(
        self,
        request: miniapplcdp_20200113_models.CloneModelInModuleRequest,
    ) -> miniapplcdp_20200113_models.CloneModelInModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_model_in_module_with_options(request, runtime)

    async def clone_model_in_module_async(
        self,
        request: miniapplcdp_20200113_models.CloneModelInModuleRequest,
    ) -> miniapplcdp_20200113_models.CloneModelInModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_model_in_module_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: miniapplcdp_20200113_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.asynchronous):
            query['Asynchronous'] = request.asynchronous
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.platform_version):
            query['PlatformVersion'] = request.platform_version
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_commit_id):
            query['SourceCommitId'] = request.source_commit_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.templated):
            query['Templated'] = request.templated
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.asynchronous):
            query['Asynchronous'] = request.asynchronous
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.platform_version):
            query['PlatformVersion'] = request.platform_version
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_commit_id):
            query['SourceCommitId'] = request.source_commit_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.templated):
            query['Templated'] = request.templated
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: miniapplcdp_20200113_models.CreateAppRequest,
    ) -> miniapplcdp_20200113_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: miniapplcdp_20200113_models.CreateAppRequest,
    ) -> miniapplcdp_20200113_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_commit_with_options(
        self,
        request: miniapplcdp_20200113_models.CreateCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commit_log):
            query['CommitLog'] = request.commit_log
        if not UtilClient.is_unset(request.commit_type):
            query['CommitType'] = request.commit_type
        if not UtilClient.is_unset(request.main_module_commit_id):
            query['MainModuleCommitId'] = request.main_module_commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.rollback_to_commit_id):
            query['RollbackToCommitId'] = request.rollback_to_commit_id
        if not UtilClient.is_unset(request.rollback_type):
            query['RollbackType'] = request.rollback_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_commit_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreateCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commit_log):
            query['CommitLog'] = request.commit_log
        if not UtilClient.is_unset(request.commit_type):
            query['CommitType'] = request.commit_type
        if not UtilClient.is_unset(request.main_module_commit_id):
            query['MainModuleCommitId'] = request.main_module_commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.rollback_to_commit_id):
            query['RollbackToCommitId'] = request.rollback_to_commit_id
        if not UtilClient.is_unset(request.rollback_type):
            query['RollbackType'] = request.rollback_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_commit(
        self,
        request: miniapplcdp_20200113_models.CreateCommitRequest,
    ) -> miniapplcdp_20200113_models.CreateCommitResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_commit_with_options(request, runtime)

    async def create_commit_async(
        self,
        request: miniapplcdp_20200113_models.CreateCommitRequest,
    ) -> miniapplcdp_20200113_models.CreateCommitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_commit_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: miniapplcdp_20200113_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_certificate):
            query['WithCertificate'] = request.with_certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_certificate):
            query['WithCertificate'] = request.with_certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: miniapplcdp_20200113_models.CreateDomainRequest,
    ) -> miniapplcdp_20200113_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: miniapplcdp_20200113_models.CreateDomainRequest,
    ) -> miniapplcdp_20200113_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_link_entity_and_association_with_options(
        self,
        request: miniapplcdp_20200113_models.CreateLinkEntityAndAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateLinkEntityAndAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.model_data):
            query['ModelData'] = request.model_data
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLinkEntityAndAssociation',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateLinkEntityAndAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_link_entity_and_association_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreateLinkEntityAndAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateLinkEntityAndAssociationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.model_data):
            query['ModelData'] = request.model_data
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLinkEntityAndAssociation',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateLinkEntityAndAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_link_entity_and_association(
        self,
        request: miniapplcdp_20200113_models.CreateLinkEntityAndAssociationRequest,
    ) -> miniapplcdp_20200113_models.CreateLinkEntityAndAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_link_entity_and_association_with_options(request, runtime)

    async def create_link_entity_and_association_async(
        self,
        request: miniapplcdp_20200113_models.CreateLinkEntityAndAssociationRequest,
    ) -> miniapplcdp_20200113_models.CreateLinkEntityAndAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_link_entity_and_association_with_options_async(request, runtime)

    def create_model_with_options(
        self,
        request: miniapplcdp_20200113_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.link_model_id):
            query['LinkModelId'] = request.link_model_id
        if not UtilClient.is_unset(request.link_module_id):
            query['LinkModuleId'] = request.link_module_id
        if not UtilClient.is_unset(request.linked):
            query['Linked'] = request.linked
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.link_model_id):
            query['LinkModelId'] = request.link_model_id
        if not UtilClient.is_unset(request.link_module_id):
            query['LinkModuleId'] = request.link_module_id
        if not UtilClient.is_unset(request.linked):
            query['Linked'] = request.linked
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        request: miniapplcdp_20200113_models.CreateModelRequest,
    ) -> miniapplcdp_20200113_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    async def create_model_async(
        self,
        request: miniapplcdp_20200113_models.CreateModelRequest,
    ) -> miniapplcdp_20200113_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_model_with_options_async(request, runtime)

    def create_module_with_options(
        self,
        request: miniapplcdp_20200113_models.CreateModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.minimum_platform_version):
            query['MinimumPlatformVersion'] = request.minimum_platform_version
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_module_id):
            query['SourceModuleId'] = request.source_module_id
        if not UtilClient.is_unset(request.target_app_source):
            query['TargetAppSource'] = request.target_app_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreateModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.minimum_platform_version):
            query['MinimumPlatformVersion'] = request.minimum_platform_version
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_module_id):
            query['SourceModuleId'] = request.source_module_id
        if not UtilClient.is_unset(request.target_app_source):
            query['TargetAppSource'] = request.target_app_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module(
        self,
        request: miniapplcdp_20200113_models.CreateModuleRequest,
    ) -> miniapplcdp_20200113_models.CreateModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_module_with_options(request, runtime)

    async def create_module_async(
        self,
        request: miniapplcdp_20200113_models.CreateModuleRequest,
    ) -> miniapplcdp_20200113_models.CreateModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_module_with_options_async(request, runtime)

    def create_module_publish_with_options(
        self,
        request: miniapplcdp_20200113_models.CreateModulePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateModulePublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.publish_version):
            query['PublishVersion'] = request.publish_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModulePublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModulePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_publish_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreateModulePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateModulePublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.publish_version):
            query['PublishVersion'] = request.publish_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModulePublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateModulePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module_publish(
        self,
        request: miniapplcdp_20200113_models.CreateModulePublishRequest,
    ) -> miniapplcdp_20200113_models.CreateModulePublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_module_publish_with_options(request, runtime)

    async def create_module_publish_async(
        self,
        request: miniapplcdp_20200113_models.CreateModulePublishRequest,
    ) -> miniapplcdp_20200113_models.CreateModulePublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_module_publish_with_options_async(request, runtime)

    def create_publish_with_options(
        self,
        request: miniapplcdp_20200113_models.CreatePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreatePublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.publish_type):
            query['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreatePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_publish_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreatePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreatePublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.publish_type):
            query['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreatePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_publish(
        self,
        request: miniapplcdp_20200113_models.CreatePublishRequest,
    ) -> miniapplcdp_20200113_models.CreatePublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_publish_with_options(request, runtime)

    async def create_publish_async(
        self,
        request: miniapplcdp_20200113_models.CreatePublishRequest,
    ) -> miniapplcdp_20200113_models.CreatePublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_publish_with_options_async(request, runtime)

    def create_resource_with_options(
        self,
        request: miniapplcdp_20200113_models.CreateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request: miniapplcdp_20200113_models.CreateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.CreateResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: miniapplcdp_20200113_models.CreateResourceRequest,
    ) -> miniapplcdp_20200113_models.CreateResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_with_options(request, runtime)

    async def create_resource_async(
        self,
        request: miniapplcdp_20200113_models.CreateResourceRequest,
    ) -> miniapplcdp_20200113_models.CreateResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: miniapplcdp_20200113_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: miniapplcdp_20200113_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: miniapplcdp_20200113_models.DeleteAppRequest,
    ) -> miniapplcdp_20200113_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: miniapplcdp_20200113_models.DeleteAppRequest,
    ) -> miniapplcdp_20200113_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_commit_with_options(
        self,
        request: miniapplcdp_20200113_models.DeleteCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_commit_with_options_async(
        self,
        request: miniapplcdp_20200113_models.DeleteCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_commit(
        self,
        request: miniapplcdp_20200113_models.DeleteCommitRequest,
    ) -> miniapplcdp_20200113_models.DeleteCommitResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_commit_with_options(request, runtime)

    async def delete_commit_async(
        self,
        request: miniapplcdp_20200113_models.DeleteCommitRequest,
    ) -> miniapplcdp_20200113_models.DeleteCommitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_commit_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: miniapplcdp_20200113_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: miniapplcdp_20200113_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: miniapplcdp_20200113_models.DeleteDomainRequest,
    ) -> miniapplcdp_20200113_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: miniapplcdp_20200113_models.DeleteDomainRequest,
    ) -> miniapplcdp_20200113_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_model_with_options(
        self,
        request: miniapplcdp_20200113_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        request: miniapplcdp_20200113_models.DeleteModelRequest,
    ) -> miniapplcdp_20200113_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    async def delete_model_async(
        self,
        request: miniapplcdp_20200113_models.DeleteModelRequest,
    ) -> miniapplcdp_20200113_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_model_with_options_async(request, runtime)

    def delete_module_with_options(
        self,
        request: miniapplcdp_20200113_models.DeleteModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_module_with_options_async(
        self,
        request: miniapplcdp_20200113_models.DeleteModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_module(
        self,
        request: miniapplcdp_20200113_models.DeleteModuleRequest,
    ) -> miniapplcdp_20200113_models.DeleteModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_module_with_options(request, runtime)

    async def delete_module_async(
        self,
        request: miniapplcdp_20200113_models.DeleteModuleRequest,
    ) -> miniapplcdp_20200113_models.DeleteModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_module_with_options_async(request, runtime)

    def delete_resource_with_options(
        self,
        request: miniapplcdp_20200113_models.DeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        request: miniapplcdp_20200113_models.DeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.DeleteResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        request: miniapplcdp_20200113_models.DeleteResourceRequest,
    ) -> miniapplcdp_20200113_models.DeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_with_options(request, runtime)

    async def delete_resource_async(
        self,
        request: miniapplcdp_20200113_models.DeleteResourceRequest,
    ) -> miniapplcdp_20200113_models.DeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_with_options_async(request, runtime)

    def generate_app_user_password_with_options(
        self,
        request: miniapplcdp_20200113_models.GenerateAppUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GenerateAppUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAppUserPassword',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateAppUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_app_user_password_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GenerateAppUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GenerateAppUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAppUserPassword',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateAppUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_app_user_password(
        self,
        request: miniapplcdp_20200113_models.GenerateAppUserPasswordRequest,
    ) -> miniapplcdp_20200113_models.GenerateAppUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_app_user_password_with_options(request, runtime)

    async def generate_app_user_password_async(
        self,
        request: miniapplcdp_20200113_models.GenerateAppUserPasswordRequest,
    ) -> miniapplcdp_20200113_models.GenerateAppUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_app_user_password_with_options_async(request, runtime)

    def generate_auth_token_with_options(
        self,
        request: miniapplcdp_20200113_models.GenerateAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GenerateAuthTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAuthToken',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_auth_token_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GenerateAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GenerateAuthTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAuthToken',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_auth_token(
        self,
        request: miniapplcdp_20200113_models.GenerateAuthTokenRequest,
    ) -> miniapplcdp_20200113_models.GenerateAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_auth_token_with_options(request, runtime)

    async def generate_auth_token_async(
        self,
        request: miniapplcdp_20200113_models.GenerateAuthTokenRequest,
    ) -> miniapplcdp_20200113_models.GenerateAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_auth_token_with_options_async(request, runtime)

    def generate_upload_token_with_options(
        self,
        request: miniapplcdp_20200113_models.GenerateUploadTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GenerateUploadTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.upload_token_type):
            query['UploadTokenType'] = request.upload_token_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadToken',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_token_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GenerateUploadTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GenerateUploadTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.upload_token_type):
            query['UploadTokenType'] = request.upload_token_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadToken',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GenerateUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_token(
        self,
        request: miniapplcdp_20200113_models.GenerateUploadTokenRequest,
    ) -> miniapplcdp_20200113_models.GenerateUploadTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_token_with_options(request, runtime)

    async def generate_upload_token_async(
        self,
        request: miniapplcdp_20200113_models.GenerateUploadTokenRequest,
    ) -> miniapplcdp_20200113_models.GenerateUploadTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_token_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: miniapplcdp_20200113_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        request: miniapplcdp_20200113_models.GetAppRequest,
    ) -> miniapplcdp_20200113_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: miniapplcdp_20200113_models.GetAppRequest,
    ) -> miniapplcdp_20200113_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_app_model_with_options(
        self,
        request: miniapplcdp_20200113_models.GetAppModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetAppModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetAppModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetAppModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_model(
        self,
        request: miniapplcdp_20200113_models.GetAppModelRequest,
    ) -> miniapplcdp_20200113_models.GetAppModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_model_with_options(request, runtime)

    async def get_app_model_async(
        self,
        request: miniapplcdp_20200113_models.GetAppModelRequest,
    ) -> miniapplcdp_20200113_models.GetAppModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_model_with_options_async(request, runtime)

    def get_app_secret_with_options(
        self,
        request: miniapplcdp_20200113_models.GetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetAppSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSecret',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_secret_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetAppSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSecret',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_secret(
        self,
        request: miniapplcdp_20200113_models.GetAppSecretRequest,
    ) -> miniapplcdp_20200113_models.GetAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    async def get_app_secret_async(
        self,
        request: miniapplcdp_20200113_models.GetAppSecretRequest,
    ) -> miniapplcdp_20200113_models.GetAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_secret_with_options_async(request, runtime)

    def get_artifact_with_options(
        self,
        request: miniapplcdp_20200113_models.GetArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetArtifactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifact',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetArtifactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifact',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact(
        self,
        request: miniapplcdp_20200113_models.GetArtifactRequest,
    ) -> miniapplcdp_20200113_models.GetArtifactResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_with_options(request, runtime)

    async def get_artifact_async(
        self,
        request: miniapplcdp_20200113_models.GetArtifactRequest,
    ) -> miniapplcdp_20200113_models.GetArtifactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_artifact_with_options_async(request, runtime)

    def get_commit_with_options(
        self,
        request: miniapplcdp_20200113_models.GetCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_commit_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_commit(
        self,
        request: miniapplcdp_20200113_models.GetCommitRequest,
    ) -> miniapplcdp_20200113_models.GetCommitResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_commit_with_options(request, runtime)

    async def get_commit_async(
        self,
        request: miniapplcdp_20200113_models.GetCommitRequest,
    ) -> miniapplcdp_20200113_models.GetCommitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_commit_with_options_async(request, runtime)

    def get_default_app_user_with_options(
        self,
        request: miniapplcdp_20200113_models.GetDefaultAppUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetDefaultAppUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDefaultAppUser',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDefaultAppUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_app_user_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetDefaultAppUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetDefaultAppUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDefaultAppUser',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDefaultAppUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_app_user(
        self,
        request: miniapplcdp_20200113_models.GetDefaultAppUserRequest,
    ) -> miniapplcdp_20200113_models.GetDefaultAppUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_app_user_with_options(request, runtime)

    async def get_default_app_user_async(
        self,
        request: miniapplcdp_20200113_models.GetDefaultAppUserRequest,
    ) -> miniapplcdp_20200113_models.GetDefaultAppUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_app_user_with_options_async(request, runtime)

    def get_domain_cname_with_options(
        self,
        request: miniapplcdp_20200113_models.GetDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetDomainCnameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainCname',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_cname_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetDomainCnameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainCname',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDomainCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_cname(
        self,
        request: miniapplcdp_20200113_models.GetDomainCnameRequest,
    ) -> miniapplcdp_20200113_models.GetDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_cname_with_options(request, runtime)

    async def get_domain_cname_async(
        self,
        request: miniapplcdp_20200113_models.GetDomainCnameRequest,
    ) -> miniapplcdp_20200113_models.GetDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_cname_with_options_async(request, runtime)

    def get_domain_overview_with_options(
        self,
        request: miniapplcdp_20200113_models.GetDomainOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetDomainOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainOverview',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDomainOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_overview_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetDomainOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetDomainOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainOverview',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetDomainOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_overview(
        self,
        request: miniapplcdp_20200113_models.GetDomainOverviewRequest,
    ) -> miniapplcdp_20200113_models.GetDomainOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_overview_with_options(request, runtime)

    async def get_domain_overview_async(
        self,
        request: miniapplcdp_20200113_models.GetDomainOverviewRequest,
    ) -> miniapplcdp_20200113_models.GetDomainOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_overview_with_options_async(request, runtime)

    def get_environment_with_options(
        self,
        request: miniapplcdp_20200113_models.GetEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment(
        self,
        request: miniapplcdp_20200113_models.GetEnvironmentRequest,
    ) -> miniapplcdp_20200113_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_environment_with_options(request, runtime)

    async def get_environment_async(
        self,
        request: miniapplcdp_20200113_models.GetEnvironmentRequest,
    ) -> miniapplcdp_20200113_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_environment_with_options_async(request, runtime)

    def get_history_stats_with_options(
        self,
        request: miniapplcdp_20200113_models.GetHistoryStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetHistoryStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryStats',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetHistoryStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_history_stats_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetHistoryStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetHistoryStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryStats',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetHistoryStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_history_stats(
        self,
        request: miniapplcdp_20200113_models.GetHistoryStatsRequest,
    ) -> miniapplcdp_20200113_models.GetHistoryStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_history_stats_with_options(request, runtime)

    async def get_history_stats_async(
        self,
        request: miniapplcdp_20200113_models.GetHistoryStatsRequest,
    ) -> miniapplcdp_20200113_models.GetHistoryStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_history_stats_with_options_async(request, runtime)

    def get_latest_commit_with_options(
        self,
        request: miniapplcdp_20200113_models.GetLatestCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetLatestCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLatestCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetLatestCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_latest_commit_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetLatestCommitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetLatestCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLatestCommit',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetLatestCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_latest_commit(
        self,
        request: miniapplcdp_20200113_models.GetLatestCommitRequest,
    ) -> miniapplcdp_20200113_models.GetLatestCommitResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_latest_commit_with_options(request, runtime)

    async def get_latest_commit_async(
        self,
        request: miniapplcdp_20200113_models.GetLatestCommitRequest,
    ) -> miniapplcdp_20200113_models.GetLatestCommitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_latest_commit_with_options_async(request, runtime)

    def get_model_with_options(
        self,
        request: miniapplcdp_20200113_models.GetModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model(
        self,
        request: miniapplcdp_20200113_models.GetModelRequest,
    ) -> miniapplcdp_20200113_models.GetModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_model_with_options(request, runtime)

    async def get_model_async(
        self,
        request: miniapplcdp_20200113_models.GetModelRequest,
    ) -> miniapplcdp_20200113_models.GetModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_model_with_options_async(request, runtime)

    def get_module_with_options(
        self,
        request: miniapplcdp_20200113_models.GetModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_module_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_module(
        self,
        request: miniapplcdp_20200113_models.GetModuleRequest,
    ) -> miniapplcdp_20200113_models.GetModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_module_with_options(request, runtime)

    async def get_module_async(
        self,
        request: miniapplcdp_20200113_models.GetModuleRequest,
    ) -> miniapplcdp_20200113_models.GetModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_module_with_options_async(request, runtime)

    def get_publish_with_options(
        self,
        request: miniapplcdp_20200113_models.GetPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetPublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.publish_id):
            query['PublishId'] = request.publish_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetPublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_publish_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetPublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.publish_id):
            query['PublishId'] = request.publish_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublish',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetPublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_publish(
        self,
        request: miniapplcdp_20200113_models.GetPublishRequest,
    ) -> miniapplcdp_20200113_models.GetPublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_publish_with_options(request, runtime)

    async def get_publish_async(
        self,
        request: miniapplcdp_20200113_models.GetPublishRequest,
    ) -> miniapplcdp_20200113_models.GetPublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_publish_with_options_async(request, runtime)

    def get_realtime_stats_with_options(
        self,
        request: miniapplcdp_20200113_models.GetRealtimeStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetRealtimeStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeStats',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetRealtimeStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_stats_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetRealtimeStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetRealtimeStatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeStats',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetRealtimeStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_stats(
        self,
        request: miniapplcdp_20200113_models.GetRealtimeStatsRequest,
    ) -> miniapplcdp_20200113_models.GetRealtimeStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_stats_with_options(request, runtime)

    async def get_realtime_stats_async(
        self,
        request: miniapplcdp_20200113_models.GetRealtimeStatsRequest,
    ) -> miniapplcdp_20200113_models.GetRealtimeStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_stats_with_options_async(request, runtime)

    def get_resource_with_options(
        self,
        request: miniapplcdp_20200113_models.GetResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(
        self,
        request: miniapplcdp_20200113_models.GetResourceRequest,
    ) -> miniapplcdp_20200113_models.GetResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_with_options(request, runtime)

    async def get_resource_async(
        self,
        request: miniapplcdp_20200113_models.GetResourceRequest,
    ) -> miniapplcdp_20200113_models.GetResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: miniapplcdp_20200113_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: miniapplcdp_20200113_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: miniapplcdp_20200113_models.GetUserRequest,
    ) -> miniapplcdp_20200113_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: miniapplcdp_20200113_models.GetUserRequest,
    ) -> miniapplcdp_20200113_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def list_app_modules_with_options(
        self,
        request: miniapplcdp_20200113_models.ListAppModulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListAppModulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppModulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_modules_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListAppModulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListAppModulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppModulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_modules(
        self,
        request: miniapplcdp_20200113_models.ListAppModulesRequest,
    ) -> miniapplcdp_20200113_models.ListAppModulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_modules_with_options(request, runtime)

    async def list_app_modules_async(
        self,
        request: miniapplcdp_20200113_models.ListAppModulesRequest,
    ) -> miniapplcdp_20200113_models.ListAppModulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_modules_with_options_async(request, runtime)

    def list_app_templates_with_options(
        self,
        request: miniapplcdp_20200113_models.ListAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListAppTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppTemplates',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_templates_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListAppTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppTemplates',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_templates(
        self,
        request: miniapplcdp_20200113_models.ListAppTemplatesRequest,
    ) -> miniapplcdp_20200113_models.ListAppTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_templates_with_options(request, runtime)

    async def list_app_templates_async(
        self,
        request: miniapplcdp_20200113_models.ListAppTemplatesRequest,
    ) -> miniapplcdp_20200113_models.ListAppTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_templates_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: miniapplcdp_20200113_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_status):
            query['AppStatus'] = request.app_status
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.main_module_id):
            query['MainModuleId'] = request.main_module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_status):
            query['AppStatus'] = request.app_status
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.main_module_id):
            query['MainModuleId'] = request.main_module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apps(
        self,
        request: miniapplcdp_20200113_models.ListAppsRequest,
    ) -> miniapplcdp_20200113_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: miniapplcdp_20200113_models.ListAppsRequest,
    ) -> miniapplcdp_20200113_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_artifacts_with_options(
        self,
        request: miniapplcdp_20200113_models.ListArtifactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListArtifactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.publish_id):
            query['PublishId'] = request.publish_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifacts',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListArtifactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifacts_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListArtifactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListArtifactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.publish_id):
            query['PublishId'] = request.publish_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifacts',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListArtifactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifacts(
        self,
        request: miniapplcdp_20200113_models.ListArtifactsRequest,
    ) -> miniapplcdp_20200113_models.ListArtifactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_artifacts_with_options(request, runtime)

    async def list_artifacts_async(
        self,
        request: miniapplcdp_20200113_models.ListArtifactsRequest,
    ) -> miniapplcdp_20200113_models.ListArtifactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_artifacts_with_options_async(request, runtime)

    def list_commits_with_options(
        self,
        request: miniapplcdp_20200113_models.ListCommitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListCommitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_log):
            query['CommitLog'] = request.commit_log
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommits',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListCommitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_commits_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListCommitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListCommitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_log):
            query['CommitLog'] = request.commit_log
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommits',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListCommitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_commits(
        self,
        request: miniapplcdp_20200113_models.ListCommitsRequest,
    ) -> miniapplcdp_20200113_models.ListCommitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_commits_with_options(request, runtime)

    async def list_commits_async(
        self,
        request: miniapplcdp_20200113_models.ListCommitsRequest,
    ) -> miniapplcdp_20200113_models.ListCommitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_commits_with_options_async(request, runtime)

    def list_domains_with_options(
        self,
        request: miniapplcdp_20200113_models.ListDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: miniapplcdp_20200113_models.ListDomainsRequest,
    ) -> miniapplcdp_20200113_models.ListDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    async def list_domains_async(
        self,
        request: miniapplcdp_20200113_models.ListDomainsRequest,
    ) -> miniapplcdp_20200113_models.ListDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_domains_with_options_async(request, runtime)

    def list_environment_overviews_with_options(
        self,
        request: miniapplcdp_20200113_models.ListEnvironmentOverviewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListEnvironmentOverviewsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentOverviews',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListEnvironmentOverviewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_overviews_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListEnvironmentOverviewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListEnvironmentOverviewsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentOverviews',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListEnvironmentOverviewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_overviews(
        self,
        request: miniapplcdp_20200113_models.ListEnvironmentOverviewsRequest,
    ) -> miniapplcdp_20200113_models.ListEnvironmentOverviewsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_environment_overviews_with_options(request, runtime)

    async def list_environment_overviews_async(
        self,
        request: miniapplcdp_20200113_models.ListEnvironmentOverviewsRequest,
    ) -> miniapplcdp_20200113_models.ListEnvironmentOverviewsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_environment_overviews_with_options_async(request, runtime)

    def list_environments_with_options(
        self,
        request: miniapplcdp_20200113_models.ListEnvironmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListEnvironmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListEnvironmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListEnvironmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        request: miniapplcdp_20200113_models.ListEnvironmentsRequest,
    ) -> miniapplcdp_20200113_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_environments_with_options(request, runtime)

    async def list_environments_async(
        self,
        request: miniapplcdp_20200113_models.ListEnvironmentsRequest,
    ) -> miniapplcdp_20200113_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_environments_with_options_async(request, runtime)

    def list_models_with_options(
        self,
        request: miniapplcdp_20200113_models.ListModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModels',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModels',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_models(
        self,
        request: miniapplcdp_20200113_models.ListModelsRequest,
    ) -> miniapplcdp_20200113_models.ListModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_models_with_options(request, runtime)

    async def list_models_async(
        self,
        request: miniapplcdp_20200113_models.ListModelsRequest,
    ) -> miniapplcdp_20200113_models.ListModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_models_with_options_async(request, runtime)

    def list_models_by_page_with_options(
        self,
        request: miniapplcdp_20200113_models.ListModelsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModelsByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelsByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModelsByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_by_page_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListModelsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModelsByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelsByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModelsByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_models_by_page(
        self,
        request: miniapplcdp_20200113_models.ListModelsByPageRequest,
    ) -> miniapplcdp_20200113_models.ListModelsByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_models_by_page_with_options(request, runtime)

    async def list_models_by_page_async(
        self,
        request: miniapplcdp_20200113_models.ListModelsByPageRequest,
    ) -> miniapplcdp_20200113_models.ListModelsByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_models_by_page_with_options_async(request, runtime)

    def list_module_dependencies_with_options(
        self,
        request: miniapplcdp_20200113_models.ListModuleDependenciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModuleDependenciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleDependencies',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleDependenciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_module_dependencies_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListModuleDependenciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModuleDependenciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.recursive):
            query['Recursive'] = request.recursive
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleDependencies',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleDependenciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_module_dependencies(
        self,
        request: miniapplcdp_20200113_models.ListModuleDependenciesRequest,
    ) -> miniapplcdp_20200113_models.ListModuleDependenciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_module_dependencies_with_options(request, runtime)

    async def list_module_dependencies_async(
        self,
        request: miniapplcdp_20200113_models.ListModuleDependenciesRequest,
    ) -> miniapplcdp_20200113_models.ListModuleDependenciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_module_dependencies_with_options_async(request, runtime)

    def list_module_models_with_options(
        self,
        request: miniapplcdp_20200113_models.ListModuleModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModuleModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_types):
            query['SubTypes'] = request.sub_types
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleModels',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_module_models_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListModuleModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModuleModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_types):
            query['SubTypes'] = request.sub_types
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleModels',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_module_models(
        self,
        request: miniapplcdp_20200113_models.ListModuleModelsRequest,
    ) -> miniapplcdp_20200113_models.ListModuleModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_module_models_with_options(request, runtime)

    async def list_module_models_async(
        self,
        request: miniapplcdp_20200113_models.ListModuleModelsRequest,
    ) -> miniapplcdp_20200113_models.ListModuleModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_module_models_with_options_async(request, runtime)

    def list_module_publish_versions_with_options(
        self,
        request: miniapplcdp_20200113_models.ListModulePublishVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModulePublishVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            query['ModuleVersion'] = request.module_version
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModulePublishVersions',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulePublishVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_module_publish_versions_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListModulePublishVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModulePublishVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            query['ModuleVersion'] = request.module_version
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModulePublishVersions',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulePublishVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_module_publish_versions(
        self,
        request: miniapplcdp_20200113_models.ListModulePublishVersionsRequest,
    ) -> miniapplcdp_20200113_models.ListModulePublishVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_module_publish_versions_with_options(request, runtime)

    async def list_module_publish_versions_async(
        self,
        request: miniapplcdp_20200113_models.ListModulePublishVersionsRequest,
    ) -> miniapplcdp_20200113_models.ListModulePublishVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_module_publish_versions_with_options_async(request, runtime)

    def list_module_resources_with_options(
        self,
        request: miniapplcdp_20200113_models.ListModuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModuleResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_module_resources_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListModuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModuleResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModuleResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_module_resources(
        self,
        request: miniapplcdp_20200113_models.ListModuleResourcesRequest,
    ) -> miniapplcdp_20200113_models.ListModuleResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_module_resources_with_options(request, runtime)

    async def list_module_resources_async(
        self,
        request: miniapplcdp_20200113_models.ListModuleResourcesRequest,
    ) -> miniapplcdp_20200113_models.ListModuleResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_module_resources_with_options_async(request, runtime)

    def list_modules_with_options(
        self,
        request: miniapplcdp_20200113_models.ListModulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_modules_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListModulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_modules(
        self,
        request: miniapplcdp_20200113_models.ListModulesRequest,
    ) -> miniapplcdp_20200113_models.ListModulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_modules_with_options(request, runtime)

    async def list_modules_async(
        self,
        request: miniapplcdp_20200113_models.ListModulesRequest,
    ) -> miniapplcdp_20200113_models.ListModulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_modules_with_options_async(request, runtime)

    def list_modules_by_page_with_options(
        self,
        request: miniapplcdp_20200113_models.ListModulesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModulesByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModulesByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_modules_by_page_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListModulesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListModulesByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_parent_id):
            query['CustomParentId'] = request.custom_parent_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModulesByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListModulesByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_modules_by_page(
        self,
        request: miniapplcdp_20200113_models.ListModulesByPageRequest,
    ) -> miniapplcdp_20200113_models.ListModulesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_modules_by_page_with_options(request, runtime)

    async def list_modules_by_page_async(
        self,
        request: miniapplcdp_20200113_models.ListModulesByPageRequest,
    ) -> miniapplcdp_20200113_models.ListModulesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_modules_by_page_with_options_async(request, runtime)

    def list_publish_versions_with_options(
        self,
        request: miniapplcdp_20200113_models.ListPublishVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListPublishVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishVersions',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_publish_versions_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListPublishVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListPublishVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishVersions',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_publish_versions(
        self,
        request: miniapplcdp_20200113_models.ListPublishVersionsRequest,
    ) -> miniapplcdp_20200113_models.ListPublishVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_publish_versions_with_options(request, runtime)

    async def list_publish_versions_async(
        self,
        request: miniapplcdp_20200113_models.ListPublishVersionsRequest,
    ) -> miniapplcdp_20200113_models.ListPublishVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_publish_versions_with_options_async(request, runtime)

    def list_published_modules_with_options(
        self,
        request: miniapplcdp_20200113_models.ListPublishedModulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListPublishedModulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_app_id):
            query['ExcludeAppId'] = request.exclude_app_id
        if not UtilClient.is_unset(request.exclude_module_id):
            query['ExcludeModuleId'] = request.exclude_module_id
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishedModulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_modules_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListPublishedModulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListPublishedModulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.exclude_app_id):
            query['ExcludeAppId'] = request.exclude_app_id
        if not UtilClient.is_unset(request.exclude_module_id):
            query['ExcludeModuleId'] = request.exclude_module_id
        if not UtilClient.is_unset(request.has_owner_app):
            query['HasOwnerApp'] = request.has_owner_app
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.module_type):
            query['ModuleType'] = request.module_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedModules',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishedModulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_modules(
        self,
        request: miniapplcdp_20200113_models.ListPublishedModulesRequest,
    ) -> miniapplcdp_20200113_models.ListPublishedModulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_published_modules_with_options(request, runtime)

    async def list_published_modules_async(
        self,
        request: miniapplcdp_20200113_models.ListPublishedModulesRequest,
    ) -> miniapplcdp_20200113_models.ListPublishedModulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_published_modules_with_options_async(request, runtime)

    def list_publishes_with_options(
        self,
        request: miniapplcdp_20200113_models.ListPublishesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListPublishesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.publish_status):
            query['PublishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.publish_type):
            query['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishes',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_publishes_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListPublishesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListPublishesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.publish_status):
            query['PublishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.publish_type):
            query['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishes',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListPublishesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_publishes(
        self,
        request: miniapplcdp_20200113_models.ListPublishesRequest,
    ) -> miniapplcdp_20200113_models.ListPublishesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_publishes_with_options(request, runtime)

    async def list_publishes_async(
        self,
        request: miniapplcdp_20200113_models.ListPublishesRequest,
    ) -> miniapplcdp_20200113_models.ListPublishesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_publishes_with_options_async(request, runtime)

    def list_resources_with_options(
        self,
        request: miniapplcdp_20200113_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: miniapplcdp_20200113_models.ListResourcesRequest,
    ) -> miniapplcdp_20200113_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    async def list_resources_async(
        self,
        request: miniapplcdp_20200113_models.ListResourcesRequest,
    ) -> miniapplcdp_20200113_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_with_options_async(request, runtime)

    def list_resources_by_page_with_options(
        self,
        request: miniapplcdp_20200113_models.ListResourcesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListResourcesByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListResourcesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_by_page_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ListResourcesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ListResourcesByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_process_parameter):
            query['ImageProcessParameter'] = request.image_process_parameter
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.with_content):
            query['WithContent'] = request.with_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesByPage',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ListResourcesByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources_by_page(
        self,
        request: miniapplcdp_20200113_models.ListResourcesByPageRequest,
    ) -> miniapplcdp_20200113_models.ListResourcesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resources_by_page_with_options(request, runtime)

    async def list_resources_by_page_async(
        self,
        request: miniapplcdp_20200113_models.ListResourcesByPageRequest,
    ) -> miniapplcdp_20200113_models.ListResourcesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_by_page_with_options_async(request, runtime)

    def reset_app_user_password_with_options(
        self,
        request: miniapplcdp_20200113_models.ResetAppUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ResetAppUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppUserPassword',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ResetAppUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_user_password_with_options_async(
        self,
        request: miniapplcdp_20200113_models.ResetAppUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.ResetAppUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppUserPassword',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.ResetAppUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_user_password(
        self,
        request: miniapplcdp_20200113_models.ResetAppUserPasswordRequest,
    ) -> miniapplcdp_20200113_models.ResetAppUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_app_user_password_with_options(request, runtime)

    async def reset_app_user_password_async(
        self,
        request: miniapplcdp_20200113_models.ResetAppUserPasswordRequest,
    ) -> miniapplcdp_20200113_models.ResetAppUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_app_user_password_with_options_async(request, runtime)

    def restore_model_with_options(
        self,
        request: miniapplcdp_20200113_models.RestoreModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.RestoreModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.RestoreModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.RestoreModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.RestoreModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.RestoreModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_model(
        self,
        request: miniapplcdp_20200113_models.RestoreModelRequest,
    ) -> miniapplcdp_20200113_models.RestoreModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_model_with_options(request, runtime)

    async def restore_model_async(
        self,
        request: miniapplcdp_20200113_models.RestoreModelRequest,
    ) -> miniapplcdp_20200113_models.RestoreModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_model_with_options_async(request, runtime)

    def run_logic_model_with_options(
        self,
        request: miniapplcdp_20200113_models.RunLogicModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.RunLogicModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunLogicModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.RunLogicModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_logic_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.RunLogicModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.RunLogicModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.commit_id):
            query['CommitId'] = request.commit_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunLogicModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.RunLogicModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_logic_model(
        self,
        request: miniapplcdp_20200113_models.RunLogicModelRequest,
    ) -> miniapplcdp_20200113_models.RunLogicModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_logic_model_with_options(request, runtime)

    async def run_logic_model_async(
        self,
        request: miniapplcdp_20200113_models.RunLogicModelRequest,
    ) -> miniapplcdp_20200113_models.RunLogicModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_logic_model_with_options_async(request, runtime)

    def set_environment_default_domain_with_options(
        self,
        request: miniapplcdp_20200113_models.SetEnvironmentDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.SetEnvironmentDefaultDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEnvironmentDefaultDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.SetEnvironmentDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_environment_default_domain_with_options_async(
        self,
        request: miniapplcdp_20200113_models.SetEnvironmentDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.SetEnvironmentDefaultDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEnvironmentDefaultDomain',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.SetEnvironmentDefaultDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_environment_default_domain(
        self,
        request: miniapplcdp_20200113_models.SetEnvironmentDefaultDomainRequest,
    ) -> miniapplcdp_20200113_models.SetEnvironmentDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_environment_default_domain_with_options(request, runtime)

    async def set_environment_default_domain_async(
        self,
        request: miniapplcdp_20200113_models.SetEnvironmentDefaultDomainRequest,
    ) -> miniapplcdp_20200113_models.SetEnvironmentDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_environment_default_domain_with_options_async(request, runtime)

    def start_app_server_with_options(
        self,
        request: miniapplcdp_20200113_models.StartAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.StartAppServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAppServer',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.StartAppServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_app_server_with_options_async(
        self,
        request: miniapplcdp_20200113_models.StartAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.StartAppServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAppServer',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.StartAppServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_app_server(
        self,
        request: miniapplcdp_20200113_models.StartAppServerRequest,
    ) -> miniapplcdp_20200113_models.StartAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_app_server_with_options(request, runtime)

    async def start_app_server_async(
        self,
        request: miniapplcdp_20200113_models.StartAppServerRequest,
    ) -> miniapplcdp_20200113_models.StartAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_app_server_with_options_async(request, runtime)

    def stop_app_server_with_options(
        self,
        request: miniapplcdp_20200113_models.StopAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.StopAppServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppServer',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.StopAppServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_app_server_with_options_async(
        self,
        request: miniapplcdp_20200113_models.StopAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.StopAppServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppServer',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.StopAppServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_app_server(
        self,
        request: miniapplcdp_20200113_models.StopAppServerRequest,
    ) -> miniapplcdp_20200113_models.StopAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_app_server_with_options(request, runtime)

    async def stop_app_server_async(
        self,
        request: miniapplcdp_20200113_models.StopAppServerRequest,
    ) -> miniapplcdp_20200113_models.StopAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_app_server_with_options_async(request, runtime)

    def update_app_with_options(
        self,
        request: miniapplcdp_20200113_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: miniapplcdp_20200113_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app(
        self,
        request: miniapplcdp_20200113_models.UpdateAppRequest,
    ) -> miniapplcdp_20200113_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: miniapplcdp_20200113_models.UpdateAppRequest,
    ) -> miniapplcdp_20200113_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)

    def update_app_model_with_options(
        self,
        request: miniapplcdp_20200113_models.UpdateAppModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateAppModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateAppModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.UpdateAppModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateAppModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateAppModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_model(
        self,
        request: miniapplcdp_20200113_models.UpdateAppModelRequest,
    ) -> miniapplcdp_20200113_models.UpdateAppModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_model_with_options(request, runtime)

    async def update_app_model_async(
        self,
        request: miniapplcdp_20200113_models.UpdateAppModelRequest,
    ) -> miniapplcdp_20200113_models.UpdateAppModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_model_with_options_async(request, runtime)

    def update_model_with_options(
        self,
        request: miniapplcdp_20200113_models.UpdateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_with_options_async(
        self,
        request: miniapplcdp_20200113_models.UpdateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateModel',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model(
        self,
        request: miniapplcdp_20200113_models.UpdateModelRequest,
    ) -> miniapplcdp_20200113_models.UpdateModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_model_with_options(request, runtime)

    async def update_model_async(
        self,
        request: miniapplcdp_20200113_models.UpdateModelRequest,
    ) -> miniapplcdp_20200113_models.UpdateModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_model_with_options_async(request, runtime)

    def update_module_with_options(
        self,
        request: miniapplcdp_20200113_models.UpdateModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_module_with_options_async(
        self,
        request: miniapplcdp_20200113_models.UpdateModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateModule',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_module(
        self,
        request: miniapplcdp_20200113_models.UpdateModuleRequest,
    ) -> miniapplcdp_20200113_models.UpdateModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_module_with_options(request, runtime)

    async def update_module_async(
        self,
        request: miniapplcdp_20200113_models.UpdateModuleRequest,
    ) -> miniapplcdp_20200113_models.UpdateModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_module_with_options_async(request, runtime)

    def update_resource_with_options(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceRequest,
    ) -> miniapplcdp_20200113_models.UpdateResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_with_options(request, runtime)

    async def update_resource_async(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceRequest,
    ) -> miniapplcdp_20200113_models.UpdateResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_with_options_async(request, runtime)

    def update_resource_content_with_options(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateResourceContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceContent',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_content_with_options_async(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateResourceContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceContent',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_content(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceContentRequest,
    ) -> miniapplcdp_20200113_models.UpdateResourceContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_content_with_options(request, runtime)

    async def update_resource_content_async(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceContentRequest,
    ) -> miniapplcdp_20200113_models.UpdateResourceContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_content_with_options_async(request, runtime)

    def update_resource_info_with_options(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateResourceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceInfo',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_info_with_options_async(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> miniapplcdp_20200113_models.UpdateResourceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            query['ModuleId'] = request.module_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceInfo',
            version='2020-01-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            miniapplcdp_20200113_models.UpdateResourceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_info(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceInfoRequest,
    ) -> miniapplcdp_20200113_models.UpdateResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_info_with_options(request, runtime)

    async def update_resource_info_async(
        self,
        request: miniapplcdp_20200113_models.UpdateResourceInfoRequest,
    ) -> miniapplcdp_20200113_models.UpdateResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_info_with_options_async(request, runtime)
