# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cms20240330 import models as cms_20240330_models
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
        self._endpoint = self.get_endpoint('cms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_alert_actions_with_options(
        self,
        tmp_req: cms_20240330_models.ListAlertActionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary 查询告警动作
        
        @param tmp_req: ListAlertActionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertActionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListAlertActionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_action_ids):
            request.alert_action_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_action_ids, 'alertActionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_action_ids_shrink):
            query['alertActionIds'] = request.alert_action_ids_shrink
        if not UtilClient.is_unset(request.alert_action_name):
            query['alertActionName'] = request.alert_action_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertActions',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/alertActions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAlertActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_actions_with_options_async(
        self,
        tmp_req: cms_20240330_models.ListAlertActionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary 查询告警动作
        
        @param tmp_req: ListAlertActionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertActionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListAlertActionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_action_ids):
            request.alert_action_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_action_ids, 'alertActionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_action_ids_shrink):
            query['alertActionIds'] = request.alert_action_ids_shrink
        if not UtilClient.is_unset(request.alert_action_name):
            query['alertActionName'] = request.alert_action_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertActions',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/alertActions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAlertActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_actions(
        self,
        request: cms_20240330_models.ListAlertActionsRequest,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary 查询告警动作
        
        @param request: ListAlertActionsRequest
        @return: ListAlertActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alert_actions_with_options(request, headers, runtime)

    async def list_alert_actions_async(
        self,
        request: cms_20240330_models.ListAlertActionsRequest,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary 查询告警动作
        
        @param request: ListAlertActionsRequest
        @return: ListAlertActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alert_actions_with_options_async(request, headers, runtime)
