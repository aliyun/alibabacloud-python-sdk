# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cnip20201201 import models as cnip_20201201_models
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
        self._endpoint = self.get_endpoint('cnip', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_environment(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(uid, headers, runtime)

    async def get_environment_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(uid, headers, runtime)

    def get_environment_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentResponse(),
            self.do_roarequest('GetEnvironment', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}', 'json', req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentResponse(),
            await self.do_roarequest_async('GetEnvironment', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}', 'json', req, runtime)
        )

    def list_product_version_related_component_versions(
        self,
        uid: str,
    ) -> cnip_20201201_models.ListProductVersionRelatedComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_version_related_component_versions_with_options(uid, headers, runtime)

    async def list_product_version_related_component_versions_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.ListProductVersionRelatedComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_version_related_component_versions_with_options_async(uid, headers, runtime)

    def list_product_version_related_component_versions_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListProductVersionRelatedComponentVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionRelatedComponentVersionsResponse(),
            self.do_roarequest('ListProductVersionRelatedComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/component_versions', 'json', req, runtime)
        )

    async def list_product_version_related_component_versions_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListProductVersionRelatedComponentVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionRelatedComponentVersionsResponse(),
            await self.do_roarequest_async('ListProductVersionRelatedComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/component_versions', 'json', req, runtime)
        )

    def get_component_version_children(
        self,
        uid: str,
        version_uid: str,
    ) -> cnip_20201201_models.GetComponentVersionChildrenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_component_version_children_with_options(uid, version_uid, headers, runtime)

    async def get_component_version_children_async(
        self,
        uid: str,
        version_uid: str,
    ) -> cnip_20201201_models.GetComponentVersionChildrenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_component_version_children_with_options_async(uid, version_uid, headers, runtime)

    def get_component_version_children_with_options(
        self,
        uid: str,
        version_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetComponentVersionChildrenResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetComponentVersionChildrenResponse(),
            self.do_roarequest('GetComponentVersionChildren', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/components/{uid}/versions/{version_uid}/children', 'json', req, runtime)
        )

    async def get_component_version_children_with_options_async(
        self,
        uid: str,
        version_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetComponentVersionChildrenResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetComponentVersionChildrenResponse(),
            await self.do_roarequest_async('GetComponentVersionChildren', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/components/{uid}/versions/{version_uid}/children', 'json', req, runtime)
        )

    def get_product_environment(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetProductEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_environment_with_options(uid, headers, runtime)

    async def get_product_environment_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetProductEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_environment_with_options_async(uid, headers, runtime)

    def get_product_environment_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductEnvironmentResponse(),
            self.do_roarequest('GetProductEnvironment', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_envs/{uid}', 'json', req, runtime)
        )

    async def get_product_environment_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductEnvironmentResponse(),
            await self.do_roarequest_async('GetProductEnvironment', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_envs/{uid}', 'json', req, runtime)
        )

    def get_product_version_package(
        self,
        uid: str,
        request: cnip_20201201_models.GetProductVersionPackageRequest,
    ) -> cnip_20201201_models.GetProductVersionPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_package_with_options(uid, request, headers, runtime)

    async def get_product_version_package_async(
        self,
        uid: str,
        request: cnip_20201201_models.GetProductVersionPackageRequest,
    ) -> cnip_20201201_models.GetProductVersionPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_version_package_with_options_async(uid, request, headers, runtime)

    def get_product_version_package_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.GetProductVersionPackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductVersionPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionPackageResponse(),
            self.do_roarequest('GetProductVersionPackage', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/hosting/product_versions/{uid}/packages', 'json', req, runtime)
        )

    async def get_product_version_package_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.GetProductVersionPackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductVersionPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionPackageResponse(),
            await self.do_roarequest_async('GetProductVersionPackage', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/hosting/product_versions/{uid}/packages', 'json', req, runtime)
        )

    def list_alicloud_region(self) -> cnip_20201201_models.ListAlicloudRegionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alicloud_region_with_options(headers, runtime)

    async def list_alicloud_region_async(self) -> cnip_20201201_models.ListAlicloudRegionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alicloud_region_with_options_async(headers, runtime)

    def list_alicloud_region_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListAlicloudRegionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListAlicloudRegionResponse(),
            self.do_roarequest('ListAlicloudRegion', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/alicloud/regions', 'json', req, runtime)
        )

    async def list_alicloud_region_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListAlicloudRegionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListAlicloudRegionResponse(),
            await self.do_roarequest_async('ListAlicloudRegion', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/alicloud/regions', 'json', req, runtime)
        )

    def list_component_versions(
        self,
        uid: str,
        request: cnip_20201201_models.ListComponentVersionsRequest,
    ) -> cnip_20201201_models.ListComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_component_versions_with_options(uid, request, headers, runtime)

    async def list_component_versions_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListComponentVersionsRequest,
    ) -> cnip_20201201_models.ListComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_component_versions_with_options_async(uid, request, headers, runtime)

    def list_component_versions_with_options(
        self,
        uid: str,
        tmp_req: cnip_20201201_models.ListComponentVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListComponentVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.ListComponentVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListComponentVersionsResponse(),
            self.do_roarequest('ListComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/components/{uid}/versions', 'json', req, runtime)
        )

    async def list_component_versions_with_options_async(
        self,
        uid: str,
        tmp_req: cnip_20201201_models.ListComponentVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListComponentVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.ListComponentVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListComponentVersionsResponse(),
            await self.do_roarequest_async('ListComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/components/{uid}/versions', 'json', req, runtime)
        )

    def update_snapshot_instance_join_option_with_batch(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchRequest,
    ) -> cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_instance_join_option_with_batch_with_options(uid, request, headers, runtime)

    async def update_snapshot_instance_join_option_with_batch_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchRequest,
    ) -> cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_snapshot_instance_join_option_with_batch_with_options_async(uid, request, headers, runtime)

    def update_snapshot_instance_join_option_with_batch_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_uids):
            query['instanceUIDs'] = request.instance_uids
        body = {}
        if not UtilClient.is_unset(request.join_snapshot):
            body['joinSnapshot'] = request.join_snapshot
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchResponse(),
            self.do_roarequest('UpdateSnapshotInstanceJoinOptionWithBatch', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/snapshots/{uid}/instances', 'json', req, runtime)
        )

    async def update_snapshot_instance_join_option_with_batch_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_uids):
            query['instanceUIDs'] = request.instance_uids
        body = {}
        if not UtilClient.is_unset(request.join_snapshot):
            body['joinSnapshot'] = request.join_snapshot
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchResponse(),
            await self.do_roarequest_async('UpdateSnapshotInstanceJoinOptionWithBatch', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/snapshots/{uid}/instances', 'json', req, runtime)
        )

    def generate_vendor_config_template(
        self,
        uid: str,
    ) -> cnip_20201201_models.GenerateVendorConfigTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_vendor_config_template_with_options(uid, headers, runtime)

    async def generate_vendor_config_template_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GenerateVendorConfigTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_vendor_config_template_with_options_async(uid, headers, runtime)

    def generate_vendor_config_template_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GenerateVendorConfigTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GenerateVendorConfigTemplateResponse(),
            self.do_roarequest('GenerateVendorConfigTemplate', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/vendorConfigTmpl', 'json', req, runtime)
        )

    async def generate_vendor_config_template_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GenerateVendorConfigTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GenerateVendorConfigTemplateResponse(),
            await self.do_roarequest_async('GenerateVendorConfigTemplate', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/vendorConfigTmpl', 'json', req, runtime)
        )

    def update_product_component(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductComponentRequest,
    ) -> cnip_20201201_models.UpdateProductComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_component_with_options(uid, request, headers, runtime)

    async def update_product_component_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductComponentRequest,
    ) -> cnip_20201201_models.UpdateProductComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_component_with_options_async(uid, request, headers, runtime)

    def update_product_component_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateProductComponentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductComponentResponse(),
            self.do_roarequest('UpdateProductComponent', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/productComponentVersions/{uid}', 'json', req, runtime)
        )

    async def update_product_component_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateProductComponentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductComponentResponse(),
            await self.do_roarequest_async('UpdateProductComponent', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/productComponentVersions/{uid}', 'json', req, runtime)
        )

    def update_environment_nodes(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentNodesRequest,
    ) -> cnip_20201201_models.UpdateEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_nodes_with_options(uid, request, headers, runtime)

    async def update_environment_nodes_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentNodesRequest,
    ) -> cnip_20201201_models.UpdateEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_nodes_with_options_async(uid, request, headers, runtime)

    def update_environment_nodes_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateEnvironmentNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.data_disk_2):
            body['dataDisk2'] = request.data_disk_2
        if not UtilClient.is_unset(request.env_uid):
            body['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.node_ip):
            body['nodeIP'] = request.node_ip
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.system_disk_2):
            body['systemDisk2'] = request.system_disk_2
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentNodesResponse(),
            self.do_roarequest('UpdateEnvironmentNodes', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/environmentnodes/{uid}', 'json', req, runtime)
        )

    async def update_environment_nodes_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateEnvironmentNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.data_disk_2):
            body['dataDisk2'] = request.data_disk_2
        if not UtilClient.is_unset(request.env_uid):
            body['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.node_ip):
            body['nodeIP'] = request.node_ip
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.system_disk_2):
            body['systemDisk2'] = request.system_disk_2
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentNodesResponse(),
            await self.do_roarequest_async('UpdateEnvironmentNodes', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/environmentnodes/{uid}', 'json', req, runtime)
        )

    def list_environment_packages(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentPackagesRequest,
    ) -> cnip_20201201_models.ListEnvironmentPackagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_packages_with_options(uid, request, headers, runtime)

    async def list_environment_packages_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentPackagesRequest,
    ) -> cnip_20201201_models.ListEnvironmentPackagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environment_packages_with_options_async(uid, request, headers, runtime)

    def list_environment_packages_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentPackagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentPackagesResponse(),
            self.do_roarequest('ListEnvironmentPackages', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/packages', 'json', req, runtime)
        )

    async def list_environment_packages_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentPackagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentPackagesResponse(),
            await self.do_roarequest_async('ListEnvironmentPackages', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/packages', 'json', req, runtime)
        )

    def create_environment(
        self,
        request: cnip_20201201_models.CreateEnvironmentRequest,
    ) -> cnip_20201201_models.CreateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateEnvironmentHeaders()
        return self.create_environment_with_options(request, headers, runtime)

    async def create_environment_async(
        self,
        request: cnip_20201201_models.CreateEnvironmentRequest,
    ) -> cnip_20201201_models.CreateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateEnvironmentHeaders()
        return await self.create_environment_with_options_async(request, headers, runtime)

    def create_environment_with_options(
        self,
        request: cnip_20201201_models.CreateEnvironmentRequest,
        headers: cnip_20201201_models.CreateEnvironmentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentResponse(),
            self.do_roarequest('CreateEnvironment', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments', 'json', req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: cnip_20201201_models.CreateEnvironmentRequest,
        headers: cnip_20201201_models.CreateEnvironmentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentResponse(),
            await self.do_roarequest_async('CreateEnvironment', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments', 'json', req, runtime)
        )

    def get_environment_log(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetEnvironmentLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_log_with_options(uid, headers, runtime)

    async def get_environment_log_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetEnvironmentLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_log_with_options_async(uid, headers, runtime)

    def get_environment_log_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetEnvironmentLogResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentLogResponse(),
            self.do_roarequest('GetEnvironmentLog', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/envLogs/{uid}', 'json', req, runtime)
        )

    async def get_environment_log_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetEnvironmentLogResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentLogResponse(),
            await self.do_roarequest_async('GetEnvironmentLog', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/envLogs/{uid}', 'json', req, runtime)
        )

    def list_environment_node(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentNodeRequest,
    ) -> cnip_20201201_models.ListEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_node_with_options(uid, request, headers, runtime)

    async def list_environment_node_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentNodeRequest,
    ) -> cnip_20201201_models.ListEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environment_node_with_options_async(uid, request, headers, runtime)

    def list_environment_node_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.node_ip):
            query['nodeIp'] = request.node_ip
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentNodeResponse(),
            self.do_roarequest('ListEnvironmentNode', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/nodes', 'json', req, runtime)
        )

    async def list_environment_node_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.node_ip):
            query['nodeIp'] = request.node_ip
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentNodeResponse(),
            await self.do_roarequest_async('ListEnvironmentNode', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/nodes', 'json', req, runtime)
        )

    def list_product_version_related_foundation_component_versions(
        self,
        uid: str,
    ) -> cnip_20201201_models.ListProductVersionRelatedFoundationComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_version_related_foundation_component_versions_with_options(uid, headers, runtime)

    async def list_product_version_related_foundation_component_versions_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.ListProductVersionRelatedFoundationComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_version_related_foundation_component_versions_with_options_async(uid, headers, runtime)

    def list_product_version_related_foundation_component_versions_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListProductVersionRelatedFoundationComponentVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionRelatedFoundationComponentVersionsResponse(),
            self.do_roarequest('ListProductVersionRelatedFoundationComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/foundation/component_versions', 'json', req, runtime)
        )

    async def list_product_version_related_foundation_component_versions_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListProductVersionRelatedFoundationComponentVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionRelatedFoundationComponentVersionsResponse(),
            await self.do_roarequest_async('ListProductVersionRelatedFoundationComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/foundation/component_versions', 'json', req, runtime)
        )

    def sync_component(
        self,
        request: cnip_20201201_models.SyncComponentRequest,
    ) -> cnip_20201201_models.SyncComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_component_with_options(request, headers, runtime)

    async def sync_component_async(
        self,
        request: cnip_20201201_models.SyncComponentRequest,
    ) -> cnip_20201201_models.SyncComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sync_component_with_options_async(request, headers, runtime)

    def sync_component_with_options(
        self,
        request: cnip_20201201_models.SyncComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.SyncComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.SyncComponentResponse(),
            self.do_roarequest('SyncComponent', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/oss/sync/apps', 'json', req, runtime)
        )

    async def sync_component_with_options_async(
        self,
        request: cnip_20201201_models.SyncComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.SyncComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.SyncComponentResponse(),
            await self.do_roarequest_async('SyncComponent', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/oss/sync/apps', 'json', req, runtime)
        )

    def update_component_to_product(
        self,
        id: str,
        version_id: str,
        product_component_version_relation_id: str,
        request: cnip_20201201_models.UpdateComponentToProductRequest,
    ) -> cnip_20201201_models.UpdateComponentToProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_component_to_product_with_options(id, version_id, product_component_version_relation_id, request, headers, runtime)

    async def update_component_to_product_async(
        self,
        id: str,
        version_id: str,
        product_component_version_relation_id: str,
        request: cnip_20201201_models.UpdateComponentToProductRequest,
    ) -> cnip_20201201_models.UpdateComponentToProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_component_to_product_with_options_async(id, version_id, product_component_version_relation_id, request, headers, runtime)

    def update_component_to_product_with_options(
        self,
        id: str,
        version_id: str,
        product_component_version_relation_id: str,
        request: cnip_20201201_models.UpdateComponentToProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateComponentToProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_version_id):
            query['componentVersionID'] = request.component_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateComponentToProductResponse(),
            self.do_roarequest('UpdateComponentToProduct', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/componentVersionRelations/{product_component_version_relation_id}', 'json', req, runtime)
        )

    async def update_component_to_product_with_options_async(
        self,
        id: str,
        version_id: str,
        product_component_version_relation_id: str,
        request: cnip_20201201_models.UpdateComponentToProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateComponentToProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_version_id):
            query['componentVersionID'] = request.component_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateComponentToProductResponse(),
            await self.do_roarequest_async('UpdateComponentToProduct', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/componentVersionRelations/{product_component_version_relation_id}', 'json', req, runtime)
        )

    def create_environment_node(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentNodeRequest,
    ) -> cnip_20201201_models.CreateEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_node_with_options(uid, request, headers, runtime)

    async def create_environment_node_async(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentNodeRequest,
    ) -> cnip_20201201_models.CreateEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_node_with_options_async(uid, request, headers, runtime)

    def create_environment_node_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.os):
            body['os'] = request.os
        if not UtilClient.is_unset(request.private_ip):
            body['privateIP'] = request.private_ip
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentNodeResponse(),
            self.do_roarequest('CreateEnvironmentNode', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/nodes', 'json', req, runtime)
        )

    async def create_environment_node_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.os):
            body['os'] = request.os
        if not UtilClient.is_unset(request.private_ip):
            body['privateIP'] = request.private_ip
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentNodeResponse(),
            await self.do_roarequest_async('CreateEnvironmentNode', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/nodes', 'json', req, runtime)
        )

    def get_component(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_component_with_options(uid, headers, runtime)

    async def get_component_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_component_with_options_async(uid, headers, runtime)

    def get_component_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetComponentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetComponentResponse(),
            self.do_roarequest('GetComponent', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/components/{uid}', 'json', req, runtime)
        )

    async def get_component_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetComponentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetComponentResponse(),
            await self.do_roarequest_async('GetComponent', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/components/{uid}', 'json', req, runtime)
        )

    def list_foundation_version_related_component_versions(
        self,
        uid: str,
    ) -> cnip_20201201_models.ListFoundationVersionRelatedComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_version_related_component_versions_with_options(uid, headers, runtime)

    async def list_foundation_version_related_component_versions_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.ListFoundationVersionRelatedComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_foundation_version_related_component_versions_with_options_async(uid, headers, runtime)

    def list_foundation_version_related_component_versions_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListFoundationVersionRelatedComponentVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListFoundationVersionRelatedComponentVersionsResponse(),
            self.do_roarequest('ListFoundationVersionRelatedComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/foundation/versions/{uid}/component_versions', 'json', req, runtime)
        )

    async def list_foundation_version_related_component_versions_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListFoundationVersionRelatedComponentVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListFoundationVersionRelatedComponentVersionsResponse(),
            await self.do_roarequest_async('ListFoundationVersionRelatedComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/foundation/versions/{uid}/component_versions', 'json', req, runtime)
        )

    def get_snapshot(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_with_options(uid, headers, runtime)

    async def get_snapshot_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_snapshot_with_options_async(uid, headers, runtime)

    def get_snapshot_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetSnapshotResponse(),
            self.do_roarequest('GetSnapshot', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/snapshots/{uid}', 'json', req, runtime)
        )

    async def get_snapshot_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetSnapshotResponse(),
            await self.do_roarequest_async('GetSnapshot', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/snapshots/{uid}', 'json', req, runtime)
        )

    def get_license(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_license_with_options(uid, headers, runtime)

    async def get_license_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_license_with_options_async(uid, headers, runtime)

    def get_license_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetLicenseResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetLicenseResponse(),
            self.do_roarequest('GetLicense', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/licenses', 'json', req, runtime)
        )

    async def get_license_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetLicenseResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetLicenseResponse(),
            await self.do_roarequest_async('GetLicense', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/licenses', 'json', req, runtime)
        )

    def create_latest_product_version(
        self,
        uid: str,
        version_uid: str,
    ) -> cnip_20201201_models.CreateLatestProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateLatestProductVersionHeaders()
        return self.create_latest_product_version_with_options(uid, version_uid, headers, runtime)

    async def create_latest_product_version_async(
        self,
        uid: str,
        version_uid: str,
    ) -> cnip_20201201_models.CreateLatestProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateLatestProductVersionHeaders()
        return await self.create_latest_product_version_with_options_async(uid, version_uid, headers, runtime)

    def create_latest_product_version_with_options(
        self,
        uid: str,
        version_uid: str,
        headers: cnip_20201201_models.CreateLatestProductVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateLatestProductVersionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateLatestProductVersionResponse(),
            self.do_roarequest('CreateLatestProductVersion', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/products/{uid}/versions/{version_uid}', 'json', req, runtime)
        )

    async def create_latest_product_version_with_options_async(
        self,
        uid: str,
        version_uid: str,
        headers: cnip_20201201_models.CreateLatestProductVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateLatestProductVersionResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateLatestProductVersionResponse(),
            await self.do_roarequest_async('CreateLatestProductVersion', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/products/{uid}/versions/{version_uid}', 'json', req, runtime)
        )

    def list_alicloud_vpc(
        self,
        regionid: str,
    ) -> cnip_20201201_models.ListAlicloudVPCResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alicloud_vpcwith_options(regionid, headers, runtime)

    async def list_alicloud_vpc_async(
        self,
        regionid: str,
    ) -> cnip_20201201_models.ListAlicloudVPCResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alicloud_vpcwith_options_async(regionid, headers, runtime)

    def list_alicloud_vpcwith_options(
        self,
        regionid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListAlicloudVPCResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListAlicloudVPCResponse(),
            self.do_roarequest('ListAlicloudVPC', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/alicloud/regions/{regionid}/vpcs', 'json', req, runtime)
        )

    async def list_alicloud_vpcwith_options_async(
        self,
        regionid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListAlicloudVPCResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListAlicloudVPCResponse(),
            await self.do_roarequest_async('ListAlicloudVPC', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/alicloud/regions/{regionid}/vpcs', 'json', req, runtime)
        )

    def create_product(
        self,
        request: cnip_20201201_models.CreateProductRequest,
    ) -> cnip_20201201_models.CreateProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateProductHeaders()
        return self.create_product_with_options(request, headers, runtime)

    async def create_product_async(
        self,
        request: cnip_20201201_models.CreateProductRequest,
    ) -> cnip_20201201_models.CreateProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateProductHeaders()
        return await self.create_product_with_options_async(request, headers, runtime)

    def create_product_with_options(
        self,
        request: cnip_20201201_models.CreateProductRequest,
        headers: cnip_20201201_models.CreateProductHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.prometheus_uid):
            body['prometheusUID'] = request.prometheus_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateProductResponse(),
            self.do_roarequest('CreateProduct', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/products', 'json', req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: cnip_20201201_models.CreateProductRequest,
        headers: cnip_20201201_models.CreateProductHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.prometheus_uid):
            body['prometheusUID'] = request.prometheus_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateProductResponse(),
            await self.do_roarequest_async('CreateProduct', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/products', 'json', req, runtime)
        )

    def get_product_environments(
        self,
        request: cnip_20201201_models.GetProductEnvironmentsRequest,
    ) -> cnip_20201201_models.GetProductEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_environments_with_options(request, headers, runtime)

    async def get_product_environments_async(
        self,
        request: cnip_20201201_models.GetProductEnvironmentsRequest,
    ) -> cnip_20201201_models.GetProductEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_environments_with_options_async(request, headers, runtime)

    def get_product_environments_with_options(
        self,
        tmp_req: cnip_20201201_models.GetProductEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductEnvironmentsResponse:
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.GetProductEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.product_uid):
            query['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.env_type):
            query['envType'] = request.env_type
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductEnvironmentsResponse(),
            self.do_roarequest('GetProductEnvironments', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_envs', 'json', req, runtime)
        )

    async def get_product_environments_with_options_async(
        self,
        tmp_req: cnip_20201201_models.GetProductEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductEnvironmentsResponse:
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.GetProductEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.product_uid):
            query['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.env_type):
            query['envType'] = request.env_type
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductEnvironmentsResponse(),
            await self.do_roarequest_async('GetProductEnvironments', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_envs', 'json', req, runtime)
        )

    def delete_component(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_component_with_options(uid, headers, runtime)

    async def delete_component_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_component_with_options_async(uid, headers, runtime)

    def delete_component_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteComponentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteComponentResponse(),
            self.do_roarequest('DeleteComponent', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/integration/api/v1/components/{uid}', 'json', req, runtime)
        )

    async def delete_component_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteComponentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteComponentResponse(),
            await self.do_roarequest_async('DeleteComponent', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/integration/api/v1/components/{uid}', 'json', req, runtime)
        )

    def delete_product_component(
        self,
        id: str,
        version_id: str,
        product_component_version_relation_id: str,
    ) -> cnip_20201201_models.DeleteProductComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_component_with_options(id, version_id, product_component_version_relation_id, headers, runtime)

    async def delete_product_component_async(
        self,
        id: str,
        version_id: str,
        product_component_version_relation_id: str,
    ) -> cnip_20201201_models.DeleteProductComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_component_with_options_async(id, version_id, product_component_version_relation_id, headers, runtime)

    def delete_product_component_with_options(
        self,
        id: str,
        version_id: str,
        product_component_version_relation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteProductComponentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteProductComponentResponse(),
            self.do_roarequest('DeleteProductComponent', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/componentVersionRelations/{product_component_version_relation_id}', 'json', req, runtime)
        )

    async def delete_product_component_with_options_async(
        self,
        id: str,
        version_id: str,
        product_component_version_relation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteProductComponentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteProductComponentResponse(),
            await self.do_roarequest_async('DeleteProductComponent', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/componentVersionRelations/{product_component_version_relation_id}', 'json', req, runtime)
        )

    def create_environment_with_snapshot(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentWithSnapshotRequest,
    ) -> cnip_20201201_models.CreateEnvironmentWithSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_with_snapshot_with_options(uid, request, headers, runtime)

    async def create_environment_with_snapshot_async(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentWithSnapshotRequest,
    ) -> cnip_20201201_models.CreateEnvironmentWithSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_with_snapshot_with_options_async(uid, request, headers, runtime)

    def create_environment_with_snapshot_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentWithSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentWithSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_desc):
            body['environmentDesc'] = request.environment_desc
        if not UtilClient.is_unset(request.environment_name):
            body['environmentName'] = request.environment_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentWithSnapshotResponse(),
            self.do_roarequest('CreateEnvironmentWithSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/snapshots/{uid}/environments', 'json', req, runtime)
        )

    async def create_environment_with_snapshot_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentWithSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentWithSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_desc):
            body['environmentDesc'] = request.environment_desc
        if not UtilClient.is_unset(request.environment_name):
            body['environmentName'] = request.environment_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentWithSnapshotResponse(),
            await self.do_roarequest_async('CreateEnvironmentWithSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/snapshots/{uid}/environments', 'json', req, runtime)
        )

    def delete_environment(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(uid, headers, runtime)

    async def delete_environment_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(uid, headers, runtime)

    def delete_environment_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentResponse(),
            self.do_roarequest('DeleteEnvironment', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/api/v1/environments/{uid}', 'json', req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentResponse(),
            await self.do_roarequest_async('DeleteEnvironment', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/api/v1/environments/{uid}', 'json', req, runtime)
        )

    def update_product_version(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductVersionRequest,
    ) -> cnip_20201201_models.UpdateProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_version_with_options(uid, request, headers, runtime)

    async def update_product_version_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductVersionRequest,
    ) -> cnip_20201201_models.UpdateProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_version_with_options_async(uid, request, headers, runtime)

    def update_product_version_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compatible_versions):
            body['compatibleVersions'] = request.compatible_versions
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductVersionResponse(),
            self.do_roarequest('UpdateProductVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/product_versions/{uid}', 'json', req, runtime)
        )

    async def update_product_version_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compatible_versions):
            body['compatibleVersions'] = request.compatible_versions
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductVersionResponse(),
            await self.do_roarequest_async('UpdateProductVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/product_versions/{uid}', 'json', req, runtime)
        )

    def get_children_component_version_parameters_list(
        self,
        id: str,
        version_id: str,
        request: cnip_20201201_models.GetChildrenComponentVersionParametersListRequest,
    ) -> cnip_20201201_models.GetChildrenComponentVersionParametersListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_children_component_version_parameters_list_with_options(id, version_id, request, headers, runtime)

    async def get_children_component_version_parameters_list_async(
        self,
        id: str,
        version_id: str,
        request: cnip_20201201_models.GetChildrenComponentVersionParametersListRequest,
    ) -> cnip_20201201_models.GetChildrenComponentVersionParametersListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_children_component_version_parameters_list_with_options_async(id, version_id, request, headers, runtime)

    def get_children_component_version_parameters_list_with_options(
        self,
        id: str,
        version_id: str,
        request: cnip_20201201_models.GetChildrenComponentVersionParametersListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetChildrenComponentVersionParametersListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_id):
            query['relation_id'] = request.relation_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetChildrenComponentVersionParametersListResponse(),
            self.do_roarequest('GetChildrenComponentVersionParametersList', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/components/{id}/versions/{version_id}/parameters', 'json', req, runtime)
        )

    async def get_children_component_version_parameters_list_with_options_async(
        self,
        id: str,
        version_id: str,
        request: cnip_20201201_models.GetChildrenComponentVersionParametersListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetChildrenComponentVersionParametersListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_id):
            query['relation_id'] = request.relation_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetChildrenComponentVersionParametersListResponse(),
            await self.do_roarequest_async('GetChildrenComponentVersionParametersList', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/components/{id}/versions/{version_id}/parameters', 'json', req, runtime)
        )

    def create_snapshot(
        self,
        request: cnip_20201201_models.CreateSnapshotRequest,
    ) -> cnip_20201201_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_snapshot_with_options(request, headers, runtime)

    async def create_snapshot_async(
        self,
        request: cnip_20201201_models.CreateSnapshotRequest,
    ) -> cnip_20201201_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_snapshot_with_options_async(request, headers, runtime)

    def create_snapshot_with_options(
        self,
        request: cnip_20201201_models.CreateSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_desc):
            body['productVersionDesc'] = request.product_version_desc
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.vpcid):
            body['vpcid'] = request.vpcid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateSnapshotResponse(),
            self.do_roarequest('CreateSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/snapshots', 'json', req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: cnip_20201201_models.CreateSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_desc):
            body['productVersionDesc'] = request.product_version_desc
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.vpcid):
            body['vpcid'] = request.vpcid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateSnapshotResponse(),
            await self.do_roarequest_async('CreateSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/snapshots', 'json', req, runtime)
        )

    def get_latest_version_differences(
        self,
        id: str,
        version_id: str,
        request: cnip_20201201_models.GetLatestVersionDifferencesRequest,
    ) -> cnip_20201201_models.GetLatestVersionDifferencesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_latest_version_differences_with_options(id, version_id, request, headers, runtime)

    async def get_latest_version_differences_async(
        self,
        id: str,
        version_id: str,
        request: cnip_20201201_models.GetLatestVersionDifferencesRequest,
    ) -> cnip_20201201_models.GetLatestVersionDifferencesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_latest_version_differences_with_options_async(id, version_id, request, headers, runtime)

    def get_latest_version_differences_with_options(
        self,
        id: str,
        version_id: str,
        request: cnip_20201201_models.GetLatestVersionDifferencesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetLatestVersionDifferencesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_version_id):
            query['preVersionID'] = request.pre_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetLatestVersionDifferencesResponse(),
            self.do_roarequest('GetLatestVersionDifferences', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/differences', 'json', req, runtime)
        )

    async def get_latest_version_differences_with_options_async(
        self,
        id: str,
        version_id: str,
        request: cnip_20201201_models.GetLatestVersionDifferencesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetLatestVersionDifferencesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_version_id):
            query['preVersionID'] = request.pre_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetLatestVersionDifferencesResponse(),
            await self.do_roarequest_async('GetLatestVersionDifferences', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/differences', 'json', req, runtime)
        )

    def delete_environment_node(
        self,
        uid: str,
        request: cnip_20201201_models.DeleteEnvironmentNodeRequest,
    ) -> cnip_20201201_models.DeleteEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_node_with_options(uid, request, headers, runtime)

    async def delete_environment_node_async(
        self,
        uid: str,
        request: cnip_20201201_models.DeleteEnvironmentNodeRequest,
    ) -> cnip_20201201_models.DeleteEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_node_with_options_async(uid, request, headers, runtime)

    def delete_environment_node_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.DeleteEnvironmentNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteEnvironmentNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_uid):
            query['envUID'] = request.env_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentNodeResponse(),
            self.do_roarequest('DeleteEnvironmentNode', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/api/v1/environmentnodes/{uid}', 'json', req, runtime)
        )

    async def delete_environment_node_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.DeleteEnvironmentNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteEnvironmentNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_uid):
            query['envUID'] = request.env_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentNodeResponse(),
            await self.do_roarequest_async('DeleteEnvironmentNode', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/api/v1/environmentnodes/{uid}', 'json', req, runtime)
        )

    def apply_component(
        self,
        request: cnip_20201201_models.ApplyComponentRequest,
    ) -> cnip_20201201_models.ApplyComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_component_with_options(request, headers, runtime)

    async def apply_component_async(
        self,
        request: cnip_20201201_models.ApplyComponentRequest,
    ) -> cnip_20201201_models.ApplyComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.apply_component_with_options_async(request, headers, runtime)

    def apply_component_with_options(
        self,
        request: cnip_20201201_models.ApplyComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ApplyComponentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_version):
            body['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.component_class):
            body['componentClass'] = request.component_class
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.documents):
            body['documents'] = request.documents
        if not UtilClient.is_unset(request.images_mapping):
            body['imagesMapping'] = request.images_mapping
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        if not UtilClient.is_unset(request.orchestration_type):
            body['orchestrationType'] = request.orchestration_type
        if not UtilClient.is_unset(request.orchestration_values):
            body['orchestrationValues'] = request.orchestration_values
        if not UtilClient.is_unset(request.package_url):
            body['packageURL'] = request.package_url
        if not UtilClient.is_unset(request.parent_component):
            body['parentComponent'] = request.parent_component
        if not UtilClient.is_unset(request.platforms):
            body['platforms'] = request.platforms
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.public):
            body['public'] = request.public
        if not UtilClient.is_unset(request.readme):
            body['readme'] = request.readme
        if not UtilClient.is_unset(request.resources):
            body['resources'] = request.resources
        if not UtilClient.is_unset(request.singleton):
            body['singleton'] = request.singleton
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ApplyComponentResponse(),
            self.do_roarequest('ApplyComponent', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/apps', 'json', req, runtime)
        )

    async def apply_component_with_options_async(
        self,
        request: cnip_20201201_models.ApplyComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ApplyComponentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_version):
            body['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.component_class):
            body['componentClass'] = request.component_class
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.documents):
            body['documents'] = request.documents
        if not UtilClient.is_unset(request.images_mapping):
            body['imagesMapping'] = request.images_mapping
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        if not UtilClient.is_unset(request.orchestration_type):
            body['orchestrationType'] = request.orchestration_type
        if not UtilClient.is_unset(request.orchestration_values):
            body['orchestrationValues'] = request.orchestration_values
        if not UtilClient.is_unset(request.package_url):
            body['packageURL'] = request.package_url
        if not UtilClient.is_unset(request.parent_component):
            body['parentComponent'] = request.parent_component
        if not UtilClient.is_unset(request.platforms):
            body['platforms'] = request.platforms
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.public):
            body['public'] = request.public
        if not UtilClient.is_unset(request.readme):
            body['readme'] = request.readme
        if not UtilClient.is_unset(request.resources):
            body['resources'] = request.resources
        if not UtilClient.is_unset(request.singleton):
            body['singleton'] = request.singleton
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ApplyComponentResponse(),
            await self.do_roarequest_async('ApplyComponent', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/apps', 'json', req, runtime)
        )

    def get_snapshot_instances(
        self,
        uid: str,
        request: cnip_20201201_models.GetSnapshotInstancesRequest,
    ) -> cnip_20201201_models.GetSnapshotInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_instances_with_options(uid, request, headers, runtime)

    async def get_snapshot_instances_async(
        self,
        uid: str,
        request: cnip_20201201_models.GetSnapshotInstancesRequest,
    ) -> cnip_20201201_models.GetSnapshotInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_snapshot_instances_with_options_async(uid, request, headers, runtime)

    def get_snapshot_instances_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.GetSnapshotInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetSnapshotInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.sort_key):
            query['sortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_direct):
            query['sortDirect'] = request.sort_direct
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetSnapshotInstancesResponse(),
            self.do_roarequest('GetSnapshotInstances', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/snapshots/{uid}/instances', 'json', req, runtime)
        )

    async def get_snapshot_instances_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.GetSnapshotInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetSnapshotInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.sort_key):
            query['sortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_direct):
            query['sortDirect'] = request.sort_direct
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetSnapshotInstancesResponse(),
            await self.do_roarequest_async('GetSnapshotInstances', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/snapshots/{uid}/instances', 'json', req, runtime)
        )

    def list_environments(
        self,
        request: cnip_20201201_models.ListEnvironmentsRequest,
    ) -> cnip_20201201_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(request, headers, runtime)

    async def list_environments_async(
        self,
        request: cnip_20201201_models.ListEnvironmentsRequest,
    ) -> cnip_20201201_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(request, headers, runtime)

    def list_environments_with_options(
        self,
        request: cnip_20201201_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.instance_status):
            query['instanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.vendor_type):
            query['vendorType'] = request.vendor_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentsResponse(),
            self.do_roarequest('ListEnvironments', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments', 'json', req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        request: cnip_20201201_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.instance_status):
            query['instanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.vendor_type):
            query['vendorType'] = request.vendor_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentsResponse(),
            await self.do_roarequest_async('ListEnvironments', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments', 'json', req, runtime)
        )

    def check_slr(
        self,
        request: cnip_20201201_models.CheckSLRRequest,
    ) -> cnip_20201201_models.CheckSLRResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_slrwith_options(request, headers, runtime)

    async def check_slr_async(
        self,
        request: cnip_20201201_models.CheckSLRRequest,
    ) -> cnip_20201201_models.CheckSLRResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_slrwith_options_async(request, headers, runtime)

    def check_slrwith_options(
        self,
        request: cnip_20201201_models.CheckSLRRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CheckSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CheckSLRResponse(),
            self.do_roarequest('CheckSLR', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/slr', 'json', req, runtime)
        )

    async def check_slrwith_options_async(
        self,
        request: cnip_20201201_models.CheckSLRRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CheckSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CheckSLRResponse(),
            await self.do_roarequest_async('CheckSLR', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/slr', 'json', req, runtime)
        )

    def update_product(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductRequest,
    ) -> cnip_20201201_models.UpdateProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_with_options(uid, request, headers, runtime)

    async def update_product_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductRequest,
    ) -> cnip_20201201_models.UpdateProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_with_options_async(uid, request, headers, runtime)

    def update_product_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.description
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductResponse(),
            self.do_roarequest('UpdateProduct', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/products/{uid}', 'json', req, runtime)
        )

    async def update_product_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.description
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductResponse(),
            await self.do_roarequest_async('UpdateProduct', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/products/{uid}', 'json', req, runtime)
        )

    def apply_components(
        self,
        request: cnip_20201201_models.ApplyComponentsRequest,
    ) -> cnip_20201201_models.ApplyComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_components_with_options(request, headers, runtime)

    async def apply_components_async(
        self,
        request: cnip_20201201_models.ApplyComponentsRequest,
    ) -> cnip_20201201_models.ApplyComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.apply_components_with_options_async(request, headers, runtime)

    def apply_components_with_options(
        self,
        request: cnip_20201201_models.ApplyComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ApplyComponentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.children_list):
            body['childrenList'] = request.children_list
        if not UtilClient.is_unset(request.component):
            body['component'] = request.component
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ApplyComponentsResponse(),
            self.do_roarequest('ApplyComponents', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/components', 'json', req, runtime)
        )

    async def apply_components_with_options_async(
        self,
        request: cnip_20201201_models.ApplyComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ApplyComponentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.children_list):
            body['childrenList'] = request.children_list
        if not UtilClient.is_unset(request.component):
            body['component'] = request.component
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ApplyComponentsResponse(),
            await self.do_roarequest_async('ApplyComponents', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/components', 'json', req, runtime)
        )

    def create_package_config(
        self,
        uid: str,
    ) -> cnip_20201201_models.CreatePackageConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_package_config_with_options(uid, headers, runtime)

    async def create_package_config_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.CreatePackageConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_package_config_with_options_async(uid, headers, runtime)

    def create_package_config_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreatePackageConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreatePackageConfigResponse(),
            self.do_roarequest('CreatePackageConfig', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/package_config', 'json', req, runtime)
        )

    async def create_package_config_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreatePackageConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreatePackageConfigResponse(),
            await self.do_roarequest_async('CreatePackageConfig', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/package_config', 'json', req, runtime)
        )

    def add_product_component(
        self,
        id: str,
        version_id: str,
        component_version_id: str,
        client_token: str,
        request: cnip_20201201_models.AddProductComponentRequest,
    ) -> cnip_20201201_models.AddProductComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_product_component_with_options(id, version_id, component_version_id, client_token, request, headers, runtime)

    async def add_product_component_async(
        self,
        id: str,
        version_id: str,
        component_version_id: str,
        client_token: str,
        request: cnip_20201201_models.AddProductComponentRequest,
    ) -> cnip_20201201_models.AddProductComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_product_component_with_options_async(id, version_id, component_version_id, client_token, request, headers, runtime)

    def add_product_component_with_options(
        self,
        id: str,
        version_id: str,
        component_version_id: str,
        client_token: str,
        request: cnip_20201201_models.AddProductComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.AddProductComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.release_name
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddProductComponentResponse(),
            self.do_roarequest('AddProductComponent', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/componentVersions/{component_version_id}', 'json', req, runtime)
        )

    async def add_product_component_with_options_async(
        self,
        id: str,
        version_id: str,
        component_version_id: str,
        client_token: str,
        request: cnip_20201201_models.AddProductComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.AddProductComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.release_name
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddProductComponentResponse(),
            await self.do_roarequest_async('AddProductComponent', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/componentVersions/{component_version_id}', 'json', req, runtime)
        )

    def delete_snapshot(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_snapshot_with_options(uid, headers, runtime)

    async def delete_snapshot_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_snapshot_with_options_async(uid, headers, runtime)

    def delete_snapshot_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteSnapshotResponse(),
            self.do_roarequest('DeleteSnapshot', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/api/v1/snapshots/{uid}', 'json', req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteSnapshotResponse(),
            await self.do_roarequest_async('DeleteSnapshot', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/api/v1/snapshots/{uid}', 'json', req, runtime)
        )

    def list_environments_with_snapshot(
        self,
        uid: str,
    ) -> cnip_20201201_models.ListEnvironmentsWithSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_snapshot_with_options(uid, headers, runtime)

    async def list_environments_with_snapshot_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.ListEnvironmentsWithSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_snapshot_with_options_async(uid, headers, runtime)

    def list_environments_with_snapshot_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentsWithSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentsWithSnapshotResponse(),
            self.do_roarequest('ListEnvironmentsWithSnapshot', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/snapshots/{uid}/environments', 'json', req, runtime)
        )

    async def list_environments_with_snapshot_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentsWithSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentsWithSnapshotResponse(),
            await self.do_roarequest_async('ListEnvironmentsWithSnapshot', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/snapshots/{uid}/environments', 'json', req, runtime)
        )

    def get_environment_node(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_node_with_options(uid, headers, runtime)

    async def get_environment_node_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_node_with_options_async(uid, headers, runtime)

    def get_environment_node_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetEnvironmentNodeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentNodeResponse(),
            self.do_roarequest('GetEnvironmentNode', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environmentnodes/{uid}', 'json', req, runtime)
        )

    async def get_environment_node_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetEnvironmentNodeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentNodeResponse(),
            await self.do_roarequest_async('GetEnvironmentNode', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environmentnodes/{uid}', 'json', req, runtime)
        )

    def update_snapshot(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotRequest,
    ) -> cnip_20201201_models.UpdateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_with_options(uid, request, headers, runtime)

    async def update_snapshot_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotRequest,
    ) -> cnip_20201201_models.UpdateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_snapshot_with_options_async(uid, request, headers, runtime)

    def update_snapshot_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_desc):
            body['productVersionDesc'] = request.product_version_desc
        if not UtilClient.is_unset(request.update_key):
            body['updateKey'] = request.update_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotResponse(),
            self.do_roarequest('UpdateSnapshot', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/snapshots/{uid}', 'json', req, runtime)
        )

    async def update_snapshot_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_desc):
            body['productVersionDesc'] = request.product_version_desc
        if not UtilClient.is_unset(request.update_key):
            body['updateKey'] = request.update_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotResponse(),
            await self.do_roarequest_async('UpdateSnapshot', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/snapshots/{uid}', 'json', req, runtime)
        )

    def create_environment_and_generate_vendor_config(
        self,
        request: cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigRequest,
    ) -> cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigHeaders()
        return self.create_environment_and_generate_vendor_config_with_options(request, headers, runtime)

    async def create_environment_and_generate_vendor_config_async(
        self,
        request: cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigRequest,
    ) -> cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigHeaders()
        return await self.create_environment_and_generate_vendor_config_with_options_async(request, headers, runtime)

    def create_environment_and_generate_vendor_config_with_options(
        self,
        request: cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigRequest,
        headers: cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env_uid):
            body['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigResponse(),
            self.do_roarequest('CreateEnvironmentAndGenerateVendorConfig', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/product_envs/vendor_config', 'json', req, runtime)
        )

    async def create_environment_and_generate_vendor_config_with_options_async(
        self,
        request: cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigRequest,
        headers: cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env_uid):
            body['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigResponse(),
            await self.do_roarequest_async('CreateEnvironmentAndGenerateVendorConfig', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/product_envs/vendor_config', 'json', req, runtime)
        )

    def create_environment_snapshot(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentSnapshotRequest,
    ) -> cnip_20201201_models.CreateEnvironmentSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_snapshot_with_options(uid, request, headers, runtime)

    async def create_environment_snapshot_async(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentSnapshotRequest,
    ) -> cnip_20201201_models.CreateEnvironmentSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_snapshot_with_options_async(uid, request, headers, runtime)

    def create_environment_snapshot_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentSnapshotResponse(),
            self.do_roarequest('CreateEnvironmentSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/snapshots', 'json', req, runtime)
        )

    async def create_environment_snapshot_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.CreateEnvironmentSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateEnvironmentSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentSnapshotResponse(),
            await self.do_roarequest_async('CreateEnvironmentSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/snapshots', 'json', req, runtime)
        )

    def init_snapshot_instance(
        self,
        uid: str,
    ) -> cnip_20201201_models.InitSnapshotInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.init_snapshot_instance_with_options(uid, headers, runtime)

    async def init_snapshot_instance_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.InitSnapshotInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.init_snapshot_instance_with_options_async(uid, headers, runtime)

    def init_snapshot_instance_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.InitSnapshotInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.InitSnapshotInstanceResponse(),
            self.do_roarequest('InitSnapshotInstance', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/snapshots/{uid}/instances', 'json', req, runtime)
        )

    async def init_snapshot_instance_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.InitSnapshotInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.InitSnapshotInstanceResponse(),
            await self.do_roarequest_async('InitSnapshotInstance', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/snapshots/{uid}/instances', 'json', req, runtime)
        )

    def update_product_version_related_foundation_version(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionRequest,
    ) -> cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_version_related_foundation_version_with_options(uid, request, headers, runtime)

    async def update_product_version_related_foundation_version_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionRequest,
    ) -> cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_version_related_foundation_version_with_options_async(uid, request, headers, runtime)

    def update_product_version_related_foundation_version_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.foundation_version_uid
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionResponse(),
            self.do_roarequest('UpdateProductVersionRelatedFoundationVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/product_versions/{uid}/foundation', 'json', req, runtime)
        )

    async def update_product_version_related_foundation_version_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.foundation_version_uid
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionResponse(),
            await self.do_roarequest_async('UpdateProductVersionRelatedFoundationVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/product_versions/{uid}/foundation', 'json', req, runtime)
        )

    def list_environment_params(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentParamsRequest,
    ) -> cnip_20201201_models.ListEnvironmentParamsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_params_with_options(uid, request, headers, runtime)

    async def list_environment_params_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentParamsRequest,
    ) -> cnip_20201201_models.ListEnvironmentParamsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environment_params_with_options_async(uid, request, headers, runtime)

    def list_environment_params_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentParamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentParamsResponse(),
            self.do_roarequest('ListEnvironmentParams', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/params', 'json', req, runtime)
        )

    async def list_environment_params_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentParamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentParamsResponse(),
            await self.do_roarequest_async('ListEnvironmentParams', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/params', 'json', req, runtime)
        )

    def get_foundation_version(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetFoundationVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_foundation_version_with_options(uid, headers, runtime)

    async def get_foundation_version_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetFoundationVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_foundation_version_with_options_async(uid, headers, runtime)

    def get_foundation_version_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetFoundationVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetFoundationVersionResponse(),
            self.do_roarequest('GetFoundationVersion', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/foundation/versions/{uid}', 'json', req, runtime)
        )

    async def get_foundation_version_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetFoundationVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetFoundationVersionResponse(),
            await self.do_roarequest_async('GetFoundationVersion', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/foundation/versions/{uid}', 'json', req, runtime)
        )

    def delete_product(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_with_options(uid, headers, runtime)

    async def delete_product_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_with_options_async(uid, headers, runtime)

    def delete_product_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteProductResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteProductResponse(),
            self.do_roarequest('DeleteProduct', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/integration/api/v1/products/{uid}', 'json', req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteProductResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteProductResponse(),
            await self.do_roarequest_async('DeleteProduct', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/integration/api/v1/products/{uid}', 'json', req, runtime)
        )

    def update_environment(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentRequest,
    ) -> cnip_20201201_models.UpdateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(uid, request, headers, runtime)

    async def update_environment_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentRequest,
    ) -> cnip_20201201_models.UpdateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_with_options_async(uid, request, headers, runtime)

    def update_environment_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateEnvironmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.vendor_config):
            body['vendorConfig'] = request.vendor_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentResponse(),
            self.do_roarequest('UpdateEnvironment', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/environments/{uid}', 'json', req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateEnvironmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.vendor_config):
            body['vendorConfig'] = request.vendor_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentResponse(),
            await self.do_roarequest_async('UpdateEnvironment', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/environments/{uid}', 'json', req, runtime)
        )

    def get_environment_package(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetEnvironmentPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_package_with_options(uid, headers, runtime)

    async def get_environment_package_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetEnvironmentPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_package_with_options_async(uid, headers, runtime)

    def get_environment_package_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetEnvironmentPackageResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentPackageResponse(),
            self.do_roarequest('GetEnvironmentPackage', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/envPackages/{uid}', 'json', req, runtime)
        )

    async def get_environment_package_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetEnvironmentPackageResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentPackageResponse(),
            await self.do_roarequest_async('GetEnvironmentPackage', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/envPackages/{uid}', 'json', req, runtime)
        )

    def get_product_component_detail(
        self,
        uid: str,
        version_uid: str,
        product_component_version_relation_uid: str,
    ) -> cnip_20201201_models.GetProductComponentDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_component_detail_with_options(uid, version_uid, product_component_version_relation_uid, headers, runtime)

    async def get_product_component_detail_async(
        self,
        uid: str,
        version_uid: str,
        product_component_version_relation_uid: str,
    ) -> cnip_20201201_models.GetProductComponentDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_component_detail_with_options_async(uid, version_uid, product_component_version_relation_uid, headers, runtime)

    def get_product_component_detail_with_options(
        self,
        uid: str,
        version_uid: str,
        product_component_version_relation_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductComponentDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductComponentDetailResponse(),
            self.do_roarequest('GetProductComponentDetail', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/products/{uid}/versions/{version_uid}/productComponentVersionRelations/{product_component_version_relation_uid}/detail', 'json', req, runtime)
        )

    async def get_product_component_detail_with_options_async(
        self,
        uid: str,
        version_uid: str,
        product_component_version_relation_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductComponentDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductComponentDetailResponse(),
            await self.do_roarequest_async('GetProductComponentDetail', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/products/{uid}/versions/{version_uid}/productComponentVersionRelations/{product_component_version_relation_uid}/detail', 'json', req, runtime)
        )

    def import_environment_nodes(
        self,
        uid: str,
        request: cnip_20201201_models.ImportEnvironmentNodesRequest,
    ) -> cnip_20201201_models.ImportEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.import_environment_nodes_with_options(uid, request, headers, runtime)

    async def import_environment_nodes_async(
        self,
        uid: str,
        request: cnip_20201201_models.ImportEnvironmentNodesRequest,
    ) -> cnip_20201201_models.ImportEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.import_environment_nodes_with_options_async(uid, request, headers, runtime)

    def import_environment_nodes_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.ImportEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ImportEnvironmentNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.node_list_yaml
        )
        return TeaCore.from_map(
            cnip_20201201_models.ImportEnvironmentNodesResponse(),
            self.do_roarequest('ImportEnvironmentNodes', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/importnodes', 'json', req, runtime)
        )

    async def import_environment_nodes_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.ImportEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ImportEnvironmentNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.node_list_yaml
        )
        return TeaCore.from_map(
            cnip_20201201_models.ImportEnvironmentNodesResponse(),
            await self.do_roarequest_async('ImportEnvironmentNodes', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/importnodes', 'json', req, runtime)
        )

    def list_components(
        self,
        request: cnip_20201201_models.ListComponentsRequest,
    ) -> cnip_20201201_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_components_with_options(request, headers, runtime)

    async def list_components_async(
        self,
        request: cnip_20201201_models.ListComponentsRequest,
    ) -> cnip_20201201_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_components_with_options_async(request, headers, runtime)

    def list_components_with_options(
        self,
        request: cnip_20201201_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListComponentsResponse(),
            self.do_roarequest('ListComponents', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/components', 'json', req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: cnip_20201201_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListComponentsResponse(),
            await self.do_roarequest_async('ListComponents', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/components', 'json', req, runtime)
        )

    def add_environment_product_version(
        self,
        uid: str,
        request: cnip_20201201_models.AddEnvironmentProductVersionRequest,
    ) -> cnip_20201201_models.AddEnvironmentProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.AddEnvironmentProductVersionHeaders()
        return self.add_environment_product_version_with_options(uid, request, headers, runtime)

    async def add_environment_product_version_async(
        self,
        uid: str,
        request: cnip_20201201_models.AddEnvironmentProductVersionRequest,
    ) -> cnip_20201201_models.AddEnvironmentProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.AddEnvironmentProductVersionHeaders()
        return await self.add_environment_product_version_with_options_async(uid, request, headers, runtime)

    def add_environment_product_version_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.AddEnvironmentProductVersionRequest,
        headers: cnip_20201201_models.AddEnvironmentProductVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.AddEnvironmentProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddEnvironmentProductVersionResponse(),
            self.do_roarequest('AddEnvironmentProductVersion', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/productVersions', 'json', req, runtime)
        )

    async def add_environment_product_version_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.AddEnvironmentProductVersionRequest,
        headers: cnip_20201201_models.AddEnvironmentProductVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.AddEnvironmentProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddEnvironmentProductVersionResponse(),
            await self.do_roarequest_async('AddEnvironmentProductVersion', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/productVersions', 'json', req, runtime)
        )

    def list_product_versions(
        self,
        uid: str,
        request: cnip_20201201_models.ListProductVersionsRequest,
    ) -> cnip_20201201_models.ListProductVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_versions_with_options(uid, request, headers, runtime)

    async def list_product_versions_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListProductVersionsRequest,
    ) -> cnip_20201201_models.ListProductVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_versions_with_options_async(uid, request, headers, runtime)

    def list_product_versions_with_options(
        self,
        uid: str,
        tmp_req: cnip_20201201_models.ListProductVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListProductVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.ListProductVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.released):
            query['released'] = request.released
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionsResponse(),
            self.do_roarequest('ListProductVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/products/{uid}/versions', 'json', req, runtime)
        )

    async def list_product_versions_with_options_async(
        self,
        uid: str,
        tmp_req: cnip_20201201_models.ListProductVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListProductVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.ListProductVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.released):
            query['released'] = request.released
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionsResponse(),
            await self.do_roarequest_async('ListProductVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/products/{uid}/versions', 'json', req, runtime)
        )

    def get_children_component_version_list(
        self,
        id: str,
        version_id: str,
    ) -> cnip_20201201_models.GetChildrenComponentVersionListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_children_component_version_list_with_options(id, version_id, headers, runtime)

    async def get_children_component_version_list_async(
        self,
        id: str,
        version_id: str,
    ) -> cnip_20201201_models.GetChildrenComponentVersionListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_children_component_version_list_with_options_async(id, version_id, headers, runtime)

    def get_children_component_version_list_with_options(
        self,
        id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetChildrenComponentVersionListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetChildrenComponentVersionListResponse(),
            self.do_roarequest('GetChildrenComponentVersionList', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/children', 'json', req, runtime)
        )

    async def get_children_component_version_list_with_options_async(
        self,
        id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetChildrenComponentVersionListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetChildrenComponentVersionListResponse(),
            await self.do_roarequest_async('GetChildrenComponentVersionList', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/integration/api/v1/products/{id}/versions/{version_id}/children', 'json', req, runtime)
        )

    def create_slr(self) -> cnip_20201201_models.CreateSLRResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateSLRHeaders()
        return self.create_slrwith_options(headers, runtime)

    async def create_slr_async(self) -> cnip_20201201_models.CreateSLRResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateSLRHeaders()
        return await self.create_slrwith_options_async(headers, runtime)

    def create_slrwith_options(
        self,
        headers: cnip_20201201_models.CreateSLRHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateSLRResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateSLRResponse(),
            self.do_roarequest('CreateSLR', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/slr', 'json', req, runtime)
        )

    async def create_slrwith_options_async(
        self,
        headers: cnip_20201201_models.CreateSLRHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateSLRResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateSLRResponse(),
            await self.do_roarequest_async('CreateSLR', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/slr', 'json', req, runtime)
        )

    def get_product_version_related_component_version_detail(
        self,
        uid: str,
        relation_uid: str,
    ) -> cnip_20201201_models.GetProductVersionRelatedComponentVersionDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_related_component_version_detail_with_options(uid, relation_uid, headers, runtime)

    async def get_product_version_related_component_version_detail_async(
        self,
        uid: str,
        relation_uid: str,
    ) -> cnip_20201201_models.GetProductVersionRelatedComponentVersionDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_version_related_component_version_detail_with_options_async(uid, relation_uid, headers, runtime)

    def get_product_version_related_component_version_detail_with_options(
        self,
        uid: str,
        relation_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductVersionRelatedComponentVersionDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionRelatedComponentVersionDetailResponse(),
            self.do_roarequest('GetProductVersionRelatedComponentVersionDetail', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/relations/{relation_uid}', 'json', req, runtime)
        )

    async def get_product_version_related_component_version_detail_with_options_async(
        self,
        uid: str,
        relation_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductVersionRelatedComponentVersionDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionRelatedComponentVersionDetailResponse(),
            await self.do_roarequest_async('GetProductVersionRelatedComponentVersionDetail', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/relations/{relation_uid}', 'json', req, runtime)
        )

    def add_environment_package(
        self,
        uid: str,
        request: cnip_20201201_models.AddEnvironmentPackageRequest,
    ) -> cnip_20201201_models.AddEnvironmentPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.AddEnvironmentPackageHeaders()
        return self.add_environment_package_with_options(uid, request, headers, runtime)

    async def add_environment_package_async(
        self,
        uid: str,
        request: cnip_20201201_models.AddEnvironmentPackageRequest,
    ) -> cnip_20201201_models.AddEnvironmentPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.AddEnvironmentPackageHeaders()
        return await self.add_environment_package_with_options_async(uid, request, headers, runtime)

    def add_environment_package_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.AddEnvironmentPackageRequest,
        headers: cnip_20201201_models.AddEnvironmentPackageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.AddEnvironmentPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddEnvironmentPackageResponse(),
            self.do_roarequest('AddEnvironmentPackage', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/package', 'json', req, runtime)
        )

    async def add_environment_package_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.AddEnvironmentPackageRequest,
        headers: cnip_20201201_models.AddEnvironmentPackageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.AddEnvironmentPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddEnvironmentPackageResponse(),
            await self.do_roarequest_async('AddEnvironmentPackage', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/package', 'json', req, runtime)
        )

    def update_environment_product_version(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentProductVersionRequest,
    ) -> cnip_20201201_models.UpdateEnvironmentProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_product_version_with_options(uid, request, headers, runtime)

    async def update_environment_product_version_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentProductVersionRequest,
    ) -> cnip_20201201_models.UpdateEnvironmentProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_product_version_with_options_async(uid, request, headers, runtime)

    def update_environment_product_version_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateEnvironmentProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compatible_versions):
            body['compatibleVersions'] = request.compatible_versions
        if not UtilClient.is_unset(request.old_product_version):
            body['oldProductVersion'] = request.old_product_version
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentProductVersionResponse(),
            self.do_roarequest('UpdateEnvironmentProductVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/environments/{uid}/product_versions', 'json', req, runtime)
        )

    async def update_environment_product_version_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.UpdateEnvironmentProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateEnvironmentProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compatible_versions):
            body['compatibleVersions'] = request.compatible_versions
        if not UtilClient.is_unset(request.old_product_version):
            body['oldProductVersion'] = request.old_product_version
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentProductVersionResponse(),
            await self.do_roarequest_async('UpdateEnvironmentProductVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/environments/{uid}/product_versions', 'json', req, runtime)
        )

    def get_product_version_platforms(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetProductVersionPlatformsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_platforms_with_options(uid, headers, runtime)

    async def get_product_version_platforms_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetProductVersionPlatformsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_version_platforms_with_options_async(uid, headers, runtime)

    def get_product_version_platforms_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductVersionPlatformsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionPlatformsResponse(),
            self.do_roarequest('GetProductVersionPlatforms', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/platforms', 'json', req, runtime)
        )

    async def get_product_version_platforms_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductVersionPlatformsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionPlatformsResponse(),
            await self.do_roarequest_async('GetProductVersionPlatforms', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/platforms', 'json', req, runtime)
        )

    def save_environment_param(
        self,
        uid: str,
        request: cnip_20201201_models.SaveEnvironmentParamRequest,
    ) -> cnip_20201201_models.SaveEnvironmentParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_environment_param_with_options(uid, request, headers, runtime)

    async def save_environment_param_async(
        self,
        uid: str,
        request: cnip_20201201_models.SaveEnvironmentParamRequest,
    ) -> cnip_20201201_models.SaveEnvironmentParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_environment_param_with_options_async(uid, request, headers, runtime)

    def save_environment_param_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.SaveEnvironmentParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.SaveEnvironmentParamResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_uid):
            body['componentUID'] = request.component_uid
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.param_uid):
            body['paramUID'] = request.param_uid
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.SaveEnvironmentParamResponse(),
            self.do_roarequest('SaveEnvironmentParam', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/environments/{uid}/params', 'json', req, runtime)
        )

    async def save_environment_param_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.SaveEnvironmentParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.SaveEnvironmentParamResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_uid):
            body['componentUID'] = request.component_uid
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.param_uid):
            body['paramUID'] = request.param_uid
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.SaveEnvironmentParamResponse(),
            await self.do_roarequest_async('SaveEnvironmentParam', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/environments/{uid}/params', 'json', req, runtime)
        )

    def update_snapshot_instance_join_option(
        self,
        instanceuid: str,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotInstanceJoinOptionRequest,
    ) -> cnip_20201201_models.UpdateSnapshotInstanceJoinOptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_instance_join_option_with_options(instanceuid, uid, request, headers, runtime)

    async def update_snapshot_instance_join_option_async(
        self,
        instanceuid: str,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotInstanceJoinOptionRequest,
    ) -> cnip_20201201_models.UpdateSnapshotInstanceJoinOptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_snapshot_instance_join_option_with_options_async(instanceuid, uid, request, headers, runtime)

    def update_snapshot_instance_join_option_with_options(
        self,
        instanceuid: str,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotInstanceJoinOptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateSnapshotInstanceJoinOptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_snapshot):
            body['joinSnapshot'] = request.join_snapshot
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotInstanceJoinOptionResponse(),
            self.do_roarequest('UpdateSnapshotInstanceJoinOption', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/snapshots/{uid}/instances/{instanceuid}', 'json', req, runtime)
        )

    async def update_snapshot_instance_join_option_with_options_async(
        self,
        instanceuid: str,
        uid: str,
        request: cnip_20201201_models.UpdateSnapshotInstanceJoinOptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.UpdateSnapshotInstanceJoinOptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_snapshot):
            body['joinSnapshot'] = request.join_snapshot
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotInstanceJoinOptionResponse(),
            await self.do_roarequest_async('UpdateSnapshotInstanceJoinOption', '2020-12-01', 'HTTPS', 'PUT', 'AK', f'/api/v1/snapshots/{uid}/instances/{instanceuid}', 'json', req, runtime)
        )

    def get_product_version_resource(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetProductVersionResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_resource_with_options(uid, headers, runtime)

    async def get_product_version_resource_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetProductVersionResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_version_resource_with_options_async(uid, headers, runtime)

    def get_product_version_resource_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductVersionResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionResourceResponse(),
            self.do_roarequest('GetProductVersionResource', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/resources', 'json', req, runtime)
        )

    async def get_product_version_resource_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductVersionResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionResourceResponse(),
            await self.do_roarequest_async('GetProductVersionResource', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/product_versions/{uid}/resources', 'json', req, runtime)
        )

    def create_license(
        self,
        uid: str,
        request: cnip_20201201_models.CreateLicenseRequest,
    ) -> cnip_20201201_models.CreateLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_license_with_options(uid, request, headers, runtime)

    async def create_license_async(
        self,
        uid: str,
        request: cnip_20201201_models.CreateLicenseRequest,
    ) -> cnip_20201201_models.CreateLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_license_with_options_async(uid, request, headers, runtime)

    def create_license_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.CreateLicenseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_year):
            query['effectiveYear'] = request.effective_year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateLicenseResponse(),
            self.do_roarequest('CreateLicense', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/licenses', 'json', req, runtime)
        )

    async def create_license_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.CreateLicenseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.CreateLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_year):
            query['effectiveYear'] = request.effective_year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateLicenseResponse(),
            await self.do_roarequest_async('CreateLicense', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/licenses', 'json', req, runtime)
        )

    def share_snapshot(
        self,
        uid: str,
        request: cnip_20201201_models.ShareSnapshotRequest,
    ) -> cnip_20201201_models.ShareSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.share_snapshot_with_options(uid, request, headers, runtime)

    async def share_snapshot_async(
        self,
        uid: str,
        request: cnip_20201201_models.ShareSnapshotRequest,
    ) -> cnip_20201201_models.ShareSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.share_snapshot_with_options_async(uid, request, headers, runtime)

    def share_snapshot_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.ShareSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ShareSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.target_provider):
            body['targetProvider'] = request.target_provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ShareSnapshotResponse(),
            self.do_roarequest('ShareSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/snapshots/{uid}/snapshots', 'json', req, runtime)
        )

    async def share_snapshot_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.ShareSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ShareSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.target_provider):
            body['targetProvider'] = request.target_provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ShareSnapshotResponse(),
            await self.do_roarequest_async('ShareSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/snapshots/{uid}/snapshots', 'json', req, runtime)
        )

    def delete_environment_param(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteEnvironmentParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_param_with_options(uid, headers, runtime)

    async def delete_environment_param_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeleteEnvironmentParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_param_with_options_async(uid, headers, runtime)

    def delete_environment_param_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteEnvironmentParamResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentParamResponse(),
            self.do_roarequest('DeleteEnvironmentParam', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/api/v1/environmentparams/{uid}', 'json', req, runtime)
        )

    async def delete_environment_param_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteEnvironmentParamResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentParamResponse(),
            await self.do_roarequest_async('DeleteEnvironmentParam', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/api/v1/environmentparams/{uid}', 'json', req, runtime)
        )

    def get_product(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_with_options(uid, headers, runtime)

    async def get_product_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.GetProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_with_options_async(uid, headers, runtime)

    def get_product_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductResponse(),
            self.do_roarequest('GetProduct', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/products/{uid}', 'json', req, runtime)
        )

    async def get_product_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.GetProductResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductResponse(),
            await self.do_roarequest_async('GetProduct', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/products/{uid}', 'json', req, runtime)
        )

    def delete_component_version(
        self,
        uid: str,
        version_uid: str,
    ) -> cnip_20201201_models.DeleteComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_component_version_with_options(uid, version_uid, headers, runtime)

    async def delete_component_version_async(
        self,
        uid: str,
        version_uid: str,
    ) -> cnip_20201201_models.DeleteComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_component_version_with_options_async(uid, version_uid, headers, runtime)

    def delete_component_version_with_options(
        self,
        uid: str,
        version_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteComponentVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteComponentVersionResponse(),
            self.do_roarequest('DeleteComponentVersion', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/integration/api/v1/components/{uid}/versions/{version_uid}', 'json', req, runtime)
        )

    async def delete_component_version_with_options_async(
        self,
        uid: str,
        version_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeleteComponentVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteComponentVersionResponse(),
            await self.do_roarequest_async('DeleteComponentVersion', '2020-12-01', 'HTTPS', 'DELETE', 'AK', f'/integration/api/v1/components/{uid}/versions/{version_uid}', 'json', req, runtime)
        )

    def deploy_environment_product(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeployEnvironmentProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_environment_product_with_options(uid, headers, runtime)

    async def deploy_environment_product_async(
        self,
        uid: str,
    ) -> cnip_20201201_models.DeployEnvironmentProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_environment_product_with_options_async(uid, headers, runtime)

    def deploy_environment_product_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeployEnvironmentProductResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeployEnvironmentProductResponse(),
            self.do_roarequest('DeployEnvironmentProduct', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/deployment', 'json', req, runtime)
        )

    async def deploy_environment_product_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.DeployEnvironmentProductResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeployEnvironmentProductResponse(),
            await self.do_roarequest_async('DeployEnvironmentProduct', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/deployment', 'json', req, runtime)
        )

    def init_environment_resource(
        self,
        uid: str,
        request: cnip_20201201_models.InitEnvironmentResourceRequest,
    ) -> cnip_20201201_models.InitEnvironmentResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.init_environment_resource_with_options(uid, request, headers, runtime)

    async def init_environment_resource_async(
        self,
        uid: str,
        request: cnip_20201201_models.InitEnvironmentResourceRequest,
    ) -> cnip_20201201_models.InitEnvironmentResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.init_environment_resource_with_options_async(uid, request, headers, runtime)

    def init_environment_resource_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.InitEnvironmentResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.InitEnvironmentResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyID'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.security_token):
            body['securityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.InitEnvironmentResourceResponse(),
            self.do_roarequest('InitEnvironmentResource', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/resources', 'json', req, runtime)
        )

    async def init_environment_resource_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.InitEnvironmentResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.InitEnvironmentResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyID'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.security_token):
            body['securityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.InitEnvironmentResourceResponse(),
            await self.do_roarequest_async('InitEnvironmentResource', '2020-12-01', 'HTTPS', 'POST', 'AK', f'/api/v1/environments/{uid}/resources', 'json', req, runtime)
        )

    def list_foundation_versions(self) -> cnip_20201201_models.ListFoundationVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_versions_with_options(headers, runtime)

    async def list_foundation_versions_async(self) -> cnip_20201201_models.ListFoundationVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_foundation_versions_with_options_async(headers, runtime)

    def list_foundation_versions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListFoundationVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListFoundationVersionsResponse(),
            self.do_roarequest('ListFoundationVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/foundation/versions', 'json', req, runtime)
        )

    async def list_foundation_versions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListFoundationVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListFoundationVersionsResponse(),
            await self.do_roarequest_async('ListFoundationVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/foundation/versions', 'json', req, runtime)
        )

    def list_environment_deploy_record(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentDeployRecordRequest,
    ) -> cnip_20201201_models.ListEnvironmentDeployRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_deploy_record_with_options(uid, request, headers, runtime)

    async def list_environment_deploy_record_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentDeployRecordRequest,
    ) -> cnip_20201201_models.ListEnvironmentDeployRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environment_deploy_record_with_options_async(uid, request, headers, runtime)

    def list_environment_deploy_record_with_options(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentDeployRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentDeployRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentDeployRecordResponse(),
            self.do_roarequest('ListEnvironmentDeployRecord', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/deployments', 'json', req, runtime)
        )

    async def list_environment_deploy_record_with_options_async(
        self,
        uid: str,
        request: cnip_20201201_models.ListEnvironmentDeployRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cnip_20201201_models.ListEnvironmentDeployRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentDeployRecordResponse(),
            await self.do_roarequest_async('ListEnvironmentDeployRecord', '2020-12-01', 'HTTPS', 'GET', 'AK', f'/api/v1/environments/{uid}/deployments', 'json', req, runtime)
        )
