# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_airec20181012 import models as airec_20181012_models
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
        self._endpoint = self.get_endpoint('airec', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_dataset(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.AttachDatasetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_dataset_with_options(instance_id, version_id, headers, runtime)

    async def attach_dataset_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.AttachDatasetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_dataset_with_options_async(instance_id, version_id, headers, runtime)

    def attach_dataset_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.AttachDatasetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachDataset',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/actions/current',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.AttachDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_dataset_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.AttachDatasetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachDataset',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/actions/current',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.AttachDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diversify(
        self,
        instance_id: str,
    ) -> airec_20181012_models.CreateDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_diversify_with_options(instance_id, headers, runtime)

    async def create_diversify_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.CreateDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_diversify_with_options_async(instance_id, headers, runtime)

    def create_diversify_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateDiversifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diversify_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateDiversifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(self) -> airec_20181012_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(headers, runtime)

    async def create_instance_async(self) -> airec_20181012_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(headers, runtime)

    def create_instance_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mix(
        self,
        instance_id: str,
    ) -> airec_20181012_models.CreateMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_mix_with_options(instance_id, headers, runtime)

    async def create_mix_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.CreateMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_mix_with_options_async(instance_id, headers, runtime)

    def create_mix_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateMixResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mix_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateMixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        instance_id: str,
    ) -> airec_20181012_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rule_with_options(instance_id, headers, runtime)

    async def create_rule_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_rule_with_options_async(instance_id, headers, runtime)

    def create_rule_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene(
        self,
        instance_id: str,
        request: airec_20181012_models.CreateSceneRequest,
    ) -> airec_20181012_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scene_with_options(instance_id, request, headers, runtime)

    async def create_scene_async(
        self,
        instance_id: str,
        request: airec_20181012_models.CreateSceneRequest,
    ) -> airec_20181012_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_scene_with_options_async(instance_id, request, headers, runtime)

    def create_scene_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.CreateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_set(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.DeleteDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_set_with_options(instance_id, version_id, headers, runtime)

    async def delete_data_set_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.DeleteDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_data_set_with_options_async(instance_id, version_id, headers, runtime)

    def delete_data_set_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DeleteDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DeleteDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_set_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DeleteDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DeleteDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_diversify(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.DeleteDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_diversify_with_options(instance_id, name, headers, runtime)

    async def delete_diversify_async(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.DeleteDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_diversify_with_options_async(instance_id, name, headers, runtime)

    def delete_diversify_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DeleteDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies/{{Name}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DeleteDiversifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_diversify_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DeleteDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies/{{Name}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DeleteDiversifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mix(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.DeleteMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_mix_with_options(instance_id, name, headers, runtime)

    async def delete_mix_async(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.DeleteMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_mix_with_options_async(instance_id, name, headers, runtime)

    def delete_mix_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DeleteMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes/{{Name}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DeleteMixResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mix_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DeleteMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes/{{Name}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DeleteMixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20181012_models.DeleteSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scene_with_options(instance_id, scene_id, headers, runtime)

    async def delete_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20181012_models.DeleteSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def delete_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DeleteSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DeleteSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DeleteSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_set_message(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.DescribeDataSetMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_data_set_message_with_options(instance_id, version_id, headers, runtime)

    async def describe_data_set_message_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.DescribeDataSetMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_data_set_message_with_options_async(instance_id, version_id, headers, runtime)

    def describe_data_set_message_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeDataSetMessageResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataSetMessage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeDataSetMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_set_message_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeDataSetMessageResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataSetMessage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeDataSetMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_set_report(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.DescribeDataSetReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_data_set_report_with_options(instance_id, version_id, headers, runtime)

    async def describe_data_set_report_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.DescribeDataSetReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_data_set_report_with_options_async(instance_id, version_id, headers, runtime)

    def describe_data_set_report_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeDataSetReportResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataSetReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeDataSetReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_set_report_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeDataSetReportResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataSetReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeDataSetReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diversify(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.DescribeDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_diversify_with_options(instance_id, name, headers, runtime)

    async def describe_diversify_async(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.DescribeDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_diversify_with_options_async(instance_id, name, headers, runtime)

    def describe_diversify_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies/{{Name}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeDiversifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diversify_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies/{{Name}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeDiversifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exposure_settings(
        self,
        instance_id: str,
    ) -> airec_20181012_models.DescribeExposureSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_exposure_settings_with_options(instance_id, headers, runtime)

    async def describe_exposure_settings_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.DescribeExposureSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_exposure_settings_with_options_async(instance_id, headers, runtime)

    def describe_exposure_settings_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeExposureSettingsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExposureSettings',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/exposure-settings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeExposureSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exposure_settings_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeExposureSettingsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExposureSettings',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/exposure-settings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeExposureSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        instance_id: str,
    ) -> airec_20181012_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    async def describe_instance_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_with_options_async(instance_id, headers, runtime)

    def describe_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mix(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.DescribeMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_mix_with_options(instance_id, name, headers, runtime)

    async def describe_mix_async(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.DescribeMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_mix_with_options_async(instance_id, name, headers, runtime)

    def describe_mix_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes/{{Name}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeMixResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mix_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes/{{Name}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeMixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quota(
        self,
        instance_id: str,
    ) -> airec_20181012_models.DescribeQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quota_with_options(instance_id, headers, runtime)

    async def describe_quota_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.DescribeQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_quota_with_options_async(instance_id, headers, runtime)

    def describe_quota_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQuota',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quota_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQuota',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: airec_20181012_models.DescribeRegionsRequest,
    ) -> airec_20181012_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: airec_20181012_models.DescribeRegionsRequest,
    ) -> airec_20181012_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        request: airec_20181012_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/configurations/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: airec_20181012_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/configurations/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20181012_models.DescribeRuleRequest,
    ) -> airec_20181012_models.DescribeRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rule_with_options(instance_id, rule_id, request, headers, runtime)

    async def describe_rule_async(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20181012_models.DescribeRuleRequest,
    ) -> airec_20181012_models.DescribeRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rule_with_options_async(instance_id, rule_id, request, headers, runtime)

    def describe_rule_with_options(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20181012_models.DescribeRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRule',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules/{{RuleId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_with_options_async(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20181012_models.DescribeRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRule',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules/{{RuleId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20181012_models.DescribeSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scene_with_options(instance_id, scene_id, headers, runtime)

    async def describe_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20181012_models.DescribeSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScene',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScene',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_throughput(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20181012_models.DescribeSceneThroughputResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scene_throughput_with_options(instance_id, scene_id, headers, runtime)

    async def describe_scene_throughput_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20181012_models.DescribeSceneThroughputResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scene_throughput_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_scene_throughput_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeSceneThroughputResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneThroughput',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}/throughput',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeSceneThroughputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_throughput_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeSceneThroughputResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneThroughput',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}/throughput',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeSceneThroughputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_report_detail(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeSyncReportDetailRequest,
    ) -> airec_20181012_models.DescribeSyncReportDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_sync_report_detail_with_options(instance_id, request, headers, runtime)

    async def describe_sync_report_detail_async(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeSyncReportDetailRequest,
    ) -> airec_20181012_models.DescribeSyncReportDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_sync_report_detail_with_options_async(instance_id, request, headers, runtime)

    def describe_sync_report_detail_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeSyncReportDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeSyncReportDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.level_type):
            query['LevelType'] = request.level_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportDetail',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeSyncReportDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_report_detail_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeSyncReportDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeSyncReportDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.level_type):
            query['LevelType'] = request.level_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportDetail',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeSyncReportDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_report_outliers(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeSyncReportOutliersRequest,
    ) -> airec_20181012_models.DescribeSyncReportOutliersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_sync_report_outliers_with_options(instance_id, request, headers, runtime)

    async def describe_sync_report_outliers_async(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeSyncReportOutliersRequest,
    ) -> airec_20181012_models.DescribeSyncReportOutliersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_sync_report_outliers_with_options_async(instance_id, request, headers, runtime)

    def describe_sync_report_outliers_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeSyncReportOutliersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeSyncReportOutliersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.level_type):
            query['LevelType'] = request.level_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportOutliers',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/outliers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeSyncReportOutliersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_report_outliers_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeSyncReportOutliersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeSyncReportOutliersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.level_type):
            query['LevelType'] = request.level_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportOutliers',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/outliers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeSyncReportOutliersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_metrics(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeUserMetricsRequest,
    ) -> airec_20181012_models.DescribeUserMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_metrics_with_options(instance_id, request, headers, runtime)

    async def describe_user_metrics_async(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeUserMetricsRequest,
    ) -> airec_20181012_models.DescribeUserMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_metrics_with_options_async(instance_id, request, headers, runtime)

    def describe_user_metrics_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeUserMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeUserMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserMetrics',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeUserMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_metrics_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.DescribeUserMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DescribeUserMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserMetrics',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DescribeUserMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_instance(
        self,
        instance_id: str,
    ) -> airec_20181012_models.DowngradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.downgrade_instance_with_options(instance_id, headers, runtime)

    async def downgrade_instance_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.DowngradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.downgrade_instance_with_options_async(instance_id, headers, runtime)

    def downgrade_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DowngradeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DowngradeInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/downgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DowngradeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.DowngradeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DowngradeInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/downgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.DowngradeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardRequest,
    ) -> airec_20181012_models.ListDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardRequest,
    ) -> airec_20181012_models.ListDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboard',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboard',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_details(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardDetailsRequest,
    ) -> airec_20181012_models.ListDashboardDetailsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_details_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_details_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardDetailsRequest,
    ) -> airec_20181012_models.ListDashboardDetailsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_details_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_details_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.trace_ids):
            query['TraceIds'] = request.trace_ids
        if not UtilClient.is_unset(request.scene_ids):
            query['SceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetails',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/details',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_details_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.trace_ids):
            query['TraceIds'] = request.trace_ids
        if not UtilClient.is_unset(request.scene_ids):
            query['SceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetails',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/details',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_details_flows(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardDetailsFlowsRequest,
    ) -> airec_20181012_models.ListDashboardDetailsFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_details_flows_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_details_flows_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardDetailsFlowsRequest,
    ) -> airec_20181012_models.ListDashboardDetailsFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_details_flows_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_details_flows_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardDetailsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardDetailsFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.trace_ids):
            query['TraceIds'] = request.trace_ids
        if not UtilClient.is_unset(request.scene_ids):
            query['SceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetailsFlows',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/details/flows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardDetailsFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_details_flows_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardDetailsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardDetailsFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.trace_ids):
            query['TraceIds'] = request.trace_ids
        if not UtilClient.is_unset(request.scene_ids):
            query['SceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetailsFlows',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/details/flows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardDetailsFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_metrics(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardMetricsRequest,
    ) -> airec_20181012_models.ListDashboardMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_metrics_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_metrics_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardMetricsRequest,
    ) -> airec_20181012_models.ListDashboardMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_metrics_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_metrics_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetrics',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_metrics_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetrics',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_metrics_flows(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardMetricsFlowsRequest,
    ) -> airec_20181012_models.ListDashboardMetricsFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_metrics_flows_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_metrics_flows_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardMetricsFlowsRequest,
    ) -> airec_20181012_models.ListDashboardMetricsFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_metrics_flows_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_metrics_flows_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardMetricsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardMetricsFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetricsFlows',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/metrics/flows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardMetricsFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_metrics_flows_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListDashboardMetricsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardMetricsFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetricsFlows',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/metrics/flows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardMetricsFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_parameters(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDashboardParametersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_parameters_with_options(instance_id, headers, runtime)

    async def list_dashboard_parameters_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDashboardParametersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_parameters_with_options_async(instance_id, headers, runtime)

    def list_dashboard_parameters_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardParametersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDashboardParameters',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/parameters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_parameters_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardParametersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDashboardParameters',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/parameters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_uid(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDashboardUidResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_uid_with_options(instance_id, headers, runtime)

    async def list_dashboard_uid_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDashboardUidResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_uid_with_options_async(instance_id, headers, runtime)

    def list_dashboard_uid_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardUidResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDashboardUid',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/uid',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_uid_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDashboardUidResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDashboardUid',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dashboard/uid',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDashboardUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_set_with_options(instance_id, headers, runtime)

    async def list_data_set_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_set_with_options_async(instance_id, headers, runtime)

    def list_data_set_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_with_options(instance_id, headers, runtime)

    async def list_data_source_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_source_with_options_async(instance_id, headers, runtime)

    def list_data_source_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diversify(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diversify_with_options(instance_id, headers, runtime)

    async def list_diversify_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_diversify_with_options_async(instance_id, headers, runtime)

    def list_diversify_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDiversifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diversify_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListDiversifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: airec_20181012_models.ListInstanceRequest,
    ) -> airec_20181012_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    async def list_instance_async(
        self,
        request: airec_20181012_models.ListInstanceRequest,
    ) -> airec_20181012_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_with_options_async(request, headers, runtime)

    def list_instance_with_options(
        self,
        request: airec_20181012_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: airec_20181012_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_task(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListInstanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_task_with_options(instance_id, headers, runtime)

    async def list_instance_task_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListInstanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_task_with_options_async(instance_id, headers, runtime)

    def list_instance_task_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListInstanceTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListInstanceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_task_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListInstanceTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceTask',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListInstanceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_items(
        self,
        instance_id: str,
        request: airec_20181012_models.ListItemsRequest,
    ) -> airec_20181012_models.ListItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_items_with_options(instance_id, request, headers, runtime)

    async def list_items_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListItemsRequest,
    ) -> airec_20181012_models.ListItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_items_with_options_async(instance_id, request, headers, runtime)

    def list_items_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListItems',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/items/actions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_items_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListItems',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/items/actions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logs(
        self,
        instance_id: str,
        request: airec_20181012_models.ListLogsRequest,
    ) -> airec_20181012_models.ListLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logs_with_options(instance_id, request, headers, runtime)

    async def list_logs_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListLogsRequest,
    ) -> airec_20181012_models.ListLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logs_with_options_async(instance_id, request, headers, runtime)

    def list_logs_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_params):
            query['QueryParams'] = request.query_params
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logs_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_params):
            query['QueryParams'] = request.query_params
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mix(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mix_with_options(instance_id, headers, runtime)

    async def list_mix_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mix_with_options_async(instance_id, headers, runtime)

    def list_mix_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListMixResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mix_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListMixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rule_conditions(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListRuleConditionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rule_conditions_with_options(instance_id, headers, runtime)

    async def list_rule_conditions_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ListRuleConditionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rule_conditions_with_options_async(instance_id, headers, runtime)

    def list_rule_conditions_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListRuleConditionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRuleConditions',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rule-conditions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListRuleConditionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rule_conditions_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListRuleConditionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRuleConditions',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rule-conditions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListRuleConditionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        instance_id: str,
        request: airec_20181012_models.ListRulesRequest,
    ) -> airec_20181012_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rules_with_options(instance_id, request, headers, runtime)

    async def list_rules_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListRulesRequest,
    ) -> airec_20181012_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rules_with_options_async(instance_id, request, headers, runtime)

    def list_rules_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rule_tasks(
        self,
        instance_id: str,
        request: airec_20181012_models.ListRuleTasksRequest,
    ) -> airec_20181012_models.ListRuleTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rule_tasks_with_options(instance_id, request, headers, runtime)

    async def list_rule_tasks_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListRuleTasksRequest,
    ) -> airec_20181012_models.ListRuleTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rule_tasks_with_options_async(instance_id, request, headers, runtime)

    def list_rule_tasks_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListRuleTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListRuleTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuleTasks',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rule-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListRuleTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rule_tasks_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListRuleTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListRuleTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuleTasks',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rule-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListRuleTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scene_items(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20181012_models.ListSceneItemsRequest,
    ) -> airec_20181012_models.ListSceneItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scene_items_with_options(instance_id, scene_id, request, headers, runtime)

    async def list_scene_items_async(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20181012_models.ListSceneItemsRequest,
    ) -> airec_20181012_models.ListSceneItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scene_items_with_options_async(instance_id, scene_id, request, headers, runtime)

    def list_scene_items_with_options(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20181012_models.ListSceneItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListSceneItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_rule_id):
            query['OperationRuleId'] = request.operation_rule_id
        if not UtilClient.is_unset(request.selection_rule_id):
            query['SelectionRuleId'] = request.selection_rule_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.preview_type):
            query['PreviewType'] = request.preview_type
        if not UtilClient.is_unset(request.query_count):
            query['QueryCount'] = request.query_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSceneItems',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListSceneItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scene_items_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20181012_models.ListSceneItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListSceneItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_rule_id):
            query['OperationRuleId'] = request.operation_rule_id
        if not UtilClient.is_unset(request.selection_rule_id):
            query['SelectionRuleId'] = request.selection_rule_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.preview_type):
            query['PreviewType'] = request.preview_type
        if not UtilClient.is_unset(request.query_count):
            query['QueryCount'] = request.query_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSceneItems',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListSceneItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scenes(
        self,
        instance_id: str,
        request: airec_20181012_models.ListScenesRequest,
    ) -> airec_20181012_models.ListScenesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scenes_with_options(instance_id, request, headers, runtime)

    async def list_scenes_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListScenesRequest,
    ) -> airec_20181012_models.ListScenesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scenes_with_options_async(instance_id, request, headers, runtime)

    def list_scenes_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListScenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scenes_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListScenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_umeng_appkeys(self) -> airec_20181012_models.ListUmengAppkeysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_umeng_appkeys_with_options(headers, runtime)

    async def list_umeng_appkeys_async(self) -> airec_20181012_models.ListUmengAppkeysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_umeng_appkeys_with_options_async(headers, runtime)

    def list_umeng_appkeys_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListUmengAppkeysResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUmengAppkeys',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/umeng/appkeys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListUmengAppkeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_umeng_appkeys_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListUmengAppkeysResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUmengAppkeys',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/umeng/appkeys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ListUmengAppkeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_source(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20181012_models.ModifyDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_data_source_with_options(instance_id, table_name, headers, runtime)

    async def modify_data_source_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20181012_models.ModifyDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_data_source_with_options_async(instance_id, table_name, headers, runtime)

    def modify_data_source_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSources/{{TableName}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_source_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSources/{{TableName}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_diversify(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.ModifyDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_diversify_with_options(instance_id, name, headers, runtime)

    async def modify_diversify_async(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.ModifyDiversifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_diversify_with_options_async(instance_id, name, headers, runtime)

    def modify_diversify_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies/{{Name}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyDiversifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_diversify_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyDiversifyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyDiversify',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/diversifies/{{Name}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyDiversifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_exposure_settings(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ModifyExposureSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_exposure_settings_with_options(instance_id, headers, runtime)

    async def modify_exposure_settings_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ModifyExposureSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_exposure_settings_with_options_async(instance_id, headers, runtime)

    def modify_exposure_settings_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyExposureSettingsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyExposureSettings',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/exposure-settings',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyExposureSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_exposure_settings_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyExposureSettingsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyExposureSettings',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/exposure-settings',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyExposureSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_instance_with_options(instance_id, headers, runtime)

    async def modify_instance_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_instance_with_options_async(instance_id, headers, runtime)

    def modify_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_items(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ModifyItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_items_with_options(instance_id, headers, runtime)

    async def modify_items_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ModifyItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_items_with_options_async(instance_id, headers, runtime)

    def modify_items_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyItemsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyItems',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/items',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_items_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyItemsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyItems',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/items',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mix(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.ModifyMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_mix_with_options(instance_id, name, headers, runtime)

    async def modify_mix_async(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20181012_models.ModifyMixResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_mix_with_options_async(instance_id, name, headers, runtime)

    def modify_mix_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes/{{Name}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyMixResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mix_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyMixResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyMix',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/mixes/{{Name}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyMixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rule(
        self,
        instance_id: str,
        rule_id: str,
    ) -> airec_20181012_models.ModifyRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_rule_with_options(instance_id, rule_id, headers, runtime)

    async def modify_rule_async(
        self,
        instance_id: str,
        rule_id: str,
    ) -> airec_20181012_models.ModifyRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_rule_with_options_async(instance_id, rule_id, headers, runtime)

    def modify_rule_with_options(
        self,
        instance_id: str,
        rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules/{{RuleId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_with_options_async(
        self,
        instance_id: str,
        rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifyRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules/{{RuleId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20181012_models.ModifySceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scene_with_options(instance_id, scene_id, headers, runtime)

    async def modify_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20181012_models.ModifySceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def modify_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifySceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyScene',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifySceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scene_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ModifySceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyScene',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/scenes/{{SceneId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ModifySceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_rule(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20181012_models.PublishRuleRequest,
    ) -> airec_20181012_models.PublishRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_rule_with_options(instance_id, rule_id, request, headers, runtime)

    async def publish_rule_async(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20181012_models.PublishRuleRequest,
    ) -> airec_20181012_models.PublishRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_rule_with_options_async(instance_id, rule_id, request, headers, runtime)

    def publish_rule_with_options(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20181012_models.PublishRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.PublishRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishRule',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules/{{RuleId}}/actions/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.PublishRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_rule_with_options_async(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20181012_models.PublishRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.PublishRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishRule',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/rules/{{RuleId}}/actions/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.PublishRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_document(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20181012_models.PushDocumentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_document_with_options(instance_id, table_name, headers, runtime)

    async def push_document_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20181012_models.PushDocumentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_document_with_options_async(instance_id, table_name, headers, runtime)

    def push_document_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.PushDocumentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushDocument',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tables/{{TableName}}/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.PushDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_document_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.PushDocumentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushDocument',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tables/{{TableName}}/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.PushDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_intervention(
        self,
        instance_id: str,
    ) -> airec_20181012_models.PushInterventionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_intervention_with_options(instance_id, headers, runtime)

    async def push_intervention_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.PushInterventionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_intervention_with_options_async(instance_id, headers, runtime)

    def push_intervention_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.PushInterventionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushIntervention',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/intervene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.PushInterventionResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_intervention_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.PushInterventionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushIntervention',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/intervene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.PushInterventionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_message(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryDataMessageRequest,
    ) -> airec_20181012_models.QueryDataMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_data_message_with_options(instance_id, table, request, headers, runtime)

    async def query_data_message_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryDataMessageRequest,
    ) -> airec_20181012_models.QueryDataMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_data_message_with_options_async(instance_id, table, request, headers, runtime)

    def query_data_message_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryDataMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QueryDataMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.cmd_type):
            query['CmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['ItemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.bhv_type):
            query['BhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.message_source):
            query['MessageSource'] = request.message_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tables/{{Table}}/data-message',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QueryDataMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_message_with_options_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryDataMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QueryDataMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.cmd_type):
            query['CmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['ItemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.bhv_type):
            query['BhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.message_source):
            query['MessageSource'] = request.message_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessage',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tables/{{Table}}/data-message',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QueryDataMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_message_statistics(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryDataMessageStatisticsRequest,
    ) -> airec_20181012_models.QueryDataMessageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_data_message_statistics_with_options(instance_id, table, request, headers, runtime)

    async def query_data_message_statistics_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryDataMessageStatisticsRequest,
    ) -> airec_20181012_models.QueryDataMessageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_data_message_statistics_with_options_async(instance_id, table, request, headers, runtime)

    def query_data_message_statistics_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryDataMessageStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QueryDataMessageStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.cmd_type):
            query['CmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['ItemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.bhv_type):
            query['BhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.message_source):
            query['MessageSource'] = request.message_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessageStatistics',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tables/{{Table}}/data-message-statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QueryDataMessageStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_message_statistics_with_options_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryDataMessageStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QueryDataMessageStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.cmd_type):
            query['CmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['ItemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.bhv_type):
            query['BhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.message_source):
            query['MessageSource'] = request.message_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessageStatistics',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tables/{{Table}}/data-message-statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QueryDataMessageStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_exception_history(
        self,
        instance_id: str,
        request: airec_20181012_models.QueryExceptionHistoryRequest,
    ) -> airec_20181012_models.QueryExceptionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_exception_history_with_options(instance_id, request, headers, runtime)

    async def query_exception_history_async(
        self,
        instance_id: str,
        request: airec_20181012_models.QueryExceptionHistoryRequest,
    ) -> airec_20181012_models.QueryExceptionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_exception_history_with_options_async(instance_id, request, headers, runtime)

    def query_exception_history_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.QueryExceptionHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QueryExceptionHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExceptionHistory',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/exception-history',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QueryExceptionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_exception_history_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.QueryExceptionHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QueryExceptionHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExceptionHistory',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/exception-history',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QueryExceptionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_raw_data(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryRawDataRequest,
    ) -> airec_20181012_models.QueryRawDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_raw_data_with_options(instance_id, table, request, headers, runtime)

    async def query_raw_data_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryRawDataRequest,
    ) -> airec_20181012_models.QueryRawDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_raw_data_with_options_async(instance_id, table, request, headers, runtime)

    def query_raw_data_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryRawDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QueryRawDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['ItemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRawData',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tables/{{Table}}/raw-data',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QueryRawDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_raw_data_with_options_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20181012_models.QueryRawDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QueryRawDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['ItemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRawData',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/tables/{{Table}}/raw-data',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QueryRawDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_single_aggregation_report(
        self,
        instance_id: str,
    ) -> airec_20181012_models.QuerySingleAggregationReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_single_aggregation_report_with_options(instance_id, headers, runtime)

    async def query_single_aggregation_report_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.QuerySingleAggregationReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_single_aggregation_report_with_options_async(instance_id, headers, runtime)

    def query_single_aggregation_report_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QuerySingleAggregationReportResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QuerySingleAggregationReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/single-aggregation-report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QuerySingleAggregationReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_single_aggregation_report_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QuerySingleAggregationReportResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QuerySingleAggregationReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/single-aggregation-report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QuerySingleAggregationReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_single_report(
        self,
        instance_id: str,
        request: airec_20181012_models.QuerySingleReportRequest,
    ) -> airec_20181012_models.QuerySingleReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_single_report_with_options(instance_id, request, headers, runtime)

    async def query_single_report_async(
        self,
        instance_id: str,
        request: airec_20181012_models.QuerySingleReportRequest,
    ) -> airec_20181012_models.QuerySingleReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_single_report_with_options_async(instance_id, request, headers, runtime)

    def query_single_report_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.QuerySingleReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QuerySingleReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySingleReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/single-report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QuerySingleReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_single_report_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.QuerySingleReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QuerySingleReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySingleReport',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/single-report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QuerySingleReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sync_report_aggregation(
        self,
        instance_id: str,
        request: airec_20181012_models.QuerySyncReportAggregationRequest,
    ) -> airec_20181012_models.QuerySyncReportAggregationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_sync_report_aggregation_with_options(instance_id, request, headers, runtime)

    async def query_sync_report_aggregation_async(
        self,
        instance_id: str,
        request: airec_20181012_models.QuerySyncReportAggregationRequest,
    ) -> airec_20181012_models.QuerySyncReportAggregationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_sync_report_aggregation_with_options_async(instance_id, request, headers, runtime)

    def query_sync_report_aggregation_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.QuerySyncReportAggregationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QuerySyncReportAggregationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySyncReportAggregation',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/aggregation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QuerySyncReportAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sync_report_aggregation_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.QuerySyncReportAggregationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.QuerySyncReportAggregationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySyncReportAggregation',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/sync-reports/aggregation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.QuerySyncReportAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recommend(
        self,
        instance_id: str,
        request: airec_20181012_models.RecommendRequest,
    ) -> airec_20181012_models.RecommendResponse:
        runtime = util_models.RuntimeOptions()
        headers = airec_20181012_models.RecommendHeaders()
        return self.recommend_with_options(instance_id, request, headers, runtime)

    async def recommend_async(
        self,
        instance_id: str,
        request: airec_20181012_models.RecommendRequest,
    ) -> airec_20181012_models.RecommendResponse:
        runtime = util_models.RuntimeOptions()
        headers = airec_20181012_models.RecommendHeaders()
        return await self.recommend_with_options_async(instance_id, request, headers, runtime)

    def recommend_with_options(
        self,
        instance_id: str,
        request: airec_20181012_models.RecommendRequest,
        headers: airec_20181012_models.RecommendHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.RecommendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.imei):
            query['Imei'] = request.imei
        if not UtilClient.is_unset(request.return_count):
            query['ReturnCount'] = request.return_count
        if not UtilClient.is_unset(request.items):
            query['Items'] = request.items
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.region_id):
            real_headers['RegionId'] = headers.region_id
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Recommend',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/recommend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.RecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def recommend_with_options_async(
        self,
        instance_id: str,
        request: airec_20181012_models.RecommendRequest,
        headers: airec_20181012_models.RecommendHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.RecommendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.imei):
            query['Imei'] = request.imei
        if not UtilClient.is_unset(request.return_count):
            query['ReturnCount'] = request.return_count
        if not UtilClient.is_unset(request.items):
            query['Items'] = request.items
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.region_id):
            real_headers['RegionId'] = headers.region_id
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Recommend',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/recommend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.RecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_instance(
        self,
        instance_id: str,
    ) -> airec_20181012_models.RunInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_instance_with_options(instance_id, headers, runtime)

    async def run_instance_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.RunInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_instance_with_options_async(instance_id, headers, runtime)

    def run_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.RunInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RunInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.RunInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.RunInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RunInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.RunInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_data_set(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.StopDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_data_set_with_options(instance_id, version_id, headers, runtime)

    async def stop_data_set_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20181012_models.StopDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_data_set_with_options_async(instance_id, version_id, headers, runtime)

    def stop_data_set_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.StopDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopDataSet',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/actions/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.StopDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_data_set_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.StopDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopDataSet',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/actions/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.StopDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_instance(
        self,
        instance_id: str,
    ) -> airec_20181012_models.UpgradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_instance_with_options(instance_id, headers, runtime)

    async def upgrade_instance_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.UpgradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_instance_with_options_async(instance_id, headers, runtime)

    def upgrade_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.UpgradeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.UpgradeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.UpgradeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.UpgradeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_instance(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ValidateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_instance_with_options(instance_id, headers, runtime)

    async def validate_instance_async(
        self,
        instance_id: str,
    ) -> airec_20181012_models.ValidateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_instance_with_options_async(instance_id, headers, runtime)

    def validate_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ValidateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ValidateInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/validate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ValidateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ValidateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ValidateInstance',
            version='2018-10-12',
            protocol='HTTPS',
            pathname=f'/openapi/instances/{instance_id}/actions/validate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20181012_models.ValidateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )
