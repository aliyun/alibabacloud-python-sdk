# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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
        return airec_20181012_models.AttachDatasetResponse().from_map(
            self.do_roarequest('AttachDataset', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/actions/current', 'json', req, runtime)
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
        return airec_20181012_models.AttachDatasetResponse().from_map(
            await self.do_roarequest_async('AttachDataset', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/actions/current', 'json', req, runtime)
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
        return airec_20181012_models.CreateDiversifyResponse().from_map(
            self.do_roarequest('CreateDiversify', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/diversifies', 'json', req, runtime)
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
        return airec_20181012_models.CreateDiversifyResponse().from_map(
            await self.do_roarequest_async('CreateDiversify', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/diversifies', 'json', req, runtime)
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
        return airec_20181012_models.CreateInstanceResponse().from_map(
            self.do_roarequest('CreateInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.CreateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return airec_20181012_models.CreateInstanceResponse().from_map(
            await self.do_roarequest_async('CreateInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances', 'json', req, runtime)
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
        return airec_20181012_models.CreateMixResponse().from_map(
            self.do_roarequest('CreateMix', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/mixes', 'json', req, runtime)
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
        return airec_20181012_models.CreateMixResponse().from_map(
            await self.do_roarequest_async('CreateMix', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/mixes', 'json', req, runtime)
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
        return airec_20181012_models.CreateRuleResponse().from_map(
            self.do_roarequest('CreateRule', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/rules', 'json', req, runtime)
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
        return airec_20181012_models.CreateRuleResponse().from_map(
            await self.do_roarequest_async('CreateRule', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/rules', 'json', req, runtime)
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
        return airec_20181012_models.CreateSceneResponse().from_map(
            self.do_roarequest('CreateScene', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/scenes', 'json', req, runtime)
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
        return airec_20181012_models.CreateSceneResponse().from_map(
            await self.do_roarequest_async('CreateScene', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/scenes', 'json', req, runtime)
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
        return airec_20181012_models.DeleteDataSetResponse().from_map(
            self.do_roarequest('DeleteDataSet', '2018-10-12', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}', 'json', req, runtime)
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
        return airec_20181012_models.DeleteDataSetResponse().from_map(
            await self.do_roarequest_async('DeleteDataSet', '2018-10-12', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}', 'json', req, runtime)
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
        return airec_20181012_models.DeleteDiversifyResponse().from_map(
            self.do_roarequest('DeleteDiversify', '2018-10-12', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/diversifies/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.DeleteDiversifyResponse().from_map(
            await self.do_roarequest_async('DeleteDiversify', '2018-10-12', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/diversifies/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.DeleteMixResponse().from_map(
            self.do_roarequest('DeleteMix', '2018-10-12', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/mixes/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.DeleteMixResponse().from_map(
            await self.do_roarequest_async('DeleteMix', '2018-10-12', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/mixes/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.DeleteSceneResponse().from_map(
            self.do_roarequest('DeleteScene', '2018-10-12', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}', 'json', req, runtime)
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
        return airec_20181012_models.DeleteSceneResponse().from_map(
            await self.do_roarequest_async('DeleteScene', '2018-10-12', 'HTTPS', 'DELETE', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeDataSetMessageResponse().from_map(
            self.do_roarequest('DescribeDataSetMessage', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/messages', 'json', req, runtime)
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
        return airec_20181012_models.DescribeDataSetMessageResponse().from_map(
            await self.do_roarequest_async('DescribeDataSetMessage', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/messages', 'json', req, runtime)
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
        return airec_20181012_models.DescribeDataSetReportResponse().from_map(
            self.do_roarequest('DescribeDataSetReport', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/report', 'json', req, runtime)
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
        return airec_20181012_models.DescribeDataSetReportResponse().from_map(
            await self.do_roarequest_async('DescribeDataSetReport', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/report', 'json', req, runtime)
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
        return airec_20181012_models.DescribeDiversifyResponse().from_map(
            self.do_roarequest('DescribeDiversify', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/diversifies/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeDiversifyResponse().from_map(
            await self.do_roarequest_async('DescribeDiversify', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/diversifies/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeExposureSettingsResponse().from_map(
            self.do_roarequest('DescribeExposureSettings', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/exposure-settings', 'json', req, runtime)
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
        return airec_20181012_models.DescribeExposureSettingsResponse().from_map(
            await self.do_roarequest_async('DescribeExposureSettings', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/exposure-settings', 'json', req, runtime)
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
        return airec_20181012_models.DescribeInstanceResponse().from_map(
            self.do_roarequest('DescribeInstance', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeInstanceResponse().from_map(
            await self.do_roarequest_async('DescribeInstance', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeMixResponse().from_map(
            self.do_roarequest('DescribeMix', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/mixes/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeMixResponse().from_map(
            await self.do_roarequest_async('DescribeMix', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/mixes/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeQuotaResponse().from_map(
            self.do_roarequest('DescribeQuota', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/quota', 'json', req, runtime)
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
        return airec_20181012_models.DescribeQuotaResponse().from_map(
            await self.do_roarequest_async('DescribeQuota', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/quota', 'json', req, runtime)
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
        return airec_20181012_models.DescribeRegionsResponse().from_map(
            self.do_roarequest('DescribeRegions', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/configurations/regions', 'json', req, runtime)
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
        return airec_20181012_models.DescribeRegionsResponse().from_map(
            await self.do_roarequest_async('DescribeRegions', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/configurations/regions', 'json', req, runtime)
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
        return airec_20181012_models.DescribeRuleResponse().from_map(
            self.do_roarequest('DescribeRule', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/rules/{{RuleId}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeRuleResponse().from_map(
            await self.do_roarequest_async('DescribeRule', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/rules/{{RuleId}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeSceneResponse().from_map(
            self.do_roarequest('DescribeScene', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeSceneResponse().from_map(
            await self.do_roarequest_async('DescribeScene', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}', 'json', req, runtime)
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
        return airec_20181012_models.DescribeSceneThroughputResponse().from_map(
            self.do_roarequest('DescribeSceneThroughput', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}/throughput', 'json', req, runtime)
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
        return airec_20181012_models.DescribeSceneThroughputResponse().from_map(
            await self.do_roarequest_async('DescribeSceneThroughput', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}/throughput', 'json', req, runtime)
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
        return airec_20181012_models.DescribeSyncReportDetailResponse().from_map(
            self.do_roarequest('DescribeSyncReportDetail', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/detail', 'json', req, runtime)
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
        return airec_20181012_models.DescribeSyncReportDetailResponse().from_map(
            await self.do_roarequest_async('DescribeSyncReportDetail', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/detail', 'json', req, runtime)
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
        return airec_20181012_models.DescribeSyncReportOutliersResponse().from_map(
            self.do_roarequest('DescribeSyncReportOutliers', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/outliers', 'json', req, runtime)
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
        return airec_20181012_models.DescribeSyncReportOutliersResponse().from_map(
            await self.do_roarequest_async('DescribeSyncReportOutliers', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/outliers', 'json', req, runtime)
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
        return airec_20181012_models.DescribeUserMetricsResponse().from_map(
            self.do_roarequest('DescribeUserMetrics', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/metrics', 'json', req, runtime)
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
        return airec_20181012_models.DescribeUserMetricsResponse().from_map(
            await self.do_roarequest_async('DescribeUserMetrics', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/metrics', 'json', req, runtime)
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
        return airec_20181012_models.DowngradeInstanceResponse().from_map(
            self.do_roarequest('DowngradeInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/downgrade', 'json', req, runtime)
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
        return airec_20181012_models.DowngradeInstanceResponse().from_map(
            await self.do_roarequest_async('DowngradeInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/downgrade', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardResponse().from_map(
            self.do_roarequest('ListDashboard', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/statistics', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardResponse().from_map(
            await self.do_roarequest_async('ListDashboard', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/statistics', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardDetailsResponse().from_map(
            self.do_roarequest('ListDashboardDetails', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/details', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardDetailsResponse().from_map(
            await self.do_roarequest_async('ListDashboardDetails', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/details', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardDetailsFlowsResponse().from_map(
            self.do_roarequest('ListDashboardDetailsFlows', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/details/flows', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardDetailsFlowsResponse().from_map(
            await self.do_roarequest_async('ListDashboardDetailsFlows', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/details/flows', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardMetricsResponse().from_map(
            self.do_roarequest('ListDashboardMetrics', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/metrics', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardMetricsResponse().from_map(
            await self.do_roarequest_async('ListDashboardMetrics', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/metrics', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardMetricsFlowsResponse().from_map(
            self.do_roarequest('ListDashboardMetricsFlows', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/metrics/flows', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardMetricsFlowsResponse().from_map(
            await self.do_roarequest_async('ListDashboardMetricsFlows', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/metrics/flows', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardParametersResponse().from_map(
            self.do_roarequest('ListDashboardParameters', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/parameters', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardParametersResponse().from_map(
            await self.do_roarequest_async('ListDashboardParameters', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/parameters', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardUidResponse().from_map(
            self.do_roarequest('ListDashboardUid', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/uid', 'json', req, runtime)
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
        return airec_20181012_models.ListDashboardUidResponse().from_map(
            await self.do_roarequest_async('ListDashboardUid', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dashboard/uid', 'json', req, runtime)
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
        return airec_20181012_models.ListDataSetResponse().from_map(
            self.do_roarequest('ListDataSet', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dataSets', 'json', req, runtime)
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
        return airec_20181012_models.ListDataSetResponse().from_map(
            await self.do_roarequest_async('ListDataSet', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dataSets', 'json', req, runtime)
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
        return airec_20181012_models.ListDataSourceResponse().from_map(
            self.do_roarequest('ListDataSource', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dataSources', 'json', req, runtime)
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
        return airec_20181012_models.ListDataSourceResponse().from_map(
            await self.do_roarequest_async('ListDataSource', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/dataSources', 'json', req, runtime)
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
        return airec_20181012_models.ListDiversifyResponse().from_map(
            self.do_roarequest('ListDiversify', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/diversifies', 'json', req, runtime)
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
        return airec_20181012_models.ListDiversifyResponse().from_map(
            await self.do_roarequest_async('ListDiversify', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/diversifies', 'json', req, runtime)
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
        return airec_20181012_models.ListInstanceResponse().from_map(
            self.do_roarequest('ListInstance', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances', 'json', req, runtime)
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
        return airec_20181012_models.ListInstanceResponse().from_map(
            await self.do_roarequest_async('ListInstance', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances', 'json', req, runtime)
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
        return airec_20181012_models.ListInstanceTaskResponse().from_map(
            self.do_roarequest('ListInstanceTask', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/tasks', 'json', req, runtime)
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
        return airec_20181012_models.ListInstanceTaskResponse().from_map(
            await self.do_roarequest_async('ListInstanceTask', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/tasks', 'json', req, runtime)
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
        return airec_20181012_models.ListItemsResponse().from_map(
            self.do_roarequest('ListItems', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/items/actions/list', 'json', req, runtime)
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
        return airec_20181012_models.ListItemsResponse().from_map(
            await self.do_roarequest_async('ListItems', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/items/actions/list', 'json', req, runtime)
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
        return airec_20181012_models.ListLogsResponse().from_map(
            self.do_roarequest('ListLogs', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/logs', 'json', req, runtime)
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
        return airec_20181012_models.ListLogsResponse().from_map(
            await self.do_roarequest_async('ListLogs', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/logs', 'json', req, runtime)
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
        return airec_20181012_models.ListMixResponse().from_map(
            self.do_roarequest('ListMix', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/mixes', 'json', req, runtime)
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
        return airec_20181012_models.ListMixResponse().from_map(
            await self.do_roarequest_async('ListMix', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/mixes', 'json', req, runtime)
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
        return airec_20181012_models.ListRuleConditionsResponse().from_map(
            self.do_roarequest('ListRuleConditions', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/rule-conditions', 'json', req, runtime)
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
        return airec_20181012_models.ListRuleConditionsResponse().from_map(
            await self.do_roarequest_async('ListRuleConditions', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/rule-conditions', 'json', req, runtime)
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
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return airec_20181012_models.ListRulesResponse().from_map(
            self.do_roarequest('ListRules', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/rules', 'json', req, runtime)
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
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return airec_20181012_models.ListRulesResponse().from_map(
            await self.do_roarequest_async('ListRules', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/rules', 'json', req, runtime)
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
        return airec_20181012_models.ListRuleTasksResponse().from_map(
            self.do_roarequest('ListRuleTasks', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/rule-tasks', 'json', req, runtime)
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
        return airec_20181012_models.ListRuleTasksResponse().from_map(
            await self.do_roarequest_async('ListRuleTasks', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/rule-tasks', 'json', req, runtime)
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
        return airec_20181012_models.ListSceneItemsResponse().from_map(
            self.do_roarequest('ListSceneItems', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}/items', 'json', req, runtime)
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
        return airec_20181012_models.ListSceneItemsResponse().from_map(
            await self.do_roarequest_async('ListSceneItems', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}/items', 'json', req, runtime)
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
        return airec_20181012_models.ListScenesResponse().from_map(
            self.do_roarequest('ListScenes', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/scenes', 'json', req, runtime)
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
        return airec_20181012_models.ListScenesResponse().from_map(
            await self.do_roarequest_async('ListScenes', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/scenes', 'json', req, runtime)
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
        return airec_20181012_models.ListUmengAppkeysResponse().from_map(
            self.do_roarequest('ListUmengAppkeys', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/umeng/appkeys', 'json', req, runtime)
        )

    async def list_umeng_appkeys_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20181012_models.ListUmengAppkeysResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return airec_20181012_models.ListUmengAppkeysResponse().from_map(
            await self.do_roarequest_async('ListUmengAppkeys', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/umeng/appkeys', 'json', req, runtime)
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
        return airec_20181012_models.ModifyDataSourceResponse().from_map(
            self.do_roarequest('ModifyDataSource', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/dataSources/{{TableName}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyDataSourceResponse().from_map(
            await self.do_roarequest_async('ModifyDataSource', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/dataSources/{{TableName}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyDiversifyResponse().from_map(
            self.do_roarequest('ModifyDiversify', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/diversifies/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyDiversifyResponse().from_map(
            await self.do_roarequest_async('ModifyDiversify', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/diversifies/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyExposureSettingsResponse().from_map(
            self.do_roarequest('ModifyExposureSettings', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/exposure-settings', 'json', req, runtime)
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
        return airec_20181012_models.ModifyExposureSettingsResponse().from_map(
            await self.do_roarequest_async('ModifyExposureSettings', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/exposure-settings', 'json', req, runtime)
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
        return airec_20181012_models.ModifyInstanceResponse().from_map(
            self.do_roarequest('ModifyInstance', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyInstanceResponse().from_map(
            await self.do_roarequest_async('ModifyInstance', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyItemsResponse().from_map(
            self.do_roarequest('ModifyItems', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/items', 'json', req, runtime)
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
        return airec_20181012_models.ModifyItemsResponse().from_map(
            await self.do_roarequest_async('ModifyItems', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/items', 'json', req, runtime)
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
        return airec_20181012_models.ModifyMixResponse().from_map(
            self.do_roarequest('ModifyMix', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/mixes/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyMixResponse().from_map(
            await self.do_roarequest_async('ModifyMix', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/mixes/{{Name}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyRuleResponse().from_map(
            self.do_roarequest('ModifyRule', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/rules/{{RuleId}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifyRuleResponse().from_map(
            await self.do_roarequest_async('ModifyRule', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/rules/{{RuleId}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifySceneResponse().from_map(
            self.do_roarequest('ModifyScene', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}', 'json', req, runtime)
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
        return airec_20181012_models.ModifySceneResponse().from_map(
            await self.do_roarequest_async('ModifyScene', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/scenes/{{SceneId}}', 'json', req, runtime)
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
        return airec_20181012_models.PublishRuleResponse().from_map(
            self.do_roarequest('PublishRule', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/rules/{{RuleId}}/actions/publish', 'json', req, runtime)
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
        return airec_20181012_models.PublishRuleResponse().from_map(
            await self.do_roarequest_async('PublishRule', '2018-10-12', 'HTTPS', 'PUT', 'AK', f'/openapi/instances/{instance_id}/rules/{{RuleId}}/actions/publish', 'json', req, runtime)
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
        return airec_20181012_models.PushDocumentResponse().from_map(
            self.do_roarequest('PushDocument', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/tables/{{TableName}}/actions/bulk', 'json', req, runtime)
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
        return airec_20181012_models.PushDocumentResponse().from_map(
            await self.do_roarequest_async('PushDocument', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/tables/{{TableName}}/actions/bulk', 'json', req, runtime)
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
        return airec_20181012_models.PushInterventionResponse().from_map(
            self.do_roarequest('PushIntervention', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/intervene', 'json', req, runtime)
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
        return airec_20181012_models.PushInterventionResponse().from_map(
            await self.do_roarequest_async('PushIntervention', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/intervene', 'json', req, runtime)
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
        return airec_20181012_models.QueryDataMessageResponse().from_map(
            self.do_roarequest('QueryDataMessage', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/tables/{{Table}}/data-message', 'json', req, runtime)
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
        return airec_20181012_models.QueryDataMessageResponse().from_map(
            await self.do_roarequest_async('QueryDataMessage', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/tables/{{Table}}/data-message', 'json', req, runtime)
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
        return airec_20181012_models.QueryDataMessageStatisticsResponse().from_map(
            self.do_roarequest('QueryDataMessageStatistics', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/tables/{{Table}}/data-message-statistics', 'json', req, runtime)
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
        return airec_20181012_models.QueryDataMessageStatisticsResponse().from_map(
            await self.do_roarequest_async('QueryDataMessageStatistics', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/tables/{{Table}}/data-message-statistics', 'json', req, runtime)
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
        return airec_20181012_models.QueryExceptionHistoryResponse().from_map(
            self.do_roarequest('QueryExceptionHistory', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/exception-history', 'json', req, runtime)
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
        return airec_20181012_models.QueryExceptionHistoryResponse().from_map(
            await self.do_roarequest_async('QueryExceptionHistory', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/exception-history', 'json', req, runtime)
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
        return airec_20181012_models.QueryRawDataResponse().from_map(
            self.do_roarequest('QueryRawData', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/tables/{{Table}}/raw-data', 'json', req, runtime)
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
        return airec_20181012_models.QueryRawDataResponse().from_map(
            await self.do_roarequest_async('QueryRawData', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/tables/{{Table}}/raw-data', 'json', req, runtime)
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
        return airec_20181012_models.QuerySingleAggregationReportResponse().from_map(
            self.do_roarequest('QuerySingleAggregationReport', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/single-aggregation-report', 'json', req, runtime)
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
        return airec_20181012_models.QuerySingleAggregationReportResponse().from_map(
            await self.do_roarequest_async('QuerySingleAggregationReport', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/single-aggregation-report', 'json', req, runtime)
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
        return airec_20181012_models.QuerySingleReportResponse().from_map(
            self.do_roarequest('QuerySingleReport', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/single-report', 'json', req, runtime)
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
        return airec_20181012_models.QuerySingleReportResponse().from_map(
            await self.do_roarequest_async('QuerySingleReport', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/single-report', 'json', req, runtime)
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
        return airec_20181012_models.QuerySyncReportAggregationResponse().from_map(
            self.do_roarequest('QuerySyncReportAggregation', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/aggregation', 'json', req, runtime)
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
        return airec_20181012_models.QuerySyncReportAggregationResponse().from_map(
            await self.do_roarequest_async('QuerySyncReportAggregation', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/sync-reports/aggregation', 'json', req, runtime)
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
        return airec_20181012_models.RecommendResponse().from_map(
            self.do_roarequest('Recommend', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/actions/recommend', 'json', req, runtime)
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
        return airec_20181012_models.RecommendResponse().from_map(
            await self.do_roarequest_async('Recommend', '2018-10-12', 'HTTPS', 'GET', 'AK', f'/openapi/instances/{instance_id}/actions/recommend', 'json', req, runtime)
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
        return airec_20181012_models.RunInstanceResponse().from_map(
            self.do_roarequest('RunInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/import', 'json', req, runtime)
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
        return airec_20181012_models.RunInstanceResponse().from_map(
            await self.do_roarequest_async('RunInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/import', 'json', req, runtime)
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
        return airec_20181012_models.StopDataSetResponse().from_map(
            self.do_roarequest('StopDataSet', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/actions/stop', 'json', req, runtime)
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
        return airec_20181012_models.StopDataSetResponse().from_map(
            await self.do_roarequest_async('StopDataSet', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/dataSets/{{VersionId}}/actions/stop', 'json', req, runtime)
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
        return airec_20181012_models.UpgradeInstanceResponse().from_map(
            self.do_roarequest('UpgradeInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/upgrade', 'json', req, runtime)
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
        return airec_20181012_models.UpgradeInstanceResponse().from_map(
            await self.do_roarequest_async('UpgradeInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/upgrade', 'json', req, runtime)
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
        return airec_20181012_models.ValidateInstanceResponse().from_map(
            self.do_roarequest('ValidateInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/validate', 'json', req, runtime)
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
        return airec_20181012_models.ValidateInstanceResponse().from_map(
            await self.do_roarequest_async('ValidateInstance', '2018-10-12', 'HTTPS', 'POST', 'AK', f'/openapi/instances/{instance_id}/actions/validate', 'json', req, runtime)
        )
