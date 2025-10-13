# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_metaspace20221014 import models as metaspace_20221014_models
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
        self._endpoint = self.get_endpoint('metaspace', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_coordination_for_coordinator_with_options(
        self,
        request: metaspace_20221014_models.ApplyCoordinationForCoordinatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20221014_models.ApplyCoordinationForCoordinatorResponse:
        """
        @summary 协同者发起流协同请求并获取协同ticket的API接口。
        
        @description ## 请求说明
        - 该API为内部使用，主要用于协同者发起流协同。
        - `DependOnMainStream`参数指定了是否依赖主流的状态来建立或断开协同流。
        - 当`InitiatorType`设置为强制协同类型时（如`ADMIN_INITIATE_FORCE`或`COORDINATOR_INITIATE_FORCE`），将返回一个`CoordinateTicket`。
        - 协同资源列表`CoordinationResourceCandidates`中必须包含至少一项资源信息，并且所有提供的资源ID、类型和地区等信息需准确无误。
        - 确保`OwnerAliUid`与协同者的租户ID相同，否则可能无法成功发起协同请求。
        - 对于AD用户，请务必填写`AdDomainName`字段。
        
        @param request: ApplyCoordinationForCoordinatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyCoordinationForCoordinatorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.coordination_resource_candidates):
            body_flat['CoordinationResourceCandidates'] = request.coordination_resource_candidates
        if not UtilClient.is_unset(request.initiator_type):
            body['InitiatorType'] = request.initiator_type
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyCoordinationForCoordinator',
            version='2022-10-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20221014_models.ApplyCoordinationForCoordinatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_coordination_for_coordinator_with_options_async(
        self,
        request: metaspace_20221014_models.ApplyCoordinationForCoordinatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20221014_models.ApplyCoordinationForCoordinatorResponse:
        """
        @summary 协同者发起流协同请求并获取协同ticket的API接口。
        
        @description ## 请求说明
        - 该API为内部使用，主要用于协同者发起流协同。
        - `DependOnMainStream`参数指定了是否依赖主流的状态来建立或断开协同流。
        - 当`InitiatorType`设置为强制协同类型时（如`ADMIN_INITIATE_FORCE`或`COORDINATOR_INITIATE_FORCE`），将返回一个`CoordinateTicket`。
        - 协同资源列表`CoordinationResourceCandidates`中必须包含至少一项资源信息，并且所有提供的资源ID、类型和地区等信息需准确无误。
        - 确保`OwnerAliUid`与协同者的租户ID相同，否则可能无法成功发起协同请求。
        - 对于AD用户，请务必填写`AdDomainName`字段。
        
        @param request: ApplyCoordinationForCoordinatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyCoordinationForCoordinatorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.coordination_resource_candidates):
            body_flat['CoordinationResourceCandidates'] = request.coordination_resource_candidates
        if not UtilClient.is_unset(request.initiator_type):
            body['InitiatorType'] = request.initiator_type
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyCoordinationForCoordinator',
            version='2022-10-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20221014_models.ApplyCoordinationForCoordinatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_coordination_for_coordinator(
        self,
        request: metaspace_20221014_models.ApplyCoordinationForCoordinatorRequest,
    ) -> metaspace_20221014_models.ApplyCoordinationForCoordinatorResponse:
        """
        @summary 协同者发起流协同请求并获取协同ticket的API接口。
        
        @description ## 请求说明
        - 该API为内部使用，主要用于协同者发起流协同。
        - `DependOnMainStream`参数指定了是否依赖主流的状态来建立或断开协同流。
        - 当`InitiatorType`设置为强制协同类型时（如`ADMIN_INITIATE_FORCE`或`COORDINATOR_INITIATE_FORCE`），将返回一个`CoordinateTicket`。
        - 协同资源列表`CoordinationResourceCandidates`中必须包含至少一项资源信息，并且所有提供的资源ID、类型和地区等信息需准确无误。
        - 确保`OwnerAliUid`与协同者的租户ID相同，否则可能无法成功发起协同请求。
        - 对于AD用户，请务必填写`AdDomainName`字段。
        
        @param request: ApplyCoordinationForCoordinatorRequest
        @return: ApplyCoordinationForCoordinatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_coordination_for_coordinator_with_options(request, runtime)

    async def apply_coordination_for_coordinator_async(
        self,
        request: metaspace_20221014_models.ApplyCoordinationForCoordinatorRequest,
    ) -> metaspace_20221014_models.ApplyCoordinationForCoordinatorResponse:
        """
        @summary 协同者发起流协同请求并获取协同ticket的API接口。
        
        @description ## 请求说明
        - 该API为内部使用，主要用于协同者发起流协同。
        - `DependOnMainStream`参数指定了是否依赖主流的状态来建立或断开协同流。
        - 当`InitiatorType`设置为强制协同类型时（如`ADMIN_INITIATE_FORCE`或`COORDINATOR_INITIATE_FORCE`），将返回一个`CoordinateTicket`。
        - 协同资源列表`CoordinationResourceCandidates`中必须包含至少一项资源信息，并且所有提供的资源ID、类型和地区等信息需准确无误。
        - 确保`OwnerAliUid`与协同者的租户ID相同，否则可能无法成功发起协同请求。
        - 对于AD用户，请务必填写`AdDomainName`字段。
        
        @param request: ApplyCoordinationForCoordinatorRequest
        @return: ApplyCoordinationForCoordinatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_coordination_for_coordinator_with_options_async(request, runtime)

    def cancel_coordination_with_options(
        self,
        request: metaspace_20221014_models.CancelCoordinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20221014_models.CancelCoordinationResponse:
        """
        @summary 取消协同请求
        
        @param request: CancelCoordinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelCoordinationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.co_ids):
            body_flat['CoIds'] = request.co_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelCoordination',
            version='2022-10-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20221014_models.CancelCoordinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_coordination_with_options_async(
        self,
        request: metaspace_20221014_models.CancelCoordinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20221014_models.CancelCoordinationResponse:
        """
        @summary 取消协同请求
        
        @param request: CancelCoordinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelCoordinationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.co_ids):
            body_flat['CoIds'] = request.co_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelCoordination',
            version='2022-10-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20221014_models.CancelCoordinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_coordination(
        self,
        request: metaspace_20221014_models.CancelCoordinationRequest,
    ) -> metaspace_20221014_models.CancelCoordinationResponse:
        """
        @summary 取消协同请求
        
        @param request: CancelCoordinationRequest
        @return: CancelCoordinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_coordination_with_options(request, runtime)

    async def cancel_coordination_async(
        self,
        request: metaspace_20221014_models.CancelCoordinationRequest,
    ) -> metaspace_20221014_models.CancelCoordinationResponse:
        """
        @summary 取消协同请求
        
        @param request: CancelCoordinationRequest
        @return: CancelCoordinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_coordination_with_options_async(request, runtime)

    def get_coordination_ticket_with_options(
        self,
        request: metaspace_20221014_models.GetCoordinationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20221014_models.GetCoordinationTicketResponse:
        """
        @summary 获取协同流连接ticket
        
        @param request: GetCoordinationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCoordinationTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.co_id):
            body['CoId'] = request.co_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCoordinationTicket',
            version='2022-10-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20221014_models.GetCoordinationTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_coordination_ticket_with_options_async(
        self,
        request: metaspace_20221014_models.GetCoordinationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> metaspace_20221014_models.GetCoordinationTicketResponse:
        """
        @summary 获取协同流连接ticket
        
        @param request: GetCoordinationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCoordinationTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.co_id):
            body['CoId'] = request.co_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCoordinationTicket',
            version='2022-10-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            metaspace_20221014_models.GetCoordinationTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_coordination_ticket(
        self,
        request: metaspace_20221014_models.GetCoordinationTicketRequest,
    ) -> metaspace_20221014_models.GetCoordinationTicketResponse:
        """
        @summary 获取协同流连接ticket
        
        @param request: GetCoordinationTicketRequest
        @return: GetCoordinationTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_coordination_ticket_with_options(request, runtime)

    async def get_coordination_ticket_async(
        self,
        request: metaspace_20221014_models.GetCoordinationTicketRequest,
    ) -> metaspace_20221014_models.GetCoordinationTicketResponse:
        """
        @summary 获取协同流连接ticket
        
        @param request: GetCoordinationTicketRequest
        @return: GetCoordinationTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_coordination_ticket_with_options_async(request, runtime)
