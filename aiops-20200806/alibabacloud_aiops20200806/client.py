# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiops20200806 import models as aiops_20200806_models
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
        self._endpoint = self.get_endpoint('aiops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_algorithm_with_options(
        self,
        request: aiops_20200806_models.AddAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_id):
            query['AlgorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.algorithm_type):
            query['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expand_information):
            query['ExpandInformation'] = request.expand_information
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_algorithm_with_options_async(
        self,
        request: aiops_20200806_models.AddAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_id):
            query['AlgorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.algorithm_type):
            query['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expand_information):
            query['ExpandInformation'] = request.expand_information
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_algorithm(
        self,
        request: aiops_20200806_models.AddAlgorithmRequest,
    ) -> aiops_20200806_models.AddAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_algorithm_with_options(request, runtime)

    async def add_algorithm_async(
        self,
        request: aiops_20200806_models.AddAlgorithmRequest,
    ) -> aiops_20200806_models.AddAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_algorithm_with_options_async(request, runtime)

    def add_business_group_with_options(
        self,
        tmp_req: aiops_20200806_models.AddBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddBusinessGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.AddBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.create_user):
            query['CreateUser'] = request.create_user
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_business_group_with_options_async(
        self,
        tmp_req: aiops_20200806_models.AddBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddBusinessGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.AddBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.create_user):
            query['CreateUser'] = request.create_user
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddBusinessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_business_group(
        self,
        request: aiops_20200806_models.AddBusinessGroupRequest,
    ) -> aiops_20200806_models.AddBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_business_group_with_options(request, runtime)

    async def add_business_group_async(
        self,
        request: aiops_20200806_models.AddBusinessGroupRequest,
    ) -> aiops_20200806_models.AddBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_business_group_with_options_async(request, runtime)

    def add_business_group_one_with_options(
        self,
        request: aiops_20200806_models.AddBusinessGroupOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddBusinessGroupOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.business_group_desc):
            body['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_name):
            body['BusinessGroupName'] = request.business_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddBusinessGroupOne',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddBusinessGroupOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_business_group_one_with_options_async(
        self,
        request: aiops_20200806_models.AddBusinessGroupOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddBusinessGroupOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.business_group_desc):
            body['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_name):
            body['BusinessGroupName'] = request.business_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddBusinessGroupOne',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddBusinessGroupOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_business_group_one(
        self,
        request: aiops_20200806_models.AddBusinessGroupOneRequest,
    ) -> aiops_20200806_models.AddBusinessGroupOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_business_group_one_with_options(request, runtime)

    async def add_business_group_one_async(
        self,
        request: aiops_20200806_models.AddBusinessGroupOneRequest,
    ) -> aiops_20200806_models.AddBusinessGroupOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_business_group_one_with_options_async(request, runtime)

    def add_scenario_with_options(
        self,
        request: aiops_20200806_models.AddScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            query['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_scenario_with_options_async(
        self,
        request: aiops_20200806_models.AddScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            query['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_scenario(
        self,
        request: aiops_20200806_models.AddScenarioRequest,
    ) -> aiops_20200806_models.AddScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_scenario_with_options(request, runtime)

    async def add_scenario_async(
        self,
        request: aiops_20200806_models.AddScenarioRequest,
    ) -> aiops_20200806_models.AddScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_scenario_with_options_async(request, runtime)

    def add_scene_list_with_options(
        self,
        request: aiops_20200806_models.AddSceneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddSceneListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_scene_list_with_options_async(
        self,
        request: aiops_20200806_models.AddSceneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddSceneListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_scene_list(
        self,
        request: aiops_20200806_models.AddSceneListRequest,
    ) -> aiops_20200806_models.AddSceneListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_scene_list_with_options(request, runtime)

    async def add_scene_list_async(
        self,
        request: aiops_20200806_models.AddSceneListRequest,
    ) -> aiops_20200806_models.AddSceneListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_scene_list_with_options_async(request, runtime)

    def add_script_with_options(
        self,
        request: aiops_20200806_models.AddScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handle_suggest_desc):
            query['HandleSuggestDesc'] = request.handle_suggest_desc
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.root_cause_desc):
            query['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_causes_log):
            query['RootCausesLog'] = request.root_causes_log
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        if not UtilClient.is_unset(request.script_desc):
            query['ScriptDesc'] = request.script_desc
        if not UtilClient.is_unset(request.script_language):
            query['ScriptLanguage'] = request.script_language
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_version):
            query['ScriptVersion'] = request.script_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_script_with_options_async(
        self,
        request: aiops_20200806_models.AddScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handle_suggest_desc):
            query['HandleSuggestDesc'] = request.handle_suggest_desc
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.root_cause_desc):
            query['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_causes_log):
            query['RootCausesLog'] = request.root_causes_log
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        if not UtilClient.is_unset(request.script_desc):
            query['ScriptDesc'] = request.script_desc
        if not UtilClient.is_unset(request.script_language):
            query['ScriptLanguage'] = request.script_language
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_version):
            query['ScriptVersion'] = request.script_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_script(
        self,
        request: aiops_20200806_models.AddScriptRequest,
    ) -> aiops_20200806_models.AddScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_script_with_options(request, runtime)

    async def add_script_async(
        self,
        request: aiops_20200806_models.AddScriptRequest,
    ) -> aiops_20200806_models.AddScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_script_with_options_async(request, runtime)

    def add_tag_info_with_options(
        self,
        request: aiops_20200806_models.AddTagInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddTagInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddTagInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tag_info_with_options_async(
        self,
        request: aiops_20200806_models.AddTagInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AddTagInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddTagInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tag_info(
        self,
        request: aiops_20200806_models.AddTagInfoRequest,
    ) -> aiops_20200806_models.AddTagInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tag_info_with_options(request, runtime)

    async def add_tag_info_async(
        self,
        request: aiops_20200806_models.AddTagInfoRequest,
    ) -> aiops_20200806_models.AddTagInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tag_info_with_options_async(request, runtime)

    def again_submit_apply_permission_with_options(
        self,
        request: aiops_20200806_models.AgainSubmitApplyPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AgainSubmitApplyPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgainSubmitApplyPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AgainSubmitApplyPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def again_submit_apply_permission_with_options_async(
        self,
        request: aiops_20200806_models.AgainSubmitApplyPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.AgainSubmitApplyPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgainSubmitApplyPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AgainSubmitApplyPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def again_submit_apply_permission(
        self,
        request: aiops_20200806_models.AgainSubmitApplyPermissionRequest,
    ) -> aiops_20200806_models.AgainSubmitApplyPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.again_submit_apply_permission_with_options(request, runtime)

    async def again_submit_apply_permission_async(
        self,
        request: aiops_20200806_models.AgainSubmitApplyPermissionRequest,
    ) -> aiops_20200806_models.AgainSubmitApplyPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.again_submit_apply_permission_with_options_async(request, runtime)

    def apply_authorization_with_options(
        self,
        request: aiops_20200806_models.ApplyAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ApplyAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ApplyAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_authorization_with_options_async(
        self,
        request: aiops_20200806_models.ApplyAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ApplyAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ApplyAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_authorization(
        self,
        request: aiops_20200806_models.ApplyAuthorizationRequest,
    ) -> aiops_20200806_models.ApplyAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_authorization_with_options(request, runtime)

    async def apply_authorization_async(
        self,
        request: aiops_20200806_models.ApplyAuthorizationRequest,
    ) -> aiops_20200806_models.ApplyAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_authorization_with_options_async(request, runtime)

    def check_data_source_link_connection_with_options(
        self,
        request: aiops_20200806_models.CheckDataSourceLinkConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CheckDataSourceLinkConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDataSourceLinkConnection',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CheckDataSourceLinkConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_source_link_connection_with_options_async(
        self,
        request: aiops_20200806_models.CheckDataSourceLinkConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CheckDataSourceLinkConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDataSourceLinkConnection',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CheckDataSourceLinkConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_source_link_connection(
        self,
        request: aiops_20200806_models.CheckDataSourceLinkConnectionRequest,
    ) -> aiops_20200806_models.CheckDataSourceLinkConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_data_source_link_connection_with_options(request, runtime)

    async def check_data_source_link_connection_async(
        self,
        request: aiops_20200806_models.CheckDataSourceLinkConnectionRequest,
    ) -> aiops_20200806_models.CheckDataSourceLinkConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_data_source_link_connection_with_options_async(request, runtime)

    def check_log_with_options(
        self,
        request: aiops_20200806_models.CheckLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CheckLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CheckLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_log_with_options_async(
        self,
        request: aiops_20200806_models.CheckLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CheckLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CheckLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_log(
        self,
        request: aiops_20200806_models.CheckLogRequest,
    ) -> aiops_20200806_models.CheckLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_log_with_options(request, runtime)

    async def check_log_async(
        self,
        request: aiops_20200806_models.CheckLogRequest,
    ) -> aiops_20200806_models.CheckLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_log_with_options_async(request, runtime)

    def close_event_with_options(
        self,
        request: aiops_20200806_models.CloseEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CloseEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.close_desc):
            query['CloseDesc'] = request.close_desc
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CloseEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_event_with_options_async(
        self,
        request: aiops_20200806_models.CloseEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CloseEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.close_desc):
            query['CloseDesc'] = request.close_desc
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CloseEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_event(
        self,
        request: aiops_20200806_models.CloseEventRequest,
    ) -> aiops_20200806_models.CloseEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_event_with_options(request, runtime)

    async def close_event_async(
        self,
        request: aiops_20200806_models.CloseEventRequest,
    ) -> aiops_20200806_models.CloseEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_event_with_options_async(request, runtime)

    def confirm_authorization_with_options(
        self,
        request: aiops_20200806_models.ConfirmAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ConfirmAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ConfirmAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_authorization_with_options_async(
        self,
        request: aiops_20200806_models.ConfirmAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ConfirmAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ConfirmAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_authorization(
        self,
        request: aiops_20200806_models.ConfirmAuthorizationRequest,
    ) -> aiops_20200806_models.ConfirmAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_authorization_with_options(request, runtime)

    async def confirm_authorization_async(
        self,
        request: aiops_20200806_models.ConfirmAuthorizationRequest,
    ) -> aiops_20200806_models.ConfirmAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_authorization_with_options_async(request, runtime)

    def count_latest_reports_with_options(
        self,
        request: aiops_20200806_models.CountLatestReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CountLatestReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountLatestReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CountLatestReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_latest_reports_with_options_async(
        self,
        request: aiops_20200806_models.CountLatestReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CountLatestReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountLatestReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CountLatestReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_latest_reports(
        self,
        request: aiops_20200806_models.CountLatestReportsRequest,
    ) -> aiops_20200806_models.CountLatestReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_latest_reports_with_options(request, runtime)

    async def count_latest_reports_async(
        self,
        request: aiops_20200806_models.CountLatestReportsRequest,
    ) -> aiops_20200806_models.CountLatestReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_latest_reports_with_options_async(request, runtime)

    def create_alert_contact_with_options(
        self,
        request: aiops_20200806_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateAlertContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.webhook):
            body['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_contact_with_options_async(
        self,
        request: aiops_20200806_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateAlertContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.webhook):
            body['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_contact(
        self,
        request: aiops_20200806_models.CreateAlertContactRequest,
    ) -> aiops_20200806_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    async def create_alert_contact_async(
        self,
        request: aiops_20200806_models.CreateAlertContactRequest,
    ) -> aiops_20200806_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_with_options_async(request, runtime)

    def create_alert_contact_group_with_options(
        self,
        request: aiops_20200806_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_contact_group_json):
            body['AlertContactGroupJson'] = request.alert_contact_group_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_contact_group_with_options_async(
        self,
        request: aiops_20200806_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_contact_group_json):
            body['AlertContactGroupJson'] = request.alert_contact_group_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_contact_group(
        self,
        request: aiops_20200806_models.CreateAlertContactGroupRequest,
    ) -> aiops_20200806_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    async def create_alert_contact_group_async(
        self,
        request: aiops_20200806_models.CreateAlertContactGroupRequest,
    ) -> aiops_20200806_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_group_with_options_async(request, runtime)

    def create_command_with_options(
        self,
        request: aiops_20200806_models.CreateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommand',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_command_with_options_async(
        self,
        request: aiops_20200806_models.CreateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommand',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_command(
        self,
        request: aiops_20200806_models.CreateCommandRequest,
    ) -> aiops_20200806_models.CreateCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    async def create_command_async(
        self,
        request: aiops_20200806_models.CreateCommandRequest,
    ) -> aiops_20200806_models.CreateCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_command_with_options_async(request, runtime)

    def create_dump_with_options(
        self,
        request: aiops_20200806_models.CreateDumpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateDumpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDump',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateDumpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dump_with_options_async(
        self,
        request: aiops_20200806_models.CreateDumpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateDumpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDump',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateDumpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dump(
        self,
        request: aiops_20200806_models.CreateDumpRequest,
    ) -> aiops_20200806_models.CreateDumpResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dump_with_options(request, runtime)

    async def create_dump_async(
        self,
        request: aiops_20200806_models.CreateDumpRequest,
    ) -> aiops_20200806_models.CreateDumpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dump_with_options_async(request, runtime)

    def create_inspection_record_with_options(
        self,
        request: aiops_20200806_models.CreateInspectionRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateInspectionRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInspectionRecord',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateInspectionRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_inspection_record_with_options_async(
        self,
        request: aiops_20200806_models.CreateInspectionRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateInspectionRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInspectionRecord',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateInspectionRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_inspection_record(
        self,
        request: aiops_20200806_models.CreateInspectionRecordRequest,
    ) -> aiops_20200806_models.CreateInspectionRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_inspection_record_with_options(request, runtime)

    async def create_inspection_record_async(
        self,
        request: aiops_20200806_models.CreateInspectionRecordRequest,
    ) -> aiops_20200806_models.CreateInspectionRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_inspection_record_with_options_async(request, runtime)

    def create_message_with_options(
        self,
        request: aiops_20200806_models.CreateMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessage',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_message_with_options_async(
        self,
        request: aiops_20200806_models.CreateMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessage',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_message(
        self,
        request: aiops_20200806_models.CreateMessageRequest,
    ) -> aiops_20200806_models.CreateMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_message_with_options(request, runtime)

    async def create_message_async(
        self,
        request: aiops_20200806_models.CreateMessageRequest,
    ) -> aiops_20200806_models.CreateMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_message_with_options_async(request, runtime)

    def create_scene_with_options(
        self,
        request: aiops_20200806_models.CreateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.metric_list_json):
            body['MetricListJson'] = request.metric_list_json
        if not UtilClient.is_unset(request.node_list_json):
            body['NodeListJson'] = request.node_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_desc):
            body['SceneDesc'] = request.scene_desc
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_owner):
            body['SceneOwner'] = request.scene_owner
        if not UtilClient.is_unset(request.scene_webhook):
            body['SceneWebhook'] = request.scene_webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_with_options_async(
        self,
        request: aiops_20200806_models.CreateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.metric_list_json):
            body['MetricListJson'] = request.metric_list_json
        if not UtilClient.is_unset(request.node_list_json):
            body['NodeListJson'] = request.node_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_desc):
            body['SceneDesc'] = request.scene_desc
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_owner):
            body['SceneOwner'] = request.scene_owner
        if not UtilClient.is_unset(request.scene_webhook):
            body['SceneWebhook'] = request.scene_webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene(
        self,
        request: aiops_20200806_models.CreateSceneRequest,
    ) -> aiops_20200806_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scene_with_options(request, runtime)

    async def create_scene_async(
        self,
        request: aiops_20200806_models.CreateSceneRequest,
    ) -> aiops_20200806_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scene_with_options_async(request, runtime)

    def create_scene_model_with_options(
        self,
        request: aiops_20200806_models.CreateSceneModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateSceneModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fc_function_name):
            body['FcFunctionName'] = request.fc_function_name
        if not UtilClient.is_unset(request.fc_handler):
            body['FcHandler'] = request.fc_handler
        if not UtilClient.is_unset(request.fc_initializer):
            body['FcInitializer'] = request.fc_initializer
        if not UtilClient.is_unset(request.fc_region_no):
            body['FcRegionNo'] = request.fc_region_no
        if not UtilClient.is_unset(request.fc_service_name):
            body['FcServiceName'] = request.fc_service_name
        if not UtilClient.is_unset(request.model_desc):
            body['ModelDesc'] = request.model_desc
        if not UtilClient.is_unset(request.model_language):
            body['ModelLanguage'] = request.model_language
        if not UtilClient.is_unset(request.model_memo):
            body['ModelMemo'] = request.model_memo
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.root_cause_desc):
            body['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_cause_solution):
            body['RootCauseSolution'] = request.root_cause_solution
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_model_with_options_async(
        self,
        request: aiops_20200806_models.CreateSceneModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateSceneModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fc_function_name):
            body['FcFunctionName'] = request.fc_function_name
        if not UtilClient.is_unset(request.fc_handler):
            body['FcHandler'] = request.fc_handler
        if not UtilClient.is_unset(request.fc_initializer):
            body['FcInitializer'] = request.fc_initializer
        if not UtilClient.is_unset(request.fc_region_no):
            body['FcRegionNo'] = request.fc_region_no
        if not UtilClient.is_unset(request.fc_service_name):
            body['FcServiceName'] = request.fc_service_name
        if not UtilClient.is_unset(request.model_desc):
            body['ModelDesc'] = request.model_desc
        if not UtilClient.is_unset(request.model_language):
            body['ModelLanguage'] = request.model_language
        if not UtilClient.is_unset(request.model_memo):
            body['ModelMemo'] = request.model_memo
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.root_cause_desc):
            body['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_cause_solution):
            body['RootCauseSolution'] = request.root_cause_solution
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene_model(
        self,
        request: aiops_20200806_models.CreateSceneModelRequest,
    ) -> aiops_20200806_models.CreateSceneModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scene_model_with_options(request, runtime)

    async def create_scene_model_async(
        self,
        request: aiops_20200806_models.CreateSceneModelRequest,
    ) -> aiops_20200806_models.CreateSceneModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scene_model_with_options_async(request, runtime)

    def create_scene_model_apply_with_options(
        self,
        request: aiops_20200806_models.CreateSceneModelApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateSceneModelApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSceneModelApply',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneModelApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_model_apply_with_options_async(
        self,
        request: aiops_20200806_models.CreateSceneModelApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.CreateSceneModelApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSceneModelApply',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneModelApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene_model_apply(
        self,
        request: aiops_20200806_models.CreateSceneModelApplyRequest,
    ) -> aiops_20200806_models.CreateSceneModelApplyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scene_model_apply_with_options(request, runtime)

    async def create_scene_model_apply_async(
        self,
        request: aiops_20200806_models.CreateSceneModelApplyRequest,
    ) -> aiops_20200806_models.CreateSceneModelApplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scene_model_apply_with_options_async(request, runtime)

    def del_business_group_with_options(
        self,
        request: aiops_20200806_models.DelBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DelBusinessGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DelBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_business_group_with_options_async(
        self,
        request: aiops_20200806_models.DelBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DelBusinessGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DelBusinessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_business_group(
        self,
        request: aiops_20200806_models.DelBusinessGroupRequest,
    ) -> aiops_20200806_models.DelBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.del_business_group_with_options(request, runtime)

    async def del_business_group_async(
        self,
        request: aiops_20200806_models.DelBusinessGroupRequest,
    ) -> aiops_20200806_models.DelBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.del_business_group_with_options_async(request, runtime)

    def delete_alert_contact_with_options(
        self,
        request: aiops_20200806_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_with_options_async(
        self,
        request: aiops_20200806_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact(
        self,
        request: aiops_20200806_models.DeleteAlertContactRequest,
    ) -> aiops_20200806_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    async def delete_alert_contact_async(
        self,
        request: aiops_20200806_models.DeleteAlertContactRequest,
    ) -> aiops_20200806_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_with_options_async(request, runtime)

    def delete_alert_contact_from_group_with_options(
        self,
        request: aiops_20200806_models.DeleteAlertContactFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertContactFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactFromGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_from_group_with_options_async(
        self,
        request: aiops_20200806_models.DeleteAlertContactFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertContactFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactFromGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact_from_group(
        self,
        request: aiops_20200806_models.DeleteAlertContactFromGroupRequest,
    ) -> aiops_20200806_models.DeleteAlertContactFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_from_group_with_options(request, runtime)

    async def delete_alert_contact_from_group_async(
        self,
        request: aiops_20200806_models.DeleteAlertContactFromGroupRequest,
    ) -> aiops_20200806_models.DeleteAlertContactFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_from_group_with_options_async(request, runtime)

    def delete_alert_contact_group_with_options(
        self,
        request: aiops_20200806_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_group_with_options_async(
        self,
        request: aiops_20200806_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact_group(
        self,
        request: aiops_20200806_models.DeleteAlertContactGroupRequest,
    ) -> aiops_20200806_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

    async def delete_alert_contact_group_async(
        self,
        request: aiops_20200806_models.DeleteAlertContactGroupRequest,
    ) -> aiops_20200806_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_group_with_options_async(request, runtime)

    def delete_alert_setting_with_options(
        self,
        request: aiops_20200806_models.DeleteAlertSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_setting_with_options_async(
        self,
        request: aiops_20200806_models.DeleteAlertSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_setting(
        self,
        request: aiops_20200806_models.DeleteAlertSettingRequest,
    ) -> aiops_20200806_models.DeleteAlertSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_setting_with_options(request, runtime)

    async def delete_alert_setting_async(
        self,
        request: aiops_20200806_models.DeleteAlertSettingRequest,
    ) -> aiops_20200806_models.DeleteAlertSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_setting_with_options_async(request, runtime)

    def delete_alert_setting_list_with_options(
        self,
        request: aiops_20200806_models.DeleteAlertSettingListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertSettingListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.customer_ids_json):
            body['CustomerIdsJson'] = request.customer_ids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertSettingList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertSettingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_setting_list_with_options_async(
        self,
        request: aiops_20200806_models.DeleteAlertSettingListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlertSettingListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.customer_ids_json):
            body['CustomerIdsJson'] = request.customer_ids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertSettingList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertSettingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_setting_list(
        self,
        request: aiops_20200806_models.DeleteAlertSettingListRequest,
    ) -> aiops_20200806_models.DeleteAlertSettingListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_setting_list_with_options(request, runtime)

    async def delete_alert_setting_list_async(
        self,
        request: aiops_20200806_models.DeleteAlertSettingListRequest,
    ) -> aiops_20200806_models.DeleteAlertSettingListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_setting_list_with_options_async(request, runtime)

    def delete_algorithm_info_with_options(
        self,
        request: aiops_20200806_models.DeleteAlgorithmInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlgorithmInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlgorithmInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlgorithmInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_algorithm_info_with_options_async(
        self,
        request: aiops_20200806_models.DeleteAlgorithmInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteAlgorithmInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlgorithmInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlgorithmInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_algorithm_info(
        self,
        request: aiops_20200806_models.DeleteAlgorithmInfoRequest,
    ) -> aiops_20200806_models.DeleteAlgorithmInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_algorithm_info_with_options(request, runtime)

    async def delete_algorithm_info_async(
        self,
        request: aiops_20200806_models.DeleteAlgorithmInfoRequest,
    ) -> aiops_20200806_models.DeleteAlgorithmInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_algorithm_info_with_options_async(request, runtime)

    def delete_business_group_with_options(
        self,
        request: aiops_20200806_models.DeleteBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteBusinessGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_business_group_with_options_async(
        self,
        request: aiops_20200806_models.DeleteBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteBusinessGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteBusinessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_business_group(
        self,
        request: aiops_20200806_models.DeleteBusinessGroupRequest,
    ) -> aiops_20200806_models.DeleteBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_business_group_with_options(request, runtime)

    async def delete_business_group_async(
        self,
        request: aiops_20200806_models.DeleteBusinessGroupRequest,
    ) -> aiops_20200806_models.DeleteBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_business_group_with_options_async(request, runtime)

    def delete_business_resource_tag_with_options(
        self,
        request: aiops_20200806_models.DeleteBusinessResourceTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteBusinessResourceTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessResourceTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteBusinessResourceTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_business_resource_tag_with_options_async(
        self,
        request: aiops_20200806_models.DeleteBusinessResourceTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteBusinessResourceTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessResourceTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteBusinessResourceTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_business_resource_tag(
        self,
        request: aiops_20200806_models.DeleteBusinessResourceTagRequest,
    ) -> aiops_20200806_models.DeleteBusinessResourceTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_business_resource_tag_with_options(request, runtime)

    async def delete_business_resource_tag_async(
        self,
        request: aiops_20200806_models.DeleteBusinessResourceTagRequest,
    ) -> aiops_20200806_models.DeleteBusinessResourceTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_business_resource_tag_with_options_async(request, runtime)

    def delete_data_source_config_with_options(
        self,
        request: aiops_20200806_models.DeleteDataSourceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteDataSourceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteDataSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_config_with_options_async(
        self,
        request: aiops_20200806_models.DeleteDataSourceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteDataSourceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteDataSourceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source_config(
        self,
        request: aiops_20200806_models.DeleteDataSourceConfigRequest,
    ) -> aiops_20200806_models.DeleteDataSourceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_config_with_options(request, runtime)

    async def delete_data_source_config_async(
        self,
        request: aiops_20200806_models.DeleteDataSourceConfigRequest,
    ) -> aiops_20200806_models.DeleteDataSourceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_config_with_options_async(request, runtime)

    def delete_group_topology_tag_log_with_options(
        self,
        request: aiops_20200806_models.DeleteGroupTopologyTagLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteGroupTopologyTagLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupTopologyTagLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteGroupTopologyTagLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_topology_tag_log_with_options_async(
        self,
        request: aiops_20200806_models.DeleteGroupTopologyTagLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteGroupTopologyTagLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupTopologyTagLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteGroupTopologyTagLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_topology_tag_log(
        self,
        request: aiops_20200806_models.DeleteGroupTopologyTagLogRequest,
    ) -> aiops_20200806_models.DeleteGroupTopologyTagLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_topology_tag_log_with_options(request, runtime)

    async def delete_group_topology_tag_log_async(
        self,
        request: aiops_20200806_models.DeleteGroupTopologyTagLogRequest,
    ) -> aiops_20200806_models.DeleteGroupTopologyTagLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_topology_tag_log_with_options_async(request, runtime)

    def delete_real_scene_info_with_options(
        self,
        request: aiops_20200806_models.DeleteRealSceneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteRealSceneInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRealSceneInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteRealSceneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_real_scene_info_with_options_async(
        self,
        request: aiops_20200806_models.DeleteRealSceneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteRealSceneInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRealSceneInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteRealSceneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_real_scene_info(
        self,
        request: aiops_20200806_models.DeleteRealSceneInfoRequest,
    ) -> aiops_20200806_models.DeleteRealSceneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_real_scene_info_with_options(request, runtime)

    async def delete_real_scene_info_async(
        self,
        request: aiops_20200806_models.DeleteRealSceneInfoRequest,
    ) -> aiops_20200806_models.DeleteRealSceneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_real_scene_info_with_options_async(request, runtime)

    def delete_report_email_config_with_options(
        self,
        request: aiops_20200806_models.DeleteReportEmailConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteReportEmailConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mail_config_id):
            body['MailConfigId'] = request.mail_config_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteReportEmailConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteReportEmailConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_report_email_config_with_options_async(
        self,
        request: aiops_20200806_models.DeleteReportEmailConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteReportEmailConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mail_config_id):
            body['MailConfigId'] = request.mail_config_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteReportEmailConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteReportEmailConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_report_email_config(
        self,
        request: aiops_20200806_models.DeleteReportEmailConfigRequest,
    ) -> aiops_20200806_models.DeleteReportEmailConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_report_email_config_with_options(request, runtime)

    async def delete_report_email_config_async(
        self,
        request: aiops_20200806_models.DeleteReportEmailConfigRequest,
    ) -> aiops_20200806_models.DeleteReportEmailConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_report_email_config_with_options_async(request, runtime)

    def delete_resource_whitelist_with_options(
        self,
        request: aiops_20200806_models.DeleteResourceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteResourceWhitelistResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inspection_whitelist_id):
            body['InspectionWhitelistId'] = request.inspection_whitelist_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResourceWhitelist',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteResourceWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_whitelist_with_options_async(
        self,
        request: aiops_20200806_models.DeleteResourceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteResourceWhitelistResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inspection_whitelist_id):
            body['InspectionWhitelistId'] = request.inspection_whitelist_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResourceWhitelist',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteResourceWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_whitelist(
        self,
        request: aiops_20200806_models.DeleteResourceWhitelistRequest,
    ) -> aiops_20200806_models.DeleteResourceWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_whitelist_with_options(request, runtime)

    async def delete_resource_whitelist_async(
        self,
        request: aiops_20200806_models.DeleteResourceWhitelistRequest,
    ) -> aiops_20200806_models.DeleteResourceWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_whitelist_with_options_async(request, runtime)

    def delete_scenario_with_options(
        self,
        request: aiops_20200806_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scenario_with_options_async(
        self,
        request: aiops_20200806_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scenario(
        self,
        request: aiops_20200806_models.DeleteScenarioRequest,
    ) -> aiops_20200806_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

    async def delete_scenario_async(
        self,
        request: aiops_20200806_models.DeleteScenarioRequest,
    ) -> aiops_20200806_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scenario_with_options_async(request, runtime)

    def delete_scene_with_options(
        self,
        request: aiops_20200806_models.DeleteSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_with_options_async(
        self,
        request: aiops_20200806_models.DeleteSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene(
        self,
        request: aiops_20200806_models.DeleteSceneRequest,
    ) -> aiops_20200806_models.DeleteSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_with_options(request, runtime)

    async def delete_scene_async(
        self,
        request: aiops_20200806_models.DeleteSceneRequest,
    ) -> aiops_20200806_models.DeleteSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scene_with_options_async(request, runtime)

    def delete_scene_list_with_options(
        self,
        request: aiops_20200806_models.DeleteSceneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteSceneListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_list_with_options_async(
        self,
        request: aiops_20200806_models.DeleteSceneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteSceneListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene_list(
        self,
        request: aiops_20200806_models.DeleteSceneListRequest,
    ) -> aiops_20200806_models.DeleteSceneListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_list_with_options(request, runtime)

    async def delete_scene_list_async(
        self,
        request: aiops_20200806_models.DeleteSceneListRequest,
    ) -> aiops_20200806_models.DeleteSceneListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scene_list_with_options_async(request, runtime)

    def delete_scene_model_with_options(
        self,
        request: aiops_20200806_models.DeleteSceneModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteSceneModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.sure_delete):
            body['SureDelete'] = request.sure_delete
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_model_with_options_async(
        self,
        request: aiops_20200806_models.DeleteSceneModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteSceneModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.sure_delete):
            body['SureDelete'] = request.sure_delete
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene_model(
        self,
        request: aiops_20200806_models.DeleteSceneModelRequest,
    ) -> aiops_20200806_models.DeleteSceneModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_model_with_options(request, runtime)

    async def delete_scene_model_async(
        self,
        request: aiops_20200806_models.DeleteSceneModelRequest,
    ) -> aiops_20200806_models.DeleteSceneModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scene_model_with_options_async(request, runtime)

    def delete_tag_info_with_options(
        self,
        request: aiops_20200806_models.DeleteTagInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteTagInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteTagInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_info_with_options_async(
        self,
        request: aiops_20200806_models.DeleteTagInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DeleteTagInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteTagInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag_info(
        self,
        request: aiops_20200806_models.DeleteTagInfoRequest,
    ) -> aiops_20200806_models.DeleteTagInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_info_with_options(request, runtime)

    async def delete_tag_info_async(
        self,
        request: aiops_20200806_models.DeleteTagInfoRequest,
    ) -> aiops_20200806_models.DeleteTagInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_info_with_options_async(request, runtime)

    def describe_account_alert_event_with_options(
        self,
        request: aiops_20200806_models.DescribeAccountAlertEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAccountAlertEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAlertEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAccountAlertEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_alert_event_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAccountAlertEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAccountAlertEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAlertEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAccountAlertEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_alert_event(
        self,
        request: aiops_20200806_models.DescribeAccountAlertEventRequest,
    ) -> aiops_20200806_models.DescribeAccountAlertEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_alert_event_with_options(request, runtime)

    async def describe_account_alert_event_async(
        self,
        request: aiops_20200806_models.DescribeAccountAlertEventRequest,
    ) -> aiops_20200806_models.DescribeAccountAlertEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_alert_event_with_options_async(request, runtime)

    def describe_advisor_inspection_products_with_options(
        self,
        request: aiops_20200806_models.DescribeAdvisorInspectionProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAdvisorInspectionProductsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorInspectionProducts',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAdvisorInspectionProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advisor_inspection_products_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAdvisorInspectionProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAdvisorInspectionProductsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorInspectionProducts',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAdvisorInspectionProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advisor_inspection_products(
        self,
        request: aiops_20200806_models.DescribeAdvisorInspectionProductsRequest,
    ) -> aiops_20200806_models.DescribeAdvisorInspectionProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_advisor_inspection_products_with_options(request, runtime)

    async def describe_advisor_inspection_products_async(
        self,
        request: aiops_20200806_models.DescribeAdvisorInspectionProductsRequest,
    ) -> aiops_20200806_models.DescribeAdvisorInspectionProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_advisor_inspection_products_with_options_async(request, runtime)

    def describe_alert_business_group_with_alert_setting_id_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertBusinessGroupWithAlertSettingId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_business_group_with_alert_setting_id_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertBusinessGroupWithAlertSettingId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_business_group_with_alert_setting_id(
        self,
        request: aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdRequest,
    ) -> aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_business_group_with_alert_setting_id_with_options(request, runtime)

    async def describe_alert_business_group_with_alert_setting_id_async(
        self,
        request: aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdRequest,
    ) -> aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_business_group_with_alert_setting_id_with_options_async(request, runtime)

    def describe_alert_contact_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_by):
            body['SearchBy'] = request.search_by
        if not UtilClient.is_unset(request.search_like):
            body['SearchLike'] = request.search_like
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_contact_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_by):
            body['SearchBy'] = request.search_by
        if not UtilClient.is_unset(request.search_like):
            body['SearchLike'] = request.search_like
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_contact(
        self,
        request: aiops_20200806_models.DescribeAlertContactRequest,
    ) -> aiops_20200806_models.DescribeAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_contact_with_options(request, runtime)

    async def describe_alert_contact_async(
        self,
        request: aiops_20200806_models.DescribeAlertContactRequest,
    ) -> aiops_20200806_models.DescribeAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_contact_with_options_async(request, runtime)

    def describe_alert_contact_group_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertContactGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_like):
            body['SearchLike'] = request.search_like
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_contact_group_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertContactGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_like):
            body['SearchLike'] = request.search_like
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_contact_group(
        self,
        request: aiops_20200806_models.DescribeAlertContactGroupRequest,
    ) -> aiops_20200806_models.DescribeAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_contact_group_with_options(request, runtime)

    async def describe_alert_contact_group_async(
        self,
        request: aiops_20200806_models.DescribeAlertContactGroupRequest,
    ) -> aiops_20200806_models.DescribeAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_contact_group_with_options_async(request, runtime)

    def describe_alert_contact_with_alert_setting_id_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertContactWithAlertSettingIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertContactWithAlertSettingIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.contact_type):
            body['ContactType'] = request.contact_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactWithAlertSettingId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactWithAlertSettingIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_contact_with_alert_setting_id_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertContactWithAlertSettingIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertContactWithAlertSettingIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.contact_type):
            body['ContactType'] = request.contact_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactWithAlertSettingId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactWithAlertSettingIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_contact_with_alert_setting_id(
        self,
        request: aiops_20200806_models.DescribeAlertContactWithAlertSettingIdRequest,
    ) -> aiops_20200806_models.DescribeAlertContactWithAlertSettingIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_contact_with_alert_setting_id_with_options(request, runtime)

    async def describe_alert_contact_with_alert_setting_id_async(
        self,
        request: aiops_20200806_models.DescribeAlertContactWithAlertSettingIdRequest,
    ) -> aiops_20200806_models.DescribeAlertContactWithAlertSettingIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_contact_with_alert_setting_id_with_options_async(request, runtime)

    def describe_alert_contact_with_group_id_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertContactWithGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertContactWithGroupIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactWithGroupId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactWithGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_contact_with_group_id_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertContactWithGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertContactWithGroupIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactWithGroupId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactWithGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_contact_with_group_id(
        self,
        request: aiops_20200806_models.DescribeAlertContactWithGroupIdRequest,
    ) -> aiops_20200806_models.DescribeAlertContactWithGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_contact_with_group_id_with_options(request, runtime)

    async def describe_alert_contact_with_group_id_async(
        self,
        request: aiops_20200806_models.DescribeAlertContactWithGroupIdRequest,
    ) -> aiops_20200806_models.DescribeAlertContactWithGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_contact_with_group_id_with_options_async(request, runtime)

    def describe_alert_detail_data_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertDetailDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertDetailData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_detail_data_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertDetailDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertDetailData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertDetailDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_detail_data(
        self,
        request: aiops_20200806_models.DescribeAlertDetailDataRequest,
    ) -> aiops_20200806_models.DescribeAlertDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_detail_data_with_options(request, runtime)

    async def describe_alert_detail_data_async(
        self,
        request: aiops_20200806_models.DescribeAlertDetailDataRequest,
    ) -> aiops_20200806_models.DescribeAlertDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_detail_data_with_options_async(request, runtime)

    def describe_alert_detail_trend_data_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertDetailTrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertDetailTrendDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertDetailTrendDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_detail_trend_data_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertDetailTrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertDetailTrendDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertDetailTrendDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_detail_trend_data(
        self,
        request: aiops_20200806_models.DescribeAlertDetailTrendDataRequest,
    ) -> aiops_20200806_models.DescribeAlertDetailTrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_detail_trend_data_with_options(request, runtime)

    async def describe_alert_detail_trend_data_async(
        self,
        request: aiops_20200806_models.DescribeAlertDetailTrendDataRequest,
    ) -> aiops_20200806_models.DescribeAlertDetailTrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_detail_trend_data_with_options_async(request, runtime)

    def describe_alert_event_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_event_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_event(
        self,
        request: aiops_20200806_models.DescribeAlertEventRequest,
    ) -> aiops_20200806_models.DescribeAlertEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_event_with_options(request, runtime)

    async def describe_alert_event_async(
        self,
        request: aiops_20200806_models.DescribeAlertEventRequest,
    ) -> aiops_20200806_models.DescribeAlertEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_event_with_options_async(request, runtime)

    def describe_alert_final_data_list_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertFinalDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertFinalDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertFinalDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertFinalDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_final_data_list_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertFinalDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertFinalDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertFinalDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertFinalDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_final_data_list(
        self,
        request: aiops_20200806_models.DescribeAlertFinalDataListRequest,
    ) -> aiops_20200806_models.DescribeAlertFinalDataListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_final_data_list_with_options(request, runtime)

    async def describe_alert_final_data_list_async(
        self,
        request: aiops_20200806_models.DescribeAlertFinalDataListRequest,
    ) -> aiops_20200806_models.DescribeAlertFinalDataListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_final_data_list_with_options_async(request, runtime)

    def describe_alert_resource_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_resource_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_resource(
        self,
        request: aiops_20200806_models.DescribeAlertResourceRequest,
    ) -> aiops_20200806_models.DescribeAlertResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_resource_with_options(request, runtime)

    async def describe_alert_resource_async(
        self,
        request: aiops_20200806_models.DescribeAlertResourceRequest,
    ) -> aiops_20200806_models.DescribeAlertResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_resource_with_options_async(request, runtime)

    def describe_alert_setting_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertSettingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.customer_name):
            body['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.setting_status):
            body['SettingStatus'] = request.setting_status
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_setting_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertSettingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.customer_name):
            body['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.setting_status):
            body['SettingStatus'] = request.setting_status
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_setting(
        self,
        request: aiops_20200806_models.DescribeAlertSettingRequest,
    ) -> aiops_20200806_models.DescribeAlertSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_setting_with_options(request, runtime)

    async def describe_alert_setting_async(
        self,
        request: aiops_20200806_models.DescribeAlertSettingRequest,
    ) -> aiops_20200806_models.DescribeAlertSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_setting_with_options_async(request, runtime)

    def describe_alert_setting_by_id_with_options(
        self,
        request: aiops_20200806_models.DescribeAlertSettingByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertSettingByIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSettingById',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertSettingByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_setting_by_id_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAlertSettingByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAlertSettingByIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSettingById',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertSettingByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_setting_by_id(
        self,
        request: aiops_20200806_models.DescribeAlertSettingByIdRequest,
    ) -> aiops_20200806_models.DescribeAlertSettingByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_setting_by_id_with_options(request, runtime)

    async def describe_alert_setting_by_id_async(
        self,
        request: aiops_20200806_models.DescribeAlertSettingByIdRequest,
    ) -> aiops_20200806_models.DescribeAlertSettingByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_setting_by_id_with_options_async(request, runtime)

    def describe_all_alert_contact_with_options(
        self,
        request: aiops_20200806_models.DescribeAllAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAllAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_alert_contact_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAllAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAllAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_alert_contact(
        self,
        request: aiops_20200806_models.DescribeAllAlertContactRequest,
    ) -> aiops_20200806_models.DescribeAllAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_alert_contact_with_options(request, runtime)

    async def describe_all_alert_contact_async(
        self,
        request: aiops_20200806_models.DescribeAllAlertContactRequest,
    ) -> aiops_20200806_models.DescribeAllAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_alert_contact_with_options_async(request, runtime)

    def describe_all_alert_contact_group_with_options(
        self,
        request: aiops_20200806_models.DescribeAllAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAllAlertContactGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAllAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_alert_contact_group_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAllAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAllAlertContactGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAllAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_alert_contact_group(
        self,
        request: aiops_20200806_models.DescribeAllAlertContactGroupRequest,
    ) -> aiops_20200806_models.DescribeAllAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_alert_contact_group_with_options(request, runtime)

    async def describe_all_alert_contact_group_async(
        self,
        request: aiops_20200806_models.DescribeAllAlertContactGroupRequest,
    ) -> aiops_20200806_models.DescribeAllAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_alert_contact_group_with_options_async(request, runtime)

    def describe_all_business_group_info_with_options(
        self,
        request: aiops_20200806_models.DescribeAllBusinessGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAllBusinessGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllBusinessGroupInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllBusinessGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_business_group_info_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAllBusinessGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAllBusinessGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllBusinessGroupInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllBusinessGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_business_group_info(
        self,
        request: aiops_20200806_models.DescribeAllBusinessGroupInfoRequest,
    ) -> aiops_20200806_models.DescribeAllBusinessGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_business_group_info_with_options(request, runtime)

    async def describe_all_business_group_info_async(
        self,
        request: aiops_20200806_models.DescribeAllBusinessGroupInfoRequest,
    ) -> aiops_20200806_models.DescribeAllBusinessGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_business_group_info_with_options_async(request, runtime)

    def describe_all_scene_model_with_options(
        self,
        request: aiops_20200806_models.DescribeAllSceneModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAllSceneModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAllSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllSceneModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_scene_model_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAllSceneModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAllSceneModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAllSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllSceneModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_scene_model(
        self,
        request: aiops_20200806_models.DescribeAllSceneModelRequest,
    ) -> aiops_20200806_models.DescribeAllSceneModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_scene_model_with_options(request, runtime)

    async def describe_all_scene_model_async(
        self,
        request: aiops_20200806_models.DescribeAllSceneModelRequest,
    ) -> aiops_20200806_models.DescribeAllSceneModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_scene_model_with_options_async(request, runtime)

    def describe_analysis_data_list_with_options(
        self,
        request: aiops_20200806_models.DescribeAnalysisDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAnalysisDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_extend):
            query['MetricExtend'] = request.metric_extend
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnalysisDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAnalysisDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_analysis_data_list_with_options_async(
        self,
        request: aiops_20200806_models.DescribeAnalysisDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeAnalysisDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_extend):
            query['MetricExtend'] = request.metric_extend
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnalysisDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAnalysisDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_analysis_data_list(
        self,
        request: aiops_20200806_models.DescribeAnalysisDataListRequest,
    ) -> aiops_20200806_models.DescribeAnalysisDataListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_analysis_data_list_with_options(request, runtime)

    async def describe_analysis_data_list_async(
        self,
        request: aiops_20200806_models.DescribeAnalysisDataListRequest,
    ) -> aiops_20200806_models.DescribeAnalysisDataListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_analysis_data_list_with_options_async(request, runtime)

    def describe_business_analysis_data_list_with_options(
        self,
        request: aiops_20200806_models.DescribeBusinessAnalysisDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeBusinessAnalysisDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_path):
            query['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBusinessAnalysisDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeBusinessAnalysisDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_business_analysis_data_list_with_options_async(
        self,
        request: aiops_20200806_models.DescribeBusinessAnalysisDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeBusinessAnalysisDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_path):
            query['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBusinessAnalysisDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeBusinessAnalysisDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_business_analysis_data_list(
        self,
        request: aiops_20200806_models.DescribeBusinessAnalysisDataListRequest,
    ) -> aiops_20200806_models.DescribeBusinessAnalysisDataListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_business_analysis_data_list_with_options(request, runtime)

    async def describe_business_analysis_data_list_async(
        self,
        request: aiops_20200806_models.DescribeBusinessAnalysisDataListRequest,
    ) -> aiops_20200806_models.DescribeBusinessAnalysisDataListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_business_analysis_data_list_with_options_async(request, runtime)

    def describe_diagnose_with_options(
        self,
        request: aiops_20200806_models.DescribeDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnose',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnose_with_options_async(
        self,
        request: aiops_20200806_models.DescribeDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnose',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnose(
        self,
        request: aiops_20200806_models.DescribeDiagnoseRequest,
    ) -> aiops_20200806_models.DescribeDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnose_with_options(request, runtime)

    async def describe_diagnose_async(
        self,
        request: aiops_20200806_models.DescribeDiagnoseRequest,
    ) -> aiops_20200806_models.DescribeDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnose_with_options_async(request, runtime)

    def describe_diagnose_result_with_options(
        self,
        request: aiops_20200806_models.DescribeDiagnoseResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeDiagnoseResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnoseResult',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeDiagnoseResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnose_result_with_options_async(
        self,
        request: aiops_20200806_models.DescribeDiagnoseResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeDiagnoseResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnoseResult',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeDiagnoseResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnose_result(
        self,
        request: aiops_20200806_models.DescribeDiagnoseResultRequest,
    ) -> aiops_20200806_models.DescribeDiagnoseResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnose_result_with_options(request, runtime)

    async def describe_diagnose_result_async(
        self,
        request: aiops_20200806_models.DescribeDiagnoseResultRequest,
    ) -> aiops_20200806_models.DescribeDiagnoseResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnose_result_with_options_async(request, runtime)

    def describe_event_topology_with_options(
        self,
        request: aiops_20200806_models.DescribeEventTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeEventTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTopology',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeEventTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_topology_with_options_async(
        self,
        request: aiops_20200806_models.DescribeEventTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeEventTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTopology',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeEventTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_topology(
        self,
        request: aiops_20200806_models.DescribeEventTopologyRequest,
    ) -> aiops_20200806_models.DescribeEventTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_topology_with_options(request, runtime)

    async def describe_event_topology_async(
        self,
        request: aiops_20200806_models.DescribeEventTopologyRequest,
    ) -> aiops_20200806_models.DescribeEventTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_topology_with_options_async(request, runtime)

    def describe_event_topology_detail_with_options(
        self,
        request: aiops_20200806_models.DescribeEventTopologyDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeEventTopologyDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTopologyDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeEventTopologyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_topology_detail_with_options_async(
        self,
        request: aiops_20200806_models.DescribeEventTopologyDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeEventTopologyDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTopologyDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeEventTopologyDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_topology_detail(
        self,
        request: aiops_20200806_models.DescribeEventTopologyDetailRequest,
    ) -> aiops_20200806_models.DescribeEventTopologyDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_topology_detail_with_options(request, runtime)

    async def describe_event_topology_detail_async(
        self,
        request: aiops_20200806_models.DescribeEventTopologyDetailRequest,
    ) -> aiops_20200806_models.DescribeEventTopologyDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_topology_detail_with_options_async(request, runtime)

    def describe_fc_function_with_options(
        self,
        request: aiops_20200806_models.DescribeFcFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeFcFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcFunction',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fc_function_with_options_async(
        self,
        request: aiops_20200806_models.DescribeFcFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeFcFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcFunction',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fc_function(
        self,
        request: aiops_20200806_models.DescribeFcFunctionRequest,
    ) -> aiops_20200806_models.DescribeFcFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fc_function_with_options(request, runtime)

    async def describe_fc_function_async(
        self,
        request: aiops_20200806_models.DescribeFcFunctionRequest,
    ) -> aiops_20200806_models.DescribeFcFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fc_function_with_options_async(request, runtime)

    def describe_fc_region_with_options(
        self,
        request: aiops_20200806_models.DescribeFcRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeFcRegionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcRegion',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fc_region_with_options_async(
        self,
        request: aiops_20200806_models.DescribeFcRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeFcRegionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcRegion',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fc_region(
        self,
        request: aiops_20200806_models.DescribeFcRegionRequest,
    ) -> aiops_20200806_models.DescribeFcRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fc_region_with_options(request, runtime)

    async def describe_fc_region_async(
        self,
        request: aiops_20200806_models.DescribeFcRegionRequest,
    ) -> aiops_20200806_models.DescribeFcRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fc_region_with_options_async(request, runtime)

    def describe_fc_service_with_options(
        self,
        request: aiops_20200806_models.DescribeFcServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeFcServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcService',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fc_service_with_options_async(
        self,
        request: aiops_20200806_models.DescribeFcServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeFcServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcService',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fc_service(
        self,
        request: aiops_20200806_models.DescribeFcServiceRequest,
    ) -> aiops_20200806_models.DescribeFcServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fc_service_with_options(request, runtime)

    async def describe_fc_service_async(
        self,
        request: aiops_20200806_models.DescribeFcServiceRequest,
    ) -> aiops_20200806_models.DescribeFcServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fc_service_with_options_async(request, runtime)

    def describe_history_risk_with_options(
        self,
        request: aiops_20200806_models.DescribeHistoryRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeHistoryRiskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.last_find_time_end):
            body['LastFindTimeEnd'] = request.last_find_time_end
        if not UtilClient.is_unset(request.last_find_time_start):
            body['LastFindTimeStart'] = request.last_find_time_start
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            body['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeHistoryRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeHistoryRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_risk_with_options_async(
        self,
        request: aiops_20200806_models.DescribeHistoryRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeHistoryRiskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.last_find_time_end):
            body['LastFindTimeEnd'] = request.last_find_time_end
        if not UtilClient.is_unset(request.last_find_time_start):
            body['LastFindTimeStart'] = request.last_find_time_start
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            body['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeHistoryRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeHistoryRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_risk(
        self,
        request: aiops_20200806_models.DescribeHistoryRiskRequest,
    ) -> aiops_20200806_models.DescribeHistoryRiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_history_risk_with_options(request, runtime)

    async def describe_history_risk_async(
        self,
        request: aiops_20200806_models.DescribeHistoryRiskRequest,
    ) -> aiops_20200806_models.DescribeHistoryRiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_risk_with_options_async(request, runtime)

    def describe_inspection_progress_with_options(
        self,
        request: aiops_20200806_models.DescribeInspectionProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionProgressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inspection_record_id):
            body['InspectionRecordId'] = request.inspection_record_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionProgress',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inspection_progress_with_options_async(
        self,
        request: aiops_20200806_models.DescribeInspectionProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionProgressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inspection_record_id):
            body['InspectionRecordId'] = request.inspection_record_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionProgress',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inspection_progress(
        self,
        request: aiops_20200806_models.DescribeInspectionProgressRequest,
    ) -> aiops_20200806_models.DescribeInspectionProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_progress_with_options(request, runtime)

    async def describe_inspection_progress_async(
        self,
        request: aiops_20200806_models.DescribeInspectionProgressRequest,
    ) -> aiops_20200806_models.DescribeInspectionProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inspection_progress_with_options_async(request, runtime)

    def describe_inspection_resources_with_options(
        self,
        request: aiops_20200806_models.DescribeInspectionResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionResources',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inspection_resources_with_options_async(
        self,
        request: aiops_20200806_models.DescribeInspectionResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionResources',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inspection_resources(
        self,
        request: aiops_20200806_models.DescribeInspectionResourcesRequest,
    ) -> aiops_20200806_models.DescribeInspectionResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_resources_with_options(request, runtime)

    async def describe_inspection_resources_async(
        self,
        request: aiops_20200806_models.DescribeInspectionResourcesRequest,
    ) -> aiops_20200806_models.DescribeInspectionResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inspection_resources_with_options_async(request, runtime)

    def describe_inspection_result_with_options(
        self,
        request: aiops_20200806_models.DescribeInspectionResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.severity):
            body['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionResult',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inspection_result_with_options_async(
        self,
        request: aiops_20200806_models.DescribeInspectionResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.severity):
            body['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionResult',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inspection_result(
        self,
        request: aiops_20200806_models.DescribeInspectionResultRequest,
    ) -> aiops_20200806_models.DescribeInspectionResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_result_with_options(request, runtime)

    async def describe_inspection_result_async(
        self,
        request: aiops_20200806_models.DescribeInspectionResultRequest,
    ) -> aiops_20200806_models.DescribeInspectionResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inspection_result_with_options_async(request, runtime)

    def describe_inspection_settings_with_options(
        self,
        request: aiops_20200806_models.DescribeInspectionSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionSettingsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.risk_desc):
            body['RiskDesc'] = request.risk_desc
        if not UtilClient.is_unset(request.risk_enable_status):
            body['RiskEnableStatus'] = request.risk_enable_status
        if not UtilClient.is_unset(request.risk_name):
            body['RiskName'] = request.risk_name
        if not UtilClient.is_unset(request.risk_type):
            body['RiskType'] = request.risk_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionSettings',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inspection_settings_with_options_async(
        self,
        request: aiops_20200806_models.DescribeInspectionSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionSettingsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.risk_desc):
            body['RiskDesc'] = request.risk_desc
        if not UtilClient.is_unset(request.risk_enable_status):
            body['RiskEnableStatus'] = request.risk_enable_status
        if not UtilClient.is_unset(request.risk_name):
            body['RiskName'] = request.risk_name
        if not UtilClient.is_unset(request.risk_type):
            body['RiskType'] = request.risk_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionSettings',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inspection_settings(
        self,
        request: aiops_20200806_models.DescribeInspectionSettingsRequest,
    ) -> aiops_20200806_models.DescribeInspectionSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_settings_with_options(request, runtime)

    async def describe_inspection_settings_async(
        self,
        request: aiops_20200806_models.DescribeInspectionSettingsRequest,
    ) -> aiops_20200806_models.DescribeInspectionSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inspection_settings_with_options_async(request, runtime)

    def describe_inspection_threshold_with_options(
        self,
        request: aiops_20200806_models.DescribeInspectionThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionThresholdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionThreshold',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inspection_threshold_with_options_async(
        self,
        request: aiops_20200806_models.DescribeInspectionThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionThresholdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionThreshold',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inspection_threshold(
        self,
        request: aiops_20200806_models.DescribeInspectionThresholdRequest,
    ) -> aiops_20200806_models.DescribeInspectionThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_threshold_with_options(request, runtime)

    async def describe_inspection_threshold_async(
        self,
        request: aiops_20200806_models.DescribeInspectionThresholdRequest,
    ) -> aiops_20200806_models.DescribeInspectionThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inspection_threshold_with_options_async(request, runtime)

    def describe_inspection_whitelists_with_options(
        self,
        request: aiops_20200806_models.DescribeInspectionWhitelistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionWhitelistsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionWhitelists',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionWhitelistsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inspection_whitelists_with_options_async(
        self,
        request: aiops_20200806_models.DescribeInspectionWhitelistsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInspectionWhitelistsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionWhitelists',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionWhitelistsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inspection_whitelists(
        self,
        request: aiops_20200806_models.DescribeInspectionWhitelistsRequest,
    ) -> aiops_20200806_models.DescribeInspectionWhitelistsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_whitelists_with_options(request, runtime)

    async def describe_inspection_whitelists_async(
        self,
        request: aiops_20200806_models.DescribeInspectionWhitelistsRequest,
    ) -> aiops_20200806_models.DescribeInspectionWhitelistsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inspection_whitelists_with_options_async(request, runtime)

    def describe_invocation_results_with_options(
        self,
        request: aiops_20200806_models.DescribeInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInvocationResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocationResults',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInvocationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocation_results_with_options_async(
        self,
        request: aiops_20200806_models.DescribeInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeInvocationResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocationResults',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInvocationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocation_results(
        self,
        request: aiops_20200806_models.DescribeInvocationResultsRequest,
    ) -> aiops_20200806_models.DescribeInvocationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocation_results_with_options(request, runtime)

    async def describe_invocation_results_async(
        self,
        request: aiops_20200806_models.DescribeInvocationResultsRequest,
    ) -> aiops_20200806_models.DescribeInvocationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocation_results_with_options_async(request, runtime)

    def describe_last_inspection_summary_with_options(
        self,
        request: aiops_20200806_models.DescribeLastInspectionSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeLastInspectionSummaryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLastInspectionSummary',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeLastInspectionSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_last_inspection_summary_with_options_async(
        self,
        request: aiops_20200806_models.DescribeLastInspectionSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeLastInspectionSummaryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLastInspectionSummary',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeLastInspectionSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_last_inspection_summary(
        self,
        request: aiops_20200806_models.DescribeLastInspectionSummaryRequest,
    ) -> aiops_20200806_models.DescribeLastInspectionSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_last_inspection_summary_with_options(request, runtime)

    async def describe_last_inspection_summary_async(
        self,
        request: aiops_20200806_models.DescribeLastInspectionSummaryRequest,
    ) -> aiops_20200806_models.DescribeLastInspectionSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_last_inspection_summary_with_options_async(request, runtime)

    def describe_model_relation_scenes_with_options(
        self,
        request: aiops_20200806_models.DescribeModelRelationScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeModelRelationScenesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeModelRelationScenes',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeModelRelationScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_model_relation_scenes_with_options_async(
        self,
        request: aiops_20200806_models.DescribeModelRelationScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeModelRelationScenesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeModelRelationScenes',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeModelRelationScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_model_relation_scenes(
        self,
        request: aiops_20200806_models.DescribeModelRelationScenesRequest,
    ) -> aiops_20200806_models.DescribeModelRelationScenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_model_relation_scenes_with_options(request, runtime)

    async def describe_model_relation_scenes_async(
        self,
        request: aiops_20200806_models.DescribeModelRelationScenesRequest,
    ) -> aiops_20200806_models.DescribeModelRelationScenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_model_relation_scenes_with_options_async(request, runtime)

    def describe_product_risk_pie_with_options(
        self,
        request: aiops_20200806_models.DescribeProductRiskPieRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeProductRiskPieResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductRiskPie',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeProductRiskPieResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_risk_pie_with_options_async(
        self,
        request: aiops_20200806_models.DescribeProductRiskPieRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeProductRiskPieResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductRiskPie',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeProductRiskPieResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_risk_pie(
        self,
        request: aiops_20200806_models.DescribeProductRiskPieRequest,
    ) -> aiops_20200806_models.DescribeProductRiskPieResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_product_risk_pie_with_options(request, runtime)

    async def describe_product_risk_pie_async(
        self,
        request: aiops_20200806_models.DescribeProductRiskPieRequest,
    ) -> aiops_20200806_models.DescribeProductRiskPieResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_risk_pie_with_options_async(request, runtime)

    def describe_report_data_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeReportDataResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeReportData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_report_data_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeReportDataResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeReportData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_report_data(self) -> aiops_20200806_models.DescribeReportDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_report_data_with_options(runtime)

    async def describe_report_data_async(self) -> aiops_20200806_models.DescribeReportDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_report_data_with_options_async(runtime)

    def describe_report_email_configs_with_options(
        self,
        request: aiops_20200806_models.DescribeReportEmailConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeReportEmailConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReportEmailConfigs',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportEmailConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_report_email_configs_with_options_async(
        self,
        request: aiops_20200806_models.DescribeReportEmailConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeReportEmailConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReportEmailConfigs',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportEmailConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_report_email_configs(
        self,
        request: aiops_20200806_models.DescribeReportEmailConfigsRequest,
    ) -> aiops_20200806_models.DescribeReportEmailConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_report_email_configs_with_options(request, runtime)

    async def describe_report_email_configs_async(
        self,
        request: aiops_20200806_models.DescribeReportEmailConfigsRequest,
    ) -> aiops_20200806_models.DescribeReportEmailConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_report_email_configs_with_options_async(request, runtime)

    def describe_report_subscriptions_with_options(
        self,
        request: aiops_20200806_models.DescribeReportSubscriptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeReportSubscriptionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReportSubscriptions',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_report_subscriptions_with_options_async(
        self,
        request: aiops_20200806_models.DescribeReportSubscriptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeReportSubscriptionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReportSubscriptions',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportSubscriptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_report_subscriptions(
        self,
        request: aiops_20200806_models.DescribeReportSubscriptionsRequest,
    ) -> aiops_20200806_models.DescribeReportSubscriptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_report_subscriptions_with_options(request, runtime)

    async def describe_report_subscriptions_async(
        self,
        request: aiops_20200806_models.DescribeReportSubscriptionsRequest,
    ) -> aiops_20200806_models.DescribeReportSubscriptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_report_subscriptions_with_options_async(request, runtime)

    def describe_resource_metric_with_options(
        self,
        request: aiops_20200806_models.DescribeResourceMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeResourceMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.first_load):
            query['FirstLoad'] = request.first_load
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeResourceMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_metric_with_options_async(
        self,
        request: aiops_20200806_models.DescribeResourceMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeResourceMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.first_load):
            query['FirstLoad'] = request.first_load
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeResourceMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_metric(
        self,
        request: aiops_20200806_models.DescribeResourceMetricRequest,
    ) -> aiops_20200806_models.DescribeResourceMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_metric_with_options(request, runtime)

    async def describe_resource_metric_async(
        self,
        request: aiops_20200806_models.DescribeResourceMetricRequest,
    ) -> aiops_20200806_models.DescribeResourceMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_metric_with_options_async(request, runtime)

    def describe_risk_with_options(
        self,
        request: aiops_20200806_models.DescribeRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_with_options_async(
        self,
        request: aiops_20200806_models.DescribeRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk(
        self,
        request: aiops_20200806_models.DescribeRiskRequest,
    ) -> aiops_20200806_models.DescribeRiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_with_options(request, runtime)

    async def describe_risk_async(
        self,
        request: aiops_20200806_models.DescribeRiskRequest,
    ) -> aiops_20200806_models.DescribeRiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_with_options_async(request, runtime)

    def describe_risk_config_with_options(
        self,
        request: aiops_20200806_models.DescribeRiskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_config_with_options_async(
        self,
        request: aiops_20200806_models.DescribeRiskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_config(
        self,
        request: aiops_20200806_models.DescribeRiskConfigRequest,
    ) -> aiops_20200806_models.DescribeRiskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_config_with_options(request, runtime)

    async def describe_risk_config_async(
        self,
        request: aiops_20200806_models.DescribeRiskConfigRequest,
    ) -> aiops_20200806_models.DescribeRiskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_config_with_options_async(request, runtime)

    def describe_risk_event_details_with_options(
        self,
        request: aiops_20200806_models.DescribeRiskEventDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskEventDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_details_with_options_async(
        self,
        request: aiops_20200806_models.DescribeRiskEventDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskEventDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_details(
        self,
        request: aiops_20200806_models.DescribeRiskEventDetailsRequest,
    ) -> aiops_20200806_models.DescribeRiskEventDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_details_with_options(request, runtime)

    async def describe_risk_event_details_async(
        self,
        request: aiops_20200806_models.DescribeRiskEventDetailsRequest,
    ) -> aiops_20200806_models.DescribeRiskEventDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_event_details_with_options_async(request, runtime)

    def describe_risk_event_list_with_options(
        self,
        request: aiops_20200806_models.DescribeRiskEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_list_with_options_async(
        self,
        request: aiops_20200806_models.DescribeRiskEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_list(
        self,
        request: aiops_20200806_models.DescribeRiskEventListRequest,
    ) -> aiops_20200806_models.DescribeRiskEventListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_list_with_options(request, runtime)

    async def describe_risk_event_list_async(
        self,
        request: aiops_20200806_models.DescribeRiskEventListRequest,
    ) -> aiops_20200806_models.DescribeRiskEventListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_event_list_with_options_async(request, runtime)

    def describe_risk_event_topology_with_options(
        self,
        request: aiops_20200806_models.DescribeRiskEventTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskEventTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventTopology',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_topology_with_options_async(
        self,
        request: aiops_20200806_models.DescribeRiskEventTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskEventTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventTopology',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_topology(
        self,
        request: aiops_20200806_models.DescribeRiskEventTopologyRequest,
    ) -> aiops_20200806_models.DescribeRiskEventTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_topology_with_options(request, runtime)

    async def describe_risk_event_topology_async(
        self,
        request: aiops_20200806_models.DescribeRiskEventTopologyRequest,
    ) -> aiops_20200806_models.DescribeRiskEventTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_event_topology_with_options_async(request, runtime)

    def describe_risk_result_severity_summary_with_options(
        self,
        request: aiops_20200806_models.DescribeRiskResultSeveritySummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskResultSeveritySummaryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskResultSeveritySummary',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResultSeveritySummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_result_severity_summary_with_options_async(
        self,
        request: aiops_20200806_models.DescribeRiskResultSeveritySummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskResultSeveritySummaryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskResultSeveritySummary',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResultSeveritySummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_result_severity_summary(
        self,
        request: aiops_20200806_models.DescribeRiskResultSeveritySummaryRequest,
    ) -> aiops_20200806_models.DescribeRiskResultSeveritySummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_result_severity_summary_with_options(request, runtime)

    async def describe_risk_result_severity_summary_async(
        self,
        request: aiops_20200806_models.DescribeRiskResultSeveritySummaryRequest,
    ) -> aiops_20200806_models.DescribeRiskResultSeveritySummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_result_severity_summary_with_options_async(request, runtime)

    def describe_risk_result_statistical_with_options(
        self,
        request: aiops_20200806_models.DescribeRiskResultStatisticalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskResultStatisticalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskResultStatistical',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResultStatisticalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_result_statistical_with_options_async(
        self,
        request: aiops_20200806_models.DescribeRiskResultStatisticalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeRiskResultStatisticalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskResultStatistical',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResultStatisticalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_result_statistical(
        self,
        request: aiops_20200806_models.DescribeRiskResultStatisticalRequest,
    ) -> aiops_20200806_models.DescribeRiskResultStatisticalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_result_statistical_with_options(request, runtime)

    async def describe_risk_result_statistical_async(
        self,
        request: aiops_20200806_models.DescribeRiskResultStatisticalRequest,
    ) -> aiops_20200806_models.DescribeRiskResultStatisticalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_result_statistical_with_options_async(request, runtime)

    def describe_scene_detail_with_options(
        self,
        request: aiops_20200806_models.DescribeSceneDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_detail_with_options_async(
        self,
        request: aiops_20200806_models.DescribeSceneDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_detail(
        self,
        request: aiops_20200806_models.DescribeSceneDetailRequest,
    ) -> aiops_20200806_models.DescribeSceneDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_detail_with_options(request, runtime)

    async def describe_scene_detail_async(
        self,
        request: aiops_20200806_models.DescribeSceneDetailRequest,
    ) -> aiops_20200806_models.DescribeSceneDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_detail_with_options_async(request, runtime)

    def describe_scene_model_by_type_with_options(
        self,
        request: aiops_20200806_models.DescribeSceneModelByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneModelByTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelByType',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_model_by_type_with_options_async(
        self,
        request: aiops_20200806_models.DescribeSceneModelByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneModelByTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelByType',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelByTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_model_by_type(
        self,
        request: aiops_20200806_models.DescribeSceneModelByTypeRequest,
    ) -> aiops_20200806_models.DescribeSceneModelByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_model_by_type_with_options(request, runtime)

    async def describe_scene_model_by_type_async(
        self,
        request: aiops_20200806_models.DescribeSceneModelByTypeRequest,
    ) -> aiops_20200806_models.DescribeSceneModelByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_model_by_type_with_options_async(request, runtime)

    def describe_scene_model_detail_with_options(
        self,
        request: aiops_20200806_models.DescribeSceneModelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneModelDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_model_detail_with_options_async(
        self,
        request: aiops_20200806_models.DescribeSceneModelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneModelDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_model_detail(
        self,
        request: aiops_20200806_models.DescribeSceneModelDetailRequest,
    ) -> aiops_20200806_models.DescribeSceneModelDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_model_detail_with_options(request, runtime)

    async def describe_scene_model_detail_async(
        self,
        request: aiops_20200806_models.DescribeSceneModelDetailRequest,
    ) -> aiops_20200806_models.DescribeSceneModelDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_model_detail_with_options_async(request, runtime)

    def describe_scene_model_version_history_with_options(
        self,
        request: aiops_20200806_models.DescribeSceneModelVersionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneModelVersionHistoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelVersionHistory',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelVersionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_model_version_history_with_options_async(
        self,
        request: aiops_20200806_models.DescribeSceneModelVersionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneModelVersionHistoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelVersionHistory',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelVersionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_model_version_history(
        self,
        request: aiops_20200806_models.DescribeSceneModelVersionHistoryRequest,
    ) -> aiops_20200806_models.DescribeSceneModelVersionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_model_version_history_with_options(request, runtime)

    async def describe_scene_model_version_history_async(
        self,
        request: aiops_20200806_models.DescribeSceneModelVersionHistoryRequest,
    ) -> aiops_20200806_models.DescribeSceneModelVersionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_model_version_history_with_options_async(request, runtime)

    def describe_scene_models_with_options(
        self,
        request: aiops_20200806_models.DescribeSceneModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneModelsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_status):
            body['ApplyStatus'] = request.apply_status
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModels',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_models_with_options_async(
        self,
        request: aiops_20200806_models.DescribeSceneModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneModelsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_status):
            body['ApplyStatus'] = request.apply_status
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModels',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_models(
        self,
        request: aiops_20200806_models.DescribeSceneModelsRequest,
    ) -> aiops_20200806_models.DescribeSceneModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_models_with_options(request, runtime)

    async def describe_scene_models_async(
        self,
        request: aiops_20200806_models.DescribeSceneModelsRequest,
    ) -> aiops_20200806_models.DescribeSceneModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_models_with_options_async(request, runtime)

    def describe_scene_system_model_with_options(
        self,
        request: aiops_20200806_models.DescribeSceneSystemModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneSystemModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_status):
            body['ModelStatus'] = request.model_status
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type_id):
            body['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneSystemModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneSystemModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_system_model_with_options_async(
        self,
        request: aiops_20200806_models.DescribeSceneSystemModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeSceneSystemModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_status):
            body['ModelStatus'] = request.model_status
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type_id):
            body['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneSystemModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneSystemModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_system_model(
        self,
        request: aiops_20200806_models.DescribeSceneSystemModelRequest,
    ) -> aiops_20200806_models.DescribeSceneSystemModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_system_model_with_options(request, runtime)

    async def describe_scene_system_model_async(
        self,
        request: aiops_20200806_models.DescribeSceneSystemModelRequest,
    ) -> aiops_20200806_models.DescribeSceneSystemModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_system_model_with_options_async(request, runtime)

    def describe_scenes_with_options(
        self,
        request: aiops_20200806_models.DescribeScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeScenesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_status):
            body['SceneStatus'] = request.scene_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeScenes',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scenes_with_options_async(
        self,
        request: aiops_20200806_models.DescribeScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeScenesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_status):
            body['SceneStatus'] = request.scene_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeScenes',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scenes(
        self,
        request: aiops_20200806_models.DescribeScenesRequest,
    ) -> aiops_20200806_models.DescribeScenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scenes_with_options(request, runtime)

    async def describe_scenes_async(
        self,
        request: aiops_20200806_models.DescribeScenesRequest,
    ) -> aiops_20200806_models.DescribeScenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scenes_with_options_async(request, runtime)

    def describe_statistical_data_by_product_with_options(
        self,
        request: aiops_20200806_models.DescribeStatisticalDataByProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeStatisticalDataByProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalDataByProduct',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeStatisticalDataByProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_statistical_data_by_product_with_options_async(
        self,
        request: aiops_20200806_models.DescribeStatisticalDataByProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeStatisticalDataByProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalDataByProduct',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeStatisticalDataByProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_statistical_data_by_product(
        self,
        request: aiops_20200806_models.DescribeStatisticalDataByProductRequest,
    ) -> aiops_20200806_models.DescribeStatisticalDataByProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_statistical_data_by_product_with_options(request, runtime)

    async def describe_statistical_data_by_product_async(
        self,
        request: aiops_20200806_models.DescribeStatisticalDataByProductRequest,
    ) -> aiops_20200806_models.DescribeStatisticalDataByProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_statistical_data_by_product_with_options_async(request, runtime)

    def describe_statistical_data_by_risk_code_with_options(
        self,
        request: aiops_20200806_models.DescribeStatisticalDataByRiskCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeStatisticalDataByRiskCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalDataByRiskCode',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeStatisticalDataByRiskCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_statistical_data_by_risk_code_with_options_async(
        self,
        request: aiops_20200806_models.DescribeStatisticalDataByRiskCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeStatisticalDataByRiskCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalDataByRiskCode',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeStatisticalDataByRiskCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_statistical_data_by_risk_code(
        self,
        request: aiops_20200806_models.DescribeStatisticalDataByRiskCodeRequest,
    ) -> aiops_20200806_models.DescribeStatisticalDataByRiskCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_statistical_data_by_risk_code_with_options(request, runtime)

    async def describe_statistical_data_by_risk_code_async(
        self,
        request: aiops_20200806_models.DescribeStatisticalDataByRiskCodeRequest,
    ) -> aiops_20200806_models.DescribeStatisticalDataByRiskCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_statistical_data_by_risk_code_with_options_async(request, runtime)

    def describe_whitelist_resources_with_options(
        self,
        request: aiops_20200806_models.DescribeWhitelistResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeWhitelistResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWhitelistResources',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeWhitelistResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_whitelist_resources_with_options_async(
        self,
        request: aiops_20200806_models.DescribeWhitelistResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.DescribeWhitelistResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWhitelistResources',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeWhitelistResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_whitelist_resources(
        self,
        request: aiops_20200806_models.DescribeWhitelistResourcesRequest,
    ) -> aiops_20200806_models.DescribeWhitelistResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_resources_with_options(request, runtime)

    async def describe_whitelist_resources_async(
        self,
        request: aiops_20200806_models.DescribeWhitelistResourcesRequest,
    ) -> aiops_20200806_models.DescribeWhitelistResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_whitelist_resources_with_options_async(request, runtime)

    def end_script_list_with_options(
        self,
        request: aiops_20200806_models.EndScriptListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.EndScriptListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.EndScriptListResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_script_list_with_options_async(
        self,
        request: aiops_20200806_models.EndScriptListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.EndScriptListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.EndScriptListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_script_list(
        self,
        request: aiops_20200806_models.EndScriptListRequest,
    ) -> aiops_20200806_models.EndScriptListResponse:
        runtime = util_models.RuntimeOptions()
        return self.end_script_list_with_options(request, runtime)

    async def end_script_list_async(
        self,
        request: aiops_20200806_models.EndScriptListRequest,
    ) -> aiops_20200806_models.EndScriptListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.end_script_list_with_options_async(request, runtime)

    def feedback_alert_algorithm_with_options(
        self,
        request: aiops_20200806_models.FeedbackAlertAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.FeedbackAlertAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.algorithm_accurate_describe):
            query['AlgorithmAccurateDescribe'] = request.algorithm_accurate_describe
        if not UtilClient.is_unset(request.algorithm_accurate_state):
            query['AlgorithmAccurateState'] = request.algorithm_accurate_state
        if not UtilClient.is_unset(request.feedback_type):
            query['FeedbackType'] = request.feedback_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FeedbackAlertAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.FeedbackAlertAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_alert_algorithm_with_options_async(
        self,
        request: aiops_20200806_models.FeedbackAlertAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.FeedbackAlertAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.algorithm_accurate_describe):
            query['AlgorithmAccurateDescribe'] = request.algorithm_accurate_describe
        if not UtilClient.is_unset(request.algorithm_accurate_state):
            query['AlgorithmAccurateState'] = request.algorithm_accurate_state
        if not UtilClient.is_unset(request.feedback_type):
            query['FeedbackType'] = request.feedback_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FeedbackAlertAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.FeedbackAlertAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback_alert_algorithm(
        self,
        request: aiops_20200806_models.FeedbackAlertAlgorithmRequest,
    ) -> aiops_20200806_models.FeedbackAlertAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.feedback_alert_algorithm_with_options(request, runtime)

    async def feedback_alert_algorithm_async(
        self,
        request: aiops_20200806_models.FeedbackAlertAlgorithmRequest,
    ) -> aiops_20200806_models.FeedbackAlertAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.feedback_alert_algorithm_with_options_async(request, runtime)

    def get_aiops_event_list_with_options(
        self,
        request: aiops_20200806_models.GetAiopsEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAiopsEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.event_unique_id):
            query['EventUniqueId'] = request.event_unique_id
        if not UtilClient.is_unset(request.feedback_status):
            query['FeedbackStatus'] = request.feedback_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prediction_state):
            query['PredictionState'] = request.prediction_state
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiopsEventList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAiopsEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiops_event_list_with_options_async(
        self,
        request: aiops_20200806_models.GetAiopsEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAiopsEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.event_unique_id):
            query['EventUniqueId'] = request.event_unique_id
        if not UtilClient.is_unset(request.feedback_status):
            query['FeedbackStatus'] = request.feedback_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prediction_state):
            query['PredictionState'] = request.prediction_state
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiopsEventList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAiopsEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiops_event_list(
        self,
        request: aiops_20200806_models.GetAiopsEventListRequest,
    ) -> aiops_20200806_models.GetAiopsEventListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aiops_event_list_with_options(request, runtime)

    async def get_aiops_event_list_async(
        self,
        request: aiops_20200806_models.GetAiopsEventListRequest,
    ) -> aiops_20200806_models.GetAiopsEventListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aiops_event_list_with_options_async(request, runtime)

    def get_aiops_event_new_list_with_options(
        self,
        request: aiops_20200806_models.GetAiopsEventNewListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAiopsEventNewListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiopsEventNewList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAiopsEventNewListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiops_event_new_list_with_options_async(
        self,
        request: aiops_20200806_models.GetAiopsEventNewListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAiopsEventNewListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiopsEventNewList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAiopsEventNewListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiops_event_new_list(
        self,
        request: aiops_20200806_models.GetAiopsEventNewListRequest,
    ) -> aiops_20200806_models.GetAiopsEventNewListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aiops_event_new_list_with_options(request, runtime)

    async def get_aiops_event_new_list_async(
        self,
        request: aiops_20200806_models.GetAiopsEventNewListRequest,
    ) -> aiops_20200806_models.GetAiopsEventNewListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aiops_event_new_list_with_options_async(request, runtime)

    def get_alert_detail_trend_data_with_options(
        self,
        request: aiops_20200806_models.GetAlertDetailTrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlertDetailTrendDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.abnormal_id):
            query['AbnormalId'] = request.abnormal_id
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertDetailTrendDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_detail_trend_data_with_options_async(
        self,
        request: aiops_20200806_models.GetAlertDetailTrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlertDetailTrendDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.abnormal_id):
            query['AbnormalId'] = request.abnormal_id
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertDetailTrendDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_detail_trend_data(
        self,
        request: aiops_20200806_models.GetAlertDetailTrendDataRequest,
    ) -> aiops_20200806_models.GetAlertDetailTrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_alert_detail_trend_data_with_options(request, runtime)

    async def get_alert_detail_trend_data_async(
        self,
        request: aiops_20200806_models.GetAlertDetailTrendDataRequest,
    ) -> aiops_20200806_models.GetAlertDetailTrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_alert_detail_trend_data_with_options_async(request, runtime)

    def get_alert_list_with_options(
        self,
        request: aiops_20200806_models.GetAlertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlertListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_list_with_options_async(
        self,
        request: aiops_20200806_models.GetAlertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlertListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_list(
        self,
        request: aiops_20200806_models.GetAlertListRequest,
    ) -> aiops_20200806_models.GetAlertListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_alert_list_with_options(request, runtime)

    async def get_alert_list_async(
        self,
        request: aiops_20200806_models.GetAlertListRequest,
    ) -> aiops_20200806_models.GetAlertListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_alert_list_with_options_async(request, runtime)

    def get_alert_trent_with_options(
        self,
        request: aiops_20200806_models.GetAlertTrentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlertTrentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertTrentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_trent_with_options_async(
        self,
        request: aiops_20200806_models.GetAlertTrentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlertTrentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertTrentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_trent(
        self,
        request: aiops_20200806_models.GetAlertTrentRequest,
    ) -> aiops_20200806_models.GetAlertTrentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_alert_trent_with_options(request, runtime)

    async def get_alert_trent_async(
        self,
        request: aiops_20200806_models.GetAlertTrentRequest,
    ) -> aiops_20200806_models.GetAlertTrentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_alert_trent_with_options_async(request, runtime)

    def get_algorithm_with_options(
        self,
        request: aiops_20200806_models.GetAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expand_information):
            query['ExpandInformation'] = request.expand_information
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_with_options_async(
        self,
        request: aiops_20200806_models.GetAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expand_information):
            query['ExpandInformation'] = request.expand_information
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm(
        self,
        request: aiops_20200806_models.GetAlgorithmRequest,
    ) -> aiops_20200806_models.GetAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_with_options(request, runtime)

    async def get_algorithm_async(
        self,
        request: aiops_20200806_models.GetAlgorithmRequest,
    ) -> aiops_20200806_models.GetAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_with_options_async(request, runtime)

    def get_algorithm_config_with_options(
        self,
        request: aiops_20200806_models.GetAlgorithmConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_type_code):
            query['AlgorithmTypeCode'] = request.algorithm_type_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_config_with_options_async(
        self,
        request: aiops_20200806_models.GetAlgorithmConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_type_code):
            query['AlgorithmTypeCode'] = request.algorithm_type_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm_config(
        self,
        request: aiops_20200806_models.GetAlgorithmConfigRequest,
    ) -> aiops_20200806_models.GetAlgorithmConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_config_with_options(request, runtime)

    async def get_algorithm_config_async(
        self,
        request: aiops_20200806_models.GetAlgorithmConfigRequest,
    ) -> aiops_20200806_models.GetAlgorithmConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_config_with_options_async(request, runtime)

    def get_algorithm_data_with_options(
        self,
        request: aiops_20200806_models.GetAlgorithmDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_data_with_options_async(
        self,
        request: aiops_20200806_models.GetAlgorithmDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm_data(
        self,
        request: aiops_20200806_models.GetAlgorithmDataRequest,
    ) -> aiops_20200806_models.GetAlgorithmDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_data_with_options(request, runtime)

    async def get_algorithm_data_async(
        self,
        request: aiops_20200806_models.GetAlgorithmDataRequest,
    ) -> aiops_20200806_models.GetAlgorithmDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_data_with_options_async(request, runtime)

    def get_algorithm_details_with_options(
        self,
        request: aiops_20200806_models.GetAlgorithmDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_details_with_options_async(
        self,
        request: aiops_20200806_models.GetAlgorithmDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm_details(
        self,
        request: aiops_20200806_models.GetAlgorithmDetailsRequest,
    ) -> aiops_20200806_models.GetAlgorithmDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_details_with_options(request, runtime)

    async def get_algorithm_details_async(
        self,
        request: aiops_20200806_models.GetAlgorithmDetailsRequest,
    ) -> aiops_20200806_models.GetAlgorithmDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_details_with_options_async(request, runtime)

    def get_algorithm_forecast_data_with_options(
        self,
        request: aiops_20200806_models.GetAlgorithmForecastDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmForecastDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmForecastData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmForecastDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_forecast_data_with_options_async(
        self,
        request: aiops_20200806_models.GetAlgorithmForecastDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmForecastDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmForecastData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmForecastDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm_forecast_data(
        self,
        request: aiops_20200806_models.GetAlgorithmForecastDataRequest,
    ) -> aiops_20200806_models.GetAlgorithmForecastDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_forecast_data_with_options(request, runtime)

    async def get_algorithm_forecast_data_async(
        self,
        request: aiops_20200806_models.GetAlgorithmForecastDataRequest,
    ) -> aiops_20200806_models.GetAlgorithmForecastDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_forecast_data_with_options_async(request, runtime)

    def get_algorithm_forecast_details_with_options(
        self,
        request: aiops_20200806_models.GetAlgorithmForecastDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmForecastDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmForecastDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmForecastDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_forecast_details_with_options_async(
        self,
        request: aiops_20200806_models.GetAlgorithmForecastDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmForecastDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmForecastDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmForecastDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm_forecast_details(
        self,
        request: aiops_20200806_models.GetAlgorithmForecastDetailsRequest,
    ) -> aiops_20200806_models.GetAlgorithmForecastDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_forecast_details_with_options(request, runtime)

    async def get_algorithm_forecast_details_async(
        self,
        request: aiops_20200806_models.GetAlgorithmForecastDetailsRequest,
    ) -> aiops_20200806_models.GetAlgorithmForecastDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_forecast_details_with_options_async(request, runtime)

    def get_algorithm_list_with_options(
        self,
        request: aiops_20200806_models.GetAlgorithmListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_list_with_options_async(
        self,
        request: aiops_20200806_models.GetAlgorithmListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAlgorithmListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm_list(
        self,
        request: aiops_20200806_models.GetAlgorithmListRequest,
    ) -> aiops_20200806_models.GetAlgorithmListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_list_with_options(request, runtime)

    async def get_algorithm_list_async(
        self,
        request: aiops_20200806_models.GetAlgorithmListRequest,
    ) -> aiops_20200806_models.GetAlgorithmListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_list_with_options_async(request, runtime)

    def get_all_algorithm_config_with_options(
        self,
        request: aiops_20200806_models.GetAllAlgorithmConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAllAlgorithmConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllAlgorithmConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAllAlgorithmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_algorithm_config_with_options_async(
        self,
        request: aiops_20200806_models.GetAllAlgorithmConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAllAlgorithmConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllAlgorithmConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAllAlgorithmConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_algorithm_config(
        self,
        request: aiops_20200806_models.GetAllAlgorithmConfigRequest,
    ) -> aiops_20200806_models.GetAllAlgorithmConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_algorithm_config_with_options(request, runtime)

    async def get_all_algorithm_config_async(
        self,
        request: aiops_20200806_models.GetAllAlgorithmConfigRequest,
    ) -> aiops_20200806_models.GetAllAlgorithmConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_algorithm_config_with_options_async(request, runtime)

    def get_all_tag_resource_num_list_with_options(
        self,
        request: aiops_20200806_models.GetAllTagResourceNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAllTagResourceNumListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllTagResourceNumList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAllTagResourceNumListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_tag_resource_num_list_with_options_async(
        self,
        request: aiops_20200806_models.GetAllTagResourceNumListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAllTagResourceNumListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllTagResourceNumList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAllTagResourceNumListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_tag_resource_num_list(
        self,
        request: aiops_20200806_models.GetAllTagResourceNumListRequest,
    ) -> aiops_20200806_models.GetAllTagResourceNumListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_tag_resource_num_list_with_options(request, runtime)

    async def get_all_tag_resource_num_list_async(
        self,
        request: aiops_20200806_models.GetAllTagResourceNumListRequest,
    ) -> aiops_20200806_models.GetAllTagResourceNumListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_tag_resource_num_list_with_options_async(request, runtime)

    def get_analysis_process_with_options(
        self,
        request: aiops_20200806_models.GetAnalysisProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAnalysisProcessResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnalysisProcess',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAnalysisProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_analysis_process_with_options_async(
        self,
        request: aiops_20200806_models.GetAnalysisProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAnalysisProcessResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnalysisProcess',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAnalysisProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_analysis_process(
        self,
        request: aiops_20200806_models.GetAnalysisProcessRequest,
    ) -> aiops_20200806_models.GetAnalysisProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_analysis_process_with_options(request, runtime)

    async def get_analysis_process_async(
        self,
        request: aiops_20200806_models.GetAnalysisProcessRequest,
    ) -> aiops_20200806_models.GetAnalysisProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_analysis_process_with_options_async(request, runtime)

    def get_authorization_with_options(
        self,
        request: aiops_20200806_models.GetAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_authorization_with_options_async(
        self,
        request: aiops_20200806_models.GetAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_authorization(
        self,
        request: aiops_20200806_models.GetAuthorizationRequest,
    ) -> aiops_20200806_models.GetAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_with_options(request, runtime)

    async def get_authorization_async(
        self,
        request: aiops_20200806_models.GetAuthorizationRequest,
    ) -> aiops_20200806_models.GetAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_authorization_with_options_async(request, runtime)

    def get_avg_repair_time_with_options(
        self,
        request: aiops_20200806_models.GetAvgRepairTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAvgRepairTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAvgRepairTime',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAvgRepairTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_avg_repair_time_with_options_async(
        self,
        request: aiops_20200806_models.GetAvgRepairTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetAvgRepairTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAvgRepairTime',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAvgRepairTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_avg_repair_time(
        self,
        request: aiops_20200806_models.GetAvgRepairTimeRequest,
    ) -> aiops_20200806_models.GetAvgRepairTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_avg_repair_time_with_options(request, runtime)

    async def get_avg_repair_time_async(
        self,
        request: aiops_20200806_models.GetAvgRepairTimeRequest,
    ) -> aiops_20200806_models.GetAvgRepairTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_avg_repair_time_with_options_async(request, runtime)

    def get_back_script_list_with_options(
        self,
        request: aiops_20200806_models.GetBackScriptListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBackScriptListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBackScriptListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_back_script_list_with_options_async(
        self,
        request: aiops_20200806_models.GetBackScriptListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBackScriptListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBackScriptListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_back_script_list(
        self,
        request: aiops_20200806_models.GetBackScriptListRequest,
    ) -> aiops_20200806_models.GetBackScriptListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_back_script_list_with_options(request, runtime)

    async def get_back_script_list_async(
        self,
        request: aiops_20200806_models.GetBackScriptListRequest,
    ) -> aiops_20200806_models.GetBackScriptListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_back_script_list_with_options_async(request, runtime)

    def get_business_group_with_options(
        self,
        request: aiops_20200806_models.GetBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_group_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_group(
        self,
        request: aiops_20200806_models.GetBusinessGroupRequest,
    ) -> aiops_20200806_models.GetBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_with_options(request, runtime)

    async def get_business_group_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupRequest,
    ) -> aiops_20200806_models.GetBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_group_with_options_async(request, runtime)

    def get_business_group_all_with_options(
        self,
        request: aiops_20200806_models.GetBusinessGroupAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_group_all_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_group_all(
        self,
        request: aiops_20200806_models.GetBusinessGroupAllRequest,
    ) -> aiops_20200806_models.GetBusinessGroupAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_all_with_options(request, runtime)

    async def get_business_group_all_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupAllRequest,
    ) -> aiops_20200806_models.GetBusinessGroupAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_group_all_with_options_async(request, runtime)

    def get_business_group_index_with_options(
        self,
        request: aiops_20200806_models.GetBusinessGroupIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupIndexResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupIndex',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_group_index_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupIndexResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupIndex',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_group_index(
        self,
        request: aiops_20200806_models.GetBusinessGroupIndexRequest,
    ) -> aiops_20200806_models.GetBusinessGroupIndexResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_index_with_options(request, runtime)

    async def get_business_group_index_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupIndexRequest,
    ) -> aiops_20200806_models.GetBusinessGroupIndexResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_group_index_with_options_async(request, runtime)

    def get_business_group_info_with_options(
        self,
        request: aiops_20200806_models.GetBusinessGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_group_info_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_group_info(
        self,
        request: aiops_20200806_models.GetBusinessGroupInfoRequest,
    ) -> aiops_20200806_models.GetBusinessGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_info_with_options(request, runtime)

    async def get_business_group_info_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupInfoRequest,
    ) -> aiops_20200806_models.GetBusinessGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_group_info_with_options_async(request, runtime)

    def get_business_group_overview_list_with_options(
        self,
        request: aiops_20200806_models.GetBusinessGroupOverviewListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupOverviewListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupOverviewList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupOverviewListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_group_overview_list_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupOverviewListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessGroupOverviewListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupOverviewList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupOverviewListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_group_overview_list(
        self,
        request: aiops_20200806_models.GetBusinessGroupOverviewListRequest,
    ) -> aiops_20200806_models.GetBusinessGroupOverviewListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_overview_list_with_options(request, runtime)

    async def get_business_group_overview_list_async(
        self,
        request: aiops_20200806_models.GetBusinessGroupOverviewListRequest,
    ) -> aiops_20200806_models.GetBusinessGroupOverviewListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_group_overview_list_with_options_async(request, runtime)

    def get_business_log_alert_detail_with_options(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessLogAlertDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_log_alert_detail_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessLogAlertDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_log_alert_detail(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertDetailRequest,
    ) -> aiops_20200806_models.GetBusinessLogAlertDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_log_alert_detail_with_options(request, runtime)

    async def get_business_log_alert_detail_async(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertDetailRequest,
    ) -> aiops_20200806_models.GetBusinessLogAlertDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_log_alert_detail_with_options_async(request, runtime)

    def get_business_log_alert_list_with_options(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessLogAlertListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_log_alert_list_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessLogAlertListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_log_alert_list(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertListRequest,
    ) -> aiops_20200806_models.GetBusinessLogAlertListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_log_alert_list_with_options(request, runtime)

    async def get_business_log_alert_list_async(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertListRequest,
    ) -> aiops_20200806_models.GetBusinessLogAlertListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_log_alert_list_with_options_async(request, runtime)

    def get_business_log_alert_top_nwith_options(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessLogAlertTopNResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertTopN',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_log_alert_top_nwith_options_async(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessLogAlertTopNResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertTopN',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_log_alert_top_n(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertTopNRequest,
    ) -> aiops_20200806_models.GetBusinessLogAlertTopNResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_log_alert_top_nwith_options(request, runtime)

    async def get_business_log_alert_top_n_async(
        self,
        request: aiops_20200806_models.GetBusinessLogAlertTopNRequest,
    ) -> aiops_20200806_models.GetBusinessLogAlertTopNResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_log_alert_top_nwith_options_async(request, runtime)

    def get_business_metric_alert_detail_list_with_options(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricAlertDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_metric_alert_detail_list_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricAlertDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_metric_alert_detail_list(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertDetailListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricAlertDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_alert_detail_list_with_options(request, runtime)

    async def get_business_metric_alert_detail_list_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertDetailListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricAlertDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_metric_alert_detail_list_with_options_async(request, runtime)

    def get_business_metric_alert_list_with_options(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricAlertListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_metric_alert_list_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricAlertListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_metric_alert_list(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricAlertListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_alert_list_with_options(request, runtime)

    async def get_business_metric_alert_list_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricAlertListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_metric_alert_list_with_options_async(request, runtime)

    def get_business_metric_alert_top_nwith_options(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricAlertTopNResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertTopN',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_metric_alert_top_nwith_options_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricAlertTopNResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertTopN',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_metric_alert_top_n(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertTopNRequest,
    ) -> aiops_20200806_models.GetBusinessMetricAlertTopNResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_alert_top_nwith_options(request, runtime)

    async def get_business_metric_alert_top_n_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricAlertTopNRequest,
    ) -> aiops_20200806_models.GetBusinessMetricAlertTopNResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_metric_alert_top_nwith_options_async(request, runtime)

    def get_business_metric_all_list_with_options(
        self,
        request: aiops_20200806_models.GetBusinessMetricAllListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricAllListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAllList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAllListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_metric_all_list_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricAllListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricAllListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAllList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAllListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_metric_all_list(
        self,
        request: aiops_20200806_models.GetBusinessMetricAllListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricAllListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_all_list_with_options(request, runtime)

    async def get_business_metric_all_list_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricAllListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricAllListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_metric_all_list_with_options_async(request, runtime)

    def get_business_metric_forecast_list_with_options(
        self,
        request: aiops_20200806_models.GetBusinessMetricForecastListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricForecastListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricForecastList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricForecastListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_metric_forecast_list_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricForecastListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricForecastListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricForecastList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricForecastListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_metric_forecast_list(
        self,
        request: aiops_20200806_models.GetBusinessMetricForecastListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricForecastListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_forecast_list_with_options(request, runtime)

    async def get_business_metric_forecast_list_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricForecastListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricForecastListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_metric_forecast_list_with_options_async(request, runtime)

    def get_business_metric_resource_by_metric_id_with_options(
        self,
        request: aiops_20200806_models.GetBusinessMetricResourceByMetricIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricResourceByMetricIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricResourceByMetricId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricResourceByMetricIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_metric_resource_by_metric_id_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricResourceByMetricIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricResourceByMetricIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricResourceByMetricId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricResourceByMetricIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_metric_resource_by_metric_id(
        self,
        request: aiops_20200806_models.GetBusinessMetricResourceByMetricIdRequest,
    ) -> aiops_20200806_models.GetBusinessMetricResourceByMetricIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_resource_by_metric_id_with_options(request, runtime)

    async def get_business_metric_resource_by_metric_id_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricResourceByMetricIdRequest,
    ) -> aiops_20200806_models.GetBusinessMetricResourceByMetricIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_metric_resource_by_metric_id_with_options_async(request, runtime)

    def get_business_metric_scene_list_with_options(
        self,
        request: aiops_20200806_models.GetBusinessMetricSceneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricSceneListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_metric_scene_list_with_options_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricSceneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetBusinessMetricSceneListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_metric_scene_list(
        self,
        request: aiops_20200806_models.GetBusinessMetricSceneListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricSceneListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_scene_list_with_options(request, runtime)

    async def get_business_metric_scene_list_async(
        self,
        request: aiops_20200806_models.GetBusinessMetricSceneListRequest,
    ) -> aiops_20200806_models.GetBusinessMetricSceneListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_metric_scene_list_with_options_async(request, runtime)

    def get_cid_info_with_options(
        self,
        request: aiops_20200806_models.GetCidInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetCidInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCidInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCidInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cid_info_with_options_async(
        self,
        request: aiops_20200806_models.GetCidInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetCidInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCidInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCidInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cid_info(
        self,
        request: aiops_20200806_models.GetCidInfoRequest,
    ) -> aiops_20200806_models.GetCidInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cid_info_with_options(request, runtime)

    async def get_cid_info_async(
        self,
        request: aiops_20200806_models.GetCidInfoRequest,
    ) -> aiops_20200806_models.GetCidInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cid_info_with_options_async(request, runtime)

    def get_cloud_all_resource_list_with_options(
        self,
        request: aiops_20200806_models.GetCloudAllResourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetCloudAllResourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudAllResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudAllResourceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_all_resource_list_with_options_async(
        self,
        request: aiops_20200806_models.GetCloudAllResourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetCloudAllResourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudAllResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudAllResourceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_all_resource_list(
        self,
        request: aiops_20200806_models.GetCloudAllResourceListRequest,
    ) -> aiops_20200806_models.GetCloudAllResourceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_all_resource_list_with_options(request, runtime)

    async def get_cloud_all_resource_list_async(
        self,
        request: aiops_20200806_models.GetCloudAllResourceListRequest,
    ) -> aiops_20200806_models.GetCloudAllResourceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_all_resource_list_with_options_async(request, runtime)

    def get_cloud_resource_with_options(
        self,
        request: aiops_20200806_models.GetCloudResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetCloudResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_resource_with_options_async(
        self,
        request: aiops_20200806_models.GetCloudResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetCloudResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_resource(
        self,
        request: aiops_20200806_models.GetCloudResourceRequest,
    ) -> aiops_20200806_models.GetCloudResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_resource_with_options(request, runtime)

    async def get_cloud_resource_async(
        self,
        request: aiops_20200806_models.GetCloudResourceRequest,
    ) -> aiops_20200806_models.GetCloudResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_resource_with_options_async(request, runtime)

    def get_cloud_resource_list_with_options(
        self,
        request: aiops_20200806_models.GetCloudResourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetCloudResourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_region_id):
            query['CloudRegionId'] = request.cloud_region_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_optional):
            query['IsOptional'] = request.is_optional
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.release_status):
            query['ReleaseStatus'] = request.release_status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudResourceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_resource_list_with_options_async(
        self,
        request: aiops_20200806_models.GetCloudResourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetCloudResourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_region_id):
            query['CloudRegionId'] = request.cloud_region_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_optional):
            query['IsOptional'] = request.is_optional
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.release_status):
            query['ReleaseStatus'] = request.release_status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudResourceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_resource_list(
        self,
        request: aiops_20200806_models.GetCloudResourceListRequest,
    ) -> aiops_20200806_models.GetCloudResourceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_resource_list_with_options(request, runtime)

    async def get_cloud_resource_list_async(
        self,
        request: aiops_20200806_models.GetCloudResourceListRequest,
    ) -> aiops_20200806_models.GetCloudResourceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_resource_list_with_options_async(request, runtime)

    def get_connect_instances_with_options(
        self,
        request: aiops_20200806_models.GetConnectInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetConnectInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectInstances',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetConnectInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connect_instances_with_options_async(
        self,
        request: aiops_20200806_models.GetConnectInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetConnectInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectInstances',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetConnectInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connect_instances(
        self,
        request: aiops_20200806_models.GetConnectInstancesRequest,
    ) -> aiops_20200806_models.GetConnectInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_connect_instances_with_options(request, runtime)

    async def get_connect_instances_async(
        self,
        request: aiops_20200806_models.GetConnectInstancesRequest,
    ) -> aiops_20200806_models.GetConnectInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_connect_instances_with_options_async(request, runtime)

    def get_data_source_detail_with_options(
        self,
        request: aiops_20200806_models.GetDataSourceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDataSourceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_detail_with_options_async(
        self,
        request: aiops_20200806_models.GetDataSourceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDataSourceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_detail(
        self,
        request: aiops_20200806_models.GetDataSourceDetailRequest,
    ) -> aiops_20200806_models.GetDataSourceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_detail_with_options(request, runtime)

    async def get_data_source_detail_async(
        self,
        request: aiops_20200806_models.GetDataSourceDetailRequest,
    ) -> aiops_20200806_models.GetDataSourceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_source_detail_with_options_async(request, runtime)

    def get_data_source_list_with_options(
        self,
        request: aiops_20200806_models.GetDataSourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDataSourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_list_with_options_async(
        self,
        request: aiops_20200806_models.GetDataSourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDataSourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_list(
        self,
        request: aiops_20200806_models.GetDataSourceListRequest,
    ) -> aiops_20200806_models.GetDataSourceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_list_with_options(request, runtime)

    async def get_data_source_list_async(
        self,
        request: aiops_20200806_models.GetDataSourceListRequest,
    ) -> aiops_20200806_models.GetDataSourceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_source_list_with_options_async(request, runtime)

    def get_data_source_target_param_list_with_options(
        self,
        request: aiops_20200806_models.GetDataSourceTargetParamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDataSourceTargetParamListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceTargetParamList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceTargetParamListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_target_param_list_with_options_async(
        self,
        request: aiops_20200806_models.GetDataSourceTargetParamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDataSourceTargetParamListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceTargetParamList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceTargetParamListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_target_param_list(
        self,
        request: aiops_20200806_models.GetDataSourceTargetParamListRequest,
    ) -> aiops_20200806_models.GetDataSourceTargetParamListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_target_param_list_with_options(request, runtime)

    async def get_data_source_target_param_list_async(
        self,
        request: aiops_20200806_models.GetDataSourceTargetParamListRequest,
    ) -> aiops_20200806_models.GetDataSourceTargetParamListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_source_target_param_list_with_options_async(request, runtime)

    def get_data_volume_with_options(
        self,
        request: aiops_20200806_models.GetDataVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDataVolumeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataVolume',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_volume_with_options_async(
        self,
        request: aiops_20200806_models.GetDataVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDataVolumeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataVolume',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_volume(
        self,
        request: aiops_20200806_models.GetDataVolumeRequest,
    ) -> aiops_20200806_models.GetDataVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_volume_with_options(request, runtime)

    async def get_data_volume_async(
        self,
        request: aiops_20200806_models.GetDataVolumeRequest,
    ) -> aiops_20200806_models.GetDataVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_volume_with_options_async(request, runtime)

    def get_diag_info_with_options(
        self,
        request: aiops_20200806_models.GetDiagInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDiagInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.diagnostic_id):
            query['DiagnosticId'] = request.diagnostic_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDiagInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diag_info_with_options_async(
        self,
        request: aiops_20200806_models.GetDiagInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDiagInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.diagnostic_id):
            query['DiagnosticId'] = request.diagnostic_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDiagInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diag_info(
        self,
        request: aiops_20200806_models.GetDiagInfoRequest,
    ) -> aiops_20200806_models.GetDiagInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_diag_info_with_options(request, runtime)

    async def get_diag_info_async(
        self,
        request: aiops_20200806_models.GetDiagInfoRequest,
    ) -> aiops_20200806_models.GetDiagInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_diag_info_with_options_async(request, runtime)

    def get_domain_config_with_options(
        self,
        request: aiops_20200806_models.GetDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_config_with_options_async(
        self,
        request: aiops_20200806_models.GetDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_config(
        self,
        request: aiops_20200806_models.GetDomainConfigRequest,
    ) -> aiops_20200806_models.GetDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_config_with_options(request, runtime)

    async def get_domain_config_async(
        self,
        request: aiops_20200806_models.GetDomainConfigRequest,
    ) -> aiops_20200806_models.GetDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_config_with_options_async(request, runtime)

    def get_event_ab_normal_detail_with_options(
        self,
        request: aiops_20200806_models.GetEventAbNormalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventAbNormalDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_ab_normal_detail_with_options_async(
        self,
        request: aiops_20200806_models.GetEventAbNormalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventAbNormalDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_ab_normal_detail(
        self,
        request: aiops_20200806_models.GetEventAbNormalDetailRequest,
    ) -> aiops_20200806_models.GetEventAbNormalDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_ab_normal_detail_with_options(request, runtime)

    async def get_event_ab_normal_detail_async(
        self,
        request: aiops_20200806_models.GetEventAbNormalDetailRequest,
    ) -> aiops_20200806_models.GetEventAbNormalDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_ab_normal_detail_with_options_async(request, runtime)

    def get_event_ab_normal_detail_trend_data_with_options(
        self,
        request: aiops_20200806_models.GetEventAbNormalDetailTrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventAbNormalDetailTrendDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalDetailTrendDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_ab_normal_detail_trend_data_with_options_async(
        self,
        request: aiops_20200806_models.GetEventAbNormalDetailTrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventAbNormalDetailTrendDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalDetailTrendDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_ab_normal_detail_trend_data(
        self,
        request: aiops_20200806_models.GetEventAbNormalDetailTrendDataRequest,
    ) -> aiops_20200806_models.GetEventAbNormalDetailTrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_ab_normal_detail_trend_data_with_options(request, runtime)

    async def get_event_ab_normal_detail_trend_data_async(
        self,
        request: aiops_20200806_models.GetEventAbNormalDetailTrendDataRequest,
    ) -> aiops_20200806_models.GetEventAbNormalDetailTrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_ab_normal_detail_trend_data_with_options_async(request, runtime)

    def get_event_ab_normal_list_with_options(
        self,
        request: aiops_20200806_models.GetEventAbNormalListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventAbNormalListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_ab_normal_list_with_options_async(
        self,
        request: aiops_20200806_models.GetEventAbNormalListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventAbNormalListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_ab_normal_list(
        self,
        request: aiops_20200806_models.GetEventAbNormalListRequest,
    ) -> aiops_20200806_models.GetEventAbNormalListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_ab_normal_list_with_options(request, runtime)

    async def get_event_ab_normal_list_async(
        self,
        request: aiops_20200806_models.GetEventAbNormalListRequest,
    ) -> aiops_20200806_models.GetEventAbNormalListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_ab_normal_list_with_options_async(request, runtime)

    def get_event_business_metric_list_with_options(
        self,
        request: aiops_20200806_models.GetEventBusinessMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventBusinessMetricListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventBusinessMetricList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventBusinessMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_business_metric_list_with_options_async(
        self,
        request: aiops_20200806_models.GetEventBusinessMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventBusinessMetricListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventBusinessMetricList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventBusinessMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_business_metric_list(
        self,
        request: aiops_20200806_models.GetEventBusinessMetricListRequest,
    ) -> aiops_20200806_models.GetEventBusinessMetricListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_business_metric_list_with_options(request, runtime)

    async def get_event_business_metric_list_async(
        self,
        request: aiops_20200806_models.GetEventBusinessMetricListRequest,
    ) -> aiops_20200806_models.GetEventBusinessMetricListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_business_metric_list_with_options_async(request, runtime)

    def get_event_detail_with_options(
        self,
        request: aiops_20200806_models.GetEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_detail_with_options_async(
        self,
        request: aiops_20200806_models.GetEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_detail(
        self,
        request: aiops_20200806_models.GetEventDetailRequest,
    ) -> aiops_20200806_models.GetEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_detail_with_options(request, runtime)

    async def get_event_detail_async(
        self,
        request: aiops_20200806_models.GetEventDetailRequest,
    ) -> aiops_20200806_models.GetEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_detail_with_options_async(request, runtime)

    def get_event_root_cause_with_options(
        self,
        request: aiops_20200806_models.GetEventRootCauseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventRootCauseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventRootCauseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_root_cause_with_options_async(
        self,
        request: aiops_20200806_models.GetEventRootCauseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventRootCauseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventRootCauseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_root_cause(
        self,
        request: aiops_20200806_models.GetEventRootCauseRequest,
    ) -> aiops_20200806_models.GetEventRootCauseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_root_cause_with_options(request, runtime)

    async def get_event_root_cause_async(
        self,
        request: aiops_20200806_models.GetEventRootCauseRequest,
    ) -> aiops_20200806_models.GetEventRootCauseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_root_cause_with_options_async(request, runtime)

    def get_event_sequential_trent_with_options(
        self,
        request: aiops_20200806_models.GetEventSequentialTrentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventSequentialTrentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventSequentialTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventSequentialTrentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_sequential_trent_with_options_async(
        self,
        request: aiops_20200806_models.GetEventSequentialTrentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventSequentialTrentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventSequentialTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventSequentialTrentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_sequential_trent(
        self,
        request: aiops_20200806_models.GetEventSequentialTrentRequest,
    ) -> aiops_20200806_models.GetEventSequentialTrentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_sequential_trent_with_options(request, runtime)

    async def get_event_sequential_trent_async(
        self,
        request: aiops_20200806_models.GetEventSequentialTrentRequest,
    ) -> aiops_20200806_models.GetEventSequentialTrentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_sequential_trent_with_options_async(request, runtime)

    def get_event_statistics_with_options(
        self,
        request: aiops_20200806_models.GetEventStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_statistics_with_options_async(
        self,
        request: aiops_20200806_models.GetEventStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_statistics(
        self,
        request: aiops_20200806_models.GetEventStatisticsRequest,
    ) -> aiops_20200806_models.GetEventStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_statistics_with_options(request, runtime)

    async def get_event_statistics_async(
        self,
        request: aiops_20200806_models.GetEventStatisticsRequest,
    ) -> aiops_20200806_models.GetEventStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_statistics_with_options_async(request, runtime)

    def get_event_trent_with_options(
        self,
        request: aiops_20200806_models.GetEventTrentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventTrentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity_type):
            query['GranularityType'] = request.granularity_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_type):
            query['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventTrentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_trent_with_options_async(
        self,
        request: aiops_20200806_models.GetEventTrentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventTrentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity_type):
            query['GranularityType'] = request.granularity_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_type):
            query['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventTrentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_trent(
        self,
        request: aiops_20200806_models.GetEventTrentRequest,
    ) -> aiops_20200806_models.GetEventTrentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_trent_with_options(request, runtime)

    async def get_event_trent_async(
        self,
        request: aiops_20200806_models.GetEventTrentRequest,
    ) -> aiops_20200806_models.GetEventTrentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_trent_with_options_async(request, runtime)

    def get_event_type_with_options(
        self,
        request: aiops_20200806_models.GetEventTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventType',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_type_with_options_async(
        self,
        request: aiops_20200806_models.GetEventTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetEventTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventType',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_type(
        self,
        request: aiops_20200806_models.GetEventTypeRequest,
    ) -> aiops_20200806_models.GetEventTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_type_with_options(request, runtime)

    async def get_event_type_async(
        self,
        request: aiops_20200806_models.GetEventTypeRequest,
    ) -> aiops_20200806_models.GetEventTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_type_with_options_async(request, runtime)

    def get_exceptions_with_options(
        self,
        request: aiops_20200806_models.GetExceptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetExceptionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExceptions',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetExceptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_exceptions_with_options_async(
        self,
        request: aiops_20200806_models.GetExceptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetExceptionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExceptions',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetExceptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_exceptions(
        self,
        request: aiops_20200806_models.GetExceptionsRequest,
    ) -> aiops_20200806_models.GetExceptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_exceptions_with_options(request, runtime)

    async def get_exceptions_async(
        self,
        request: aiops_20200806_models.GetExceptionsRequest,
    ) -> aiops_20200806_models.GetExceptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_exceptions_with_options_async(request, runtime)

    def get_extend_with_options(
        self,
        request: aiops_20200806_models.GetExtendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetExtendResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExtend',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetExtendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_extend_with_options_async(
        self,
        request: aiops_20200806_models.GetExtendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetExtendResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExtend',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetExtendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_extend(
        self,
        request: aiops_20200806_models.GetExtendRequest,
    ) -> aiops_20200806_models.GetExtendResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_extend_with_options(request, runtime)

    async def get_extend_async(
        self,
        request: aiops_20200806_models.GetExtendRequest,
    ) -> aiops_20200806_models.GetExtendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_extend_with_options_async(request, runtime)

    def get_forecast_business_metric_with_options(
        self,
        request: aiops_20200806_models.GetForecastBusinessMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetForecastBusinessMetricResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetForecastBusinessMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetForecastBusinessMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_forecast_business_metric_with_options_async(
        self,
        request: aiops_20200806_models.GetForecastBusinessMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetForecastBusinessMetricResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetForecastBusinessMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetForecastBusinessMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_forecast_business_metric(
        self,
        request: aiops_20200806_models.GetForecastBusinessMetricRequest,
    ) -> aiops_20200806_models.GetForecastBusinessMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_forecast_business_metric_with_options(request, runtime)

    async def get_forecast_business_metric_async(
        self,
        request: aiops_20200806_models.GetForecastBusinessMetricRequest,
    ) -> aiops_20200806_models.GetForecastBusinessMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_forecast_business_metric_with_options_async(request, runtime)

    def get_function_valid_info_with_options(
        self,
        request: aiops_20200806_models.GetFunctionValidInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetFunctionValidInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.function_name):
            body['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFunctionValidInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetFunctionValidInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_valid_info_with_options_async(
        self,
        request: aiops_20200806_models.GetFunctionValidInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetFunctionValidInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.function_name):
            body['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFunctionValidInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetFunctionValidInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_valid_info(
        self,
        request: aiops_20200806_models.GetFunctionValidInfoRequest,
    ) -> aiops_20200806_models.GetFunctionValidInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_function_valid_info_with_options(request, runtime)

    async def get_function_valid_info_async(
        self,
        request: aiops_20200806_models.GetFunctionValidInfoRequest,
    ) -> aiops_20200806_models.GetFunctionValidInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_function_valid_info_with_options_async(request, runtime)

    def get_group_by_dimension_data_with_options(
        self,
        request: aiops_20200806_models.GetGroupByDimensionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetGroupByDimensionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupByDimensionData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupByDimensionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_by_dimension_data_with_options_async(
        self,
        request: aiops_20200806_models.GetGroupByDimensionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetGroupByDimensionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupByDimensionData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupByDimensionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_by_dimension_data(
        self,
        request: aiops_20200806_models.GetGroupByDimensionDataRequest,
    ) -> aiops_20200806_models.GetGroupByDimensionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_by_dimension_data_with_options(request, runtime)

    async def get_group_by_dimension_data_async(
        self,
        request: aiops_20200806_models.GetGroupByDimensionDataRequest,
    ) -> aiops_20200806_models.GetGroupByDimensionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_by_dimension_data_with_options_async(request, runtime)

    def get_group_resource_num_with_options(
        self,
        request: aiops_20200806_models.GetGroupResourceNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetGroupResourceNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupResourceNum',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupResourceNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_resource_num_with_options_async(
        self,
        request: aiops_20200806_models.GetGroupResourceNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetGroupResourceNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupResourceNum',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupResourceNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_resource_num(
        self,
        request: aiops_20200806_models.GetGroupResourceNumRequest,
    ) -> aiops_20200806_models.GetGroupResourceNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_resource_num_with_options(request, runtime)

    async def get_group_resource_num_async(
        self,
        request: aiops_20200806_models.GetGroupResourceNumRequest,
    ) -> aiops_20200806_models.GetGroupResourceNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_resource_num_with_options_async(request, runtime)

    def get_group_topology_tag_with_options(
        self,
        request: aiops_20200806_models.GetGroupTopologyTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetGroupTopologyTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupTopologyTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupTopologyTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_topology_tag_with_options_async(
        self,
        request: aiops_20200806_models.GetGroupTopologyTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetGroupTopologyTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupTopologyTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupTopologyTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_topology_tag(
        self,
        request: aiops_20200806_models.GetGroupTopologyTagRequest,
    ) -> aiops_20200806_models.GetGroupTopologyTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_topology_tag_with_options(request, runtime)

    async def get_group_topology_tag_async(
        self,
        request: aiops_20200806_models.GetGroupTopologyTagRequest,
    ) -> aiops_20200806_models.GetGroupTopologyTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_topology_tag_with_options_async(request, runtime)

    def get_incident_all_with_options(
        self,
        request: aiops_20200806_models.GetIncidentAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetIncidentAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIncidentAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIncidentAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_incident_all_with_options_async(
        self,
        request: aiops_20200806_models.GetIncidentAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetIncidentAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIncidentAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIncidentAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_incident_all(
        self,
        request: aiops_20200806_models.GetIncidentAllRequest,
    ) -> aiops_20200806_models.GetIncidentAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_incident_all_with_options(request, runtime)

    async def get_incident_all_async(
        self,
        request: aiops_20200806_models.GetIncidentAllRequest,
    ) -> aiops_20200806_models.GetIncidentAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_incident_all_with_options_async(request, runtime)

    def get_index_dialysis_array_with_options(
        self,
        request: aiops_20200806_models.GetIndexDialysisArrayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetIndexDialysisArrayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisArray',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisArrayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_dialysis_array_with_options_async(
        self,
        request: aiops_20200806_models.GetIndexDialysisArrayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetIndexDialysisArrayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisArray',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisArrayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_dialysis_array(
        self,
        request: aiops_20200806_models.GetIndexDialysisArrayRequest,
    ) -> aiops_20200806_models.GetIndexDialysisArrayResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_index_dialysis_array_with_options(request, runtime)

    async def get_index_dialysis_array_async(
        self,
        request: aiops_20200806_models.GetIndexDialysisArrayRequest,
    ) -> aiops_20200806_models.GetIndexDialysisArrayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_index_dialysis_array_with_options_async(request, runtime)

    def get_index_dialysis_list_with_options(
        self,
        request: aiops_20200806_models.GetIndexDialysisListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetIndexDialysisListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_dialysis_list_with_options_async(
        self,
        request: aiops_20200806_models.GetIndexDialysisListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetIndexDialysisListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_dialysis_list(
        self,
        request: aiops_20200806_models.GetIndexDialysisListRequest,
    ) -> aiops_20200806_models.GetIndexDialysisListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_index_dialysis_list_with_options(request, runtime)

    async def get_index_dialysis_list_async(
        self,
        request: aiops_20200806_models.GetIndexDialysisListRequest,
    ) -> aiops_20200806_models.GetIndexDialysisListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_index_dialysis_list_with_options_async(request, runtime)

    def get_index_dialysis_list_line_with_options(
        self,
        request: aiops_20200806_models.GetIndexDialysisListLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetIndexDialysisListLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.metric_extend):
            query['MetricExtend'] = request.metric_extend
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisListLine',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisListLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_dialysis_list_line_with_options_async(
        self,
        request: aiops_20200806_models.GetIndexDialysisListLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetIndexDialysisListLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.metric_extend):
            query['MetricExtend'] = request.metric_extend
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisListLine',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisListLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_dialysis_list_line(
        self,
        request: aiops_20200806_models.GetIndexDialysisListLineRequest,
    ) -> aiops_20200806_models.GetIndexDialysisListLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_index_dialysis_list_line_with_options(request, runtime)

    async def get_index_dialysis_list_line_async(
        self,
        request: aiops_20200806_models.GetIndexDialysisListLineRequest,
    ) -> aiops_20200806_models.GetIndexDialysisListLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_index_dialysis_list_line_with_options_async(request, runtime)

    def get_inspection_report_download_url_with_options(
        self,
        request: aiops_20200806_models.GetInspectionReportDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetInspectionReportDownloadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.download_report_list_json):
            body['DownloadReportListJson'] = request.download_report_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInspectionReportDownloadUrl',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetInspectionReportDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inspection_report_download_url_with_options_async(
        self,
        request: aiops_20200806_models.GetInspectionReportDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetInspectionReportDownloadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.download_report_list_json):
            body['DownloadReportListJson'] = request.download_report_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInspectionReportDownloadUrl',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetInspectionReportDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inspection_report_download_url(
        self,
        request: aiops_20200806_models.GetInspectionReportDownloadUrlRequest,
    ) -> aiops_20200806_models.GetInspectionReportDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_inspection_report_download_url_with_options(request, runtime)

    async def get_inspection_report_download_url_async(
        self,
        request: aiops_20200806_models.GetInspectionReportDownloadUrlRequest,
    ) -> aiops_20200806_models.GetInspectionReportDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_inspection_report_download_url_with_options_async(request, runtime)

    def get_instances_num_with_options(
        self,
        request: aiops_20200806_models.GetInstancesNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetInstancesNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstancesNum',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetInstancesNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instances_num_with_options_async(
        self,
        request: aiops_20200806_models.GetInstancesNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetInstancesNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstancesNum',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetInstancesNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instances_num(
        self,
        request: aiops_20200806_models.GetInstancesNumRequest,
    ) -> aiops_20200806_models.GetInstancesNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instances_num_with_options(request, runtime)

    async def get_instances_num_async(
        self,
        request: aiops_20200806_models.GetInstancesNumRequest,
    ) -> aiops_20200806_models.GetInstancesNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instances_num_with_options_async(request, runtime)

    def get_log_sample_with_options(
        self,
        request: aiops_20200806_models.GetLogSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetLogSampleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_field):
            query['AppField'] = request.app_field
        if not UtilClient.is_unset(request.app_value):
            query['AppValue'] = request.app_value
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.log_field):
            query['LogField'] = request.log_field
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogSample',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetLogSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_sample_with_options_async(
        self,
        request: aiops_20200806_models.GetLogSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetLogSampleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_field):
            query['AppField'] = request.app_field
        if not UtilClient.is_unset(request.app_value):
            query['AppValue'] = request.app_value
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.log_field):
            query['LogField'] = request.log_field
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogSample',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetLogSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_sample(
        self,
        request: aiops_20200806_models.GetLogSampleRequest,
    ) -> aiops_20200806_models.GetLogSampleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_sample_with_options(request, runtime)

    async def get_log_sample_async(
        self,
        request: aiops_20200806_models.GetLogSampleRequest,
    ) -> aiops_20200806_models.GetLogSampleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_sample_with_options_async(request, runtime)

    def get_log_sample_column_with_options(
        self,
        request: aiops_20200806_models.GetLogSampleColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetLogSampleColumnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogSampleColumn',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetLogSampleColumnResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_sample_column_with_options_async(
        self,
        request: aiops_20200806_models.GetLogSampleColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetLogSampleColumnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogSampleColumn',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetLogSampleColumnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_sample_column(
        self,
        request: aiops_20200806_models.GetLogSampleColumnRequest,
    ) -> aiops_20200806_models.GetLogSampleColumnResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_log_sample_column_with_options(request, runtime)

    async def get_log_sample_column_async(
        self,
        request: aiops_20200806_models.GetLogSampleColumnRequest,
    ) -> aiops_20200806_models.GetLogSampleColumnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_log_sample_column_with_options_async(request, runtime)

    def get_metric_event_sequential_trent_with_options(
        self,
        request: aiops_20200806_models.GetMetricEventSequentialTrentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetMetricEventSequentialTrentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetricEventSequentialTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetMetricEventSequentialTrentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_metric_event_sequential_trent_with_options_async(
        self,
        request: aiops_20200806_models.GetMetricEventSequentialTrentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetMetricEventSequentialTrentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetricEventSequentialTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetMetricEventSequentialTrentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_metric_event_sequential_trent(
        self,
        request: aiops_20200806_models.GetMetricEventSequentialTrentRequest,
    ) -> aiops_20200806_models.GetMetricEventSequentialTrentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_metric_event_sequential_trent_with_options(request, runtime)

    async def get_metric_event_sequential_trent_async(
        self,
        request: aiops_20200806_models.GetMetricEventSequentialTrentRequest,
    ) -> aiops_20200806_models.GetMetricEventSequentialTrentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_metric_event_sequential_trent_with_options_async(request, runtime)

    def get_new_optimization_item_data_with_options(
        self,
        request: aiops_20200806_models.GetNewOptimizationItemDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetNewOptimizationItemDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNewOptimizationItemData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetNewOptimizationItemDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_new_optimization_item_data_with_options_async(
        self,
        request: aiops_20200806_models.GetNewOptimizationItemDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetNewOptimizationItemDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNewOptimizationItemData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetNewOptimizationItemDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_new_optimization_item_data(
        self,
        request: aiops_20200806_models.GetNewOptimizationItemDataRequest,
    ) -> aiops_20200806_models.GetNewOptimizationItemDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_new_optimization_item_data_with_options(request, runtime)

    async def get_new_optimization_item_data_async(
        self,
        request: aiops_20200806_models.GetNewOptimizationItemDataRequest,
    ) -> aiops_20200806_models.GetNewOptimizationItemDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_new_optimization_item_data_with_options_async(request, runtime)

    def get_patrol_inspection_detail_list_with_options(
        self,
        request: aiops_20200806_models.GetPatrolInspectionDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionDetailListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_patrol_inspection_detail_list_with_options_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionDetailListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_patrol_inspection_detail_list(
        self,
        request: aiops_20200806_models.GetPatrolInspectionDetailListRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_detail_list_with_options(request, runtime)

    async def get_patrol_inspection_detail_list_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionDetailListRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_patrol_inspection_detail_list_with_options_async(request, runtime)

    def get_patrol_inspection_detail_thrend_data_with_options(
        self,
        request: aiops_20200806_models.GetPatrolInspectionDetailThrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionDetailThrendDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.request_content):
            query['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionDetailThrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionDetailThrendDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_patrol_inspection_detail_thrend_data_with_options_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionDetailThrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionDetailThrendDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.request_content):
            query['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionDetailThrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionDetailThrendDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_patrol_inspection_detail_thrend_data(
        self,
        request: aiops_20200806_models.GetPatrolInspectionDetailThrendDataRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionDetailThrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_detail_thrend_data_with_options(request, runtime)

    async def get_patrol_inspection_detail_thrend_data_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionDetailThrendDataRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionDetailThrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_patrol_inspection_detail_thrend_data_with_options_async(request, runtime)

    def get_patrol_inspection_items_list_with_options(
        self,
        request: aiops_20200806_models.GetPatrolInspectionItemsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionItemsListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionItemsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionItemsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_patrol_inspection_items_list_with_options_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionItemsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionItemsListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionItemsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionItemsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_patrol_inspection_items_list(
        self,
        request: aiops_20200806_models.GetPatrolInspectionItemsListRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionItemsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_items_list_with_options(request, runtime)

    async def get_patrol_inspection_items_list_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionItemsListRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionItemsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_patrol_inspection_items_list_with_options_async(request, runtime)

    def get_patrol_inspection_list_with_options(
        self,
        request: aiops_20200806_models.GetPatrolInspectionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_patrol_inspection_list_with_options_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_patrol_inspection_list(
        self,
        request: aiops_20200806_models.GetPatrolInspectionListRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_list_with_options(request, runtime)

    async def get_patrol_inspection_list_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionListRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_patrol_inspection_list_with_options_async(request, runtime)

    def get_patrol_inspection_status_with_options(
        self,
        request: aiops_20200806_models.GetPatrolInspectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_patrol_inspection_status_with_options_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetPatrolInspectionStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_patrol_inspection_status(
        self,
        request: aiops_20200806_models.GetPatrolInspectionStatusRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_status_with_options(request, runtime)

    async def get_patrol_inspection_status_async(
        self,
        request: aiops_20200806_models.GetPatrolInspectionStatusRequest,
    ) -> aiops_20200806_models.GetPatrolInspectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_patrol_inspection_status_with_options_async(request, runtime)

    def get_product_instance_with_options(
        self,
        request: aiops_20200806_models.GetProductInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetProductInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductInstance',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetProductInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_instance_with_options_async(
        self,
        request: aiops_20200806_models.GetProductInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetProductInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductInstance',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetProductInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_instance(
        self,
        request: aiops_20200806_models.GetProductInstanceRequest,
    ) -> aiops_20200806_models.GetProductInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_product_instance_with_options(request, runtime)

    async def get_product_instance_async(
        self,
        request: aiops_20200806_models.GetProductInstanceRequest,
    ) -> aiops_20200806_models.GetProductInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_product_instance_with_options_async(request, runtime)

    def get_product_metric_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetProductMetricListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetProductMetricList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetProductMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_metric_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetProductMetricListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetProductMetricList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetProductMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_metric_list(self) -> aiops_20200806_models.GetProductMetricListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_product_metric_list_with_options(runtime)

    async def get_product_metric_list_async(self) -> aiops_20200806_models.GetProductMetricListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_product_metric_list_with_options_async(runtime)

    def get_real_data_with_options(
        self,
        request: aiops_20200806_models.GetRealDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRealDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRealDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_real_data_with_options_async(
        self,
        request: aiops_20200806_models.GetRealDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRealDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRealDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_real_data(
        self,
        request: aiops_20200806_models.GetRealDataRequest,
    ) -> aiops_20200806_models.GetRealDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_real_data_with_options(request, runtime)

    async def get_real_data_async(
        self,
        request: aiops_20200806_models.GetRealDataRequest,
    ) -> aiops_20200806_models.GetRealDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_real_data_with_options_async(request, runtime)

    def get_region_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRegionListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRegionList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRegionListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRegionList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRegionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_region_list(self) -> aiops_20200806_models.GetRegionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_region_list_with_options(runtime)

    async def get_region_list_async(self) -> aiops_20200806_models.GetRegionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_region_list_with_options_async(runtime)

    def get_repair_script_with_options(
        self,
        request: aiops_20200806_models.GetRepairScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRepairScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepairScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRepairScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repair_script_with_options_async(
        self,
        request: aiops_20200806_models.GetRepairScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRepairScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepairScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRepairScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repair_script(
        self,
        request: aiops_20200806_models.GetRepairScriptRequest,
    ) -> aiops_20200806_models.GetRepairScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_repair_script_with_options(request, runtime)

    async def get_repair_script_async(
        self,
        request: aiops_20200806_models.GetRepairScriptRequest,
    ) -> aiops_20200806_models.GetRepairScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_repair_script_with_options_async(request, runtime)

    def get_resource_list_with_options(
        self,
        request: aiops_20200806_models.GetResourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetResourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_list_with_options_async(
        self,
        request: aiops_20200806_models.GetResourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetResourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_list(
        self,
        request: aiops_20200806_models.GetResourceListRequest,
    ) -> aiops_20200806_models.GetResourceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_list_with_options(request, runtime)

    async def get_resource_list_async(
        self,
        request: aiops_20200806_models.GetResourceListRequest,
    ) -> aiops_20200806_models.GetResourceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_list_with_options_async(request, runtime)

    def get_resource_tag_drop_list_with_options(
        self,
        request: aiops_20200806_models.GetResourceTagDropListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetResourceTagDropListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTagDropList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceTagDropListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_tag_drop_list_with_options_async(
        self,
        request: aiops_20200806_models.GetResourceTagDropListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetResourceTagDropListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTagDropList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceTagDropListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_tag_drop_list(
        self,
        request: aiops_20200806_models.GetResourceTagDropListRequest,
    ) -> aiops_20200806_models.GetResourceTagDropListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_tag_drop_list_with_options(request, runtime)

    async def get_resource_tag_drop_list_async(
        self,
        request: aiops_20200806_models.GetResourceTagDropListRequest,
    ) -> aiops_20200806_models.GetResourceTagDropListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_tag_drop_list_with_options_async(request, runtime)

    def get_resource_type_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetResourceTypeListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceTypeList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetResourceTypeListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceTypeList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceTypeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type_list(self) -> aiops_20200806_models.GetResourceTypeListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_list_with_options(runtime)

    async def get_resource_type_list_async(self) -> aiops_20200806_models.GetResourceTypeListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_type_list_with_options_async(runtime)

    def get_risk_in_all_with_options(
        self,
        request: aiops_20200806_models.GetRiskInAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskInAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.screen):
            query['Screen'] = request.screen
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_in_all_with_options_async(
        self,
        request: aiops_20200806_models.GetRiskInAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskInAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.screen):
            query['Screen'] = request.screen
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_in_all(
        self,
        request: aiops_20200806_models.GetRiskInAllRequest,
    ) -> aiops_20200806_models.GetRiskInAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_in_all_with_options(request, runtime)

    async def get_risk_in_all_async(
        self,
        request: aiops_20200806_models.GetRiskInAllRequest,
    ) -> aiops_20200806_models.GetRiskInAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_in_all_with_options_async(request, runtime)

    def get_risk_inspect_statistics_with_options(
        self,
        request: aiops_20200806_models.GetRiskInspectStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskInspectStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInspectStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInspectStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_inspect_statistics_with_options_async(
        self,
        request: aiops_20200806_models.GetRiskInspectStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskInspectStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInspectStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInspectStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_inspect_statistics(
        self,
        request: aiops_20200806_models.GetRiskInspectStatisticsRequest,
    ) -> aiops_20200806_models.GetRiskInspectStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_inspect_statistics_with_options(request, runtime)

    async def get_risk_inspect_statistics_async(
        self,
        request: aiops_20200806_models.GetRiskInspectStatisticsRequest,
    ) -> aiops_20200806_models.GetRiskInspectStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_inspect_statistics_with_options_async(request, runtime)

    def get_risk_inspection_type_list_with_options(
        self,
        request: aiops_20200806_models.GetRiskInspectionTypeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskInspectionTypeListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInspectionTypeList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInspectionTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_inspection_type_list_with_options_async(
        self,
        request: aiops_20200806_models.GetRiskInspectionTypeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskInspectionTypeListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInspectionTypeList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInspectionTypeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_inspection_type_list(
        self,
        request: aiops_20200806_models.GetRiskInspectionTypeListRequest,
    ) -> aiops_20200806_models.GetRiskInspectionTypeListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_inspection_type_list_with_options(request, runtime)

    async def get_risk_inspection_type_list_async(
        self,
        request: aiops_20200806_models.GetRiskInspectionTypeListRequest,
    ) -> aiops_20200806_models.GetRiskInspectionTypeListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_inspection_type_list_with_options_async(request, runtime)

    def get_risk_patrol_detail_list_with_options(
        self,
        request: aiops_20200806_models.GetRiskPatrolDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolDetailListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_patrol_detail_list_with_options_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolDetailListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_patrol_detail_list(
        self,
        request: aiops_20200806_models.GetRiskPatrolDetailListRequest,
    ) -> aiops_20200806_models.GetRiskPatrolDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_detail_list_with_options(request, runtime)

    async def get_risk_patrol_detail_list_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolDetailListRequest,
    ) -> aiops_20200806_models.GetRiskPatrolDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_patrol_detail_list_with_options_async(request, runtime)

    def get_risk_patrol_list_with_options(
        self,
        request: aiops_20200806_models.GetRiskPatrolListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.patrol_id):
            query['PatrolId'] = request.patrol_id
        if not UtilClient.is_unset(request.risk_patrol_item):
            query['RiskPatrolItem'] = request.risk_patrol_item
        if not UtilClient.is_unset(request.severity_level):
            query['SeverityLevel'] = request.severity_level
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_patrol_list_with_options_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.patrol_id):
            query['PatrolId'] = request.patrol_id
        if not UtilClient.is_unset(request.risk_patrol_item):
            query['RiskPatrolItem'] = request.risk_patrol_item
        if not UtilClient.is_unset(request.severity_level):
            query['SeverityLevel'] = request.severity_level
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_patrol_list(
        self,
        request: aiops_20200806_models.GetRiskPatrolListRequest,
    ) -> aiops_20200806_models.GetRiskPatrolListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_list_with_options(request, runtime)

    async def get_risk_patrol_list_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolListRequest,
    ) -> aiops_20200806_models.GetRiskPatrolListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_patrol_list_with_options_async(request, runtime)

    def get_risk_patrol_statistical_trends_with_options(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatisticalTrendsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolStatisticalTrendsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatisticalTrends',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatisticalTrendsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_patrol_statistical_trends_with_options_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatisticalTrendsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolStatisticalTrendsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatisticalTrends',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatisticalTrendsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_patrol_statistical_trends(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatisticalTrendsRequest,
    ) -> aiops_20200806_models.GetRiskPatrolStatisticalTrendsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_statistical_trends_with_options(request, runtime)

    async def get_risk_patrol_statistical_trends_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatisticalTrendsRequest,
    ) -> aiops_20200806_models.GetRiskPatrolStatisticalTrendsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_patrol_statistical_trends_with_options_async(request, runtime)

    def get_risk_patrol_statistics_with_options(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_patrol_statistics_with_options_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_patrol_statistics(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatisticsRequest,
    ) -> aiops_20200806_models.GetRiskPatrolStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_statistics_with_options(request, runtime)

    async def get_risk_patrol_statistics_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatisticsRequest,
    ) -> aiops_20200806_models.GetRiskPatrolStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_patrol_statistics_with_options_async(request, runtime)

    def get_risk_patrol_status_with_options(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_patrol_status_with_options_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRiskPatrolStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_patrol_status(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatusRequest,
    ) -> aiops_20200806_models.GetRiskPatrolStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_status_with_options(request, runtime)

    async def get_risk_patrol_status_async(
        self,
        request: aiops_20200806_models.GetRiskPatrolStatusRequest,
    ) -> aiops_20200806_models.GetRiskPatrolStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_risk_patrol_status_with_options_async(request, runtime)

    def get_role_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRoleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRole',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRoleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRole',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(self) -> aiops_20200806_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_role_with_options(runtime)

    async def get_role_async(self) -> aiops_20200806_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_role_with_options_async(runtime)

    def get_root_cause_with_options(
        self,
        request: aiops_20200806_models.GetRootCauseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRootCauseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRootCauseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_root_cause_with_options_async(
        self,
        request: aiops_20200806_models.GetRootCauseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetRootCauseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRootCauseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_root_cause(
        self,
        request: aiops_20200806_models.GetRootCauseRequest,
    ) -> aiops_20200806_models.GetRootCauseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_root_cause_with_options(request, runtime)

    async def get_root_cause_async(
        self,
        request: aiops_20200806_models.GetRootCauseRequest,
    ) -> aiops_20200806_models.GetRootCauseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_root_cause_with_options_async(request, runtime)

    def get_scenario_detail_with_options(
        self,
        request: aiops_20200806_models.GetScenarioDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetScenarioDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scenario_detail_with_options_async(
        self,
        request: aiops_20200806_models.GetScenarioDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetScenarioDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scenario_detail(
        self,
        request: aiops_20200806_models.GetScenarioDetailRequest,
    ) -> aiops_20200806_models.GetScenarioDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scenario_detail_with_options(request, runtime)

    async def get_scenario_detail_async(
        self,
        request: aiops_20200806_models.GetScenarioDetailRequest,
    ) -> aiops_20200806_models.GetScenarioDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scenario_detail_with_options_async(request, runtime)

    def get_scenario_list_with_options(
        self,
        request: aiops_20200806_models.GetScenarioListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetScenarioListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scenario_name):
            query['ScenarioName'] = request.scenario_name
        if not UtilClient.is_unset(request.scene_select_label):
            query['SceneSelectLabel'] = request.scene_select_label
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scenario_list_with_options_async(
        self,
        request: aiops_20200806_models.GetScenarioListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetScenarioListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scenario_name):
            query['ScenarioName'] = request.scenario_name
        if not UtilClient.is_unset(request.scene_select_label):
            query['SceneSelectLabel'] = request.scene_select_label
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scenario_list(
        self,
        request: aiops_20200806_models.GetScenarioListRequest,
    ) -> aiops_20200806_models.GetScenarioListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scenario_list_with_options(request, runtime)

    async def get_scenario_list_async(
        self,
        request: aiops_20200806_models.GetScenarioListRequest,
    ) -> aiops_20200806_models.GetScenarioListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scenario_list_with_options_async(request, runtime)

    def get_scenario_statistics_list_with_options(
        self,
        request: aiops_20200806_models.GetScenarioStatisticsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetScenarioStatisticsListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scenario_ids):
            query['ScenarioIds'] = request.scenario_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioStatisticsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioStatisticsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scenario_statistics_list_with_options_async(
        self,
        request: aiops_20200806_models.GetScenarioStatisticsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetScenarioStatisticsListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scenario_ids):
            query['ScenarioIds'] = request.scenario_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioStatisticsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioStatisticsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scenario_statistics_list(
        self,
        request: aiops_20200806_models.GetScenarioStatisticsListRequest,
    ) -> aiops_20200806_models.GetScenarioStatisticsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scenario_statistics_list_with_options(request, runtime)

    async def get_scenario_statistics_list_async(
        self,
        request: aiops_20200806_models.GetScenarioStatisticsListRequest,
    ) -> aiops_20200806_models.GetScenarioStatisticsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scenario_statistics_list_with_options_async(request, runtime)

    def get_scene_by_id_with_options(
        self,
        request: aiops_20200806_models.GetSceneByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSceneByIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneById',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_by_id_with_options_async(
        self,
        request: aiops_20200806_models.GetSceneByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSceneByIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneById',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_by_id(
        self,
        request: aiops_20200806_models.GetSceneByIdRequest,
    ) -> aiops_20200806_models.GetSceneByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_by_id_with_options(request, runtime)

    async def get_scene_by_id_async(
        self,
        request: aiops_20200806_models.GetSceneByIdRequest,
    ) -> aiops_20200806_models.GetSceneByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_by_id_with_options_async(request, runtime)

    def get_scene_details_list_with_options(
        self,
        request: aiops_20200806_models.GetSceneDetailsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSceneDetailsListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneDetailsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneDetailsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_details_list_with_options_async(
        self,
        request: aiops_20200806_models.GetSceneDetailsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSceneDetailsListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneDetailsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneDetailsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_details_list(
        self,
        request: aiops_20200806_models.GetSceneDetailsListRequest,
    ) -> aiops_20200806_models.GetSceneDetailsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_details_list_with_options(request, runtime)

    async def get_scene_details_list_async(
        self,
        request: aiops_20200806_models.GetSceneDetailsListRequest,
    ) -> aiops_20200806_models.GetSceneDetailsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_details_list_with_options_async(request, runtime)

    def get_scene_list_with_options(
        self,
        request: aiops_20200806_models.GetSceneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSceneListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_total):
            query['PageTotal'] = request.page_total
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_list_with_options_async(
        self,
        request: aiops_20200806_models.GetSceneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSceneListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_total):
            query['PageTotal'] = request.page_total
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_list(
        self,
        request: aiops_20200806_models.GetSceneListRequest,
    ) -> aiops_20200806_models.GetSceneListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_list_with_options(request, runtime)

    async def get_scene_list_async(
        self,
        request: aiops_20200806_models.GetSceneListRequest,
    ) -> aiops_20200806_models.GetSceneListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_list_with_options_async(request, runtime)

    def get_scene_metric_table_with_options(
        self,
        request: aiops_20200806_models.GetSceneMetricTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSceneMetricTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneMetricTable',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneMetricTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_metric_table_with_options_async(
        self,
        request: aiops_20200806_models.GetSceneMetricTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSceneMetricTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneMetricTable',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneMetricTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_metric_table(
        self,
        request: aiops_20200806_models.GetSceneMetricTableRequest,
    ) -> aiops_20200806_models.GetSceneMetricTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_metric_table_with_options(request, runtime)

    async def get_scene_metric_table_async(
        self,
        request: aiops_20200806_models.GetSceneMetricTableRequest,
    ) -> aiops_20200806_models.GetSceneMetricTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_metric_table_with_options_async(request, runtime)

    def get_script_event_root_cause_with_options(
        self,
        request: aiops_20200806_models.GetScriptEventRootCauseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetScriptEventRootCauseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScriptEventRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScriptEventRootCauseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_script_event_root_cause_with_options_async(
        self,
        request: aiops_20200806_models.GetScriptEventRootCauseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetScriptEventRootCauseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScriptEventRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScriptEventRootCauseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_script_event_root_cause(
        self,
        request: aiops_20200806_models.GetScriptEventRootCauseRequest,
    ) -> aiops_20200806_models.GetScriptEventRootCauseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_script_event_root_cause_with_options(request, runtime)

    async def get_script_event_root_cause_async(
        self,
        request: aiops_20200806_models.GetScriptEventRootCauseRequest,
    ) -> aiops_20200806_models.GetScriptEventRootCauseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_script_event_root_cause_with_options_async(request, runtime)

    def get_sls_log_data_with_options(
        self,
        request: aiops_20200806_models.GetSlsLogDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSlsLogDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSlsLogData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSlsLogDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sls_log_data_with_options_async(
        self,
        request: aiops_20200806_models.GetSlsLogDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSlsLogDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSlsLogData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSlsLogDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sls_log_data(
        self,
        request: aiops_20200806_models.GetSlsLogDataRequest,
    ) -> aiops_20200806_models.GetSlsLogDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sls_log_data_with_options(request, runtime)

    async def get_sls_log_data_async(
        self,
        request: aiops_20200806_models.GetSlsLogDataRequest,
    ) -> aiops_20200806_models.GetSlsLogDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sls_log_data_with_options_async(request, runtime)

    def get_syn_cloud_resource_list_with_options(
        self,
        request: aiops_20200806_models.GetSynCloudResourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSynCloudResourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSynCloudResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSynCloudResourceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_syn_cloud_resource_list_with_options_async(
        self,
        request: aiops_20200806_models.GetSynCloudResourceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetSynCloudResourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSynCloudResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSynCloudResourceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_syn_cloud_resource_list(
        self,
        request: aiops_20200806_models.GetSynCloudResourceListRequest,
    ) -> aiops_20200806_models.GetSynCloudResourceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_syn_cloud_resource_list_with_options(request, runtime)

    async def get_syn_cloud_resource_list_async(
        self,
        request: aiops_20200806_models.GetSynCloudResourceListRequest,
    ) -> aiops_20200806_models.GetSynCloudResourceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_syn_cloud_resource_list_with_options_async(request, runtime)

    def get_tag_business_group_list_with_options(
        self,
        request: aiops_20200806_models.GetTagBusinessGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetTagBusinessGroupListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagBusinessGroupList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTagBusinessGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tag_business_group_list_with_options_async(
        self,
        request: aiops_20200806_models.GetTagBusinessGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetTagBusinessGroupListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagBusinessGroupList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTagBusinessGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tag_business_group_list(
        self,
        request: aiops_20200806_models.GetTagBusinessGroupListRequest,
    ) -> aiops_20200806_models.GetTagBusinessGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tag_business_group_list_with_options(request, runtime)

    async def get_tag_business_group_list_async(
        self,
        request: aiops_20200806_models.GetTagBusinessGroupListRequest,
    ) -> aiops_20200806_models.GetTagBusinessGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tag_business_group_list_with_options_async(request, runtime)

    def get_tag_drop_list_with_options(
        self,
        request: aiops_20200806_models.GetTagDropListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetTagDropListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagDropList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTagDropListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tag_drop_list_with_options_async(
        self,
        request: aiops_20200806_models.GetTagDropListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetTagDropListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagDropList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTagDropListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tag_drop_list(
        self,
        request: aiops_20200806_models.GetTagDropListRequest,
    ) -> aiops_20200806_models.GetTagDropListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tag_drop_list_with_options(request, runtime)

    async def get_tag_drop_list_async(
        self,
        request: aiops_20200806_models.GetTagDropListRequest,
    ) -> aiops_20200806_models.GetTagDropListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tag_drop_list_with_options_async(request, runtime)

    def get_target_dimension_data_with_options(
        self,
        request: aiops_20200806_models.GetTargetDimensionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetTargetDimensionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.label_value):
            query['LabelValue'] = request.label_value
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTargetDimensionData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTargetDimensionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_target_dimension_data_with_options_async(
        self,
        request: aiops_20200806_models.GetTargetDimensionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetTargetDimensionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.label_value):
            query['LabelValue'] = request.label_value
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTargetDimensionData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTargetDimensionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_target_dimension_data(
        self,
        request: aiops_20200806_models.GetTargetDimensionDataRequest,
    ) -> aiops_20200806_models.GetTargetDimensionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_target_dimension_data_with_options(request, runtime)

    async def get_target_dimension_data_async(
        self,
        request: aiops_20200806_models.GetTargetDimensionDataRequest,
    ) -> aiops_20200806_models.GetTargetDimensionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_target_dimension_data_with_options_async(request, runtime)

    def get_threshold_list_with_options(
        self,
        request: aiops_20200806_models.GetThresholdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetThresholdListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThresholdList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetThresholdListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_threshold_list_with_options_async(
        self,
        request: aiops_20200806_models.GetThresholdListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetThresholdListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThresholdList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetThresholdListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_threshold_list(
        self,
        request: aiops_20200806_models.GetThresholdListRequest,
    ) -> aiops_20200806_models.GetThresholdListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_threshold_list_with_options(request, runtime)

    async def get_threshold_list_async(
        self,
        request: aiops_20200806_models.GetThresholdListRequest,
    ) -> aiops_20200806_models.GetThresholdListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_threshold_list_with_options_async(request, runtime)

    def get_through_put_with_options(
        self,
        request: aiops_20200806_models.GetThroughPutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetThroughPutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThroughPut',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetThroughPutResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_through_put_with_options_async(
        self,
        request: aiops_20200806_models.GetThroughPutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetThroughPutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThroughPut',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetThroughPutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_through_put(
        self,
        request: aiops_20200806_models.GetThroughPutRequest,
    ) -> aiops_20200806_models.GetThroughPutResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_through_put_with_options(request, runtime)

    async def get_through_put_async(
        self,
        request: aiops_20200806_models.GetThroughPutRequest,
    ) -> aiops_20200806_models.GetThroughPutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_through_put_with_options_async(request, runtime)

    def get_trend_sls_reports_with_options(
        self,
        request: aiops_20200806_models.GetTrendSlsReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetTrendSlsReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrendSlsReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTrendSlsReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trend_sls_reports_with_options_async(
        self,
        request: aiops_20200806_models.GetTrendSlsReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetTrendSlsReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrendSlsReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTrendSlsReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trend_sls_reports(
        self,
        request: aiops_20200806_models.GetTrendSlsReportsRequest,
    ) -> aiops_20200806_models.GetTrendSlsReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trend_sls_reports_with_options(request, runtime)

    async def get_trend_sls_reports_async(
        self,
        request: aiops_20200806_models.GetTrendSlsReportsRequest,
    ) -> aiops_20200806_models.GetTrendSlsReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trend_sls_reports_with_options_async(request, runtime)

    def get_user_info_with_options(
        self,
        request: aiops_20200806_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        request: aiops_20200806_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_info(
        self,
        request: aiops_20200806_models.GetUserInfoRequest,
    ) -> aiops_20200806_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_info_with_options(request, runtime)

    async def get_user_info_async(
        self,
        request: aiops_20200806_models.GetUserInfoRequest,
    ) -> aiops_20200806_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_info_with_options_async(request, runtime)

    def get_user_login_info_with_options(
        self,
        request: aiops_20200806_models.GetUserLoginInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetUserLoginInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_principal_name):
            query['AccountPrincipalName'] = request.account_principal_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.current_pk):
            query['CurrentPk'] = request.current_pk
        if not UtilClient.is_unset(request.main_account_pk):
            query['MainAccountPk'] = request.main_account_pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserLoginInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserLoginInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_login_info_with_options_async(
        self,
        request: aiops_20200806_models.GetUserLoginInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetUserLoginInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_principal_name):
            query['AccountPrincipalName'] = request.account_principal_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.current_pk):
            query['CurrentPk'] = request.current_pk
        if not UtilClient.is_unset(request.main_account_pk):
            query['MainAccountPk'] = request.main_account_pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserLoginInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserLoginInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_login_info(
        self,
        request: aiops_20200806_models.GetUserLoginInfoRequest,
    ) -> aiops_20200806_models.GetUserLoginInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_login_info_with_options(request, runtime)

    async def get_user_login_info_async(
        self,
        request: aiops_20200806_models.GetUserLoginInfoRequest,
    ) -> aiops_20200806_models.GetUserLoginInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_login_info_with_options_async(request, runtime)

    def get_user_order_config_with_options(
        self,
        request: aiops_20200806_models.GetUserOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetUserOrderConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserOrderConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserOrderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_order_config_with_options_async(
        self,
        request: aiops_20200806_models.GetUserOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.GetUserOrderConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserOrderConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserOrderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_order_config(
        self,
        request: aiops_20200806_models.GetUserOrderConfigRequest,
    ) -> aiops_20200806_models.GetUserOrderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_order_config_with_options(request, runtime)

    async def get_user_order_config_async(
        self,
        request: aiops_20200806_models.GetUserOrderConfigRequest,
    ) -> aiops_20200806_models.GetUserOrderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_order_config_with_options_async(request, runtime)

    def ignore_alarms_with_options(
        self,
        request: aiops_20200806_models.IgnoreAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.IgnoreAlarmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreAlarms',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.IgnoreAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ignore_alarms_with_options_async(
        self,
        request: aiops_20200806_models.IgnoreAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.IgnoreAlarmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreAlarms',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.IgnoreAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ignore_alarms(
        self,
        request: aiops_20200806_models.IgnoreAlarmsRequest,
    ) -> aiops_20200806_models.IgnoreAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.ignore_alarms_with_options(request, runtime)

    async def ignore_alarms_async(
        self,
        request: aiops_20200806_models.IgnoreAlarmsRequest,
    ) -> aiops_20200806_models.IgnoreAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ignore_alarms_with_options_async(request, runtime)

    def list_apply_authorization_with_options(
        self,
        request: aiops_20200806_models.ListApplyAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListApplyAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplyAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListApplyAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apply_authorization_with_options_async(
        self,
        request: aiops_20200806_models.ListApplyAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListApplyAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplyAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListApplyAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apply_authorization(
        self,
        request: aiops_20200806_models.ListApplyAuthorizationRequest,
    ) -> aiops_20200806_models.ListApplyAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apply_authorization_with_options(request, runtime)

    async def list_apply_authorization_async(
        self,
        request: aiops_20200806_models.ListApplyAuthorizationRequest,
    ) -> aiops_20200806_models.ListApplyAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apply_authorization_with_options_async(request, runtime)

    def list_auth_with_options(
        self,
        request: aiops_20200806_models.ListAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuth',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auth_with_options_async(
        self,
        request: aiops_20200806_models.ListAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuth',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auth(
        self,
        request: aiops_20200806_models.ListAuthRequest,
    ) -> aiops_20200806_models.ListAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_auth_with_options(request, runtime)

    async def list_auth_async(
        self,
        request: aiops_20200806_models.ListAuthRequest,
    ) -> aiops_20200806_models.ListAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_auth_with_options_async(request, runtime)

    def list_authorized_uid_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListAuthorizedUidResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAuthorizedUid',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListAuthorizedUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_uid_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListAuthorizedUidResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAuthorizedUid',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListAuthorizedUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_uid(self) -> aiops_20200806_models.ListAuthorizedUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_authorized_uid_with_options(runtime)

    async def list_authorized_uid_async(self) -> aiops_20200806_models.ListAuthorizedUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_authorized_uid_with_options_async(runtime)

    def list_cause_plan_with_options(
        self,
        request: aiops_20200806_models.ListCausePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListCausePlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCausePlan',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListCausePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cause_plan_with_options_async(
        self,
        request: aiops_20200806_models.ListCausePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListCausePlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCausePlan',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListCausePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cause_plan(
        self,
        request: aiops_20200806_models.ListCausePlanRequest,
    ) -> aiops_20200806_models.ListCausePlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cause_plan_with_options(request, runtime)

    async def list_cause_plan_async(
        self,
        request: aiops_20200806_models.ListCausePlanRequest,
    ) -> aiops_20200806_models.ListCausePlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cause_plan_with_options_async(request, runtime)

    def list_confirm_authorization_with_options(
        self,
        request: aiops_20200806_models.ListConfirmAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListConfirmAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfirmAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListConfirmAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_confirm_authorization_with_options_async(
        self,
        request: aiops_20200806_models.ListConfirmAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListConfirmAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfirmAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListConfirmAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_confirm_authorization(
        self,
        request: aiops_20200806_models.ListConfirmAuthorizationRequest,
    ) -> aiops_20200806_models.ListConfirmAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_confirm_authorization_with_options(request, runtime)

    async def list_confirm_authorization_async(
        self,
        request: aiops_20200806_models.ListConfirmAuthorizationRequest,
    ) -> aiops_20200806_models.ListConfirmAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_confirm_authorization_with_options_async(request, runtime)

    def list_event_with_options(
        self,
        request: aiops_20200806_models.ListEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_with_options_async(
        self,
        request: aiops_20200806_models.ListEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event(
        self,
        request: aiops_20200806_models.ListEventRequest,
    ) -> aiops_20200806_models.ListEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_with_options(request, runtime)

    async def list_event_async(
        self,
        request: aiops_20200806_models.ListEventRequest,
    ) -> aiops_20200806_models.ListEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_with_options_async(request, runtime)

    def list_not_authorized_uid_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListNotAuthorizedUidResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListNotAuthorizedUid',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListNotAuthorizedUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_not_authorized_uid_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListNotAuthorizedUidResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListNotAuthorizedUid',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListNotAuthorizedUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_not_authorized_uid(self) -> aiops_20200806_models.ListNotAuthorizedUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_not_authorized_uid_with_options(runtime)

    async def list_not_authorized_uid_async(self) -> aiops_20200806_models.ListNotAuthorizedUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_not_authorized_uid_with_options_async(runtime)

    def list_reports_with_options(
        self,
        request: aiops_20200806_models.ListReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_reports_with_options_async(
        self,
        request: aiops_20200806_models.ListReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_reports(
        self,
        request: aiops_20200806_models.ListReportsRequest,
    ) -> aiops_20200806_models.ListReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_reports_with_options(request, runtime)

    async def list_reports_async(
        self,
        request: aiops_20200806_models.ListReportsRequest,
    ) -> aiops_20200806_models.ListReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_reports_with_options_async(request, runtime)

    def list_root_cause_with_options(
        self,
        request: aiops_20200806_models.ListRootCauseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListRootCauseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListRootCauseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_root_cause_with_options_async(
        self,
        request: aiops_20200806_models.ListRootCauseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListRootCauseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListRootCauseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_root_cause(
        self,
        request: aiops_20200806_models.ListRootCauseRequest,
    ) -> aiops_20200806_models.ListRootCauseResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_root_cause_with_options(request, runtime)

    async def list_root_cause_async(
        self,
        request: aiops_20200806_models.ListRootCauseRequest,
    ) -> aiops_20200806_models.ListRootCauseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_root_cause_with_options_async(request, runtime)

    def list_sls_reports_with_options(
        self,
        request: aiops_20200806_models.ListSlsReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListSlsReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSlsReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListSlsReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sls_reports_with_options_async(
        self,
        request: aiops_20200806_models.ListSlsReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ListSlsReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSlsReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListSlsReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sls_reports(
        self,
        request: aiops_20200806_models.ListSlsReportsRequest,
    ) -> aiops_20200806_models.ListSlsReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sls_reports_with_options(request, runtime)

    async def list_sls_reports_async(
        self,
        request: aiops_20200806_models.ListSlsReportsRequest,
    ) -> aiops_20200806_models.ListSlsReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sls_reports_with_options_async(request, runtime)

    def put_alert_contact_with_options(
        self,
        request: aiops_20200806_models.PutAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.webhook):
            body['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_alert_contact_with_options_async(
        self,
        request: aiops_20200806_models.PutAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.webhook):
            body['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_alert_contact(
        self,
        request: aiops_20200806_models.PutAlertContactRequest,
    ) -> aiops_20200806_models.PutAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_alert_contact_with_options(request, runtime)

    async def put_alert_contact_async(
        self,
        request: aiops_20200806_models.PutAlertContactRequest,
    ) -> aiops_20200806_models.PutAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_alert_contact_with_options_async(request, runtime)

    def put_alert_contact_group_with_options(
        self,
        request: aiops_20200806_models.PutAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.alert_contact_group_json):
            body['AlertContactGroupJson'] = request.alert_contact_group_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_alert_contact_group_with_options_async(
        self,
        request: aiops_20200806_models.PutAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.alert_contact_group_json):
            body['AlertContactGroupJson'] = request.alert_contact_group_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_alert_contact_group(
        self,
        request: aiops_20200806_models.PutAlertContactGroupRequest,
    ) -> aiops_20200806_models.PutAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_alert_contact_group_with_options(request, runtime)

    async def put_alert_contact_group_async(
        self,
        request: aiops_20200806_models.PutAlertContactGroupRequest,
    ) -> aiops_20200806_models.PutAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_alert_contact_group_with_options_async(request, runtime)

    def put_alert_contact_to_group_with_options(
        self,
        request: aiops_20200806_models.PutAlertContactToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertContactToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id_list_json):
            body['GroupIdListJson'] = request.group_id_list_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContactToGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_alert_contact_to_group_with_options_async(
        self,
        request: aiops_20200806_models.PutAlertContactToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertContactToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id_list_json):
            body['GroupIdListJson'] = request.group_id_list_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContactToGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_alert_contact_to_group(
        self,
        request: aiops_20200806_models.PutAlertContactToGroupRequest,
    ) -> aiops_20200806_models.PutAlertContactToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_alert_contact_to_group_with_options(request, runtime)

    async def put_alert_contact_to_group_async(
        self,
        request: aiops_20200806_models.PutAlertContactToGroupRequest,
    ) -> aiops_20200806_models.PutAlertContactToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_alert_contact_to_group_with_options_async(request, runtime)

    def put_alert_ignore_with_options(
        self,
        request: aiops_20200806_models.PutAlertIgnoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertIgnoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutAlertIgnore',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertIgnoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_alert_ignore_with_options_async(
        self,
        request: aiops_20200806_models.PutAlertIgnoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertIgnoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutAlertIgnore',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertIgnoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_alert_ignore(
        self,
        request: aiops_20200806_models.PutAlertIgnoreRequest,
    ) -> aiops_20200806_models.PutAlertIgnoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_alert_ignore_with_options(request, runtime)

    async def put_alert_ignore_async(
        self,
        request: aiops_20200806_models.PutAlertIgnoreRequest,
    ) -> aiops_20200806_models.PutAlertIgnoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_alert_ignore_with_options_async(request, runtime)

    def put_alert_setting_with_options(
        self,
        request: aiops_20200806_models.PutAlertSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_silence_config):
            query['AlertSilenceConfig'] = request.alert_silence_config
        body = {}
        if not UtilClient.is_unset(request.alarm_level):
            body['AlarmLevel'] = request.alarm_level
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.business_group_ids_json):
            body['BusinessGroupIdsJson'] = request.business_group_ids_json
        if not UtilClient.is_unset(request.contact_group_ids_json):
            body['ContactGroupIdsJson'] = request.contact_group_ids_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        if not UtilClient.is_unset(request.customer_uid):
            body['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.send_dingtalk_notice):
            body['SendDingtalkNotice'] = request.send_dingtalk_notice
        if not UtilClient.is_unset(request.send_email_notice):
            body['SendEmailNotice'] = request.send_email_notice
        if not UtilClient.is_unset(request.send_sms_notice):
            body['SendSmsNotice'] = request.send_sms_notice
        if not UtilClient.is_unset(request.stop_duration):
            body['StopDuration'] = request.stop_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_alert_setting_with_options_async(
        self,
        request: aiops_20200806_models.PutAlertSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_silence_config):
            query['AlertSilenceConfig'] = request.alert_silence_config
        body = {}
        if not UtilClient.is_unset(request.alarm_level):
            body['AlarmLevel'] = request.alarm_level
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.business_group_ids_json):
            body['BusinessGroupIdsJson'] = request.business_group_ids_json
        if not UtilClient.is_unset(request.contact_group_ids_json):
            body['ContactGroupIdsJson'] = request.contact_group_ids_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        if not UtilClient.is_unset(request.customer_uid):
            body['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.send_dingtalk_notice):
            body['SendDingtalkNotice'] = request.send_dingtalk_notice
        if not UtilClient.is_unset(request.send_email_notice):
            body['SendEmailNotice'] = request.send_email_notice
        if not UtilClient.is_unset(request.send_sms_notice):
            body['SendSmsNotice'] = request.send_sms_notice
        if not UtilClient.is_unset(request.stop_duration):
            body['StopDuration'] = request.stop_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_alert_setting(
        self,
        request: aiops_20200806_models.PutAlertSettingRequest,
    ) -> aiops_20200806_models.PutAlertSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_alert_setting_with_options(request, runtime)

    async def put_alert_setting_async(
        self,
        request: aiops_20200806_models.PutAlertSettingRequest,
    ) -> aiops_20200806_models.PutAlertSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_alert_setting_with_options_async(request, runtime)

    def put_alert_setting_list_with_options(
        self,
        request: aiops_20200806_models.PutAlertSettingListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertSettingListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_edit_request_list_json):
            body['AlertSettingEditRequestListJson'] = request.alert_setting_edit_request_list_json
        if not UtilClient.is_unset(request.contact_group_ids_json):
            body['ContactGroupIdsJson'] = request.contact_group_ids_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSettingList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_alert_setting_list_with_options_async(
        self,
        request: aiops_20200806_models.PutAlertSettingListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertSettingListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_edit_request_list_json):
            body['AlertSettingEditRequestListJson'] = request.alert_setting_edit_request_list_json
        if not UtilClient.is_unset(request.contact_group_ids_json):
            body['ContactGroupIdsJson'] = request.contact_group_ids_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSettingList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_alert_setting_list(
        self,
        request: aiops_20200806_models.PutAlertSettingListRequest,
    ) -> aiops_20200806_models.PutAlertSettingListResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_alert_setting_list_with_options(request, runtime)

    async def put_alert_setting_list_async(
        self,
        request: aiops_20200806_models.PutAlertSettingListRequest,
    ) -> aiops_20200806_models.PutAlertSettingListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_alert_setting_list_with_options_async(request, runtime)

    def put_alert_setting_status_with_options(
        self,
        request: aiops_20200806_models.PutAlertSettingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertSettingStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.setting_status):
            body['SettingStatus'] = request.setting_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSettingStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_alert_setting_status_with_options_async(
        self,
        request: aiops_20200806_models.PutAlertSettingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutAlertSettingStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.setting_status):
            body['SettingStatus'] = request.setting_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSettingStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_alert_setting_status(
        self,
        request: aiops_20200806_models.PutAlertSettingStatusRequest,
    ) -> aiops_20200806_models.PutAlertSettingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_alert_setting_status_with_options(request, runtime)

    async def put_alert_setting_status_async(
        self,
        request: aiops_20200806_models.PutAlertSettingStatusRequest,
    ) -> aiops_20200806_models.PutAlertSettingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_alert_setting_status_with_options_async(request, runtime)

    def put_data_source_config_with_options(
        self,
        request: aiops_20200806_models.PutDataSourceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutDataSourceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_describe):
            query['DataSourceDescribe'] = request.data_source_describe
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_params_mapping):
            query['DataSourceParamsMapping'] = request.data_source_params_mapping
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutDataSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_data_source_config_with_options_async(
        self,
        request: aiops_20200806_models.PutDataSourceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutDataSourceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_describe):
            query['DataSourceDescribe'] = request.data_source_describe
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_params_mapping):
            query['DataSourceParamsMapping'] = request.data_source_params_mapping
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutDataSourceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_data_source_config(
        self,
        request: aiops_20200806_models.PutDataSourceConfigRequest,
    ) -> aiops_20200806_models.PutDataSourceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_data_source_config_with_options(request, runtime)

    async def put_data_source_config_async(
        self,
        request: aiops_20200806_models.PutDataSourceConfigRequest,
    ) -> aiops_20200806_models.PutDataSourceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_data_source_config_with_options_async(request, runtime)

    def put_group_resource_tag_with_options(
        self,
        request: aiops_20200806_models.PutGroupResourceTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutGroupResourceTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupResourceTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutGroupResourceTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_group_resource_tag_with_options_async(
        self,
        request: aiops_20200806_models.PutGroupResourceTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutGroupResourceTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupResourceTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutGroupResourceTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_group_resource_tag(
        self,
        request: aiops_20200806_models.PutGroupResourceTagRequest,
    ) -> aiops_20200806_models.PutGroupResourceTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_group_resource_tag_with_options(request, runtime)

    async def put_group_resource_tag_async(
        self,
        request: aiops_20200806_models.PutGroupResourceTagRequest,
    ) -> aiops_20200806_models.PutGroupResourceTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_group_resource_tag_with_options_async(request, runtime)

    def put_group_topology_tag_log_with_options(
        self,
        request: aiops_20200806_models.PutGroupTopologyTagLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutGroupTopologyTagLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupTopologyTagLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutGroupTopologyTagLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_group_topology_tag_log_with_options_async(
        self,
        request: aiops_20200806_models.PutGroupTopologyTagLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutGroupTopologyTagLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupTopologyTagLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutGroupTopologyTagLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_group_topology_tag_log(
        self,
        request: aiops_20200806_models.PutGroupTopologyTagLogRequest,
    ) -> aiops_20200806_models.PutGroupTopologyTagLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_group_topology_tag_log_with_options(request, runtime)

    async def put_group_topology_tag_log_async(
        self,
        request: aiops_20200806_models.PutGroupTopologyTagLogRequest,
    ) -> aiops_20200806_models.PutGroupTopologyTagLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_group_topology_tag_log_with_options_async(request, runtime)

    def put_report_email_config_with_options(
        self,
        request: aiops_20200806_models.PutReportEmailConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutReportEmailConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutReportEmailConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutReportEmailConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_report_email_config_with_options_async(
        self,
        request: aiops_20200806_models.PutReportEmailConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutReportEmailConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutReportEmailConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutReportEmailConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_report_email_config(
        self,
        request: aiops_20200806_models.PutReportEmailConfigRequest,
    ) -> aiops_20200806_models.PutReportEmailConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_report_email_config_with_options(request, runtime)

    async def put_report_email_config_async(
        self,
        request: aiops_20200806_models.PutReportEmailConfigRequest,
    ) -> aiops_20200806_models.PutReportEmailConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_report_email_config_with_options_async(request, runtime)

    def put_resource_whitelist_with_options(
        self,
        request: aiops_20200806_models.PutResourceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutResourceWhitelistResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutResourceWhitelist',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutResourceWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_resource_whitelist_with_options_async(
        self,
        request: aiops_20200806_models.PutResourceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.PutResourceWhitelistResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutResourceWhitelist',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutResourceWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_resource_whitelist(
        self,
        request: aiops_20200806_models.PutResourceWhitelistRequest,
    ) -> aiops_20200806_models.PutResourceWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_resource_whitelist_with_options(request, runtime)

    async def put_resource_whitelist_async(
        self,
        request: aiops_20200806_models.PutResourceWhitelistRequest,
    ) -> aiops_20200806_models.PutResourceWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_resource_whitelist_with_options_async(request, runtime)

    def replace_script_list_with_options(
        self,
        request: aiops_20200806_models.ReplaceScriptListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ReplaceScriptListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ReplaceScriptListResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_script_list_with_options_async(
        self,
        request: aiops_20200806_models.ReplaceScriptListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.ReplaceScriptListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ReplaceScriptListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_script_list(
        self,
        request: aiops_20200806_models.ReplaceScriptListRequest,
    ) -> aiops_20200806_models.ReplaceScriptListResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_script_list_with_options(request, runtime)

    async def replace_script_list_async(
        self,
        request: aiops_20200806_models.ReplaceScriptListRequest,
    ) -> aiops_20200806_models.ReplaceScriptListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_script_list_with_options_async(request, runtime)

    def revoke_submit_apply_permission_with_options(
        self,
        request: aiops_20200806_models.RevokeSubmitApplyPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RevokeSubmitApplyPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSubmitApplyPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RevokeSubmitApplyPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_submit_apply_permission_with_options_async(
        self,
        request: aiops_20200806_models.RevokeSubmitApplyPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RevokeSubmitApplyPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSubmitApplyPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RevokeSubmitApplyPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_submit_apply_permission(
        self,
        request: aiops_20200806_models.RevokeSubmitApplyPermissionRequest,
    ) -> aiops_20200806_models.RevokeSubmitApplyPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_submit_apply_permission_with_options(request, runtime)

    async def revoke_submit_apply_permission_async(
        self,
        request: aiops_20200806_models.RevokeSubmitApplyPermissionRequest,
    ) -> aiops_20200806_models.RevokeSubmitApplyPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_submit_apply_permission_with_options_async(request, runtime)

    def run_analysis_process_with_options(
        self,
        request: aiops_20200806_models.RunAnalysisProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunAnalysisProcessResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunAnalysisProcess',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunAnalysisProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_analysis_process_with_options_async(
        self,
        request: aiops_20200806_models.RunAnalysisProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunAnalysisProcessResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunAnalysisProcess',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunAnalysisProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_analysis_process(
        self,
        request: aiops_20200806_models.RunAnalysisProcessRequest,
    ) -> aiops_20200806_models.RunAnalysisProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_analysis_process_with_options(request, runtime)

    async def run_analysis_process_async(
        self,
        request: aiops_20200806_models.RunAnalysisProcessRequest,
    ) -> aiops_20200806_models.RunAnalysisProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_analysis_process_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        request: aiops_20200806_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        request: aiops_20200806_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: aiops_20200806_models.RunCommandRequest,
    ) -> aiops_20200806_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: aiops_20200806_models.RunCommandRequest,
    ) -> aiops_20200806_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def run_forecast_analyze_with_options(
        self,
        request: aiops_20200806_models.RunForecastAnalyzeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunForecastAnalyzeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunForecastAnalyze',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunForecastAnalyzeResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_forecast_analyze_with_options_async(
        self,
        request: aiops_20200806_models.RunForecastAnalyzeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunForecastAnalyzeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunForecastAnalyze',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunForecastAnalyzeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_forecast_analyze(
        self,
        request: aiops_20200806_models.RunForecastAnalyzeRequest,
    ) -> aiops_20200806_models.RunForecastAnalyzeResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_forecast_analyze_with_options(request, runtime)

    async def run_forecast_analyze_async(
        self,
        request: aiops_20200806_models.RunForecastAnalyzeRequest,
    ) -> aiops_20200806_models.RunForecastAnalyzeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_forecast_analyze_with_options_async(request, runtime)

    def run_patrol_inspection_with_options(
        self,
        request: aiops_20200806_models.RunPatrolInspectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunPatrolInspectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunPatrolInspection',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunPatrolInspectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_patrol_inspection_with_options_async(
        self,
        request: aiops_20200806_models.RunPatrolInspectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunPatrolInspectionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunPatrolInspection',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunPatrolInspectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_patrol_inspection(
        self,
        request: aiops_20200806_models.RunPatrolInspectionRequest,
    ) -> aiops_20200806_models.RunPatrolInspectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_patrol_inspection_with_options(request, runtime)

    async def run_patrol_inspection_async(
        self,
        request: aiops_20200806_models.RunPatrolInspectionRequest,
    ) -> aiops_20200806_models.RunPatrolInspectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_patrol_inspection_with_options_async(request, runtime)

    def run_repair_script_with_options(
        self,
        request: aiops_20200806_models.RunRepairScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunRepairScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunRepairScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunRepairScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_repair_script_with_options_async(
        self,
        request: aiops_20200806_models.RunRepairScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunRepairScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunRepairScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunRepairScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_repair_script(
        self,
        request: aiops_20200806_models.RunRepairScriptRequest,
    ) -> aiops_20200806_models.RunRepairScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_repair_script_with_options(request, runtime)

    async def run_repair_script_async(
        self,
        request: aiops_20200806_models.RunRepairScriptRequest,
    ) -> aiops_20200806_models.RunRepairScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_repair_script_with_options_async(request, runtime)

    def run_risk_patrol_with_options(
        self,
        request: aiops_20200806_models.RunRiskPatrolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunRiskPatrolResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunRiskPatrol',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunRiskPatrolResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_risk_patrol_with_options_async(
        self,
        request: aiops_20200806_models.RunRiskPatrolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.RunRiskPatrolResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunRiskPatrol',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunRiskPatrolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_risk_patrol(
        self,
        request: aiops_20200806_models.RunRiskPatrolRequest,
    ) -> aiops_20200806_models.RunRiskPatrolResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_risk_patrol_with_options(request, runtime)

    async def run_risk_patrol_async(
        self,
        request: aiops_20200806_models.RunRiskPatrolRequest,
    ) -> aiops_20200806_models.RunRiskPatrolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_risk_patrol_with_options_async(request, runtime)

    def switch_user_top_with_options(
        self,
        request: aiops_20200806_models.SwitchUserTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.SwitchUserTopResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchUserTop',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.SwitchUserTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_user_top_with_options_async(
        self,
        request: aiops_20200806_models.SwitchUserTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.SwitchUserTopResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchUserTop',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.SwitchUserTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_user_top(
        self,
        request: aiops_20200806_models.SwitchUserTopRequest,
    ) -> aiops_20200806_models.SwitchUserTopResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_user_top_with_options(request, runtime)

    async def switch_user_top_async(
        self,
        request: aiops_20200806_models.SwitchUserTopRequest,
    ) -> aiops_20200806_models.SwitchUserTopResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_user_top_with_options_async(request, runtime)

    def upd_business_group_with_options(
        self,
        tmp_req: aiops_20200806_models.UpdBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdBusinessGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.UpdBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def upd_business_group_with_options_async(
        self,
        tmp_req: aiops_20200806_models.UpdBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdBusinessGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.UpdBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdBusinessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upd_business_group(
        self,
        request: aiops_20200806_models.UpdBusinessGroupRequest,
    ) -> aiops_20200806_models.UpdBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.upd_business_group_with_options(request, runtime)

    async def upd_business_group_async(
        self,
        request: aiops_20200806_models.UpdBusinessGroupRequest,
    ) -> aiops_20200806_models.UpdBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upd_business_group_with_options_async(request, runtime)

    def update_authorization_with_options(
        self,
        request: aiops_20200806_models.UpdateAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_authorization_with_options_async(
        self,
        request: aiops_20200806_models.UpdateAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_authorization(
        self,
        request: aiops_20200806_models.UpdateAuthorizationRequest,
    ) -> aiops_20200806_models.UpdateAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_authorization_with_options(request, runtime)

    async def update_authorization_async(
        self,
        request: aiops_20200806_models.UpdateAuthorizationRequest,
    ) -> aiops_20200806_models.UpdateAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_authorization_with_options_async(request, runtime)

    def update_bind_metric_with_options(
        self,
        request: aiops_20200806_models.UpdateBindMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateBindMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBindMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBindMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bind_metric_with_options_async(
        self,
        request: aiops_20200806_models.UpdateBindMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateBindMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBindMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBindMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bind_metric(
        self,
        request: aiops_20200806_models.UpdateBindMetricRequest,
    ) -> aiops_20200806_models.UpdateBindMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_bind_metric_with_options(request, runtime)

    async def update_bind_metric_async(
        self,
        request: aiops_20200806_models.UpdateBindMetricRequest,
    ) -> aiops_20200806_models.UpdateBindMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_bind_metric_with_options_async(request, runtime)

    def update_business_group_with_options(
        self,
        tmp_req: aiops_20200806_models.UpdateBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateBusinessGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.UpdateBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.cloud_resource_type_id):
            query['CloudResourceTypeId'] = request.cloud_resource_type_id
        if not UtilClient.is_unset(request.deal_type):
            query['DealType'] = request.deal_type
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_business_group_with_options_async(
        self,
        tmp_req: aiops_20200806_models.UpdateBusinessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateBusinessGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.UpdateBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.cloud_resource_type_id):
            query['CloudResourceTypeId'] = request.cloud_resource_type_id
        if not UtilClient.is_unset(request.deal_type):
            query['DealType'] = request.deal_type
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_business_group(
        self,
        request: aiops_20200806_models.UpdateBusinessGroupRequest,
    ) -> aiops_20200806_models.UpdateBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_business_group_with_options(request, runtime)

    async def update_business_group_async(
        self,
        request: aiops_20200806_models.UpdateBusinessGroupRequest,
    ) -> aiops_20200806_models.UpdateBusinessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_business_group_with_options_async(request, runtime)

    def update_business_metric_alert_config_with_options(
        self,
        request: aiops_20200806_models.UpdateBusinessMetricAlertConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateBusinessMetricAlertConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessMetricAlertConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessMetricAlertConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_business_metric_alert_config_with_options_async(
        self,
        request: aiops_20200806_models.UpdateBusinessMetricAlertConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateBusinessMetricAlertConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessMetricAlertConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessMetricAlertConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_business_metric_alert_config(
        self,
        request: aiops_20200806_models.UpdateBusinessMetricAlertConfigRequest,
    ) -> aiops_20200806_models.UpdateBusinessMetricAlertConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_business_metric_alert_config_with_options(request, runtime)

    async def update_business_metric_alert_config_async(
        self,
        request: aiops_20200806_models.UpdateBusinessMetricAlertConfigRequest,
    ) -> aiops_20200806_models.UpdateBusinessMetricAlertConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_business_metric_alert_config_with_options_async(request, runtime)

    def update_business_metric_resource_with_options(
        self,
        request: aiops_20200806_models.UpdateBusinessMetricResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateBusinessMetricResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_metric_id):
            query['BusinessMetricId'] = request.business_metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_list):
            query['ResourceList'] = request.resource_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessMetricResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessMetricResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_business_metric_resource_with_options_async(
        self,
        request: aiops_20200806_models.UpdateBusinessMetricResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateBusinessMetricResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_metric_id):
            query['BusinessMetricId'] = request.business_metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_list):
            query['ResourceList'] = request.resource_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessMetricResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessMetricResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_business_metric_resource(
        self,
        request: aiops_20200806_models.UpdateBusinessMetricResourceRequest,
    ) -> aiops_20200806_models.UpdateBusinessMetricResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_business_metric_resource_with_options(request, runtime)

    async def update_business_metric_resource_async(
        self,
        request: aiops_20200806_models.UpdateBusinessMetricResourceRequest,
    ) -> aiops_20200806_models.UpdateBusinessMetricResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_business_metric_resource_with_options_async(request, runtime)

    def update_data_source_config_with_options(
        self,
        request: aiops_20200806_models.UpdateDataSourceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateDataSourceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_describe):
            query['DataSourceDescribe'] = request.data_source_describe
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_params_mapping):
            query['DataSourceParamsMapping'] = request.data_source_params_mapping
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateDataSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_config_with_options_async(
        self,
        request: aiops_20200806_models.UpdateDataSourceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateDataSourceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_describe):
            query['DataSourceDescribe'] = request.data_source_describe
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_params_mapping):
            query['DataSourceParamsMapping'] = request.data_source_params_mapping
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateDataSourceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source_config(
        self,
        request: aiops_20200806_models.UpdateDataSourceConfigRequest,
    ) -> aiops_20200806_models.UpdateDataSourceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_config_with_options(request, runtime)

    async def update_data_source_config_async(
        self,
        request: aiops_20200806_models.UpdateDataSourceConfigRequest,
    ) -> aiops_20200806_models.UpdateDataSourceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_data_source_config_with_options_async(request, runtime)

    def update_handle_risk_with_options(
        self,
        request: aiops_20200806_models.UpdateHandleRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateHandleRiskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHandleRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateHandleRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_handle_risk_with_options_async(
        self,
        request: aiops_20200806_models.UpdateHandleRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateHandleRiskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHandleRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateHandleRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_handle_risk(
        self,
        request: aiops_20200806_models.UpdateHandleRiskRequest,
    ) -> aiops_20200806_models.UpdateHandleRiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_handle_risk_with_options(request, runtime)

    async def update_handle_risk_async(
        self,
        request: aiops_20200806_models.UpdateHandleRiskRequest,
    ) -> aiops_20200806_models.UpdateHandleRiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_handle_risk_with_options_async(request, runtime)

    def update_handle_risk_base_with_options(
        self,
        request: aiops_20200806_models.UpdateHandleRiskBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateHandleRiskBaseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHandleRiskBase',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateHandleRiskBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_handle_risk_base_with_options_async(
        self,
        request: aiops_20200806_models.UpdateHandleRiskBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateHandleRiskBaseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHandleRiskBase',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateHandleRiskBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_handle_risk_base(
        self,
        request: aiops_20200806_models.UpdateHandleRiskBaseRequest,
    ) -> aiops_20200806_models.UpdateHandleRiskBaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_handle_risk_base_with_options(request, runtime)

    async def update_handle_risk_base_async(
        self,
        request: aiops_20200806_models.UpdateHandleRiskBaseRequest,
    ) -> aiops_20200806_models.UpdateHandleRiskBaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_handle_risk_base_with_options_async(request, runtime)

    def update_ignore_risk_with_options(
        self,
        request: aiops_20200806_models.UpdateIgnoreRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateIgnoreRiskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIgnoreRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateIgnoreRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ignore_risk_with_options_async(
        self,
        request: aiops_20200806_models.UpdateIgnoreRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateIgnoreRiskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIgnoreRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateIgnoreRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ignore_risk(
        self,
        request: aiops_20200806_models.UpdateIgnoreRiskRequest,
    ) -> aiops_20200806_models.UpdateIgnoreRiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ignore_risk_with_options(request, runtime)

    async def update_ignore_risk_async(
        self,
        request: aiops_20200806_models.UpdateIgnoreRiskRequest,
    ) -> aiops_20200806_models.UpdateIgnoreRiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ignore_risk_with_options_async(request, runtime)

    def update_ignore_risk_base_with_options(
        self,
        request: aiops_20200806_models.UpdateIgnoreRiskBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateIgnoreRiskBaseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIgnoreRiskBase',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateIgnoreRiskBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ignore_risk_base_with_options_async(
        self,
        request: aiops_20200806_models.UpdateIgnoreRiskBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateIgnoreRiskBaseResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIgnoreRiskBase',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateIgnoreRiskBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ignore_risk_base(
        self,
        request: aiops_20200806_models.UpdateIgnoreRiskBaseRequest,
    ) -> aiops_20200806_models.UpdateIgnoreRiskBaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ignore_risk_base_with_options(request, runtime)

    async def update_ignore_risk_base_async(
        self,
        request: aiops_20200806_models.UpdateIgnoreRiskBaseRequest,
    ) -> aiops_20200806_models.UpdateIgnoreRiskBaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ignore_risk_base_with_options_async(request, runtime)

    def update_inspection_setting_status_with_options(
        self,
        request: aiops_20200806_models.UpdateInspectionSettingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateInspectionSettingStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.risk_enable_status):
            body['RiskEnableStatus'] = request.risk_enable_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInspectionSettingStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateInspectionSettingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_inspection_setting_status_with_options_async(
        self,
        request: aiops_20200806_models.UpdateInspectionSettingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateInspectionSettingStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.risk_enable_status):
            body['RiskEnableStatus'] = request.risk_enable_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInspectionSettingStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateInspectionSettingStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_inspection_setting_status(
        self,
        request: aiops_20200806_models.UpdateInspectionSettingStatusRequest,
    ) -> aiops_20200806_models.UpdateInspectionSettingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_inspection_setting_status_with_options(request, runtime)

    async def update_inspection_setting_status_async(
        self,
        request: aiops_20200806_models.UpdateInspectionSettingStatusRequest,
    ) -> aiops_20200806_models.UpdateInspectionSettingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_inspection_setting_status_with_options_async(request, runtime)

    def update_inspection_threshold_with_options(
        self,
        request: aiops_20200806_models.UpdateInspectionThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateInspectionThresholdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.threshold_item_list_json):
            body['ThresholdItemListJson'] = request.threshold_item_list_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInspectionThreshold',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateInspectionThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_inspection_threshold_with_options_async(
        self,
        request: aiops_20200806_models.UpdateInspectionThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateInspectionThresholdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.threshold_item_list_json):
            body['ThresholdItemListJson'] = request.threshold_item_list_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInspectionThreshold',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateInspectionThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_inspection_threshold(
        self,
        request: aiops_20200806_models.UpdateInspectionThresholdRequest,
    ) -> aiops_20200806_models.UpdateInspectionThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_inspection_threshold_with_options(request, runtime)

    async def update_inspection_threshold_async(
        self,
        request: aiops_20200806_models.UpdateInspectionThresholdRequest,
    ) -> aiops_20200806_models.UpdateInspectionThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_inspection_threshold_with_options_async(request, runtime)

    def update_operation_permission_with_options(
        self,
        request: aiops_20200806_models.UpdateOperationPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateOperationPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOperationPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateOperationPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_operation_permission_with_options_async(
        self,
        request: aiops_20200806_models.UpdateOperationPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateOperationPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOperationPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateOperationPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_operation_permission(
        self,
        request: aiops_20200806_models.UpdateOperationPermissionRequest,
    ) -> aiops_20200806_models.UpdateOperationPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_operation_permission_with_options(request, runtime)

    async def update_operation_permission_async(
        self,
        request: aiops_20200806_models.UpdateOperationPermissionRequest,
    ) -> aiops_20200806_models.UpdateOperationPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_operation_permission_with_options_async(request, runtime)

    def update_report_email_config_status_with_options(
        self,
        request: aiops_20200806_models.UpdateReportEmailConfigStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateReportEmailConfigStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_status):
            body['ConfigStatus'] = request.config_status
        if not UtilClient.is_unset(request.mail_config_id):
            body['MailConfigId'] = request.mail_config_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportEmailConfigStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateReportEmailConfigStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_report_email_config_status_with_options_async(
        self,
        request: aiops_20200806_models.UpdateReportEmailConfigStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateReportEmailConfigStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_status):
            body['ConfigStatus'] = request.config_status
        if not UtilClient.is_unset(request.mail_config_id):
            body['MailConfigId'] = request.mail_config_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportEmailConfigStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateReportEmailConfigStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_report_email_config_status(
        self,
        request: aiops_20200806_models.UpdateReportEmailConfigStatusRequest,
    ) -> aiops_20200806_models.UpdateReportEmailConfigStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_report_email_config_status_with_options(request, runtime)

    async def update_report_email_config_status_async(
        self,
        request: aiops_20200806_models.UpdateReportEmailConfigStatusRequest,
    ) -> aiops_20200806_models.UpdateReportEmailConfigStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_report_email_config_status_with_options_async(request, runtime)

    def update_report_subscription_with_options(
        self,
        request: aiops_20200806_models.UpdateReportSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateReportSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.day_of_week):
            body['DayOfWeek'] = request.day_of_week
        if not UtilClient.is_unset(request.hour_of_day):
            body['HourOfDay'] = request.hour_of_day
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.report_name):
            body['ReportName'] = request.report_name
        if not UtilClient.is_unset(request.subscribe):
            body['Subscribe'] = request.subscribe
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportSubscription',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateReportSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_report_subscription_with_options_async(
        self,
        request: aiops_20200806_models.UpdateReportSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateReportSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.day_of_week):
            body['DayOfWeek'] = request.day_of_week
        if not UtilClient.is_unset(request.hour_of_day):
            body['HourOfDay'] = request.hour_of_day
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.report_name):
            body['ReportName'] = request.report_name
        if not UtilClient.is_unset(request.subscribe):
            body['Subscribe'] = request.subscribe
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportSubscription',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateReportSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_report_subscription(
        self,
        request: aiops_20200806_models.UpdateReportSubscriptionRequest,
    ) -> aiops_20200806_models.UpdateReportSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_report_subscription_with_options(request, runtime)

    async def update_report_subscription_async(
        self,
        request: aiops_20200806_models.UpdateReportSubscriptionRequest,
    ) -> aiops_20200806_models.UpdateReportSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_report_subscription_with_options_async(request, runtime)

    def update_scenario_with_options(
        self,
        request: aiops_20200806_models.UpdateScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            query['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scenario_with_options_async(
        self,
        request: aiops_20200806_models.UpdateScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            query['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scenario(
        self,
        request: aiops_20200806_models.UpdateScenarioRequest,
    ) -> aiops_20200806_models.UpdateScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scenario_with_options(request, runtime)

    async def update_scenario_async(
        self,
        request: aiops_20200806_models.UpdateScenarioRequest,
    ) -> aiops_20200806_models.UpdateScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scenario_with_options_async(request, runtime)

    def update_scene_with_options(
        self,
        request: aiops_20200806_models.UpdateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.metric_list_json):
            body['MetricListJson'] = request.metric_list_json
        if not UtilClient.is_unset(request.node_list_json):
            body['NodeListJson'] = request.node_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_desc):
            body['SceneDesc'] = request.scene_desc
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_owner):
            body['SceneOwner'] = request.scene_owner
        if not UtilClient.is_unset(request.scene_webhook):
            body['SceneWebhook'] = request.scene_webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_with_options_async(
        self,
        request: aiops_20200806_models.UpdateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.metric_list_json):
            body['MetricListJson'] = request.metric_list_json
        if not UtilClient.is_unset(request.node_list_json):
            body['NodeListJson'] = request.node_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_desc):
            body['SceneDesc'] = request.scene_desc
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_owner):
            body['SceneOwner'] = request.scene_owner
        if not UtilClient.is_unset(request.scene_webhook):
            body['SceneWebhook'] = request.scene_webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene(
        self,
        request: aiops_20200806_models.UpdateSceneRequest,
    ) -> aiops_20200806_models.UpdateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scene_with_options(request, runtime)

    async def update_scene_async(
        self,
        request: aiops_20200806_models.UpdateSceneRequest,
    ) -> aiops_20200806_models.UpdateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scene_with_options_async(request, runtime)

    def update_scene_model_with_options(
        self,
        request: aiops_20200806_models.UpdateSceneModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fc_function_name):
            body['FcFunctionName'] = request.fc_function_name
        if not UtilClient.is_unset(request.fc_handler):
            body['FcHandler'] = request.fc_handler
        if not UtilClient.is_unset(request.fc_initializer):
            body['FcInitializer'] = request.fc_initializer
        if not UtilClient.is_unset(request.fc_region_no):
            body['FcRegionNo'] = request.fc_region_no
        if not UtilClient.is_unset(request.fc_service_name):
            body['FcServiceName'] = request.fc_service_name
        if not UtilClient.is_unset(request.model_desc):
            body['ModelDesc'] = request.model_desc
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_language):
            body['ModelLanguage'] = request.model_language
        if not UtilClient.is_unset(request.model_memo):
            body['ModelMemo'] = request.model_memo
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.root_cause_desc):
            body['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_cause_solution):
            body['RootCauseSolution'] = request.root_cause_solution
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_model_with_options_async(
        self,
        request: aiops_20200806_models.UpdateSceneModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fc_function_name):
            body['FcFunctionName'] = request.fc_function_name
        if not UtilClient.is_unset(request.fc_handler):
            body['FcHandler'] = request.fc_handler
        if not UtilClient.is_unset(request.fc_initializer):
            body['FcInitializer'] = request.fc_initializer
        if not UtilClient.is_unset(request.fc_region_no):
            body['FcRegionNo'] = request.fc_region_no
        if not UtilClient.is_unset(request.fc_service_name):
            body['FcServiceName'] = request.fc_service_name
        if not UtilClient.is_unset(request.model_desc):
            body['ModelDesc'] = request.model_desc
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_language):
            body['ModelLanguage'] = request.model_language
        if not UtilClient.is_unset(request.model_memo):
            body['ModelMemo'] = request.model_memo
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.root_cause_desc):
            body['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_cause_solution):
            body['RootCauseSolution'] = request.root_cause_solution
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene_model(
        self,
        request: aiops_20200806_models.UpdateSceneModelRequest,
    ) -> aiops_20200806_models.UpdateSceneModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scene_model_with_options(request, runtime)

    async def update_scene_model_async(
        self,
        request: aiops_20200806_models.UpdateSceneModelRequest,
    ) -> aiops_20200806_models.UpdateSceneModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scene_model_with_options_async(request, runtime)

    def update_scene_model_apply_with_options(
        self,
        request: aiops_20200806_models.UpdateSceneModelApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneModelApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_content):
            body['ApplyContent'] = request.apply_content
        if not UtilClient.is_unset(request.apply_id):
            body['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.apply_status):
            body['ApplyStatus'] = request.apply_status
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModelApply',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_model_apply_with_options_async(
        self,
        request: aiops_20200806_models.UpdateSceneModelApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneModelApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_content):
            body['ApplyContent'] = request.apply_content
        if not UtilClient.is_unset(request.apply_id):
            body['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.apply_status):
            body['ApplyStatus'] = request.apply_status
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModelApply',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene_model_apply(
        self,
        request: aiops_20200806_models.UpdateSceneModelApplyRequest,
    ) -> aiops_20200806_models.UpdateSceneModelApplyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scene_model_apply_with_options(request, runtime)

    async def update_scene_model_apply_async(
        self,
        request: aiops_20200806_models.UpdateSceneModelApplyRequest,
    ) -> aiops_20200806_models.UpdateSceneModelApplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scene_model_apply_with_options_async(request, runtime)

    def update_scene_model_cur_version_with_options(
        self,
        request: aiops_20200806_models.UpdateSceneModelCurVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneModelCurVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_id):
            body['ExtId'] = request.ext_id
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModelCurVersion',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelCurVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_model_cur_version_with_options_async(
        self,
        request: aiops_20200806_models.UpdateSceneModelCurVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneModelCurVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_id):
            body['ExtId'] = request.ext_id
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModelCurVersion',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelCurVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene_model_cur_version(
        self,
        request: aiops_20200806_models.UpdateSceneModelCurVersionRequest,
    ) -> aiops_20200806_models.UpdateSceneModelCurVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scene_model_cur_version_with_options(request, runtime)

    async def update_scene_model_cur_version_async(
        self,
        request: aiops_20200806_models.UpdateSceneModelCurVersionRequest,
    ) -> aiops_20200806_models.UpdateSceneModelCurVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scene_model_cur_version_with_options_async(request, runtime)

    def update_scene_system_model_status_with_options(
        self,
        request: aiops_20200806_models.UpdateSceneSystemModelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneSystemModelStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_status):
            body['ModelStatus'] = request.model_status
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneSystemModelStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneSystemModelStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_system_model_status_with_options_async(
        self,
        request: aiops_20200806_models.UpdateSceneSystemModelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateSceneSystemModelStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_status):
            body['ModelStatus'] = request.model_status
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneSystemModelStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneSystemModelStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene_system_model_status(
        self,
        request: aiops_20200806_models.UpdateSceneSystemModelStatusRequest,
    ) -> aiops_20200806_models.UpdateSceneSystemModelStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scene_system_model_status_with_options(request, runtime)

    async def update_scene_system_model_status_async(
        self,
        request: aiops_20200806_models.UpdateSceneSystemModelStatusRequest,
    ) -> aiops_20200806_models.UpdateSceneSystemModelStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scene_system_model_status_with_options_async(request, runtime)

    def update_scenestatus_with_options(
        self,
        request: aiops_20200806_models.UpdateScenestatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateScenestatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScenestatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScenestatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scenestatus_with_options_async(
        self,
        request: aiops_20200806_models.UpdateScenestatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateScenestatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScenestatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScenestatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scenestatus(
        self,
        request: aiops_20200806_models.UpdateScenestatusRequest,
    ) -> aiops_20200806_models.UpdateScenestatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scenestatus_with_options(request, runtime)

    async def update_scenestatus_async(
        self,
        request: aiops_20200806_models.UpdateScenestatusRequest,
    ) -> aiops_20200806_models.UpdateScenestatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scenestatus_with_options_async(request, runtime)

    def update_script_with_options(
        self,
        request: aiops_20200806_models.UpdateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handle_suggest_desc):
            query['HandleSuggestDesc'] = request.handle_suggest_desc
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.root_cause_desc):
            query['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_causes_log):
            query['RootCausesLog'] = request.root_causes_log
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        if not UtilClient.is_unset(request.script_language):
            query['ScriptLanguage'] = request.script_language
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_script_with_options_async(
        self,
        request: aiops_20200806_models.UpdateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handle_suggest_desc):
            query['HandleSuggestDesc'] = request.handle_suggest_desc
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.root_cause_desc):
            query['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_causes_log):
            query['RootCausesLog'] = request.root_causes_log
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        if not UtilClient.is_unset(request.script_language):
            query['ScriptLanguage'] = request.script_language
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_script(
        self,
        request: aiops_20200806_models.UpdateScriptRequest,
    ) -> aiops_20200806_models.UpdateScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_script_with_options(request, runtime)

    async def update_script_async(
        self,
        request: aiops_20200806_models.UpdateScriptRequest,
    ) -> aiops_20200806_models.UpdateScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_script_with_options_async(request, runtime)

    def update_status_of_scene_with_options(
        self,
        request: aiops_20200806_models.UpdateStatusOfSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateStatusOfSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_status):
            body['SceneStatus'] = request.scene_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStatusOfScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateStatusOfSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_status_of_scene_with_options_async(
        self,
        request: aiops_20200806_models.UpdateStatusOfSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateStatusOfSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_status):
            body['SceneStatus'] = request.scene_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStatusOfScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateStatusOfSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_status_of_scene(
        self,
        request: aiops_20200806_models.UpdateStatusOfSceneRequest,
    ) -> aiops_20200806_models.UpdateStatusOfSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_status_of_scene_with_options(request, runtime)

    async def update_status_of_scene_async(
        self,
        request: aiops_20200806_models.UpdateStatusOfSceneRequest,
    ) -> aiops_20200806_models.UpdateStatusOfSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_status_of_scene_with_options_async(request, runtime)

    def update_tag_info_with_options(
        self,
        request: aiops_20200806_models.UpdateTagInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateTagInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateTagInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tag_info_with_options_async(
        self,
        request: aiops_20200806_models.UpdateTagInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiops_20200806_models.UpdateTagInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateTagInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tag_info(
        self,
        request: aiops_20200806_models.UpdateTagInfoRequest,
    ) -> aiops_20200806_models.UpdateTagInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_tag_info_with_options(request, runtime)

    async def update_tag_info_async(
        self,
        request: aiops_20200806_models.UpdateTagInfoRequest,
    ) -> aiops_20200806_models.UpdateTagInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_tag_info_with_options_async(request, runtime)
