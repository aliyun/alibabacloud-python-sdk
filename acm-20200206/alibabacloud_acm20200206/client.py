# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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

    def batch_export_configurations(
        self,
        request: acm_20200206_models.BatchExportConfigurationsRequest,
    ) -> acm_20200206_models.BatchExportConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_export_configurations_with_options(request, headers, runtime)

    async def batch_export_configurations_async(
        self,
        request: acm_20200206_models.BatchExportConfigurationsRequest,
    ) -> acm_20200206_models.BatchExportConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_export_configurations_with_options_async(request, headers, runtime)

    def batch_export_configurations_with_options(
        self,
        request: acm_20200206_models.BatchExportConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.BatchExportConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.BatchExportConfigurationsResponse().from_map(
            self.do_roarequest('BatchExportConfigurations', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/batch/export', 'json', req, runtime)
        )

    async def batch_export_configurations_with_options_async(
        self,
        request: acm_20200206_models.BatchExportConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.BatchExportConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.BatchExportConfigurationsResponse().from_map(
            await self.do_roarequest_async('BatchExportConfigurations', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/batch/export', 'json', req, runtime)
        )

    def batch_import_configurations(
        self,
        request: acm_20200206_models.BatchImportConfigurationsRequest,
    ) -> acm_20200206_models.BatchImportConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_import_configurations_with_options(request, headers, runtime)

    async def batch_import_configurations_async(
        self,
        request: acm_20200206_models.BatchImportConfigurationsRequest,
    ) -> acm_20200206_models.BatchImportConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_import_configurations_with_options_async(request, headers, runtime)

    def batch_import_configurations_with_options(
        self,
        request: acm_20200206_models.BatchImportConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.BatchImportConfigurationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.BatchImportConfigurationsResponse().from_map(
            self.do_roarequest_with_form('BatchImportConfigurations', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/batch/import', 'json', req, runtime)
        )

    async def batch_import_configurations_with_options_async(
        self,
        request: acm_20200206_models.BatchImportConfigurationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.BatchImportConfigurationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.BatchImportConfigurationsResponse().from_map(
            await self.do_roarequest_with_form_async('BatchImportConfigurations', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/batch/import', 'json', req, runtime)
        )

    def check_configuration_clone(
        self,
        request: acm_20200206_models.CheckConfigurationCloneRequest,
    ) -> acm_20200206_models.CheckConfigurationCloneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_configuration_clone_with_options(request, headers, runtime)

    async def check_configuration_clone_async(
        self,
        request: acm_20200206_models.CheckConfigurationCloneRequest,
    ) -> acm_20200206_models.CheckConfigurationCloneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_configuration_clone_with_options_async(request, headers, runtime)

    def check_configuration_clone_with_options(
        self,
        request: acm_20200206_models.CheckConfigurationCloneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CheckConfigurationCloneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.namespace_from):
            body['NamespaceFrom'] = request.namespace_from
        if not UtilClient.is_unset(request.namespace_to):
            body['NamespaceTo'] = request.namespace_to
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CheckConfigurationCloneResponse().from_map(
            self.do_roarequest_with_form('CheckConfigurationClone', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/batch/checkForClone', 'json', req, runtime)
        )

    async def check_configuration_clone_with_options_async(
        self,
        request: acm_20200206_models.CheckConfigurationCloneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CheckConfigurationCloneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.namespace_from):
            body['NamespaceFrom'] = request.namespace_from
        if not UtilClient.is_unset(request.namespace_to):
            body['NamespaceTo'] = request.namespace_to
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CheckConfigurationCloneResponse().from_map(
            await self.do_roarequest_with_form_async('CheckConfigurationClone', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/batch/checkForClone', 'json', req, runtime)
        )

    def check_configuration_export(
        self,
        request: acm_20200206_models.CheckConfigurationExportRequest,
    ) -> acm_20200206_models.CheckConfigurationExportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_configuration_export_with_options(request, headers, runtime)

    async def check_configuration_export_async(
        self,
        request: acm_20200206_models.CheckConfigurationExportRequest,
    ) -> acm_20200206_models.CheckConfigurationExportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_configuration_export_with_options_async(request, headers, runtime)

    def check_configuration_export_with_options(
        self,
        request: acm_20200206_models.CheckConfigurationExportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CheckConfigurationExportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CheckConfigurationExportResponse().from_map(
            self.do_roarequest_with_form('CheckConfigurationExport', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/batch/checkForExport', 'json', req, runtime)
        )

    async def check_configuration_export_with_options_async(
        self,
        request: acm_20200206_models.CheckConfigurationExportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CheckConfigurationExportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CheckConfigurationExportResponse().from_map(
            await self.do_roarequest_with_form_async('CheckConfigurationExport', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/batch/checkForExport', 'json', req, runtime)
        )

    def clone_configuration(
        self,
        request: acm_20200206_models.CloneConfigurationRequest,
    ) -> acm_20200206_models.CloneConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_configuration_with_options(request, headers, runtime)

    async def clone_configuration_async(
        self,
        request: acm_20200206_models.CloneConfigurationRequest,
    ) -> acm_20200206_models.CloneConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_configuration_with_options_async(request, headers, runtime)

    def clone_configuration_with_options(
        self,
        request: acm_20200206_models.CloneConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CloneConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.namespace_from):
            body['NamespaceFrom'] = request.namespace_from
        if not UtilClient.is_unset(request.namespace_to):
            body['NamespaceTo'] = request.namespace_to
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CloneConfigurationResponse().from_map(
            self.do_roarequest_with_form('CloneConfiguration', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/batch/clone', 'json', req, runtime)
        )

    async def clone_configuration_with_options_async(
        self,
        request: acm_20200206_models.CloneConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CloneConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.namespace_from):
            body['NamespaceFrom'] = request.namespace_from
        if not UtilClient.is_unset(request.namespace_to):
            body['NamespaceTo'] = request.namespace_to
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CloneConfigurationResponse().from_map(
            await self.do_roarequest_with_form_async('CloneConfiguration', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/batch/clone', 'json', req, runtime)
        )

    def create_configuration(
        self,
        request: acm_20200206_models.CreateConfigurationRequest,
    ) -> acm_20200206_models.CreateConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_configuration_with_options(request, headers, runtime)

    async def create_configuration_async(
        self,
        request: acm_20200206_models.CreateConfigurationRequest,
    ) -> acm_20200206_models.CreateConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_configuration_with_options_async(request, headers, runtime)

    def create_configuration_with_options(
        self,
        request: acm_20200206_models.CreateConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CreateConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CreateConfigurationResponse().from_map(
            self.do_roarequest_with_form('CreateConfiguration', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/configuration', 'json', req, runtime)
        )

    async def create_configuration_with_options_async(
        self,
        request: acm_20200206_models.CreateConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CreateConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CreateConfigurationResponse().from_map(
            await self.do_roarequest_with_form_async('CreateConfiguration', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/configuration', 'json', req, runtime)
        )

    def create_namespace(
        self,
        request: acm_20200206_models.CreateNamespaceRequest,
    ) -> acm_20200206_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_namespace_with_options(request, headers, runtime)

    async def create_namespace_async(
        self,
        request: acm_20200206_models.CreateNamespaceRequest,
    ) -> acm_20200206_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_namespace_with_options_async(request, headers, runtime)

    def create_namespace_with_options(
        self,
        request: acm_20200206_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CreateNamespaceResponse().from_map(
            self.do_roarequest_with_form('CreateNamespace', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/namespace', 'json', req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: acm_20200206_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.CreateNamespaceResponse().from_map(
            await self.do_roarequest_with_form_async('CreateNamespace', '2020-02-06', 'HTTPS', 'POST', 'AK', f'/diamond-ops/pop/namespace', 'json', req, runtime)
        )

    def delete_configuration(
        self,
        request: acm_20200206_models.DeleteConfigurationRequest,
    ) -> acm_20200206_models.DeleteConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_configuration_with_options(request, headers, runtime)

    async def delete_configuration_async(
        self,
        request: acm_20200206_models.DeleteConfigurationRequest,
    ) -> acm_20200206_models.DeleteConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_configuration_with_options_async(request, headers, runtime)

    def delete_configuration_with_options(
        self,
        request: acm_20200206_models.DeleteConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeleteConfigurationResponse:
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
        return acm_20200206_models.DeleteConfigurationResponse().from_map(
            self.do_roarequest('DeleteConfiguration', '2020-02-06', 'HTTPS', 'DELETE', 'AK', f'/diamond-ops/pop/configuration', 'json', req, runtime)
        )

    async def delete_configuration_with_options_async(
        self,
        request: acm_20200206_models.DeleteConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeleteConfigurationResponse:
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
        return acm_20200206_models.DeleteConfigurationResponse().from_map(
            await self.do_roarequest_async('DeleteConfiguration', '2020-02-06', 'HTTPS', 'DELETE', 'AK', f'/diamond-ops/pop/configuration', 'json', req, runtime)
        )

    def delete_namespace(
        self,
        request: acm_20200206_models.DeleteNamespaceRequest,
    ) -> acm_20200206_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_namespace_with_options(request, headers, runtime)

    async def delete_namespace_async(
        self,
        request: acm_20200206_models.DeleteNamespaceRequest,
    ) -> acm_20200206_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_namespace_with_options_async(request, headers, runtime)

    def delete_namespace_with_options(
        self,
        request: acm_20200206_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.DeleteNamespaceResponse().from_map(
            self.do_roarequest('DeleteNamespace', '2020-02-06', 'HTTPS', 'DELETE', 'AK', f'/diamond-ops/pop/namespace', 'json', req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: acm_20200206_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.DeleteNamespaceResponse().from_map(
            await self.do_roarequest_async('DeleteNamespace', '2020-02-06', 'HTTPS', 'DELETE', 'AK', f'/diamond-ops/pop/namespace', 'json', req, runtime)
        )

    def deploy_configuration(
        self,
        request: acm_20200206_models.DeployConfigurationRequest,
    ) -> acm_20200206_models.DeployConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_configuration_with_options(request, headers, runtime)

    async def deploy_configuration_async(
        self,
        request: acm_20200206_models.DeployConfigurationRequest,
    ) -> acm_20200206_models.DeployConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_configuration_with_options_async(request, headers, runtime)

    def deploy_configuration_with_options(
        self,
        request: acm_20200206_models.DeployConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeployConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.beta_ips):
            body['BetaIps'] = request.beta_ips
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.DeployConfigurationResponse().from_map(
            self.do_roarequest_with_form('DeployConfiguration', '2020-02-06', 'HTTPS', 'PUT', 'AK', f'/diamond-ops/pop/configuration', 'json', req, runtime)
        )

    async def deploy_configuration_with_options_async(
        self,
        request: acm_20200206_models.DeployConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DeployConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.namespace_id):
            body['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.beta_ips):
            body['BetaIps'] = request.beta_ips
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return acm_20200206_models.DeployConfigurationResponse().from_map(
            await self.do_roarequest_with_form_async('DeployConfiguration', '2020-02-06', 'HTTPS', 'PUT', 'AK', f'/diamond-ops/pop/configuration', 'json', req, runtime)
        )

    def describe_configuration(
        self,
        request: acm_20200206_models.DescribeConfigurationRequest,
    ) -> acm_20200206_models.DescribeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_configuration_with_options(request, headers, runtime)

    async def describe_configuration_async(
        self,
        request: acm_20200206_models.DescribeConfigurationRequest,
    ) -> acm_20200206_models.DescribeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_configuration_with_options_async(request, headers, runtime)

    def describe_configuration_with_options(
        self,
        request: acm_20200206_models.DescribeConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeConfigurationResponse:
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
        return acm_20200206_models.DescribeConfigurationResponse().from_map(
            self.do_roarequest('DescribeConfiguration', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/configuration', 'json', req, runtime)
        )

    async def describe_configuration_with_options_async(
        self,
        request: acm_20200206_models.DescribeConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeConfigurationResponse:
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
        return acm_20200206_models.DescribeConfigurationResponse().from_map(
            await self.do_roarequest_async('DescribeConfiguration', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/configuration', 'json', req, runtime)
        )

    def describe_import_file_url(
        self,
        request: acm_20200206_models.DescribeImportFileUrlRequest,
    ) -> acm_20200206_models.DescribeImportFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_import_file_url_with_options(request, headers, runtime)

    async def describe_import_file_url_async(
        self,
        request: acm_20200206_models.DescribeImportFileUrlRequest,
    ) -> acm_20200206_models.DescribeImportFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_import_file_url_with_options_async(request, headers, runtime)

    def describe_import_file_url_with_options(
        self,
        request: acm_20200206_models.DescribeImportFileUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeImportFileUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.DescribeImportFileUrlResponse().from_map(
            self.do_roarequest('DescribeImportFileUrl', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/batch/importFileUrl', 'json', req, runtime)
        )

    async def describe_import_file_url_with_options_async(
        self,
        request: acm_20200206_models.DescribeImportFileUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeImportFileUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.DescribeImportFileUrlResponse().from_map(
            await self.do_roarequest_async('DescribeImportFileUrl', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/batch/importFileUrl', 'json', req, runtime)
        )

    def describe_namespace(
        self,
        request: acm_20200206_models.DescribeNamespaceRequest,
    ) -> acm_20200206_models.DescribeNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_with_options(request, headers, runtime)

    async def describe_namespace_async(
        self,
        request: acm_20200206_models.DescribeNamespaceRequest,
    ) -> acm_20200206_models.DescribeNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespace_with_options_async(request, headers, runtime)

    def describe_namespace_with_options(
        self,
        request: acm_20200206_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.DescribeNamespaceResponse().from_map(
            self.do_roarequest('DescribeNamespace', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/namespace', 'json', req, runtime)
        )

    async def describe_namespace_with_options_async(
        self,
        request: acm_20200206_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.DescribeNamespaceResponse().from_map(
            await self.do_roarequest_async('DescribeNamespace', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/namespace', 'json', req, runtime)
        )

    def describe_namespaces(self) -> acm_20200206_models.DescribeNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespaces_with_options(headers, runtime)

    async def describe_namespaces_async(self) -> acm_20200206_models.DescribeNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespaces_with_options_async(headers, runtime)

    def describe_namespaces_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespacesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return acm_20200206_models.DescribeNamespacesResponse().from_map(
            self.do_roarequest('DescribeNamespaces', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/namespace/list', 'json', req, runtime)
        )

    async def describe_namespaces_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespacesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return acm_20200206_models.DescribeNamespacesResponse().from_map(
            await self.do_roarequest_async('DescribeNamespaces', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/namespace/list', 'json', req, runtime)
        )

    def describe_namespaces_with_create(self) -> acm_20200206_models.DescribeNamespacesWithCreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespaces_with_create_with_options(headers, runtime)

    async def describe_namespaces_with_create_async(self) -> acm_20200206_models.DescribeNamespacesWithCreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespaces_with_create_with_options_async(headers, runtime)

    def describe_namespaces_with_create_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespacesWithCreateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return acm_20200206_models.DescribeNamespacesWithCreateResponse().from_map(
            self.do_roarequest('DescribeNamespacesWithCreate', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/namespace/listWithCreate', 'json', req, runtime)
        )

    async def describe_namespaces_with_create_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeNamespacesWithCreateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return acm_20200206_models.DescribeNamespacesWithCreateResponse().from_map(
            await self.do_roarequest_async('DescribeNamespacesWithCreate', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/namespace/listWithCreate', 'json', req, runtime)
        )

    def describe_trace_by_configuration(
        self,
        request: acm_20200206_models.DescribeTraceByConfigurationRequest,
    ) -> acm_20200206_models.DescribeTraceByConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_trace_by_configuration_with_options(request, headers, runtime)

    async def describe_trace_by_configuration_async(
        self,
        request: acm_20200206_models.DescribeTraceByConfigurationRequest,
    ) -> acm_20200206_models.DescribeTraceByConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_trace_by_configuration_with_options_async(request, headers, runtime)

    def describe_trace_by_configuration_with_options(
        self,
        request: acm_20200206_models.DescribeTraceByConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeTraceByConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.DescribeTraceByConfigurationResponse().from_map(
            self.do_roarequest('DescribeTraceByConfiguration', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/trace/getByConfiguration', 'json', req, runtime)
        )

    async def describe_trace_by_configuration_with_options_async(
        self,
        request: acm_20200206_models.DescribeTraceByConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.DescribeTraceByConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return acm_20200206_models.DescribeTraceByConfigurationResponse().from_map(
            await self.do_roarequest_async('DescribeTraceByConfiguration', '2020-02-06', 'HTTPS', 'GET', 'AK', f'/diamond-ops/pop/trace/getByConfiguration', 'json', req, runtime)
        )

    def update_namespace(
        self,
        request: acm_20200206_models.UpdateNamespaceRequest,
    ) -> acm_20200206_models.UpdateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_with_options(request, headers, runtime)

    async def update_namespace_async(
        self,
        request: acm_20200206_models.UpdateNamespaceRequest,
    ) -> acm_20200206_models.UpdateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_namespace_with_options_async(request, headers, runtime)

    def update_namespace_with_options(
        self,
        request: acm_20200206_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.UpdateNamespaceResponse:
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
        return acm_20200206_models.UpdateNamespaceResponse().from_map(
            self.do_roarequest_with_form('UpdateNamespace', '2020-02-06', 'HTTPS', 'PUT', 'AK', f'/diamond-ops/pop/namespace', 'json', req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: acm_20200206_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> acm_20200206_models.UpdateNamespaceResponse:
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
        return acm_20200206_models.UpdateNamespaceResponse().from_map(
            await self.do_roarequest_with_form_async('UpdateNamespace', '2020-02-06', 'HTTPS', 'PUT', 'AK', f'/diamond-ops/pop/namespace', 'json', req, runtime)
        )
