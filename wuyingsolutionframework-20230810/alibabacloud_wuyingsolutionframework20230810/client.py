# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_wuyingsolutionframework20230810 import models as wuying_solution_framework_20230810_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('wuyingsolutionframework', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def send_ops_message_to_terminal_with_options(
        self,
        request: wuying_solution_framework_20230810_models.SendOpsMessageToTerminalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_solution_framework_20230810_models.SendOpsMessageToTerminalResponse:
        """
        @summary 发送运维消息
        
        @param request: SendOpsMessageToTerminalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendOpsMessageToTerminalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.message_body):
            query['MessageBody'] = request.message_body
        if not UtilClient.is_unset(request.office_region_id):
            query['OfficeRegionId'] = request.office_region_id
        if not UtilClient.is_unset(request.ops_action):
            query['OpsAction'] = request.ops_action
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.wait_for_ack):
            query['WaitForAck'] = request.wait_for_ack
        if not UtilClient.is_unset(request.wait_for_msg):
            query['WaitForMsg'] = request.wait_for_msg
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendOpsMessageToTerminal',
            version='2023-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_solution_framework_20230810_models.SendOpsMessageToTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_ops_message_to_terminal_with_options_async(
        self,
        request: wuying_solution_framework_20230810_models.SendOpsMessageToTerminalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wuying_solution_framework_20230810_models.SendOpsMessageToTerminalResponse:
        """
        @summary 发送运维消息
        
        @param request: SendOpsMessageToTerminalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendOpsMessageToTerminalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.message_body):
            query['MessageBody'] = request.message_body
        if not UtilClient.is_unset(request.office_region_id):
            query['OfficeRegionId'] = request.office_region_id
        if not UtilClient.is_unset(request.ops_action):
            query['OpsAction'] = request.ops_action
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.wait_for_ack):
            query['WaitForAck'] = request.wait_for_ack
        if not UtilClient.is_unset(request.wait_for_msg):
            query['WaitForMsg'] = request.wait_for_msg
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendOpsMessageToTerminal',
            version='2023-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wuying_solution_framework_20230810_models.SendOpsMessageToTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_ops_message_to_terminal(
        self,
        request: wuying_solution_framework_20230810_models.SendOpsMessageToTerminalRequest,
    ) -> wuying_solution_framework_20230810_models.SendOpsMessageToTerminalResponse:
        """
        @summary 发送运维消息
        
        @param request: SendOpsMessageToTerminalRequest
        @return: SendOpsMessageToTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_ops_message_to_terminal_with_options(request, runtime)

    async def send_ops_message_to_terminal_async(
        self,
        request: wuying_solution_framework_20230810_models.SendOpsMessageToTerminalRequest,
    ) -> wuying_solution_framework_20230810_models.SendOpsMessageToTerminalResponse:
        """
        @summary 发送运维消息
        
        @param request: SendOpsMessageToTerminalRequest
        @return: SendOpsMessageToTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_ops_message_to_terminal_with_options_async(request, runtime)
