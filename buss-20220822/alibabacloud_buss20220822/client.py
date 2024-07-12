# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_buss20220822 import models as buss_20220822_models
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
        self._endpoint = self.get_endpoint('buss', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def business_result_service_with_options(
        self,
        tmp_req: buss_20220822_models.BusinessResultServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.BusinessResultServiceResponse:
        """
        @summary 处罚请求异步接口回调
        
        @param tmp_req: BusinessResultServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BusinessResultServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.BusinessResultServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.result):
            request.result_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.result, 'Result', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BusinessResultService',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.BusinessResultServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def business_result_service_with_options_async(
        self,
        tmp_req: buss_20220822_models.BusinessResultServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.BusinessResultServiceResponse:
        """
        @summary 处罚请求异步接口回调
        
        @param tmp_req: BusinessResultServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BusinessResultServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.BusinessResultServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.result):
            request.result_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.result, 'Result', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BusinessResultService',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.BusinessResultServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def business_result_service(
        self,
        request: buss_20220822_models.BusinessResultServiceRequest,
    ) -> buss_20220822_models.BusinessResultServiceResponse:
        """
        @summary 处罚请求异步接口回调
        
        @param request: BusinessResultServiceRequest
        @return: BusinessResultServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.business_result_service_with_options(request, runtime)

    async def business_result_service_async(
        self,
        request: buss_20220822_models.BusinessResultServiceRequest,
    ) -> buss_20220822_models.BusinessResultServiceResponse:
        """
        @summary 处罚请求异步接口回调
        
        @param request: BusinessResultServiceRequest
        @return: BusinessResultServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.business_result_service_with_options_async(request, runtime)

    def create_user_investigation_info_query_task_with_options(
        self,
        request: buss_20220822_models.CreateUserInvestigationInfoQueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.CreateUserInvestigationInfoQueryTaskResponse:
        """
        @summary 协查中心查询任务接口
        
        @param request: CreateUserInvestigationInfoQueryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserInvestigationInfoQueryTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserInvestigationInfoQueryTask',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.CreateUserInvestigationInfoQueryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_investigation_info_query_task_with_options_async(
        self,
        request: buss_20220822_models.CreateUserInvestigationInfoQueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.CreateUserInvestigationInfoQueryTaskResponse:
        """
        @summary 协查中心查询任务接口
        
        @param request: CreateUserInvestigationInfoQueryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserInvestigationInfoQueryTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserInvestigationInfoQueryTask',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.CreateUserInvestigationInfoQueryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_investigation_info_query_task(
        self,
        request: buss_20220822_models.CreateUserInvestigationInfoQueryTaskRequest,
    ) -> buss_20220822_models.CreateUserInvestigationInfoQueryTaskResponse:
        """
        @summary 协查中心查询任务接口
        
        @param request: CreateUserInvestigationInfoQueryTaskRequest
        @return: CreateUserInvestigationInfoQueryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_investigation_info_query_task_with_options(request, runtime)

    async def create_user_investigation_info_query_task_async(
        self,
        request: buss_20220822_models.CreateUserInvestigationInfoQueryTaskRequest,
    ) -> buss_20220822_models.CreateUserInvestigationInfoQueryTaskResponse:
        """
        @summary 协查中心查询任务接口
        
        @param request: CreateUserInvestigationInfoQueryTaskRequest
        @return: CreateUserInvestigationInfoQueryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_investigation_info_query_task_with_options_async(request, runtime)

    def find_instance_info_with_options(
        self,
        tmp_req: buss_20220822_models.FindInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.FindInstanceInfoResponse:
        """
        @summary 反查资源
        
        @param tmp_req: FindInstanceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindInstanceInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.FindInstanceInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extras):
            request.extras_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extras, 'extras', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindInstanceInfo',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.FindInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_instance_info_with_options_async(
        self,
        tmp_req: buss_20220822_models.FindInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.FindInstanceInfoResponse:
        """
        @summary 反查资源
        
        @param tmp_req: FindInstanceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindInstanceInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.FindInstanceInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extras):
            request.extras_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extras, 'extras', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindInstanceInfo',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.FindInstanceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_instance_info(
        self,
        request: buss_20220822_models.FindInstanceInfoRequest,
    ) -> buss_20220822_models.FindInstanceInfoResponse:
        """
        @summary 反查资源
        
        @param request: FindInstanceInfoRequest
        @return: FindInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_instance_info_with_options(request, runtime)

    async def find_instance_info_async(
        self,
        request: buss_20220822_models.FindInstanceInfoRequest,
    ) -> buss_20220822_models.FindInstanceInfoResponse:
        """
        @summary 反查资源
        
        @param request: FindInstanceInfoRequest
        @return: FindInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_instance_info_with_options_async(request, runtime)

    def find_user_availble_resources_with_options(
        self,
        request: buss_20220822_models.FindUserAvailbleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.FindUserAvailbleResourcesResponse:
        """
        @summary 根据用户id查询对应产品下全部可用资产信息接口
        
        @param request: FindUserAvailbleResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindUserAvailbleResourcesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindUserAvailbleResources',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.FindUserAvailbleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_user_availble_resources_with_options_async(
        self,
        request: buss_20220822_models.FindUserAvailbleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.FindUserAvailbleResourcesResponse:
        """
        @summary 根据用户id查询对应产品下全部可用资产信息接口
        
        @param request: FindUserAvailbleResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindUserAvailbleResourcesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindUserAvailbleResources',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.FindUserAvailbleResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_user_availble_resources(
        self,
        request: buss_20220822_models.FindUserAvailbleResourcesRequest,
    ) -> buss_20220822_models.FindUserAvailbleResourcesResponse:
        """
        @summary 根据用户id查询对应产品下全部可用资产信息接口
        
        @param request: FindUserAvailbleResourcesRequest
        @return: FindUserAvailbleResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_user_availble_resources_with_options(request, runtime)

    async def find_user_availble_resources_async(
        self,
        request: buss_20220822_models.FindUserAvailbleResourcesRequest,
    ) -> buss_20220822_models.FindUserAvailbleResourcesResponse:
        """
        @summary 根据用户id查询对应产品下全部可用资产信息接口
        
        @param request: FindUserAvailbleResourcesRequest
        @return: FindUserAvailbleResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_user_availble_resources_with_options_async(request, runtime)

    def punish_resource_search_with_options(
        self,
        tmp_req: buss_20220822_models.PunishResourceSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.PunishResourceSearchResponse:
        """
        @summary 处罚资源搜索
        
        @param tmp_req: PunishResourceSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PunishResourceSearchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.PunishResourceSearchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_codes):
            request.action_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_codes, 'ActionCodes', 'json')
        if not UtilClient.is_unset(tmp_req.bussiness_codes):
            request.bussiness_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bussiness_codes, 'BussinessCodes', 'json')
        if not UtilClient.is_unset(tmp_req.source_codes):
            request.source_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_codes, 'SourceCodes', 'json')
        if not UtilClient.is_unset(tmp_req.user_ids):
            request.user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_ids, 'UserIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PunishResourceSearch',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.PunishResourceSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def punish_resource_search_with_options_async(
        self,
        tmp_req: buss_20220822_models.PunishResourceSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.PunishResourceSearchResponse:
        """
        @summary 处罚资源搜索
        
        @param tmp_req: PunishResourceSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PunishResourceSearchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.PunishResourceSearchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_codes):
            request.action_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_codes, 'ActionCodes', 'json')
        if not UtilClient.is_unset(tmp_req.bussiness_codes):
            request.bussiness_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bussiness_codes, 'BussinessCodes', 'json')
        if not UtilClient.is_unset(tmp_req.source_codes):
            request.source_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_codes, 'SourceCodes', 'json')
        if not UtilClient.is_unset(tmp_req.user_ids):
            request.user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_ids, 'UserIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PunishResourceSearch',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.PunishResourceSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def punish_resource_search(
        self,
        request: buss_20220822_models.PunishResourceSearchRequest,
    ) -> buss_20220822_models.PunishResourceSearchResponse:
        """
        @summary 处罚资源搜索
        
        @param request: PunishResourceSearchRequest
        @return: PunishResourceSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.punish_resource_search_with_options(request, runtime)

    async def punish_resource_search_async(
        self,
        request: buss_20220822_models.PunishResourceSearchRequest,
    ) -> buss_20220822_models.PunishResourceSearchResponse:
        """
        @summary 处罚资源搜索
        
        @param request: PunishResourceSearchRequest
        @return: PunishResourceSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.punish_resource_search_with_options_async(request, runtime)

    def risk_event_sync_with_options(
        self,
        request: buss_20220822_models.RiskEventSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.RiskEventSyncResponse:
        """
        @summary 风险事件同步
        
        @param request: RiskEventSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RiskEventSyncResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deleted):
            body['Deleted'] = request.deleted
        if not UtilClient.is_unset(request.discovery_time):
            body['DiscoveryTime'] = request.discovery_time
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_number):
            body['EventNumber'] = request.event_number
        if not UtilClient.is_unset(request.relevance_bu):
            body['RelevanceBu'] = request.relevance_bu
        if not UtilClient.is_unset(request.risk_detail):
            body['RiskDetail'] = request.risk_detail
        if not UtilClient.is_unset(request.risk_effect_type):
            body['RiskEffectType'] = request.risk_effect_type
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.risk_type):
            body['RiskType'] = request.risk_type
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.submitter):
            body['Submitter'] = request.submitter
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RiskEventSync',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.RiskEventSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def risk_event_sync_with_options_async(
        self,
        request: buss_20220822_models.RiskEventSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.RiskEventSyncResponse:
        """
        @summary 风险事件同步
        
        @param request: RiskEventSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RiskEventSyncResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deleted):
            body['Deleted'] = request.deleted
        if not UtilClient.is_unset(request.discovery_time):
            body['DiscoveryTime'] = request.discovery_time
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_number):
            body['EventNumber'] = request.event_number
        if not UtilClient.is_unset(request.relevance_bu):
            body['RelevanceBu'] = request.relevance_bu
        if not UtilClient.is_unset(request.risk_detail):
            body['RiskDetail'] = request.risk_detail
        if not UtilClient.is_unset(request.risk_effect_type):
            body['RiskEffectType'] = request.risk_effect_type
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.risk_type):
            body['RiskType'] = request.risk_type
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.submitter):
            body['Submitter'] = request.submitter
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RiskEventSync',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.RiskEventSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def risk_event_sync(
        self,
        request: buss_20220822_models.RiskEventSyncRequest,
    ) -> buss_20220822_models.RiskEventSyncResponse:
        """
        @summary 风险事件同步
        
        @param request: RiskEventSyncRequest
        @return: RiskEventSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.risk_event_sync_with_options(request, runtime)

    async def risk_event_sync_async(
        self,
        request: buss_20220822_models.RiskEventSyncRequest,
    ) -> buss_20220822_models.RiskEventSyncResponse:
        """
        @summary 风险事件同步
        
        @param request: RiskEventSyncRequest
        @return: RiskEventSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.risk_event_sync_with_options_async(request, runtime)

    def search_punish_events_with_options(
        self,
        tmp_req: buss_20220822_models.SearchPunishEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.SearchPunishEventsResponse:
        """
        @summary 管控事件查询
        
        @param tmp_req: SearchPunishEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchPunishEventsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.SearchPunishEventsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bussiness_codes):
            request.bussiness_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bussiness_codes, 'BussinessCodes', 'json')
        if not UtilClient.is_unset(tmp_req.case_codes):
            request.case_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_codes, 'CaseCodes', 'json')
        if not UtilClient.is_unset(tmp_req.event_codes):
            request.event_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_codes, 'EventCodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.bussiness_codes_shrink):
            query['BussinessCodes'] = request.bussiness_codes_shrink
        if not UtilClient.is_unset(request.case_codes_shrink):
            query['CaseCodes'] = request.case_codes_shrink
        if not UtilClient.is_unset(request.event_codes_shrink):
            query['EventCodes'] = request.event_codes_shrink
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPunishEvents',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.SearchPunishEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_punish_events_with_options_async(
        self,
        tmp_req: buss_20220822_models.SearchPunishEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.SearchPunishEventsResponse:
        """
        @summary 管控事件查询
        
        @param tmp_req: SearchPunishEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchPunishEventsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.SearchPunishEventsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bussiness_codes):
            request.bussiness_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bussiness_codes, 'BussinessCodes', 'json')
        if not UtilClient.is_unset(tmp_req.case_codes):
            request.case_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_codes, 'CaseCodes', 'json')
        if not UtilClient.is_unset(tmp_req.event_codes):
            request.event_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_codes, 'EventCodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.bussiness_codes_shrink):
            query['BussinessCodes'] = request.bussiness_codes_shrink
        if not UtilClient.is_unset(request.case_codes_shrink):
            query['CaseCodes'] = request.case_codes_shrink
        if not UtilClient.is_unset(request.event_codes_shrink):
            query['EventCodes'] = request.event_codes_shrink
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPunishEvents',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.SearchPunishEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_punish_events(
        self,
        request: buss_20220822_models.SearchPunishEventsRequest,
    ) -> buss_20220822_models.SearchPunishEventsResponse:
        """
        @summary 管控事件查询
        
        @param request: SearchPunishEventsRequest
        @return: SearchPunishEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_punish_events_with_options(request, runtime)

    async def search_punish_events_async(
        self,
        request: buss_20220822_models.SearchPunishEventsRequest,
    ) -> buss_20220822_models.SearchPunishEventsResponse:
        """
        @summary 管控事件查询
        
        @param request: SearchPunishEventsRequest
        @return: SearchPunishEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_punish_events_with_options_async(request, runtime)

    def search_punish_records_with_options(
        self,
        tmp_req: buss_20220822_models.SearchPunishRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.SearchPunishRecordsResponse:
        """
        @summary 管控事件查询
        
        @param tmp_req: SearchPunishRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchPunishRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.SearchPunishRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_codes):
            request.action_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_codes, 'ActionCodes', 'json')
        if not UtilClient.is_unset(tmp_req.case_codes):
            request.case_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_codes, 'CaseCodes', 'json')
        if not UtilClient.is_unset(tmp_req.event_codes):
            request.event_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_codes, 'EventCodes', 'json')
        if not UtilClient.is_unset(tmp_req.punish_status):
            request.punish_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.punish_status, 'PunishStatus', 'json')
        if not UtilClient.is_unset(tmp_req.source_codes):
            request.source_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_codes, 'SourceCodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_codes_shrink):
            query['ActionCodes'] = request.action_codes_shrink
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.bussiness_codes):
            query['BussinessCodes'] = request.bussiness_codes
        if not UtilClient.is_unset(request.case_codes_shrink):
            query['CaseCodes'] = request.case_codes_shrink
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes_shrink):
            query['EventCodes'] = request.event_codes_shrink
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.punish_status_shrink):
            query['PunishStatus'] = request.punish_status_shrink
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source_codes_shrink):
            query['SourceCodes'] = request.source_codes_shrink
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.url_fuzzy):
            query['UrlFuzzy'] = request.url_fuzzy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPunishRecords',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.SearchPunishRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_punish_records_with_options_async(
        self,
        tmp_req: buss_20220822_models.SearchPunishRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.SearchPunishRecordsResponse:
        """
        @summary 管控事件查询
        
        @param tmp_req: SearchPunishRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchPunishRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.SearchPunishRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_codes):
            request.action_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_codes, 'ActionCodes', 'json')
        if not UtilClient.is_unset(tmp_req.case_codes):
            request.case_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_codes, 'CaseCodes', 'json')
        if not UtilClient.is_unset(tmp_req.event_codes):
            request.event_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_codes, 'EventCodes', 'json')
        if not UtilClient.is_unset(tmp_req.punish_status):
            request.punish_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.punish_status, 'PunishStatus', 'json')
        if not UtilClient.is_unset(tmp_req.source_codes):
            request.source_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_codes, 'SourceCodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_codes_shrink):
            query['ActionCodes'] = request.action_codes_shrink
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.bussiness_codes):
            query['BussinessCodes'] = request.bussiness_codes
        if not UtilClient.is_unset(request.case_codes_shrink):
            query['CaseCodes'] = request.case_codes_shrink
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes_shrink):
            query['EventCodes'] = request.event_codes_shrink
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.punish_status_shrink):
            query['PunishStatus'] = request.punish_status_shrink
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.source_codes_shrink):
            query['SourceCodes'] = request.source_codes_shrink
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.url_fuzzy):
            query['UrlFuzzy'] = request.url_fuzzy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPunishRecords',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.SearchPunishRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_punish_records(
        self,
        request: buss_20220822_models.SearchPunishRecordsRequest,
    ) -> buss_20220822_models.SearchPunishRecordsResponse:
        """
        @summary 管控事件查询
        
        @param request: SearchPunishRecordsRequest
        @return: SearchPunishRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_punish_records_with_options(request, runtime)

    async def search_punish_records_async(
        self,
        request: buss_20220822_models.SearchPunishRecordsRequest,
    ) -> buss_20220822_models.SearchPunishRecordsResponse:
        """
        @summary 管控事件查询
        
        @param request: SearchPunishRecordsRequest
        @return: SearchPunishRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_punish_records_with_options_async(request, runtime)

    def search_punish_request_with_options(
        self,
        tmp_req: buss_20220822_models.SearchPunishRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.SearchPunishRequestResponse:
        """
        @summary 处罚记录查询
        
        @param tmp_req: SearchPunishRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchPunishRequestResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.SearchPunishRequestShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.anti_statuses):
            request.anti_statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.anti_statuses, 'AntiStatuses', 'json')
        if not UtilClient.is_unset(tmp_req.bussiness_codes):
            request.bussiness_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bussiness_codes, 'BussinessCodes', 'json')
        if not UtilClient.is_unset(tmp_req.event_codes):
            request.event_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_codes, 'EventCodes', 'json')
        if not UtilClient.is_unset(tmp_req.punish_statuses):
            request.punish_statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.punish_statuses, 'PunishStatuses', 'json')
        if not UtilClient.is_unset(tmp_req.source_codes):
            request.source_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_codes, 'SourceCodes', 'json')
        if not UtilClient.is_unset(tmp_req.user_ids):
            request.user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_ids, 'UserIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPunishRequest',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.SearchPunishRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_punish_request_with_options_async(
        self,
        tmp_req: buss_20220822_models.SearchPunishRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> buss_20220822_models.SearchPunishRequestResponse:
        """
        @summary 处罚记录查询
        
        @param tmp_req: SearchPunishRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchPunishRequestResponse
        """
        UtilClient.validate_model(tmp_req)
        request = buss_20220822_models.SearchPunishRequestShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.anti_statuses):
            request.anti_statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.anti_statuses, 'AntiStatuses', 'json')
        if not UtilClient.is_unset(tmp_req.bussiness_codes):
            request.bussiness_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bussiness_codes, 'BussinessCodes', 'json')
        if not UtilClient.is_unset(tmp_req.event_codes):
            request.event_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_codes, 'EventCodes', 'json')
        if not UtilClient.is_unset(tmp_req.punish_statuses):
            request.punish_statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.punish_statuses, 'PunishStatuses', 'json')
        if not UtilClient.is_unset(tmp_req.source_codes):
            request.source_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_codes, 'SourceCodes', 'json')
        if not UtilClient.is_unset(tmp_req.user_ids):
            request.user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_ids, 'UserIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPunishRequest',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            buss_20220822_models.SearchPunishRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_punish_request(
        self,
        request: buss_20220822_models.SearchPunishRequestRequest,
    ) -> buss_20220822_models.SearchPunishRequestResponse:
        """
        @summary 处罚记录查询
        
        @param request: SearchPunishRequestRequest
        @return: SearchPunishRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_punish_request_with_options(request, runtime)

    async def search_punish_request_async(
        self,
        request: buss_20220822_models.SearchPunishRequestRequest,
    ) -> buss_20220822_models.SearchPunishRequestResponse:
        """
        @summary 处罚记录查询
        
        @param request: SearchPunishRequestRequest
        @return: SearchPunishRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_punish_request_with_options_async(request, runtime)
