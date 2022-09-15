# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adp20210720 import models as adp_20210720_models
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
        self._endpoint = self.get_endpoint('adp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_environment_nodes(
        self,
        uid: str,
        request: adp_20210720_models.AddEnvironmentNodesRequest,
    ) -> adp_20210720_models.AddEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_environment_nodes_with_options(uid, request, headers, runtime)

    async def add_environment_nodes_async(
        self,
        uid: str,
        request: adp_20210720_models.AddEnvironmentNodesRequest,
    ) -> adp_20210720_models.AddEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_environment_nodes_with_options_async(uid, request, headers, runtime)

    def add_environment_nodes_with_options(
        self,
        uid: str,
        request: adp_20210720_models.AddEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddEnvironmentNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_disk):
            body['applicationDisk'] = request.application_disk
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.etcd_disk):
            body['etcdDisk'] = request.etcd_disk
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.master_private_ips):
            body['masterPrivateIPs'] = request.master_private_ips
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.os):
            body['os'] = request.os
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.trident_system_disk):
            body['tridentSystemDisk'] = request.trident_system_disk
        if not UtilClient.is_unset(request.trident_system_size_disk):
            body['tridentSystemSizeDisk'] = request.trident_system_size_disk
        if not UtilClient.is_unset(request.worker_private_ips):
            body['workerPrivateIPs'] = request.worker_private_ips
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddEnvironmentNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_environment_nodes_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.AddEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddEnvironmentNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_disk):
            body['applicationDisk'] = request.application_disk
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.etcd_disk):
            body['etcdDisk'] = request.etcd_disk
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.master_private_ips):
            body['masterPrivateIPs'] = request.master_private_ips
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.os):
            body['os'] = request.os
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.trident_system_disk):
            body['tridentSystemDisk'] = request.trident_system_disk
        if not UtilClient.is_unset(request.trident_system_size_disk):
            body['tridentSystemSizeDisk'] = request.trident_system_size_disk
        if not UtilClient.is_unset(request.worker_private_ips):
            body['workerPrivateIPs'] = request.worker_private_ips
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddEnvironmentNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_environment_product_versions(
        self,
        uid: str,
        request: adp_20210720_models.AddEnvironmentProductVersionsRequest,
    ) -> adp_20210720_models.AddEnvironmentProductVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_environment_product_versions_with_options(uid, request, headers, runtime)

    async def add_environment_product_versions_async(
        self,
        uid: str,
        request: adp_20210720_models.AddEnvironmentProductVersionsRequest,
    ) -> adp_20210720_models.AddEnvironmentProductVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_environment_product_versions_with_options_async(uid, request, headers, runtime)

    def add_environment_product_versions_with_options(
        self,
        uid: str,
        request: adp_20210720_models.AddEnvironmentProductVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddEnvironmentProductVersionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_version_info_list):
            body['productVersionInfoList'] = request.product_version_info_list
        if not UtilClient.is_unset(request.product_version_uidlist):
            body['productVersionUIDList'] = request.product_version_uidlist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEnvironmentProductVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/product-versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddEnvironmentProductVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_environment_product_versions_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.AddEnvironmentProductVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddEnvironmentProductVersionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_version_info_list):
            body['productVersionInfoList'] = request.product_version_info_list
        if not UtilClient.is_unset(request.product_version_uidlist):
            body['productVersionUIDList'] = request.product_version_uidlist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEnvironmentProductVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/product-versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddEnvironmentProductVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_product_component_version(
        self,
        uid: str,
        component_version_uid: str,
        request: adp_20210720_models.AddProductComponentVersionRequest,
    ) -> adp_20210720_models.AddProductComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_product_component_version_with_options(uid, component_version_uid, request, headers, runtime)

    async def add_product_component_version_async(
        self,
        uid: str,
        component_version_uid: str,
        request: adp_20210720_models.AddProductComponentVersionRequest,
    ) -> adp_20210720_models.AddProductComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_product_component_version_with_options_async(uid, component_version_uid, request, headers, runtime)

    def add_product_component_version_with_options(
        self,
        uid: str,
        component_version_uid: str,
        request: adp_20210720_models.AddProductComponentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddProductComponentVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/component-versions/{OpenApiUtilClient.get_encode_param(component_version_uid)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddProductComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_product_component_version_with_options_async(
        self,
        uid: str,
        component_version_uid: str,
        request: adp_20210720_models.AddProductComponentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddProductComponentVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/component-versions/{OpenApiUtilClient.get_encode_param(component_version_uid)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddProductComponentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_product_version_config(
        self,
        uid: str,
        request: adp_20210720_models.AddProductVersionConfigRequest,
    ) -> adp_20210720_models.AddProductVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_product_version_config_with_options(uid, request, headers, runtime)

    async def add_product_version_config_async(
        self,
        uid: str,
        request: adp_20210720_models.AddProductVersionConfigRequest,
    ) -> adp_20210720_models.AddProductVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_product_version_config_with_options_async(uid, request, headers, runtime)

    def add_product_version_config_with_options(
        self,
        uid: str,
        request: adp_20210720_models.AddProductVersionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddProductVersionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_release_name):
            body['componentReleaseName'] = request.component_release_name
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_release_name):
            body['parentComponentReleaseName'] = request.parent_component_release_name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddProductVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_product_version_config_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.AddProductVersionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddProductVersionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_release_name):
            body['componentReleaseName'] = request.component_release_name
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_release_name):
            body['parentComponentReleaseName'] = request.parent_component_release_name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddProductVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_resource_snapshot(
        self,
        request: adp_20210720_models.AddResourceSnapshotRequest,
    ) -> adp_20210720_models.AddResourceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_resource_snapshot_with_options(request, headers, runtime)

    async def add_resource_snapshot_async(
        self,
        request: adp_20210720_models.AddResourceSnapshotRequest,
    ) -> adp_20210720_models.AddResourceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_resource_snapshot_with_options_async(request, headers, runtime)

    def add_resource_snapshot_with_options(
        self,
        request: adp_20210720_models.AddResourceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddResourceSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_uid):
            query['clusterUID'] = request.cluster_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddResourceSnapshot',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/resource-snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddResourceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_resource_snapshot_with_options_async(
        self,
        request: adp_20210720_models.AddResourceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.AddResourceSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_uid):
            query['clusterUID'] = request.cluster_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddResourceSnapshot',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/resource-snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddResourceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_environment_nodes(
        self,
        uid: str,
        request: adp_20210720_models.BatchAddEnvironmentNodesRequest,
    ) -> adp_20210720_models.BatchAddEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_add_environment_nodes_with_options(uid, request, headers, runtime)

    async def batch_add_environment_nodes_async(
        self,
        uid: str,
        request: adp_20210720_models.BatchAddEnvironmentNodesRequest,
    ) -> adp_20210720_models.BatchAddEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_add_environment_nodes_with_options_async(uid, request, headers, runtime)

    def batch_add_environment_nodes_with_options(
        self,
        uid: str,
        request: adp_20210720_models.BatchAddEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.BatchAddEnvironmentNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_list):
            body['instanceList'] = request.instance_list
        if not UtilClient.is_unset(request.overwrite):
            body['overwrite'] = request.overwrite
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/batch/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.BatchAddEnvironmentNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_environment_nodes_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.BatchAddEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.BatchAddEnvironmentNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_list):
            body['instanceList'] = request.instance_list
        if not UtilClient.is_unset(request.overwrite):
            body['overwrite'] = request.overwrite
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/batch/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.BatchAddEnvironmentNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_product_version_config(
        self,
        uid: str,
        request: adp_20210720_models.BatchAddProductVersionConfigRequest,
    ) -> adp_20210720_models.BatchAddProductVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_add_product_version_config_with_options(uid, request, headers, runtime)

    async def batch_add_product_version_config_async(
        self,
        uid: str,
        request: adp_20210720_models.BatchAddProductVersionConfigRequest,
    ) -> adp_20210720_models.BatchAddProductVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_add_product_version_config_with_options_async(uid, request, headers, runtime)

    def batch_add_product_version_config_with_options(
        self,
        uid: str,
        request: adp_20210720_models.BatchAddProductVersionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.BatchAddProductVersionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_version_config_list):
            body['productVersionConfigList'] = request.product_version_config_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/batch/configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.BatchAddProductVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_product_version_config_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.BatchAddProductVersionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.BatchAddProductVersionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_version_config_list):
            body['productVersionConfigList'] = request.product_version_config_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/batch/configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.BatchAddProductVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        request: adp_20210720_models.CreateEnvironmentRequest,
    ) -> adp_20210720_models.CreateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateEnvironmentHeaders()
        return self.create_environment_with_options(request, headers, runtime)

    async def create_environment_async(
        self,
        request: adp_20210720_models.CreateEnvironmentRequest,
    ) -> adp_20210720_models.CreateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateEnvironmentHeaders()
        return await self.create_environment_with_options_async(request, headers, runtime)

    def create_environment_with_options(
        self,
        request: adp_20210720_models.CreateEnvironmentRequest,
        headers: adp_20210720_models.CreateEnvironmentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateEnvironmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.platform_list):
            body['platformList'] = request.platform_list
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.vendor_config):
            body['vendorConfig'] = request.vendor_config
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: adp_20210720_models.CreateEnvironmentRequest,
        headers: adp_20210720_models.CreateEnvironmentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateEnvironmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.platform_list):
            body['platformList'] = request.platform_list
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.vendor_config):
            body['vendorConfig'] = request.vendor_config
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment_license(
        self,
        uid: str,
        request: adp_20210720_models.CreateEnvironmentLicenseRequest,
    ) -> adp_20210720_models.CreateEnvironmentLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_license_with_options(uid, request, headers, runtime)

    async def create_environment_license_async(
        self,
        uid: str,
        request: adp_20210720_models.CreateEnvironmentLicenseRequest,
    ) -> adp_20210720_models.CreateEnvironmentLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_license_with_options_async(uid, request, headers, runtime)

    def create_environment_license_with_options(
        self,
        uid: str,
        request: adp_20210720_models.CreateEnvironmentLicenseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateEnvironmentLicenseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.company_name):
            body['companyName'] = request.company_name
        if not UtilClient.is_unset(request.contact):
            body['contact'] = request.contact
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.license_quota):
            body['licenseQuota'] = request.license_quota
        if not UtilClient.is_unset(request.machine_fingerprint):
            body['machineFingerprint'] = request.machine_fingerprint
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironmentLicense',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/licenses',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateEnvironmentLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_license_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.CreateEnvironmentLicenseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateEnvironmentLicenseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.company_name):
            body['companyName'] = request.company_name
        if not UtilClient.is_unset(request.contact):
            body['contact'] = request.contact
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.license_quota):
            body['licenseQuota'] = request.license_quota
        if not UtilClient.is_unset(request.machine_fingerprint):
            body['machineFingerprint'] = request.machine_fingerprint
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironmentLicense',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/licenses',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateEnvironmentLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_foundation_reference(
        self,
        request: adp_20210720_models.CreateFoundationReferenceRequest,
    ) -> adp_20210720_models.CreateFoundationReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_foundation_reference_with_options(request, headers, runtime)

    async def create_foundation_reference_async(
        self,
        request: adp_20210720_models.CreateFoundationReferenceRequest,
    ) -> adp_20210720_models.CreateFoundationReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_foundation_reference_with_options_async(request, headers, runtime)

    def create_foundation_reference_with_options(
        self,
        request: adp_20210720_models.CreateFoundationReferenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateFoundationReferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_config):
            body['clusterConfig'] = request.cluster_config
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateFoundationReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_foundation_reference_with_options_async(
        self,
        request: adp_20210720_models.CreateFoundationReferenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateFoundationReferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_config):
            body['clusterConfig'] = request.cluster_config
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateFoundationReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: adp_20210720_models.CreateProductRequest,
    ) -> adp_20210720_models.CreateProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateProductHeaders()
        return self.create_product_with_options(request, headers, runtime)

    async def create_product_async(
        self,
        request: adp_20210720_models.CreateProductRequest,
    ) -> adp_20210720_models.CreateProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateProductHeaders()
        return await self.create_product_with_options_async(request, headers, runtime)

    def create_product_with_options(
        self,
        request: adp_20210720_models.CreateProductRequest,
        headers: adp_20210720_models.CreateProductHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.categories):
            body['categories'] = request.categories
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.vendor):
            body['vendor'] = request.vendor
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/products',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: adp_20210720_models.CreateProductRequest,
        headers: adp_20210720_models.CreateProductHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.categories):
            body['categories'] = request.categories
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.vendor):
            body['vendor'] = request.vendor
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/products',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_deployment(
        self,
        request: adp_20210720_models.CreateProductDeploymentRequest,
    ) -> adp_20210720_models.CreateProductDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_product_deployment_with_options(request, headers, runtime)

    async def create_product_deployment_async(
        self,
        request: adp_20210720_models.CreateProductDeploymentRequest,
    ) -> adp_20210720_models.CreateProductDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_product_deployment_with_options_async(request, headers, runtime)

    def create_product_deployment_with_options(
        self,
        request: adp_20210720_models.CreateProductDeploymentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateProductDeploymentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_config):
            body['packageConfig'] = request.package_config
        if not UtilClient.is_unset(request.package_uid):
            body['packageUID'] = request.package_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductDeployment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/deployments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_deployment_with_options_async(
        self,
        request: adp_20210720_models.CreateProductDeploymentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateProductDeploymentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_config):
            body['packageConfig'] = request.package_config
        if not UtilClient.is_unset(request.package_uid):
            body['packageUID'] = request.package_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductDeployment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/deployments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_version(
        self,
        uid: str,
        request: adp_20210720_models.CreateProductVersionRequest,
    ) -> adp_20210720_models.CreateProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_product_version_with_options(uid, request, headers, runtime)

    async def create_product_version_async(
        self,
        uid: str,
        request: adp_20210720_models.CreateProductVersionRequest,
    ) -> adp_20210720_models.CreateProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_product_version_with_options_async(uid, request, headers, runtime)

    def create_product_version_with_options(
        self,
        uid: str,
        request: adp_20210720_models.CreateProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateProductVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_product_version_uid):
            query['baseProductVersionUID'] = request.base_product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_version_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.CreateProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateProductVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_product_version_uid):
            query['baseProductVersionUID'] = request.base_product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_version_package(
        self,
        uid: str,
        request: adp_20210720_models.CreateProductVersionPackageRequest,
    ) -> adp_20210720_models.CreateProductVersionPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateProductVersionPackageHeaders()
        return self.create_product_version_package_with_options(uid, request, headers, runtime)

    async def create_product_version_package_async(
        self,
        uid: str,
        request: adp_20210720_models.CreateProductVersionPackageRequest,
    ) -> adp_20210720_models.CreateProductVersionPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateProductVersionPackageHeaders()
        return await self.create_product_version_package_with_options_async(uid, request, headers, runtime)

    def create_product_version_package_with_options(
        self,
        uid: str,
        request: adp_20210720_models.CreateProductVersionPackageRequest,
        headers: adp_20210720_models.CreateProductVersionPackageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateProductVersionPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_engine_type):
            query['clusterEngineType'] = request.cluster_engine_type
        if not UtilClient.is_unset(request.foundation_reference_uid):
            query['foundationReferenceUID'] = request.foundation_reference_uid
        if not UtilClient.is_unset(request.old_foundation_reference_uid):
            query['oldFoundationReferenceUID'] = request.old_foundation_reference_uid
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_content_type):
            query['packageContentType'] = request.package_content_type
        if not UtilClient.is_unset(request.package_tool_type):
            query['packageToolType'] = request.package_tool_type
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductVersionPackage',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/hosting/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/packages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductVersionPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_version_package_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.CreateProductVersionPackageRequest,
        headers: adp_20210720_models.CreateProductVersionPackageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.CreateProductVersionPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_engine_type):
            query['clusterEngineType'] = request.cluster_engine_type
        if not UtilClient.is_unset(request.foundation_reference_uid):
            query['foundationReferenceUID'] = request.foundation_reference_uid
        if not UtilClient.is_unset(request.old_foundation_reference_uid):
            query['oldFoundationReferenceUID'] = request.old_foundation_reference_uid
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_content_type):
            query['packageContentType'] = request.package_content_type
        if not UtilClient.is_unset(request.package_tool_type):
            query['packageToolType'] = request.package_tool_type
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductVersionPackage',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/hosting/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/packages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductVersionPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        uid: str,
    ) -> adp_20210720_models.DeleteEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(uid, headers, runtime)

    async def delete_environment_async(
        self,
        uid: str,
    ) -> adp_20210720_models.DeleteEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(uid, headers, runtime)

    def delete_environment_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment_license(
        self,
        uid: str,
        license_uid: str,
    ) -> adp_20210720_models.DeleteEnvironmentLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_license_with_options(uid, license_uid, headers, runtime)

    async def delete_environment_license_async(
        self,
        uid: str,
        license_uid: str,
    ) -> adp_20210720_models.DeleteEnvironmentLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_license_with_options_async(uid, license_uid, headers, runtime)

    def delete_environment_license_with_options(
        self,
        uid: str,
        license_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteEnvironmentLicenseResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentLicense',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/licenses/{OpenApiUtilClient.get_encode_param(license_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_license_with_options_async(
        self,
        uid: str,
        license_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteEnvironmentLicenseResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentLicense',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/licenses/{OpenApiUtilClient.get_encode_param(license_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment_node(
        self,
        uid: str,
        node_uid: str,
    ) -> adp_20210720_models.DeleteEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_node_with_options(uid, node_uid, headers, runtime)

    async def delete_environment_node_async(
        self,
        uid: str,
        node_uid: str,
    ) -> adp_20210720_models.DeleteEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_node_with_options_async(uid, node_uid, headers, runtime)

    def delete_environment_node_with_options(
        self,
        uid: str,
        node_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteEnvironmentNodeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes/{OpenApiUtilClient.get_encode_param(node_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_node_with_options_async(
        self,
        uid: str,
        node_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteEnvironmentNodeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes/{OpenApiUtilClient.get_encode_param(node_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment_product_version(
        self,
        uid: str,
        product_version_uid: str,
    ) -> adp_20210720_models.DeleteEnvironmentProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_product_version_with_options(uid, product_version_uid, headers, runtime)

    async def delete_environment_product_version_async(
        self,
        uid: str,
        product_version_uid: str,
    ) -> adp_20210720_models.DeleteEnvironmentProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_product_version_with_options_async(uid, product_version_uid, headers, runtime)

    def delete_environment_product_version_with_options(
        self,
        uid: str,
        product_version_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteEnvironmentProductVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/product-versions/{OpenApiUtilClient.get_encode_param(product_version_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_product_version_with_options_async(
        self,
        uid: str,
        product_version_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteEnvironmentProductVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/product-versions/{OpenApiUtilClient.get_encode_param(product_version_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product(
        self,
        uid: str,
    ) -> adp_20210720_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_with_options(uid, headers, runtime)

    async def delete_product_async(
        self,
        uid: str,
    ) -> adp_20210720_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_with_options_async(uid, headers, runtime)

    def delete_product_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product_component_version(
        self,
        uid: str,
        relation_uid: str,
    ) -> adp_20210720_models.DeleteProductComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_component_version_with_options(uid, relation_uid, headers, runtime)

    async def delete_product_component_version_async(
        self,
        uid: str,
        relation_uid: str,
    ) -> adp_20210720_models.DeleteProductComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_component_version_with_options_async(uid, relation_uid, headers, runtime)

    def delete_product_component_version_with_options(
        self,
        uid: str,
        relation_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductComponentVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/relations/{OpenApiUtilClient.get_encode_param(relation_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_component_version_with_options_async(
        self,
        uid: str,
        relation_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductComponentVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/relations/{OpenApiUtilClient.get_encode_param(relation_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductComponentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product_instance_config(
        self,
        config_uid: str,
        request: adp_20210720_models.DeleteProductInstanceConfigRequest,
    ) -> adp_20210720_models.DeleteProductInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_instance_config_with_options(config_uid, request, headers, runtime)

    async def delete_product_instance_config_async(
        self,
        config_uid: str,
        request: adp_20210720_models.DeleteProductInstanceConfigRequest,
    ) -> adp_20210720_models.DeleteProductInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_instance_config_with_options_async(config_uid, request, headers, runtime)

    def delete_product_instance_config_with_options(
        self,
        config_uid: str,
        request: adp_20210720_models.DeleteProductInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProductInstanceConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/configs/{OpenApiUtilClient.get_encode_param(config_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_instance_config_with_options_async(
        self,
        config_uid: str,
        request: adp_20210720_models.DeleteProductInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProductInstanceConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/configs/{OpenApiUtilClient.get_encode_param(config_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product_version(
        self,
        uid: str,
    ) -> adp_20210720_models.DeleteProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_version_with_options(uid, headers, runtime)

    async def delete_product_version_async(
        self,
        uid: str,
    ) -> adp_20210720_models.DeleteProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_version_with_options_async(uid, headers, runtime)

    def delete_product_version_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_version_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product_version_config(
        self,
        uid: str,
        config_uid: str,
    ) -> adp_20210720_models.DeleteProductVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_version_config_with_options(uid, config_uid, headers, runtime)

    async def delete_product_version_config_async(
        self,
        uid: str,
        config_uid: str,
    ) -> adp_20210720_models.DeleteProductVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_version_config_with_options_async(uid, config_uid, headers, runtime)

    def delete_product_version_config_with_options(
        self,
        uid: str,
        config_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductVersionConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/configs/{OpenApiUtilClient.get_encode_param(config_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_version_config_with_options_async(
        self,
        uid: str,
        config_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.DeleteProductVersionConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/configs/{OpenApiUtilClient.get_encode_param(config_uid)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_product_instance_deployment_config(
        self,
        request: adp_20210720_models.GenerateProductInstanceDeploymentConfigRequest,
    ) -> adp_20210720_models.GenerateProductInstanceDeploymentConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_product_instance_deployment_config_with_options(request, headers, runtime)

    async def generate_product_instance_deployment_config_async(
        self,
        request: adp_20210720_models.GenerateProductInstanceDeploymentConfigRequest,
    ) -> adp_20210720_models.GenerateProductInstanceDeploymentConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_product_instance_deployment_config_with_options_async(request, headers, runtime)

    def generate_product_instance_deployment_config_with_options(
        self,
        request: adp_20210720_models.GenerateProductInstanceDeploymentConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GenerateProductInstanceDeploymentConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.package_uid):
            body['packageUID'] = request.package_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.product_version_uidlist):
            body['productVersionUIDList'] = request.product_version_uidlist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProductInstanceDeploymentConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/package-configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GenerateProductInstanceDeploymentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_product_instance_deployment_config_with_options_async(
        self,
        request: adp_20210720_models.GenerateProductInstanceDeploymentConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GenerateProductInstanceDeploymentConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.package_uid):
            body['packageUID'] = request.package_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.product_version_uidlist):
            body['productVersionUIDList'] = request.product_version_uidlist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProductInstanceDeploymentConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/package-configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GenerateProductInstanceDeploymentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_component(
        self,
        uid: str,
    ) -> adp_20210720_models.GetComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_component_with_options(uid, headers, runtime)

    async def get_component_async(
        self,
        uid: str,
    ) -> adp_20210720_models.GetComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_component_with_options_async(uid, headers, runtime)

    def get_component_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetComponentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetComponent',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/components/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_component_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetComponentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetComponent',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/components/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_component_version(
        self,
        uid: str,
        version_uid: str,
        request: adp_20210720_models.GetComponentVersionRequest,
    ) -> adp_20210720_models.GetComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_component_version_with_options(uid, version_uid, request, headers, runtime)

    async def get_component_version_async(
        self,
        uid: str,
        version_uid: str,
        request: adp_20210720_models.GetComponentVersionRequest,
    ) -> adp_20210720_models.GetComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_component_version_with_options_async(uid, version_uid, request, headers, runtime)

    def get_component_version_with_options(
        self,
        uid: str,
        version_uid: str,
        request: adp_20210720_models.GetComponentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetComponentVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.without_chart_content):
            query['withoutChartContent'] = request.without_chart_content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/components/{OpenApiUtilClient.get_encode_param(uid)}/versions/{OpenApiUtilClient.get_encode_param(version_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_component_version_with_options_async(
        self,
        uid: str,
        version_uid: str,
        request: adp_20210720_models.GetComponentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetComponentVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.without_chart_content):
            query['withoutChartContent'] = request.without_chart_content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/components/{OpenApiUtilClient.get_encode_param(uid)}/versions/{OpenApiUtilClient.get_encode_param(version_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetComponentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment(
        self,
        uid: str,
        request: adp_20210720_models.GetEnvironmentRequest,
    ) -> adp_20210720_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(uid, request, headers, runtime)

    async def get_environment_async(
        self,
        uid: str,
        request: adp_20210720_models.GetEnvironmentRequest,
    ) -> adp_20210720_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(uid, request, headers, runtime)

    def get_environment_with_options(
        self,
        uid: str,
        tmp_req: adp_20210720_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetEnvironmentResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.GetEnvironmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.options), 'options', 'json')
        query = {}
        if not UtilClient.is_unset(request.options_shrink):
            query['options'] = request.options_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        uid: str,
        tmp_req: adp_20210720_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetEnvironmentResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.GetEnvironmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.options), 'options', 'json')
        query = {}
        if not UtilClient.is_unset(request.options_shrink):
            query['options'] = request.options_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment_license(
        self,
        uid: str,
        license_uid: str,
        request: adp_20210720_models.GetEnvironmentLicenseRequest,
    ) -> adp_20210720_models.GetEnvironmentLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_license_with_options(uid, license_uid, request, headers, runtime)

    async def get_environment_license_async(
        self,
        uid: str,
        license_uid: str,
        request: adp_20210720_models.GetEnvironmentLicenseRequest,
    ) -> adp_20210720_models.GetEnvironmentLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_license_with_options_async(uid, license_uid, request, headers, runtime)

    def get_environment_license_with_options(
        self,
        uid: str,
        license_uid: str,
        tmp_req: adp_20210720_models.GetEnvironmentLicenseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetEnvironmentLicenseResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.GetEnvironmentLicenseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.options), 'options', 'json')
        query = {}
        if not UtilClient.is_unset(request.options_shrink):
            query['options'] = request.options_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironmentLicense',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/licenses/{OpenApiUtilClient.get_encode_param(license_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_license_with_options_async(
        self,
        uid: str,
        license_uid: str,
        tmp_req: adp_20210720_models.GetEnvironmentLicenseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetEnvironmentLicenseResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.GetEnvironmentLicenseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.options), 'options', 'json')
        query = {}
        if not UtilClient.is_unset(request.options_shrink):
            query['options'] = request.options_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnvironmentLicense',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/licenses/{OpenApiUtilClient.get_encode_param(license_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment_node(
        self,
        uid: str,
        node_uid: str,
    ) -> adp_20210720_models.GetEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_node_with_options(uid, node_uid, headers, runtime)

    async def get_environment_node_async(
        self,
        uid: str,
        node_uid: str,
    ) -> adp_20210720_models.GetEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_node_with_options_async(uid, node_uid, headers, runtime)

    def get_environment_node_with_options(
        self,
        uid: str,
        node_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetEnvironmentNodeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes/{OpenApiUtilClient.get_encode_param(node_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_node_with_options_async(
        self,
        uid: str,
        node_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetEnvironmentNodeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes/{OpenApiUtilClient.get_encode_param(node_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_foundation_component_reference(
        self,
        component_reference_uid: str,
        uid: str,
    ) -> adp_20210720_models.GetFoundationComponentReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_foundation_component_reference_with_options(component_reference_uid, uid, headers, runtime)

    async def get_foundation_component_reference_async(
        self,
        component_reference_uid: str,
        uid: str,
    ) -> adp_20210720_models.GetFoundationComponentReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_foundation_component_reference_with_options_async(component_reference_uid, uid, headers, runtime)

    def get_foundation_component_reference_with_options(
        self,
        component_reference_uid: str,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetFoundationComponentReferenceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFoundationComponentReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/{OpenApiUtilClient.get_encode_param(uid)}/components/{OpenApiUtilClient.get_encode_param(component_reference_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetFoundationComponentReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_foundation_component_reference_with_options_async(
        self,
        component_reference_uid: str,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetFoundationComponentReferenceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFoundationComponentReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/{OpenApiUtilClient.get_encode_param(uid)}/components/{OpenApiUtilClient.get_encode_param(component_reference_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetFoundationComponentReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_foundation_reference(
        self,
        uid: str,
    ) -> adp_20210720_models.GetFoundationReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_foundation_reference_with_options(uid, headers, runtime)

    async def get_foundation_reference_async(
        self,
        uid: str,
    ) -> adp_20210720_models.GetFoundationReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_foundation_reference_with_options_async(uid, headers, runtime)

    def get_foundation_reference_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetFoundationReferenceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/{OpenApiUtilClient.get_encode_param(uid)}/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetFoundationReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_foundation_reference_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetFoundationReferenceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/{OpenApiUtilClient.get_encode_param(uid)}/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetFoundationReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_foundation_version(
        self,
        uid: str,
    ) -> adp_20210720_models.GetFoundationVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_foundation_version_with_options(uid, headers, runtime)

    async def get_foundation_version_async(
        self,
        uid: str,
    ) -> adp_20210720_models.GetFoundationVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_foundation_version_with_options_async(uid, headers, runtime)

    def get_foundation_version_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetFoundationVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFoundationVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation/versions/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetFoundationVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_foundation_version_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetFoundationVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFoundationVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation/versions/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetFoundationVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product(
        self,
        uid: str,
        request: adp_20210720_models.GetProductRequest,
    ) -> adp_20210720_models.GetProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_with_options(uid, request, headers, runtime)

    async def get_product_async(
        self,
        uid: str,
        request: adp_20210720_models.GetProductRequest,
    ) -> adp_20210720_models.GetProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_with_options_async(uid, request, headers, runtime)

    def get_product_with_options(
        self,
        uid: str,
        request: adp_20210720_models.GetProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_icon_url):
            query['withIconURL'] = request.with_icon_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.GetProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_icon_url):
            query['withIconURL'] = request.with_icon_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_component_version(
        self,
        relation_uid: str,
        uid: str,
    ) -> adp_20210720_models.GetProductComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_component_version_with_options(relation_uid, uid, headers, runtime)

    async def get_product_component_version_async(
        self,
        relation_uid: str,
        uid: str,
    ) -> adp_20210720_models.GetProductComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_component_version_with_options_async(relation_uid, uid, headers, runtime)

    def get_product_component_version_with_options(
        self,
        relation_uid: str,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductComponentVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/relations/{OpenApiUtilClient.get_encode_param(relation_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_component_version_with_options_async(
        self,
        relation_uid: str,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductComponentVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/relations/{OpenApiUtilClient.get_encode_param(relation_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductComponentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_deployment(
        self,
        deployment_uid: str,
        request: adp_20210720_models.GetProductDeploymentRequest,
    ) -> adp_20210720_models.GetProductDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_deployment_with_options(deployment_uid, request, headers, runtime)

    async def get_product_deployment_async(
        self,
        deployment_uid: str,
        request: adp_20210720_models.GetProductDeploymentRequest,
    ) -> adp_20210720_models.GetProductDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_deployment_with_options_async(deployment_uid, request, headers, runtime)

    def get_product_deployment_with_options(
        self,
        deployment_uid: str,
        request: adp_20210720_models.GetProductDeploymentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductDeploymentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.with_param_config):
            query['withParamConfig'] = request.with_param_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductDeployment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/deployments/{OpenApiUtilClient.get_encode_param(deployment_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_deployment_with_options_async(
        self,
        deployment_uid: str,
        request: adp_20210720_models.GetProductDeploymentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductDeploymentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.with_param_config):
            query['withParamConfig'] = request.with_param_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductDeployment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/deployments/{OpenApiUtilClient.get_encode_param(deployment_uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_version(
        self,
        uid: str,
        request: adp_20210720_models.GetProductVersionRequest,
    ) -> adp_20210720_models.GetProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_with_options(uid, request, headers, runtime)

    async def get_product_version_async(
        self,
        uid: str,
        request: adp_20210720_models.GetProductVersionRequest,
    ) -> adp_20210720_models.GetProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_version_with_options_async(uid, request, headers, runtime)

    def get_product_version_with_options(
        self,
        uid: str,
        request: adp_20210720_models.GetProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_documentation_url):
            query['withDocumentationURL'] = request.with_documentation_url
        if not UtilClient.is_unset(request.with_extend_resource_url):
            query['withExtendResourceURL'] = request.with_extend_resource_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_version_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.GetProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_documentation_url):
            query['withDocumentationURL'] = request.with_documentation_url
        if not UtilClient.is_unset(request.with_extend_resource_url):
            query['withExtendResourceURL'] = request.with_extend_resource_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_version_differences(
        self,
        uid: str,
        version_uid: str,
        request: adp_20210720_models.GetProductVersionDifferencesRequest,
    ) -> adp_20210720_models.GetProductVersionDifferencesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_differences_with_options(uid, version_uid, request, headers, runtime)

    async def get_product_version_differences_async(
        self,
        uid: str,
        version_uid: str,
        request: adp_20210720_models.GetProductVersionDifferencesRequest,
    ) -> adp_20210720_models.GetProductVersionDifferencesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_version_differences_with_options_async(uid, version_uid, request, headers, runtime)

    def get_product_version_differences_with_options(
        self,
        uid: str,
        version_uid: str,
        request: adp_20210720_models.GetProductVersionDifferencesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductVersionDifferencesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_version_uid):
            query['preVersionUID'] = request.pre_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersionDifferences',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}/versions/{OpenApiUtilClient.get_encode_param(version_uid)}/differences',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionDifferencesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_version_differences_with_options_async(
        self,
        uid: str,
        version_uid: str,
        request: adp_20210720_models.GetProductVersionDifferencesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductVersionDifferencesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_version_uid):
            query['preVersionUID'] = request.pre_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersionDifferences',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/integration/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}/versions/{OpenApiUtilClient.get_encode_param(version_uid)}/differences',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionDifferencesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_version_package(
        self,
        uid: str,
        request: adp_20210720_models.GetProductVersionPackageRequest,
    ) -> adp_20210720_models.GetProductVersionPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_package_with_options(uid, request, headers, runtime)

    async def get_product_version_package_async(
        self,
        uid: str,
        request: adp_20210720_models.GetProductVersionPackageRequest,
    ) -> adp_20210720_models.GetProductVersionPackageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_product_version_package_with_options_async(uid, request, headers, runtime)

    def get_product_version_package_with_options(
        self,
        uid: str,
        request: adp_20210720_models.GetProductVersionPackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductVersionPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.foundation_reference_uid):
            query['foundationReferenceUID'] = request.foundation_reference_uid
        if not UtilClient.is_unset(request.old_foundation_reference_uid):
            query['oldFoundationReferenceUID'] = request.old_foundation_reference_uid
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_content_type):
            query['packageContentType'] = request.package_content_type
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.package_uid):
            query['packageUID'] = request.package_uid
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        if not UtilClient.is_unset(request.with_url):
            query['withURL'] = request.with_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersionPackage',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/hosting/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/packages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_version_package_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.GetProductVersionPackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetProductVersionPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.foundation_reference_uid):
            query['foundationReferenceUID'] = request.foundation_reference_uid
        if not UtilClient.is_unset(request.old_foundation_reference_uid):
            query['oldFoundationReferenceUID'] = request.old_foundation_reference_uid
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_content_type):
            query['packageContentType'] = request.package_content_type
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.package_uid):
            query['packageUID'] = request.package_uid
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        if not UtilClient.is_unset(request.with_url):
            query['withURL'] = request.with_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersionPackage',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/hosting/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/packages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_snapshot(
        self,
        request: adp_20210720_models.GetResourceSnapshotRequest,
    ) -> adp_20210720_models.GetResourceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_snapshot_with_options(request, headers, runtime)

    async def get_resource_snapshot_async(
        self,
        request: adp_20210720_models.GetResourceSnapshotRequest,
    ) -> adp_20210720_models.GetResourceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_snapshot_with_options_async(request, headers, runtime)

    def get_resource_snapshot_with_options(
        self,
        request: adp_20210720_models.GetResourceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetResourceSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceSnapshot',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/resource-snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetResourceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_snapshot_with_options_async(
        self,
        request: adp_20210720_models.GetResourceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetResourceSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceSnapshot',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/resource-snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetResourceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_status(
        self,
        request: adp_20210720_models.GetWorkflowStatusRequest,
    ) -> adp_20210720_models.GetWorkflowStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workflow_status_with_options(request, headers, runtime)

    async def get_workflow_status_async(
        self,
        request: adp_20210720_models.GetWorkflowStatusRequest,
    ) -> adp_20210720_models.GetWorkflowStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workflow_status_with_options_async(request, headers, runtime)

    def get_workflow_status_with_options(
        self,
        request: adp_20210720_models.GetWorkflowStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetWorkflowStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workflow_type):
            query['workflowType'] = request.workflow_type
        if not UtilClient.is_unset(request.xuid):
            query['xuid'] = request.xuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowStatus',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/workflows/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetWorkflowStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_status_with_options_async(
        self,
        request: adp_20210720_models.GetWorkflowStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.GetWorkflowStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workflow_type):
            query['workflowType'] = request.workflow_type
        if not UtilClient.is_unset(request.xuid):
            query['xuid'] = request.xuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowStatus',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/workflows/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetWorkflowStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_environment_resource(
        self,
        uid: str,
        request: adp_20210720_models.InitEnvironmentResourceRequest,
    ) -> adp_20210720_models.InitEnvironmentResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.init_environment_resource_with_options(uid, request, headers, runtime)

    async def init_environment_resource_async(
        self,
        uid: str,
        request: adp_20210720_models.InitEnvironmentResourceRequest,
    ) -> adp_20210720_models.InitEnvironmentResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.init_environment_resource_with_options_async(uid, request, headers, runtime)

    def init_environment_resource_with_options(
        self,
        uid: str,
        request: adp_20210720_models.InitEnvironmentResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.InitEnvironmentResourceResponse:
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
        params = open_api_models.Params(
            action='InitEnvironmentResource',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.InitEnvironmentResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_environment_resource_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.InitEnvironmentResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.InitEnvironmentResourceResponse:
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
        params = open_api_models.Params(
            action='InitEnvironmentResource',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.InitEnvironmentResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_component_versions(
        self,
        uid: str,
        request: adp_20210720_models.ListComponentVersionsRequest,
    ) -> adp_20210720_models.ListComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_component_versions_with_options(uid, request, headers, runtime)

    async def list_component_versions_async(
        self,
        uid: str,
        request: adp_20210720_models.ListComponentVersionsRequest,
    ) -> adp_20210720_models.ListComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_component_versions_with_options_async(uid, request, headers, runtime)

    def list_component_versions_with_options(
        self,
        uid: str,
        tmp_req: adp_20210720_models.ListComponentVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListComponentVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListComponentVersionsShrinkRequest()
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
        params = open_api_models.Params(
            action='ListComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/components/{OpenApiUtilClient.get_encode_param(uid)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListComponentVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_component_versions_with_options_async(
        self,
        uid: str,
        tmp_req: adp_20210720_models.ListComponentVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListComponentVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListComponentVersionsShrinkRequest()
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
        params = open_api_models.Params(
            action='ListComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/components/{OpenApiUtilClient.get_encode_param(uid)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListComponentVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: adp_20210720_models.ListComponentsRequest,
    ) -> adp_20210720_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_components_with_options(request, headers, runtime)

    async def list_components_async(
        self,
        request: adp_20210720_models.ListComponentsRequest,
    ) -> adp_20210720_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_components_with_options_async(request, headers, runtime)

    def list_components_with_options(
        self,
        request: adp_20210720_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: adp_20210720_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_licenses(
        self,
        uid: str,
        request: adp_20210720_models.ListEnvironmentLicensesRequest,
    ) -> adp_20210720_models.ListEnvironmentLicensesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_licenses_with_options(uid, request, headers, runtime)

    async def list_environment_licenses_async(
        self,
        uid: str,
        request: adp_20210720_models.ListEnvironmentLicensesRequest,
    ) -> adp_20210720_models.ListEnvironmentLicensesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environment_licenses_with_options_async(uid, request, headers, runtime)

    def list_environment_licenses_with_options(
        self,
        uid: str,
        request: adp_20210720_models.ListEnvironmentLicensesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListEnvironmentLicensesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentLicenses',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/licenses',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentLicensesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_licenses_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.ListEnvironmentLicensesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListEnvironmentLicensesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentLicenses',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/licenses',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentLicensesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_nodes(
        self,
        uid: str,
        request: adp_20210720_models.ListEnvironmentNodesRequest,
    ) -> adp_20210720_models.ListEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_nodes_with_options(uid, request, headers, runtime)

    async def list_environment_nodes_async(
        self,
        uid: str,
        request: adp_20210720_models.ListEnvironmentNodesRequest,
    ) -> adp_20210720_models.ListEnvironmentNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environment_nodes_with_options_async(uid, request, headers, runtime)

    def list_environment_nodes_with_options(
        self,
        uid: str,
        request: adp_20210720_models.ListEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListEnvironmentNodesResponse:
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
        params = open_api_models.Params(
            action='ListEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_nodes_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.ListEnvironmentNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListEnvironmentNodesResponse:
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
        params = open_api_models.Params(
            action='ListEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_tunnels(
        self,
        uid: str,
    ) -> adp_20210720_models.ListEnvironmentTunnelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_tunnels_with_options(uid, headers, runtime)

    async def list_environment_tunnels_async(
        self,
        uid: str,
    ) -> adp_20210720_models.ListEnvironmentTunnelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environment_tunnels_with_options_async(uid, headers, runtime)

    def list_environment_tunnels_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListEnvironmentTunnelsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListEnvironmentTunnels',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/tunnels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentTunnelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_tunnels_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListEnvironmentTunnelsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListEnvironmentTunnels',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/tunnels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentTunnelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        request: adp_20210720_models.ListEnvironmentsRequest,
    ) -> adp_20210720_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(request, headers, runtime)

    async def list_environments_async(
        self,
        request: adp_20210720_models.ListEnvironmentsRequest,
    ) -> adp_20210720_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(request, headers, runtime)

    def list_environments_with_options(
        self,
        request: adp_20210720_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListEnvironmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_uid):
            query['clusterUID'] = request.cluster_uid
        if not UtilClient.is_unset(request.foundation_type):
            query['foundationType'] = request.foundation_type
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.instance_status):
            query['instanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.vendor_type):
            query['vendorType'] = request.vendor_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        request: adp_20210720_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListEnvironmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_uid):
            query['clusterUID'] = request.cluster_uid
        if not UtilClient.is_unset(request.foundation_type):
            query['foundationType'] = request.foundation_type
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.instance_status):
            query['instanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.vendor_type):
            query['vendorType'] = request.vendor_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_foundation_component_versions(
        self,
        uid: str,
    ) -> adp_20210720_models.ListFoundationComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_component_versions_with_options(uid, headers, runtime)

    async def list_foundation_component_versions_async(
        self,
        uid: str,
    ) -> adp_20210720_models.ListFoundationComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_foundation_component_versions_with_options_async(uid, headers, runtime)

    def list_foundation_component_versions_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListFoundationComponentVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFoundationComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation/versions/{OpenApiUtilClient.get_encode_param(uid)}/component-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationComponentVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_foundation_component_versions_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListFoundationComponentVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFoundationComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation/versions/{OpenApiUtilClient.get_encode_param(uid)}/component-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationComponentVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_foundation_reference_components(
        self,
        request: adp_20210720_models.ListFoundationReferenceComponentsRequest,
    ) -> adp_20210720_models.ListFoundationReferenceComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_reference_components_with_options(request, headers, runtime)

    async def list_foundation_reference_components_async(
        self,
        request: adp_20210720_models.ListFoundationReferenceComponentsRequest,
    ) -> adp_20210720_models.ListFoundationReferenceComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_foundation_reference_components_with_options_async(request, headers, runtime)

    def list_foundation_reference_components_with_options(
        self,
        request: adp_20210720_models.ListFoundationReferenceComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListFoundationReferenceComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.foundation_reference_uid):
            query['foundationReferenceUID'] = request.foundation_reference_uid
        if not UtilClient.is_unset(request.foundation_version_uid):
            query['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.only_enabled):
            query['onlyEnabled'] = request.only_enabled
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoundationReferenceComponents',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/component-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationReferenceComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_foundation_reference_components_with_options_async(
        self,
        request: adp_20210720_models.ListFoundationReferenceComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListFoundationReferenceComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.foundation_reference_uid):
            query['foundationReferenceUID'] = request.foundation_reference_uid
        if not UtilClient.is_unset(request.foundation_version_uid):
            query['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.only_enabled):
            query['onlyEnabled'] = request.only_enabled
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoundationReferenceComponents',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/component-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationReferenceComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_foundation_versions(
        self,
        request: adp_20210720_models.ListFoundationVersionsRequest,
    ) -> adp_20210720_models.ListFoundationVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_versions_with_options(request, headers, runtime)

    async def list_foundation_versions_async(
        self,
        request: adp_20210720_models.ListFoundationVersionsRequest,
    ) -> adp_20210720_models.ListFoundationVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_foundation_versions_with_options_async(request, headers, runtime)

    def list_foundation_versions_with_options(
        self,
        request: adp_20210720_models.ListFoundationVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListFoundationVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sort_direct):
            query['sortDirect'] = request.sort_direct
        if not UtilClient.is_unset(request.sort_key):
            query['sortKey'] = request.sort_key
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoundationVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_foundation_versions_with_options_async(
        self,
        request: adp_20210720_models.ListFoundationVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListFoundationVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sort_direct):
            query['sortDirect'] = request.sort_direct
        if not UtilClient.is_unset(request.sort_key):
            query['sortKey'] = request.sort_key
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoundationVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_component_versions(
        self,
        uid: str,
        request: adp_20210720_models.ListProductComponentVersionsRequest,
    ) -> adp_20210720_models.ListProductComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_component_versions_with_options(uid, request, headers, runtime)

    async def list_product_component_versions_async(
        self,
        uid: str,
        request: adp_20210720_models.ListProductComponentVersionsRequest,
    ) -> adp_20210720_models.ListProductComponentVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_component_versions_with_options_async(uid, request, headers, runtime)

    def list_product_component_versions_with_options(
        self,
        uid: str,
        request: adp_20210720_models.ListProductComponentVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductComponentVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_direct):
            query['sortDirect'] = request.sort_direct
        if not UtilClient.is_unset(request.sort_key):
            query['sortKey'] = request.sort_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/component-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductComponentVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_component_versions_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.ListProductComponentVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductComponentVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_direct):
            query['sortDirect'] = request.sort_direct
        if not UtilClient.is_unset(request.sort_key):
            query['sortKey'] = request.sort_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/component-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductComponentVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_deployments(
        self,
        request: adp_20210720_models.ListProductDeploymentsRequest,
    ) -> adp_20210720_models.ListProductDeploymentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_deployments_with_options(request, headers, runtime)

    async def list_product_deployments_async(
        self,
        request: adp_20210720_models.ListProductDeploymentsRequest,
    ) -> adp_20210720_models.ListProductDeploymentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_deployments_with_options_async(request, headers, runtime)

    def list_product_deployments_with_options(
        self,
        request: adp_20210720_models.ListProductDeploymentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductDeploymentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductDeployments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/deployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_deployments_with_options_async(
        self,
        request: adp_20210720_models.ListProductDeploymentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductDeploymentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductDeployments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/deployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductDeploymentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_environments(
        self,
        uid: str,
        request: adp_20210720_models.ListProductEnvironmentsRequest,
    ) -> adp_20210720_models.ListProductEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_environments_with_options(uid, request, headers, runtime)

    async def list_product_environments_async(
        self,
        uid: str,
        request: adp_20210720_models.ListProductEnvironmentsRequest,
    ) -> adp_20210720_models.ListProductEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_environments_with_options_async(uid, request, headers, runtime)

    def list_product_environments_with_options(
        self,
        uid: str,
        tmp_req: adp_20210720_models.ListProductEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductEnvironmentsResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListProductEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.options), 'options', 'json')
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.compatible_product_version_uid):
            query['compatibleProductVersionUID'] = request.compatible_product_version_uid
        if not UtilClient.is_unset(request.env_type):
            query['envType'] = request.env_type
        if not UtilClient.is_unset(request.options_shrink):
            query['options'] = request.options_shrink
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        if not UtilClient.is_unset(request.product_version_spec_uid):
            query['productVersionSpecUID'] = request.product_version_spec_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductEnvironments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/hosting/products/{OpenApiUtilClient.get_encode_param(uid)}/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_environments_with_options_async(
        self,
        uid: str,
        tmp_req: adp_20210720_models.ListProductEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductEnvironmentsResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListProductEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.options), 'options', 'json')
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.compatible_product_version_uid):
            query['compatibleProductVersionUID'] = request.compatible_product_version_uid
        if not UtilClient.is_unset(request.env_type):
            query['envType'] = request.env_type
        if not UtilClient.is_unset(request.options_shrink):
            query['options'] = request.options_shrink
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        if not UtilClient.is_unset(request.product_version_spec_uid):
            query['productVersionSpecUID'] = request.product_version_spec_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductEnvironments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/hosting/products/{OpenApiUtilClient.get_encode_param(uid)}/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_foundation_references(
        self,
        uid: str,
    ) -> adp_20210720_models.ListProductFoundationReferencesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_foundation_references_with_options(uid, headers, runtime)

    async def list_product_foundation_references_async(
        self,
        uid: str,
    ) -> adp_20210720_models.ListProductFoundationReferencesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_foundation_references_with_options_async(uid, headers, runtime)

    def list_product_foundation_references_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductFoundationReferencesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProductFoundationReferences',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/foundation-references',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductFoundationReferencesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_foundation_references_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductFoundationReferencesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProductFoundationReferences',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/foundation-references',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductFoundationReferencesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_instance_configs(
        self,
        request: adp_20210720_models.ListProductInstanceConfigsRequest,
    ) -> adp_20210720_models.ListProductInstanceConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_instance_configs_with_options(request, headers, runtime)

    async def list_product_instance_configs_async(
        self,
        request: adp_20210720_models.ListProductInstanceConfigsRequest,
    ) -> adp_20210720_models.ListProductInstanceConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_instance_configs_with_options_async(request, headers, runtime)

    def list_product_instance_configs_with_options(
        self,
        request: adp_20210720_models.ListProductInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductInstanceConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.param_type):
            query['paramType'] = request.param_type
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductInstanceConfigs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_instance_configs_with_options_async(
        self,
        request: adp_20210720_models.ListProductInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductInstanceConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.param_type):
            query['paramType'] = request.param_type
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductInstanceConfigs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_instances(
        self,
        request: adp_20210720_models.ListProductInstancesRequest,
    ) -> adp_20210720_models.ListProductInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_instances_with_options(request, headers, runtime)

    async def list_product_instances_async(
        self,
        request: adp_20210720_models.ListProductInstancesRequest,
    ) -> adp_20210720_models.ListProductInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_instances_with_options_async(request, headers, runtime)

    def list_product_instances_with_options(
        self,
        tmp_req: adp_20210720_models.ListProductInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListProductInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.options), 'options', 'json')
        query = {}
        if not UtilClient.is_unset(request.env_uid):
            query['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.options_shrink):
            query['options'] = request.options_shrink
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductInstances',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_instances_with_options_async(
        self,
        tmp_req: adp_20210720_models.ListProductInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListProductInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.options), 'options', 'json')
        query = {}
        if not UtilClient.is_unset(request.env_uid):
            query['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.options_shrink):
            query['options'] = request.options_shrink
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductInstances',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_version_configs(
        self,
        uid: str,
        request: adp_20210720_models.ListProductVersionConfigsRequest,
    ) -> adp_20210720_models.ListProductVersionConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_version_configs_with_options(uid, request, headers, runtime)

    async def list_product_version_configs_async(
        self,
        uid: str,
        request: adp_20210720_models.ListProductVersionConfigsRequest,
    ) -> adp_20210720_models.ListProductVersionConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_version_configs_with_options_async(uid, request, headers, runtime)

    def list_product_version_configs_with_options(
        self,
        uid: str,
        request: adp_20210720_models.ListProductVersionConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductVersionConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_type):
            query['configType'] = request.config_type
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameter):
            query['parameter'] = request.parameter
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersionConfigs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductVersionConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_version_configs_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.ListProductVersionConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductVersionConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_type):
            query['configType'] = request.config_type
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameter):
            query['parameter'] = request.parameter
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersionConfigs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductVersionConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_versions(
        self,
        request: adp_20210720_models.ListProductVersionsRequest,
    ) -> adp_20210720_models.ListProductVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_versions_with_options(request, headers, runtime)

    async def list_product_versions_async(
        self,
        request: adp_20210720_models.ListProductVersionsRequest,
    ) -> adp_20210720_models.ListProductVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_product_versions_with_options_async(request, headers, runtime)

    def list_product_versions_with_options(
        self,
        tmp_req: adp_20210720_models.ListProductVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListProductVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        if not UtilClient.is_unset(tmp_req.supported_foundation_types):
            request.supported_foundation_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supported_foundation_types, 'supportedFoundationTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        if not UtilClient.is_unset(request.product_name):
            query['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            query['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.released):
            query['released'] = request.released
        if not UtilClient.is_unset(request.supported_foundation_types_shrink):
            query['supportedFoundationTypes'] = request.supported_foundation_types_shrink
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_versions_with_options_async(
        self,
        tmp_req: adp_20210720_models.ListProductVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListProductVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        if not UtilClient.is_unset(tmp_req.supported_foundation_types):
            request.supported_foundation_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supported_foundation_types, 'supportedFoundationTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        if not UtilClient.is_unset(request.product_name):
            query['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            query['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.released):
            query['released'] = request.released
        if not UtilClient.is_unset(request.supported_foundation_types_shrink):
            query['supportedFoundationTypes'] = request.supported_foundation_types_shrink
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: adp_20210720_models.ListProductsRequest,
    ) -> adp_20210720_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_products_with_options(request, headers, runtime)

    async def list_products_async(
        self,
        request: adp_20210720_models.ListProductsRequest,
    ) -> adp_20210720_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_products_with_options_async(request, headers, runtime)

    def list_products_with_options(
        self,
        request: adp_20210720_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: adp_20210720_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_task_logs(
        self,
        step_name: str,
        task_name: str,
        request: adp_20210720_models.ListWorkflowTaskLogsRequest,
    ) -> adp_20210720_models.ListWorkflowTaskLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflow_task_logs_with_options(step_name, task_name, request, headers, runtime)

    async def list_workflow_task_logs_async(
        self,
        step_name: str,
        task_name: str,
        request: adp_20210720_models.ListWorkflowTaskLogsRequest,
    ) -> adp_20210720_models.ListWorkflowTaskLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workflow_task_logs_with_options_async(step_name, task_name, request, headers, runtime)

    def list_workflow_task_logs_with_options(
        self,
        step_name: str,
        task_name: str,
        tmp_req: adp_20210720_models.ListWorkflowTaskLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListWorkflowTaskLogsResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListWorkflowTaskLogsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_values):
            request.filter_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_values, 'filterValues', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_values_shrink):
            query['filterValues'] = request.filter_values_shrink
        if not UtilClient.is_unset(request.order_type):
            query['orderType'] = request.order_type
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.workflow_type):
            query['workflowType'] = request.workflow_type
        if not UtilClient.is_unset(request.xuid):
            query['xuid'] = request.xuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowTaskLogs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/workflows/steps/{OpenApiUtilClient.get_encode_param(step_name)}/tasks/{OpenApiUtilClient.get_encode_param(task_name)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListWorkflowTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_task_logs_with_options_async(
        self,
        step_name: str,
        task_name: str,
        tmp_req: adp_20210720_models.ListWorkflowTaskLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ListWorkflowTaskLogsResponse:
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListWorkflowTaskLogsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_values):
            request.filter_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_values, 'filterValues', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_values_shrink):
            query['filterValues'] = request.filter_values_shrink
        if not UtilClient.is_unset(request.order_type):
            query['orderType'] = request.order_type
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.workflow_type):
            query['workflowType'] = request.workflow_type
        if not UtilClient.is_unset(request.xuid):
            query['xuid'] = request.xuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowTaskLogs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/workflows/steps/{OpenApiUtilClient.get_encode_param(step_name)}/tasks/{OpenApiUtilClient.get_encode_param(task_name)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListWorkflowTaskLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_environment_tunnel(
        self,
        uid: str,
        request: adp_20210720_models.PutEnvironmentTunnelRequest,
    ) -> adp_20210720_models.PutEnvironmentTunnelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_environment_tunnel_with_options(uid, request, headers, runtime)

    async def put_environment_tunnel_async(
        self,
        uid: str,
        request: adp_20210720_models.PutEnvironmentTunnelRequest,
    ) -> adp_20210720_models.PutEnvironmentTunnelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_environment_tunnel_with_options_async(uid, request, headers, runtime)

    def put_environment_tunnel_with_options(
        self,
        uid: str,
        request: adp_20210720_models.PutEnvironmentTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.PutEnvironmentTunnelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tunnel_config):
            body['tunnelConfig'] = request.tunnel_config
        if not UtilClient.is_unset(request.tunnel_type):
            body['tunnelType'] = request.tunnel_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutEnvironmentTunnel',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/tunnels',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.PutEnvironmentTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_environment_tunnel_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.PutEnvironmentTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.PutEnvironmentTunnelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tunnel_config):
            body['tunnelConfig'] = request.tunnel_config
        if not UtilClient.is_unset(request.tunnel_type):
            body['tunnelType'] = request.tunnel_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutEnvironmentTunnel',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/tunnels',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.PutEnvironmentTunnelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_product_instance_config(
        self,
        request: adp_20210720_models.PutProductInstanceConfigRequest,
    ) -> adp_20210720_models.PutProductInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_product_instance_config_with_options(request, headers, runtime)

    async def put_product_instance_config_async(
        self,
        request: adp_20210720_models.PutProductInstanceConfigRequest,
    ) -> adp_20210720_models.PutProductInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_product_instance_config_with_options_async(request, headers, runtime)

    def put_product_instance_config_with_options(
        self,
        request: adp_20210720_models.PutProductInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.PutProductInstanceConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_uid):
            body['componentUID'] = request.component_uid
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.config_uid):
            body['configUID'] = request.config_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_name):
            body['parentComponentName'] = request.parent_component_name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutProductInstanceConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/configs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.PutProductInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_product_instance_config_with_options_async(
        self,
        request: adp_20210720_models.PutProductInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.PutProductInstanceConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_uid):
            body['componentUID'] = request.component_uid
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.config_uid):
            body['configUID'] = request.config_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_name):
            body['parentComponentName'] = request.parent_component_name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutProductInstanceConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-instances/configs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.PutProductInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_environment_foundation_reference(
        self,
        uid: str,
        foundation_reference_uid: str,
    ) -> adp_20210720_models.SetEnvironmentFoundationReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_environment_foundation_reference_with_options(uid, foundation_reference_uid, headers, runtime)

    async def set_environment_foundation_reference_async(
        self,
        uid: str,
        foundation_reference_uid: str,
    ) -> adp_20210720_models.SetEnvironmentFoundationReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_environment_foundation_reference_with_options_async(uid, foundation_reference_uid, headers, runtime)

    def set_environment_foundation_reference_with_options(
        self,
        uid: str,
        foundation_reference_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.SetEnvironmentFoundationReferenceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SetEnvironmentFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/foundation-references/{OpenApiUtilClient.get_encode_param(foundation_reference_uid)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.SetEnvironmentFoundationReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_environment_foundation_reference_with_options_async(
        self,
        uid: str,
        foundation_reference_uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.SetEnvironmentFoundationReferenceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SetEnvironmentFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/foundation-references/{OpenApiUtilClient.get_encode_param(foundation_reference_uid)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.SetEnvironmentFoundationReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        uid: str,
        request: adp_20210720_models.UpdateEnvironmentRequest,
    ) -> adp_20210720_models.UpdateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(uid, request, headers, runtime)

    async def update_environment_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateEnvironmentRequest,
    ) -> adp_20210720_models.UpdateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_with_options_async(uid, request, headers, runtime)

    def update_environment_with_options(
        self,
        uid: str,
        request: adp_20210720_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateEnvironmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_configs):
            body['advancedConfigs'] = request.advanced_configs
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
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateEnvironmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_configs):
            body['advancedConfigs'] = request.advanced_configs
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
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment_node(
        self,
        uid: str,
        node_uid: str,
        request: adp_20210720_models.UpdateEnvironmentNodeRequest,
    ) -> adp_20210720_models.UpdateEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_node_with_options(uid, node_uid, request, headers, runtime)

    async def update_environment_node_async(
        self,
        uid: str,
        node_uid: str,
        request: adp_20210720_models.UpdateEnvironmentNodeRequest,
    ) -> adp_20210720_models.UpdateEnvironmentNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_node_with_options_async(uid, node_uid, request, headers, runtime)

    def update_environment_node_with_options(
        self,
        uid: str,
        node_uid: str,
        request: adp_20210720_models.UpdateEnvironmentNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateEnvironmentNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_disk):
            body['applicationDisk'] = request.application_disk
        if not UtilClient.is_unset(request.etcd_disk):
            body['etcdDisk'] = request.etcd_disk
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.trident_system_disk):
            body['tridentSystemDisk'] = request.trident_system_disk
        if not UtilClient.is_unset(request.trident_system_size_disk):
            body['tridentSystemSizeDisk'] = request.trident_system_size_disk
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes/{OpenApiUtilClient.get_encode_param(node_uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_node_with_options_async(
        self,
        uid: str,
        node_uid: str,
        request: adp_20210720_models.UpdateEnvironmentNodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateEnvironmentNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_disk):
            body['applicationDisk'] = request.application_disk
        if not UtilClient.is_unset(request.etcd_disk):
            body['etcdDisk'] = request.etcd_disk
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.trident_system_disk):
            body['tridentSystemDisk'] = request.trident_system_disk
        if not UtilClient.is_unset(request.trident_system_size_disk):
            body['tridentSystemSizeDisk'] = request.trident_system_size_disk
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/nodes/{OpenApiUtilClient.get_encode_param(node_uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment_product_version(
        self,
        uid: str,
        request: adp_20210720_models.UpdateEnvironmentProductVersionRequest,
    ) -> adp_20210720_models.UpdateEnvironmentProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_product_version_with_options(uid, request, headers, runtime)

    async def update_environment_product_version_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateEnvironmentProductVersionRequest,
    ) -> adp_20210720_models.UpdateEnvironmentProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_product_version_with_options_async(uid, request, headers, runtime)

    def update_environment_product_version_with_options(
        self,
        uid: str,
        request: adp_20210720_models.UpdateEnvironmentProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateEnvironmentProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.old_product_version_spec_uid):
            body['oldProductVersionSpecUID'] = request.old_product_version_spec_uid
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.product_version_spec_uid):
            body['productVersionSpecUID'] = request.product_version_spec_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironmentProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/product-versions',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_product_version_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateEnvironmentProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateEnvironmentProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.old_product_version_spec_uid):
            body['oldProductVersionSpecUID'] = request.old_product_version_spec_uid
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.product_version_spec_uid):
            body['productVersionSpecUID'] = request.product_version_spec_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironmentProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/product-versions',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_foundation_component_reference(
        self,
        uid: str,
        component_reference_uid: str,
        request: adp_20210720_models.UpdateFoundationComponentReferenceRequest,
    ) -> adp_20210720_models.UpdateFoundationComponentReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_foundation_component_reference_with_options(uid, component_reference_uid, request, headers, runtime)

    async def update_foundation_component_reference_async(
        self,
        uid: str,
        component_reference_uid: str,
        request: adp_20210720_models.UpdateFoundationComponentReferenceRequest,
    ) -> adp_20210720_models.UpdateFoundationComponentReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_foundation_component_reference_with_options_async(uid, component_reference_uid, request, headers, runtime)

    def update_foundation_component_reference_with_options(
        self,
        uid: str,
        component_reference_uid: str,
        request: adp_20210720_models.UpdateFoundationComponentReferenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateFoundationComponentReferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFoundationComponentReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/{OpenApiUtilClient.get_encode_param(uid)}/components/{OpenApiUtilClient.get_encode_param(component_reference_uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateFoundationComponentReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_foundation_component_reference_with_options_async(
        self,
        uid: str,
        component_reference_uid: str,
        request: adp_20210720_models.UpdateFoundationComponentReferenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateFoundationComponentReferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFoundationComponentReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/{OpenApiUtilClient.get_encode_param(uid)}/components/{OpenApiUtilClient.get_encode_param(component_reference_uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateFoundationComponentReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_foundation_reference(
        self,
        uid: str,
        request: adp_20210720_models.UpdateFoundationReferenceRequest,
    ) -> adp_20210720_models.UpdateFoundationReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_foundation_reference_with_options(uid, request, headers, runtime)

    async def update_foundation_reference_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateFoundationReferenceRequest,
    ) -> adp_20210720_models.UpdateFoundationReferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_foundation_reference_with_options_async(uid, request, headers, runtime)

    def update_foundation_reference_with_options(
        self,
        uid: str,
        request: adp_20210720_models.UpdateFoundationReferenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateFoundationReferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_config):
            body['clusterConfig'] = request.cluster_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/{OpenApiUtilClient.get_encode_param(uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateFoundationReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_foundation_reference_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateFoundationReferenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateFoundationReferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_config):
            body['clusterConfig'] = request.cluster_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/foundation-references/{OpenApiUtilClient.get_encode_param(uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateFoundationReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductRequest,
    ) -> adp_20210720_models.UpdateProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_with_options(uid, request, headers, runtime)

    async def update_product_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductRequest,
    ) -> adp_20210720_models.UpdateProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_with_options_async(uid, request, headers, runtime)

    def update_product_with_options(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.categories):
            body['categories'] = request.categories
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.vendor):
            body['vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.categories):
            body['categories'] = request.categories
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.vendor):
            body['vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/products/{OpenApiUtilClient.get_encode_param(uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product_component_version(
        self,
        uid: str,
        relation_uid: str,
        request: adp_20210720_models.UpdateProductComponentVersionRequest,
    ) -> adp_20210720_models.UpdateProductComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_component_version_with_options(uid, relation_uid, request, headers, runtime)

    async def update_product_component_version_async(
        self,
        uid: str,
        relation_uid: str,
        request: adp_20210720_models.UpdateProductComponentVersionRequest,
    ) -> adp_20210720_models.UpdateProductComponentVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_component_version_with_options_async(uid, relation_uid, request, headers, runtime)

    def update_product_component_version_with_options(
        self,
        uid: str,
        relation_uid: str,
        request: adp_20210720_models.UpdateProductComponentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductComponentVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.new_component_version_uid):
            body['newComponentVersionUID'] = request.new_component_version_uid
        if not UtilClient.is_unset(request.policy):
            body['policy'] = request.policy
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/relations/{OpenApiUtilClient.get_encode_param(relation_uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_component_version_with_options_async(
        self,
        uid: str,
        relation_uid: str,
        request: adp_20210720_models.UpdateProductComponentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductComponentVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.new_component_version_uid):
            body['newComponentVersionUID'] = request.new_component_version_uid
        if not UtilClient.is_unset(request.policy):
            body['policy'] = request.policy
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/relations/{OpenApiUtilClient.get_encode_param(relation_uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductComponentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product_foundation_version(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductFoundationVersionRequest,
    ) -> adp_20210720_models.UpdateProductFoundationVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_foundation_version_with_options(uid, request, headers, runtime)

    async def update_product_foundation_version_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductFoundationVersionRequest,
    ) -> adp_20210720_models.UpdateProductFoundationVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_foundation_version_with_options_async(uid, request, headers, runtime)

    def update_product_foundation_version_with_options(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductFoundationVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductFoundationVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductFoundationVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/foundation',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductFoundationVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_foundation_version_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductFoundationVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductFoundationVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductFoundationVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/foundation',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductFoundationVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product_version(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductVersionRequest,
    ) -> adp_20210720_models.UpdateProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_version_with_options(uid, request, headers, runtime)

    async def update_product_version_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductVersionRequest,
    ) -> adp_20210720_models.UpdateProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_version_with_options_async(uid, request, headers, runtime)

    def update_product_version_with_options(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_integration):
            body['continuousIntegration'] = request.continuous_integration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_version_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.UpdateProductVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_integration):
            body['continuousIntegration'] = request.continuous_integration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product_version_config(
        self,
        uid: str,
        config_uid: str,
        request: adp_20210720_models.UpdateProductVersionConfigRequest,
    ) -> adp_20210720_models.UpdateProductVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_version_config_with_options(uid, config_uid, request, headers, runtime)

    async def update_product_version_config_async(
        self,
        uid: str,
        config_uid: str,
        request: adp_20210720_models.UpdateProductVersionConfigRequest,
    ) -> adp_20210720_models.UpdateProductVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_product_version_config_with_options_async(uid, config_uid, request, headers, runtime)

    def update_product_version_config_with_options(
        self,
        uid: str,
        config_uid: str,
        request: adp_20210720_models.UpdateProductVersionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductVersionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/configs/{OpenApiUtilClient.get_encode_param(config_uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_version_config_with_options_async(
        self,
        uid: str,
        config_uid: str,
        request: adp_20210720_models.UpdateProductVersionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.UpdateProductVersionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/product-versions/{OpenApiUtilClient.get_encode_param(uid)}/configs/{OpenApiUtilClient.get_encode_param(config_uid)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_environment_tunnel(
        self,
        uid: str,
        request: adp_20210720_models.ValidateEnvironmentTunnelRequest,
    ) -> adp_20210720_models.ValidateEnvironmentTunnelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_environment_tunnel_with_options(uid, request, headers, runtime)

    async def validate_environment_tunnel_async(
        self,
        uid: str,
        request: adp_20210720_models.ValidateEnvironmentTunnelRequest,
    ) -> adp_20210720_models.ValidateEnvironmentTunnelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_environment_tunnel_with_options_async(uid, request, headers, runtime)

    def validate_environment_tunnel_with_options(
        self,
        uid: str,
        request: adp_20210720_models.ValidateEnvironmentTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ValidateEnvironmentTunnelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tunnel_config):
            body['tunnelConfig'] = request.tunnel_config
        if not UtilClient.is_unset(request.tunnel_type):
            body['tunnelType'] = request.tunnel_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateEnvironmentTunnel',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/tunnels/validation',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ValidateEnvironmentTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_environment_tunnel_with_options_async(
        self,
        uid: str,
        request: adp_20210720_models.ValidateEnvironmentTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> adp_20210720_models.ValidateEnvironmentTunnelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tunnel_config):
            body['tunnelConfig'] = request.tunnel_config
        if not UtilClient.is_unset(request.tunnel_type):
            body['tunnelType'] = request.tunnel_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateEnvironmentTunnel',
            version='2021-07-20',
            protocol='HTTPS',
            pathname=f'/api/v2/environments/{OpenApiUtilClient.get_encode_param(uid)}/tunnels/validation',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ValidateEnvironmentTunnelResponse(),
            await self.call_api_async(params, req, runtime)
        )
