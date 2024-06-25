# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_acm20200206 import models as acm_20200206_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('acm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_export_configurations_with_options(
        self,
        request: acm_20200206_models.BatchExportConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.BatchExportConfigurationsResponse:
        """
        @param request: BatchExportConfigurationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchExportConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchExportConfigurations',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/export',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.BatchExportConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_export_configurations_with_options_async(
        self,
        request: acm_20200206_models.BatchExportConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.BatchExportConfigurationsResponse:
        """
        @param request: BatchExportConfigurationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchExportConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchExportConfigurations',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/export',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.BatchExportConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_export_configurations(
        self,
        request: acm_20200206_models.BatchExportConfigurationsRequest,
    ) -> acm_20200206_models.BatchExportConfigurationsResponse:
        """
        @param request: BatchExportConfigurationsRequest
        @return: BatchExportConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_export_configurations_with_options(request, headers, runtime)

    async def batch_export_configurations_async(
        self,
        request: acm_20200206_models.BatchExportConfigurationsRequest,
    ) -> acm_20200206_models.BatchExportConfigurationsResponse:
        """
        @param request: BatchExportConfigurationsRequest
        @return: BatchExportConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_export_configurations_with_options_async(request, headers, runtime)

    def batch_import_configurations_with_options(
        self,
        request: acm_20200206_models.BatchImportConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.BatchImportConfigurationsResponse:
        """
        @param request: BatchImportConfigurationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchImportConfigurationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchImportConfigurations',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.BatchImportConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_import_configurations_with_options_async(
        self,
        request: acm_20200206_models.BatchImportConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.BatchImportConfigurationsResponse:
        """
        @param request: BatchImportConfigurationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchImportConfigurationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchImportConfigurations',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.BatchImportConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_import_configurations(
        self,
        request: acm_20200206_models.BatchImportConfigurationsRequest,
    ) -> acm_20200206_models.BatchImportConfigurationsResponse:
        """
        @param request: BatchImportConfigurationsRequest
        @return: BatchImportConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_import_configurations_with_options(request, headers, runtime)

    async def batch_import_configurations_async(
        self,
        request: acm_20200206_models.BatchImportConfigurationsRequest,
    ) -> acm_20200206_models.BatchImportConfigurationsResponse:
        """
        @param request: BatchImportConfigurationsRequest
        @return: BatchImportConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_import_configurations_with_options_async(request, headers, runtime)

    def check_configuration_clone_with_options(
        self,
        request: acm_20200206_models.CheckConfigurationCloneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CheckConfigurationCloneResponse:
        """
        @param request: CheckConfigurationCloneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckConfigurationCloneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.namespace_from):
            body['NamespaceFrom'] = request.namespace_from
        if not UtilClient.is_unset(request.namespace_to):
            body['NamespaceTo'] = request.namespace_to
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckConfigurationClone',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/checkForClone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CheckConfigurationCloneResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_configuration_clone_with_options_async(
        self,
        request: acm_20200206_models.CheckConfigurationCloneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CheckConfigurationCloneResponse:
        """
        @param request: CheckConfigurationCloneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckConfigurationCloneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.namespace_from):
            body['NamespaceFrom'] = request.namespace_from
        if not UtilClient.is_unset(request.namespace_to):
            body['NamespaceTo'] = request.namespace_to
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckConfigurationClone',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/checkForClone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CheckConfigurationCloneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_configuration_clone(
        self,
        request: acm_20200206_models.CheckConfigurationCloneRequest,
    ) -> acm_20200206_models.CheckConfigurationCloneResponse:
        """
        @param request: CheckConfigurationCloneRequest
        @return: CheckConfigurationCloneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_configuration_clone_with_options(request, headers, runtime)

    async def check_configuration_clone_async(
        self,
        request: acm_20200206_models.CheckConfigurationCloneRequest,
    ) -> acm_20200206_models.CheckConfigurationCloneResponse:
        """
        @param request: CheckConfigurationCloneRequest
        @return: CheckConfigurationCloneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_configuration_clone_with_options_async(request, headers, runtime)

    def check_configuration_export_with_options(
        self,
        request: acm_20200206_models.CheckConfigurationExportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CheckConfigurationExportResponse:
        """
        @param request: CheckConfigurationExportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckConfigurationExportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckConfigurationExport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/checkForExport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CheckConfigurationExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_configuration_export_with_options_async(
        self,
        request: acm_20200206_models.CheckConfigurationExportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CheckConfigurationExportResponse:
        """
        @param request: CheckConfigurationExportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckConfigurationExportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckConfigurationExport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/checkForExport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CheckConfigurationExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_configuration_export(
        self,
        request: acm_20200206_models.CheckConfigurationExportRequest,
    ) -> acm_20200206_models.CheckConfigurationExportResponse:
        """
        @param request: CheckConfigurationExportRequest
        @return: CheckConfigurationExportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_configuration_export_with_options(request, headers, runtime)

    async def check_configuration_export_async(
        self,
        request: acm_20200206_models.CheckConfigurationExportRequest,
    ) -> acm_20200206_models.CheckConfigurationExportResponse:
        """
        @param request: CheckConfigurationExportRequest
        @return: CheckConfigurationExportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_configuration_export_with_options_async(request, headers, runtime)

    def clone_configuration_with_options(
        self,
        request: acm_20200206_models.CloneConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CloneConfigurationResponse:
        """
        @param request: CloneConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneConfigurationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.namespace_from):
            body['NamespaceFrom'] = request.namespace_from
        if not UtilClient.is_unset(request.namespace_to):
            body['NamespaceTo'] = request.namespace_to
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CloneConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_configuration_with_options_async(
        self,
        request: acm_20200206_models.CloneConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CloneConfigurationResponse:
        """
        @param request: CloneConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneConfigurationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.namespace_from):
            body['NamespaceFrom'] = request.namespace_from
        if not UtilClient.is_unset(request.namespace_to):
            body['NamespaceTo'] = request.namespace_to
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CloneConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_configuration(
        self,
        request: acm_20200206_models.CloneConfigurationRequest,
    ) -> acm_20200206_models.CloneConfigurationResponse:
        """
        @param request: CloneConfigurationRequest
        @return: CloneConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_configuration_with_options(request, headers, runtime)

    async def clone_configuration_async(
        self,
        request: acm_20200206_models.CloneConfigurationRequest,
    ) -> acm_20200206_models.CloneConfigurationResponse:
        """
        @param request: CloneConfigurationRequest
        @return: CloneConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_configuration_with_options_async(request, headers, runtime)

    def create_configuration_with_options(
        self,
        request: acm_20200206_models.CreateConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CreateConfigurationResponse:
        """
        @param request: CreateConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigurationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/configuration',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CreateConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_configuration_with_options_async(
        self,
        request: acm_20200206_models.CreateConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CreateConfigurationResponse:
        """
        @param request: CreateConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigurationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/configuration',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CreateConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_configuration(
        self,
        request: acm_20200206_models.CreateConfigurationRequest,
    ) -> acm_20200206_models.CreateConfigurationResponse:
        """
        @param request: CreateConfigurationRequest
        @return: CreateConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_configuration_with_options(request, headers, runtime)

    async def create_configuration_async(
        self,
        request: acm_20200206_models.CreateConfigurationRequest,
    ) -> acm_20200206_models.CreateConfigurationResponse:
        """
        @param request: CreateConfigurationRequest
        @return: CreateConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_configuration_with_options_async(request, headers, runtime)

    def create_namespace_with_options(
        self,
        request: acm_20200206_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CreateNamespaceResponse:
        """
        @param request: CreateNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: acm_20200206_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CreateNamespaceResponse:
        """
        @param request: CreateNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: acm_20200206_models.CreateNamespaceRequest,
    ) -> acm_20200206_models.CreateNamespaceResponse:
        """
        @param request: CreateNamespaceRequest
        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_namespace_with_options(request, headers, runtime)

    async def create_namespace_async(
        self,
        request: acm_20200206_models.CreateNamespaceRequest,
    ) -> acm_20200206_models.CreateNamespaceResponse:
        """
        @param request: CreateNamespaceRequest
        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_namespace_with_options_async(request, headers, runtime)

    def delete_configuration_with_options(
        self,
        request: acm_20200206_models.DeleteConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeleteConfigurationResponse:
        """
        @param request: DeleteConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/configuration',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DeleteConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_configuration_with_options_async(
        self,
        request: acm_20200206_models.DeleteConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeleteConfigurationResponse:
        """
        @param request: DeleteConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/configuration',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DeleteConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_configuration(
        self,
        request: acm_20200206_models.DeleteConfigurationRequest,
    ) -> acm_20200206_models.DeleteConfigurationResponse:
        """
        @param request: DeleteConfigurationRequest
        @return: DeleteConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_configuration_with_options(request, headers, runtime)

    async def delete_configuration_async(
        self,
        request: acm_20200206_models.DeleteConfigurationRequest,
    ) -> acm_20200206_models.DeleteConfigurationResponse:
        """
        @param request: DeleteConfigurationRequest
        @return: DeleteConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_configuration_with_options_async(request, headers, runtime)

    def delete_namespace_with_options(
        self,
        request: acm_20200206_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeleteNamespaceResponse:
        """
        @param request: DeleteNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: acm_20200206_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeleteNamespaceResponse:
        """
        @param request: DeleteNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: acm_20200206_models.DeleteNamespaceRequest,
    ) -> acm_20200206_models.DeleteNamespaceResponse:
        """
        @param request: DeleteNamespaceRequest
        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_namespace_with_options(request, headers, runtime)

    async def delete_namespace_async(
        self,
        request: acm_20200206_models.DeleteNamespaceRequest,
    ) -> acm_20200206_models.DeleteNamespaceResponse:
        """
        @param request: DeleteNamespaceRequest
        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_namespace_with_options_async(request, headers, runtime)

    def deploy_configuration_with_options(
        self,
        request: acm_20200206_models.DeployConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeployConfigurationResponse:
        """
        @param request: DeployConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployConfigurationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.beta_ips):
            body['BetaIps'] = request.beta_ips
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/configuration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DeployConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_configuration_with_options_async(
        self,
        request: acm_20200206_models.DeployConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeployConfigurationResponse:
        """
        @param request: DeployConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployConfigurationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.beta_ips):
            body['BetaIps'] = request.beta_ips
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/configuration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DeployConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_configuration(
        self,
        request: acm_20200206_models.DeployConfigurationRequest,
    ) -> acm_20200206_models.DeployConfigurationResponse:
        """
        @param request: DeployConfigurationRequest
        @return: DeployConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_configuration_with_options(request, headers, runtime)

    async def deploy_configuration_async(
        self,
        request: acm_20200206_models.DeployConfigurationRequest,
    ) -> acm_20200206_models.DeployConfigurationResponse:
        """
        @param request: DeployConfigurationRequest
        @return: DeployConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_configuration_with_options_async(request, headers, runtime)

    def describe_configuration_with_options(
        self,
        request: acm_20200206_models.DescribeConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeConfigurationResponse:
        """
        @param request: DescribeConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/configuration',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configuration_with_options_async(
        self,
        request: acm_20200206_models.DescribeConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeConfigurationResponse:
        """
        @param request: DescribeConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/configuration',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_configuration(
        self,
        request: acm_20200206_models.DescribeConfigurationRequest,
    ) -> acm_20200206_models.DescribeConfigurationResponse:
        """
        @param request: DescribeConfigurationRequest
        @return: DescribeConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_configuration_with_options(request, headers, runtime)

    async def describe_configuration_async(
        self,
        request: acm_20200206_models.DescribeConfigurationRequest,
    ) -> acm_20200206_models.DescribeConfigurationResponse:
        """
        @param request: DescribeConfigurationRequest
        @return: DescribeConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_configuration_with_options_async(request, headers, runtime)

    def describe_import_file_url_with_options(
        self,
        request: acm_20200206_models.DescribeImportFileUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeImportFileUrlResponse:
        """
        @param request: DescribeImportFileUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImportFileUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImportFileUrl',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/importFileUrl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeImportFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_import_file_url_with_options_async(
        self,
        request: acm_20200206_models.DescribeImportFileUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeImportFileUrlResponse:
        """
        @param request: DescribeImportFileUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImportFileUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImportFileUrl',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/batch/importFileUrl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeImportFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_import_file_url(
        self,
        request: acm_20200206_models.DescribeImportFileUrlRequest,
    ) -> acm_20200206_models.DescribeImportFileUrlResponse:
        """
        @param request: DescribeImportFileUrlRequest
        @return: DescribeImportFileUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_import_file_url_with_options(request, headers, runtime)

    async def describe_import_file_url_async(
        self,
        request: acm_20200206_models.DescribeImportFileUrlRequest,
    ) -> acm_20200206_models.DescribeImportFileUrlResponse:
        """
        @param request: DescribeImportFileUrlRequest
        @return: DescribeImportFileUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_import_file_url_with_options_async(request, headers, runtime)

    def describe_namespace_with_options(
        self,
        request: acm_20200206_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespaceResponse:
        """
        @param request: DescribeNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_with_options_async(
        self,
        request: acm_20200206_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespaceResponse:
        """
        @param request: DescribeNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace(
        self,
        request: acm_20200206_models.DescribeNamespaceRequest,
    ) -> acm_20200206_models.DescribeNamespaceResponse:
        """
        @param request: DescribeNamespaceRequest
        @return: DescribeNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_with_options(request, headers, runtime)

    async def describe_namespace_async(
        self,
        request: acm_20200206_models.DescribeNamespaceRequest,
    ) -> acm_20200206_models.DescribeNamespaceResponse:
        """
        @param request: DescribeNamespaceRequest
        @return: DescribeNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespace_with_options_async(request, headers, runtime)

    def describe_namespaces_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespacesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespacesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespaces_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespacesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespacesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespaces(self) -> acm_20200206_models.DescribeNamespacesResponse:
        """
        @return: DescribeNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespaces_with_options(headers, runtime)

    async def describe_namespaces_async(self) -> acm_20200206_models.DescribeNamespacesResponse:
        """
        @return: DescribeNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespaces_with_options_async(headers, runtime)

    def describe_namespaces_with_create_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespacesWithCreateResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespacesWithCreateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeNamespacesWithCreate',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace/listWithCreate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeNamespacesWithCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespaces_with_create_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespacesWithCreateResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespacesWithCreateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeNamespacesWithCreate',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace/listWithCreate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeNamespacesWithCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespaces_with_create(self) -> acm_20200206_models.DescribeNamespacesWithCreateResponse:
        """
        @return: DescribeNamespacesWithCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespaces_with_create_with_options(headers, runtime)

    async def describe_namespaces_with_create_async(self) -> acm_20200206_models.DescribeNamespacesWithCreateResponse:
        """
        @return: DescribeNamespacesWithCreateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespaces_with_create_with_options_async(headers, runtime)

    def describe_trace_by_configuration_with_options(
        self,
        request: acm_20200206_models.DescribeTraceByConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeTraceByConfigurationResponse:
        """
        @param request: DescribeTraceByConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTraceByConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceByConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/trace/getByConfiguration',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeTraceByConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trace_by_configuration_with_options_async(
        self,
        request: acm_20200206_models.DescribeTraceByConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeTraceByConfigurationResponse:
        """
        @param request: DescribeTraceByConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTraceByConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceByConfiguration',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/trace/getByConfiguration',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.DescribeTraceByConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trace_by_configuration(
        self,
        request: acm_20200206_models.DescribeTraceByConfigurationRequest,
    ) -> acm_20200206_models.DescribeTraceByConfigurationResponse:
        """
        @param request: DescribeTraceByConfigurationRequest
        @return: DescribeTraceByConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_trace_by_configuration_with_options(request, headers, runtime)

    async def describe_trace_by_configuration_async(
        self,
        request: acm_20200206_models.DescribeTraceByConfigurationRequest,
    ) -> acm_20200206_models.DescribeTraceByConfigurationResponse:
        """
        @param request: DescribeTraceByConfigurationRequest
        @return: DescribeTraceByConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_trace_by_configuration_with_options_async(request, headers, runtime)

    def update_namespace_with_options(
        self,
        request: acm_20200206_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.UpdateNamespaceResponse:
        """
        @param request: UpdateNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            body['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: acm_20200206_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.UpdateNamespaceResponse:
        """
        @param request: UpdateNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            body['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/diamond-ops/pop/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            acm_20200206_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace(
        self,
        request: acm_20200206_models.UpdateNamespaceRequest,
    ) -> acm_20200206_models.UpdateNamespaceResponse:
        """
        @param request: UpdateNamespaceRequest
        @return: UpdateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_with_options(request, headers, runtime)

    async def update_namespace_async(
        self,
        request: acm_20200206_models.UpdateNamespaceRequest,
    ) -> acm_20200206_models.UpdateNamespaceResponse:
        """
        @param request: UpdateNamespaceRequest
        @return: UpdateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_namespace_with_options_async(request, headers, runtime)
